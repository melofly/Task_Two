from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class StorePage(BasePage):
    SORT_GMS = (By.ID, "sort_by_trigger")
    PRICE_DESC_SORT = (By.ID, "Price_DESC")
    RESULT_ITEM_FINAL_PRICE = (By.XPATH, "//*[contains(@class,'discount_final_price')]")

    def sort_games_desc(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_GMS)).click()
        self.wait.until(EC.element_to_be_clickable(self.PRICE_DESC_SORT)).click()

    @property
    def prices(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located(self.RESULT_ITEM_FINAL_PRICE))
        prices = []
        for el in elements:
            text = el.text.strip().replace(",", ".").replace("€", "")
            try:
                price = float(text)
                prices.append(price)
            except ValueError:
                continue
        return prices
