<h1 align="center">🚀 AyurSutra RAG API Deployment Guide</h1>

<p align="center">
FastAPI + RAG + ngrok (Free Deployment for Students)
</p>

<hr>

<h2>📌 Overview</h2>

<p>
This guide explains how to run and expose your FastAPI-based RAG system publicly 
using your local machine and ngrok — without any cloud or credit card.
</p>

<pre>
Laptop (FastAPI + RAG)
        ↓
ngrok (Public Tunnel)
        ↓
Internet 🌍
</pre>

<ul>
  <li>✅ 100% Free</li>
  <li>✅ No credit card required</li>
  <li>✅ Perfect for demos & projects</li>
</ul>

<hr>

<h2>🧰 Prerequisites</h2>

<ul>
  <li>Python 3.8+</li>
  <li>FastAPI project (api.py)</li>
  <li>Virtual environment (recommended)</li>
</ul>

<hr>

<h2>⚙️ Step 1: Setup Virtual Environment</h2>

<pre>
cd "D:\Agentic AI\AyurSutra_RAG"
python -m venv ragenv
ragenv\Scripts\activate
</pre>

<hr>

<h2>📦 Step 2: Install Dependencies</h2>

<pre>
pip install -r requirements.txt
</pre>

<p><i>This installs FastAPI, uvicorn, dotenv, and all required libraries.</i></p>

<hr>

<h2>▶️ Step 3: Start FastAPI Server</h2>

<pre>
uvicorn api:app --reload
</pre>

<p><b>Test locally:</b></p>

<pre>
http://localhost:8000/docs
</pre>

<p><i>Ensure your API works locally before proceeding.</i></p>

<hr>

<h2>🌐 Step 4: Create ngrok Account</h2>

<ol>
  <li>Go to <a href="https://ngrok.com/" target="_blank">https://ngrok.com/</a></li>
  <li>Sign up (Google login supported)</li>
  <li>Copy your Auth Token</li>
</ol>

<hr>

<h2>⬇️ Step 5: Download ngrok</h2>

<ol>
  <li>Download from <a href="https://ngrok.com/download" target="_blank">https://ngrok.com/download</a></li>
  <li>Extract <code>ngrok.exe</code></li>
  <li>Place it in <code>C:\ngrok</code> (or any folder)</li>
</ol>

<hr>

<h2>🔑 Step 6: Configure ngrok (One-Time Setup)</h2>

<pre>
ngrok config add-authtoken YOUR_AUTH_TOKEN
</pre>

<p><i>Run this command once after installation.</i></p>

<hr>

<h2>🚀 Step 7: Start ngrok Tunnel</h2>

<p><b>Open a NEW terminal (keep FastAPI running in first terminal)</b></p>

<pre>
cd C:\ngrok
ngrok http 8000
</pre>

<p><b>Output:</b></p>

<pre>
https://abc123.ngrok-free.app → http://localhost:8000
</pre>

<hr>

<h2>⚙️ ngrok Notes</h2>

<ul>
  <li>No additional commands required after starting ngrok</li>
  <li>Simply copy the HTTPS URL and use it</li>
  <li>If issues occur, try:</li>
</ul>

<pre>
ngrok http 8000 --host-header=localhost
</pre>

<hr>

<h2>🌍 Step 8: Access Public API</h2>

<ul>
  <li><b>Swagger UI:</b><br> https://abc123.ngrok-free.app/docs</li>
  <li><b>Health:</b><br> https://abc123.ngrok-free.app/health</li>
  <li><b>Query:</b><br> https://abc123.ngrok-free.app/query</li>
</ul>

<hr>

<h2>🧪 Example Request</h2>

<pre>
POST /query

{
  "query": "Panchakarma"
}
</pre>

<hr>

<h2>🖥️ Required Terminals</h2>

<table border="1" cellpadding="8" cellspacing="0">
<tr>
  <th>Terminal</th>
  <th>Purpose</th>
</tr>
<tr>
  <td>1</td>
  <td>Run FastAPI (uvicorn)</td>
</tr>
<tr>
  <td>2</td>
  <td>Run ngrok tunnel</td>
</tr>
</table>

<hr>

<h2>⚠️ Important Notes</h2>

<ul>
  <li>Keep both terminals running</li>
  <li>ngrok URL changes on every restart (free version)</li>
  <li>Your laptop must stay ON</li>
  <li>Allow Python in firewall if prompted</li>
</ul>

<hr>

<h2>🔍 Local vs Public Access</h2>

<table border="1" cellpadding="8" cellspacing="0">
<tr>
  <th>URL</th>
  <th>Access</th>
</tr>
<tr>
  <td>localhost:8000</td>
  <td>Only your laptop</td>
</tr>
<tr>
  <td>ngrok URL</td>
  <td>Global 🌍</td>
</tr>
</table>

<hr>

<h2>🎯 Conclusion</h2>

<ul>
  <li>✔ Fully working RAG API</li>
  <li>✔ Public deployment without cloud</li>
  <li>✔ Ideal for demos, hackathons, and interviews</li>
</ul>

<p align="center"><b>✨ Zero-cost AI deployment achieved!</b></p>

<hr>
