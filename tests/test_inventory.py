import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestInventory:
    """Kasus uji fungsional alur inventori, keranjang belanja, dan logout."""

    def test_add_backpack_to_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack_to_cart()

        badge_count = inventory_page.get_cart_badge_count()
        assert badge_count == "1", f"Diharapkan badge '1', tetapi mendapati '{badge_count}'"

    def test_logout_flow(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.logout()

        expected_url = "https://www.saucedemo.com/"
        assert login_page.get_current_url() == expected_url