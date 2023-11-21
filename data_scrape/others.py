# Run this cell to import required libraries

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

def scrape_student_clubs_site():
    """
    This function is used to scrape Student-Clubs site
    """
    data_url = "https://sites.duke.edu/prattgsps/student-clubs/"
    page = requests.get(data_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all elements with the class "elementor-widget-container"
    elements = soup.find_all(class_="elementor-widget-container")

    # # Loop through and print the elements
    # i = 0
    # for element in elements:
    #     print(i)
    #     print(element)
    #     print("__________________________________")
    #     i += 1
    student_clubs_html = elements[6].find_all('p')
    activities = {}
    for student_club in student_clubs_html:
        text = student_club.get_text()
        activities[text.split(" Club")[0]] = text

    activities_df = pd.DataFrame(list(activities.items()), columns=['Name', 'Description'])

    activities_df["Type"] = "Club"
    activities_df["Reference"] = "https://sites.duke.edu/prattgsps/student-clubs/"

    return activities_df

def scrape_student_advisory_board():
    """
    This function is used to scrape Student Advisory Board
    """
    data_url = "https://sites.duke.edu/prattgsps/engineering-masters-programs-student-advisory-board/"
    page = requests.get(data_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find all elements with the class "elementor-widget-container"
    elements = soup.find_all(class_="elementor-widget-container")

    # # Loop through and print the elements
    # i = 0
    # for element in elements:
    #     print(i)
    #     print(element)
    #     print("__________________________________")
    #     i += 1
    desc = elements[1].find('p')
    description = desc.get_text()

    # Create a dictionary for the advisory board
    advisory_board = {
        "Name": ["Engineering Master’s Programs Student Advisory Board"],
        "Description": [description],
        "Type": ["Board"],
        "Reference": ["https://sites.duke.edu/prattgsps/engineering-masters-programs-student-advisory-board/"]
    }

    # Convert the dictionary to a DataFrame
    advisory_board_df = pd.DataFrame(advisory_board)

    # Print the DataFrame
    advisory_board_df

    return advisory_board_df

def scrape_commities():
    """
    This function is used to scrape committees
    """
    data_url = "https://gpsg.duke.edu/committees/"
    page = requests.get(data_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    elements = soup.find_all(class_="entry-content clear")
    elements[0].find_all('h3')  

    # Initialize a dictionary to store the committee information
    committee_info = {}

    # Find all the <h3> tags that contain committee names
    committee_names = elements[0].find_all('h3')
    # Loop through the <h3> tags to extract committee information
    for h3 in committee_names[1:]:
        committee_name = h3.text.strip()
        # Find the <p> tag immediately following the <h3> tag
        p_tag = h3.find_next('p')
        if p_tag:
            committee_description = p_tag.text.strip()
            # Add the committee name and description to the dictionary
            committee_info[committee_name] = committee_description

    # Print the dictionary
    print(committee_info)

    committees_df = pd.DataFrame(list(committee_info.items()), columns=['Name', 'Description'])
    committees_df["Type"] = "Committee"
    committees_df["Reference"] = "https://gpsg.duke.edu/committees/"

    return committees_df

def more_resources(df):
    """
    This function manually adds other resources to the current dataset.
    """
    add_resources = [{"Name": "Lawyer Assistance Program", "Description": "The GPSG Lawyer Assistance Program provides students with legal counseling, risk reduction, and mitigation of legal issues.", "Type": "Resource", "Reference": "https://gpsg.duke.edu/resources-for-students/lawyer-assistance-program/"},
                    {"Name": "Funding for Student Groups", "Description": "The Duke Graduate and Professional Student Government encourages students to form groups around social, academic, and cultural similarities. To support these groups, the GPSG allocates a large portion of its budget to funding events and materials for these groups.", "Type": "Resource", "Reference": "https://gpsg.duke.edu/resources-for-students/resources-for-student-groups/"}]
    add_resources_df = pd.DataFrame(add_resources)
    df = pd.concat([df, add_resources_df], ignore_index = True)

    CAPS_resources = [{"Name": "Individual Counseling & Psychiatric Services", 
                  "Description": "Individual counseling provides students the opportunity to meet with a provider and collaboratively work to determine and agree upon goals of treatment in a one-on-one setting. It's part of Counseling and Psychological Services (CAPS)", 
                  "Type": "Service", 
                  "Reference": "https://students.duke.edu/wellness/caps/individual/"
                 },
                 {"Name": "Group Counseling", 
                  "Description": "Our Group Services include group therapy and discussion groups with a variety of goals that aim to promote wellbeing. Research demonstrates that group therapy is equally effective as individual therapy and is often the treatment of choice for student issues. It's part of Counseling and Psychological Services (CAPS)", 
                  "Type": "Service", 
                  "Reference": "https://students.duke.edu/wellness/caps/group/"
                 },
                 {"Name": "Workshops & Discussions", 
                  "Description": "We provide a wide range of interactive, skill-building workshops on various mental health topics for the entire Duke community. It's part of Counseling and Psychological Services (CAPS)", 
                  "Type": "Service", 
                  "Reference": "https://students.duke.edu/wellness/caps/"
                 },
                 {"Name": "Referrals to Community Providers", 
                  "Description": "Our primary goal is to ensure students have access to the best possible care based on their unique needs and sometimes this means working with a professional outside of Counseling and Psychological Services (CAPS). To start, you can meet with our referral coordinator or browse our list of community providers.", 
                  "Type": "Service", 
                  "Reference": "https://duke.miresource.com/"
                 }
                ]
    CAPS_resources_df = pd.DataFrame(CAPS_resources)
    df = pd.concat([df, CAPS_resources_df], ignore_index = True)
    return df

def main():
    activities_df = scrape_student_clubs_site()
    advisory_board_df = scrape_student_advisory_board()
    df = pd.concat([activities_df, advisory_board_df], ignore_index = True)
    committees_df = scrape_commities()
    df = pd.concat([df, committees_df], ignore_index = True)
    df = more_resources(df)

    return df

main()