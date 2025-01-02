from googlesearch import search
query = "Введите абсолютно любой запрос и опубликуются ссылочки."

for i in search(query, tld="co.in", num=5, stop=5, pause=1):
    print(i)