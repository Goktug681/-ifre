import random

sifre="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

 
soru=int(input("Şifre uzunluğu ne olsun"))
sifreler=""

for i in range(soru):
    sifreler+=random.choice(soru)
print("Şifrenz",sifreler)

