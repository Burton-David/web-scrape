import requests
from typing import Dict, Union


def web_scrape(url: str, method: str = 'GET', headers: Dict[str, str] = None, params: Dict[str, Union[str, int]] = None,
               cookies: Dict[str, str] = None, timeout: int = 30, retries: int = 0) -> str:
    """
    Scrape the HTML of the specified URL.

    Parameters:
        url (str): The URL to scrape.
        method (str): The HTTP method to use for the request (GET or POST).
        headers (Dict[str, str]): A dictionary of HTTP headers to send with the request.
        params (Dict[str, Union[str, int]]): A dictionary of query parameters to include in the request.
        cookies (Dict[str, str]): A dictionary of cookies to include in the request.
        timeout (int): The number of seconds to wait for the server to respond before giving up.
        retries (int): The number of times to retry the request if it fails.

    Returns:
        str: The HTML of the page at the specified URL.
    """
    s = requests.Session()
    s.max_redirects = 10
    s.headers.update(headers or {})
    s.auth = ('user', 'pass')

    for i in range(retries + 1):
        try:
            if method == 'GET':
                response = s.get(url, params=params,
                                 cookies=cookies, timeout=timeout)
            elif method == 'POST':
                response = s.post(url, data=params,
                                  cookies=cookies, timeout=timeout)
            else:
                raise ValueError("Invalid HTTP method: {}".format(method))
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            if i == retries:  # Last attempt
                raise Exception("Error while requesting URL: {}".format(e))
        else:
            return response.text
