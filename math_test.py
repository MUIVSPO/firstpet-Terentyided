import random

# Функция для генерации случайного математического выражения
def generate_question():
    # Список операций
    operations = ['+', '-', '*', '/']
    
    # Выбор случайной операции
    operation = random.choice(operations)
    
    # Генерация случайных чисел для операндов
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    
    # Если операция деления, гарантируем, что делитель не равен нулю
    if operation == '/':
        num1 = num1 * num2  # чтобы деление было целым
    
    # Формируем выражение и правильный ответ
    if operation == '+':
        question = f"{num1} + {num2}"
        answer = num1 + num2
    elif operation == '-':
        question = f"{num1} - {num2}"
        answer = num1 - num2
    elif operation == '*':
        question = f"{num1} * {num2}"
        answer = num1 * num2
    elif operation == '/':
        question = f"{num1} / {num2}"
        answer = num1 // num2  # целочисленное деление
    
    return question, answer

# Основная функция теста
def math_test():
    correct_answers = 0
    incorrect_answers = 0
    total_questions = 5  # Количество вопросов в тесте

    for i in range(total_questions):
        question, correct_answer = generate_question()
        print(f"Вопрос {i+1}: {question}")
        
        # Получаем ответ пользователя
        user_answer = input("Ваш ответ: ")

        try:
            # Преобразуем ответ пользователя в число
            user_answer = int(user_answer)
        except ValueError:
            print("Ошибка! Введите число.")
            continue
        
        # Проверяем правильность ответа
        if user_answer == correct_answer:
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"Неправильно! Правильный ответ: {correct_answer}")
            incorrect_answers += 1

    # Выводим результаты теста
    print(f"\nТест завершён.")
    print(f"Правильных ответов: {correct_answers}")
    print(f"Неправильных ответов: {incorrect_answers}")
    
    # Оценка результата
    if correct_answers == total_questions:
        print("Отличный результат!")
    elif correct_answers >= total_questions // 2:
        print("Хороший результат!")
    else:
        print("Нужно подтянуть знания.")

# Запуск теста
if __name__ == "__main__":
    math_test()
