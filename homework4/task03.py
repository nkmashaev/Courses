import sys


def my_precios_logger(text: str):
    """
    my_precios_logger function receives a string and write
    it to stderr if line starts with "error" and to stdout
    otherwise

    :param text: string to analyze
    """
    if text.startswith("error"):
        print(text, file=sys.stderr)
    else:
        print(text, file=sys.stdout)
