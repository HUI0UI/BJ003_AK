import os
import sys
sys.path.append(os.getcwd())
from v4.tools.read_yaml import read_yaml

import pytest

from v4.page.page_login import PageLogin


def get_data():
    arrs = []
    for i in read_yaml().values():
        arrs.append((i.get("username"), i.get("pwd")))
    return arrs

class TestLogin(object):
    def setup_class(self):
        self.login = PageLogin()
    def teardown_class(self):
        self.login.driver.quit()
    @pytest.mark.parametrize("phone,pwd",get_data())
    def test_login(self,phone,pwd):
        self.login.page_login(phone,pwd)


# pytest.main("-s test_login.py")