from pages.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.username_form_is_present()
        self.userpassword_form_is_present()

    def username_form_is_present(self):
        assert self.is_element_present(*LoginPageLocators.USERNAME_INPUT), "Username form is not present"

    def userpassword_form_is_present(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT),  "Password form is not present"

