# -*- coding: utf-8 -*-
import random
from datetime import datetime
from model.project import Project


def test_del_some_project(app):
    if len(app.soap.get_project_list()) == 0:
        app.project.create(Project(name=f"test project {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
    old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects