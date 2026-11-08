from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Page Object untuk halaman Inventori dan Keranjang Belanja."""
    
    ADD_TO_CART_BACKPACK = (By.XPATH, "//button[contains(@data-test, 'add-to-cart-sauce-labs-backpack')]")
    CART_BADGE = (By.XPATH, "//span[@data-test='shopping-cart-badge']")
    BURGER_MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def __init__(self, driver):
        super().__init__(driver)

    def add_backpack_to_cart(self):
        """Menambahkan produk Backpack ke keranjang."""
        self.click(self.ADD_TO_CART_BACKPACK)

    def get_cart_badge_count(self) -> str:
        """Mengambil angka counter pada badge keranjang belanja."""
        return self.get_text(self.CART_BADGE)

    def logout(self):
        """Melakukan aksi logout dari aplikasi."""
        self.click(self.BURGER_MENU_BUTTON)
        self.click(self.LOGOUT_LINK)