import sys
from PIL import Image, ImageOps

def checkinput():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    elif len(sys.argv) == 3:
        if sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1]. endswith(".png"):
            file1, suffix1 = sys.argv[1].split(".")
            file2, suffix2 = sys.argv[2].split(".")
            if suffix1 == suffix2:
                return True
            else:
                print("Input and output have different extensions")
                sys.exit(1)
        else:
            print("Invalid input")
            sys.exit(1)

def main():
    checkinput()
    try:
        muppetimage = Image.open(sys.argv[1])
        shirtimage = Image.open("shirt.png")

        sizemuppet = muppetimage.size
        sizeshirt = shirtimage.size
        #print(sizemuppet, sizeshirt)

        #crop muppetimage
        croppedmuppet = ImageOps.fit(muppetimage, sizeshirt)
        sizecropped = croppedmuppet.size
        #print(sizecropped)

        # overlay images, second image is the mask that is placed on top of image1
        croppedmuppet.paste(shirtimage, shirtimage)

        # save overlayed image
        croppedmuppet.save(sys.argv[2])


    except FileNotFoundError:
        sys.exit(1)


if __name__ == "__main__":
    main()

