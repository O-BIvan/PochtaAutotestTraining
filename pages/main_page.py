from pages.base_page import BasePage
from pages.locators import BasePageLocators, TrackIds

# under construction


class MainPage(BasePage):
    def search_track_id(self):
        self.insert_track_id()
        self.submit_track_id()

    def insert_track_id(self):
        input_form = self.browser.find_element(*BasePageLocators.TRACK_ID_INPUT)
        input_form.send_keys(TrackIds.TRACK_ID_WORLD)

    def submit_track_id(self):
        submit_button = self.browser.find_element(*BasePageLocators.TRACK_SUBMIT)
        submit_button.click()

    def search_incorrect_track_id(self):
        input_form = self.browser.find_element(*BasePageLocators.TRACK_ID_INPUT)
        input_form.send_keys(TrackIds.TRACK_ID_INCORRECT)






