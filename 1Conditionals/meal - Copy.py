def main():
    time = input('What time is it? ').strip()
    base10 = convert(time)

    if 7 <= base10 <= 8:
        print('breakfast time')
    elif 12 <= base10 <= 13:
        print('lunch time')
    elif 18 <= base10 <= 19:
        print('dinner time')

def convert(time):
    hours, minutes = time.split(':')
   
    h = int(hours)
    m = int(minutes)
   
    return (h + (m/60))

if __name__ == "__main__":
    main()