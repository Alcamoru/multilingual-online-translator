import requests

from bs4 import BeautifulSoup

print('Type "en" if you want to translate from French into English, '
      'or "fr" if you want to translate from English into French:')

language_choice = input()

print("Type the word you want to translate:")

word_to_translate = input()

print(f'You chose "{language_choice}" as the language to translate "{word_to_translate}" to.')

if language_choice == "en":
    r = requests.get("https://context.reverso.net/translation/french-english/" + word_to_translate,
                     headers={'User-Agent': "Mozilla/5.0"})
else:
    r = requests.get("https://context.reverso.net/translation/english-french/" + word_to_translate,
                     headers={'User-Agent': "Mozilla/5.0"})

if r:
    print(r.status_code, "OK")
    soup = BeautifulSoup(r.content, "html.parser")
    print("Translations")

    all_translations = soup.find_all("a", {"class": "translation"})
    all_examples = soup.find_all("div", {"class": "trg ltr"})

    words = []
    examples = []

    for translation in all_translations:
        print(translation.text.strip())

    print(examples)

    for example in all_examples:
        print(example.text.strip())

else:
    print("NO")
