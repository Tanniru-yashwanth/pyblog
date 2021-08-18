from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            executable_path="S:\material\chromedriver_win32\chromedriver.exe"
        )
        self.browser.get("http://localhost:8000/users/login/")
        username = self.browser.find_element_by_name('username')
        password = self.browser.find_element_by_name('password')
        submit = self.browser.find_element_by_name('submit')
        username.send_keys('yashwanth')
        password.send_keys('Tanniru@07')
        submit.send_keys(Keys.RETURN)

    def tearDown(self):
        time.sleep(5)
        self.browser.quit()

    def test_getting_index_page(self):
        # to check the home page
        self.browser.get("http://localhost:8000")
        # to check the pyblog in title
        self.assertIn("pyblog", self.browser.title)

    def test_topics_page(self):
        self.browser.get("http://localhost:8000/topics/")

    def test_topic_detail_page(self):
        self.browser.get('http://localhost:8000/topics/1/1/')


if __name__ == "__main__":
    unittest.main()
