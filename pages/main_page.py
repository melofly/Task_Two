from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class MainPage(BasePage):
    LOG_BTN = (By.XPATH, "//a[contains(@class, 'global_action_link')]")
    INPUT_FIELD_GMS = (By.XPATH, "//*[contains(@role, 'combobox')]")
    SEARCH_BTN_GMS = (By.XPATH, "//*[contains(@type, 'submit')]")


    def open_login_page(self):
        self.wait.until(EC.visibility_of_element_located(self.LOG_BTN))
        self.wait.until(EC.element_to_be_clickable(self.LOG_BTN)).click()

    def search_games_in_store(self, game):
        self.wait.until(EC.visibility_of_element_located(self.INPUT_FIELD_GMS)).send_keys(game)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN_GMS)).click()
