# 🌀 FOR DÖVRÜ TƏMƏL TAPŞIRIQLAR

# 📝 TAPSIRIQ 1:
# Siyahıdakı bütün elementləri for dövrü ilə çap et.
# Çıxış:
# alma
# armud
# banan
# heyva

fruits = ["alma", "armud", "banan", "heyva"]
for fruit in fruits:
    print(fruit)

# 📝 TAPSIRIQ 2:
# Siyahıdakı ədədlərin cəmini hesabla.
# Çıxış:
# Cəm: 35
nums = [3, 7, 12, 9, 4]
result=0
for num in nums:
    result+=num
print(result)


# 📝 TAPSIRIQ 3:
# Siyahıdakı ədədlərin kvadratlarını çap et.
# Çıxış:
# 4
# 25
# 36
nums = [2, 5, 6]
list_nums=[]

for num in nums:
    list_nums.append(num**2)
print(list_nums)



# 📝 TAPSIRIQ 4:
# Siyahıdakı tək ədədləri yeni siyahıya əlavə et və çap et.
# Çıxış:
# Tək ədədlər: [1, 7, 9]
nums = [1, 4, 7, 8, 9, 12]
odd_list=[]
for num in nums:
    if num %2==0:
        continue
    odd_list.append(num)
print(odd_list)


# 📝 TAPSIRIQ 5:
# Sözlər siyahısında neçə sözün 5 hərfdən uzun olduğunu say.
# Çıxış:
# 5 hərfdən uzun olanların sayı: 2
words = ["salam", "dunya", "python", "list", "kitabxana"]
long_word=[]
for word in words:
    if len(word) >5:
       long_word.append(word)
print(f"5 hərfdən uzun olanların sayı: {len(long_word)}")


# 🔁 FOR DÖVRÜ – ŞƏRTLİ TAPŞIRIQLAR

# 📝 TAPSIRIQ 6:
# 0-dan 10-a qədər ədədləri çap et.
# Çıxış:
# 0 1 2 3 4 5 6 7 8 9 10

for x in range(10+1):
    print(x)

# 📝 TAPSIRIQ 7:
# 1-dən 100-ə qədər olan cüt ədədlərin cəmini tap.
# Çıxış:
# Cəm: 2550

even_numbers=0

for number in range(100+1):
    if number % 2== 0:
        even_numbers+=number
print(even_numbers)

# 📝 TAPSIRIQ 8:
# İstifadəçidən 5 ədəd al və onların ortalamasını tap.
# İpucu: input() və int() istifadə et.


# 📝 TAPSIRIQ 9:
# Siyahıdakı sözlərin ilk hərflərini çap et.
# Çıxış:
# a
# b
# n
# h

words = ["alma", "banan", "nar", "heyva"]

for word in words:
    print(word[0])


# 📝 TAPSIRIQ 10:
# Siyahıdakı ədədlərin neçə dənəsi 10-dan böyükdür?
# Çıxış:
# 10-dan böyük ədədlərin sayı: 3

nums = [4, 11, 23, 5, 8, 15]
big_numbers=[]

for num in nums:
    if num >10:
        big_numbers.append(num)
print(f"10-dan böyük ədədlərin sayı: {len(big_numbers)}")