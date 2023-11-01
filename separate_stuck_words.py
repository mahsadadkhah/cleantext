from math import log

"""
This code seprate stuck words in the sentence 
for recognize all words we need a complete dictionary
"""


# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("C:\\Users\\Mahsa\\Downloads\\words.txt", encoding='utf-8').read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)


def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k, c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1, len(s)+1):
        c, k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i > 0:
        c, k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))


def separate_words(s):
    # Convert the sentence to a list of words
    words = s.split()
    # Separate merged words
    for i in range(len(words)):
        if len(words[i]) > 3:
            separated = infer_spaces(words[i])
            if len(separated.split()) == 2 or len(separated.split()) == 3:
                words[i] = separated

    # Join the words with a space and return the final sentence
    return " ".join(words)


sentence = 'علی از کتابخانهشریعتیکتابی را امانتگرفت ولیآنراپس نداد'
cleaned = separate_words(sentence)
print(cleaned)

