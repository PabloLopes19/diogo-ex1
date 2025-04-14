def get_sensored_words(text):
    words = text.split()

    for word in words:
        if(word.lower() == "bolota"):
            return text.replace(word, "***")

    return text

##print(get_sensored_words("Você é um baita de um Bolota aaa"))
    