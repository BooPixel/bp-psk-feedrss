import xml.etree.ElementTree as ET

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Build:

    def __init__(
            self,
            path_input: str = "src/assets/rss-simple.xml",
            path_output: str = "src/assets/rss-sema-rs.xml"):
        self.tree = ET.ElementTree()
        self.tree.parse(path_input)
        self.channel = self.tree.find("channel")
        self.path_output = path_output

    def setup(self, data: dict):
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

    @staticmethod
    def chrome_browser(headless: bool = False) -> webdriver.ChromeOptions:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        if headless:
            chrome_options.add_argument("--headless")

        executable_path = ChromeDriverManager().install()
        return webdriver.Chrome(
            executable_path=executable_path,
            chrome_options=chrome_options
        )


if __name__ == "__main__":
    driver = Driver().chrome_browser(headless=True)
    driver.implicitly_wait(10)
    driver.get("https://www.sema.rs.gov.br/noticias")

    content = driver.find_element(By.CLASS_NAME, "conteudo-lista__body")
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


    from pdb import set_trace; set_trace()

    if data:
        Build().setup(data=data)
