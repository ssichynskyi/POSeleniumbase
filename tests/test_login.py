from seleniumbase import BaseCase
from framework.actions.common import open_and_login
from framework.utilities.credentials_helper import normal_user


class DemoSiteTests(BaseCase):
    def test_successful_login(self):
        open_and_login(self, normal_user)
        pass
