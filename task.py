
text = input('enter the word: ')

last_letter = ' a, e, i, o, u'


if text[-1:] in last_letter:
    print(f'{text}-inator {len(text)}000')
else:
    print(f'{text}inator {len(text)}000')

