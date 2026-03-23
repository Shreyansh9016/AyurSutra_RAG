from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from rag_pipeline import load_db, generate_answer, answer_general_query
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(title="AyurSutra RAG API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your specific website URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Constants
DB_PATH = "vector_db/classical_db"

# Global variable to store loaded DB
db = None

@app.on_event("startup")
async def startup_event():
    global db
    if not os.path.exists(DB_PATH):
        # In a real API, we might want to trigger build_db here or ensure it's pre-built
        # For simplicity, we assume it's built or being handled
        pass
    
    try:
        db = load_db(DB_PATH)
        print("✅ Vector database loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load database: {e}")

class CaseQuery(BaseModel):
    age: int
    gender: str
    prakriti: str
    symptoms: str
    history: str = ""

class GeneralQuery(BaseModel):
    query: str

@app.post("/analyze")
async def analyze_case(data: CaseQuery):
    if db is None:
        raise HTTPException(status_code=500, detail="Database not loaded")
    
    query_text = f"Age: {data.age}\nGender: {data.gender}\nPrakriti: {data.prakriti}\nSymptoms: {data.symptoms}\nHistory: {data.history}"
    
    try:
        answer, docs = generate_answer(query_text, db)
        sources = [{"source": doc.metadata.get("source", "Unknown"), "content": doc.page_content[:500]} for doc in docs]
        return {"answer": answer, "sources": sources}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
async def general_query(data: GeneralQuery):
    if db is None:
        raise HTTPException(status_code=500, detail="Database not loaded")
    
    try:
        answer, docs = answer_general_query(data.query, db)
        sources = [{"source": doc.metadata.get("source", "Unknown"), "content": doc.page_content[:500]} for doc in docs]
        return {"answer": answer, "sources": sources}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database_loaded": db is not None}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
