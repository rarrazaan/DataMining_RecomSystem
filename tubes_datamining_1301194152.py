# -*- coding: utf-8 -*-
"""Tubes_DataMining_1301194152.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IyJfvoHz9BkbHccIVkMpXhu2T3nqVN9G
"""

pip install langdetect

import gdown
import pandas as pd
import numpy as np
from langdetect import detect
from langdetect import DetectorFactory
import time

!gdown --id 11AGD_fMpTlUQT9dcddV1i-oOvi80wFAw
!gdown --id 19HRNiBozT45JAGr3Ja8ds8zo8hTkz1fv
!gdown --id 1PDE0Hrkqe_c1euTiuYTBcso_qvbd7A-i

## Mendeteksi bahasa dari judul buku
items = pd.read_csv('items.csv', sep = '|')
transactions = pd.read_csv('transactions.csv', sep = '|')
evaluation  = pd.read_csv('evaluation.csv')

items

print(items.isna().sum().sum())
print(transactions.isna().sum().sum())

## Item dengan title/judul yang pendek perlu dilakukan drop
count = 0
item_counter = 0

for title in items['title']:
    if (len(title) < 4):
        print('## Title: ', title)
        print("items = items.drop(", items.loc[count, 'itemID'], ')')
        item_counter = item_counter + 1
    count = count + 1

item_counter

## Drop item yang mengandung angka karena tidak bagus jika dilakukan deteksi bahasa
item_counter = 0
count = 0

for title in items['title']:
    if (any(char.isdigit() for char in title) and len(title) < 5):
        print('## Title: ', title)
        print("items = items.drop(", items.loc[count, 'itemID'], ')')
        item_counter = item_counter + 1
    count = count + 1
item_counter

## Di sini, saya menghapus item yang tidak dapat diproses oleh library language detection,
## seperti judul yang hanya berupa angka dan judul yang terlalu pendek. 
## Pengamatan dapat dimemasukkan kembali dengan bahasanya secara manual.
# count = 0
# for title in items['title']:
#     if (len(title) < 4 or (any(char.isdigit() for char in title) and len(title) < 5)):
#         items = items.drop(items.loc[count, 'itemID'])
#     count+=1

items.shape

## Di sini, saya menghapus item yang tidak dapat diproses oleh library language detection,
## seperti judul yang hanya berupa angka dan judul yang terlalu pendek. 
## Pengamatan dapat dimemasukkan kembali dengan bahasanya secara manual.

## Title: Ferris@Bruns_LLC
items = items.drop(21929)
## Title: Tajo@Bruns_LLC
items = items.drop(32694)
## Title: 1520-1522
items = items.drop(55539)
## Title: 1523-1526
items = items.drop(64005)

