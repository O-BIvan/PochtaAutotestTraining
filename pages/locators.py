from selenium.webdriver.common.by import By


class BasePageLocators:
    TRACK_ID_INPUT = (By.CSS_SELECTOR, "#tracking-number")
    TRACK_SUBMIT = (By.CSS_SELECTOR, ".SearchButton-sc-1dh275s-0")  # генерируется? поменять привязку?


class LoginPageLocators:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#userpassword")


class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".b-header__menu-item--enter .b-header__item")
    BUSINESS_BUTTON = (By.CSS_SELECTOR, ".b-header__menu-item--for-business")
    BUSINESS_MENU = (By.CSS_SELECTOR, ".b-business-menu__container--visible")


class LinkAndId:
    TRACK_ID_WORLD = "CA123456789RU"
    TRACK_ID_RUSSIA = "35005145009747"
    TRACK_ID_INCORRECT = "123AB23"

    LINK_MAIN = "https://www.pochta.ru/"


class TrackPageLocators:
    TRACK_ID_INPUT = (By.CSS_SELECTOR, ".Input-sc-1jx0q7k-0")
    STATUS_MARK = (By.CSS_SELECTOR, ".TrackingCard__CompletedStatus-sc-1fodkqb-4")
    INCORRECT_TRACK_ID_MESSAGE = (By.CSS_SELECTOR, ".ErrorLabel-sc-1cl8x16-0")
    SEARCH_RESULT_SUCCESS = (By.CSS_SELECTOR, ".Barcode__BarcodeLayout-e22oc0-0")
