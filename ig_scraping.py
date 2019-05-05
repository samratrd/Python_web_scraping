import requests
import bs4

username = input("Enter User_name : ")
html = requests.get("https://www.instagram.com/%s/" % (username)) # input URL here
soup = bs4.BeautifulSoup(html.text, 'lxml')

meta_data = soup.find_all('meta', attrs={'property':'og:description'})
text = meta_data[0].get('content').split()



user = '%s %s' % (text[-3], text[-2])
followers = text[0]
following = text[2]
posts = text[4]

print('User:', user)
print('Followers:', followers)
print('Following:', following)
print('Total Posts:', posts)
