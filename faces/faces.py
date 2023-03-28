def convert(text):
    newtext = text.replace(":)", "🙂").replace(":(", "🙁")
    print(newtext)

def main():
    text = input("write something here")
    convert(text)

main()
