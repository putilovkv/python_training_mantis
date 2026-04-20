from fixture.base_helper import BaseHelper
from telnetlib import Telnet


class JamesHelper(BaseHelper):

    def __init__(self, app):
        super().__init__(app)
        self.james_config = app.config["james"]

    def ensure_user_exists(self, username, password):
        session = JamesHelper.Session(
            self.james_config["host"], self.james_config["port"], self.james_config["username"], self.james_config["password"])
        if session.is_user_registered(username):
            session.reset_password(username, password)
        else:
            session.create_user(username, password)
        session.quit()

    class Session:

        def __init__(self, host, port, username, password):
            self.telnet = Telnet(host, port, 5)
            self.read_until("Login id:")
            self.write(username)
            self.read_until("Password:")
            self.write(password)
            self.read_until("Welcome root. HELP for a list of commands")

        def read_until(self, text):
            self.telnet.read_until(text.encode('ascii'), 5)

        def write(self, text):
            self.telnet.write(text.encode('ascii') + b"\n")

        def is_user_registered(self, username):
            self.write(f"verify {username}")
            res = self.telnet.expect([b"exists", b"does not exist"])
            return res[0] ==  0

        def create_user(self, username, password):
            self.write(f"adduser {username} {password}")
            self.read_until(f"User {username} added")

        def reset_password(self, username, password):
            self.write(f"setpassword {username} {password}")
            self.read_until(f"Password for {username} reset")

        def quit(self):
            self.write("quit")