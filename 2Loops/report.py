spacecraft_data_table = [
    {'name': 'Voyager 1', 'distance': 163, 'speed':65.03},
    {'name': 'James Web Space Telescope', 'distance':.01, 'speed':34.27},
    {'name': 'Hubble Deep Space Telescope', 'distance':2, 'speed':35.18}]
def update_spacecraft():
    update = input('Would You like to update the table? Yes/No: ').strip().lower()
    if  update == 'yes' or update == 'y':
        name = input('What is the name of the new spacecraft? ')
        distance = float(input(f'What is the distance of {name}? '))
        speed = float(input(f'What is the speed of {name}? '))
        spacecraft_data_table.append({'name':name, 'distance':distance, 'speed':speed})
        print()
        print('!!Updated!! List of active spacecraft:')
        print()
        indexes = range(len(spacecraft_data_table))
        for index in indexes:
            spacecraft_data = spacecraft_data_table[index]
            print(index + 1, spacecraft_data['name'])
        print()
    else:
        print()
        print('List of active spacecraft:')
        print()
        indexes = range(len(spacecraft_data_table))
        for index in indexes:
            spacecraft_data = spacecraft_data_table[index]
            print(index + 1, spacecraft_data['name'])
        print()
def create_report(key):
    spacecraft_data = spacecraft_data_table[key]
    print(f"""
Name: {spacecraft_data.get('name', 'unknown')}
Distance: {spacecraft_data.get('distance', 'unknown')} AU
Speed: {spacecraft_data.get('speed', 'unknown')} km/s
""")   
def format_report():
    lookup_keys = input('Which spacecraft would you like a report on? Seperate each lookup key with a comma or type "all": ')    
    if lookup_keys == 'all':
        print('======== REPORT ========')
        for number in range(len(spacecraft_data_table)):
            create_report(number)
        print('========================')
    else:
        lookup_keys.strip().split(', ')
        print()
        print('======== REPORT ========')
        for number in lookup_keys:
            key = int(number)
            create_report(key -1)
        print('========================') 
if __name__ == '__main__':
    update_spacecraft()
    format_report()