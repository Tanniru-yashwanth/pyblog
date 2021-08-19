"""
Functional tests are used to test the application from the point of user.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class HomePageTest(unittest.TestCase):
    """
    Class to write the unittests for the every particular function.
    """

    def setUp(self):
        """
        Setup method to set the browser on and to login into the application to check the remaining pages.
        """
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
        """
        TearDown method to shut the browser after completing the testing.
        """
        time.sleep(5)
        self.browser.quit()

    def test_getting_index_page(self):
        """
         To check whether the home page is working or not.
         """
        self.browser.get("http://localhost:8000")
        # to check the pyblog in title
        self.assertIn("pyblog", self.browser.title)

    def test_topics_page(self):
        """
        To check whether the topics page is working.
        """
        self.browser.get("http://localhost:8000/topics/")

    def test_topic_detail_page(self):
        """
        To check whether the topic detail page is working.
        """
        self.browser.get('http://localhost:8000/topics/1/1/')


if __name__ == "__main__":
    unittest.main()
