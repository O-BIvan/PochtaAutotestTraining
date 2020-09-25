from pages.locators import TrackPageLocators, TrackIds

from pages.base_page import BasePage


class TrackPage(BasePage):
    def should_be_incorrect_track_id_message(self):
        assert self.is_element_present(*TrackPageLocators.INCORRECT_TRACK_ID_MESSAGE), "Incorrect track id message not present"

    def should_be_search_track_id_success(self):
        barcode = self.browser.find_element(*TrackPageLocators.SEARCH_RESULT_SUCCESS)
        assert barcode.text == TrackIds.TRACK_ID_WORLD, "Searched track id doesn't match with found one"

    def search_incorrect_track_id(self):
        error_message = self.browser.find_element(*TrackPageLocators.TRACK_ID_INPUT)
        error_message.send_keys(TrackIds.TRACK_ID_INCORRECT)