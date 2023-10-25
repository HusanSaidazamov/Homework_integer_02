#999 dan katta butun son berilgan. Butun sonni bo‘lishning bitta operatori va qolganini olish operatoridan foydalanib, 
#berilgan butun sonning minglik raqamini toping.
A= int(input("Butun sonni kiriting: "))

minglik_raqam = (A // 1000) % 10

print(f"Minglik raqam: {minglik_raqam}")