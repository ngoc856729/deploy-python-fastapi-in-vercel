from fastapi import FastAPI

from src.dtos.ISayHelloDto import ISayHelloDto
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
app = FastAPI()

BROWSERSTACK_USERNAME = "tranngocminh_AFiWRo"
BROWSERSTACK_ACCESS_KEY = "8anY1yMSZhs7qsHCzLeD"
URL = "https://hub.browserstack.com/wd/hub"


@app.get("/")
async def root():
    BROWSERSTACK_USERNAME = BROWSERSTACK_USERNAME
    BROWSERSTACK_ACCESS_KEY = BROWSERSTACK_ACCESS_KEY
    URL = URL

    bstack_options = {
        "os": "OS X",
        "osVersion": "Monterey",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack single python",
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    bstack_options["source"] = "python:sample-main:v1.0"
    options = ChromeOptions()
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)
    driver.get("https://www.synthesia.io/features/avatars")
    driver.quit()
    return {"message": "tôi tên là ngọc"}
