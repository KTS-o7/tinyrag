<div align="center">
  <h1>tinyrag</h1>
  <p>Lightweight RAG implementation for all your LLM endpoints</p>
 <img src="https://raw.githubusercontent.com/divine-architect/tinyrag/refs/heads/main/tinyrag.png" width="300" alt="tinyrag logo">
  
</div>

## About
tinyrag is a "tiny" RAG implementation that aims to give developers a plug and play experience while writing RAG applications.
It aims to be compatible with major LLM providers and be as tiny (as the name suggests) as possible while doing so.

## Usage
Before you run tinyrag make sure you have pulled the following models from the ollama repo:
- [Nomic Text Embeddings](https://ollama.com/library/nomic-embed-text)
- Any large language model of your choice from the ollama library

Install using pip: 
```sh
pip install tinyrag
```

Example usage:
```python
import ollama
from tinyrag.tinyrag import TinyRAG_Ollama

# Initialize the RAG system with embedding and LLM models
rag = TinyRAG_Ollama(
    embedding_model="nomic-embed-text",  
    llm_model="llama3.2:3b"  # Or any other model available in Ollama
)

# Add some documents to the system
documents = [
    "Artificial intelligence (AI) is intelligence demonstrated by machines.",
    "Machine learning is a subset of AI focused on building systems that learn from data.",
    "Large Language Models (LLMs) are neural networks trained on vast amounts of text data.",
    "Retrieval Augmented Generation (RAG) combines search with generative AI to improve accuracy."
]
rag.add_documents(documents)

# Query the RAG system
question = "What is the relationship between AI and machine learning?"
response = rag.query(question, top_k=2, temperature=0.5)

# Print the response
print(f"Question: {question}")
print(f"Answer: {response}")

# Ask a follow-up question that will benefit from conversation history
follow_up = "What about LLMs, how do they relate?"
follow_up_response = rag.query(follow_up, top_k=2)

print(f"\nFollow-up: {follow_up}")
print(f"Answer: {follow_up_response}")
```

## Current features:
- Uses [nomic text embeddings](https://ollama.com/library/nomic-embed-text) as the embedding model via ollama
- Is currently compatible with any model available on [Ollama](https://ollama.com/search)
- Chat history added
- More user control for LLM settings

## Planned features/Roadmap
- Add support to more embedding models
- Currently only plaintext documents are supported, so support for database files, spreadsheets, documents, ppts, etc
- Support more endpoints such as Open AI, Claude, Deepseek, etc
- Multimodal embedding support
- Chroma DB/Custom Vector DBs support
- Implement FAISS from scratch

## Contribution | Issues/Bug reports
Contributions are always welcome! Make sure to test your forks before making a PR. \
Open an issue for Bug reports or to report other issues

## License
This project is licensed under the [MIT license](https://opensource.org/license/MIT)
