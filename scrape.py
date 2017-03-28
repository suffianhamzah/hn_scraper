import requests
from bs4 import BeautifulSoup

class hnScraper(object):
	def __init__(self):
		self.urls = []
		self.requests = requests

	def print_all_posts(self,url):
		if 'ycombinator' not in url:
			raise 'This is not a valid hn url! They should contain ycombinator in the url'

		try:
			resp = self.requests.get(url)
		except Exception as e:
			print(e)
			return
		soup = BeautifulSoup(resp.text,'lxml')
		all_posts = soup.findAll(attrs={"class":"title"})
		clean_posts = [post for post in all_posts if post.text]
		for index, post in enumerate(clean_posts):
			print(index,' ',post.text)
			print(post.a['href'])
			print('\n')

scraper = hnScraper()
scraper.print_all_posts('https://news.ycombinator.com/jobs')