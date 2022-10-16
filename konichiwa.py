# from googletrans import Translator

# translator = Translator()
# while True:
#     sentence = input("Enter a sentence in English ('q' to quit) : " )
#     if sentence == 'q':
#         break
#     else:
#         print(translator.translate(sentence, src='en', dest='ja').text)
#         continue

# Offline translation

from translate import Translator
tr = Translator(to_lang='ja')

try:
    f = open('test.txt', 'r')
    content = f.read()
    result = tr.translate(content)
    print(result)
    with open('ja.txt', 'w', encoding='utf-8') as my_file:
        my_file.write(result)
except (FileNotFoundError, IOError) as err:
    print('Check file path!') 
    raise err