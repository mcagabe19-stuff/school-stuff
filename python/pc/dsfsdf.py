sozluk={"Bilim İnsanı":"Aziz Sancar","Şair":"Mehmet Akif Ersoy","Astronom":"Ali Kuşçu"}

meslekler=sozluk.copy()

print("Sözlük = ",sozluk)
print("Mesklekler = ",meslekler)

print("Sözlük Anahtarları = ",sozluk.keys())
print("Sözlük Değerleri = ",sozluk.values())

sozluk.clear()

print("Sözlük = ",sozluk)

sozluk={"Bilim İnsanı":"Aziz Sancar","Şair":"Mehmet Akif Ersoy","Astronom":"Ali Kuşçu"}

sozluk["Matematikçi"]="Cahit Arf"

print("Sözlük = ",sozluk)

print("Sözlüğün içinde Sanatçı = ","Sanatçı" in sozluk)

sozluk["Bilim İnsanı"]="Canan Dağdeviren"

print("Sözlük = ",sozluk)

print("Şair = ",sozluk["Şair"])
