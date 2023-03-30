import requests
from bs4 import BeautifulSoup

# Kontrol edilecek web sitesi
url = "https://example.com/example/"

# Web sitesinin kaynağını indirin
response = requests.get(url)

# Kaynak kodunu Beautiful Soup nesnesine dönüştürün
soup = BeautifulSoup(response.content, "html.parser")

# <a> tag'lerini alın
links = soup.find_all("a", class_="blog-thumb")

# <a> tag'lerinin href özelliklerini son_blog_thumb.txt dosyasına yazdırın
with open("linklog.txt", "w") as f:
    for link in links:
        href = link.get("href")
        if href:
            f.write(href + "\n")

# Son <a> tag'lerinin href değerlerini bir dosyada tutun ve okuyun
with open("linklog.txt", "r") as f:
    son_h1 = f.readlines()

# Eğer son <a> tag'lerinin href değerleri değiştiyse, yeni href değerlerini yazdırın
for i in range(len(links)):
    href = links[i].get("href")
    if href:
        if i >= len(son_h1):
            son_h1.append("\n")
        if href != son_h1[i].strip():
            print("Web sitesi güncellendi! Yeni href değeri: " + href)

            # Yeni href değerlerini bir dosyada saklayın
            son_h1[i] = href + "\n"
            with open("linklog.txt", "w") as f:
                f.writelines(son_h1)

# Güncelleme yapılmadıysa
if "Web sitesi güncellendi!" not in locals():
    print("Web sitesi güncel değil.")