from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        # To-Do
        self.assertIn("To-Do", self.browser.title)

        # The header also mentioned that the name of the app is: To-Do
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIN("To-Do", header_text)

        # The user is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), 
                        "Enter a to-do item")

        # The user can enter something like "Buy milk"
        inputbox.send_keys("Buy milk")

        # After the user hit enter, the item appears on their todo list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(any(row.text == "1: Buy milk" for row in rows))

        # The user is again invited to add more items to their todo list

        self.fail("Finish the test!")

        # The user enters "Buy bread" and hits <enter>

        # The list is updated with the new item, and the user is again allowed to write
        # down more things

        # The website generates a custom URL for the user, so that the user could pick
        # up where they left from

        # Trying the url, the entire list is there

if __name__ == "__main__":
    unittest.main()
