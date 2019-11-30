from selenium.webdriver.common.keys import Keys
from selenium import webdriver


def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    browser = webdriver.Chrome(executable_path='/Users/jittakoopratoomsiri/Downloads/Chromedriver')
    browser.get(url)

    #TODO get all 'a' tags on page
    #TODO for each 'a' tag, get the href attribute value

    links = []
    elements = browser.find_element_by_tag_name('a')
    for url in elements:
        links.append(url.get_attribute('href'))

    browser.close()
    return links

def main():
    get_links("https://cpske.github.io/ISP/")
    print(get_links)

main()