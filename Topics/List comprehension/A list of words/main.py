# work with the preset variable `words`
# words = ['apple', 'pear', 'banana', 'Ananas']
new_list = list()

for word in words:
    if word.startswith('a') or word.startswith('A'):
        new_list.append(word)
print(new_list)
