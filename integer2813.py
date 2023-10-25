#Hafta kunlari 1-dushanba, 2-seshanba 6-shanba, 7-yakshanba sifatida raqamlangan. 1 dan 365 gacha boʻlgan oraliqda K butun soni va 1 dan 7 gacha boʻlgan oraliqda N butun soni berilgan. 
#Yilning K-kuni uchun haftaning sonini toping, agar bu yil 1-yanvar haftaning N-kuni boʻlsa
K=int(input())
N=int(input())
Z= (N - 1) % 7 + 1
S= (Z + K ) % 7
print(S)