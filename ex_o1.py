# 1. Exercițiu:
# citește de la tastatură un string de dimensiune impară;
# afișează caracterul din mijloc.

text = input('Introduceti textul dorit:')
print(f'Textul introdus are {len(text)} caractere.')
# print (text[len(text) // 2])
print(f'Caracterul din mijloc pentru textul introdus este: {text[len(text)//2]}')

