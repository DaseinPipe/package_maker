#!/usr/bin/python3

from pathlib import Path
import os, sys


from zipfile import ZipFile
  
 
  
# package_maker_dirpath = Path('S{BASH_SOURCE[0]}').resolve().parent
package_maker_dirpath = os.path.dirname(os.path.realpath(__file__))


if package_maker_dirpath not in sys.path:
    sys.path.append(package_maker_dirpath)


venv_zipfile = os.path.join(package_maker_dirpath, 'venv.zip')
venv_folder = os.path.join(package_maker_dirpath, 'venv')

if not os.path.exists(venv_folder):
    if os.path.exists(venv_zipfile):
        with ZipFile(venv_zipfile, 'r') as zip:
            zip.extractall(path=venv_folder)
        

site_package_path = os.path.join(package_maker_dirpath, 'venv/lib/python3.8/site-packages')

if site_package_path not in sys.path:
    sys.path.append(site_package_path)
 


from package_maker.src.gui.gui_main import *


def run_GUI():
    run()


if __name__ == '__main__':   
    run()



