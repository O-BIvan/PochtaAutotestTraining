import pytest

from pages.track_page import TrackPage
from pages.main_page import MainPage

link = "https://www.pochta.ru/"


@pytest.mark.positive
def test_guest_can_track_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.search_track_id()
    track_page = TrackPage(browser, browser.current_url)
    track_page.should_be_search_track_id_success()


@pytest.mark.xfail(reason="Not ready yet - guest won't see incorrect id message")
@pytest.mark.negative
def test_guest_can_see_incorrect_track_id_message_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.search_incorrect_track_id()
    track_page = TrackPage(browser, browser.current_url)
    track_page.should_be_incorrect_track_id_message()
