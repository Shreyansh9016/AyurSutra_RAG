<h1 align="center">🧠 Panchakarma Decision Support System</h1>

<p align="center">
An evidence-based clinical decision support application for Panchakarma therapy<br>
using Retrieval-Augmented Generation (RAG) over classical Ayurveda texts.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>Evidence-based recommendations using classical Ayurveda sources</li>
  <li>Retrieval-Augmented Generation (RAG) architecture</li>
  <li>FAISS vector database for semantic search</li>
  <li>Groq LLM integration for fast inference</li>
  <li>Explainable outputs with supporting passages</li>
  <li>Streamlit web interface</li>
</ul>

<hr>

<h2>🧑‍⚕️ How to Use the Application</h2>
<ol>
  <li>Enter patient information:
    <ul>
      <li>Age</li>
      <li>Gender</li>
      <li>Prakriti (Vata / Pitta / Kapha)</li>
      <li>Medical history</li>
      <li>Symptoms</li>
    </ul>
  </li>
  <li>Click <b>Submit</b></li>
  <li>Review recommendations and supporting evidence</li>
</ol>

<hr>

<h1>💻 Running the Application LOCALLY</h1>

<h2>🔧 Prerequisites</h2>
<ul>
  <li>Python 3.10 or later</li>
  <li>Git installed</li>
  <li>An API key from <a href="https://console.groq.com/">Groq Cloud</a></li>
</ul>

<hr>

<h2>1️⃣ Clone the Repository</h2>
<pre><code>git clone https://github.com/VashuJain2024/AyurSutra_RAG
cd AyurSutra_RAG</code></pre>

<hr>

<h2>2️⃣ Create and Activate Virtual Environment</h2>

<p><b>Windows (PowerShell)</b></p>
<pre><code>python -m venv rag_env
.\rag_env\Scripts\Activate.ps1</code></pre>

<p><b>macOS / Linux</b></p>
<pre><code>python3 -m venv rag_env
source rag_env/bin/activate</code></pre>

<hr>

<h2>3️⃣ Install Dependencies</h2>
<pre><code>pip install -r requirements.txt</code></pre>

<hr>

<h2>4️⃣ Configure Environment Variables</h2>
<p>Create a <code>.env</code> file in the project root and add your Groq API key:</p>
<pre><code>GROQ_API_KEY=your_api_key_here</code></pre>

<hr>

<h2>5️⃣ Run the Application</h2>

<h3>Option A: Streamlit UI (Recommended for Users)</h3>
<pre><code>streamlit run app.py</code></pre>

<h3>Option B: FastAPI Backend (For Developers)</h3>
<pre><code>python api.py</code></pre>
<p>Once running, you can access the API documentation at <code>http://127.0.0.1:8000/docs</code> or check the health status at <code>http://127.0.0.1:8000/health</code>.</p>

<hr>

<h2>📁 Project Structure</h2>

<pre><code>AyurSutra_RAG/
│
├── app.py                # Streamlit Frontend
├── api.py                # FastAPI Backend
├── build_db.py           # Script to process PDFs and build vector DB
├── rag_pipeline.py       # Core RAG logic and LLM integration
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (created manually)
├── .gitignore            # Git ignore rules
│
├── data/                 # Source medical texts (PDFs)
│   └── classical/
│
└── vector_db/            # Generated FAISS vector database
</code></pre>

<hr>

<h2>⚠️ Disclaimer</h2>

<p>
This system is for <b>educational purposes only</b>.
</p>

<p>
<b>It is NOT a substitute for professional medical advice, diagnosis, or treatment.</b>
</p>

<p>
Always consult a qualified healthcare professional.
</p>

<hr>

<p align="center">✨ Built with RAG + AI for Healthcare Innovation ✨</p>
