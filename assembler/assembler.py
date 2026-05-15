def assemble_book(title, chapters):
    return {
        # 📘 FRONT MATTER
        "front": {
            "half_title": title,
            "title_page": {
                "title": title,
                "author": "Aditya (Generated Book System)",
                "edition": "1st Edition",
                "copyright": "© 2026 Aditya AI Book Generator. All rights reserved.",
                "dedication": "For learners who build systems, not just scripts.",
                "toc": [ch["title"] for ch in chapters]
            },
        },
        # 📚 BODY
        "chapters": chapters,
        # 📕 BACK MATTER
        "back": {
            "afterword": "Keep learning. Systems improve with iteration.",
            "references": [
                "AI-generated internal knowledge base",
                "Groq LLM outputs",
                "Custom RAG dataset"
            ],
            "about_author": "Aditya is a Software Engineer building agentic AI systems."
        }
    }