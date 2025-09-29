student_list = ['Hermione', 'Harry', 'Ron']

student_dict = {
    'Hermione':'Gryffindor',
    'Harry':'Gryffindor',
    'Ron':'Gryffindor',
    'Draco':'Slytherin'}

student_listof_dict = [
    {'name':'Hermione', 'house':'Gryffindor', 'patronus':'Otter'},
    {'name':'Harry', 'house':'Gryffindor', 'patronus':'Stag'},
    {'name':'Ron', 'house':'Gryffindor', 'patronus':'Jack Russel Terrier'},
    {'name':'Draco', 'house':'Slytherin', 'patronus':None}]


def main():
   # for index in range(len(student_list)):
    #    print(index + 1, student_list[index])

    #for student in student_dict:
    #    print(student, student_dict[student], sep=': ')

    for item in student_listof_dict:
        print(f'{item['name']}: House - {item['house']}, Patronus - {item['patronus']}')





if __name__ == '__main__':
    main()