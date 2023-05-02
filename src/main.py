from base import Build, Driver
from selenium.webdriver.common.by import By


def rss_sema_rs():
    driver = Driver().get_chrome()
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

    if data:
        Build(path_output="src/feed/rss-sema-rs.xml").setup(data=data)


if __name__ == "__main__":
    rss_sema_rs()
