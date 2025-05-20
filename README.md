# cloud_test

# Задача 1

## FastAPI-приложение
- Получение имени хоста socket.gethostname()
- Получение IP клиента gethostbyname
- Получение переменной AUTHOR
- Возвращает JSON с полями hostname, ip_address, author

## Dockerfile:
- Базовый образ: python:3.11-slim
- Копирование app.py
- установка зависимостей из requirements.txt
- Открытие порта 8000
- установка ENV-переменной 

    docker login
    docker build -t mclov/cloude_app:v0.0 .
    docker push mclov/cloude_app:v0.0


# Задача 2

Арендовал машину с ubuntu 22.04 от клауд, чтобы не париться с установкой виртульной машины на свой комп.

## roles: Nginx Docker
    Установка Docker и зависимостей
    Установка Python Docker SDK
    Логин в приватный Docker Hub
    Запуск 3 контейнеров с образом `mclov/cloude_app:v0.0`
    Установка и настройка NGINX как балансировщика

## Команда запуска
    ansible-playbook -i inventory.ini site.yml

## round-robin
Самый простой алгоритм, подходящий для этой задачи
равномерно распределяет нагрузку. Не учитывает состояние контейнеров


# Задача 3

- Namespace — `intern-app` (для изоляции) 
- Deployment — 3 реплики приложения `mclov/cloude_app:0.0`
- Service — NGINX-like балансировка через `ClusterIP` или `NodePort`

## Команды

    kubectl apply -f namespace.yaml
    kubectl apply -f secret.yaml
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml