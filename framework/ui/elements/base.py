"""Module contains base classes for web elements.

Foreword:
    It's assumed that all other web elements derived from the classes from this module
    Mixins are not self-sufficient objects. They shall be used only for inheritance.
    Treat mixin like an interface.
    When creating a new class, it's ok to inherit many mixins. No SOLID principles
    are affected by this. Still, make sure that you derive from only one non-mixing class.

General rules:
    - when creating a new web element (the entity which can have a meaningful locator),
    use UIElement and necessary number of mixins.
    - when dealing with more abstract entities like lists of similar items, i
"""
from abc import abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


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


class ClickableMixin:
    """Mixin which provides clickability for child class"""

    def click(self):
        self.do.click(self.locator, self.by)

    def click_if_visible(self):
        self.do.click_if_visible(self.locator, self.by)


class EditableTextMixin:
    """Mixin which provides feature of write text to child class"""

    def clear(self):
        """Clears text box field from all text"""
        self.do.clear(self.locator, self.by)

    def add_text(self, text):
        """Appends new text to the end of the text in text box"""
        self.do.add_text(self.locator, text, self.by)

    def write(self, text):
        """Rewrites the given text in text box"""
        self.do.write(self.locator, text, self.by)


class CheckableMixin:
    """Mixin which provides feature of check/uncheck for child class"""

    def check(self):
        """Checks checkbox/radio button"""
        self.do.select_if_unselected(self.locator, self.by)

    def uncheck(self):
        """Unchecks checkbox/radio button"""
        self.do.unselect_if_selected(self.locator, self.by)

    def checked(self):
        """Examines checkbox/radio button for status"""
        self.do.is_checked(self.locator, self.by)


class TextualMixin:
    """Mixin which provides features of non-editable text"""

    @property
    def text(self):
        return self.do.get_text(self.locator, self.by)


class SelectableMixin:
    """Mixin which provides navigation features in <select> / <options> menu"""

    def _select_option_by_text(self, text):
        self.do.select_option_by_text(self.locator, text, self.by)

    def _select_option_by_value(self, value):
        self.do.select_option_by_value(self.locator, value, self.by)

    def _select_option_by_index(self, index):
        self.do.select_option_by_index(self.locator, index, self.by)

    def _highlight_option_by_text(self, text):
        self.do.hover_on_element(text, By.LINK_TEXT)


class ButtonWithText(UIElement, ClickableMixin, TextualMixin):

    def __init__(self, infra, locator, by=By.CSS_SELECTOR):
        """Button with text label

        Args:
            infra: Seleniumbase BaseCase object
            locator: string representation of locator
            by: Selenium By object

        """
        super().__init__(infra, locator, by)


class ButtonWithIcon(UIElement, ClickableMixin):
    """Button with only icon"""

    def __init__(self, infra, locator, by=By.CSS_SELECTOR):
        super().__init__(infra, locator, by)


class EditableTextField(UIElement, ClickableMixin, EditableTextMixin):
    """Editable text input field"""

    def __init__(self, infra, locator, by=By.CSS_SELECTOR):
        super().__init__(infra, locator, by)


class TextLabel(UIElement, TextualMixin):
    """Normal non-editable text label"""

    def __init__(self, infra, locator, by=By.CSS_SELECTOR):
        super().__init__(infra, locator, by)


class SelectMenu(UIElement, SelectableMixin):
    """Menu made from <select> / <option> tags"""

    def __init__(self, infra, locator, by=By.CSS_SELECTOR):
        super().__init__(infra, locator, by)


class BaseListElement(Item):
    def __init__(self, infra):
        """Base class for list of identical items

        Remark:
            shall not be used for lists made of <select>/<option> tags.
            Please use object inherited from SelectableMixin
            Shall be used for lists of identical items made by <div>, <li>, <ul>

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra)

    @property
    @abstractmethod
    def member_locators(self) -> list:
        """Contains locators for all inner elements"""

    def update_locators(self, prefix) -> None:
        """Adds prefix for all member locators

        Assumption:
            prefix is a css selector which allows to identify this
            instance of ListElement uniquely

        Idea:
            Make a unique locator from non-unique locator of member and
            unique prefix (which supposed to be a unique locator of this web element

        Args:
              prefix: string representing a unique css selector of this instance
        """
        for member in self.member_locators:
            self.__setattr__(member, f'{prefix} > {self.__getattribute__(member)}')


class BaseListOfElements(Item):
    """List of elements of the same class"""

    def __init__(
            self,
            infra,
            element_type: type,
    ):
        super().__init__(infra)
        self._element_type = element_type
        self._items = self._get_items(By.CSS_SELECTOR)

    def _get_items(self, by):
        web_elements = self.do.find_visible_elements(self._element_type.LOCATOR, by)
        selectors = tuple(map(lambda x: generate_css_selector(self.do, x), web_elements))
        elements = [self._element_type(self.do) for _ in selectors]
        for element, selector in zip(elements, selectors):
            element.update_locators(selector)
        return elements

    def get_by_property_value(self, prop_call: str, value, full_match=True):

        for item in self._items:
            prop = item
            try:
                for prop_name in prop_call.split('.'):
                    prop = prop.__getattribute__(prop_name)
                real_value = prop
            except AttributeError as e:
                raise ValueError(f'List item has no such property {prop_call}') from e
            if full_match:
                if value == real_value:
                    return item
            else:
                if value in real_value:
                    return item
        msg = f"""Unable to locate Inventory item with property {prop_call} and value {value}"""
        raise Exception(msg)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def __getitem__(self, index):
        return self._items[index]


def generate_css_selector(infra, web_element: WebElement) -> str:
    """Generates the css selector from a given Selenium WebElement

    Args:
        infra: Seleniumbase BaseCase object
        web_element: object of type Selenium WebElement

    Returns:
        css selector as string

    """
    JS_BUILD_CSS_SELECTOR = \
        "for(var e=arguments[0],n=[],i=function(e,n){if(!e||!n)return 0;f" + \
        "or(var i=0,a=e.length;a>i;i++)if(-1==n.indexOf(e[i]))return 0;re" + \
        "turn 1};e&&1==e.nodeType&&'HTML'!=e.nodeName;e=e.parentNode){if(" + \
        "e.id){n.unshift('#'+e.id);break}for(var a=1,r=1,o=e.localName,l=" + \
        "e.className&&e.className.trim().split(/[\\s,]+/g),t=e.previousSi" + \
        "bling;t;t=t.previousSibling)10!=t.nodeType&&t.nodeName==e.nodeNa" + \
        "me&&(i(l,t.className)&&(l=null),r=0,++a);for(var t=e.nextSibling" + \
        ";t;t=t.nextSibling)t.nodeName==e.nodeName&&(i(l,t.className)&&(l" + \
        "=null),r=0);n.unshift(r?o:o+(l?'.'+l.join('.'):':nth-child('+a+'" + \
        ")'))}return n.join(' > ');"
    return infra.execute_script(JS_BUILD_CSS_SELECTOR, web_element)
