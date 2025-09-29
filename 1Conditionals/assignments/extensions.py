file = input('File name: ').strip().lower()

def main():
    if file.endswith('.gif'):
        print('image/gif')
    elif file.endswith('.jpg') or file.endswith('jpeg'):
        print('image/jpeg')
    elif file.endswith('.png'):
        print('image/png')
    elif file.endswith('.pdf'):
        print('application/pdf')
    elif file.endswith('.txt'):
        print('text/plain')
    elif file.endswith('.zip'):
        print('application/zip')
    else:
        print('application/octet-stream')

def othermain():  
    def findtype():
        match file[-4:]:
            case '.gif' | '.jpg' | 'jpeg' | '.png':
                return 'image'
            case '.pdf' | '.zip':
                return 'application'
            case '.txt':
                return 'text'
            case _:
                return 'application'
    def findext():
        match file[-4:]:
            case '.gif' | '.png' | '.pdf' | '.zip':
                return file[-3:]
            case '.jpg':
                return 'jpeg'
            case 'jpeg':
                return file[-4:]
            case '.txt':
                return 'plain'
            case _:
                return 'octet-stream'
    print(findtype(),"/", findext(), sep="")

main()