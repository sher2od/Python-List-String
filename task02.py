
sohalar = input("Sohalarni vergul bilan  kiriting: ")

sohalar_list = sohalar.split(',')

snake_case_list = [soha.strip().lower().replace(' ', '_') for soha in sohalar_list]

natija = '_'.join(snake_case_list)

print(natija)



