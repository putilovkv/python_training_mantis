from selenium.webdriver.support.ui import Select


class BaseHelper:

    def __init__(self, app):
        self.app = app

    def _change_field(self, field_name: str, text: str):
        if text is None: return
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(text)

    def _change_select_by_visible_text(self, field_name: str, text: str):
        if text is None: return
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def _change_select_by_value(self, field_name: str, value: str):
        if value is None: return
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_value(value)