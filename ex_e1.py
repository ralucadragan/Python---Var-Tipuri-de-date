# 1. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

text = 'alabala portocala'
print (f'Textul introdus esete : {text}')
primul_caract = text [0]
print (f'Primul caracter este: {primul_caract}')
print (f'Textul final este : {text[0] + text[1:len(text)-1].replace(primul_caract,primul_caract.upper()) + text[-1]}')

print('---------------------------------------------------------')

text_nou = input('Introduceti textul dorit : ')
primul_caract2 = text [0]
print (f'Primul caracter este: {primul_caract2}')
print (f'Textul final este : {text_nou[0] + text_nou[1:len(text_nou)-1].replace(primul_caract2,primul_caract2.upper()) + text_nou[-1]}')