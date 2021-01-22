import requests, re
from random import choice

def extract_url(string):
    f = re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",string)[0][0].strip("('").split('?')[0]
    return f

def main(query):
    url = 'https://unsplash.com/s/photos/'+query
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    r = requests.get(url,headers=headers)
    collected = []
    for i in r.content.decode().split(' '):
        if 'images.unsplash.com/photo-' in i:
            collected.append(i)
    return extract_url(choice(collected))
# print(main(input('Enter Query:- ')))
# print(main("hacker"))