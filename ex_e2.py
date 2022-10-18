# 2.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
# ex:   parola abc => ***
#       parola abcd => ****

user = input('Introduceti numele user-lui : ')
parola = input('Introduceti parola : ')
parola = '*'*len(parola)
print(f'Parola pentru userul {user} este {parola} si are {len(parola)} caractere.')


