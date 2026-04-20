# -*- coding: utf-8 -*-
from datetime import datetime
from model.project import Project


def test_add_project(app):
    old_projects = app.soap.get_project_list()
    project = Project(name=f"test project {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", status="development", view_status="public", description="test description")
    app.project.create(project)
    new_projects = app.soap.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)