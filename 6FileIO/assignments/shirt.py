import sys

def main():
    if len(sys.argv) < 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too few command-line arguments')
    else:
        convert_image(sys.argv[1], sys.argv[2])

def convert_image():
    ...


if __name__ == "__main__":
    main()