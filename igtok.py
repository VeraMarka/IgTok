import requests
import random
from getuseragent import UserAgent
Y = '\033[92m'
S = '\033[93m'
K = '\033[91m'
M ='\033[94m'
E = '\033[0m'
P = '\033[95m'
print('\x1b[1;32m  ____________\n\x1b[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\n\x1b[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\n\x1b[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\x1b[1;33m\n\x1b[1;32m ╔════════════╗\x1b[1;33m\n\x1b[1;32m ╚════════════╝\x1b[1;33m\n\x1b[1;31m  ║\x1b[1;36m██████████\x1b[1;31m╚╗\x1b[1;33m\n\x1b[1;31m  ║\x1b[1;36m██\x1b[1;31m╔══╗\x1b[1;36m█\x1b[1;31m╔═╗\x1b[1;36m█\x1b[1;31m║\x1b[1;33m\n\x1b[1;31m  ║\x1b[1;36m██\x1b[1;31m║\x1b[1;33m╬\x1b[1;31m╔╝\x1b[1;36m█\x1b[1;31m╚╗║\x1b[1;36m█\x1b[1;31m║\x1b[1;33m\n\x1b[1;31m  ║\x1b[1;36m██\x1b[1;31m╚═╝\x1b[1;36m█\x1b[1;31m║\x1b[1;36m█\x1b[1;31m╚╝\x1b[1;36m█\x1b[1;31m║\x1b[0m The\n\x1b[1;31m  ╚╗\x1b[1;36m█████████\x1b[1;31m═╝ \x1b[0mBest\n\x1b[1;31m   ╚╗║╠╩╩╩╩╩╝   \x1b[0m\x1b[1;95m\n\x1b[1;31m    ║║╚╗\x1b[1;33m┈\x1b[1;34m█▐█████\x1b[1;31m▒\x1b[0m.｡oO\n\x1b[1;31m    ║\x1b[1;36m██\x1b[1;31m╠╦╦╦╗\n\x1b[1;31m    ╚╗\x1b[1;36m██████ \x1b[0mDeveloper \x1b[1;31m: \x1b[48;5;0;38;5;197mVera\n\x1b[1;31m     ╚════╝  \x1b[0mTool \x1b[1;31m: \x1b[1;92mİG LİKE + \x1b[1;97mTİKTOK VİEWS \x1b[1;91m\n \x1b[1;33m<══════════════════════════════════>\n\x1b[1;31m\n\n\x1b[1;97mİnsta\x1b[1;95m Veraildez\n')
def instagram_begeni():
    ua = UserAgent("ios").Random()
    user = input(M+'|✓| İnstagram Kullanıcı Adı Gir: '+S)
    link = input(M+'|✓| Gönderi Linki : '+S)
    res = requests.post('https://api.likesjet.com/freeboost/7',
                        json={"instagram_username": user,
                              "link": link,
                              "email": f"whisper{random.randint(100000,999999)}@gmail.com"},
                        headers={"Host": "api.likesjet.com",
                                 "content-length": "137",
                                 "sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"",
                                 "accept": "application/json, text/plain, */*",
                                 "content-type": "application/json",
                                 "sec-ch-ua-mobile": "?1",
                                 "user-agent": ua,
                                 "sec-ch-ua-platform": "\"Android\"",
                                 "origin": "https://likesjet.com",
                                 "sec-fetch-site": "same-site",
                                 "sec-fetch-mode": "cors",
                                 "sec-fetch-dest": "empty",
                                 "referer": "https://likesjet.com/",
                                 "accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5"})

    if res.status_code == 200:
        print(Y+"Beğeniler Gönderildi"+E)
    else:
        print(K+"Hata oluştu, beğeniler gönderilemedi."+E)

def tiktok_goruntulenme():
    ua = UserAgent("ios").Random()
    user = input(M+'|✓| TikTok Kullanıcı Adını Gir : '+S)
    link = input(M+'|✓| Videonun Linkini Gir : '+S)

    res = requests.post('https://api.likesjet.com/freeboost/3',
                        json={"link": link,
                              "tiktok_username": user,
                              "email": f"whisper{random.randint(100000,999999)}@gmail.com"},
                        headers={"Host": "api.likesjet.com",
                                 "content-length": "137",
                                 "sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"",
                                 "accept": "application/json, text/plain, */*",
                                 "content-type": "application/json",
                                 "sec-ch-ua-mobile": "?1",
                                 "user-agent": ua,
                                 "sec-ch-ua-platform": "\"Android\"",
                                 "origin": "https://likesjet.com",
                                 "sec-fetch-site": "same-site",
                                 "sec-fetch-mode": "cors",
                                 "sec-fetch-dest": "empty",
                                 "referer": "https://likesjet.com/",
                                 "accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5"})

    if res.status_code == 200:
        print(Y+"Görüntülenme Gönderildi!"+E)
    else:
        print(K+"Hata oluştu, görüntülenmeler gönderilemedi."+E)

choice = input(f"{P}１－） Ｉｎｓｔａｇｒａｍ Ｂｅğｅｎｉ\n２－） ＴｉｋＴｏｋ Ｇöｒüｎｔüｌｅｎｍｅ\n\n{M}İŞLEM SEÇ(1 - 2)： "+S)

if choice == "1":
    instagram_begeni()
elif choice == "2":
    tiktok_goruntulenme()
else:
    print(K+"Geçersiz seçim!"+E)
