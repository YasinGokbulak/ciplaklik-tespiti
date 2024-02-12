# Gerekli kütüphaneyi ekliyoruz.
from nudity import Nudity

# Fotoğrafın dosya yolunu belirtiyoruz.
image_path = "test.jpg"

# Nudity nesnemizi oluşturuyoruz.
nudity = Nudity()

# has() metodu çıplaklık var ise True döner, yok ise False döner.
is_nude = nudity.has(image_path)
print(is_nude)

# score() metodu 0-1 aralığında bir değer döner.
nudity_score = nudity.score(image_path)
print(nudity_score)

# Bu dosya test dosyasıdır.