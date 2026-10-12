# HumaLens

**See Beyond the Search.**

HumaLens is an AI-powered search engine built using Python, Streamlit, and Ollama. It retrieves web search results and generates beginner-friendly summaries using a locally running language model.

## Features
- AI-generated summaries of web search results
- Internet searching with DDGS
- Relevant source ranking and duplicate removal
- Clickable source links
- Modern, responsive interface
- Local AI processing with Llama 3.2

## Technologies
- Python
- Streamlit
- Ollama (Llama 3.2)
- DDGS
- HTML and CSS

## Running Locally
1. Install Python and Ollama.
2. Download the model with `ollama pull llama3.2:3b`.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the application using `streamlit run app.py`.

## Limitations
HumaLens uses search-result descriptions rather than full webpage content. AI-generated summaries may be incomplete or inaccurate. The current version requires Ollama to run locally.

## Project Status
Completed first local prototype — October 2026.
