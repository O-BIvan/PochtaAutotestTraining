from selenium.webdriver.common.by import By


class TrackIds:
    TRACK_ID_WORLD = "CA123456789RU"
    TRACK_ID_RUSSIA = "35005145009747"
    TRACK_ID_WRONG = "123AB23"


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "b-header__menu-item--enter")
    TRACK_ID_INPUT = (By.CSS_SELECTOR, "#tracking-number")
    TRACK_SUBMIT = (By.CSS_SELECTOR, ".SearchButton-sc-1dh275s-0")  # генерируется? поменять привязку?


class TrackPageLocators:
    TRACK_ID_INPUT = (By.CSS_SELECTOR, ".Input-sc-1jx0q7k-0")  #
    STATUS_MARK = (By.CSS_SELECTOR, ".TrackingCard__CompletedStatus-sc-1fodkqb-4")
    WRONG_TRACK_ID_MESSAGE = (By.CSS_SELECTOR, ".ErrorLabel-sc-1cl8x16-0")
    SEARCH_RESULT_SUCCESS = (By.CSS_SELECTOR, ".Barcode__BarcodeLayout-e22oc0-0")
