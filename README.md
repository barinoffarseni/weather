# weather
Получение прогнозы погоды.

# Инструкция по установке
1. Копируем docker-compose инструкцию:
```bash
cp docker-compose.example.yml docker-compose.yml
```
2. Копируем переменные окружения:
```bash
cp example.env .env
```
3. Заполните переменные окружения в файле .env!
4. Строим контейнеры
```bash
docker-compose build
```
5. Запускаем контейнеры
```bash
docker-compose up
```