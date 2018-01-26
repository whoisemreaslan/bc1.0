# -*- coding: utf-8 -*-

import sys
import keyword
import os
import unicodedata
import time

#import yeri

print("")
print("""
   [H]========[BLINKCURSOR]=======[-][o][x]
    |                                   
    |     Programa Hoşgeldiniz!        
    |           Sürüm v1.0              
    |			EMRE ASLAN              
    |=====================================
    """)
print("")

#giriş

kullanici = raw_input("    [ > ] Kullanıcı Adı Giriniz : ")
time.sleep(1)

#kullanıcı sorgusu

print("")
print("    [ + ] Hoşgeldin " + " " + kullanici) 
print("")
time.sleep(1)

#karşılamna

print("    [ + ] Bulunan Dizin Yetkileri Listeleniyor.")
time.sleep(1)
print("")
__import__("os").system("ls -l")
time.sleep(0.5)

#dizin hakları gösterimi 

print("")

menu = """
   [H]========[BLINKCURSOR]=======[-][o][x]
    |                                 
    |     Program Menusu      	  
    |                          		         
    |1-) Çık					      
    |2-) Port Taraması                     
    |3-) Araç Kutusu
    |4-) Metasploit
    |5-) Paket Analiz
    |6-) Zaafiyet Tarama(Basic)
    |7-) SQL İnjection(Basic)                    
    |====================================
    """
    
print(menu)

time.sleep(0.5)
print("")
secim = raw_input("    " + kullanici + "" "@bcursor:~$ ")
print("")
if secim == "1":
	sys.exit()
if secim == "2":
	hdfport = raw_input("    [ > ] Port Taraması Yapılacak Hedef : ")
	__import__("os").system("nmap" + " " + hdfport)
if secim == "3":
	__import__("os").system("setoolkit")
if secim == "4":
	__import__("os").system("msfconsole")
if secim == "5":
	__import__("os").system("wireshark")
if secim == "6":
	hdfsite = raw_input("    [ > ] Tarama Yapılacak Hedef : ")
	__import__("os").system("nikto -host" + " " + hdfsite)
if secim =="7":
	sqlsite = raw_input("    [ > ] SQL Zaafiyetinin Olduğu Url'i Giriniz : ")
	__import__("os").system("sqlmap -u" + " " + sqlsite + " " + "--dbs")

