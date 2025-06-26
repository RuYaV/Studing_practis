from tinydb import TinyDB

db = TinyDB('db.json')
db.truncate()

db.insert({
  "name": "Данные пользователя",
  "login": "email",
  "tel": "phone"
})
db.insert({
  "name": "Форма заказа",
  "customer": "text",
  "order_id": "text",
  "дата_заказа": "date",
  "contact": "phone"
})
db.insert({
  "name": "Проба",
  "f_name1": "email",
  "f_name2": "date"
})
db.insert({
    "name": "Данные сотрудника",
    "login": "email",
    "phone_number": "phone",
    "information": "text"
})

db.close()
