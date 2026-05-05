# Import the GoogleTranslator class from deep_translator library
# This library is used to translate text between different languages
from deep_translator import GoogleTranslator


# Start an infinite loop so the program keeps running
# until the user decides to exit
while True:

    # Take input text from the user
    # User can type any sentence they want to translate
    text = input("Enter text (or type exit): ")

    # Check if the user wants to exit the program
    # .lower() converts input to lowercase to handle cases like EXIT, Exit, etc.
    if text.lower() == "exit":
        print("Exiting the program...")
        break   # Break the loop and stop the program

    # Ask the user to enter the target language code
    # Example: 'hi' for Hindi, 'fr' for French, 'es' for Spanish
    target = input("Enter target language (hi, fr, es): ")

    # Perform translation using GoogleTranslator
    # source='auto' → automatically detects the input language
    # target=target → translates into the language chosen by the user
    # .translate(text) → translates the given text
    translated = GoogleTranslator(source='auto', target=target).translate(text)

    # Display the translated output to the user
    print("Translated:", translated)


# End of program
