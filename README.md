# Копируем .env
cp example.env .env

# билдим контейнеры
docker-compose build

# поднимаем контейнеры
docker-compose up

# наслаждаемся

# P.S. после свитча ветки нужно перезапустить контейнер веба
