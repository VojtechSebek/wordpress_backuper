import subprocess
import shutil
import os

def dump(server : str, port : int, uzivatel : str, heslo : str, databaze : str, cilova_slozka : str):
    nazev_zalohy = databaze+"_zaloha.sql"
    command = f"mysqldump --host={server} --port={port} --user={uzivatel} --password={heslo} {databaze} > {nazev_zalohy}"
    subprocess.run(command, shell=True)
    shutil.copy(nazev_zalohy, cilova_slozka+nazev_zalohy)
    os.remove(nazev_zalohy)