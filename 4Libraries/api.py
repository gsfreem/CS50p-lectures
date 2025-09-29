import requests


def main():
    while True:
        query = input('Search the Art Institute of Chicago! ').strip()

        try:
            response = requests.get('https://api.artic.edu/api/v1/artworks/search', {'q': query})
            response.raise_for_status()
        except requests.HTTPError:
            print("Couldn't complete request!")
            pass
        else:
            content = response.json()
            for artwork in content["data"]:
                print(f'- {artwork['title']}')
            break
    
main()