filmler = {
    "The Substance": {"puan":8.7,"tur":"body-horror", "yil":2024},
    "Alien":{"puan":8.5,"tur":"bilim kurgu","yil":1979},
    "Hereditary":{"puan":7.9,"tur":"korku","yil":2018},
    "whiplash":{"puan":8.5,"tur":"dram","yil":2014},
    "Barbie":{"puan":7.2,"tur":"komedi","yil":2023},
    "Get Out":{"puan":7.7,"tur":"korku","yil":2017}
}
print("TÜM FİLMLER :\n")
for isim, bilgi in filmler.items():
    puan = bilgi["puan"]
    tur = bilgi["tur"]
    yil = bilgi["yil"]
    print(f"- {isim} ({yil}) | Tür: {tur} | puan: {puan}")
     
iyi_filmler= [isim for isim, bilgi in filmler.items() if bilgi ["puan"] >=8 ]
print ("\n8 ve üzeri puan alan filmler: ")
print(iyi_filmler)

puanlar = [bilgi["puan"] for bilgi in filmler.values()]
ortalama_puan = sum(puanlar)/len(puanlar)
print(f"\nOrtalama Puan: {ortalama_puan: .2f}")

en_yuksek_puan= -1
en_yuksek_film = ""

en_dusuk_puan=100
en_dusuk_film=""
for isim,bilgi in filmler.items():
    puan=bilgi["puan"]
    if puan > en_yuksek_puan:
        en_yuksek_puan = puan
        en_yuksek_film=isim
    if puan < en_dusuk_puan:
        en_dusuk_puan = puan
        en_dusuk_film=isim
print(f"\n En yüksek puan: {en_yuksek_film} ({en_yuksek_puan})")
print(f"\n En düşük puan: {en_dusuk_film} ({en_dusuk_puan})")

yeni_iyi_filmler=[(isim, bilgi["yil"], bilgi["puan"]) for isim, bilgi in filmler.items() if bilgi["yil"]>=2020 and bilgi["puan"]>=7.5]
with open("yeni_iyi_filmler.txt","w",encoding="utf-8") as f:
    for isim,yil,puan in yeni_iyi_filmler:
        f.write(f"{isim} ({yil}) - Puan: {puan} \n")
print("\n2020 sonrası iyi filmler 'yeni_iyi_filmler.txt' dosyasına yazıldı.")
