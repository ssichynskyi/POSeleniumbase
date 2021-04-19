from selenium.webdriver.common.by import By


class Item:
    def __init__(self, infra):
        """Base class for all UI elements.

        Explanation:
            this class is needed in order to distribute BaseCase
            context and functions to all elements and page objects.
            This is required because of Seleniumbase BaseCase god object

        Args:
            infra: infrastructure described in BaseCase class

        """
        self._do = infra

    @property
    def do(self):
        return self._do


class UIElement(Item):
    def __init__(self, infra, locator, by=By.CSS_SELECTOR):
        super().__init__(infra)
        self.locator = locator
        self.by = by

    def visible(self):
        return self.do.is_element_visible(self.locator, self.by)

    def enabled(self):
        return self.do.is_element_enabled(self.locator, self.by)


class Clickable:
    """Mixin which provides clickability for child class"""

    def click(self):
        self.do.click(self.locator, self.by)

    def click_if_visible(self):
        self.do.click_if_visible(self.locator, self.by)


class EditableText:
    """Mixin which provides feature of write text to child class"""
    def clear(self):
        self.do.clear(self.locator, self.by)

    def add_text(self, text):
        self.do.add_text(self.locator, text, self.by)

    def write(self, text):
        self.do.write(self.locator, text, self.by)


class Checkable(Clickable):
    """Mixin which provides feature of check/uncheck for child class"""
    def check(self):
        self.do.select_if_unselected(self.locator, self.by)

    def uncheck(self):
        self.do.unselect_if_selected(self.locator, self.by)

    def checked(self):
        self.do.is_checked(self.locator, self.by)


class Textual:
    """Mixin which provides features to non-editable text"""
    def text(self):
        return self.do.get_text(self.locator, self.by)
