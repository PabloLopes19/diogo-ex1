from main import get_sensored_words

def test_sensored():
    frases = [
        "Você é uma bolota",
        "Você é uma Bolota",
        "Você é um bolo de cenoura",
        "Bolota , muito bolota e desrespeitoso",
    ]

    assert get_sensored_words(frases[0]) == "Você é uma ***"
    assert get_sensored_words(frases[1]) == "Você é uma ***"
    assert get_sensored_words(frases[2]) == "Você é um bolo de cenoura"
    assert get_sensored_words(frases[3]) == "*** , muito *** e desrespeitoso"
