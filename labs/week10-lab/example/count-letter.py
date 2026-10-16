# เขียนโปรแกรม
# 1 รับค่าข้อความจากผู้ใช้ เป็นแปร str ชื่อ text
# 2 รับค่าอักขระที่ต้องการนับในข้อความ text
# 3 ดำเนินการนับอักขระตามที่ผู้ใช้ต้องการ และแสดงออกทางหน้าจอ

# ตัวอย่างหน้าจอ
# Input your text: Boonchoo Jitnupong
# Which character do you want to count: o
# 5 letters 'o' found in Boonchoo Jitnupong


print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input('Input your text: ')
x = input('Which character do you want to count: ')
for letter in text:
    if letter == x:
        count += 1
print(f"{count} letters 'l' found in '{text}'")


print("\n=== STRING METHODS ===")
text = "welcome to the world of python"

# Case methods
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")

# Search methods
print(f"Find 'world': {text.find('world')}")
print(f"Count 'o': {text.count('o')}")
print(f"Starts with 'welcome': {text.startswith('welcome')}")
print(f"Ends with 'python': {text.endswith('python')}")