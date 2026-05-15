# ALuthr
AI Book Generator (Agentic Pipeline with RAG + PDF Output)

This project is a multi-stage AI pipeline that generates a complete book from a simple topic prompt.

Add .env file with GROQ_API_KEY= xxx.... 

It uses:

LLM (via Groq API)
Retrieval-Augmented Generation (RAG)
Modular agents (planner, writer, editor, etc.)
PDF generation with proper book structure
Logging for debugging and traceability
🚀 Features

✅ Generate full books from a single prompt

✅ Multi-agent pipeline (planner → writer → formatter)

✅ RAG (injects factual knowledge into writing)

✅ Front matter (title page, dedication, TOC)

✅ Back matter (references, about author)

✅ Automatic PDF generation

✅ Logging system for debugging

🧠 Architecture
User Input

   ↓
   
Planner

   ↓
   
RAG Retriever

   ↓
   
Writer

   ↓
   
Humanizer

   ↓
   
Editor

   ↓
   
Assembler

   ↓
   
Formatter (PDF)

📁 Project Structure

project/

│

├── orchestrator.py     # Main pipeline controller

├── planner.py          # Generates book structure

├── writer.py           # Writes chapters

├── humanizer.py        # Improves tone

├── editor.py           # Cleans content

├── assembler.py        # Builds full book structure

├── formatter.py        # Converts book → PDF

├── rag.py              # Simple knowledge retrieval

├── memory.py           # Stores shared context

├── prompts.py          # LLM prompts

├── config.py           # Settings (model, tone, chapters)

├── logger.py           # Logging system

├── groq_client.py      # Groq API integration

│

└── logs/

    └── app.log         # Generated logs
    

⚙️ Installation

1️⃣ Clone project

git clone <your-repo-url>

cd project

3️⃣ Install dependencies

reportlab

groq

python-dotenv
