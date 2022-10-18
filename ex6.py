'''
6. Citeste de la tastatura:
- numele,
- prenumele.
Afiseaza: 'Numele complet are x caractere'.
'''

nume = input("Numele = ")
prenume = input("Prenumele = ")
nume_complet = nume+prenume
# print(nume_complet)
# print(len(nume_complet))
print(f'Numele complet are {len(nume_complet)} caractere.')

# print(str.__len__(str.__add__(nume, prenume)))
print(f'Numele complet are {str.__len__(str.__add__(nume, prenume))} caractere.')
