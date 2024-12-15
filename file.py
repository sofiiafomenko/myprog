#!/usr/bin/env python

import requests
import random

tag = "interior"
data = [
    {
        "title": "Rastliny ako dekorácia interiéru",
        "content": "Rastliny dokážu oživiť každý priestor a priniesť kúsok prírody do interiéru. Vyberte si nenáročné druhy, ako sú zamiokulkas, monstera alebo sukulenty. Umiestnite ich na police, stoly alebo do závesných kvetináčov. Okrem estetického efektu pomáhajú rastliny čistiť vzduch a vytvárať príjemnú atmosféru.",
        "imageLink": "https://img.freepik.com/free-photo/loft-home-office-interior-design_53876-143117.jpg?t=st=1734299779~exp=1734303379~hmac=6f60cc0b88d8ff74c418fe11094ff395a8e2b3aca731d2a57ab95b4d9daeef61&w=1480",
        "author": "Sofiia Fomenko",
        "tags": [tag]
    },
    {
            "title": "Tipy na osvetlenie pre moderný interiér",
            "content": "Osvetlenie hrá kľúčovú úlohu v dizajne. Kombinujte rôzne zdroje svetla: hlavné stropné, náladové stolové lampy a bodové svetlá pre zvýraznenie detailov. Teplé biele svetlo vytvára útulnú atmosféru, zatiaľ čo studené svetlo je vhodné do pracovných priestorov. Dimery vám umožnia meniť intenzitu svetla podľa nálady.",
            "imageLink": "https://img.freepik.com/free-photo/living-room-scandinavian-interior-design_53876-146865.jpg?t=st=1734299813~exp=1734303413~hmac=3ebb172f87ad7772b6dfd3f74805662e01ca762293867c22eb58d71d3af2e4ff&w=1480",
            "author": "Sofiia Fomenko",
            "tags": [tag]
        },
        {
                "title": "Farby v interiéri: Ako vybrať tú správnu paletu",
                "content": "Farebná schéma je základným prvkom interiérového dizajnu. Pre pokojné prostredie zvoľte neutrálnu paletu – béžovú, sivú alebo bielu. Ak chcete dodať energiu, pridajte akcenty v teplých farbách, ako je žltá alebo oranžová. Nebojte sa experimentovať s kontrastmi, ale pamätajte na rovnováhu medzi farbami.",
                "imageLink": "https://img.freepik.com/free-photo/mockup-frames-living-room-interior-with-chair-decorscandinavian-style_41470-5148.jpg?t=st=1734299930~exp=1734303530~hmac=e02f810559d6c765def4a739e673b305b55974de8322a28f26ea9df035767b08&w=996",
                "author": "Sofiia Fomenko",
                "tags": [tag]
            },
            {
                    "title": "Škandinávsky štýl: minimalizmus s teplom domova",
                    "content": "Škandinávsky štýl je perfektný pre tých, ktorí milujú jednoduchosť a čistotu. Jeho základom sú biele steny, prírodné materiály a funkčný nábytok. Drevo, jemné textílie a rastliny vytvoria príjemnú a teplú atmosféru. Dôležité je vyhýbať sa zbytočným dekoráciám, aby priestor zostal vzdušný.",
                    "imageLink": "https://img.freepik.com/free-photo/gray-sofa-brown-living-room-with-copy-space_43614-954.jpg?t=st=1734299949~exp=1734303549~hmac=be8b3ac2c51b852d836b56ce6316c77617ab77915b24f631a35087d5de3f4efc&w=1380",
                    "author": "Sofiia Fomenko",
                    "tags": [tag]
                },
                {
                        "title": "Ako vytvoriť útulný priestor v malej bytovke",
                        "content": "Pre útulnú atmosféru v malej bytovke je dôležité správne usporiadanie priestoru. Používajte svetlé farby na steny a nábytok, aby miestnosť pôsobila väčšia. Zrkadlá pridajú hĺbku a odrazia svetlo. Kompaktný multifunkčný nábytok, ako rozkladacie stoly alebo skladacie postele, šetrí miesto. Nezabudnite na textílie – mäkké deky, vankúše a koberčeky dodajú pocit pohodlia.",
                        "imageLink": "https://img.freepik.com/free-photo/modern-luxury-authentic-dining-room-interior-design-with-blank-picture-frame_53876-128700.jpg?t=st=1734299987~exp=1734303587~hmac=ea8be397bbde8c444e6107f70590f09b179395d1805cbdada3da4255a5bff73b&w=1480",
                        "author": "Sofiia Fomenko",
                        "tags": [tag]
                    },
                    {
                        "title": "Minimalistický interiér: menej je viac",
                        "content": "Minimalizmus je o funkčnosti a čistote. Vytvorte interiér s jednoduchým nábytkom a neutrálnymi farbami – biela, sivá alebo pastelové odtiene sú ideálne. Každý kus nábytku by mal mať svoj účel. Dekorácie obmedzte na minimum, napríklad jednu výraznú vázu alebo obraz, ktorý dodá priestoru charakter.",
                        "imageLink": "https://img.freepik.com/free-photo/mid-century-modern-reading-nook-apartment_53876-132819.jpg?t=st=1734300130~exp=1734303730~hmac=eaed90420afd14440042476b2d9e01a038957168da6123791c6ef9deae79d44a&w=1480",
                        "author": "Sofiia Fomenko",
                        "tags": [tag]
                    },
                    {
                        "title": "Ako vytvoriť útulný priestor v malej bytovke",
                        "content": "Podkrovné priestory môžu byť výzvou, ale aj skvelou príležitosťou na kreatívny dizajn. Využite šikmé steny na úložné priestory alebo police. Svetlé farby a strešné okná dodajú podkroviu svetlo a vzdušnosť. Pridajte nízky nábytok, ako sú pohovky či nízke stolíky, aby ste zachovali proporcie priestoru.",
                        "imageLink": "https://img.freepik.com/free-photo/view-photo-frame-with-interior-home-decor_23-2149513975.jpg?t=st=1734300101~exp=1734303701~hmac=69c5b0a3db7aeba7b6d358702ad3e357cf26878bb294236df0419afd60731790&w=740",
                        "author": "Sofiia Fomenko",
                        "tags": [tag]
                    },

                    {
                        "title": "Industriálny štýl: surová elegancia",
                        "content": "Industriálny štýl je ideálny pre moderné byty. Vyznačuje sa odhalenými tehlovými stenami, kovovými prvkami a masívnym drevom. Kombinujte tmavé farby, ako je antracitová alebo čierna, s teplými odtieňmi dreva. Doplňte priestor závesnými lampami s kovovým tienidlom a pridajte veľké koberce pre rovnováhu.",
                        "imageLink": "https://img.freepik.com/free-photo/interior-modern-high-building-high-quality-photo_114579-12190.jpg?t=st=1734300290~exp=1734303890~hmac=2a26e74aafd7431d1c2db9cd306022e08b3e5395763c17a6072a96db17c7e5d7&w=1800",
                        "author": "Sofiia Fomenko",
                        "tags": [tag]
                    },



    # add more articles here
]


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py ...")
        sys.exit(1)

    try:
        delete = int(sys.argv[1])
    except ValueError:
        print("'delete' must be 0 or 1")
        sys.exit(1)

    if delete == 0:
        print("processing {} articles".format(len(data)))
        random.shuffle(data)
        for article in data:
            response = requests.post("https://wt.kpi.fei.tuke.sk/api/article", json=article)
            print(response.status_code)
    else:
        ids = [i['id'] for i in requests.get(f"https://wt.kpi.fei.tuke.sk/api/article?tag={tag}&max=200").json()["articles"]]
        for i in ids:
            response = requests.delete(f"https://wt.kpi.fei.tuke.sk/api/article/{i}")
            print(response.status_code)