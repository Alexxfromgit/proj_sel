from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    #Locators
    _input_email = '//input[@name="Login"]'
    _input_pass = '//input[@name="Password"]'
    _submit_button = '//button[@type="submit"]'

    _logout_user = '//div[@class="top-bar__logout"]'
    _write_button = '//button[@class="default compose"]'
    _input_address = '//input[@name="toInput"]'
    _letter_theme = '//input[@name="subject"]'
    _send_button = '//button[@class="default send"]'
    _sent_success = '//div[@class="sendmsg__ads-ready"]'

    _uk_input_email = '//input[@name="Login"]'
    _uk_input_pass = '//input[@id="id-2"]'
    _uk_input_button = '//button[@type="submit"]'
    _uk_logout = '//span[@class="sidebar__list-link-name"]'

    _el_form_control = '//input[@class="form-control"]'
    _el_button_go = '//button[@class="btn btn-dark"]'

    def uk_enter_email(self, email):
        element = self.driver.find_element(By.XPATH, self._uk_input_email)
        element.send_keys(email)

    def uk_enter_password(self, password):
        element = self.driver.find_element(By.XPATH, self._uk_input_pass)
        element.send_keys(password)

    def uk_input_button(self):
        element = self.driver.find_element(By.XPATH, self._uk_input_button)
        element.click()

    def enter_email(self, email):
        element = self.driver.find_element(By.XPATH, self._input_email)
        element.send_keys(email)

    def enter_password(self, password):
        element = self.driver.find_element(By.XPATH, self._input_pass)
        element.send_keys(password)

    def next_button(self):
        element = self.driver.find_element(By.XPATH, self._submit_button)
        element.click()

    def uk_login(self, email, password):
        self.uk_enter_email(email)
        self.uk_enter_password(password)
        self.uk_input_button()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.next_button()

    def verify_page_is_loaded(self, title):
        result_title = self.driver.title
        assert result_title == title

    def uk_verify_page_is_loaded(self, title):
        result_title = self.driver.title
        assert result_title == title

    def uk_verify_login_success(self):
        element = self.driver.find_element(By.XPATH, self._uk_logout)
        if element is not None:
            return True
        else:
            return False

    def verify_login_success(self):
        element = self.driver.find_element(By.XPATH, self._logout_user)
        if element is not None:
            return True
        else:
            return False

    def verify_error_is_appeared(self):
        element = self.driver.find_element(By.XPATH, "//div[@class='error-text' and"
                                                     " .= 'Неправильно вказано логін чи пароль. Спробуйте знову.']")
        if element is not None:
            return True
        else:
            return False

    def sending_email(self, input_address, letter_topic):
        element2 = self.driver.find_element(By.XPATH, self._write_button)
        element2.click()
        element3 = self.driver.find_element(By.XPATH, self._input_address)
        element3.send_keys(input_address)
        element4 = self.driver.find_element(By.XPATH, self._letter_theme)
        element4.send_keys(letter_topic)
        element6 = self.driver.find_element(By.XPATH, self._send_button)
        element6.click()

    def uk_verify_email_sent(self):
        element = self.driver.find_element(By.XPATH, self._sent_success)
        if element is not None:
            return True
        else:
            return False

    def el_verify_inbox_email(self, address):
        element = self.driver.find_element(By.XPATH, self._el_form_control)
        element.send_keys(address)
        element2 = self.driver.find_element(By.XPATH, self._el_button_go)
        element2.click()
        element3 = self.driver.find_element(By.XPATH, "//div[@title='FROM' and"
                                                     " .= 'Test Testing']")
        if element3 is not None:
            return True
        else:
            return False

    def el_verify_email_subject(self, address):
        element = self.driver.find_element(By.XPATH, self._el_form_control)
        element.send_keys(address)
        element2 = self.driver.find_element(By.XPATH, self._el_button_go)
        element2.click()
        element3 = self.driver.find_element(By.XPATH, "//div[@class='all_message-min_text all_message-min_text-3' and"
                                                     " .= 'testingtheme']")
        if element3 is not None:
            return True
        else:
            return False
