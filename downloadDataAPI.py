import requests
import os
import json
import sys
import time
sys.stdout.reconfigure(encoding='utf-8')
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.225 Safari/537.36"
header={'useragent': user_agent}
cookie = {'ht-location':'IN', 'HTMyOffer':'myOfferHT', '_sp_ses.e8bf':'*', 'usercohortcitynew':'Delhi', 'usercitynew':'Delhi'}
def delete_all_files(folder_path):
    """Delete all files in the specified folder_path."""
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")


# Define the folder path for storing files
folder_path = r"C:\Users\littlex\PycharmProjects\instaBOT\PostData"
filepath = ""

# Fetch news data from the News API
r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=335d6bede4704155b82961e9fcc8bca5").text

try:
    # Parse the JSON response
    jdata = json.loads(r)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    sys.exit(1)

# Lists to store URLs of images and titles
urlToImage = []
title = []

# Extract relevant data from the JSON response
for article in jdata['articles']:
    if article['urlToImage'] is None:
        continue
    else:
        urlToImage.append(article['urlToImage'])
        title.append(article['title'])

# Clear existing files in the specified folder
delete_all_files(folder_path)

# Process each article and save its title to a text file and image to a jpg file
for i, value in enumerate(title):
    # Generate a file path using the folder_path and index
    filepath = os.path.join(folder_path, str(i))

    # Write the title to a text file
    with open(f"{filepath}.txt", 'w', encoding='utf-8') as af:
        af.write(title[i])

    try:
        # Download the image for the article
        r = requests.get(urlToImage[i])
        time.sleep(2)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image for {title[i]}: {e}")
        continue

    # Save the image content to a jpg file
    with open(f"{filepath}.jpg", 'wb') as ai:
        ai.write(r.content)



