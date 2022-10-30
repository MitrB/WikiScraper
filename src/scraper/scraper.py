import requests
from bs4 import BeautifulSoup

def main():
	f = open("baby_names_boys.txt", "w+")
	for i in range(2, 11):
		response = requests.get(
			url=f"https://www.vernoeming.nl/alle-jongensnamen-van-{i}-letters/"
		)
		soup = BeautifulSoup(response.content, 'html.parser')

		# Get all the links
		allLinks = soup.find_all("li")


		names = []

		for link in allLinks:
			t = link.text.strip()
			f.write(t + '\n')
	f.close()
