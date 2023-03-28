from pyfiglet import Figlet
figlet = Figlet()
import sys
import random



if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
    figlet.setFont(font = sys.argv[2])
else:
    print("Invalid usage")
    sys.exit(1)


fonts = figlet.getFonts()

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font = font)
    #print(figlet.renderText(text))

text = input("Input: ")

print("Output: ")
print(figlet.renderText(text))
