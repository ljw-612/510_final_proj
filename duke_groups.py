import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL you want to scrape
url = "https://dukegroups.com/club_signup?group_type=9999"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Initialize empty lists to store data
    ids = []
    names = []
    links = []
    tags = []
    descriptions = []

    # Find the club entries on the page
    club_entries = soup.find_all("div", class_="list-group-item")

    # Loop through the club entries and extract the information
    for club in club_entries:
        # Extract the ID
        club_id = club.find("div", class_="pull-right").text.strip()

        # Extract the name
        club_name = club.find("h4").text.strip()

        # Extract the link
        club_link = club.find("a")["href"]

        # Extract the tag
        club_tag = club.find("p", class_="club-list-tags").text.strip()

        # Extract the description
        club_description = club.find("div", class_="list-group-item-text").text.strip()

        # Append the data to the respective lists
        ids.append(club_id)
        names.append(club_name)
        links.append(club_link)
        tags.append(club_tag)
        descriptions.append(club_description)

    # Create a DataFrame from the lists
    data = {
        "ID": ids,
        "Name": names,
        "Link": links,
        "Tag": tags,
        "Description": descriptions,
    }

    df = pd.DataFrame(data)

    # Print the DataFrame
    print(df)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
