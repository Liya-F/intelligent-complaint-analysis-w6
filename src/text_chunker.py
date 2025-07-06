import pandas as pd
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextChunker:
    def __init__(self, chunk_size: int = 300, chunk_overlap: int = 50):
        """
        Initialize the text chunker.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )

    def chunk_text(self, text: str) -> List[str]:
        """
        Chunk a single cleaned narrative.
        """
        return self.splitter.split_text(text)

    def chunk_dataframe(self, df, text_column: str = "cleaned_narrative"):
        """
        Apply chunking to a DataFrame column and return a new DataFrame
        with one row per chunk, preserving original index and product.
        """
        chunked_rows = []

        for idx, row in df.iterrows():
            chunks = self.chunk_text(row[text_column])
            for chunk in chunks:
                chunked_rows.append({
                    "original_index": idx,
                    "product": row["Product"],
                    "chunk": chunk
                })

        return pd.DataFrame(chunked_rows)