## Title:  Io
items = items.drop( 136 )
## Title:  Ava
items = items.drop( 831 )
## Title:  ABC
items = items.drop( 3677 )
## Title:  EMP
items = items.drop( 4022 )
## Title:  Hex
items = items.drop( 4465 )
## Title:  Wir
items = items.drop( 4814 )
## Title:  Boy
items = items.drop( 5054 )
## Title:  Oma
items = items.drop( 5156 )
## Title:  Nik
items = items.drop( 5698 )
## Title:  Kim
items = items.drop( 6260 )
## Title:  Pet
items = items.drop( 6407 )
## Title:  M
items = items.drop( 6999 )
## Title:  Äon
items = items.drop( 7000 )
## Title:  Ava
items = items.drop( 7509 )
## Title:  XX
items = items.drop( 7963 )
## Title:  Wir
items = items.drop( 7999 )
## Title:  Dry
items = items.drop( 8895 )
## Title:  Ash
items = items.drop( 8896 )
## Title:  FOX
items = items.drop( 11149 )
## Title:  Cut
items = items.drop( 12669 )
## Title:  ID
items = items.drop( 12974 )
## Title:  Ehi
items = items.drop( 12987 )
## Title:  ICE
items = items.drop( 13010 )
## Title:  We
items = items.drop( 13142 )
## Title:  Wir
items = items.drop( 13234 )
## Title:  Pax
items = items.drop( 13532 )
## Title:  Eve
items = items.drop( 13748 )
## Title:  Ye
items = items.drop( 15053 )
## Title:  Ral
items = items.drop( 15379 )
## Title:  Ten
items = items.drop( 15749 )
## Title:  Tin
items = items.drop( 20751 )
## Title:  Lie
items = items.drop( 26609 )
## Title:  KY
items = items.drop( 26723 )
## Title:  Sol
items = items.drop( 27164 )
## Title:  Eve
items = items.drop( 27296 )
## Title:  If
items = items.drop( 28475 )
## Title:  Ink
items = items.drop( 29260 )
## Title:  L
items = items.drop( 29902 )
## Title:  Zoe
items = items.drop( 30029 )
## Title:  Tex
items = items.drop( 30314 )
## Title:  Red
items = items.drop( 31667 )
## Title:  MAY
items = items.drop( 32187 )
## Title:  Aim
items = items.drop( 32830 )
## Title:  Son
items = items.drop( 33415 )
## Title:  L
items = items.drop( 33504 )
## Title:  Nil
items = items.drop( 33672 )
## Title:  Sie
items = items.drop( 34131 )
## Title:  Eva
items = items.drop( 34908 )
## Title:  Zel
items = items.drop( 35241 )
## Title:  Web
items = items.drop( 35451 )
## Title:  Hit
items = items.drop( 36713 )
## Title:  One
items = items.drop( 36886 )
## Title:  Mia
items = items.drop( 37465 )
## Title:  Sun
items = items.drop( 37739 )
## Title:  Sea
items = items.drop( 21159 )
## Title:  SHE
items = items.drop( 22397 )
## Title:  Run
items = items.drop( 22675 )
## Title:  Noa
items = items.drop( 22696 )
## Title:  Vet
items = items.drop( 22798 )
## Title:  NDI
items = items.drop( 23453 )
## Title:  Mud
items = items.drop( 23766 )
## Title:  COR
items = items.drop( 24594 )
## Title:  Hb
items = items.drop( 25835 )
## Title:  Fee
items = items.drop( 25957 )
## Title:  Tao
items = items.drop( 26453 )
## Title:  One
items = items.drop( 38315 )
## Title:  Up
items = items.drop( 38619 )
## Title:  Liv
items = items.drop( 38885 )
## Title:  Max
items = items.drop( 39320 )
## Title:  Run
items = items.drop( 39328 )
## Title:  Red
items = items.drop( 62262 )
## Title:  Jo
items = items.drop( 62777 )
## Title:  Tok
items = items.drop( 63018 )
## Title:  Ug
items = items.drop( 64328 )
## Title:  Vic
items = items.drop( 64507 )
## Title:  FOX
items = items.drop( 64785 )
## Title:  ISO
items = items.drop( 64919 )
## Title:  Lu
items = items.drop( 65886 )
## Title:  Fey
items = items.drop( 67625 )
## Title:  Fey
items = items.drop( 67628 )
## Title:  HPI
items = items.drop( 67743 )
## Title:  Air
items = items.drop( 68029 )
## Title:  Red
items = items.drop( 68476 )
## Title:  Mer
items = items.drop( 68490 )
## Title:  Zoo
items = items.drop( 68936 )
## Title:  Bee
items = items.drop( 69689 )
## Title:  PUP
items = items.drop( 70156 )
## Title:  Été
items = items.drop( 71858 )
## Title:  Jòn
items = items.drop( 71865 )
## Title:  Ble
items = items.drop( 71876 )
## Title:  Ete
items = items.drop( 71920 )
## Title:  Vèt
items = items.drop( 71933 )
## Title:  Buk
items = items.drop( 72131 )
## Title:  Kam
items = items.drop( 72461 )
## Title:  TBC
items = items.drop( 72583 )
## Title:  ERA
items = items.drop( 72846 )
## Title:  H2O
items = items.drop( 72850 )
## Title:  Kid
items = items.drop( 72901 )
## Title:  No!
items = items.drop( 73228 )
## Title:  VTT
items = items.drop( 73954 )
## Title:  Fix
items = items.drop( 74360 )
## Title:  Bec
items = items.drop( 74598 )
## Title:  Spy
items = items.drop( 39776 )
## Title:  Jim
items = items.drop( 40474 )
## Title:  A
items = items.drop( 41040 )
## Title:  Fir
items = items.drop( 41156 )
## Title:  GEN
items = items.drop( 41759 )
## Title:  Quo
items = items.drop( 41762 )
## Title:  Sky
items = items.drop( 42360 )
## Title:  Meh
items = items.drop( 42427 )
## Title:  Eco
items = items.drop( 42706 )
## Title:  Pug
items = items.drop( 43203 )
## Title:  A
items = items.drop( 43324 )
## Title:  May
items = items.drop( 45723 )
## Title:  I
items = items.drop( 46217 )
## Title:  Sue
items = items.drop( 46444 )
## Title:  Er?
items = items.drop( 46586 )
## Title:  Sin
items = items.drop( 47139 )
## Title:  Sam
items = items.drop( 47752 )
## Title:  Ohm
items = items.drop( 48500 )
## Title:  Bob
items = items.drop( 49109 )
## Title:  Aim
items = items.drop( 49184 )
## Title:  Few
items = items.drop( 49591 )
## Title:  A M
items = items.drop( 49704 )
## Title:  War
items = items.drop( 50112 )
## Title:  Z
items = items.drop( 50130 )
## Title:  Kim
items = items.drop( 51251 )
## Title:  Kim
items = items.drop( 52784 )
## Title:  ANK
items = items.drop( 52943 )
## Title:  ADA
items = items.drop( 53145 )
## Title:  Ink
items = items.drop( 54822 )
## Title:  KAT
items = items.drop( 55063 )
## Title:  The
items = items.drop( 55499 )
## Title:  ANA
items = items.drop( 55570 )
## Title:  PC
items = items.drop( 57219 )
## Title:  Ray
items = items.drop( 59436 )
## Title:  Nyx
items = items.drop( 59743 )
## Title:  Ka
items = items.drop( 59756 )
## Title:  Reg
items = items.drop( 60311 )
## Title:  Hex
items = items.drop( 60620 )
## Title:  ABC
items = items.drop( 60681 )
## Title:  TEA
items = items.drop( 61456 )
## Title:  Wi
items = items.drop( 61998 )
## Title:  Zoo
items = items.drop( 75554 )
## Title:  WTF
items = items.drop( 77324 )
## Title:  Kim
items = items.drop( 77674 )
## Title:  Now
items = items.drop( 77983 )
## Title: 6984
items = items.drop(67286)
## Title: 12
items = items.drop(69842)
## Title: 71%
items = items.drop(72536)
## Title: 4
items = items.drop(73961)
## Title:  BEX
items = items.drop( 17253 )
## Title:  Äon
items = items.drop( 18532 )
## Title:  Yo
items = items.drop( 18912 )
## Title:  ZPG
items = items.drop( 19360 )
## Title:  Liv
items = items.drop( 19716 )
## Title:  Q
items = items.drop( 19982 )
## Title:  Dig
items = items.drop( 20544 )
## Title: 381
items = items.drop(1282)
## Title: 1,2,3
items = items.drop(35645)
## Title: 110
items = items.drop(39581)
## Title: 43
items = items.drop(10749)
## Title: 17
items = items.drop(15555)
## Title: >
items = items.drop(67092)
## Title: 11
items = items.drop(25567)
## Title: !!
items = items.drop(31055)
## Title: 444
items = items.drop(44841)
## Title: 444
items = items.drop(44842)
## Title: 5:55
items = items.drop(40733)
## Title: 1906
items = items.drop(41657)
## Title: 1906
items = items.drop(41664)
## Title: 2030
items = items.drop(43450)
## Title: 2047
items = items.drop(43766)
## Title: 2049
items = items.drop(77770)
items = items.drop(124)
items = items.drop(582)
## Title: 1984
items = items.drop(736)
## Title: 1984
items = items.drop(3660)
## Title: 2034
items = items.drop(3871)
## Title: 2021
items = items.drop(6224)
## Title: 2037
items = items.drop(7458)
## Title: 2069
items = items.drop(10944)
## Title: 2121
items = items.drop(13490)
## Title: 2394
items = items.drop(13888)
## Title: 2121
items = items.drop(15060)
## Title: 2048
items = items.drop(15940)
## Title: 2121
items = items.drop(17732)
## Title: 1632
items = items.drop(21448)
## Title: 2145
items = items.drop(61473)
## Title: 1814
items = items.drop(23431)
## Title: 2012
items = items.drop(25479)
## Title: 2501
items = items.drop(48254)
## Title: 2060
items = items.drop(48905)
## Title: 5028
items = items.drop(50669)
## Title: 2084
items = items.drop(55060)
## Title: 2053
items = items.drop(55370)
## Title: 1712
items = items.drop(64441)
## Title: 2084
items = items.drop(64706)
## Title: 2625
items = items.drop(65362)
## Title: 2084
items = items.drop(66980)
## Title: 2156
items = items.drop(67283)

