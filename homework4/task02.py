import urllib.request


def count_dots_on_i(url: str) -> int:
    """
    count_dots_on_i function accepts an URL as input
    and count how mane letters `i` are present in the
    HTML by this URL.

    :param url: url for processing
    :return: number of `i` letter
    :raise: ValueError
    """

    web_url = urllib.request.urlopen(url)
    if web_url.getcode() != 200:
        raise ValueError(f"Unreachable {url}")

    counter = 0
    for line in web_url.read().decode():
        for char in line:
            if char == "i":
                counter += 1
    return counter


if __name__ == "__main__":
    print(count_dots_on_i("https://example.com/"))
