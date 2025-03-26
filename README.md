# 🤖 AI Software Engineering Assistant
### *"How Can AI Stay Up to Date Without Constant Retraining?"*

---

## 🧭 Overview
The **AI Software Engineering Assistant** is a real-time, adaptive assistant that helps developers, architects, and DevOps teams stay updated with:
- 🔧 New frameworks & tools
- 📐 Evolving software architectures
- ⚙️ DevOps best practices

Rather than requiring constant retraining, it uses:
- 🔍 Retrieval-Augmented Generation (RAG)
- 🎯 Trust-based document ranking
- ✅ Response consistency checking

It dynamically pulls from sources like:
- ArXiv
- GitHub
- Stack Overflow
- RFCs
- Hacker News
- Dev.to
- Reddit
- Medium
- Google Scholar

---

## 🧱 Project Structure

```plaintext
📦 Project Modules
│
├── 🧠 AImodel.py         → Loads model + generates structured answers
├── 🌐 fetcher.py         → Fetches real-time data from online sources
├── 🧠 retrieval.py       → Embeds + stores documents using ChromaDB
├── 🎯 ranking.py         → Ranks retrieved docs by trust & relevance
├── 🔍 consistency.py     → Validates output against previous answers
├── 🖼️  app.py             → Streamlit UI (text, speech, image input)
```

---

## ⚙️ Installation Guide

### ✅ Step 1: Create & Activate Environment
```bash
conda create -n capstone_env python=3.10
conda activate capstone_env
```

Install PyTorch:
```bash
conda install pytorch torchvision torchaudio
```

---

### ✅ Step 2: Install Python Packages
```bash
pip install streamlit torch transformers peft trl accelerate chromadb faiss-cpu sentence-transformers langchain rank_bm25 -U langchain-community
pip install python-dotenv wandb ipywidgets
pip install speechrecognition pydub pillow pytesseract pyaudio
pip install beautifulsoup4
```

---

### 🍏 Step 3: For macOS Users (PyAudio)
```bash
# Install Homebrew (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to PATH
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile

# Install PortAudio
brew install portaudio

# Install PyAudio
pip install pyaudio
```

---

### ▶️ Step 4: Run the Assistant
```bash
streamlit run app.py
```
Your browser will open the assistant where you can enter a query, speak it, or upload an image for OCR.

---

## 🧠 Features

✅ Always Up-to-date via real-time retrieval  
✅ No need for retraining  
✅ Supports speech & image input  
✅ Response validation via semantic similarity  
✅ Uses open-source LLMs (like CodeLlama/Mistral)

---

## 👩‍💻 Contributors
- [@tanvicat](https://github.com/tanvicat)
- [@seyedeh-mona-ebrahimi](https://github.com/seyedeh-mona-ebrahimi)

---

## 📄 License
MIT License

---

## 🌍 Links & Resources
- 🔗 [LangChain](https://www.langchain.com/)
- 🔗 [ChromaDB](https://www.trychroma.com/)
- 🔗 [HuggingFace](https://huggingface.co/)
- 🔗 [Streamlit](https://streamlit.io/)

> "In a world where code evolves weekly, your assistant should too."

