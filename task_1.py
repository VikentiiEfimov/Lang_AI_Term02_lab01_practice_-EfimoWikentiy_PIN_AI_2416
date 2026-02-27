class T1:
    def __init__(self, my_list):
        self.my_list = my_list

    def is_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def bubble_sort(self):
        self.my_list = [float(x) for x in self.my_list]
        n = len(self.my_list)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.my_list[j] > self.my_list[j + 1]:
                    self.my_list[j], self.my_list[j + 1] = self.my_list[j + 1], self.my_list[j]
                    swapped = True
            if not swapped:
                break
        return self.my_list

    def run(self):
        are_numbers = [self.is_number(item) for item in self.my_list]
        positive_exists = any(
            float(self.my_list[i]) > 0
            for i, is_num in enumerate(are_numbers)
            if is_num
        )
        result1 = (
            "Список содержит хотя бы одно положительное число."
            if positive_exists
            else "Список не содержит положительных чисел."
        )

        all_numbers = all(are_numbers)
        result2 = (
            "Список состоит только из чисел."
            if all_numbers
            else "Список состоит не только из чисел."
        )

        if all_numbers:
            result3 = self.bubble_sort()
        else:
            result3 = "Сортировка невозможна"

        return result1, result2, result3