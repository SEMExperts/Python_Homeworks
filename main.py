def parse_parameters(str):
    try:
        lst = str[str.find('?') + 1:].split('&')
        key = []
        value = []
        for i in range(len(lst)):
            key.append(lst[i].split('=')[0])
            value.append(lst[i].split('=')[1])

        return dict(zip(key, value))
    except IndexError:
        return {}


def parse_cookies(str):
    try:
        str = str.replace(';', ' ')
        lst = str.split()
        key = []
        value = []
        for i in range(len(lst)):
            key.append(lst[i].split('=')[0])
            value.append(lst[i].split('=')[1])

        return dict(zip(key, value))
    except IndexError:
        return {}


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    print(parse_parameters('https://example.com/'))
    print(parse_parameters('http://example.com?product=1234&utm_source=google'))
    print(parse_parameters('https://example.com/products/women?category=dresses&color=green'))
    print(parse_parameters('https://example.com/products/women/dresses/green.html?limit=20&sessionid=123'))
    print(parse_parameters('example.com?type=dress&color=green'))
    print(parse_parameters('http://www.examples.com/search?category=shoe&brand=nike&color=red&size=5&pricefrom=10&priceto=1000.'))
    print(parse_parameters('http://www.example.com?shopping-category=shoes&sort-by=size&sort-order=asc'))
    print(parse_parameters('http://www.example.com?shopping-category=DVD-movies&sort-by=production-year&sort-order=asc'))
    print(parse_parameters('http://www.example.com?country=fr'))
    print(parse_parameters('https://www.onlinestor.com?product=socks&color=black&size=m'))

    # Tests for function "parse_cookies"
    print(parse_cookies(''))
    print(parse_cookies('name=Dima;'))
    print(parse_cookies('NAME=VALUE;expires=DATE;path=PATH;domain=DOMAIN_NAME;'))
    print(parse_cookies('NAME=VALUE;'))
    print(parse_cookies('NAME1=OPAQUE_STRING1; NAME2=OPAQUE_STRING2'))
    print(parse_cookies('CUSTOMER=WILE_E_COYOTE; path=/; expires=Wednesday,'))
    print(parse_cookies('PART_NUMBER=ROCKET_LAUNCHER_0001;'))
    print(parse_cookies('CUSTOMER=WILE_E_COYOTE; PART_NUMBER=ROCKET_LAUNCHER_0001; SHIPPING=FEDEX'))
    print(parse_cookies('PART_NUMBER=RIDING_ROCKET_0023;'))
    print(parse_cookies('PART_NUMBER=RIDING_ROCKET_0023; PART_NUMBER=ROCKET_LAUNCHER_0001'))


