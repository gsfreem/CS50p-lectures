months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

def main():
    while True:
        date = input('Date: ')

        # trys to format and print date in 'YYYY/MM/DD' format
        try:
            if '/' not in date: raise ValueError
            month, day, year = date.split('/')
            month = int(month.strip())
            day = int(day.strip())
            year = int(year.strip())
            if day > 31 or month > 12: raise ValueError
        except ValueError:
            pass
        else:
            return print(f'{year}-{month:02}-{day:02}')
        
        # trys to format and print date in 'Month DD, YYYY' format
        try:
            if ',' not in date: raise ValueError
            month, day, year = date.split(' ')
            month = month.strip().title()
            day = int(day.strip().removesuffix(','))
            year = int(year.strip())
            if day > 31 or month not in months: raise ValueError

        except ValueError:
            pass
        else: 
            month = months.index(month) + 1 
            return print(f'{year}-{month:02}-{day:02}')


main()