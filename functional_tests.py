from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase) :
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # There is a new online todo list app
        self.browser.get("http://localhost:8000")

        # The very top of the website browser the title of the new app is:
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test")

        # The user is allowed to enter a to-do item straight away

        # The user can enter something like "Buy milk"

        # After the user hit enter, the item appears on their todo list

        # The user is again invited to add more items to their todo list

        # The user enters "Buy bread" and hits <enter>

        # The list is updated with the new item, and the user is again allowed to write
        # down more things

        # The website generates a custom URL for the user, so that the user could pick
        # up where they left from

        # Trying the url, the entire list is there

if __name__ == "__main__":
    unittest.main()
