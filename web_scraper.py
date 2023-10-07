import requests
from bs4 import BeautifulSoup

def extract_title_and_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.title.string if soup.title else "No title found"
        
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        
        return title, text
    else:
        return None, None

url = "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/"  
# Replace with the desired URL
title, text = extract_title_and_text(url)

if title and text:
    print("Title:", title)
    print("Text:", text)
else:
    print("Unable to fetch title and text from the URL.")


# In[4]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

excel_file = "Input.xlsx"
df = pd.read_excel(excel_file)

# Function to extract title and text from a URL
def extract_content_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No Title"
        text = ' '.join([p.get_text() for p in soup.find_all('p')])
        return title, text
    else:
        return None, None

# Loop through URLs, extract content, and save as text files
for index, row in df.iterrows():
    url = row['URL']  # Replace with the actual column name containing URLs
    url_id = row['URL_ID']
    title, text = extract_content_from_url(url)
    
    if title and text:
        with open(f"{url_id}.txt", "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\n\n")
            f.write(f"Text: {text}\n")

print("Extraction and saving complete.")