# Aurelius
Ask the last of the Five Great Emperors of Rome for feedback on your journal entries! Based on the Gutenberg Project's copy of Marcus Aurelius' Meditations, this app uses Vector Embeddings and GPT to allow a user to ask questions about life and receive answers in Marcus Aurelius' writing style and provided knowledge. Please note that these responses will not be Marcus' real opinions, but GPT's generated advice based on the writings of Aurelius.

## Introduction
This project came from my fascination with Ancient Philosophy and it's effect on culture and even our everyday lives. Since human nature hasn't changed much in millenia, I believe it is important to stand on the shoulders of giants and rediscover the epiphanies and discoveries that philosophers from the past have already made.

When reading ancient texts like Meditations, there is a barrier to entry because of how antiquated some of the public translations are, and the belief that the advice may not be applicable to modern life. However, I believe that with tools like GPT, we can leverage the semantic understanding of Large Language Models and personalize the advice and wisdom to the user. To achieve this in this project, I have created and stored vector embeddings of the full text of Meditations, and OpenAI's GPT-3.5 API for natural language generation and interfacing with the user through chatting.

## Technical Features
- OpenAI GPT integrated with LangChain for advanced language processing and generation.
- Used OpenAI's Ada text embedding API to create embeddings of the cleaned text.
- LangChain's Pinecone integration for Vector Embedding Retrieval

## Installation
### Demo
Online demo coming soon!

### To install locally
1. Install prerequisites using ```pip install -qU langchain openai pinecone-client```
2. Add your OpenAI API key to the first cell as ```openaikey="your API Key Here"```
3. Add your Pinecone API key and Pinecone Index Environment as ```pineconekey = "your API Key Here"
pineconeenv = "Env Name Here"```

### Prerequisites
- Python 3.x
- LangChain
- OpenAI GPT API
- Pinecone
