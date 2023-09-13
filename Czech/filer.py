import shutil
import os
import owncloud

def volume(zdrojova_slozka : str, cilova_slozka : str):
    shutil.copytree(zdrojova_slozka, cilova_slozka)

def owncloud_nahrat(nazev_souboru : str, cesta_owncloud : str, uziv_jmeno : str, uziv_heslo : str, server : str):
    oc = owncloud.Client(server)
    oc.login(uziv_jmeno, uziv_heslo)
    oc.put_file(cesta_owncloud+nazev_souboru, nazev_souboru)
    link = oc.share_file_with_link(cesta_owncloud+nazev_souboru)
    return link.get_link()