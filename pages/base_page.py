from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        self.page.goto(url, wait_until='domcontentloaded')

    def fill_field(self, selector: str, value: str):
        locator = self.page.locator(selector)
        self.check_element(locator)
        locator.fill(value)
        expect(locator).to_have_value(value)

    def check_element(self, element):
        expect(element).to_be_visible()
        expect(element).to_be_enabled()