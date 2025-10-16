import csv
import sys


def main():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    else:
        convert_file(sys.argv[1],sys.argv[2])

def convert_file(original_file, new_file):
    try:
        with open(original_file) as original, open(new_file, 'w') as new:
            reader = csv.DictReader(original)
            writer = csv.DictWriter(new, fieldnames=['first', 'last', 'house'], lineterminator="\n")

            writer.writeheader()

            for row in reader:
                last, first = row['name'].split(',')
                house = row['house']
                writer.writerow({'first': first.strip(" "), 'last': last, 'house': house})
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == '__main__':
    main()