import pyjokes
from deep_translator import GoogleTranslator

# Here you have Jokes translate to French
    
def translate_to_french(text):
    translator = GoogleTranslator(source="en", target="fr")
    translated = translator.translate(text)
    return translated

def tell_french_joke():
    joke = pyjokes.get_joke()
    french_joke = translate_to_french(joke)
    print("Blague en français :")
    print(french_joke)
    
    
if __name__ == "__main__":
    tell_french_joke()
