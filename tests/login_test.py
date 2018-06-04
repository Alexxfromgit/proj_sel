import unittest

from pages.Login.login_page import LoginPage
from base.selenium_driver import SeleniumDriver


class TestALoginPage(unittest.TestCase):

    def setUp(self):
        self.instance = SeleniumDriver()
        self.driver = self.instance.driver_instance()
        self.driver.maximize_window()
        self.driver.get('https://www.ukr.net')
        self.driver.implicitly_wait(3)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_invalid_email(self):
        self.login_page.verify_page_is_loaded("UKR.NET: Всі новини України,"
                                              " останні новини дня в Україні та Світі")
        self.login_page.login('{}"{::{|/', 'Python36')
        result = self.login_page.verify_error_is_appeared()
        assert result == True

    def test_login_valid(self):
        self.login_page.verify_page_is_loaded("UKR.NET: Всі новини України,"
                                              " останні новини дня в Україні та Світі")
        self.login_page.login('testrw@ukr.net', 'Python36')
        result = self.login_page.verify_login_succsess()
        assert result == True


class TestBSendingEmail(unittest.TestCase):

    def setUp(self):
        self.instance = SeleniumDriver()
        self.driver = self.instance.driver_instance()
        self.driver.maximize_window()
        self.driver.get('https://mail.ukr.net')
        self.driver.implicitly_wait(3)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_sending_email_to_mailinator(self):
        self.login_page.uk_login('testrw@ukr.net', 'Python36')
        self.login_page.sending_email('testrwqrt@mailinator.com', 'testingtheme')#, 'testing content text message')
        result2 = self.login_page.uk_verify_email_sent()
        assert result2 == True


class TestCEmailinatorInbox(unittest.TestCase):

    def setUp(self):
        self.instance = SeleniumDriver()
        self.driver = self.instance.driver_instance()
        self.driver.maximize_window()
        self.driver.get('https://www.mailinator.com')
        self.driver.implicitly_wait(3)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_inbox_sent_email(self):
        result = self.login_page.el_verify_inbox_email('testrwqrt@mailinator.com')
        assert result == True

    def test_inbox_email_subject(self):
        result = self.login_page.el_verify_email_subject('testrwqrt@mailinator.com')
        assert result == True


if __name__ == '__main__':
    unittest.main()
