
class BasePage:
    URL = None

    def __init__(self, infra):
        """Base class for all Page Objects

        Args:
            infra: infrastructure described in BaseCase class

        """
        self._do = infra

    @property
    def do(self):
        return self._do

    def open(self):
        self.do.opent(self.URL)
