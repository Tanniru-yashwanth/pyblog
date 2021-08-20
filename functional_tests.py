"""
Functional tests are used to test the application from the point of user.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class PyBlogTest(unittest.TestCase):
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
        self.browser.quit()

    def test_getting_index_page(self):
        """
         To check whether the home page is working or not.
         """
        self.browser.get("http://localhost:8000")
        # to check the pyblog in title
        self.assertEqual("pyblog", self.browser.title)

    def test_topics_page(self):
        """
        To check whether the topics page is working.
        """
        self.browser.get("http://localhost:8000/topics/1")
        self.assertEqual('Topics', self.browser.title)

    def test_topic_detail_page(self):
        """
        To check whether the topic detail page is working.
        """
        self.browser.get('http://localhost:8000/topics/1/1/')
        self.assertEqual('TopicDetail', self.browser.title)

    def test_comment_page(self):
        """
        To check whether the comment page is working or not.
        """
        self.browser.get('http://localhost:8000/topics/1/1/comment')
        self.assertEqual('Comment', self.browser.title)

    def test_ask_page(self):
        """
        To check whether the ask page is working or not.
        """
        self.browser.get('http://localhost:8000/topics/1/1/ask')
        self.assertEqual('Ask', self.browser.title)

    def test_add_tag_page(self):
        """
        To check whether the adding tag  page is working or not.
        """
        self.browser.get('http://localhost:8000/topics/1/add_tag')
        self.assertEqual('Add Tags', self.browser.title)

    def test_add_tag_topic_page(self):
        """
        To check whether the adding tag to topic page is working or not.
        """
        self.browser.get('http://localhost:8000/topics/1/1/add_tag_topic')
        self.assertEqual('TagTopics', self.browser.title)

    def test_info_page(self):
        """
        To check whether the your account is working as expected.
        """
        self.browser.get('http://127.0.0.1:8000/users/info/1')
        self.assertEqual('Your Account', self.browser.title)

    def test_logout(self):
        """
        To check whether the logout page is working.
        """
        self.browser.get('http://127.0.0.1:8000/users/logout/')
        self.assertEqual('Logged out', self.browser.title)


if __name__ == "__main__":
    unittest.main()
