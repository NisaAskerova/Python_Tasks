# 📝 TAPSIRIQ 1:
# Verilmiş string-in hər bir hərfini for dövrü ilə çap et.
# word = "python"
# Çıxış:
# p
# y
# t
# h
# o
# n

word = "python"
for letter in word:
    print(letter)


# 📝 TAPSIRIQ 2:
# Verilmiş siyahıdakı ədədlərdən yalnız müsbət olanları çap et.
# nums = [5, -3, 8, -1, 0, 4]
# Çıxış:
# 5
# 8
# 4

nums = [5, -3, 8, -1, 0, 4]
positeive_nums=[]
for num in nums:
    if num>0:
        positeive_nums.append(num)
print(positeive_nums)


# 📝 TAPSIRIQ 3:
# Verilmiş siyahıda 0 görünənə qədər ədədləri cəmlə.
# Əgər siyahıda 0 yoxdursa, hamısını cəmlə.
# nums = [3, 7, 0, 12, 5]
# Çıxış:
# Cəm: 10
# (çünki 0 görünənə qədər olan 3 və 7 toplanır)

nums = [3, 7, 0, 12, 5]
sum=0

for num in nums:
    if num==0:
        break
    sum+=num
print(f"Cəm: {sum}")
    



# 📝 TAPSIRIQ 4:
# Verilmiş string-in içindəki saitləri çap et (a, e, i, o, u).
# text = "kod yazmaq gozeldir"
# Çıxış:
# o
# a
# a
# o
# e
# i

text = "kod yazmaq gozeldir"
vowel=["a", "e", "i", "o", "u"]

for t in text:
    if t in vowel:
        print(t)


# 📝 TAPSIRIQ 5:
# Verilmiş siyahıdakı bütün sözləri `a` hərfi ilə başlayırsa çap et.
# words = ["alma", "armud", "banan", "ananas", "heyva"]
# Çıxış:
# alma
# armud
# ananas

words = ["alma", "armud", "banan", "ananas", "heyva"]
letter="a"
for word in words:
    if word.startswith(letter):
        print(word)



# 📝 TAPSIRIQ 6:
# 1-dən 20-yə qədər ədədləri dövrə sal, amma 10-da dövrü dayandır (`break`).
# Çıxış:
# 1
# 2
# ...
# 9

for number in range(1,20):
    if number==10:
        break
    print(number)

# 📝 TAPSIRIQ 7:
# 1-dən 10-a qədər ədədlər arasında yalnız tək olanları çap et.
# Çıxış:
# 1
# 3
# 5
# 7
# 9

for num in range(10):
    if num % 2 ==0:
        continue
    print(num)

# 📝 TAPSIRIQ 8:
# Verilmiş siyahıda yalnız tam ədədləri topla. Digər tipləri atla.
# mixed = [4, "salam", 7, 3.5, True, 9] 
# Çıxış:
# Cəm: 20  (4 + 7 + 9)

mixed = [4, "salam", 7, 3.5, True, 9] 
sum=0
for num in mixed:
    if type(num)== int:
        sum+=num
print(sum)



# 📝 TAPSIRIQ 9:
# İstifadəçi adları olan siyahıdan yalnız 5 hərfdən uzun olanları yeni siyahıya əlavə et.
# users = ["nisa", "kamran", "ayla", "samir", "gulsura"]
# Çıxış:
# ['kamran', 'gulsura']

users = ["nisa", "kamran", "ayla", "samir", "gulsura"]
name_list=[]

for user in users:
    if len(user)>5:
        name_list.append(user)
print(name_list)


# 📝 TAPSIRIQ 10:
# Verilmiş cümlədə boşluqdan başqa bütün simvolları çap et.
# sentence = "Python öyrənmək gözəldir!"
# Çıxış:
# P
# y
# t
# h
# o
# n
# ö
# ...

sentence = "Python öyrənmək gözəldir!"

for char in sentence:
    if char == " ":
        continue
    print(char)
