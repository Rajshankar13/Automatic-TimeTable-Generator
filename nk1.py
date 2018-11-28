import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning#Machine_learning_tasks')
soup = bs4.BeautifulSoup(res.text, 'lxml')
for i in soup.select('.mv-headline'):
	print(i.text)
