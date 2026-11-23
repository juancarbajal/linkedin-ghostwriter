import re

forbidden_words = [
    "game changer", "revolución", "revolucionario", "revolucionaria",
    "llegó para quedarse", "disruptivo", "disruptiva", "disrupción",
    "nueva era", "el futuro ya está aquí", "adaptarse o morir", "esto lo cambia todo"
]

def check_text(text, name):
    words = len(re.findall(r'\b\w+\b', text))
    print(f"[{name}] Word count: {words}")
    lower_text = text.lower()
    for fw in forbidden_words:
        if fw in lower_text:
            print(f"  FAILED: contains forbidden phrase '{fw}'")
    return words

