from googletrans import Translator, LANGUAGES

def validate_language_code(code):
    return code.lower() in LANGUAGES

def translate_text(text, target_language):
    translator = Translator()
    translations = []
    max_chars = 20000  # Limite de caracteres para cada tradução

    for i in range(0, len(text), max_chars):
        chunk = text[i:i+max_chars]
        translation = translator.translate(chunk, dest=target_language)
        translations.append(translation.text)

    return ' '.join(translations)

def main():
    text = input("Digite o texto que deseja traduzir: ")
    target_language = input("Digite o código do idioma de destino: ")

    target_language = target_language.lower()

    # Verificar se o idioma de destino é válido
    if not validate_language_code(target_language):
        print("Idioma de destino inválido!")
        return

    translated_text = translate_text(text, target_language)
    print(f"Texto traduzido: {translated_text}")

if __name__ == "__main__":
    main()
