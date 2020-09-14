# in automate_4_1.py

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs'
]

list_length = len(spam)

text = ''

for i in range(list_length):
    if i < list_length-1:
        text = text + spam[i]
        text = text + ', '
    else:
        break

text = text + 'and ' + spam[list_length-1]

print(text)


