from ex1 import get_sensored_words

def test_sensored():
    frases = [
        "Você é uma bolota",
        "Você é uma Bolota",
        "Você é um bolo de cenoura",
        "Bolota, muito bolota e desrespeitoso",
    ]

    assert get_sensored_words(frases[0]) == "você é uma ***"
    assert get_sensored_words(frases[1]) == "você é uma ***"
    assert get_sensored_words(frases[2]) == "você é um bolo de cenoura"
    assert get_sensored_words(frases[3]) == "***, muito *** e desrespeitoso"
