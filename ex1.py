def get_sensored_words(text):
    return text.lower().replace("bolota", "***")
    

print(get_sensored_words("Bolota, muito bolota e desrespeitoso"))