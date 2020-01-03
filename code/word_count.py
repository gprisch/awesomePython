from collections import Counter

text = ('this is sample text with several words '
        'this is more sample text with some different words')

# word_dict = {}
# for w in sorted(text.split()):
#     if word_dict.get(w):
#         word_dict[w] += 1
#     else:
#         word_dict[w] = 1
word_dict = Counter(text.split())
# Header
print(f'{"WORD":<15}COUNT')
# table
for word, count in word_dict.items():
    print(f'{word:14}: {count:>3}')
# footer
print(f'The number of unique words in the text is {len(word_dict)}')


