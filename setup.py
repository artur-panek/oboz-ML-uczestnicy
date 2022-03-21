#!/usr/bin/python3
# skrypcior na instalowanie by AP & MG
import os
import sys
import subprocess
import pkg_resources
from zipfile import ZipFile
import shutil

print("Dzięki współpracy pewnych dwóch typków nie musisz recznie instalowac bibliotek ani pobierać ręcznie plików.")
input("A teraz klikaj enter i patrz jak sie instalują")

def ulepsz_pip():
    try:
        os.system("python -m pip install --upgrade pip")
    except:
        os.system("pip install --upgrade pip")

def instaluj_paczki():
    required = {'pandas-profiling', 'jupyter', 'notebook', 'jupyterlab', 'numpy', 'sklearn', 'xgboost', 'matplotlib'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    if missing:
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', *missing])
        except:
            print("Coś nie pykło przy instalowaniu paczek")
            return 0
    else:
        print("Wszystkie paczki już zainstalowane mordko")
        return 1

def pobierz_pliki():
    link = "https://github.com/gmikx/oboz_pliki/archive/refs/heads/master.zip"

    try:
        subprocess.run(["curl", "-LJOs", link])
    except:
        print("Pobieranie plików się nie powiodło")
        return 0
    else:
        print("Pliki pobrane")

    try:
        with ZipFile("oboz_pliki-master.zip", 'r') as zip:
            zip.extractall()
    except:
        print("Rozpakowywanie nie powiodło się")
        return 0
    else:
        print("Pliki rozpakowane")

    try:
        os.mkdir("pliki_ml")
    except:
        print("Nie udało się utworzyć folderu")
        return 0
    else:
        print("Folder utworzony")

    try:
        src = os.getcwd() + "/oboz_pliki-master/dla_uczestnikow/test.ipynb"
        dst = "."
        shutil.move(src, dst)

        src = os.getcwd() + "/oboz_pliki-master/dla_uczestnikow"
        dst = os.getcwd() + "/pliki_ml"
        files = os.listdir(src)
        for file in files:
            shutil.move(f"{src}/{file}", dst)
    except:
        print("Przesuwanie plików nie powiodło się")
        return 0
    else:
        print("Pliki przeniesione")

    try:
        os.remove("oboz_pliki-master.zip")
        shutil.rmtree("oboz_pliki-master")
    except:
        print("Usuwanie zbędnych plików nie powiodło się")
        return 0
    else:
        print("Zbędne pliki usunięte")
        return 1

def main():
    ulepsz_pip()
    if instaluj_paczki() == 1 and pobierz_pliki() == 1:
        print("Wszystko pobrane i zainstalowane.")
    else:
        print("Coś się wysypało. Skontaktuj się z prowadzącymi (AP lub MG) i przeslij screena wydruku tego programu")
    input("Naciśnij dowolny przycisk by zakończyć... ")

if __name__ == "__main__":
    main()
