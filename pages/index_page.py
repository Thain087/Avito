from playwright.sync_api import expect
from playwright.sync_api import Page
import config


class IndexPage:
    _CO2_COUNTER = "//div[contains(@class,'desktop-impact-items')]/div[contains(@class,'desktop-impact-item')][2]"
    _WATER_COUNTER = "//div[contains(@class,'desktop-impact-items')]/div[contains(@class,'desktop-impact-item')][4]"
    _ENERGY_COUNTER = "//div[contains(@class,'desktop-impact-items')]/div[contains(@class,'desktop-impact-item')][6]"
    _ALL_COUNTERS = "//div[contains(@class,'desktop-impact-items')]"

    def screenshot_co2_counter(self, page: Page) -> None:
        # Явное ожидание, пока селектор не станет видимым
        expect(page.locator(self._CO2_COUNTER)).to_be_visible()
        # Создание скриншота элемента
        page.locator(self._CO2_COUNTER).screenshot(path="./Output/ТС-01.png")

    def screenshot_water_counter(self, page: Page) -> None:
        # Явное ожидание, пока селектор не станет видимым
        expect(page.locator(self._WATER_COUNTER)).to_be_visible()
        # Создание скриншота элемента
        page.locator(self._WATER_COUNTER).screenshot(path="./Output/TС-02.png")

    def screenshot_energy_counter(self, page: Page) -> None:
        # Явное ожидание, пока селектор не станет видимым
        expect(page.locator(self._ENERGY_COUNTER)).to_be_visible()
        # Создание скриншота элемента
        page.locator(self._ENERGY_COUNTER).screenshot(path="./Output/TС-03.png")

    def screenshot_all_counters(self, page: Page) -> None:
        # Явное ожидание, пока селектор не станет видимым
        expect(page.locator(self._ALL_COUNTERS)).to_be_visible()
        # Создание скриншота элемента
        page.locator(self._ALL_COUNTERS).screenshot(path="./Output/TС-04.png")

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)