# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# Afișează de câte ori apare cuvântul 'the'

# 9. Același string:
# Afișează de câte ori apare cuvântul 'the';
# Printează rezultatul.

text = 'Coral is either the stupidest animal or the smartest rock'
cuvant = 'the'
print(text)
print(f'Cunatul {cuvant} apare de {str.count(text, cuvant)} ori')

# 10. Același string:
# Folosește un assert ca să verifici dacă acest string conține doar numere.
print ('--------------------------------')
text_nou = 'Coral is either the stupidest animal or the smartest rock'
assert text_nou.isnumeric()

# print ('--------------------------------')
# text_nou2 = '235697'
# assert text_nou2.isnumeric()