items.shape

## Menggunakan library langdetect untuk mendeteksi bahasa dari setiap item

DetectorFactory.seed = 0

items['bahasa'] = ''

myList = items['title']
bahasa = []

for text in myList:
    bahasa.append(detect(text))
    ##print(text)

items['bahasa'] = bahasa

items['bahasa']

# Export dataset baru yang sudah ditambahkan dengan kolom bahasa

items.to_csv('items_1.csv', index = False, header = True)

"""## Feature Engineer"""

df_items = pd.read_csv('items_1.csv')

## General topic 1 (karakter pertama dari main topic), general topic 2 (dua karakter pertama dari main topic),
## dan general topic 3 (tiga karakter pertama dari main topic)
df_items['general_topic'] = df_items['main topic'].astype(str).str[0]
df_items['general_topic_2'] = df_items['main topic'].astype(str).str[0:2]
df_items['general_topic_3'] = df_items['main topic'].astype(str).str[0:3]

## Mengkategorikan data berdasarkan general_topic, general_topic_2, dan general_topic_3
## Kategorikal dari masing-masing general topic mengambil referensi dari
## "Thema Subject Categories 1.4"
df_items['arts'] = np.where(df_items['general_topic'] == 'A', 1, 0)
df_items['language_linguistics'] = np.where(df_items['general_topic'] == 'C', 1, 0)

