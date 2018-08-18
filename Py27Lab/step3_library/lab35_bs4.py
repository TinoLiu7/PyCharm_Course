import requests, bs4

url1 = 'https://www.uuu.com.tw/'

r1 = requests.get(url1)
soup = bs4.BeautifulSoup(r1.content, "html.parser")
print type(soup), soup.title.name, soup.title.string
#print soup.prettify()
courseList = soup.find('div', {'id': 'course_list'})
for course in courseList:
    print type(course), course

print '@@@@@@@@@@@@@@@@@@@@@@'

courseLink = courseList.find_all('a')
for link in courseLink:
    print link.p
    print link.get('href')