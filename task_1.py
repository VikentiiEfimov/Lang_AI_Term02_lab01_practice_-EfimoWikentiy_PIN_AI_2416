"""Создать программу, которая работает со списком. Пользователь вводит список в программу. Реализовать следующие действия:
2. С помощью встроенной функции all проверить состоят ли все элементы
списка только из чисел.
3. Отсортировать список с помощью реализованной самостоятельно функции
Sorted - пузырьком
"""


class T1:
    def __init__(self, my_list):
        self.my_list = my_list

    def is_tchislo(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def run(self):
        result = ("Список содержит хотя бы одно положительное число." 
                if any(
                    float(item) > 0 
                    for item in self.my_list 
                    if self.is_tchislo(item)
                    ) 
                else "Список не содержит положительных чисел.")
        return result