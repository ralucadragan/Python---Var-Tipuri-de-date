# 2. Folosind o singură linie de cod :
# citește un string de la tastatură (ex: 'alabala portocala');
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.

text = 'alabala portocala'
words = text.split()
print (f'Cuvintele care alcatuiest strigul sunt : {words}')
word1 = words[0]
word2 = words[1]
print(f'Primul cuvant este : {word1}')
print(f'Al doilea cuvant este : {word2}')

print('---------------------------------------------------------')

text_nou = input('Introduceti textul dorit : ')
words_nou = text_nou.split()
print(f'Cuvintele care alcatuiest strigul sunt : {words_nou}')
w1 = words_nou[0]
w2 = words_nou[1]
print(f'Primul cuvant este : {w1}')
print(f'Al doilea cuvant este : {w2}')