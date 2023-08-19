# Тестовое задание hammer_systems

## Запуск

###### Для запуска необходимы docker и docker-compose
###### [Инструкции по установке докера](https://docs.docker.com/engine/install/)

#### Шаги:

Склонировать репозиторий
```bash
git clone git@github.com:jingleMyBells/hammer_test.git
```

Перейти в каталог с проектом и конфигурационными файлами развертки
```bash
cd hammer_test/deploy
```

Создать файл с переменными окружения по образу и подобию env-example.txt
```bash
  cat env-example.txt > .env
```

Запустить проект 
```bash
  docker-compose up
```

API будет отвечать по адресу http://localhost
```http
  POST /api/v1/request_code/
```
```http
  POST /api/v1/request_token/
```
```http
  GET /api/v1/user/{user_id}/
```
```http
  POST /api/v1/user/{user_id}/add_referrer/
```

Документация API будет доступна по адресам:
```http
  http://localhost/api/schema/swagger-ui/
```
```http
  http://localhost/api/schema/redoc/
```

## Проект развернут по адресу:

## Проект развернут по адресу:
```http
  94.198.217.113
```

###### Погонять тесты можно в:
```bash
  cd hammer_test/hammes_referral
  pytest
```

###### Заметки:

`Формулировка ТЗ позволила этого не делать, но по-хорошему нужны проверки 
на взаимную реферальность пользователей, а так же, возможно, на хронологию 
регистраций пользователей для соблюдения очевидно бизнес-цели реферальной системы`
