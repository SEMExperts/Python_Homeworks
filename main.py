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
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse_parameters('http://example.com?product=1234&utm_source=google') == {'product': '1234', 'utm_source': 'google'}
    assert parse_parameters('https://example.com/products/women?category=dresses&color=green') == {'category': 'dresses', 'color': 'green'}
    assert parse_parameters('https://example.com/products/women/dresses/green.html?limit=20&sessionid=123') == {'limit': '20', 'sessionid': '123'}
    assert parse_parameters('example.com?type=dress&color=green') == {'type': 'dress', 'color': 'green'}
    assert parse_parameters('http://www.examples.com/search?category=shoe&brand=nike&color=red&size=5&pricefrom=10&priceto=1000.') == {'category': 'shoe', 'brand': 'nike', 'color': 'red', 'size': '5', 'pricefrom': '10', 'priceto': '1000.'}
    assert parse_parameters('http://www.example.com?shopping-category=shoes&sort-by=size&sort-order=asc') == {'shopping-category': 'shoes', 'sort-by': 'size', 'sort-order': 'asc'}
    assert parse_parameters('http://www.example.com?shopping-category=DVD-movies&sort-by=production-year&sort-order=asc') == {'shopping-category': 'DVD-movies', 'sort-by': 'production-year', 'sort-order': 'asc'}
    assert parse_parameters('http://www.example.com?country=fr') == {'country': 'fr'}
    assert parse_parameters('https://www.onlinestor.com?product=socks&color=black&size=m') == {'product': 'socks', 'color': 'black', 'size': 'm'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('NAME=VALUE;expires=DATE;path=PATH;domain=DOMAIN_NAME;') == {'NAME': 'VALUE', 'expires': 'DATE', 'path': 'PATH', 'domain': 'DOMAIN_NAME'}
    assert parse_cookies('NAME=VALUE;') == {'NAME': 'VALUE'}
    assert parse_cookies('NAME1=OPAQUE_STRING1; NAME2=OPAQUE_STRING2') == {'NAME1': 'OPAQUE_STRING1', 'NAME2': 'OPAQUE_STRING2'}
    assert parse_cookies('CUSTOMER=WILE_E_COYOTE; path=/; expires=Wednesday,') == {'CUSTOMER': 'WILE_E_COYOTE', 'path': '/', 'expires': 'Wednesday,'}
    assert parse_cookies('PART_NUMBER=ROCKET_LAUNCHER_0001;') == {'PART_NUMBER': 'ROCKET_LAUNCHER_0001'}
    assert parse_cookies('CUSTOMER=WILE_E_COYOTE; PART_NUMBER=ROCKET_LAUNCHER_0001; SHIPPING=FEDEX') == {'CUSTOMER': 'WILE_E_COYOTE', 'PART_NUMBER': 'ROCKET_LAUNCHER_0001', 'SHIPPING': 'FEDEX'}
    assert parse_cookies('PART_NUMBER=RIDING_ROCKET_0023;') == {'PART_NUMBER': 'RIDING_ROCKET_0023'}
    assert parse_cookies('PART_NUMBER=RIDING_ROCKET_0023; PART_NUMBER=ROCKET_LAUNCHER_0001') == {'PART_NUMBER': 'ROCKET_LAUNCHER_0001'}


