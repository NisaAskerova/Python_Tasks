# ✅ Task 1:
# İstifadəçidən ad daxil et.
# Əgər ad "a" hərfi ilə başlayırsa, "Ad 'a' ilə başlayır" yaz.
user_name="Aaa"
lower_name=user_name.lower()
letter="a"
if lower_name[0]==letter:
    print("Ad 'a' ilə başlayır")
else:
    print("NO")
    
# ✅ Task 2:
# İstifadəçidən bir cümlə daxil et.
# Əgər cümlənin uzunluğu 20-dən çoxdursa, "Uzun cümlə", əks halda "Qısa cümlə" yaz.
sentence="sdfghjkl;jhgfdsdfgdfergtyuihj"
print("Uzun cümlə" if len(sentence)>20 else "Qısa cümlə")
    
# ✅ Task 3:
# İstifadəçidən ad daxil et.
# Əgər bütün hərflər kiçikdirsə, "Adda bütün hərflər kiçikdir" yaz.
# Əgər bütün hərflər böyükdürsə, "Adda bütün hərflər böyükdür" yaz.
name="NISE"
if name.islower():
    print("Adda bütün hərflər kiçikdir")
elif name.isupper():
    print("Adda bütün hərflər böyükdür")
else:
    print("Hecbirine daxil deyil")

# ✅ Task 4:
# İstifadəçidən şərh (comment) daxil et.
# Əgər şərh boşdursa (yəni yalnız boşluqdursa), "Şərh boşdur" yaz.
comment=""
print("Şərh boşdur" if not comment else "OK")

# ✅ Task 5:
# İstifadəçidən e-mail daxil et.
# Əgər e-mail "@gmail.com" ilə bitmirsə, "Yalnız Gmail qəbul olunur" yaz.
mail="nise@gmail.com"
if not mail.endswith("@gmail.com"):
    print("Yalnız Gmail qəbul olunur")
else:
    print("ugurla tamamlandi")
    
# ✅ Task 6:
# İstifadəçidən şifrə daxil et.
# Əgər şifrə 8 simvoldan qısadırsa, "Şifrə zəifdir", əks halda "Şifrə qəbul olundu" yaz.
password="12323ghj"
if len(password) < 8:
    print("Şifrə zəifdir")
else:
    print("Şifrə qəbul olundu")

# ✅ Task 7:
# İstifadəçidən cümlə daxil et.
# Əgər cümlədə "python" sözü varsa (kiçik hərflə), "Python tapıldı" yaz.
sentence2="Men python oyrenirem"
letter2="python"
if letter2 in sentence2:
    print("Python tapıldı")
else:
    print("Cumle tapilmadi")

# ✅ Task 8:
# İstifadəçidən ad daxil et.
# Əgər adın sonunda "ə" hərfi varsa, "Ad Azərbaycan dilinə uyğundur" yaz.
name_user="Nisə"
letter3="ə"
if name_user.endswith(letter3):
    print("Ad Azərbaycan dilinə uyğundur")
else:
    print("Ad Azərbaycan dilinə uyğun deyil")

# ✅ Task 9:
# İstifadəçidən hər hansı bir söz daxil et.
# Əgər söz rəqəmlərdən ibarətdirsə, "Bu sadəcə rəqəmdir" yaz.
num="123"
if num.isdigit():
    print("Bu sadəcə rəqəmdir")
else:
    print("tekce reqem deyil")

# ✅ Task 10:
# İstifadəçidən ad daxil et.
# Əgər ad 3 simvoldan qısadırsa və ya yalnız boşluqdan ibarətdirsə, "Düzgün ad daxil edilməyib" yaz.
name2=""
if len(name2.strip())<3:
    print("Düzgün ad daxil edilməyib")
else:
    print("ugurla tamamlandi")