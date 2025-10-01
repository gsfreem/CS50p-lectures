import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
available_fonts = figlet.getFonts()


def main():

    if len(sys.argv) == 1:
        text = input('Input: ').strip()
        selected_font = Figlet(font=random.choice(available_fonts))
        print('Output:')
        print(selected_font.renderText(text))
    elif len(sys.argv) == 3:
        if sys.argv[1] != '-f' and sys.argv[1] != '--font': sys.exit('Invalid usage')
        if sys.argv[2] not in available_fonts: sys.exit('Invalid usage')
        text = input('Input: ').strip()
        selected_font = Figlet(font=sys.argv[2])
        print('Output:')
        print(selected_font.renderText(text))
    else:
        sys.exit('Invalid usage')

if __name__ == '__main__':
    main()