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
    This function scrapes the events data (what events duke has or is going to have and event related information) from the Duke eventlist website.
    """
    if not os.path.exists("output"):
        os.makedirs("output")
    driver = webdriver.Chrome()

    csv_filename = "../output/data_events.csv"

    url = "https://dukegroups.com/events"
    driver.get(url)
    index = 3

    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                "title",
                "link", 
                "group"]
            )
        while True:
            
            try:
                xpath = "/html/body/div[5]/div[2]/div/div/div[6]/div[1]/ul/li[{}]/div/div/div[2]/div/div/h3".format(index)
                title = (
                    WebDriverWait(driver, 2)
                    .until(EC.presence_of_element_located((By.XPATH, xpath,)))
                )
            except:
                title = ""

            try:
                xpath = "/html/body/div[5]/div[2]/div/div/div[6]/div[1]/ul/li[{}]/div/div/div[2]/div/div/h3/a".format(index)
                link = (
                    WebDriverWait(driver, 2)
                    .until(EC.presence_of_element_located((By.XPATH, xpath,)))
                )
                link_url = link.get_attribute("href")
            except:
                link_url = ""

            try:
                xpath = "/html/body/div[5]/div[2]/div/div/div[6]/div[1]/ul/li[{}]/div/div/div[2]/div/div/div[2]/p/a".format(index)
                group = driver.find_elements("xpath", xpath)
                group_text = ""
                for elem in group:
                    group_text = group_text + elem.text + ", "
                group_text = group_text.rstrip(", ")
            except:
                group_text = ""

            index = index + 1

            if title and group:
                print(title.text, link_url, group_text)

                writer.writerow([title.text, link_url, group_text])


            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

main()