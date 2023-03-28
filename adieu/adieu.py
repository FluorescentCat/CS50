import inflect
p = inflect.engine()

#def printfunction():
 #   if len(names) == 1:
 #       print("Adieu, adieu, to ", names[0])
  #  elif len(names) == 2:
 #       joinlist = p.join(names)
 #       print("Adieu, adieu, to ", joinlist)
 #   elif len(names) > 2:
  #      joinlist = p.join(names, final_sep=",")
  #      print("Adieu, adieu, to ", joinlist)

names = []


while True:
    try:
        name = input("Name: ").strip()
        names.append(name)

    except EOFError:
        print("\n")
        break


joinlist = p.join(names)
#print("Adieu, adieu, to ", joinlist) - does not work with cs50 check program
#print(f"Adieu, adieu, to {joinlist}")- works with check program
print("Adieu, adieu, to " + joinlist) # also works with check program
