import pandas as pd
import numpy as np
import pickle
import os
from sentence_transformers import SentenceTransformer
import faiss
import uuid

class Portfolio:
    def __init__(self, file_path="ColdEmailGenerator/resources/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.vectorstore_path = "ColdEmailGenerator/vectorstore"
        self.index_path = os.path.join(self.vectorstore_path, "faiss_index.bin")
        self.metadata_path = os.path.join(self.vectorstore_path, "metadata.pkl")
        
        # Initialize sentence transformer for embeddings
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Create vectorstore directory if it doesn't exist
        os.makedirs(self.vectorstore_path, exist_ok=True)
        
        # Load or create FAISS index
        self.index, self.metadata = self._load_or_create_index()

    def _load_or_create_index(self):
        """Load existing FAISS index or create a new one"""
        if os.path.exists(self.index_path) and os.path.exists(self.metadata_path):
            # Load existing index
            index = faiss.read_index(self.index_path)
            with open(self.metadata_path, 'rb') as f:
                metadata = pickle.load(f)
            # print("Loaded existing FAISS index")
        else:
            # Create new index
            index = None
            metadata = []
            # print("Creating new FAISS index")
        
        return index, metadata

    def load_portfolio(self):
        """Load portfolio data into FAISS index"""
        if self.index is None:
            # Create embeddings for all tech stacks
            tech_stacks = self.data["Techstack"].tolist()
            embeddings = self.model.encode(tech_stacks, show_progress_bar=True)
            
            # Initialize FAISS index
            dimension = embeddings.shape[1]
            self.index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
            
            # Add embeddings to index
            self.index.add(embeddings.astype('float32'))
            
            # Store metadata (links) corresponding to each embedding
            self.metadata = self.data["Links"].tolist()
            
            # Save index and metadata
            faiss.write_index(self.index, self.index_path)
            with open(self.metadata_path, 'wb') as f:
                pickle.dump(self.metadata, f)
            
            # print(f"Created FAISS index with {len(tech_stacks)} portfolio items")

    def query_links(self, skills, n_results=2):
        """Query portfolio based on skills and return relevant links"""
        if self.index is None:
            print("No FAISS index found. Loading portfolio...")
            self.load_portfolio()
        
        # Convert skills list to a single query string
        if isinstance(skills, list):
            query_text = ", ".join(skills)
        else:
            query_text = str(skills)
        
        # Create embedding for the query
        query_embedding = self.model.encode([query_text])
        
        # Search the index
        scores, indices = self.index.search(query_embedding.astype('float32'), n_results)
        
        # Return metadata (links) for the top results
        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append({"links": self.metadata[idx]})
        
        return results

if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.load_portfolio()