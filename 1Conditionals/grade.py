score = int(input("Score: "))

def main():
    if 90 <= score <= 100:
        print("Grede: A")
    elif 80 <= score < 90:
        print("Grade: B")
    elif 70 <= score < 80:
        print("Grade: C")
    elif 60 <= score < 70:
        print("Grade: D")
    else:
        print("Grade: F")

main()