
shopping_list={}
shopping_list.clear()

while True:
    try:
        item = input()
        item = item.lower()
        if item in shopping_list:
            count = shopping_list[item]
            count += 1
            shopping_list[item] = count
            #print(shopping_list)
        else:
            shopping_list[item] = 1
            #print(shopping_list)
    except EOFError:
        break
    except KeyError:
        continue

sorted_shopping = dict(sorted(shopping_list.items()))

for item in sorted_shopping:
    print(sorted_shopping[item], item.upper())
