# 📝 TAPSIRIQ 1:
# Verilmiş `numbers` siyahısını artan və azalan qaydada sıralayıb ekrana çıxar.
# Çıxış:
# Artan: [1, 2, 3, 5, 8, 9]
# Azalan: [9, 8, 5, 3, 2, 1]

numbers = [5, 3, 8, 1, 9, 2]
numbers.sort()
print("Artan:", numbers) 

numbers.sort(reverse=True)
print("Azalan:", numbers)

# 📝 TAPSIRIQ 2:
# Verilmiş siyahıdakı ədədləri Cüt və tək olaraq ayır və iki ayrı siyahı kimi çap et.
# Çıxış:
# Cüt ədədlər: [4, 10, 18]
# Tək ədədlər: [7, 13, 21]

nums = [4, 7, 10, 13, 18, 21]
cut=[]
tek=[]

if nums[0] % 2==0:
    cut.append(nums[0])
else:
    tek.append(nums[0])

if nums[1] % 2==0:
    cut.append(nums[1])
else:
    tek.append(nums[1])

if nums[2] % 2==0:
    cut.append(nums[2])
else:
    tek.append(nums[2])
    
if nums[3] % 2==0:
    cut.append(nums[3])
else:
    tek.append(nums[3])
if nums[4] % 2==0:
    cut.append(nums[4])
else:
    tek.append(nums[4])
if nums[5] % 2==0:
    cut.append(nums[5])
else:
    tek.append(nums[5])

print("Cut:", cut)
print("Tek:", tek)
    


# 📝 TAPSIRIQ 3:
# Daxil edilən sözlər siyahısında, hər bir sözün uzunluğunu çap et.
# Çıxış:
# salam - 5 hərf
# dunya - 5 hərf
# python - 6 hərf
# liste - 5 hərf

words = ["salam", "dunya", "python", "liste"]
print(f"salam - {len(words[0])}  hərf")
print(f"dunya - {len(words[1])}  hərf")
print(f"python - {len(words[2])} hərf")
print(f"liste - {len(words[3])}  hərf")


# 📝 TAPSIRIQ 4:
# Verilmiş siyahıdakı rəqəmlərin kvadratlarını yeni siyahı şəklində çıxart.
# Çıxış:
# Kvadratlar: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
number_list=[]
num=numbers[0] **2
num1=numbers[1] **2
num2=numbers[2] **2
num3=numbers[3] **2
num4=numbers[4] **2

number_list.append(num)
number_list.append(num1)
number_list.append(num2)
number_list.append(num3)
number_list.append(num4)
print(f"Kvadratlar: {number_list}" )

# 📝 TAPSIRIQ 5:
# Listin içindən ən böyük və ən kiçik rəqəmi tap.
# Çıxış:
# Ən kiçik: 3
# Ən böyük: 22

nums = [13, 7, 22, 3, 19]

min_num=min(nums)
max_num=max(nums)

print(f"Ən kiçik: {min_num}")
print(f"Ən böyük: {max_num}")

# 📝 TAPSIRIQ 6:
# Verilmiş siyahıya `42` ədədini sona əlavə et.
# Çıxış:
# [3, 7, 12, 42]

numbers = [3, 7, 12]
numbers.append(42)
print(numbers)


# 📝 TAPSIRIQ 7:
# Verilmiş siyahıya `100` rəqəmini 1-ci indeksə (2-ci yerə) əlavə et.
# Çıxış:
# [10, 100, 20, 30]

nums = [10, 20, 30]
nums.insert(1, 100)
print(nums)

# 📝 TAPSIRIQ 8:
# Siyahıdan `15` ədədini sil.
# Çıxış:
# [3, 7, 20]

nums = [3, 7, 15, 20]
nums.remove(15)
print(nums)

# 📝 TAPSIRIQ 9:
# Siyahıdakı `9` rəqəminin indeksini tap və çap et.
# Çıxış:
# 2

numbers = [4, 7, 9, 12]
print(numbers.index(9))


# 📝 TAPSIRIQ 10:
# Verilmiş siyahıdakı bütün elementləri sil və boş siyahı çap et.
# Çıxış:
# []

fruits = ["alma", "armud", "banan"]
fruits.clear()
print(fruits)
