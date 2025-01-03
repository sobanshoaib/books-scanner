import requests


def get_books(isbnNum):
    url_of_api = f"https://openlibrary.org/isbn/{isbnNum}.json"

    try:
        response = requests.get(url_of_api)
        check_code = response.status_code
        if check_code == 200:
            data = response.json()
            if isbnNum in data:
                title = data["title"]
                if "authors" in data:
                    author_info = data["authors"]["author"]["key"]
                    author = get_author(author_info)
                elif "works" in data:
                    works_info = data["works"]["key"]
                    author = get_author_from_works(works_info)
            else:
                print('')
        else:
            print("Error")

    except Exception as e:
        print(e)
    
    return title, author


def get_author(author_info):
    url_author = f"https://openlibrary.org{author_info}.json"
    
    try:
        reponse = requests.get(url_author)
        check_code = reponse.status_code
        if check_code == 200:
            data = reponse.json()
            if author_info in data:
                author_name = data["name"]
                return author_name
    except Exception as e:
        print(e) 


def get_author_from_works(works_info):
    url_works = f"https://openlibrary.org{works_info}.json"

    try:
        reponse = requests.get(url_works)
        check_code = reponse.status_code
        if check_code == 200:
            data = reponse.json()
            if works_info in data:
                works_author_name = data["authors"]["author"]["key"]
                author_name = get_author(works_author_name)
                return author_name
    except Exception as e:
        print(e) 




