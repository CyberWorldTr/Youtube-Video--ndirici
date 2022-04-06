
from pytube import YouTube
#Önce Kütühaneyi İndir!!!

print("""

 .o88b. db    db d8888b. d88888b d8888b. db   d8b   db  .d88b.  d8888b. db      d8888b. 
d8P  Y8 `8b  d8' 88  `8D 88'     88  `8D 88   I8I   88 .8P  Y8. 88  `8D 88      88  `8D 
8P       `8bd8'  88oooY' 88ooooo 88oobY' 88   I8I   88 88    88 88oobY' 88      88   88 
8b         88    88~~~b. 88~~~~~ 88`8b   Y8   I8I   88 88    88 88`8b   88      88   88 
Y8b  d8    88    88   8D 88.     88 `88. `8b d8'8b d8' `8b  d8' 88 `88. 88booo. 88  .8D 
 `Y88P'    YP    Y8888P' Y88888P 88   YD  `8b8' `8d8'   `Y88P'  88   YD Y88888P Y8888D' 

__     __         _         _       __      ___     _                      _ _      _      _ 
db    db  .d88b.  db    db d888888b db    db d8888b. d88888b   db    db d888888b d8888b. d88888b  .d88b.    d888888b d8b   db d8888b. d888888b d8888b. d888888b  .o88b. d888888b 
`8b  d8' .8P  Y8. 88    88 `~~88~~' 88    88 88  `8D 88'       88    88   `88'   88  `8D 88'     .8P  Y8.     `88'   888o  88 88  `8D   `88'   88  `8D   `88'   d8P  Y8   `88'   
 `8bd8'  88    88 88    88    88    88    88 88oooY' 88ooooo   Y8    8P    88    88   88 88ooooo 88    88      88    88V8o 88 88   88    88    88oobY'    88    8P         88    
   88    88    88 88    88    88    88    88 88~~~b. 88~~~~~   `8b  d8'    88    88   88 88~~~~~ 88    88      88    88 V8o88 88   88    88    88`8b      88    8b         88    
   88    `8b  d8' 88b  d88    88    88b  d88 88   8D 88.        `8bd8'    .88.   88  .8D 88.     `8b  d8'     .88.   88  V888 88  .8D   .88.   88 `88.   .88.   Y8b  d8   .88.   
   YP     `Y88P'  ~Y8888P'    YP    ~Y8888P' Y8888P' Y88888P      YP    Y888888P Y8888D' Y88888P  `Y88P'    Y888888P VP   V8P Y8888D' Y888888P 88   YD Y888888P  `Y88P' Y888888P 

""")

#Kullanıcıya Link Sor
link = input("İndireceğiniz linki giriniz: ")
yt = YouTube(link)

#Detaylar
print("Başlık: ",yt.title)
print("Görüntüleme Sayısı: ",yt.views)
print("Video Uzunluğu: ",yt.length)
#Mümkün Olan En Yüksek Çözünürliği Al
ys = yt.streams.get_highest_resolution()

#İnrime Başlıyor
print("İndiriliyor...")
ys.download()
print("İndirme Tamamlandı!!")