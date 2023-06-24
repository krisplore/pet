import datetime  # использую для получания текущего времени
import secrets  # использую для создания уникальных строчек-приглашений в функции generate_invite
import string  # использую для создания списка - алфавита, для создания уникальных строчек-приглашений
import uuid  # использую для создания id источника, чтобы обеспечить уникальность идентификатора


AMOUNT_OF_INVITATIONS = 2
INVITATION_LENGTH = 6


#  разделяет строку по знаку запятой, создает список подстрок
#  удаляет яет начальные и конечные пробелы, а цикл for проходит по каждой подстроке и добавляет ее в список tags
def extract_tags(tags):  # если запятой нет, в список добавляется только один элемент - вся строка tags
    tags = [item.strip() for item in tags.split(',') if item.strip()]
    return tags


# функция генерирует уникальный идентификатор на основе случайных чисел
# функция str преобразует объект UUID в строку
# функция в целом возвращает строковое представление UUID04
def generate_id():
    return str(uuid.uuid4())


# в настоящем - возвращает 1 - соответствует описанию типа human
def set_type():
    return 1


# генерирует список приглашений, состоящий из случайно сгенерированных строк из 6 символов английского алфавита в
# верхнем регистре без спорных символов
# создается список символов англ.яз. + цифры - спорные символы
# внутри цикла генератор списка, чтобы создать случайную строку из списка символов установленной длины
# дальше строка добавляется в список invite, а он по итогу возвращается
def generate_invite():
    alphabet = string.ascii_uppercase + string.digits
    excluded_characters = 'IiOo01l'
    characters = [c for c in alphabet if c not in excluded_characters]
    invite = []
    for _ in range(AMOUNT_OF_INVITATIONS):
        invite.append(''.join((secrets.choice(characters) for _ in range(INVITATION_LENGTH))))
    return invite


# внутри функции вызывается метод now() - возвращает объект, представляющий текущее время
# в формате datetime.datetime на основе этого классе
# затем вызывается метод timestamp() - возвращает отметку времени в виде числа float (кол-во секунд с 1.01.70)
# функция int() преобразует отметку в целое число int
def get_time():
    return int(datetime.datetime.now().timestamp())


# функция была необходима для перевода строк моего словаря, потому что функции gettext не принимает в качестве
# аргумента тип данных dict
# функция gettext.translation создает объект, который будет использоваться для перевода текста на английский язык
# метод install устанавливает объект translation как текущий переводчик
# translation.gettext(string) - выполняется перевод текста на английский

# def translate_string(string):
#     translation = gettext.translation('pet_project', localedir='locales', languages=['en'])
#     translation.install()
#     return translation.gettext(string)


# обработка аргументов командной строки, создание словаря source
# вывод информации на экран и запись в данных в yaml файл

