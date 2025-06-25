BASE_URL = "https://qa-scooter.praktikum-services.ru"
COURIER_URL = "/api/v1/courier"
ORDER_URL = "/api/v1/orders"

CREATE_COURIER_TWICE_ERROR_MESSAGE = 'Этот логин уже используется. Попробуйте другой.'
CREATE_COURIER_MISSING_FIELD_ERROR = 'Недостаточно данных для создания учетной записи'
LOGIN_COURIER_NOT_FOUND_ERROR = 'Учетная запись не найдена'

ORDER_PAYLOAD = {
    "firstName": "TestName",
    "lastName": "TestSurname",
    "address": "Test address, 123",
    "metroStation": "42",
    "phone": "+7 800 355 35 35",
    "rentTime": "42",
    "deliveryDate": "2026-06-03",
    "comment": "some comment",
    "color": []
}