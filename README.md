# Docker

1. В корневой папке проекта есть Dockerfile, который содержит
   инструкции для создания образа.
   Создать образ:

```
docker build . -t drf
```

Проверить, что образ создан, можно с помощью команды:

```bash
docker images
```

В списке образов должен быть образ drf.

2. Запустить контейнер с приложением:

```
docker run --name django-app -p 8000:8000 drf
```

3. Открыть стартовую страницу на хостовой машине:
   http://127.0.0.1:8000


4.
- - Создать контейнер, в котором будет развернута БД PostgreSQL.
- - Создать локально папку, в которую будут размещаться данные базы.

- - Создать локальную папку для хранения данных БД.

- - Убедиться, что порт 5432 свободен.

5. Запуск контейнера с PostgreSQL с помощью официального образа.

```
docker run --name db-postgres -e POSTGRES_PASSWORD=1234567 -v ~/Documents/python_developer/skypro/postgres-data:/var/lib/postgresql/data -p 5432:5432 -d postgres
```

6Проверка работы PostgreSQL

- Запустить оболочку bash, чтобы получить доступ к командной строке контейнера

```
docker exec -it db-postgres /bin/bash
```

- Запустить клиентскую утилиту командной строки PostgreSQL

```
psql -U postgres
```

- Создать БД

```
create database postgresDRF;
```

- Просмотерть список БД

```
\l
```

- Выход

```
\q
```

- Выход из контейнера

```
exit
```