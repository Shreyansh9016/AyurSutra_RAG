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
</ul>

<hr>

<h2>1️⃣ Clone the Repository</h2>
<pre><code>git clone https://github.com/Shreyansh9016/AyurSutra_RAG/
cd AyurSutra_RAG</code></pre>

<hr>

<h2>2️⃣ Create Virtual Environment</h2>

<p><b>Windows (CMD)</b></p>
<pre><code>python -m venv rag_env</code></pre>

<p><b>macOS / Linux</b></p>
<pre><code>python3 -m venv rag_env</code></pre>

<hr>

<h2>3️⃣ Activate Virtual Environment</h2>

<p><b>Windows (CMD)</b></p>
<pre><code>rag_env\Scripts\activate</code></pre>

<p><b>Windows (PowerShell)</b></p>
<pre><code>rag_env\Scripts\Activate.ps1</code></pre>

<p><b>macOS / Linux</b></p>
<pre><code>source rag_env/bin/activate</code></pre>

<p>After activation, you should see:</p>
<pre><code>(rag_env)</code></pre>

<hr>

<h2>4️⃣ Install Dependencies</h2>
<pre><code>pip install -r requirements.txt</code></pre>

<hr>

<h2>5️⃣ Add Groq API Key</h2>
<p>Create a <code>.env</code> file in the project root:</p>

<pre><code>GROQ_API_KEY=your_api_key_here</code></pre>

<hr>

<h2>6️⃣ Run the Application</h2>
<pre><code>streamlit run app.py</code></pre>

<p>The application will open in your browser.</p>

<h3>⚠️ Notes</h3>
<ul>
  <li>Vector database builds automatically from PDFs</li>
  <li>First run may take several minutes</li>
  <li>Subsequent runs are faster</li>
</ul>

<hr>

<h1>☁️ Running ONLINE (Streamlit Cloud)</h1>

<h2>1️⃣ Open App Link</h2>
<p>Open the deployed application URL.</p>

<h2>2️⃣ Add API Key in Secrets</h2>
<p>Go to:</p>
<p><b>App → Settings → Secrets</b></p>

<pre><code>GROQ_API_KEY = "your_api_key_here"</code></pre>

<h2>3️⃣ Start the Application</h2>
<ul>
  <li>App may be asleep due to inactivity</li>
  <li>Click "Wake Up" if prompted</li>
</ul>

<h3>⏳ Initial Loading Time</h3>
<ul>
  <li>First startup: 1–3 minutes</li>
  <li>Embeddings + DB initialization happens here</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre><code>Panchakarma-Decision-Support/
│
├── app.py
├── build_db.py
├── rag_pipeline.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
│   └── classical/
│
└── vector_db/
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
