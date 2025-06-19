
text_enter = input("sozlarni vergul bilan kiriting ")

text = text_enter.split(' ')

bow = []
for i in text:
    if i == i[::-1]:
        bow.append(i)

print(bow)
