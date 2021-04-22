from framework.ui.elements.base import Item


class BasePage(Item):
    URL = None

    def __init__(self, infra):
        """Base class for all Page Objects

        Explanation:
            It's assumed that the main idea of Page Objects is to locate
            web elements, provide them to user 'as is' and provide
            some generic functions like open().

            You may think that it makes sense to add additional methods in PO
            which will incorporate several function calls:

                login_entry_field.write(login)
                password_entry_field.write(password)
                submit_button.click()

            in one method:

                login(login, password)

            However this is normally not recommended as it introduces additional
            and unnecessary level of abstraction inside the Framework while
            abstraction from all external interfaces is already in place.
            If you want to reduce the number of code for repeatable actions,
            it's better to use 'actions' module instead. Your code won't become
            more maintainable or pretty in most cases and you will simply
            write more code than necessary. Still, you are free to do so...

        Args:
            infra: object of Seleniumbase BaseCase class

        """
        super().__init__(infra)

    def open(self):
        """Opens page by it's URL"""
        self.do.open(self.URL)

    def refresh(self):
        """Refreshes this page"""
        self.do.refresh()
