import time
from fixture.base_helper import BaseHelper


class NavigationHelper(BaseHelper):

    def __init__(self, app):
        super().__init__(app)
        self.web_config = app.config["web"]

    def open_page(self, url, sleep_interval = 0):
        wd = self.app.wd
        wd.get(url)
        time.sleep(sleep_interval)

    def open_home_page(self):
        self.open_page(self.web_config["baseUrl"])

    def open_signup_page(self):
        self.open_page(self.web_config["baseUrl"] + "/signup_page.php")

    def go_to_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            self.app.session.login_if_not_logged()
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()