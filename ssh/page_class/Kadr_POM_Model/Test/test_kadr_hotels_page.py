from class_test_kadr_hotels_page import *
from class_test_kadr_hotels_email_subscribe import *


def case_1(page_link):
    try:
        test_kadr_hotels_page = TestKadrHotelsPage(webdriver.Chrome(), page_link)
        test_kadr_hotels_page.go_to_site()
        test_kadr_hotels_page.enter_word()
        test_kadr_hotels_page.click_on_the_search_button()
        test_kadr_hotels_page.quit_driver()
        print("Test case is passed")

    except Exception as err:
        print("Something did not work out, please try again")




def case_2(page_link):
    try:
        test_test_kadr_hotels_email_subscribe = TestKadrHotelsEmailSubscribe(webdriver.Chrome(), page_link)
        test_test_kadr_hotels_email_subscribe.go_to_site()
        test_test_kadr_hotels_email_subscribe.scroll_down_page()
        test_test_kadr_hotels_email_subscribe.send_emil_address()
        test_test_kadr_hotels_email_subscribe.clik_button_send_emils()
        test_test_kadr_hotels_email_subscribe.quit_driver()
        print("Test case is passed")
    except Exception:
        print("Oops!  That was no valid element.  Try again...")
