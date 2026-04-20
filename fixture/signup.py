import re
from fixture.base_helper import BaseHelper


class SignupHelper(BaseHelper):

    def new_user(self, username, email, password):
        wd =self.app.wd
        self.app.navigation.open_signup_page()
        self._change_field("username", username)
        self._change_field("email", email)
        wd.find_element_by_css_selector("input[type='submit']").click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmation_url(mail)

        self.app.navigation.open_page(url, 1) #при открытии указанного url страница как будто дважды загружается - все поля очищаются, поэтому нужно подождать
        self._change_field("password", password)
        self._change_field("password_confirm", password)
        wd.find_element_by_css_selector("input[value='Update User']").click()

    def extract_confirmation_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)