df_items['literature'] = np.where(df_items['general_topic'] == 'D', 1, 0)
df_items['poetry'] = np.where(df_items['general_topic_2'] == 'DC', 1, 0)

df_items['fiction'] = np.where(df_items['general_topic'] == 'F', 1, 0)
df_items['science_fiction'] = np.where(df_items['general_topic_2'] == 'FL', 1, 0)
df_items['fiction_fantasy'] = np.where(df_items['general_topic_2'] == 'FM', 1, 0)

df_items['reference'] = np.where(df_items['general_topic'] == 'G', 1, 0)

df_items['social_sciences'] = np.where(df_items['general_topic'] == 'J', 1, 0)
df_items['education'] = np.where(df_items['general_topic_2'] == 'JN', 1, 0)
df_items['politics_government'] = np.where(df_items['general_topic_2'] == 'JP', 1, 0)
df_items['warfare'] = np.where(df_items['general_topic_2'] == 'JW', 1, 0)

df_items['business'] = np.where(df_items['general_topic'] == 'K', 1, 0)
df_items['law'] = np.where(df_items['general_topic'] == 'L', 1, 0)
df_items['medicine'] = np.where(df_items['general_topic'] == 'M', 1, 0)
df_items['history'] = np.where(df_items['general_topic'] == 'N', 1, 0)

df_items['math_sciences'] = np.where(df_items['general_topic'] == 'P', 1, 0)
df_items['math'] = np.where(df_items['general_topic_2'] == 'PB', 1, 0)
df_items['astronomy'] = np.where(df_items['general_topic_2'] == 'PG', 1, 0)
df_items['physics'] = np.where(df_items['general_topic_2'] == 'PH', 1, 0)
df_items['chemistry'] = np.where(df_items['general_topic_2'] == 'PN', 1, 0)
df_items['biology'] = np.where(df_items['general_topic_2'] == 'PS', 1, 0)

df_items['philosophy_religion'] = np.where(df_items['general_topic'] == 'Q', 1, 0)
df_items['philosophy'] = np.where(df_items['general_topic_2'] == 'QD', 1, 0)
df_items['religion'] = np.where(df_items['general_topic_2'] == 'QR', 1, 0)

df_items['earth_sciences'] = np.where(df_items['general_topic'] == 'R', 1, 0)
df_items['geography'] = np.where(df_items['general_topic_2'] == 'RG', 1, 0)

df_items['sports'] = np.where(df_items['general_topic'] == 'S', 1, 0)
df_items['general_sports'] = np.where(df_items['general_topic_2'] == 'SC', 1, 0)
df_items['ball_sports'] = np.where(df_items['general_topic_2'] == 'SF', 1, 0)
df_items['athletics_gynastics'] = np.where(df_items['general_topic_2'] == 'SH', 1, 0)
df_items['equestrian'] = np.where(df_items['general_topic_2'] == 'SK', 1, 0)
df_items['vehicle_sports'] = np.where(df_items['general_topic_2'] == 'SM', 1, 0)
df_items['water_sports'] = np.where(df_items['general_topic_2'] == 'SP', 1, 0)
df_items['combat_sports'] = np.where(df_items['general_topic_2'] == 'SR', 1, 0)
df_items['field_sports'] = np.where(df_items['general_topic_2'] == 'SV', 1, 0)
df_items['outdoors'] = np.where(df_items['general_topic_2'] == 'SZ', 1, 0)

df_items['technology'] = np.where(df_items['general_topic'] == 'T', 1, 0)
df_items['agriculture'] = np.where(df_items['general_topic_2'] == 'TV', 1, 0)

df_items['computing'] = np.where(df_items['general_topic'] == 'U', 1, 0)

df_items['health'] = np.where(df_items['general_topic'] == 'V', 1, 0)
df_items['family_health'] = np.where(df_items['general_topic_2'] == 'VF', 1, 0)
df_items['self_help'] = np.where(df_items['general_topic_2'] == 'VS', 1, 0)
df_items['mind_body_spirit'] = np.where(df_items['general_topic_2'] == 'VX', 1, 0)

