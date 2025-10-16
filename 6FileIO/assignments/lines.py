import sys

def main():
    
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        file = str(sys.argv[1])
        ext = ''.join(file[-3:])
        match ext:
            case '.py':
                print(file_length(file))
            case _:
                sys.exit('not a python file')
        
def file_length(file):
    file_length =[]

    try:
        with open(file) as script:
            lines = script.readlines()
            for line in lines:
                line = line.lstrip(" ")
                if line.startswith("#"):
                    pass
                elif line.isspace():
                    pass
                else: 
                    file_length.append(line)
    except FileNotFoundError:
            sys.exit('File Not Found')
    else:
        return len(file_length)


if __name__ == "__main__":
    main()