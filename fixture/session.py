from fixture.base_helper import BaseHelper


class SessionHelper(BaseHelper):

    def login(self, username: str, password: str):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self._change_field("username", username)
        self._change_field("password", password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_as(self, username: str):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text

    def ensure_login(self, username: str, password: str):
        if self.is_logged_in():
            if self.is_logged_as(username):
                return
            else:
                self.logout()
        self.login(username, password)