"""
Module Config
"""

import logging
from base import Build, Driver
from selenium.webdriver.common.by import By


class SemaRS:

    URL = "https://www.sema.rs.gov.br/noticias"
    FILE = "src/feed/rss-sema-rs.xml"

    def __init__(self) -> None:
        self.driver = Driver().get_chrome()
        self.driver.get(self.URL)

        try:
            self.run()
        except Exception as error:
            logging.error(error)

    def run(self):
        content = self.driver.find_element(By.CLASS_NAME, "conteudo-lista__body")
        posts = content.find_elements(By.TAG_NAME, "article")

        data = []
        for post in posts:
            try:
                data.append(
                    dict(
                        title=str(post.find_element(By.TAG_NAME, "h2").text),
                        link=str(post.find_element(By.TAG_NAME, "a").get_attribute('href')),
                        description=str(post.find_element(By.TAG_NAME, "p").text)
                    )
                )
            except Exception as error:
                print(error)

        if data:
            Build(path_output=self.FILE).setup(data=data)


class SemaCE:

    URL = "https://www.sema.ce.gov.br/"
    FILE = "src/feed/rss-sema-ce.xml"

    def __init__(self) -> None:
        self.driver = Driver().get_chrome()
        self.driver.get(self.URL)

        try:
            self.run()
        except Exception as error:
            logging.error(error)

    def run(self):
        content = self.driver.find_element(By.CLASS_NAME, "cc-posts")
        posts = content.find_elements(By.CLASS_NAME, "cc-post")

        data = []
        for post in posts:
            title = post.find_element(By.CLASS_NAME, "cc-post-title")
            try:
                data.append(
                    dict(
                        title=str(title.text),
                        link=str(title.get_attribute('href')),
                        description=str(post.find_element(By.CLASS_NAME, "cc-post-excerpt").text)
                    )
                )
            except Exception as error:
                print(error)

        if data:
            Build(path_output=self.FILE).setup(data=data)
