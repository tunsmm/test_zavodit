# Тестовое задание для Django разработчика

**Описание задания**: 

На Django реализовать список новостей с возможностью просматривать новость. Каждая новость должна включать теги. Нужно уметь заполнять новости в админке. Каждая новость состоит из Заголовка, Текста, Картинки, тегов. Нужно иметь страницы: Новости, Новость, Новости по тегу. Также должна быть страница статистике просмотров новостей. По REST-API новости можно получить/создать/удалить.

Дизайн не важен, можно использовать bootstrap. 

## Запуск проекта

1. Клонировать [репозиторий](https://github.com/tunsmm/test_zavodit.git)
2. Создать и запустить виртуальную среду

```bash
python -m venv venv
source venv/Scripts/activate
```

3. Установить нужные пакеты

```bash
pip install -r requirements.txt
```

4. Запустить сервер

```bash
python manage.py runserver
```

5. Перейти на локальный хост 127.0.0.1:8000 и проверить результат работы