# Complaint Text Semantic Search Preparation

## Project Overview

This project processes a dataset of complaint texts to enable semantic search by performing:

1. **Text Chunking**  
   - Long complaint texts are split into smaller overlapping chunks (e.g., 300 tokens with 50-token overlap) to preserve context and improve embedding quality.

2. **Text Embedding**  
   - Each text chunk is converted into a dense vector embedding using a Sentence Transformers model (`paraphrase-MiniLM-L3-v2`), which balances speed and accuracy.

3. **Vector Indexing and Storage**  
   - Embeddings are stored in a FAISS vector index for efficient similarity search.  
   - Metadata associated with each chunk (original complaint ID, product category, chunk text) is saved alongside embeddings to allow tracing back to the original source.

