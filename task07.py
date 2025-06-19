
malumot = "Ism:Ali, Familiya:Valiyev, Yil:2002"

juftliklar = malumot.split(',')


for juftlik in juftliklar:
    kalit, qiymat = juftlik.split(':')
    print(f"{kalit.strip()}: {qiymat.strip()}")
