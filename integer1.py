#Uch xonali butun son berilgan. 
#Birlik va o'nlik raqamlarini almashtirish orqali berilgandan olingan butun sonni chiqaring (masalan, 123 132 ga o'zgartiriladi)
son = int(input("Uch xonali butun sonni kiriting: "))

birinchi_xona = son // 100
ikkinchi_xona = (son // 10) % 10
uchinchi_xona = son % 10

chap_raqam = birinchi_xona
birinchi_xona = uchinchi_xona
uchinchi_xona = chap_raqam

yangi_son = uchinchi_xona * 100 +  birinchi_xona*10+ ikkinchi_xona

print(f"Natija: {yangi_son}")