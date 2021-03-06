# 
# Parse Band Info from http://www.wacken.com/en/bands/bands-billing/
#
import requests
from bs4 import BeautifulSoup
import json

# Wacken band website
url = "http://www.wacken.com/en/bands/bands-billing/"
outputFile = "wacken.json"

# Get content
page = requests.get(url)

# Parse HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Get band list
bands = soup.find_all('div', class_='col-sm-20')

# Create list 
bandData = []

# Band info starts on the 2nd item
index = 1
for band in enumerate(bands[2:]):
  # Parse bands file
  index = index + 1
  bandName = bands[index].find_all("a")[1].get_text()
  bandImage = bands[index].find("img")['src']
  bandAddedOn = bands[index].get_text().split(":",1)[1].lstrip()
  bandUrl = bands[index].find_all("a")[0]['href']

  # Append data to the list
  bandData.append(
    {
      'bandName':bandName,
      'bandImage':bandImage,
      'bandAddedOn':bandAddedOn,
      'bandUrl':bandUrl
    }
    )

# Save to file
with open(outputFile, 'w') as outfile:
    json.dump(bandData, outfile)