# CSS - 3. Ödev
[Patika.dev](https://www.patika.dev/tr) adresi üzerinden aldığım CSS Eğitimi içerisindeki 3. ödevimin kodlarını aşağıdaki listede görebilirsiniz.

## index.html

```html

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="images/faviconGoogle.ico">
    <link rel="stylesheet" href="style.css">
    <title>Google</title>
</head>
<body>
    <!-- sayfa tasarımını 5 farklı etiketin içinde tasarlayacağım. Semantik etiketler kullanacağım
    main etiketinin içinde; header, navigation, section(logo kısmı), article, article ve footer etiketleri yer alacak.
    -->
    <!-- main start -->
    <main class="main-style">
        <!-- header start -->
        <header class="header-style1 header-style2 header-style3">
            <!-- nav start -->
            <!-- gmail, görseller, mail hesabının sembolü ve menü kısmının  yer alacağı kısımlar -->
            <nav class="nav-style">
                <div class="fp fpx fp_2a">
                    <div class="fp-wx fp-dx">
                        <div class="fp_8d">
                            <div class="fp-c">
                                <a class="fp-v" href="https://mail.google.com/mail/&ogbl" target="_top" >
                                    Gmail
                                </a>
                            </div>
                            <div class="fp-c">
                                <a class="fp-v" href="https://www.google.com.tr/imghp?hl=tr&amp;ogbl" target="_top">Görseller</a>
                            </div>
                        </div>
                        <div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 328px; z-index: 991; height: 0px; 
                        margin-top: 57px; transition: height 0.3s ease-in-out 0s; right: 0px; margin-right: 4px;"><iframe role="presentation" 
                        frameborder="0" scrolling="no" name="app" src="https://ogs.google.com/u/0/widget/app?origin=https%3A%2F%2Fwww.google.com&amp;cn=app&amp;pid=1&amp;spid=538&amp;hl=tr" 
                        style="height: 100%; width: 100%; visibility: hidden;"></iframe></div>
                        <div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 372px;
                        z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div>
                        <div class="fp-pf">
                            <a href="#" >Oturum Açın</a>
                        </div>
                    </div>
                    
                </div>
            </nav>
            <!-- nav end -->
        </header>
        <!-- header end -->

        <!-- section start -->
        <!-- logonun geleceği kısım -->
        <section class="f-section">
            <div class="logo">
                <img src="images/logo.png" alt="Google">
            </div>
        </section>
        <!-- section end -->

        <!-- article  start-->
        <!-- arama çubuğu ve butonların yer alacağı kısım -->
        <article class="f-search">
            <div class="fp-s search-bar">
                <div class="sb-x">
                    <div class="sb-imagine">
                        <style data-iml="1666809353813">.CcAdNb{margin:auto}.QCzoEc{margin-top:3px;color:#9aa0a6}</style>
                        <div>
                            <span class="QCzoEc z1asCe MZy1Rb" style="height:20px;line-height:20px;width:20px">
                                <svg focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                    <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path>
                                </svg>
                            </span>
                        </div>
                    </div>
                    <div jscontroller="vZr2rb" class="a4bIc" jsname="gLFyf" jsaction="h5M12e;input:d3sQLd;blur:jI3wzf">
                        <style data-iml="1666809353813">.gLFyf{background-color:transparent;border:none;margin:0;padding:0;color:rgba(0,0,0,.87);
                            word-wrap:break-word;outline:none;display:flex;flex:100%;-webkit-tap-highlight-color:transparent;
                            margin-top:-37px;height:34px;font-size:16px;}
                            .minidiv .gLFyf{margin-top:-35px;}
                            .a4bIc{display:flex;flex:1;flex-wrap:wrap}.YacQv{color:transparent;flex:100%;white-space:pre;height:34px;font-size:16px;}
                            .YacQv span{background:url("/images/experiments/wavy-underline.png") repeat-x scroll 0 100% transparent;padding:0 0 10px 0;}
                        </style>
                        <div class="YacQv gsfi" jsname="vdLsw">

                        </div>
                        <input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text"
                        aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" 
                        autofocus="" role="combobox" spellcheck="false" title="Ara" value="" aria-label="Ara" 
                        data-ved="0ahUKEwiRsafbxP76AhUsRPEDHawKBXsQ39UDCAQ">
                    </div>
                    <div class="dRYYxd">
                        <style data-iml="1666809353813">
                            .dRYYxd{display:flex;flex:0 0 auto;margin-top:-5px;align-items:stretch;flex-direction:row}
                            .minidiv .dRYYxd{margin-top:0}
                        </style> 
                        <style data-iml="1666809353813">
                            .BKRPef{background:transparent;align-items:center;flex:1 0 auto;flex-direction:row;display:flex;cursor:pointer}
                            .vOY7J{background:transparent;border:0;align-items:center;flex:1 0 auto;cursor:pointer;display:none;
                            height:100%;line-height:44px;outline:none;padding:0 12px}
                            .M2vV3{display:flex}.ExCKkf{height:100%;color:#70757a;vertical-align:middle;outline:none}
                            .minidiv .vOY7J{line-height:32px}.minidiv .ExCKkf{width:20px}
                        </style>
                        <style data-iml="1666809353814">.BKRPef{padding-right:4px}
                            .ACRAdd{border-left:1px solid #dadce0;height:65%}
                            .ACRAdd{display:none}.ACRAdd.M2vV3{display:block}
                        </style>
                    <div jscontroller="PymCCe" jsname="RP0xob" class="BKRPef">
                        <div class="vOY7J" tabindex="0" jsname="pkjasb" aria-label="Temizle" role="button" 
                            jsaction="AVsnlb;rcuQ6b:npT2md" data-ved="0ahUKEwiRsafbxP76AhUsRPEDHawKBXsQ05YFCAU"> 
                            <span class="ExCKkf z1asCe rzyADb" jsname="itVqKe">
                                <svg focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                    <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z">

                                    </path>
                                </svg>
                            </span>
                        </div>
                        <span jsname="s1VaRe" class="ACRAdd">
                        </span>
                    </div>
                    <style data-iml="1666809353814">
                        .Umvnrc{flex:1 0 auto;display:flex;cursor:pointer;
                        align-items:center;border:0;background:transparent;outline:none;padding:0 8px;width:24px;line-height:44px}
                        .ly0Ckb{background:url('//www.gstatic.com/inputtools/images/tia.png') no-repeat center;
                        height:24px;width:24px;vertical-align:middle}
                        .yAnw3c{visibility:hidden}
                    </style>
                    <div jscontroller="Y9t9Sc" class="Umvnrc" aria-label="Harf çevirme aracı" role="button" tabindex="0" jsaction="h5M12e;rcuQ6b:npT2md">
                        <span class="ly0Ckb"><img class="yAnw3c" src="images/tia.png" tia_disable_swap="true" 
                            tia_field_name="q" jsname="JyIpdf" data-iml="1666809353814" data-atf="0" data-frt="0" tia_property="web">
                        </span>
                    </div>
                    <style data-iml="1666809353814">.XDyW0e{flex:1 0 auto;display:flex;cursor:pointer;
                        align-items:center;border:0;background:transparent;outline:none;padding:0 8px;width:24px;line-height:44px}
                        .goxjub{height:24px;width:24px;vertical-align:middle}
                        .minidiv .XDyW0e{line-height:32px}.minidiv .goxjub{width:20px;height:20px}
                    </style>
                    <div jscontroller="unV4T" class="XDyW0e" aria-label="Sesle arama yapın" role="button" tabindex="0" 
                    jsaction="h5M12e;rcuQ6b:npT2md" data-ved="0ahUKEwiRsafbxP76AhUsRPEDHawKBXsQvs8DCAY">
                    <svg class="goxjub" focusable="false" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path fill="#4285f4" d="m12 15c1.66 0 3-1.31 3-2.97v-7.02c0-1.66-1.34-3.01-3-3.01s-3 1.34-3 3.01v7.02c0 1.66 1.34 2.97 3 2.97z">
                        </path>
                        <path fill="#34a853" d="m11 18.08h2v3.92h-2z"></path>
                        <path fill="#fbbc05" d="m7.05 16.87c-1.27-1.33-2.05-2.83-2.05-4.87h2c0 1.45 0.56 2.42 1.47 3.38v0.32l-1.15 1.18z"></path>
                        <path fill="#ea4335" d="m12 16.93a4.97 5.25 0 0 1 -3.54 -1.55l-1.41 1.49c1.26 1.34 3.02 2.13 4.95 2.13 3.87 0 6.99-2.92 6.99-7h-1.99c0 2.92-2.24 4.93-5 4.93z"></path>
                    </svg>
                </div>
                <style data-iml="1666809353814">.nDcEnd{flex:1 0 auto;display:flex;cursor:pointer;
                    align-items:center;border:0;background:transparent;outline:none;padding:0 8px;width:24px;line-height:44px}
                    .Gdd5U{height:24px;width:24px;vertical-align:middle}.minidiv .nDcEnd{line-height:32px}.minidiv .Gdd5U{width:20px;height:20px}</style>
                    <div jscontroller="lpsUAf" jsname="R5mgy" class="nDcEnd" data-is-images-mode="false" data-propagated-experiment-ids="" 
                        aria-label="Görselle arama" role="button" tabindex="0" jsaction="rcuQ6b:npT2md;h5M12e" data-ved="0ahUKEwiRsafbxP76AhUsRPEDHawKBXsQhqEICAc">
                        <img class="Gdd5U" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDI0LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IlN0YW5kYXJkX3Byb2R1Y3RfaWNvbiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIKCSB4PSIwcHgiIHk9IjBweCIgd2lkdGg9IjE5MnB4IiBoZWlnaHQ9IjE5MnB4IiB2aWV3Qm94PSIwIDAgMTkyIDE5MiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMTkyIDE5MiIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxyZWN0IGlkPSJib3VuZGluZ19ib3hfMV8iIGZpbGw9Im5vbmUiIHdpZHRoPSIxOTIiIGhlaWdodD0iMTkyIi8+CjxnIGlkPSJhcnRfbGF5ZXIiPgoJPGNpcmNsZSBpZD0iRG90IiBmaWxsPSIjNDI4NUY0IiBjeD0iOTYiIGN5PSIxMDQuMTUiIHI9IjI4Ii8+Cgk8cGF0aCBpZD0iUmVkIiBmaWxsPSIjRUE0MzM1IiBkPSJNMTYwLDcydjQwLjE1VjEzNmMwLDEuNjktMC4zNCwzLjI5LTAuODIsNC44MnYwdjBjLTEuNTcsNC45Mi01LjQzLDguNzgtMTAuMzUsMTAuMzVoMHYwCgkJYy0xLjUzLDAuNDktMy4xMywwLjgyLTQuODIsMC44Mkg2NmwxNiwxNmg1MGgxMmM0LjQyLDAsOC42My0wLjksMTIuNDYtMi41MWMzLjgzLTEuNjIsNy4yOC0zLjk2LDEwLjE3LTYuODYKCQljMS40NS0xLjQ1LDIuNzYtMy4wMywzLjkxLTQuNzRjMi4zLTMuNCwzLjk2LTcuMjgsNC44MS0xMS40NGMwLjQzLTIuMDgsMC42NS00LjI0LDAuNjUtNi40NXYtMTJWOTYuMTVWODRsLTYtMTlsLTEwLjgyLDIuMTgKCQlDMTU5LjY2LDY4LjcxLDE2MCw3MC4zMSwxNjAsNzJ6Ii8+Cgk8cGF0aCBpZD0iQmx1ZSIgZmlsbD0iIzQyODVGNCIgZD0iTTMyLDcyYzAtMS42OSwwLjM0LTMuMjksMC44Mi00LjgyYzEuNTctNC45Miw1LjQzLTguNzgsMTAuMzUtMTAuMzVDNDQuNzEsNTYuMzQsNDYuMzEsNTYsNDgsNTYKCQloOTZjMS42OSwwLDMuMjksMC4zNCw0LjgyLDAuODJjMCwwLDAsMCwwLDBMMTQ5LDQ1bC0xNy01bC0xNi0xNmgtMTMuNDRIOTZoLTYuNTZINzZMNjAsNDBINDhjLTE3LjY3LDAtMzIsMTQuMzMtMzIsMzJ2MTJ2MjBsMTYsMTYKCQlWNzJ6Ii8+Cgk8cGF0aCBpZD0iR3JlZW4iIGZpbGw9IiMzNEE4NTMiIGQ9Ik0xNDQsNDBoLTEybDE2LjgzLDE2LjgzYzEuMjMsMC4zOSwyLjM5LDAuOTMsMy40NywxLjU5YzIuMTYsMS4zMiwzLjk3LDMuMTMsNS4yOSw1LjI5CgkJYzAuNjYsMS4wOCwxLjIsMi4yNCwxLjU5LDMuNDd2MEwxNzYsODRWNzJDMTc2LDU0LjMzLDE2MS42Nyw0MCwxNDQsNDB6Ii8+Cgk8cGF0aCBpZD0iWWVsbG93IiBmaWxsPSIjRkJCQzA0IiBkPSJNNDgsMTY4aDM5Ljg5bC0xNi0xNkg0OGMtOC44MiwwLTE2LTcuMTgtMTYtMTZ2LTIzLjg5bC0xNi0xNlYxMzZDMTYsMTUzLjY3LDMwLjMzLDE2OCw0OCwxNjh6CgkJIi8+CjwvZz4KPC9zdmc+Cg==" alt="Kamera ile arama" data-iml="1666809353814" data-atf="1" data-frt="0">
                    </div>
                </div>
                </div>
            </div>
            <div class="FPdoLc lJ9FBc">  
                <center> 
                    <input class="gNO89b" value="Google'da Ara" aria-label="Google'da Ara" name="btnK" 
                        role="button" tabindex="0" type="submit" data-ved="0ahUKEwiBhZXU2P76AhU5X_EDHfgOBQAQ4dUDCA0"> 
                    <input class="RNmpXc" value="Kendimi Şanslı Hissediyorum" aria-label="Kendimi Şanslı Hissediyorum" 
                    name="btnI" type="submit" jsaction="trigger.kWlxhc" data-ved="0ahUKEwiBhZXU2P76AhU5X_EDHfgOBQAQ19QECA4">  
                </center> 
            </div>
        </article>
        <!-- article end  -->

        <!-- article start -->
        <!-- sayfanın alt kısmındaki boşluğun yer alacağı kısım -->
        <article class="page-space">
        </article>
        <!-- article end -->

        <!-- footer start -->
        <!-- sayfanın en alt kısmının geleceği yer -->
        <footer class="footer-page">
            <div class="footer-cn">
                <span style="color: #70757a; font-size: 15px;">Türkiye</span>
            </div>
            <div class="footer-cnd">
                <div class="footer-ul">
                    <ul>
                        <li><a href="#">Hakkında</a></li>
                        <li><a href="#">Reklam</a></li>
                        <li><a href="#">İşletme</a></li>
                        <li><a href="#">Arama nasıl çalışır?</a></li>
                    </ul>
                </div>
                <div class="footer-text">
                    <a href="#">
                        <img class="leave" src="images/leave.png" width="12px" height="14px" class="Pb9hCb" alt="" data-atf="1" data-frt="0" >
                        <span>2007'den bu yana karbon nötr</span>
                    </a>        
                </div>
                <div class="footer-end">
                    <ul>
                        <li><a href="#">Gizlilik</a></li>
                        <li><a href="#">Şartlar</a></li>
                        <li><a href="#">Ayarlar</a></li>
                    </ul>
                </div>
            </div>
        </footer>
        <!-- footer end -->
    </main>
    <!-- main end -->
</body>
</html>
```

```css
body {
    height: 100%;
    margin: 0;
    padding: 0;
    font-family: arial,sans-serif;
    font-size: 14px;
}
.main-style{
    display: flex;
    flex-direction: column;
    height: 100%;
}
.header-style1{
    /* kullanılarak kapsayıcı içerisindeki öğelere artık esneklik vermeye başlayabiliriz. 
    Bu tanımla artık bu kapsayıcının esnek bir görünümde olduğunu belirtiyoruz. */
    display: flex;
    /* nesnelerin dikey eksende nasıl hizalanacaklarını belirler
    : center - Nesneler ortalı bir şekilde dikey olarak sıralanırlar.
     */
    align-items: center;
    padding: 6px;
}
.header-style2{
    height: 60px;
}
.header-style3{
    /* esnek kutu için büzülme faktörünü belirler.
    flex-shrink tanımlanmış eleman, esnek kapsayıcı eleman içindeki diğer elemanlara göre göreceli olarak nasıl büzüleceğini belirler. */
    flex-shrink: 0;
    box-sizing: border-box;
}
.nav-style{
    display: inline-block;
    flex-grow: 1;
    padding-left: 75%;
}

.fp.fpx{
    min-width: auto;
}
.fpx{
    height: 48px;
}
.fp_2a:not(.fp_Id) {
    font: 13px/27px Roboto,Arial,sans-serif;
    z-index: 986;
}

.fp-wx{
    box-sizing: border-box;
    height: 48px;
    line-height: normal;
    padding: 0 4px;
    flex: 0 0 auto;
}
.fp-dx{
    vertical-align: middle;
    white-space: nowrap;
    -webkit-box-align: center;
    align-items: center;
    display: flex;
}
div{
    display: block;
}
.fp_8d {
    font-family: arial,sans-serif;
    line-height: normal;
    padding-right: 15px;
}
.fp-c{
    display: inline-block;
    padding-left: 15px;
}
.fp-c .fp-v{
    display: inline-block;
    line-height: 24px;
    vertical-align: middle;
}
a.fp-v{
    color: black;
    text-decoration: none;
}
a:hover{
    text-decoration: underline;
}
.fe{
    position: relative;
}
.fe-q{
    display: inline;
}
.fe-z{
    padding: 4px;
    vertical-align: middle;
    display: inline-block;
}
.fe-z:first-child{
    padding-left: 4px;
}

.fp-pf {
    font-family: Google Sans,Roboto,Helvetica,Arial,sans-serif;    
    color:#fff;
    background-color: #1a73e8;
    width: 40%;
    margin-left: 10px;
    margin-right: 8px;
    padding: 9px 23px;
    text-align: center;
    border-radius: 3px;
    line-height: 16px;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 0.25px;
    vertical-align: middle;
    -webkit-border-radius: 5px;
    box-sizing: border-box; 
    text-decoration: none;

}
.fp-pf a{
    text-decoration: none;
    color: #fff;
}
.fp-pf:hover{
   background-color:  #164c92;
   transition: 0.3s;
}

.logo{
    display: flex;
    flex-direction: column;
    align-items: center;
}

.logo-x{
    min-height: 92px;
    max-height: 92px;
    position: relative;
    height: 100%;
    margin-top: 10px;
}

.f-section{
    padding: 5px;
}

.f-search{
    height: 140px;
    margin: 20px;
}
.fp-s{
    max-height: 160px;
    height: 140px;
    display: flex;
    align-items: center;
    flex-direction: column;
}

.search-bar{
    display: flex;
    /* z-index: 3; */
    height: 46px;
    background: #fff;
    border: 1px solid #dfe1e5;
    box-shadow: none;
    border-radius: 24px;
    margin: 0 auto;
    width: calc(632px + 6px);
    width: auto;
    max-width: 584px;
    margin-top: 6px;
}
.search-bar:hover{
    -webkit-box-shadow: 0px -1px 7px 1px rgba(145,140,145,0.37);
    -moz-box-shadow: 0px -1px 7px 1px rgba(145,140,145,0.37);
    box-shadow: 0px -1px 7px 1px rgba(145,140,145,0.37);
}
.sb-x{
    flex: 1;
    display: flex;
    padding: 5px 8px 0 14px;
    height: 44px;
    width: 582px;
}
.sb-imagine{
    display: flex;
    align-items: center;
    padding-right: 13px;
    margin-top: -5px;
}
.sb-ix{
    margin: auto;
}

.QCzoEc {
    margin-top: 3px;
    color: #9aa0a6;
}
.z1asCe {
    display: inline-block;
    fill: currentColor;
    height: 24px;
    line-height: 24px;
    position: relative;
    width: 24px;
    padding-left: 10px;
}
.z1asCe svg {
    display: block;
    height: 100%;
    width: 100%;
}
.a4bIc {
    display: flex;
    flex: 1;
    flex-wrap: wrap;
}
.YacQv {
    color: transparent;
    flex: 100%;
    white-space: pre;
    height: 34px;
    font-size: 16px;
}
.gLFyf {
    background-color: transparent;
    border: none;
    margin: 0;
    padding: 0;
    color: rgba(0,0,0,.87);
    word-wrap: break-word;
    outline: none;
    display: flex;
    flex: 100%;
    -webkit-tap-highlight-color: transparent;
    margin-top: -37px;
    height: 34px;
    font-size: 16px;
}
.dRYYxd {
    display: flex;
    flex: 0 0 auto;
    margin-top: -5px;
    align-items: stretch;
    flex-direction: row;
}
.vOY7J {
    background: transparent;
    border: 0;
    align-items: center;
    flex: 1 0 auto;
    cursor: pointer;
    display: none;
    height: 100%;
    line-height: 44px;
    outline: none;
    padding: 0 12px;
}
.ExCKkf {
    height: 100%;
    color: #70757a;
    vertical-align: middle;
    outline: none;
}

.z1asCe {
    display: inline-block;
    fill: currentColor;
    height: 24px;
    line-height: 24px;
    position: relative;
    width: 24px;
}
.ACRAdd {
    display: none;
}

.ACRAdd {
    border-left: 1px solid #dadce0;
    height: 65%;
}
.Umvnrc {
    flex: 1 0 auto;
    display: flex;
    cursor: pointer;
    align-items: center;
    border: 0;
    background: transparent;
    outline: none;
    padding: 0 8px;
    width: 24px;
    line-height: 44px;
}
.ly0Ckb {
    background:url(images/tia.png);
    height: 24px;
    width: 24px;
    vertical-align: middle;
}
.yAnw3c {
    visibility: hidden;
    
}
.XDyW0e {
    flex: 1 0 auto;
    display: flex;
    cursor: pointer;
    align-items: center;
    border: 0;
    background: transparent;
    outline: none;
    padding: 0 8px;
    width: 24px;
    line-height: 44px;
}
.goxjub {
    height: 24px;
    width: 24px;
    vertical-align: middle;
}
.nDcEnd {
    flex: 1 0 auto;
    display: flex;
    cursor: pointer;
    align-items: center;
    border: 0;
    background: transparent;
    outline: none;
    padding: 0 8px;
    width: 24px;
    line-height: 44px;
}
.Gdd5U {
    height: 24px;
    width: 24px;
    vertical-align: middle;
}
input {
    writing-mode: horizontal-tb !important;
    text-rendering: auto;
    color: fieldtext;
    letter-spacing: normal;
    word-spacing: normal;
    line-height: normal;
    text-transform: none;
    text-indent: 0px;
    text-shadow: none;
    display: inline-block;
    text-align: start;
    appearance: auto;
    -webkit-rtl-ordering: logical;
    cursor: text;
    background-color: field;
    margin: 0em;
    padding: 1px 2px;
    border-width: 2px;
    border-style: inset;
    border-color: -internal-light-dark(rgb(118, 118, 118), rgb(133, 133, 133));
    border-image: initial;
}
.lJ9FBc {
    height: 70px;
}

.FPdoLc {
    padding-top: 18px;
}

center {
    display: block;
    text-align: -webkit-center;
}
.lJ9FBc input[type="submit"], .gbqfba {
    background-color: #f8f9fa;
    border: 1px solid #f8f9fa;
    border-radius: 4px;
    color: #3c4043;
    font-family: arial,sans-serif;
    font-size: 14px;
    margin: 11px 4px;
    padding: 0 16px;
    line-height: 27px;
    height: 36px;
    min-width: 54px;
    text-align: center;
    cursor: pointer;
    user-select: none;
}
.gNO89b:hover{
    box-shadow: 0px 0px 0px 1px rgba(0,0,0,0.1);
    -webkit-box-shadow: 0px 0px 0px 1px rgba(0,0,0,0.1);
    -moz-box-shadow: 0px 0px 0px 1px rgba(0,0,0,0.1);
}
.RNmpXc:hover{
    box-shadow: 0px 0px 0px 1px rgba(0,0,0,0.1);
    -webkit-box-shadow: 0px 0px 0px 1px rgba(0,0,0,0.1);
    -moz-box-shadow: 0px 0px 0px 1px rgba(0,0,0,0.1);
}
.page-space{
    margin-top: -25px;
    width: 100%;
    height: 245px;
    flex-grow: 1;
    /* background-color: #1a73e8; */
}
.footer-page{
    background:#f2f2f2;
    width: 100%;
    height: auto

}
.footer-cn{
    width: 98%;
    height: 29px;
    background-color: #f2f2f2;
    border-bottom: 1px solid #dadce0;
    padding-left: 27px;
    padding-top: 10px;
    position: absolute;
    z-index: 2;
}
.footer-cnd{
    width: 1346px;
    height: 95px;
    display: flex;
    flex-wrap: wrap;
    padding: 0 10px;
    background-color: #f2f2f2;
}
.footer-text{
    width: auto;
    justify-content: center;
    display: flex;
    align-items: center;
    flex-direction: column;
    padding-top: 50px;
    padding-left: 60px;
    float: left;
}
.footer-text a{
    color: #70757a;
    text-decoration: none;
    font-size: 14px;
}
.footer-text a:hover{
    text-decoration: underline;
}
.leave{
    margin-right: 6px;
}
.footer-ul{
    height: auto;
    width: 500px;
    padding-top: 58px;
    float: left;
}
ul{
    list-style: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
}
li{ 
float: left;
}
li a{
    display: block;
    text-decoration: none;
    color: #70757a;
    padding: 8px 16px;
}
li a:hover{
    text-decoration: underline;
}
.footer-end{
    width: auto;
    padding-top: 58px;
    padding-left: 26%;
    float: left;
}
```
