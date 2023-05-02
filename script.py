"""
selenium==4.6.0
webdriver-manager==3.8.4
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_browser(headless: bool = False):
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
    driver = get_chrome_browser(headless=True)
    driver.get("https://www.sema.rs.gov.br/noticias?publicacaodatahoraini=17%2F04%2F2023&publicacaodatahorafim=01%2F05%2F2023&ordem=RECENTES")

    content = driver.find_element(By.CLASS_NAME, "conteudo-lista__body")
    posts = content.find_elements(By.TAG_NAME, "article")

    for post in posts:
        print(50*"=")
        print(post.find_element(By.TAG_NAME, "h2").text)
        print(post.find_element(By.TAG_NAME, "a").get_attribute('href'))
        print(post.find_element(By.TAG_NAME, "p").text)
        print(50*"=")
