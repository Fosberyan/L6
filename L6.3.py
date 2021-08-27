class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'выгода': wage, "бонус": bonus}
class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_full_profit(self):
        return f"{sum(self._income.values())}"
m = Position("Кайл", 'Брахловскм', "Школьник, Житель Южного Парка", 25, 10)
print(f'Зовут: {m.get_full_name()}')
print(f'Социум: {m.position}')
print(f'Доход в семье: {m.get_full_profit()}')