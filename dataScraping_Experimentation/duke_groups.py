from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import csv
import time

def main():
    """
    This function scrapes the groups data (what groups Duke has and their information) from the Duke eventlist website.
    """
    if not os.path.exists("output"):
        os.makedirs("output")
    driver = webdriver.Chrome()

    csv_filename = "../output/data_groups.csv"

    url = "https://dukegroups.com/club_signup?view=all&"
    driver.get(url)
    index = 3

    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                "title", 
                "link",
                "mission"]
            )
        while True:
            
            try:
                xpath = "/html/body/div[5]/div[2]/div/div/div[7]/ul/form/li[{}]/div/div[2]/div[1]/div[2]/h2".format(index)
                title = (
                    WebDriverWait(driver, 2)
                    .until(EC.presence_of_element_located((By.XPATH, xpath,)))
                )
                # title_text = title.text
            except:
                title = ""

            try:
                xpath = "/html/body/div[5]/div[2]/div/div/div[7]/ul/form/li[{}]/div/div[2]/div[1]/div[2]/div/p[1]/a[1]".format(index)
                link = (
                    WebDriverWait(driver, 2)
                    .until(EC.presence_of_element_located((By.XPATH, xpath,)))
                )
                # group_text = group.text
            except:
                link = ""
            # print(link.get_attribute("href"))
            try:
                xpath = "/html/body/div[5]/div[2]/div/div/div[7]/ul/form/li[{}]/div/div[2]/div[1]/div[2]/div/p[3]".format(index)
                # /div[1]/ul/li[{}]/div/div/div[2]/div/div/div[2]"
                mission = (
                    WebDriverWait(driver, 2)
                    .until(EC.presence_of_element_located((By.XPATH, xpath,)))
                )
                mission_data = mission.get_attribute("innerHTML")
                mission_text = [item.strip() for item in mission_data.split("<br>")][1]
                # group_text = group.text
            except:
                mission = ""


            index = index + 1

            if title and link and mission:
                print(title.text, link.get_attribute("href"), mission_text)

                writer.writerow([title.text, link.get_attribute("href"), mission_text])

            # last_height = driver.execute_script("return document.body.scrollHeight")

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
main()