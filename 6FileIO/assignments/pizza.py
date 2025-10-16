import sys
import csv
from tabulate import *

def main():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    else:
        menu_path = sys.argv[1]
        get_menu(menu_path)
        

def get_menu(path):
    f_menu = []
    if path.endswith('.csv'):
        try:
            with open(path) as menu:
                rows = menu.readlines()
                for row in rows:
                    row = row.strip("\n").split(',')
                    f_menu.append(row)
                    header = f_menu[0]
                    body = f_menu[1:]
                print(tabulate(body, header, tablefmt='grid'), end="\n")
        except FileNotFoundError:
            sys.exit('File Not Found')
    else:
        sys.exit('Not a .csv file')



if __name__ == '__main__':
    main()