from framework.ui.elements.base import Item


class BasePage(Item):
    URL = None

    def __init__(self, infra):
        """Base class for all Page Objects

        Args:
            infra: infrastructure described in BaseCase class

        """
        super().__init__(infra)

    def open(self):
        self.do.open(self.URL)
