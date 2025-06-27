# Vokal NO Vokal
Bu proje, müzik dosyalarındaki vokal ve enstrümantal parçaları ayırmak için kullanılan bir Python uygulamasıdır.

## 🎯 Özellikler
- MP3 ve WAV formatındaki müzik dosyalarını işleyebilme
- Vokal ve enstrümantal parçaları otomatik ayırma
- Demucs AI modeli kullanarak yüksek kaliteli ses ayrıştırma
- Çoklu dosya desteği
## 📁 Proje Yapısı
```
.
├── downloads/           # İşlenecek 
müzik dosyalarının bulunduğu klasör
├── separated/          # Ayrıştırılmış 
ses dosyalarının çıktı klasörü
│   └── htdemucs/      # Demucs model 
çıktıları
└── main.py            # Ana uygulama 
dosyası
```
## 🚀 Başlangıç
### Gereksinimler
- Python 3.x
- FFmpeg
- Demucs
### Kurulum
1. Projeyi klonlayın:
```
git clone https://github.com/
kullaniciadi/vokalNOvokal.git
cd vokalNOvokal
```
2. Gerekli Python paketlerini yükleyin:
```
pip install -r requirements.txt
```
### Kullanım
1. İşlemek istediğiniz müzik dosyalarını downloads klasörüne yerleştirin
2. Ana programı çalıştırın:
```
python main.py
```
3. İşlem tamamlandığında, ayrıştırılmış dosyalar separated/htdemucs klasöründe oluşturulacaktır
## 📝 Lisans
Bu proje MIT lisansı altında lisanslanmıştır.

## ✨ Katkıda Bulunma
1. Bu projeyi fork edin
2. Feature branch'i oluşturun ( git checkout -b feature/AmazingFeature )
3. Değişikliklerinizi commit edin ( git commit -m 'Add some AmazingFeature' )
4. Branch'inizi push edin ( git push origin feature/AmazingFeature )
5. Pull Request oluşturun
## 📞 İletişim
Proje Sahibi - @github_kullaniciadiniz

Proje Linki: https://github.com/kullaniciadi/vokalNOvokal

⭐️ Bu projeyi beğendiyseniz yıldızlamayı unutmayın!