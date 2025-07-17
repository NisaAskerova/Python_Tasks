# 📝 TAPSIRIQ 1:
# Bir tuple yarat: my_tuple = (10, 20, 30, 40, 50)
# Bu tuple-ın bütün elementlərini for dövrü ilə çap et.

my_tuple = (10, 20, 30, 40, 50)
for t in my_tuple:
    print(t)

# 📝 TAPSIRIQ 2:
# Aşağıdakı tuple-dakı ikinci elementi ekrana çıxar.
numbers = (3, 6, 9, 12, 15)
print(f"Ikinci element-> {numbers[1]}")

# 📝 TAPSIRIQ 3:
# Aşağıdakı tuple-dakı sonuncu elementi çıxar.
fruits = ("alma", "armud", "banan", "əncir")
print(f"Sonuncu element-> {fruits[-1]}")

# 📝 TAPSIRIQ 4:
# Aşağıdakı iki dəyişəni tuple unpacking ilə ayır:
person = ("Ali", 25)
# name, age = ? → print(name), print(age)
name, age=person
print(name)  
print(age)

# 📝 TAPSIRIQ 5:
# Tuple-un içində olan cüt ədədləri çap et.
nums = (1, 4, 7, 8, 10, 13, 16)
for num in nums:
    if num % 2 == 0:
        print(f"Cut eded-> {num}")

# 📝 TAPSIRIQ 6:
# Bir tuple daxilində neçə element olduğunu tap və çap et.
colors = ("qırmızı", "yaşıl", "mavi", "sarı")
print(len(colors))

# 📝 TAPSIRIQ 7:
# Aşağıdakı tuple-dan "Python" sözünü çıxar (remove etmək mümkün deyil, ona görə yeni bir tuple qur).
langs = ("C", "C++", "Python", "JavaScript")
new_lang=[]
for lang in langs:
    if lang=="Python":
        continue
    new_lang.append(lang)
new_lang=tuple(new_lang)
print(new_lang)

# 📝 TAPSIRIQ 8:
# Tuple içərisindəki ədədin mövcud olub-olmadığını yoxla.
# 15 ədədi bu tuple-da varsa "var", yoxdursa "yoxdur" yaz.
numbers = (5, 10, 15, 20, 25)
num=15
if num in numbers:
    print("Var")
else:
    print("Yoxdur")

# 📝 TAPSIRIQ 9:
# Tuple-ları birləşdir:
# Yeni bir tuple qur: (1, 2, 3, 4, 5, 6)
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1+=t2
print(t1)

# 📝 TAPSIRIQ 10:
# Aşağıdakı tuple-dakı elementləri for dövrü ilə bir-bir unpack edib çap et:
# Çıxış:
# Ad: Nigar, Yaş: 20
# Ad: Rəşid, Yaş: 22
# Ad: Tunar, Yaş: 19
students = [("Nigar", 20), ("Rəşid", 22), ("Tunar", 19)]
for name, age in students:
    print(f"Ad: {name}, Yas: {age}")
