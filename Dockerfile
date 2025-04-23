FROM python:3.11-slim

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Установка переменной окружения
ENV PYTHONUNBUFFERED=1

# Запуск
CMD ["python", "main.py"]