df_items['lifestyle_hobbies'] = np.where(df_items['general_topic'] == 'W', 1, 0)
df_items['cooking'] = np.where(df_items['general_topic_2'] == 'WB', 1, 0)
df_items['antiques'] = np.where(df_items['general_topic_2'] == 'WC', 1, 0)
df_items['quizzes_games'] = np.where(df_items['general_topic_2'] == 'WD', 1, 0)
df_items['crafts'] = np.where(df_items['general_topic_2'] == 'WF', 1, 0)
df_items['humour'] = np.where(df_items['general_topic_2'] == 'WH', 1, 0)
df_items['personal_style'] = np.where(df_items['general_topic_2'] == 'WJ', 1, 0)
df_items['home'] = np.where(df_items['general_topic_2'] == 'WK', 1, 0)
df_items['gardening'] = np.where(df_items['general_topic_2'] == 'WM', 1, 0)
df_items['nature'] = np.where(df_items['general_topic_2'] == 'WN', 1, 0)
df_items['travel_holiday'] = np.where(df_items['general_topic_2'] == 'WT', 1, 0)
df_items['stationary'] = np.where(df_items['general_topic_2'] == 'WZ', 1, 0)

df_items['graphic_novels'] = np.where(df_items['general_topic'] == 'X', 1, 0)
df_items['cartoons'] = np.where(df_items['general_topic_2'] == 'XY', 1, 0)

df_items['childrens'] = np.where(df_items['general_topic'] == 'Y', 1, 0)
df_items['childrens_young'] = np.where(df_items['general_topic_2'] == 'YB', 1, 0)
df_items['childrens_fiction'] = np.where(df_items['general_topic_2'] == 'YF', 1, 0)
df_items['childrens_educational'] = np.where(df_items['general_topic_2'] == 'YP', 1, 0)

## Mengkategorikan data berdasarkan bahasanya
## Hal ini dilakukan untuk 6 bahasa paling banyak

df_items['english'] = np.where(df_items['bahasa'] == 'en', 1, 0)
df_items['german'] = np.where(df_items['bahasa'] == 'de', 1, 0)
df_items['spanish'] = np.where(df_items['bahasa'] == 'es', 1, 0)
df_items['italian'] = np.where(df_items['bahasa'] == 'it', 1, 0)
df_items['french'] = np.where(df_items['bahasa'] == 'fr', 1, 0)
df_items['portuguese'] = np.where(df_items['bahasa'] == 'pt', 1, 0)

df_items['bahasa_lain'] = np.where(~np.isin(df_items['bahasa'], ['en', 'de', 'es', 'it', 'fr', 'pt']), 1, 0)

## Mengkategorikan data berdasarkan author/penulis nya
## Hal ini dilakukan untuk 50 author/penulis teratas yang ada pada dataset

