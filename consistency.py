import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from langchain_community.vectorstores import FAISS, Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize ChromaDB with embedding function
db = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)

def consistency_check(query, new_response, threshold=0.6):

    """Checks consistency of new response by comparing it with past responses."""
    
    # Retrieve past responses from the database
    past_responses = db.similarity_search(query, k=3)
    
    # If no past responses exist, assume consistency
    if not past_responses:
        print("ℹ️ No past responses found. Assuming consistency.")
        return True
    
    past_texts = [doc.page_content for doc in past_responses]
    
    # Convert responses to vector representation
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(past_texts + [new_response])
    
    # Compute cosine similarity between new response and past responses
    cosine_sim = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
    
    # Check similarity threshold
    max_sim = np.max(cosine_sim)
    if max_sim < threshold:
        print(f"⚠️ Possible knowledge drift detected! Max similarity: {max_sim:.2f}")
        return False
    
    print(f"✅ Response is consistent. Max similarity: {max_sim:.2f}")
    return True
