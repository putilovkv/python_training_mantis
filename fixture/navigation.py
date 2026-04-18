from fixture.base_helper import BaseHelper


class NavigationHelper(BaseHelper):

    def __init__(self, app, base_url):
        super().__init__(app)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.base_url)

    def go_to_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            self.app.session.login_if_not_logged()
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()