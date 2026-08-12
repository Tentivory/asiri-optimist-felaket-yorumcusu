#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AŞIRI OPTİMİST FELAKET YORUMCUSU v9.11.42
=========================================
Bu yazılım, insanlığın en karanlık anlarını
bir mutluluk patlamasına dönüştürmek için
geliştirilmiştir. Bilim insanları (ben)
tarafından onaylanmıştır.
"""

import random
import time
import sys

# Bilimsel olarak seçilmiş umut cümleleri (kaynak: rüyalarım)
UMUT_KATALOGU = [
    "çünkü bu, evrenin sana özel bir hediyesi olabilir (muhtemelen değil ama olsun)",
    "çünkü şimdi daha güçlü olacaksın... veya daha yorgun",
    "çünkü bu sayede hayat hikayen Netflix dizisi olacak",
    "çünkü yıldızlar bu gece senin için parlıyor (gerçekten, bak yukarı)",
    "çünkü bu olay, gelecekteki senin için bir anı olacak ve güleceksin (veya ağlayacaksın)",
    "çünkü en kötüsü geride kaldı... umarım",
    "çünkü bu, senin karakterini geliştirecek (karakter zaten yeterince gelişmişti)",
    "çünkü artık daha az şeye takılacaksın (çünkü daha büyük sorunların var)",
    "çünkü bu, seni gerçekten önemli olan şeylere odaklandıracak (mesela pizza)",
    "çünkü evren seni seviyor ve bu şekilde gösteriyor (evrenin sevgi dili biraz garip)",
    "çünkü bu deneyim seni bir efsaneye dönüştürecek",
    "çünkü en azından bugün sıkılmadın",
    "çünkü bu, seni daha yaratıcı çözümler bulmaya itecek",
    "çünkü her bulutun gümüş bir kenarı vardır (bu bulutun kenarı biraz karanlık ama)",
    "çünkü sen buna değersin... bekle, yanlış cümle. Sen bundan daha iyisin!"
]

DRAMATIK_GIRISLER = [
    "DİKKAT! DİKKAT! KÜRESEL OPTİMİZM SİSTEMİ AKTİF!",
    "Felaket algılandı. Umut motorları çalıştırılıyor...",
    "Karanlık güçler devrede. Işık kılıcı çekiliyor...",
    "Acil durum: Aşırı iyimserlik protokolü başlatıldı.",
    "Uyarı: Bu yorum sizi gülümsetebilir veya şaşırtabilir."
]

def dramatize_bekle(saniye=1.5):
    """Dramatik bekleme efekti"""
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print()

def yorumla(felaket):
    """Felaketi umuda çeviren ana fonksiyon"""
    print("\n" + "="*60)
    print(random.choice(DRAMATIK_GIRISLER))
    print("="*60)
    dramatize_bekle()
    
    print(f"\nGirdiğiniz felaket: '{felaket}'")
    dramatize_bekle(1)
    
    print("\nAnaliz ediliyor...")
    dramatize_bekle()
    
    print("Negatif enerji tespit edildi!")
    dramatize_bekle()
    
    print("Umut enjektörleri devreye sokuluyor...")
    dramatize_bekle()
    
    umut = random.choice(UMUT_KATALOGU)
    
    print("\n" + "*"*60)
    print(f"🌟 YORUM: Bu aslında harika bir şey, {umut}")
    print("*"*60)
    
    print("\n✅ Optimizm seviyesi: %99.9 (yuvarlama hatası olabilir)")
    print("✅ Mutluluk katsayısı: Aşırı yüksek")
    print("✅ Bilimsel kanıt: Yok ama hissiyat var\n")
    
    return True

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║     AŞIRI OPTİMİST FELAKET YORUMCUSU v9.11.42            ║
║     'Her şey yolunda... muhtemelen'                      ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) > 1:
        felaket = " ".join(sys.argv[1:])
        yorumla(felaket)
    else:
        print("Kullanım: python felaket_yorumcu.py 'başına gelen kötü şey'")
        print("Örnek: python felaket_yorumcu.py 'sabah alarmı çalmadı'")
        print("\nVeya interaktif mod için bir şey yazın (çıkmak için 'q'):\n")
        
        while True:
            try:
                felaket = input("Felaketinizi girin > ").strip()
                if felaket.lower() in ['q', 'quit', 'exit', 'çık']:
                    print("\nOptimizm sisteminden çıkılıyor...")
                    print("Unutma: Yarın daha iyi olacak. Veya olmayacak. Ama bugün gülümse!")
                    break
                if felaket:
                    yorumla(felaket)
                else:
                    print("Boş felaket kabul edilmez. Lütfen bir trajedi girin.")
            except KeyboardInterrupt:
                print("\n\nCtrl+C ile kaçmaya çalıştınız. Ama umut peşinizi bırakmaz!")
                break

if __name__ == "__main__":
    main()
