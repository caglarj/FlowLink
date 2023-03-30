# FlowLink

https://example.com/example/ kullanımında olan bir web sitesinde aşağıdaki örnekte yapılandırılmış bir class yapısına ve a tagine ait url'nin güncellenip güncellenmediğini kontrol eden bir eğitim script çalışmasıdır.  



```

örnek yapı : 

<!DOCTYPE html>
<html lang="en">
  <head>
    <title></title>
    <meta charset="UTF-8" />
    <meta name="example" content="" />
  </head>

  <body>
    <div>
        <div class="" id="">
            <div class="blog-thumb" id=""><a href="#"></a>
              </div>
          </div>
    </div>
  </body>
</html>

```



- ilk olarak, request modülü kullanılarak url değileninde belirtilen web sitenin kaynağı indirilir ve reposnse değişkenine atanır

```
response = requests.get(url)
```

- Ardından, BeatifulShop modülü kullanılarak reponse.content içeriği html.parsel ile ayrıştırılır ve soup değişkenine atanır.

```
soup = BeautifulSoup(response.content, "html.parser")
```

- links = soup.find*all("a", class*="blog-thumb") kullanılarak, sadece class\_="blog-thumb" özelliğine sahip a> taglerini alır ve links değişkenine atanır.

```
links = soup.find_all("a", class_="blog-thumb")
```

- ilk olarak, request modülü kullanılarak url değileninde belirtilen web sitenşin kaynağı indirilir ve reposnse değişkenine atanır.

```
response = requests.get(url)
```

- Ardından, BeatifulShop modülü kullanılarak reponse.content içeriği html.persel ile ayrıştırılır ve soup değişkenine atanır.

```
soup = BeautifulSoup(response.content, "html.parser")
```

- links = soup.find*all("a", class*="blog-thumb") kullanılarak, sadece class\_="blog-thumb" özelliğine sahip a> taglerini alır ve links değişkenine atanır.

```
links = soup.find_all("a", class_="blog-thumb")
```

- links değişkenindeki a> taglerinin href özellikleri for döngüsü kullara alarak linklog.txt dosyasına yazdırılır.

```
with open("linklog.txt", "w") as f:
    for link in links:
        href = link.get("href")
        if href:
            f.write(href + "\n")
```

- linklog.txt Dosyası açılır ve readlines() metodu kullanılarak.dosyadaki tüm satırlar Son_h1 bir etiketini atanır.

```
with open("linklog.txt", "r") as f:
    son_h1 = f.readlines()
```

- For döngüsü kullanılarak links değişkenindeki a> taglerinin href Özellikleri kontrol edilir. Eğer bir değişiklik varsa print() fonksiyonu kullanılarak web sitesi güncellendi. Yeni href değeri mesaja yazdırılır.

```
for i in range(len(links)):
  href = links[i].get("href")
    if href:
     if i >= len(son_h1):
        son_h1.append("\n")
         if href != son_h1[i].strip():
         print("Web sitesi güncellendi! Yeni href değeri: " + href)
```

- Eğer bir güncelleme yapılmışsa son_h1 Değişikliğindeki ilgili satır güncellenir ve linklog.Txt dosyasına yazdırılır.

```
son_h1[i] = href + "\n"
with open("linklog.txt", "w") as f:
    f.writelines(son_h1)

```

- Son olarak if koşulu kullanılarak güncelleme yapılmadıysa web sitesi güncel değil mesaja yazdırılır.

```
if "Web sitesi güncellendi!" not in locals():
    print("Web sitesi güncel değil.")
```

- Bu şekilde a taglerinin href özellikleri kontrol edilir ve güncellenir. Eğer bir güncelle yapılmışsa.Linklog.txt dosyasına yazılır.