df_items['GarciaSantiago']=np.where(df_items['author']=='Garcia Santiago',1,0)
df_items['ShelleyAdmont,KidkiddosBooks']=np.where(df_items['author']=='Shelley Admont, Kidkiddos Books',1,0)
df_items['JamesManning']=np.where(df_items['author']=='James Manning',1,0)
df_items['JulesVerne']=np.where(df_items['author']=='Jules Verne',1,0)
df_items['IdriesShah']=np.where(df_items['author']=='Idries Shah',1,0)
df_items['ErinHunter']=np.where(df_items['author']=='Erin Hunter',1,0)
df_items['EnidBlyton']=np.where(df_items['author']=='Enid Blyton',1,0)
df_items['R.L.Stine']=np.where(df_items['author']=='R. L. Stine',1,0)
df_items['TerryPratchett']=np.where(df_items['author']=='Terry Pratchett',1,0)
df_items['SpeedyPublishingLlc']=np.where(df_items['author']=='Speedy Publishing Llc',1,0)
df_items['H.G.Wells']=np.where(df_items['author']=='H. G. Wells',1,0)
df_items['RogerHargreaves']=np.where(df_items['author']=='Roger Hargreaves',1,0)
df_items['SteveHerman']=np.where(df_items['author']=='Steve Herman',1,0)
df_items['TuulaPere']=np.where(df_items['author']=='Tuula Pere',1,0)
df_items['DaisyMeadows']=np.where(df_items['author']=='Daisy Meadows',1,0)
df_items['ElBlokehead']=np.where(df_items['author']=='El Blokehead',1,0)
df_items['RoaldDahl']=np.where(df_items['author']=='Roald Dahl',1,0)
df_items['LewisCarroll']=np.where(df_items['author']=='Lewis Carroll',1,0)
df_items['AlfredBekker']=np.where(df_items['author']=='Alfred Bekker',1,0)
df_items['PenelopeDyan']=np.where(df_items['author']=='Penelope Dyan',1,0)
df_items['FionaWatt']=np.where(df_items['author']=='Fiona Watt',1,0)
df_items['MichelleM.Pillow']=np.where(df_items['author']=='Michelle M. Pillow',1,0)
df_items['L.FrankBaum']=np.where(df_items['author']=='L. Frank Baum',1,0)
df_items['MatildeCorreia']=np.where(df_items['author']=='Matilde Correia',1,0)
df_items['GinoBianchi']=np.where(df_items['author']=='Gino Bianchi',1,0)
df_items['NorbertPautner']=np.where(df_items['author']=='Norbert Pautner',1,0)
df_items['BrandonSanderson']=np.where(df_items['author']=='Brandon Sanderson',1,0)
df_items['CaroleMarsh']=np.where(df_items['author']=='Carole Marsh',1,0)
df_items['CarolynKeene']=np.where(df_items['author']=='Carolyn Keene',1,0)
df_items['MichaelMorpurgo']=np.where(df_items['author']=='Michael Morpurgo',1,0)
df_items['JenniferL.Armentrout']=np.where(df_items['author']=='Jennifer L. Armentrout',1,0)
df_items['DanGutman']=np.where(df_items['author']=='Dan Gutman',1,0)
df_items['RickRiordan']=np.where(df_items['author']=='Rick Riordan',1,0)
df_items['L.M.Montgomery']=np.where(df_items['author']=='L. M. Montgomery',1,0)
df_items['Thithiajobs']=np.where(df_items['author']=='Thithiajobs',1,0)
df_items['PeterHertzberg']=np.where(df_items['author']=='Peter Hertzberg',1,0)
df_items['JacquelineWilson']=np.where(df_items['author']=='Jacqueline Wilson',1,0)
df_items['GraceGoodwin']=np.where(df_items['author']=='Grace Goodwin',1,0)
df_items['CassandraClare']=np.where(df_items['author']=='Cassandra Clare',1,0)
df_items['LouisaMayAlcott']=np.where(df_items['author']=='Louisa May Alcott',1,0)
df_items['JeffKinney']=np.where(df_items['author']=='Jeff Kinney',1,0)
df_items['J.R.R.Tolkien']=np.where(df_items['author']=='J. R. R. Tolkien',1,0)
df_items['MaryPopeOsborne']=np.where(df_items['author']=='Mary Pope Osborne',1,0)
df_items['Panini']=np.where(df_items['author']=='Panini',1,0)
df_items['J.R.Ward']=np.where(df_items['author']=='J. R. Ward',1,0)
df_items['GeorgeR.R.Martin']=np.where(df_items['author']=='George R. R. Martin',1,0)
df_items['SaraShepard']=np.where(df_items['author']=='Sara Shepard',1,0)
df_items['JakeMaddox']=np.where(df_items['author']=='Jake Maddox',1,0)
df_items['MarkusHeitz']=np.where(df_items['author']=='Markus Heitz',1,0)
df_items['LincolnPeirce']=np.where(df_items['author']=='Lincoln Peirce',1,0)

## Meng-export dataframe yang akan dimasukkan kedalam model
df_items.to_csv('items_final_newer.csv', index = False, header = True)

"""## KNN"""

from sklearn.metrics.pairwise import euclidean_distances

def top_5_item(book, items):
    
    """
    
    Fungsi ini mengembalikan lima buku serupa teratas untuk buku tertentu dan 
    ukuran kesamaan. Fungsi ini mengambil argumen berikut:

    book: buku yang akan diberikan lima rekomnedasinya.
    
    items: dataframe yang berisi semua buku dengan featured engineer yang sesuai.

    
    """
    
    ## menyarin buku dengan judul yang sama namun dengan publisher yang berbeda
    temp = items[items['itemID'] == book]
    temp_title = items.loc[items['itemID'] == book, 'title']
    items = items[~np.isin(items['title'], temp_title)]
    items = pd.concat([temp, items]).reset_index(drop = True)
        
    ## Memilih buku berdasarkan kesamaan topik dan bahasa
    items = items[np.isin(items['bahasa'], temp['bahasa'])].reset_index(drop = True)
    
    if (items[np.isin(items['general_topic'], temp['general_topic'])].shape[0] > 5):
        if (sum(items['general_topic'] == 'Y') > 15000):
            
            if (all(temp['general_topic_2'] == 'YF') == False):
                
                if (items[np.isin(items['general_topic_2'], temp['general_topic_2'])].shape[0] < 6):
                    items = items[np.isin(items['general_topic'], temp['general_topic'])].reset_index(drop = True)
                
                else:
                    items = items[np.isin(items['general_topic_2'], temp['general_topic_2'])].reset_index(drop = True) 
           
            else:
                items = items[np.isin(items['general_topic_3'], temp['general_topic_3'])].reset_index(drop = True)

            
    ## Memilih variables of interest 
    to_remove = ['itemID', 'title', 'author', 'publisher', 'subtopics', 'general_topic', 'general_topic_2', 'general_topic_3', 'bahasa', 'main topic']
    variables_of_interest = items.columns[~np.isin(items.columns, to_remove)]
    items_temp = items[variables_of_interest]
        
    ## Memilih 5 buku rekomendasi
    D = euclidean_distances(items_temp)
    to_select = np.argsort(D[:, 0])[1:6]
            
        
    return [items.loc[to_select[0], 'itemID'], items.loc[to_select[1], 'itemID'], items.loc[to_select[2], 'itemID'], items.loc[to_select[3], 'itemID'], items.loc[to_select[4], 'itemID']]

