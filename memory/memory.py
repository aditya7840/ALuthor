memory = {
    "facts": [],
    "concepts": [],
    "tone": None,
    "callbacks": []
}


def init_memory(tone):
    memory["tone"] = tone


def add_fact(f):
    memory["facts"].append(f)


def get_memory():
    return memory