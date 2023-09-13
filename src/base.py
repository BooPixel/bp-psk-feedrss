"""
Module Base
"""

import xml.etree.ElementTree as ET

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Build:

    def __init__(
            self,
            path_input: str = "src/assets/rss.xml",
            path_output: str = "src/feed/rss.xml",
            description: str = "Feed RSS",
            title: str = "RSS",
            link: str = "#"):
        self.path_input = path_input
        self.path_output = path_output
        self.description = description
        self.title = title
        self.link = link

        self.tree = ET.ElementTree()
        self.tree.parse(self.path_input)

    def setup(self, data: dict):
        self.channel = self.tree.find("channel")

        self.channel.find("description").text = self.description
        self.channel.find("title").text = self.title
        self.channel.find("link").text = self.link

        for item in data:
            element = self.new_element(
                title=item.get("title"),
                link=item.get("link"),
                description=item.get("description")
            )
            self.channel.append(element)
        self.write()

    def new_element(
            self,
            title: str,
            link: str,
            description: str) -> ET.Element:
        item = ET.Element('item')
        ET.SubElement(item, 'title').text = title
        ET.SubElement(item, 'link').text = link
        ET.SubElement(item, 'description').text = description
        return item

    def write(self):
        self.tree.write(self.path_output, encoding="UTF8")


class Driver:

    def __init__(self, headless: bool = True) -> None:
        self.headless = headless
        self.chrome = Chrome

    def get_chrome(self):
        chrome = Chrome(self.headless)
        return chrome.browser()


class Chrome:

    def __init__(self, headless: bool) -> None:
        self.headless = headless

    def options(self) -> webdriver.ChromeOptions:
        """Chrome Options
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        if self.headless:
            chrome_options.add_argument("--headless")
        return chrome_options

    def browser(self) -> webdriver.Chrome:
        """Chrome Browser
        """
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=self.options()
        )
        driver.implicitly_wait(10)
        return driver
