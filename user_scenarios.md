### MAIN PAGE
___
Test name: test_guest_can_track_from_main_page</br>

Scenario:
1) Guest opens the main page
2) Types in **valid** track id into track input field
3) Got redirected to tracking page
4) Result of the search displayed on the page
___
Test name: test_guest_can_go_to_login_page_from_main_page</br>

Scenario:
1) Guest opens the main page
2) Clicks on "Login" link
3) Got redirected to login page
4) Sees login and password fields
___
Test name: test_guest_can_open_business_menu</br>

Scenario:
1) Guest opens the main page
2) Clicks on "For business" link
3) Business menu opens up
___
Test name: test_guest_can_see_incorrect_track_id_message_from_main_page</br>

Scenario:
1) Guest opens the main page
2) Types in **invalid** track id into track input field
3) Got redirected to tracking page
4) Got "Incorrect track id message"

*Mark as x-fail: guest will be redirected to tracking page, but wont see</br>
error message*
___

