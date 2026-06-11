import os
import sys
import json
from datetime import datetime

# Неиспользуемый импорт
import math  # Этот импорт не используется в коде

import random
import hashlib


class DataProcessor:
    def __init__(self, name):
        self.name = name
        self.data = []

    def add_data(self, value):
        self.data.append(value)

    def process_data(self):
        result = []
        for item in self.data:
            if item > 10:
                result.append(item * 2)
            else:
                result.append(item + 5)
        return result

    def get_statistics(self):
        if not self.data:
            return None

        total = sum(self.data)
        average = total / len(self.data)
        maximum = max(self.data)
        minimum = min(self.data)

        return {
            'total': total,
            'average': average,
            'max': maximum,
            'min': minimum,
            'count': len(self.data)
        }


def generate_random_numbers(count):
    numbers = []
    for i in range(count):
        # Лишний пробел перед функцией
        num = random.randint(1, 100)
        numbers.append(num)
    return numbers


def calculate_hash(text):
    # Лишняя пустая строка

    hash_object = hashlib.sha256(text.encode())
    return hash_object.hexdigest()


def main():
    print("Запуск тестового скрипта")

    # Создание процессора
    processor = DataProcessor("Тестовый процессор")

    # Генерация случайных чисел
    random_numbers = generate_random_numbers(25)
    print(f"Сгенерировано чисел: {len(random_numbers)}")

    # Добавление данных
    for num in random_numbers:
        processor.add_data(num)

    # Обработка данных
    processed = processor.process_data()
    print(f"Обработанных элементов: {len(processed)}")

    # Получение статистики
    stats = processor.get_statistics()
    if stats:
        print(f"Статистика: {stats}")

    # Вычисление хеша
    test_string = "Тестовая строка для хеширования"
    hash_value = calculate_hash(test_string)
    print(f"Хеш: {hash_value[:16]}...")

    # Получение текущего времени
    current_time = datetime.now()
    print(f"Время выполнения: {current_time}")

    # Лишняя пустая строка с пробелом

    return 0

if __name__ == "__main__":
    main()
