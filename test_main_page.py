import pytest

from pages.locators import LinkAndId
from pages.track_page import TrackPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.mark.positive
def test_guest_can_track_from_main_page(browser):
    page = MainPage(browser, LinkAndId.LINK_MAIN)
    page.open()
    page.search_track_id()
    track_page = TrackPage(browser, browser.current_url)
    track_page.should_be_search_track_id_success()


@pytest.mark.positive
def test_guest_can_go_to_login_page_from_main_page(browser):
    page = MainPage(browser, LinkAndId.LINK_MAIN)
    page.open()
    page.go_to_login_page_from_main_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.positive
def test_guest_can_open_business_menu(browser):
    page = MainPage(browser, LinkAndId.LINK_MAIN)
    page.open()
    page.open_business_menu()
    page.should_be_visible_business_menu()


@pytest.mark.xfail(reason="Not ready yet - guest won't see incorrect track id message")
@pytest.mark.negative
def test_guest_can_see_incorrect_track_id_message_from_main_page(browser):
    page = MainPage(browser, LinkAndId.LINK_MAIN)
    page.open()
    page.search_incorrect_track_id()
    track_page = TrackPage(browser, browser.current_url)
    track_page.should_be_incorrect_track_id_message()
