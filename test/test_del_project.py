# -*- coding: utf-8 -*-
import random
from datetime import datetime
from model.project import Project


def test_del_some_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name=f"test project {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects