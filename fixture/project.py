from fixture.base_helper import BaseHelper
from model.project import Project
from typing import List


class ProjectHelper(BaseHelper):

    def __init__(self, app):
        super().__init__(app)
        self.__project_cache = None

    def create(self, project: Project):
        wd = self.app.wd
        self.app.navigation.go_to_project_page()
        # init project creation
        wd.find_element_by_css_selector("[value='Create New Project']").click()
        self._fill_project_form(project)
        # submit project creation
        wd.find_element_by_css_selector("[value='Add Project']").click()
        self.__project_cache = None
        self.app.navigation.go_to_project_page()

    def count(self) -> int:
        wd = self.app.wd
        self.app.navigation.go_to_project_page()
        table = wd.find_elements_by_tag_name("table")[2]
        return len(table.find_elements_by_tag_name("tr")[2:])

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.go_to_project_page()
        self._open_project_modification_form_by_id(id)
        # submit deletion
        wd.find_element_by_css_selector("[value='Delete Project']").click()
        # confirm deletion
        wd.find_element_by_css_selector("[value='Delete Project']").click()
        self.__project_cache = None
        self.app.navigation.go_to_project_page()

    def get_project_list(self) -> List[Project]:
        if self.__project_cache is None:
            wd = self.app.wd
            self.app.navigation.go_to_project_page()
            self.__project_cache = []
            table = wd.find_elements_by_tag_name("table")[2]
            for row in table.find_elements_by_tag_name("tr")[2:]:
                tds = row.find_elements_by_tag_name("td")
                id = tds[0].find_element_by_tag_name("a").get_attribute("href").split('=')[-1]
                name = tds[0].text
                status = tds[1].text
                view_status = tds[3].text
                description = tds[4].text
                self.__project_cache.append(Project(id=id, name=name, status=status, view_status=view_status, description=description))
        return list(self.__project_cache)

    def _open_project_modification_form_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f"a[href='manage_proj_edit_page.php?project_id={id}']").click()

    def _fill_project_form(self, project: Project):
        self._change_field("name", project.name)
        self._change_select_by_visible_text("status", project.status)
        self._change_select_by_visible_text("view_state", project.view_status)
        self._change_field("description", project.description)