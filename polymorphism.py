import fasttext
import numpy as np


"""
download farsi word2vec:  https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.fa.300.bin.gz
get word2vec farsi vectors that is include the meanings of words
if the correlation of Polymorphic word and neighbors is lower than 0.3 replace with value
neighbors must relative to Polymorphic word!!

"""

dict = {
'خار':'خوار',
'خوار':'خار',

'صفر':'سفر',
'سفر':'صفر',

'ثواب':'صواب',
'صواب':'ثواب',

'حیاط':'حیات',
'حیات':'حیاط',

'قریب':'غریب',
'غریب':'قریب',

'غربت':'قربت',
'قربت':'غربت',

'منصوب':'منسوب',
'منسوب':'منصوب',

'فراق':'فراغ',
'فراغ':'فراق',

'گفتار':'کفتار',
'کفتار':'گفتار',

'غدیر':'قدیر',
'قدیر':'غدیر',

'شصت':'شست',
'شست':'شصت',

'صد':'سد',
'سد':'صد',

'راضی':'رازی',
'رازی':'راضی',

'منصوب':'منسوب',
'منسوب':'منصوب',

'اقرب':'عقرب',
'عقرب':'اقرب',

'اساس':'اثاث',
'اثاث':'اساس',

'خان':'خوان',
'خوان':'خان',

}

ft = fasttext.load_model('cc.fa.300.bin')
def calculate_correlation(sentence, dict):

    # Tokenize the sentence
    words = sentence.split(" ")


    correlations = []


    # Iterate through each token in the sentence
    for i, token in enumerate(words):
        # Check if the token is in the word list
        if token in dict:
        # if token in word_list:
              # Get word vectors for the current word, its preceding word, and succeeding word
               word_vector = ft.get_word_vector(token)
               prev_word_vector = ft.get_word_vector(words[i-1]) if i > 0 else np.zeros_like(word_vector)
               print(prev_word_vector.shape)
               next_word_vector =ft.get_word_vector(words[i+1]) if i < len(words)-1 else np.zeros_like(word_vector)

               # Calculate correlations
               correlation_prev = np.corrcoef(word_vector, prev_word_vector)[0, 1]
               correlation_next = np.corrcoef(word_vector, next_word_vector)[0, 1]

               a = correlation_next + correlation_prev / 2
               print("a", a)

               if  a > 0.3:
                  break
               else:
                  words[i]= words[i].replace(words[i], dict[words[i]])
               print(words)


               correlations.append({
                    'word': words[i],
                    'prev_word': words[i-1] if i > 0 else 0 ,
                    'next_word': words[i+1] if i < len(words)-1 else 0,
                    'correlation_prev': correlation_prev,
                    'correlation_next': correlation_next
                })

    return correlations


# Example usage
sentence = " غریب به صد سال است که از این روزگار قریب میگذریم خواهیم گذشت"
result = calculate_correlation(sentence, dict)

for item in result:
    print(item)
