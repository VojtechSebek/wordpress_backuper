import konfigurace as cf
import smtp as smtp
import datumacas as datumacas
import pocitadlo as pocitadlo
import filer as filer
import mysqldump as mysqldump
import shutil
import os
from time import sleep

# MOTD a Deklarace
print("BackUPer by Vojtěch Šebek")
print("Version : 1.6 (Czech)")
print("")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Funkce tvořící název záloy
def Nazev():
    global nazevsouboru
    global nazevzalohy
    nazevzalohy = "Záloha č."+cislo+" "+datumacas.aktualnidatumacas()+cf.zaloha_onzaceni
    nazevsouboru = "Zaloha c."+cislo+datumacas.aktualnidatumacasf()+cf.zaloha_onzaceni

# Funkce sloužící pro poslání e-mailu
def Email():
    smtp.poslatmail(cf.email_odesilatel, cf.email_dkim, cf.email_domena, cf.email_private_dkim_klic, cf.email_prijemce, nazevzalohy, nazevzalohy + " Byla úspěšně vytvořena! \n\n" + "LINK :" + link, cf.email_dkim_selektor, cf.email_server, cf.email_port, cf.email_jmeno, cf.email_heslo)

# Funkce sloužící pro číslování záloh pomocí souboru cislo.txt (je možno upravit manuálně)
def Cislo():
    global cislo
    cislo = pocitadlo.cislo("cislo.txt")
    return str(cislo)

# Hlavní funkce sloužící pro samotné zálohování a spouštění sekvenčních funkcí
def Zaloha():
    try:
        print(datumacas.aktualnidatumacas() + " [STATUS] - [###............] : Konfigurace načtena úspěšně")
        Cislo()
        Nazev()
        filer.volume("WP","tmp/Wordpress")
        mysqldump.dump(cf.mysql_server, cf.mysql_port, cf.mysql_jmeno, cf.mysql_heslo, cf.mysql_databaze, "tmp/")
        print(datumacas.aktualnidatumacas() + " [STATUS] - [######.........] : Zálohováno dle konfigurace")
        print(datumacas.aktualnidatumacas() + " [STATUS] - [#########......] : Přesun byl spuštěn")
        shutil.make_archive(nazevsouboru, 'zip', "tmp")
        global link
        link = filer.owncloud_nahrat(nazevsouboru+".zip", cf.owncloud_cesta, cf.owncloud_jmeno, cf.owncloud_heslo, cf.owncloud_url)
        if cf.email == True:
            Email()
        shutil.rmtree("tmp")
        os.remove(nazevsouboru+".zip")
        print(datumacas.aktualnidatumacas() + " [STATUS] - [############...] : Přesun byl dokončen")
    except Exception as error:
        print(datumacas.aktualnidatumacas() + " [ERROR (Záloha)] : " + error)
        sys.exit()
 
# Cyklus while bude detekovat dny zálohy a následně spustí funkci Zaloha()
while True:
    if datumacas.aktualniden() in cf.dny_zalohy:
        print(datumacas.aktualnidatumacas() + " [STATUS] - [...............] : Detekce proběhla úspěšně")
        Zaloha()
        print(datumacas.aktualnidatumacas() + " [STATUS] - [###############] : Záloha č."+cislo+" byla úspěšně vytvořena!")
        print(datumacas.aktualnidatumacas() + " [STATUS] - [###############] : [" + link + "]")
        sleep(86400)
    else:
        print(datumacas.aktualnidatumacas() + " [STATUS] : Detekce proběhla neúspěšně")
        sleep(21600)