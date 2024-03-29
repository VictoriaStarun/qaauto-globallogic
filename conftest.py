import pytest


class User:

    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Sergii"
        self.second_name = "Butenko"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user  # все що до - виконається до тесту, все що після - виконається після тесту

    user.remove()