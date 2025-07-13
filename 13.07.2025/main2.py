# Task 1:
# İstifadəçidən ədəd daxil et.
# Əgər ədəd müsbətdirsə, “Müsbət ədəd” çap et.
user_num=123
if user_num>0:
    print(f"Mesbet eded: {user_num}")
else:
    print("Eded menfi ve ya 0-dir")

# Task 2:
# İstifadəçidən yaşını soruş.
# Əgər yaş 18 və ya daha çoxdursa, “Seçki verməyə icazən var” yaz.
age=27
if age >=18:
    print(f"Seçki verməyə icazən var. Yas: {age}")
else:
    print("Seckide istirak haqqiniz yoxdur")
    
# Task 3:
# İstifadəçidən 3 ədəd daxil et.
# Ən böyük ədədi tapıb çap et.
num1=9
num2=6
num3=15
if num1>num2 and num1>num3:
    print(f"en boyuk eded {num1}")
elif num2>num1 and num2>num3:
    print(f"en boyuk eded {num2}")
else:
    print(f"en boyuk eded {num3}")
    
    
# Task 4:
# İstifadəçidən bir hərf daxil et.
# Əgər hərf saitdirsə (a, e, i, o, u), “Sait hərf”, yoxsa “Samit hərf” çap et.
#     Array kecmemisem

# Task 5:
# İstifadəçidən şifrə soruş.
# Əgər şifrə “admin123” ilə eynidirsə, “Uğurlu giriş”, əks halda “Giriş rədd edildi” yaz.
password="admin123"
admin_password="admin123"
print("Ugurlu giris" if password==admin_password else "Giris redd edildi")

# Task 6:
# İstifadəçidən ədəd soruş.
# Əgər ədəd həm müsbət, həm də cütdürsə, “Müsbət cüt ədəd” çap et.
number=-26
if number>0 and number % 2 == 0:
    print("Müsbət cüt ədəd")
else:
    print("Eded menfi ve ya tek ededdir")

# Task 7:
# İstifadəçidən ədəd soruş.
# Əgər ədəd 0-dan kiçikdirsə və ya 100-dən böyükdürsə, “Ədəd diapazon xaricindədir” yaz.
num=2
if num < 0 or num > 100:
    print("Ədəd diapazon xaricindədir")
else:
    print("OK")

# Task 8:
# İstifadəçidən istifadəçi adı daxil et.
# Əgər istifadəçi adı boşdursa (yəni ""), “Ad daxil edilməyib” mesajı göstər.
user_name=""
print("Ad daxil edilməyib" if not user_name else "Ugurlu")

# Task 9:
# İstifadəçidən 2 ədəd daxil et.
# Əgər ədədlər bərabərdirsə, “Ədədlər bərabərdir”, yoxsa “Ədədlər fərqlidir” yaz.
number1=123
number2=1223
print("Ədədlər bərabərdir" if number1==number2 else "Ədədlər fərqlidir")

# Task 10:
# İstifadəçidən il daxil et.
# Əgər il 4-ə bölünürsə, “Artıq ildir” çap et, yoxsa “Adi ildir” yaz.
year=16

if year % 4 == 0:
    print("Artıq ildir")
else:
    print("Adi ildir")