import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

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

directory_name = "Output Files"

if not os.path.exists(directory_name):
    os.mkdir(directory_name)

# Loop through URLs, extract content, and save as text files
for index, row in df.iterrows():
    url = row['URL']  # Replace with the actual column name containing URLs
    url_id = row['URL_ID']
    title, text = extract_content_from_url(url)
    
    if title and text:
        file_path = os.path.join(directory_name,f"{url_id}.txt")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\n\n")
            f.write(f"Text: {text}\n")

print("Extraction and saving complete.")