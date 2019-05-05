import requests
import bs4
import csv

html = requests.get("https://inshorts.com/en/read") # input URL here

soup = bs4.BeautifulSoup(html.text, 'lxml')
cards_stacks = soup.find_all('div', class_ = 'news-card')

def get_image_url(image):
        split = image.split('(')
        splittwo = split[1].split('?')[0]
        #print(splittwo)
        return splittwo[1:]

def write_into_csv(row):
    with open('news_data.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()


for card in cards_stacks:
    #getting image url
        image = card.find('div', class_ = 'news-card-image').get('style')
        img_link = get_image_url(image)
        print(img_link)

        #Headlines
        print("Headlines:")
        headlines = card.find('span', attrs={"itemprop": "headline"}).text
        print(headlines)

        #getting dates
        print("Date:")
        on_date = card.find('span', class_ = 'date').text
        print(on_date)

        #ArticleBody
        print("Body:")
        news_body = card.find('div', attrs={"itemprop": "articleBody"}).text
        print(news_body)

        #getting author
        print("Author:")
        author = card.find('span', class_ = 'author').text
        print(author)

        #Read More
        print("More Detail @:")
        read_more = card.find('a', class_ = 'source')
        if read_more is None:

            link = "Not Available"
            print(link)

        else:
            link = read_more.get('href')
            print(link)

        #row = [img_link, headlines, on_date, news_body, author, link]
        #write_into_csv(row)
        print("#################################----NEW----############################################")
