

fish = input("FISH ni kiriting (Familiya Ism Sharif): ")

qisimlar = fish.split()

familiya = qisimlar[0]

ism_sharif = ' '.join(qisimlar[1:])


natija = f"{ism_sharif}, {familiya}"
print(natija)

























''''''
# nums = [1,2,3,7,8,9]
# result = []

# i = 0
# while i < len(nums):
#     j = i + 1
#     while j < len(nums):
#         if nums[i] + nums[j] == 10:
#             result.append([nums[i],nums[j]])
#         j += 1
    
#     i += 1

# print(result)

''''''

# TODO listlarni bir qatorda yaratish  


# nums = [value for value in range(1,10)]

# print(nums)



# TODO .split()


# text = "qizil qora oq kok"

# color = text.split(" ")

# print(color)



# TODO .join()

# nums = ['65','45','34','3423']

# text = "_".join(nums)

# print(text)