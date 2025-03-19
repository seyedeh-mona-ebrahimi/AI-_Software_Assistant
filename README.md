#### GROUP 4: AIMonvi

### Team members:    Seyedeh (Mona) Ebrahimi, Tanvi Sharma
### Project's Mentor: Ayman                      
### PROJECT 4: How Can AI Stay Up to Date Without Constant Retraining


#### For the app.py to run, please install the below dependencies

## First create a virtual environment
1. conda create -n capstone_env python=3.10
2. conda activate capstone_env
3. conda install pytorch torchvision torchaudio
 
## Then install the following 
1. pip install streamlit
2. pip install torch transformers peft trl accelerate chromadb faiss-cpu sentence-transformers langchain rank_bm25 -U langchain-community
3. pip install dotenv
4. pip install wandb
5. pip install ipybwidgets
6. pip install speechrecognition pydub pillow pytesseract pyaudio
7. pip install bs4

## To install pyaudio on mac

1. Install Homebrew if not installed: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. Run these commands in your terminal to add Homebrew to your PATH:
    echo >> /Users/xbtash/.zprofile
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/xbtash/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"

3. brew install portaudio
4. pip install pyaudio



## The flow of the python files

1. AImodel.py → Initializes and loads the model.
2. arxiv_fetcher.py → Fetches the latest knowledge.
3. retrieval.py → Adds the fetched knowledge to the database.
4. ranking.py → Ranks the retrieved documents based on trust and relevance.
5. consistency.py → Ensures that responses are consistent with previous responses.
6. app.py → The Streamlit UI for interacting with the assistant.
