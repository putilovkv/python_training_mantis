from typing import List
from requests import Session
from suds.client import Client
from suds import WebFault
from fixture.base_helper import BaseHelper
from model.project import Project


class SoapHelper(BaseHelper):

    def __init__(self, app):
        super().__init__(app)
        self.soap_config = app.config["soap"]

    def can_login(self, username, password):
        client = Client(self.soap_config["url"])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self) -> List[Project]:
        client = Client(self.soap_config["url"])
        projects_soap = client.service.mc_projects_get_user_accessible(self.soap_config["username"], self.soap_config["password"])
        return [Project(id=str(s.id), name=s.name, status=s.status.name, view_status=s.view_state.name, description=s.description) for s in projects_soap]