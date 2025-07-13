# ✅ Task 1:
# Verilmiş string dəyişəni üçün:
text = "Python Dili Öyrənmək Gözəldir"
# - uzunluğunu çap et
print(len(text))
# - bütün hərflərini kiçik hərfə çevir
print(text.lower())
# - bütün hərflərini böyük hərfə çevir
print(text.upper())




# ✅ Task 2:
# Aşağıdakı stringin əvvəlində və sonunda olan boşluqları sil və nəticəni çap et.
text2 = "   Salam Dünya!   "
print(text2.strip())
print(text2.lstrip())
print(text2.rstrip())

# ✅ Task 3: 
# Verilmiş cümlədə "python" sözünü "JavaScript" ilə əvəz et və hər sözün baş hərfini böyük yaz.
text3 = "python proqramlaşdırma dilidir"
replace_text=text3.replace("python", "JavaScript")
title_text=replace_text.title()
print(title_text)

# ✅ Task 4: 
# Verilmiş cümləni sözlərə böl və vergüllə ayrılmış formada birləşdir.
text4 = "Mən Python dilini öyrənirəm"
split_text=text4.split()
print(split_text)
join_text=", ".join(split_text)
print(join_text)

# ✅ Task 5: find(), count()
# Verilmiş stringdə "a" hərfinin:
# - ilk dəfə harada olduğunu tap
# - neçə dəfə təkrarlandığını tap
text5 = "salam dünya"
to_find=text5.find("a")
print(to_find)
count_text=text5.count("a")
print(count_text)

# ✅ Task 6: startswith(), endswith()
# Aşağıdakı string:
# - "Salam" ilə başlayır?
# - "dünya" ilə bitir?
text6 = "Salam, Python dünyası!"
print("Yes" if text6.startswith("Salam") else "NO")
print("Yes" if text6.endswith("dünya") else "NO")

# ✅ Task 7: isalpha(), isdigit(), isalnum()
# Aşağıdakı stringləri yoxla:
text7_1 = "Salam"
text7_2 = "12345"
text7_3 = "Python123"

# Hansı yalnız hərflərdən, hansı yalnız rəqəmlərdən, hansı hərf və rəqəmlərdən ibarətdir?
if text7_1.isalpha():
    print(f"'{text7_1}' yalnız hərflərdən ibarətdir.")
else:
    print(f"'{text7_1}' yalnız hərflərdən ibarət deyil.")

if text7_2.isdigit():
    print(f"'{text7_2}' yalnız rəqəmlərdən ibarətdir.")
else:
    print(f"'{text7_2}' yalnız rəqəmlərdən ibarət deyil.")

if text7_3.isalnum():
    print(f"'{text7_3}' hərf və rəqəmlərdən ibarətdir.")
else:
    print(f"'{text7_3}' hərf və rəqəmlərdən ibarət deyil.")


# ✅ Task 8: Bonus
# İstifadəçidən ad və soyad daxil etməsini istə.
# 1. Boşluqları sil
# 2. Hərflərin ilkini böyük et (title)
# 3. Adın uzunluğunu çap et
# 4. Adın ilk hərfini tap
# 5. Adda neçə "a" olduğunu say

full_name="  nise esgerova  "
strip_name=full_name.strip()
print(strip_name)
title_name=strip_name.title()
print(title_name)
len_name=len(title_name)
print(len_name)
first_letter=title_name[0]
print(first_letter)
count_letter=title_name.count("a")
print(count_letter)