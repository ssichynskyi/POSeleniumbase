"""
To override default Seleniumbase settings.py,
change the values here and add "--settings=custom_settings.py" when running.
"""

# Default timeout values for waiting for page elements to appear.
MINI_TIMEOUT = 2
SMALL_TIMEOUT = 5
LARGE_TIMEOUT = 8
EXTREME_TIMEOUT = 12

# If False, only logs from the most recent test run will be saved.
ARCHIVE_EXISTING_LOGS = False
ARCHIVE_EXISTING_DOWNLOADS = False

# Waiting for Document.readyState to be "Complete" after browser actions.
WAIT_FOR_RSC_ON_PAGE_LOADS = True
WAIT_FOR_RSC_ON_CLICKS = True
WAIT_FOR_ANGULARJS = True

# Changing the default behavior of Demo Mode. Activate with: --demo_mode
DEFAULT_DEMO_MODE_TIMEOUT = 0.5
HIGHLIGHTS = 4
DEFAULT_MESSAGE_DURATION = 2.55

# Disabling the Content Security Policy of the browser by default.
DISABLE_CSP_ON_FIREFOX = True
DISABLE_CSP_ON_CHROME = True

# If True and --proxy=IP_ADDRESS:PORT is invalid, then error immediately.
RAISE_INVALID_PROXY_STRING_EXCEPTION = True

# Default browser resolutions when opening new windows for tests.
# (Headless resolutions take priority, and include all browsers.)
# (Firefox starts maximized by default when running in GUI Mode.)
CHROME_START_WIDTH = 1250
CHROME_START_HEIGHT = 840
HEADLESS_START_WIDTH = 1440
HEADLESS_START_HEIGHT = 1880
