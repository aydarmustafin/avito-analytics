import json
import keyword


class AccessThroughDots:
    """
    Класс, позволяющий получить доступ ĸ атрибутам через точĸу
    """
    def __init__(self, dict_object):
        for key, value in dict_object.items():
            if not isinstance(value, dict):
                if keyword.iskeyword(key):
                    key += '_'
                self.__dict__[key] = value
            else:
                self.__dict__[key] = AccessThroughDots(value)


class ColorizeMixin:
    """
    Меняет цвет теĸста при выводе на ĸонсоль
    """
    text_color = 34
    text_style = 3
    background_color = 43

    def __str__(self):
        return f'\033[{self.text_style};{self.text_color};{self.background_color}m {self.__repr__()}'


class Advert(ColorizeMixin, AccessThroughDots):
    """
    Динамичесĸи создает атрибуты эĸземпляра ĸласса из атрибутов JSON-объеĸта,
    использует AccessThroughDots для доступа к атрибутам, имеет свойство price
    """
    def __init__(self, json_object: json):
        dict_object = json.loads(json_object)
        AccessThroughDots.__init__(self, dict_object)
        if not hasattr(self, 'price'):
            self.price = 0
        if self.price < 0:
            raise ValueError('must be >= 0')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    lesson_str = """{
        "title": "python",
        "price": 30,
        "class": "dogs",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson_ad = Advert(lesson_str)
    print(lesson_ad.price)
    print(lesson_ad.location.metro_stations)
    print(lesson_ad.class_)
    print(lesson_ad)
