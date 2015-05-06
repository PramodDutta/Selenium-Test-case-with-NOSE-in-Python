import nose
from selenium import webdriver
import unittest
from nose.plugins.attrib import attr


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.get("http://newtours.demoaut.com/mercurysignon.php")

    @attr(priority="high")
    def test_LoginTest(self):
        ## Login in the Application ##
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys("techdutta")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("test123")
        self.driver.find_element_by_xpath("//input[@name='login']").click()


        ## Verify that the Profile is Comming , Means Login ##
        self.assertTrue(self.driver.find_element_by_xpath("//html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a").is_displayed())


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    nose.main(verbosity=2)



