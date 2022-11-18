# CSS - 2. Ödev
[Patika.dev](https://www.patika.dev/tr) adresi üzerinden aldığım CSS Eğitimi içerisindeki 2. ödevimin kodlarını aşağıdaki listede görebilirsiniz.

## index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="stlye.css">
    <title>Google</title>
</head>
<body>

    <div id="cerceve"><!--Genel Çerçeve Div-->
        <div>
            <img src="images/google.jpg" alt="google"><!--Resim Eklendi-->
        </div>
        <div id="arama">
            <p id="search">Search the web using Google! <br>
            <input type="text" style="width: 300px;"><br><!--Arama kutucuğu eklendi-->
            <input type="submit" value="Google Search"><!--Arama butonu-->
            <input type="submit" value="I'm feeling lucky!"></p><!--Küçükken de bu butonun ne işe yaradığını anlamamıştım hala anlamadım-->
        </div>
        <table id="altcerceve"> <!--Alt tarafı tablo haline getirdik-->
            <tr>
                <td id="left"> <!--Sol kutucuk-->
                    Special Searches<br>
                    <a href="#">Stanford Search</a><br>
                    <a href="#">Linux Search</a>
                    </td>
                <td id="center"><!--Ortadaki kutucuk-->
                    <a href="#">Help!</a><br>
                    <a href="#">About Google!</a><br>
                    <a href="#">Company Info</a><br>
                    <a href="#">Google! Logos</a><br>
                </td>
                <td id="right"><!--Sağ kutucuk-->
                    Get Google! <br>
                    updates monthly: <br>
                    <input type="text" placeholder="your e-mail"><br><!--Mail yazılması gereken text kısmına placeholder ile otoyazı ekledik-->
                    <input type="submit" value="Subscribe"><!--Abone olma butonu-->
                    <a href="#">Archive</a>
                </td>
            </tr>
        </table>
    </div>
    
</body>
</html>
```

## style.css

```css
#cerceve{
    text-align: center; /*En dış çerçeveyi ortaladık*/
}
img{
    margin-bottom: 1px;/*Resmin alt taraftaki oto-margin kısmını küçülttük*/
}
#search{/*Üst taraf ile alt tarafın arasındaki boşluğu küçültüyoruz*/
    margin-top: 1px;
    margin-bottom: 1px;
}
#arama{/*Arama kısmının arka planını ayarlıyor ve genişliğini duyarlı hale getiriyoruz*/
    background-color: rgb(206, 206, 206);
    width: 100%;
    margin-bottom: 1px;
}
#altcerceve{/*Alt tarafın etrafındaki boşluğunu küçültüyor ve genişliğini sayfaya duyarlı yapıyoruz*/
    margin: 1px;
    width: 100%;
}
#left{/*Alt sol tarafın arkaplan rengi ve padding ayarları*/
    background-color: #7EE5DA;
    padding: 7px;
    width: 37%;
}
#center{/*Alt orta tarafın arkaplan rengi ve padding ayarları*/
    background-color: #70CCC2;
    padding: 7px;
}
#right{/*Alt sağ tarafın arkaplan rengi ve padding ayarları*/
    background-color: #62B3AA;
    padding: 7px;
}
```
