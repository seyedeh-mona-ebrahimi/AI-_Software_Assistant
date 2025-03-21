             
# AI Software Engineering Assistant 
### How Can AI Stay Up to Date Without Constant Retraining


# Overview
AI-powered Software Engineering Meeting Assistant is designed to keep developers, architects, and DevOps teams informed about the latest programming languages, software architectures, and DevOps practices. Instead of requiring constant retraining, it retrieves real-time updates from trusted sources like ArXiv, GitHub, Stack Overflow, and RFCs, dynamically modifies responses based on new releases, and ensures consistency in recommendations. This project focuses on implementing a retrieval-augmented generation (RAG) approach, trust-based ranking, and consistency checking to ensure AI-generated responses remain relevant and aligned with industry best practices.


# Project Structure & Workflow
## Flow of Python Files

1. AImodel.py → Initializes and loads the model.
2. arxiv_fetcher.py → Fetches the latest knowledge.
3. retrieval.py → Stores the fetched knowledge in the database for later use.
4. ranking.py → Ranks the retrieved documents based on trustworthiness and relevance.
5. consistency.py → Ensures the AI responses remain consistent with previously generated answers.
6. app.py → The Streamlit UI, allows users to interact with the assistant.


## Installation Instructions

## Step 1: Set Up a Virtual Environment
To avoid dependency conflicts, create and activate a Conda environment:
1. conda create -n capstone_env python=3.10
2. conda activate capstone_env

Install PyTorch and related dependencies: 
1. conda install pytorch torchvision torchaudio

## Step 2: Install Required Python Libraries
Once inside the virtual environment, install the required dependencies:

1. pip install streamlit
2. pip install torch transformers peft trl accelerate chromadb faiss-cpu sentence-transformers langchain rank_bm25 -U langchain-community
3. pip install python-dotenv
4. pip install wandb
5. pip install ipywidgets
6. pip install speechrecognition pydub pillow pytesseract pyaudio
7. pip install beautifulsoup4

## Step 3: Special Installation for macOS Users (PyAudio)
If you are using macOS, you may need to install pyaudio using Homebrew:

### 1. Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

### 2. Add Homebrew to your PATH
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/xbtash/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

### 3. Install PortAudio (required for PyAudio)
brew install portaudio

### 4. Install PyAudio
pip install pyaudio


## Step 4: Running the Application
Once all dependencies are installed, run the Streamlit UI using:

1. streamlit run app.py

This will launch the AI-powered assistant in your browser, allowing you to input queries and receive real-time, up-to-date responses.





