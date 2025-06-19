email_enter = input("Emailingiz >> ")

emails = email_enter.split(',')

domains = []

for i in emails:
    i = i.strip()  # bo'shliqlarni olib tashlash
    i_index = i.find('@')
    if i_index != -1:
        domain = i[i_index:]  # '@' dan boshlab oxirigacha
        if domain not in domains:  # takrorlanmas bo‘lishi uchun
            domains.append(domain)

print(domains)






