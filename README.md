# QRKot
### Автор 
- [Ильин Данила](https://github.com/RH1532)
### Техно-стек 
- FastAPI
- Python
- Alembic
- Google API

## Оглавление
- [QRKot](#qrkot)
- [Автор](#автор)
- [Техно-стек ](#техно-стек)
- [Развёртывание проекта](#Развёртывание-проекта)
- [Команды](#команды)
- [Справка](#справка)
- [Документация](#документация-api)


## Развёртывание проекта

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/RH1532/yacut.git
```

```
cd cat_chaity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
### Команды
- `alembic upgrade head`: Применение миграций.
- `uvicorn app.main:app`: Запустить проект. 
## Справка
## Проект QRKot — это приложение для Благотворительного фонда поддержки котиков
### Основные возможности проекта:

Проекты

В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

Пожертвования

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

Пользователи

Целевые проекты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.
# Документация API
- [Скачайте спецификацию проекта](https://github.com/RH1532/yacut/blob/master/openapi.yml)
- Для просмотра документации загрузите файл на [сайт](https://redocly.github.io/redoc/). Вверху страницы есть кнопка Upload a file, нажмите её и загрузите скачанный файл. Спецификация проекта отобразится в формате ReDoc.