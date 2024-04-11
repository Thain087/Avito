import pytest
from pages.index_page import IndexPage

@pytest.fixture()
def index_page(page):
    return IndexPage()

def test_co2_counter_screenshot(page, index_page):
    index_page.open_index_page(page)
    index_page.screenshot_co2_counter(page)
    # скриншот СО2

def test_water_counter_screenshot(page, index_page):
    index_page.open_index_page(page)
    index_page.screenshot_water_counter(page)
    # скриншот воды

def test_energy_counter_screenshot(page, index_page):
    index_page.open_index_page(page)
    index_page.screenshot_energy_counter(page)
    # скриншот энергии

def test_all_counters_screenshot(page, index_page):
    index_page.open_index_page(page)
    index_page.screenshot_all_counters(page)
    # скрин всего
