class ScrapeError(Exception):
    """
    Exception raised when there is an error while scraping a website.
    """
    pass


class InvalidUrlError(Exception):
    """
    Exception raised when an invalid URL is provided to the web scraper.
    """
    pass


class InvalidHttpMethodError(Exception):
    """
    Exception raised when an invalid HTTP method is provided to the web scraper.
    """
    pass


class InvalidHeadersError(Exception):
    """
    Exception raised when an invalid set of HTTP headers is provided to the web scraper.
    """
    pass


class InvalidCookiesError(Exception):
    """
    Exception raised when an invalid set of cookies is provided to the web scraper.
    """
    pass


class InvalidTimeoutError(Exception):
    """
    Exception raised when an invalid timeout value is provided to the web scraper.
    """
    pass
