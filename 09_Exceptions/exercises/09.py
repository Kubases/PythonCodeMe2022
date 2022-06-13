import webbrowser


class URLError(Exception):
    pass


def get_url():
    prefixes = ('https://', 'http://', 'www.')
    suffixes = ('.pl', '.com')
    url = input('Write address of website -> ')
    if not url.startswith(prefixes):
        raise URLError("Prefix incorrect")
    if not url.endswith(suffixes):
        raise URLError("Suffix incorrect")
    return url


def main():
    while True:
        try:
            current_url = get_url()
        except Exception as err:
            print(err)
        else:
            break

    webbrowser.open(current_url)


main()
