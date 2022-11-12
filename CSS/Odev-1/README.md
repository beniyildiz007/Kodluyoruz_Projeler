# CSS - 1. Ödev
[Patika.dev](https://www.patika.dev/tr) adresi üzerinden aldığım CSS Eğitimi içerisindeki 1. ödevimin kodlarını aşağıdaki listede görebilirsiniz.

## index.html

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Patika - Ödev 1</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div>
		<div id='muzik'>
			Müzik Dükkanım
		</div>
		<div id='liste'>
			<ul>
				<li><a href="index.html">Anasayfa</a></li>
				<li><a href="urunlerimiz.html">Ürünlerimiz</a></li>
				<li><a href="hakkimizda.html">Hakkımızda</a></li>
			</ul>
		</div>
		<div id="anasayfa">
			Ana Sayfa
		</div>
		<div>
			<p id="anasayfa-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
			consequat. Duis aute irure dolor in reprehenderit in <a href="urunlerimiz.html">Ürünlerimiz</a> velit esse
			cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
			proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
		</div>
		<div id="muzik-aletleri">
			Sitemizde Bulunan Müzik Aletleri
		</div>

		<div id="aletler-liste">
			<ul>
				<li>Gitar</li>
				<li>Davul</li>
				<li>Piyano</li>
				<li>Keman</li>
			</ul>
		</div>
	</div>
</body>
</html>

```

## urunlerimiz.html

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Patika - Ödev 1</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

	<div>
		<div id='muzik'>
			Müzik Dükkanım
		</div>
		<div id='liste'>
			<ul>
				<li><a href="index.html">Anasayfa</a></li>
				<li><a href="urunlerimiz.html">Ürünlerimiz</a></li>
				<li><a href="hakkimizda.html">Hakkımızda</a></li>
			</ul>
		</div>
		<div id="anasayfa">
			Ürünlerimiz
		</div>
		<div id="urunler-liste">
			<ol>
				<li><img src="images/davul-clipart-musical-instruments-drum.png">
					<p>Clipart Musical Instruments davul <b>5000₺</b></p></li>
				<li><img src="images/davul-Snare-Drum.png">
					<p>Snare Black Drum Davul <b>4500₺</b></p></li>
				<li><img src="images/davul-transparent-drum-stick-drums.png">
					<p>Transparent Stick davul <b>12000₺</b></p></li>
				<li><img src="images/guitar-acoustic.png">
					<p>Akustik Gitar <b>3000₺</b></p></li>
				<li><img src="images/Guitar-Purple-Electric.png">
					<p>Mor Klasik Gitar<b>4500₺</b></p></li>
				<li><img src="images/guitar-red-white.png">
					<p>Kırmızı Klasik Gitar <b>5000₺</b></p></li>
				<li><img src="images/keman-classic.png">
					<p>Klasik Keman <b>5000₺</b></p></li>
				<li><img src="images/keman-double-bass-bow.png">
					<p>Double Bass Bow Keman <b>7000₺</b></p></li>
				<li><img src="images/keman-kirmizi.png">
					<p>Kırmızı Keman <b>8000₺</b></p></li>
				<li><img src="images/piano-angle-furniture.png">
					<p>Köşeye Oturan Piyano <b>18000₺</b></p></li>
				<li><img src="images/piano-clipart-black.png">
					<p>Clipart Siyah Piyano<b>15000₺</b></p></li>
				<li><img src="images/piano-foot-bass.png">
					<p>Ayak Destekli Piyano <b>17000₺</b></p></li>
			</ol>
		</div>

	</div>

</body>
</html>

```

## hakkimizda.html

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Patika - Ödev 1</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

	<div>
		<div id='muzik'>
			Müzik Dükkanım
		</div>
		<div id='liste'>
			<ul>
				<li><a href="index.html">Anasayfa</a></li>
				<li><a href="urunlerimiz.html">Ürünlerimiz</a></li>
				<li><a href="hakkimizda.html">Hakkımızda</a></li>
			</ul>
		</div>
		<div id="anasayfa">
			Hakkımızda
		</div>
		<div>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
			consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
			cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
			proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
		</div>
		<div>
			<p id="vizyon">Vizyonumuz</p>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
			consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
			cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
			proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
			consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
			cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
			proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
			consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
			cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
			proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
		</div>
		<div>
			<p id="vizyon">Misyonumuz</p>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
			consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
			cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
			proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
			consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
			cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
			proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
		</div>

	</div>

</body>
</html>

```


## style.css

```css
		#muzik{
			color: red;
			font-size: 30px;
			text-align: center;
			font-weight: bolder;
			margin: 20px;
		}
		#liste ul{
			list-style-type: none;
			display: inline;
			list-style: none;
			list-style-position: inside;
		}
		#liste li{
			display: inline;
			margin: 10px;
			list-style-position: inside;
		}
		#liste{
			list-style-position: inside;
			text-align: center;
		}
		#anasayfa{
			text-align: center;
			font-size: 20px;
			color: purple;
			font-weight: bold;
			margin: 10px;
		}
		body{
			font-family: Arial, Helvetica, sans-serif;
		}
		#muzik-aletleri{
			text-align: center;
			color: darkgreen;
			font-weight: bold;
		}
		#aletler-liste ul{
			list-style-type: disc;
			list-style-position: inside;
		}
		#aletler-liste{
			text-align: center;
		}
		#urunler-liste{
			text-align: center;
		}
		#urunler-liste li{
			list-style-position: inside;
		}
		img{
			width: 350px;
			height: 300px;
		}
		#vizyon{
			color: darkgreen;
			font-weight: bold;
		}


```