def top_5_item_transaction(book, book_to_recommend, items):
    
    """
    
    Fungsi ini mengembalikan lima buku serupa teratas untuk buku tertentu, 
    buku dari riwayat transaksi, item, dan ukuran kesamaan. 
    Fungsi ini mengambil argumen berikut:
    
    book: buku yang akan diberikan lima rekomnedasinya.
    
    book_to_recommend: list buku dari riwayat transaksi.
    
    items: dataframe yang berisi semua buku dengan featured engineer yang sesuai.
    
    """
    
    ## Memilih buku berdasarkan transaksi
    items_temp = items.loc[np.isin(items['itemID'], book_to_recommend)]
    
    ## Memilih buku berdasarkan bahasa dan topik yang sama
    temp = items[items['itemID'] == book]
    temp_title = items.loc[items['itemID'] == book, 'title']
    
    items_temp = items_temp[~np.isin(items_temp['title'], temp_title)]
    items_temp = pd.concat([temp, items_temp]).reset_index(drop = True)
    
    ## Memilih buku berdasarkan bahasa
    items_temp = items_temp[np.isin(items_temp['bahasa'], temp['bahasa'])].reset_index(drop = True)
    
    ## memilih variables of interest
    to_remove = ['itemID', 'title', 'author', 'publisher', 'subtopics', 'general_topic', 'general_topic_2', 'general_topic_3', 'bahasa', 'main topic']
    variables_of_interest = items.columns[~np.isin(items.columns, to_remove)]
    items_temp_1 = items_temp[variables_of_interest]
    
    ## Sanity check 
    if (items_temp.shape[0] >= 6):
        
        ## Memilih 5 buku serupa teratas
        D = euclidean_distances(items_temp_1)
        to_select = np.argsort(D[:, 0])[1:6]

        return [items_temp.loc[to_select[0], 'itemID'], items_temp.loc[to_select[1], 'itemID'], items_temp.loc[to_select[2], 'itemID'], items_temp.loc[to_select[3], 'itemID'], items_temp.loc[to_select[4], 'itemID']]

    else:
        
        knn_top_5 = top_5_item(book, items)
        return knn_top_5

"""## Recommendation"""

def Book_Recommendation(items, transactions, evaluation):
    
    """
    
    Fungsi ini adalah fungsi utama yang memanggil fungsi lainnya. 
    Fungsi ini mengulang semua item dalam file evaluation dan memberikan 
    lima rekomendasi teratas. Fungsi ini mengambil argumen berikut:
    
    items: dataframe yang berisi semua buku dengan featured engineer yang sesuai.
    
    trasactions: dataframe yang berisi semua riwayat transaksi.
    
    evaluation: dataframe yang berisi itemID yang akan diberikan rekomendasinya.
    
    similarity_measure: nilai yang memungkinkan Euclidean, Cosine or Manhattan
    
    """
    
    ## Membuat kolom baru untuk rekomendasi
    evaluation['rec_1'] = np.nan
    evaluation['rec_2'] = np.nan
    evaluation['rec_3'] = np.nan
    evaluation['rec_4'] = np.nan
    evaluation['rec_5'] = np.nan
    
    ## Mendapatkan jumlah buku dalam evaluation
    n = evaluation.shape[0]
    
    for i in range(0, n):

        recommedations = recommendation(evaluation.loc[i, 'itemID'], transactions, items)
        evaluation.loc[i, 'rec_1'] = recommedations[0]
        evaluation.loc[i, 'rec_2'] = recommedations[1]
        evaluation.loc[i, 'rec_3'] = recommedations[2]
        evaluation.loc[i, 'rec_4'] = recommedations[3]
        evaluation.loc[i, 'rec_5'] = recommedations[4]
    
    evaluation['rec_1'] = evaluation['rec_1'].astype(int)
    evaluation['rec_2'] = evaluation['rec_2'].astype(int)
    evaluation['rec_3'] = evaluation['rec_3'].astype(int)
    evaluation['rec_4'] = evaluation['rec_4'].astype(int)
    evaluation['rec_5'] = evaluation['rec_5'].astype(int)

    return evaluation

