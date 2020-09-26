from pages.base_page import BasePage
from pages.locators import BasePageLocators, LinkAndId, MainPageLocators


class MainPage(BasePage):
    def search_incorrect_track_id(self):
        self.insert_incorrect_track_id()
        self.submit_track_id()

    def search_track_id(self):
        self.insert_track_id()
        self.submit_track_id()

    def should_be_visible_business_menu(self):
        assert self.is_element_present(*MainPageLocators.BUSINESS_MENU), "Business menu is not visible"

    def insert_incorrect_track_id(self):
        input_form = self.browser.find_element(*BasePageLocators.TRACK_ID_INPUT)
        input_form.send_keys(LinkAndId.TRACK_ID_INCORRECT)

    def insert_track_id(self):
        input_form = self.browser.find_element(*BasePageLocators.TRACK_ID_INPUT)
        input_form.send_keys(LinkAndId.TRACK_ID_WORLD)

    def go_to_login_page_from_main_page(self):
        login = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)
        login.click()

    def open_business_menu(self):
        business_menu = self.browser.find_element(*MainPageLocators.BUSINESS_BUTTON)
        business_menu.click()

    def submit_track_id(self):
        submit_button = self.browser.find_element(*BasePageLocators.TRACK_SUBMIT)
        submit_button.click()

