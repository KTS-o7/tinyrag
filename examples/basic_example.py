from tinyrag.tinyrag import TinyRAG_Ollama

rag = TinyRAG_Ollama(llm_model='llama3.2:1b')

sample_docs = [ # made up info, pass any text here
    "Zephyr Quantum was founded in 2023 by Dr. Voss in Maple Ridge, BC.",
    "QuantumShield 3.0 launched January 2025 with 512-bit encryption.",
    "Board: Dr. Voss (CEO), Chen (CTO), Karim (CFO), plus 3 non-execs.",
    "Series B: $42M in October 2024 from Horizon, Quantum Capital, TechFusion.",
    "78 employees across Maple Ridge, Singapore, Zurich. 120 planned by end of 2025.",
    "Competitors: QuantumWall (US), SecureFuture (Germany), NexGen (Israel).",
    "Q4 2024: $8.7M revenue, up 34%. 2025 projection: $45-50M.",
    "Project Aurora: quantum-resistant IoT protocol in development.",
    "Clients: 2 Fortune 500 banks, 3 govt agencies, healthcare providers. Largest: GlobalBank.",
    "17 patents filed, 9 granted as of January 2025."
]

rag.add_documents(sample_docs) # add custom instructions to the LLM here if required
result = rag.query("What's Zephyr Quantums largest client? and give me more info about who their other clients are, be super verbose about it (do not makeup info and stick to the context)")
print(result)