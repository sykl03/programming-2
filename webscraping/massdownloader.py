# massdownloader.py
# downloads all xkcd comics to disk

import os
import requests
import bs4

url = "https://xkcd.com" # starting url

# create a folder/directory to store comics
os.makedirs("xkcdimages", exist_ok=True)

# Loop while URL does not ends with a "#"
while not url.endswith("#"):
    #TODO: download the html
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.status_code
    res.raise_for_status() # stop if there is a 404 error
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # TODO: find the url/href of the image
    comic_elem = soup.select("#comic img")
    if comic_elem == [] or comic_elem[0].get("src").startswith("/2067"):
        print("couldn't find image...")
    else:
        comic_url = "https:" + comic_elem[0].get("src")
        print(f"\tDownloading image {comic_url}...")
    # todo: download the image
        res = requests.get(comic_url)
        res.raise_for_status()
    # todo: save the image to disk
    image_file = open(os.path.join("xkcdimages", os.path.basename(comic_url)), "wb")
    for chunk in res.iter_content(1000000):
        image_file.write(chunk)
    image_file.close()

    # todo: get the previous' button to URL
    prev_link = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prev_link.get("href")
print("done")