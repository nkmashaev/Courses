import urllib.request
from urllib.error import HTTPError


def count_dots_on_i(url: str) -> int:
    """
    count_dots_on_i function accepts an URL as input
    and count how mane letters `i` are present in the
    HTML by this URL.

    :param url: url for processing
    :return: number of `i` letter
    :raise: ValueError
    """

    try:
        return sum(
            sum(1 for char in line.decode() if char == "i")
            for line in urllib.request.urlopen(url)
        )
    except HTTPError as e:
        raise ValueError(f"Unreachable {url}") from e


if __name__ == "__main__":
    print(count_dots_on_i("https://example.com/"))
