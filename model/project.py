from sys import maxsize


class Project:

    def __init__(self, id=None, name=None, status=None, view_status=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return f"{self.id}:{self.name};{self.description}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
            and self.name == other.name\
            and self.status == other.status\
            and self.view_status == other.view_status\
            and self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def fill_if_none(self, other):
        if self.name is None:
            self.name = other.name
        if self.status is None:
            self.status = other.status
        if self.view_status is None:
            self.view_status = other.view_status
        if self.description is None:
            self.description = other.description