from fixture.base_helper import BaseHelper


class NavigationHelper(BaseHelper):

    def __init__(self, app, base_url):
        super().__init__(app)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.base_url)