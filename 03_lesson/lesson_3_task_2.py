from smartphone import Smartphone

catalog = [
    Smartphone ("Apple", "iPhone 14", "+7923 568 92 36"),
    Smartphone ("Samsung", "Galaxy S23 Ultra", "+7923 568 88 88"),
    Smartphone ("Google", "Pixel 7 Pro", "+7923 568 56 00"),
    Smartphone ("OnePlus", "11 Pro ", "+7923 568 89 98"),
    Smartphone ("Xiaomi", "Redmi Note 12", "+7923 568 11 11")
]
for smartphone in catalog:
 print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")