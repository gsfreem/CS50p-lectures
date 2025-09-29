from sys import argv, exit
# sys.argv is a global variable that individually stores every word that has been typed 
# into the command line
# exit is a function that both prints its argument and cancels the program from its line

def main1():
    # If your main functionality is hidden inside of a bunch or obscure error handeling
    # it might be hard to make sense of what is going on.
    # In this case sys.exit() helps with that
    if len(argv) < 2:
        exit('Too few arguments')
    elif len(argv) > 2:
        exit('Too many arguments')



    # because of sys.exit it is safe to assume that when the program reaches this line
    # there will be a value only in sys.argv[1]
    print('Hello! My name is', argv[1])


def main2():
    if len(argv) < 2:
        exit('Too few arguments')

    for arg in argv[1:]:    
        print('Hello! My name is', arg)









        

if __name__ == '__main__':
    main2()