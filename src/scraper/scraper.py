import requests
from bs4 import BeautifulSoup

def main():
	response = requests.get(
		url="https://en.wikipedia.org/wiki/List_of_fictional_countries"
	)
	soup = BeautifulSoup(response.content, 'html.parser')

	# Get all the links
	allLinks = soup.find(id="bodyContent").find_all("td")


	names = []

	f = open("fictional_nation.txt", "w")
	for link in allLinks:
		t = link.text.strip()
		if len(t) < 20:
			names.append(t)
	for i, name in enumerate(names):
		if i + 1 < len(names):
			if len(names[i+1]) == 0:
				f.write(name + '\n')
	f.close()
