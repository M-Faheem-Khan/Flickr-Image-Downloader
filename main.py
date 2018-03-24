import urllib.request
import requests
from bs4 import BeautifulSoup

def flickr_img(search, no_img):
# gets page source
	url = "https://www.flickr.com/search/?text="+search
	html = urllib.request.urlopen(url)
	soup = BeautifulSoup(html, "html.parser")

# gets the urls from the div tags
	ls = soup.find_all("div", {"class": "view photo-list-photo-view requiredToShowOnServer awake"})
	k = []
	for i in ls:
		i = str(i)
		i_o = i.index("/")
		i_p = i[::-1].index(")")
		i = i[i_o:-i_p-1]
		i = "https:"+i
		k.append(i)

# downloads all the images
	for i in range(no_img):
		with open(str(i)+".jpg", "wb") as handle:
			response = requests.get(k[i], stream=True)
			if not response.ok:
				print (response)
			for block in response.iter_content(1024):
				if not block:
					break
				handle.write(block)

# makes sure that user enters something
def get_search():
	flag = True
	while flag:
		ui = input("What do you want images of: ")
		if len(ui) == 0:
			print("Search cannot be empty")
		else:
			return ui

# makes sure that the user enters a integer
def get_images():
	flag = True
	while flag:
		try:
			ui = int(input("Out of 22 how many images do you want to download: "))
			if ui <= 22:
				return ui
			else:
				print("Pick a number between 0 and 22")
		except ValueError:
			print("Invalid Input \n Integers only!!")

# Waning
print("If you choose to download any pictures from the website please be sure to know that who they belong and the licenses that come with it. \n\n\nUSE AT YOUR OWN RISK")

# Help
print("HELP \nEnter what you are looking for \nEnter the number of images you want to download less than 22 because that is the default number of images that the website loads")

# calling the necessary functions
search = get_search()
no_img = get_images()

flickr_img(search, no_img)
