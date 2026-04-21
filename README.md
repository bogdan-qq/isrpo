📚 Каталог: хранение данных о книге (Вариант 27)

👥 Состав команды

Роль | Участник | Модуль


Бэкенд / Поиск | Лесников Сергей | Модуль B (поиск по автору или названию)

Бэкенд / Рекомендации | Малышев Богдан | Модуль C (рекомендации книг)

Бэкенд / Каталог | Исайкин Егор | Модуль A (хранение данных о книге)




🛠 Описание модулей

Модуль A — хранение данных о книгах

Модуль B — поиск книг по автору или названию

Модуль C — выдача случайных рекомендаций




🚀 Инструкция по запуску

Клонирование репозитория

git clone https://github.com/bogdan-qq/isrpo.git
cd isrpo




Запуск компонентов

python 9_modul_a.py
python 9_modul_b.py
python 9_modul_c.py

🧪 Разработка и испытания

Установка окружения

pip install pytest flake8 black




Проверка кода

black 9_modul_a.py 9_modul_b.py 9_modul_c.py


flake8 9_modul_a.py 9_modul_b.py 9_modul_c.py



Запуск тестов

pytest tests/ -v

📊 Статус тестов

Все модули успешно прошли проверку:

tests/test_catalog.py::test_add_book ПРОЙДЕНО

tests/test_catalog.py::test_get_all_books ПРОЙДЕНО

tests/test_search.py::test_search_by_title ПРОЙДЕНО

tests/test_search.py::test_search_by_author ПРОЙДЕНО

tests/test_search.py::test_search_not_found ПРОЙДЕНО

tests/test_recommendation.py::test_get_random_book ПРОЙДЕНО

tests/test_recommendation.py::test_empty_catalog ПРОЙДЕНО

✅ 7 тестов пройдено за 0.04 с
