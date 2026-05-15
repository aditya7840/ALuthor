BOOK_KNOWLEDGE = {
    "personal finance": [
        "Budgeting helps track income and expenses.",
        "Saving should ideally be 20% of income.",
        "Investing early benefits from compounding.",
        "Emergency funds cover 3-6 months of expenses."
    ],
    "java": [
        "Java is object-oriented programming language.",
        "JVM runs Java bytecode.",
        "Classes and objects are core concepts.",
        "Inheritance enables code reuse."
    ]
}


def retrieve(topic):
    topic = topic.lower()
    results = []

    for key in BOOK_KNOWLEDGE:
        if key in topic:
            print("rag is working")
            results.extend(BOOK_KNOWLEDGE[key])

    return results[:5]