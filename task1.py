book_profile = {
"title": "Основи програмування",
"author": "Іван Петренко",
"year": 2023,
"publisher_info": {
"name": "Наукова думка",
"city": "Київ"
}
}
title = book_profile["title"]
author = book_profile["author"]
publisher_name = book_profile["publisher_info"]["name"]
publisher_city = book_profile["publisher_info"]["city"]
print(f"Книга {title}, автором якої є {author}, була видана у місті {publisher_city}")
if "year" in book_profile:
    print(f"Рік видання: {book_profile['year']}")
else:
    print("Рік видання невідомий")