def recommendation(book, transactions, items): 
    
    ## Mendeklarasikan list untuk menambahkan rekomendasi potensial
    book_to_recommend = []
    
    if (np.isin(book, [37378, 47675])):
        
        book_to_recommend = [55699, 78643, 23654, 58522, 74398]
        
        return book_to_recommend
    
    else:
        
        ## Mendapatkan rekomendasi berdasarkan order
        sessionID_order = transactions[(transactions['itemID'] == book) & (transactions['order'] > 0)]['sessionID'].values
        order_to_append = transactions[np.isin(transactions['sessionID'], sessionID_order)]['itemID'].values
        order_to_append = order_to_append[~np.isin(order_to_append, [book])]
        book_to_recommend.extend(order_to_append)    

        ## Mendapatkan rekomendasi berdasarkan basket
        sessionID_basket = transactions[(transactions['itemID'] == book) & (transactions['basket'] > 0)]['sessionID'].values
        basket_to_append = transactions[np.isin(transactions['sessionID'], sessionID_basket)]['itemID'].values
        basket_to_append = basket_to_append[~np.isin(basket_to_append, [book])]
        book_to_recommend.extend(basket_to_append)

        ## Mendapatkan rekomendasi berdasarkan click
        sessionID_click = transactions[(transactions['itemID'] == book) & (transactions['click'] > 0)]['sessionID'].values    
        click_to_append = transactions[np.isin(transactions['sessionID'], sessionID_click)]['itemID'].values
        click_to_append = click_to_append[~np.isin(click_to_append, [book])]
        book_to_recommend.extend(click_to_append)

        ## Mendapatkan rekomendasi berdasarkan list di atas
        to_append_next_layer = np.array(recommendation_help(book_to_recommend, transactions))
        to_append_next_layer = to_append_next_layer[~np.isin(to_append_next_layer, [book])]
        book_to_recommend.extend(to_append_next_layer)

        ## Running k-NN (5 nearest neighbors)
        book_to_recommend = top_5_item_transaction(book, book_to_recommend, items)
        
        return book_to_recommend

def recommendation_help(books, transactions):
    
    ## Mendeklarasikan list untuk menyimpan hasil
    results =  []
    
    ## Menentukan jumlah item
    n = len(books)
    
    for i in range(0, n):
        
        results.extend(helper(books[i], transactions))
        
    return results

def helper(book, transactions): 
    
    ## Mendeklarasikan list untuk menambahkan rekomendasi
    book_to_recommend = []
    
    ## Mendapatkan rekomendasi berdasarkan order
    sessionID_order = transactions[(transactions['itemID'] == book) & (transactions['order'] > 0)]['sessionID'].values
    order_to_append = transactions[np.isin(transactions['sessionID'], sessionID_order)]['itemID'].values
    order_to_append = order_to_append[~np.isin(order_to_append, [book])]
    book_to_recommend.extend(order_to_append)
        
    ##  Mendapatkan rekomendasi berdasarkan basket
    sessionID_basket = transactions[(transactions['itemID'] == book) & (transactions['basket'] > 0)]['sessionID'].values
    basket_to_append = transactions[np.isin(transactions['sessionID'], sessionID_basket)]['itemID'].values
    basket_to_append = basket_to_append[~np.isin(basket_to_append, [book])]
    book_to_recommend.extend(basket_to_append)
    
    ##  Mendapatkan rekomendasi berdasarkan click
    sessionID_click = transactions[(transactions['itemID'] == book) & (transactions['click'] > 0)]['sessionID'].values    
    click_to_append = transactions[np.isin(transactions['sessionID'], sessionID_click)]['itemID'].values
    click_to_append = click_to_append[~np.isin(click_to_append, [book])]
    book_to_recommend.extend(click_to_append)   
    
    return book_to_recommend

"""## Main Program"""

## read csv
items = pd.read_csv('items_final_newer.csv')

## Running book recommendation
recommendation = Book_Recommendation(items, transactions, evaluation)

recommendation

recommendation.to_csv('recommendation_result.csv', index = False, header = True)