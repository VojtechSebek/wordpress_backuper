https://hub.docker.com/r/vojtechsebek/wordpress_backuper

Hello GitHub users,

first things first, this is my first attempt to create some bigger python project and try to create docker image at the same time.
I tried to create Wordpress Backuper that will backup my Wordpress docker volume and dump my database and save it into my Owncloud Backups folder.
At the end it can send email with DKIM protocol in mind (You can disable both)
For now, there´s only Czech language avalible, so the first thing to do is translate it into English (Until 1 week)

IMPORTANT TO WORK :
You have to create configuration file (konfigurace.py) for it to work.
Guide is below...

------------------------------------------
Docker Compose ($ = Variables)  :
```
version: '3'
services:
  backuper:
    image: vojtechsebek/wordpress_backuper
    container_name: $Your_Container_Name
    volumes:
      - $Your_Volume_With_Wordpress:/home/WP
      - ./konfigurace.py:/home/konfigurace.py
      - ./key.pem:/home/key.pem
    networks:
      - $Your_Database_Network
```
------------------------------------------
Configuration (konfigurace.py)  :
```
zaloha_onzaceni = "Wordpress Website With Database"
dny_zalohy = [0] # 0 is Monday, 6 is Sunday (Array = You can have multiple days selected)
email = True
email_dkim = True
email_odesilatel = "mail@domain.net"
email_domena = "domain.net"
email_private_dkim_klic = "key.pem"
email_prijemce = "mail@domain.net"
email_dkim_selektor = "selector"
email_server = "smtp.domain.net"
email_port = 587
email_heslo = "********"
email_jmeno = "mail@domain.net"
owncloud_cesta = "Backups/"
owncloud_jmeno = "user"
owncloud_heslo = "********"
owncloud_url = "https://owncloud.domain.net/"
mysql_server = "database"
mysql_port = 3306
mysql_jmeno = "user"
mysql_heslo = "*********"
mysql_databaze = "specific_database"
```
------------------------------------------

TO DO :
- For now, there´s only Czech language avalible, so the first thing to do is transtlate it into English (Untill 1 week)
- Fix some bugs (description space issue)
- Create more ways to store backups (other volume, FTP, ...)
- Create better mail structure (HTML)
