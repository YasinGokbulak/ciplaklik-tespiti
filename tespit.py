# Gerekli kütüphaneleri tanımlıyoruz.
from nudity import Nudity
from PIL import Image, ImageFilter

# Fotoğrafın yolunu belirtiyoruz.
image_path = "test.jpg"

# Fotoğrafın açılmasını sağlıyoruz.
image = Image.open(image_path)

# Nudity nesnemizi oluşturuyoruz.
nudity = Nudity()

# has() metodu çıplaklık var ise True döner, yok ise False döner.
is_nude = nudity.has(image.path)

# Eğer çıplaklık varsa fotoğraf blurlanır.
if is_nude:
    image = image.filter(ImagFilter.GaussianBlur(radius=50))

# Fotoğrafı görüntüler.
image.show()