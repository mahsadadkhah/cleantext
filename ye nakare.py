from hazm import *

modell = "C:\\Users\\Mahsa\\Downloads\\pos_tagger.model"

def remove_ye_nun(text, file_path):
    normalizer = Normalizer()
    text = normalizer.normalize(text)
    tokens = word_tokenize(text)
    tagger = POSTagger(model=modell)
    tagged_tokens = tagger.tag(tokens)

    new_tokens = []
    with open(file_path, 'r', encoding='utf-8') as file:
        words_to_skip = set(file.read().split())

    for token, tag in tagged_tokens:
        if tag == 'NOUN' or tag == 'Ne' or tag == 'PRON' or tag == 'PRON' or tag == 'ADJ' and tag != 'NOUN,EZ':
            if token[-1].endswith('ی') and token not in words_to_skip:
                token = token.replace('ی', '')
            new_token = token
        else:
            new_token = token
        new_tokens.append(new_token)
    return ' '.join(new_tokens)

file_path= "C:\\Users\\Mahsa\\Desktop\\New folder\\cleaned_output_file.txt"
text = "علی درختی را روی نقاشی جنگلی دید"
print(remove_ye_nun(text, file_path))
