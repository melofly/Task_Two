from time import sleep

import pytest
from pages.main_page import MainPage
from pages.store_page import StorePage


@pytest.mark.parametrize(
    'game, value_n', [
        ('The Witcher', 10),
        ('Fallout 4', 20)
             ]
)
def test_search_game(game, value_n, driver):
    main_page_driver = MainPage(driver=driver)
    main_page_driver.search_games_in_store(game=game)

    store_page_driver = StorePage(driver=driver)
    store_page_driver.sort_games_desc()

    actual = store_page_driver.get_prices(value_n)
    expected = sorted(actual, reverse=True)

    assert actual == expected, f"нам надо это '{expected}',а это хуйня '{actual}'"
