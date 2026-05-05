from deep_translator import GoogleTranslator

while True:
    text = input("Enter text (or type exit): ")

    if text.lower() == "exit":
        break

    target = input("Enter target language (hi, fr, es): ")

    translated = GoogleTranslator(source='auto', target=target).translate(text)

    print("Translated:", translated)