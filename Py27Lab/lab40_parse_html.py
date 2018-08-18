import requests
from bs4 import BeautifulSoup

base_url = 'https://www.mobile01.com/'
# https://www.mobile01.com/category.php?id=4
# https://www.mobile01.com/category.php?id=2
# https://www.mobile01.com/category.php?id=15
sub_url = 'https://www.mobile01.com/category.php?id=%d'
ids = [4, 2, 15]
for id in ids:
    result = requests.get(sub_url % (id))
    base_soup = BeautifulSoup(result.content, 'html.parser')
    print base_soup.title.name, base_soup.title.string
    hot_posts = base_soup.find('div', {'id': 'hot-posts'})
    hot_posts_links = hot_posts.find_all('a')
    for link in hot_posts_links:
        print link

r1 = requests.get(base_url)
base_soup = BeautifulSoup(r1.content, 'html.parser')
print base_soup.title.name, base_soup.title.string
hot_posts = base_soup.find('div', {'id': 'hot-posts'})
hot_posts_links = hot_posts.find_all('a')
for link in hot_posts_links:
    print link
