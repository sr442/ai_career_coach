def generate_response(mode, text):
    if mode == "Concise":
        return ". ".join(text.split(".")[:2]) + "."
    elif mode == "Detailed":
        return text
    return text
