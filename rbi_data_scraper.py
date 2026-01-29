#!/usr/bin/env python
# coding: utf-8

# In[63]:


import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import re

# Create a list of URLs for the 12 months
base_url = "https://www.rbi.org.in/Scripts/ATMView.aspx?atmid="
urls = [base_url + str(atmid) for atmid in range(134, 146)]

# Loop through each URL
for url in urls:
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data for {url}")
        continue

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all hyperlinks on the page
    all_links = soup.find_all("a")

    # Find the data file link
    data_url = None
    for link in all_links:
        if "href" in link.attrs:
            href = link["href"]
            if "XLSX" in href.upper() or "XLS" in href.upper():
                data_url = href
                break

    if not data_url:
        print(f"No data file found for {url}")
        continue

    # Extract the file name from the URL
    file_name = data_url.split("/")[-1]

    # Download the data file
    urllib.request.urlretrieve(data_url, file_name)
    print(f"Data link: {url}"


# In[ ]:




