# CrediTrust Complaint Insight Assistant

This project is an internal AI-powered chatbot tool built for **CrediTrust Financial**, designed to help teams quickly understand customer pain points from thousands of unstructured complaint narratives. By leveraging Retrieval-Augmented Generation (RAG), this assistant enables product managers, compliance officers, and support teams to ask natural language questions and get concise, context-backed answers.


### Project Goals

-  Reduce time-to-insight from days to minutes
-  Empower non-technical teams to find answers easily
-  Proactively identify and fix issues across products

---

## 🔧 Technical Overview

This project uses **Retrieval-Augmented Generation (RAG)** to combine semantic search and large language models for Q&A over complaint data.

### Core Components

1. **Data Preprocessing**
   - Loaded and cleaned the CFPB complaints dataset
   - Filtered to five core financial products
   - Removed boilerplate and empty entries

2. **Text Embedding & Vector Store**
   - Split long texts into chunks
   - Used `all-MiniLM-L6-v2` from `sentence-transformers` for embeddings
   - Stored in ChromaDB with metadata

3. **RAG Pipeline**
   - Embeds user question
   - Retrieves top-k relevant complaint chunks
   - Uses LLM to generate concise, grounded answers
   - Returns both the answer and source chunks for transparency

4. **Interactive Interface**
   - Built with **Gradio**
   - Features:
     - Text input for questions
     - AI-generated answer
     - Display of source text for transparency
     - "Clear" button to reset the chat

