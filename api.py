from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from rag_pipeline import load_db, generate_answer, answer_general_query
import os
from dotenv import load_dotenv
import traceback

# -------------------------
# LOAD ENV VARIABLES
# -------------------------
load_dotenv()

# -------------------------
# INITIALIZE APP
# -------------------------
app = FastAPI(title="AyurSutra RAG API")

# -------------------------
# CORS CONFIG (for React)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# CONSTANTS
# -------------------------
DB_PATH = "vector_db/classical_db"

# -------------------------
# GLOBAL DB VARIABLE
# -------------------------
db = None

# -------------------------
# STARTUP EVENT
# -------------------------
@app.on_event("startup")
async def startup_event():
    global db

    if not os.path.exists(DB_PATH):
        raise RuntimeError("❌ Vector DB not found. Please build it first.")

    try:
        db = load_db(DB_PATH)
        print("✅ Vector database loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load database: {e}")
        traceback.print_exc()
        raise e


# -------------------------
# ROOT ROUTE
# -------------------------
@app.get("/")
def root():
    return {"message": "AyurSutra API running 🚀"}


# -------------------------
# HEALTH CHECK
# -------------------------
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database_loaded": db is not None
    }


# -------------------------
# REQUEST MODELS
# -------------------------
class CaseQuery(BaseModel):
    age: int
    gender: str
    prakriti: str
    symptoms: str
    history: str = ""


class GeneralQuery(BaseModel):
    query: str


# -------------------------
# ANALYZE PATIENT CASE
# -------------------------
@app.post("/analyze")
async def analyze_case(data: CaseQuery):
    if db is None:
        raise HTTPException(status_code=500, detail="Database not loaded")

    query_text = (
        f"Age: {data.age}\n"
        f"Gender: {data.gender}\n"
        f"Prakriti: {data.prakriti}\n"
        f"Symptoms: {data.symptoms}\n"
        f"History: {data.history}"
    )

    try:
        answer, docs = generate_answer(query_text, db)

        sources = [
            {
                "source": doc.metadata.get("source", "Unknown"),
                "preview": doc.page_content[:200]
            }
            for doc in docs
        ]

        return {
            "answer": answer,
            "sources": sources
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")


# -------------------------
# GENERAL QUERY ENDPOINT
# -------------------------
@app.post("/query")
async def general_query(data: GeneralQuery):
    if db is None:
        raise HTTPException(status_code=500, detail="Database not loaded")

    try:
        answer, docs = answer_general_query(data.query, db)

        sources = [
            {
                "source": doc.metadata.get("source", "Unknown"),
                "preview": doc.page_content[:200]
            }
            for doc in docs
        ]

        return {
            "answer": answer,
            "sources": sources
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")


# -------------------------
# RUN SERVER (LOCAL ONLY)
# -------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
