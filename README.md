# pertemuan15

# Web Scraping menggunakan python

> langkah pertama downlad dan instal library request terlebih dahulu di CMD(Comand prompt) menggunakan perintah
     
            pip install requests
            
PIP merupakan package manager untuk mengelola package dan modul pada python.

• Dengan menggunakan PIP, kita dapat menggunakan library yang tersedia bebas dari direktory package library python.

> lalu instal library beautifulsoap di CMD(Comand prompt) juga dengan menggunakan perintah

          pip intsal beautifulsoap4
          
![Screenshot (247)](https://user-images.githubusercontent.com/116137169/213136474-17dd5503-54b6-495c-b455-623e23b2f276.png)


setelah proses selesai masuklah ke aplikasi coding disini saya menggunakan aplikasi VISUAL STUDIO CODE

> lalu ketikan 
                     import requests
                     from bs4 import Beautiulsoup
                     page requests.get('LINK YANG AKAN DI SCRAPING')
                     
                     print(page.content)
                     

> disini saya menggunakan link https://jadwalsholat.org/jadwal-sholat/monthly.php?id=226

![Screenshot (248)](https://user-images.githubusercontent.com/116137169/213139062-4ad4fb69-67af-4ade-b8f7-936e3eb8d723.png)


> karena data belum lengkap dan cara mengekstrak semua tag disini saya menggunakan perulangan for 

> dan juga menggunkanan find_all
LANGKAH PERTAMA 

> masuk ke link klik kanan lalu inspect

![Screenshot (252)](https://user-images.githubusercontent.com/116137169/213142456-084bcee4-7b82-49bb-ad3d-88d81aeafc57.png)


# pilih yang mau anda tampilkan.Disini saya menggunakan table_navigasi karena ingin menampilkan codingan kota/daerah



![Screenshot (251)](https://user-images.githubusercontent.com/116137169/213143776-7fdb4aa2-7144-4c5b-bf82-475824539bae.png)

               import requests
               from bs4 import BeautifulSoup

               page = requests.get('https://jadwalsholat.org/jadwal-sholat/monthly.php')

               print(page.content)

              after_bs = BeautifulSoup(page.content, 'html.parser')
              find_data = after_bs.find_all(id="table_navigasi")

              for x in find_data:
               print(x.table)

> hasil run untuk melihat codingan
![Screenshot (250)](https://user-images.githubusercontent.com/116137169/213144775-b0978e8c-fc22-4585-af37-f4b21b794550.png)



# kasus jadwal sholat
![Screenshot (253)](https://user-images.githubusercontent.com/116137169/213145751-51889290-e6fd-465c-938f-3760f482fbbe.png)

> penjelasan  Dengan menggunakan library Python 'requests', codingan mengirim permintaan GET ke URL "https://jadwalsholat.org/jadwal-sholat/monthly.php?id=226"

yang merupakan halaman web yang berisi informasi jadwal sholat. Kemudian, dengan menggunakan library 'BeautifulSoup', codingan menganalisis konten halaman web yang didapat dari permintaan GET tersebut dengan menggunakan parser HTML.

