import pytest
from work_with_pattern import pattern

def devide(str: str):
  parts = str.split(' --')
  names = []
  for i, part in enumerate(parts):
    if i == 0:
      continue
    name = part.split('=')
    names.append(name[0])
  return names


def test_first_pattern_correct1():
  str = 'app.py get_tpl --login=aaa@bbb.ru --tel=+7 999 888 77 66'
  assert pattern(str) == "Данные пользователя"

def test_first_pattern_correct2():
  str = 'app.py get_tpl --login=aaa@bbb.ru --tel=+7 999 888 77 66 --rrr=vasya'
  assert pattern(str) == "Данные пользователя"

def test_second_pattern_correct1():
  str = 'app.py get_tpl --customer=Potap --дата_заказа=2025-05-27 --order_id=ji54i2o --contact=+7 111 222 33 44'
  assert pattern(str) == "Форма заказа"

def test_second_pattern_correct2():
  str = 'app.py get_tpl --customer=Potap --дата_заказа=2025-05-27 --order_id=ji54i2o --contact=+7 111 222 33 44'
  assert pattern(str) == "Форма заказа"

def test_third_pattern_correct1():
  str = 'app.py get_tpl --f_name1=aaa@bbb.ru --f_name2=27.05.2025'
  assert pattern(str) == "Проба"

def test_third_pattern_correct2():
  str = 'app.py get_tpl --login=vasya --f_name1=aaa@bbb.ru --f_name2=27.05.2025'
  assert pattern(str) == "Проба"

def test_fourth_pattern_correct():
  str = 'app.py get_tpl --phone_number=+7 999 888 77 66 --information=vasya --login=va@sya.ru'
  assert pattern(str) == "Данные сотрудника"

def test_fourth_pattern_correct():
  str = 'app.py get_tpl --login=va@sya.ru --phone_number=+7 999 888 77 66 --information=vasya --xxx=vasilevich'
  assert pattern(str) == "Данные сотрудника"

def test_incorrect_email():
  str = 'app.py get_tpl --f_name1=aaa@bbb.ru'
  names = devide(str)
  assert pattern(str) == f"{{'{names[0]}': 'email'}}"

def test_incorrect_date_phone():
  str = 'app.py get_tpl --f_name1=27.05.2025 --f_name2=+7 903 123 45 78'
  names = devide(str)
  assert pattern(str) == f"{{'{names[0]}': 'date', '{names[1]}': 'phone'}}"

def test_incorrect_date_phone_text():
  str = 'app.py get_tpl --f_name1=27.05.2025 --f_name2=+7 903 123 45 78 --f_name3=546fty'
  names = devide(str)
  assert pattern(str) == f"{{'{names[0]}': 'date', '{names[1]}': 'phone', '{names[2]}': 'text'}}"

def test_incorrect_text_date1():
  str = 'app.py get_tpl --login=vasya --f_name2=27.05.2025'
  names = devide(str)
  assert pattern(str) == f"{{'{names[0]}': 'text', '{names[1]}': 'date'}}"

def test_incorrect_text_date2():
  str = 'app.py get_tpl --f_name1=vasya --f_name2=2025-05-27'
  names = devide(str)
  assert pattern(str) == f"{{'{names[0]}': 'text', '{names[1]}': 'date'}}"
