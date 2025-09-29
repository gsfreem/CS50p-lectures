grocery_list = {}

def main():
    
    while True:
        try:
            item = input().strip().upper()
            if item not in grocery_list:
                grocery_list.update({item: 1})
            elif item in grocery_list:
                grocery_list.update({item: grocery_list[item] + 1})
        except EOFError:
            break

    for item in sorted(grocery_list):
        print(grocery_list[item], item)

main()

