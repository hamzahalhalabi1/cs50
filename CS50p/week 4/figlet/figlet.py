import sys
from pyfiglet import Figlet

if len(sys.argv) == 1:
    # No command-line arguments, use a random font
    figlet = Figlet()
    font_info = "Random Font"
elif len(sys.argv) == 3 and (sys.argv[1] in ['-f', '--font']):
    # Two command-line arguments with -f or --font option
    font_name = sys.argv[2]
    figlet = Figlet(font=font_name)
    font_info = f"Font: {font_name}"
else:
    print("Usage: python script.py  # for random font\n"
          "       python script.py -f <font_name>  # for specific font")
    sys.exit(1)

s = input('Input: ')
print(f"{font_info}\n{figlet.renderText(s)}")
