[![Codacy Badge](https://app.codacy.com/project/badge/Grade/bacd0f8e775b454f8e52da10740dfa14)](https://www.codacy.com/gh/ssichynskyi/POSeleniumbase/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ssichynskyi/POSeleniumbase&amp;utm_campaign=Badge_Grade)
# POSeleniumbase
This is Page Object friendly wrapper around famous UI testing framework
[Seleniumbase]: https://github.com/seleniumbase/SeleniumBase

## Why this project
Seleniumbase is a feature-rich, well-maintained UI testing framework, however by design
it does not encourage the usage of OOP in tests, code-reuse and Page Object as example.

Such approach does not allow to create a large and easy maintainable test coverage.
Although it is possible to find in SeleniumBase repo the example of Page Object usage,
it's too simplified and not usable (there pages are only holders for locators).

Because of the nature of SeleniumBase, it's necessary to provide BaseCase object
to all Page Objects and Page Elements. Which means one extra parameter by default for
every object that uses WebDriver API. You'll see it inside.

## Content
I'm still working on this project in order to provide a clean version of this wrapper.
Still, you can already use it for your needs.
Just replace modules with AUT-specific files with your own:

### Must have modules
- framework/ui/elements/base.py
- framework/ui/pages/base.py
- framework/ui/pages/base_page.py

### Optional modules
- config/seleniumbase_config.py
- framework/utilities/credentials_helper.py

All the rest are just examples which might me helpful or even highly reusable in your case.

### Usage
You are free to use it any way you like, and it will still work.
Just in order to get maximum from this wrapper, these rules of thumb apply:

1. Use CSS selectors as locators everywhere
   (anyway, nearly all Selenium By locators at the end are converted to css :-))

2. Differentiate between entities:

   **Elements** - are parts of the page: buttons, labels, links, lists of items, etc
   (read more: framework/ui/elements/base.py about creation of new elements).

   **Pages** (Page Objects) - it's an object (model) which reflects the content of a
   Web page, or it's meaningful part. Page Objects shall contain Elements and their
   locators (read more: framework/ui/pages/base_page.py). As well as it's own URL and
   some basic functionality like refresh(). Do not put user functions there nor verification.

   **Actions** - repeatable interactions of the simulated user with Pages or Elements.
   This is the right place to store such typical user routines like: login/logout, etc.
   (read more: framework/actions/common.py)

   **Verificators** - some complex helpers for verification. Something repeatable and 
   bigger, than one line probably shall land in this module.
   (read more: framework/verificators/\_\_init\_\_.py)

3. If possible, inside test cases give preference to those that are to the left of another:
   action > page objects > page elements > direct calls of BaseCase (normally shall be avoided)

4. That might be not always easy to understand if this shall be a Page or and Element.
For this case I recommend the following:
   - something which is strictly bound to a certain URL is Page
   - something that is locatable on the page is Element 
   - if Element is present on many URLs, it's better to use it directly or via actions

### Run the tests
1. Install python3 and pip
2. Install pipenv
```console
$pip install pipenv
```
3. Clone this repo
```console
$git clone https://github.com/ssichynskyi/web_testing.git
```
4. Create and customize files:
   - .env from .env.example
   (if you want to run the existing tests, put in .env credentials
   of this website: <https://www.saucedemo.com/>. They are written just on the main page)

   - config/seleniumbase_config from config/seleniumbase_config.example

5. Customize tests/pytest.ini or nose config files if necessary
6. In the root project folder execute

```console
$pipenv shell
$cd tests
$python -m pytest 
```

for more test options see:
<https://github.com/seleniumbase/SeleniumBase>
