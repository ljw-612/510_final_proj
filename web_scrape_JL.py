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


if not os.path.exists("output"):
    os.makedirs("output")
driver = webdriver.Chrome()

csv_filename = "output/data_events.csv"

url = "https://dukegroups.com/events"
driver.get(url)
index = 3

with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        [
            "index",
            "title", 
            "group"]
        )
    while True:
        
        try:
            xpath = "/html/body/div[5]/div[2]/div/div/div[6]/div[1]/ul/li[{}]/div/div/div[2]/div/div/h3".format(index)
            title = (
                WebDriverWait(driver, 2)
                .until(EC.presence_of_element_located((By.XPATH, xpath,)))
                .text
            )
        except:
            title = ""

        try:
            xpath = "/html/body/div[5]/div[2]/div/div/div[6]/div[1]/ul/li[{}]/div/div/div[2]/div/div/div[2]".format(index)
            group = (
                WebDriverWait(driver, 2)
                .until(EC.presence_of_element_located((By.XPATH, xpath,)))
                .text
            )
        except:
            group = ""

        index = index + 1

        if title and group:
            writer = csv.writer(csvfile)
            writer.writerow([title, group])







