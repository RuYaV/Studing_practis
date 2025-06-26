import re
from tinydb import TinyDB
import pattern

def devide(str: str):
  parts = str.split(' --')
  return parts[1:]

def devide_names(parts):
  names = []
  for part in parts:
    name = part.split('=')[0]
    names.append(name)
  return names

def devide_info(parts):
  info = []
  for part in parts:
    value = part.split('=')[1]
    info.append(value)
  return info

def get_type(value):
  if re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", value):
    return "email"
  elif re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value):
    return "phone"
  elif re.match(r"^\d{2}\.\d{2}\.\d{4}$", value) or re.match(r"^\d{4}-\d{2}-\d{2}$", value):
    return "date"
  else:
    return "text"

def pattern(string: str):
  parts = devide(string)
  names = devide_names(parts)
  values = devide_info(parts)
  types = [get_type(v) for v in values]

  db = TinyDB('db.json')
  templates = db.all()
  db.close()

  for tpl in templates:
    expected = {k: v for k, v in tpl.items() if k != "name"}
    match = True

    for field, field_type in expected.items():
      if field in names:
        index = names.index(field)
        if types[index] != field_type:
          match = False
          break
      else:
        match = False
        break

    if match:
      return tpl["name"]

  result = {names[i]: types[i] for i in range(len(names))}
  return str(result)
