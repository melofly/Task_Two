import pytest
from pages.main_page import MainPage
from pages.store_page import StorePage


@pytest.mark.parametrize(
    'game', [
        ('The Witcher'),
        ('Fallout 4')
             ]
)
def test_search_game(game, driver):
    main_page_driver = MainPage(driver=driver)
    main_page_driver.search_games_in_store(game=game)

    store_page_driver = StorePage(driver=driver)
    store_page_driver.sort_games_desc()

    actual = store_page_driver.prices[0]
    expected = store_page_driver.prices[-1]


    assert actual > expected, f"нам надо это '{expected}',а это хуйня '{actual}'"
