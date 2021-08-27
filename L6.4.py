class Car:
    def __init__(self, speed: int, color: str, name: str, police: bool):
        self._speed = speed
        self._color = color
        self._name = name
        self._police = police

    def speed(self) -> None:
        print(f'Скорость тачки {self._name}  {self._speed} км\ч')

    def go(self) -> None:
        print(f'{self._name} гонит')

    def stop(self) -> None:
        print(f'{self._name} отановилась')

    def turn(self, direction) -> None:
        print(f'{self._name} поворачивает на {direction}.')

class WorkCar(Car):
    def speed(self) -> None:
        if self._speed > 60:
            print('Перемещение во времени - 120.')

        Car.speed(self)

class SportCar(Car):
    pass

class TownCar(Car):
    def speed(self) -> None:
        if self._speed > 120:
            print('За семью скорость я разовью  - 60.')

        Car.speed(self)

class PoliceCar(Car):
    pass

def run_car(car: Car) -> None:
    car.go()
    car.turn('лев')
    car.turn('назад')
    car.turn('прав')
    car.turn('перед')
    car.speed()
    car.stop()
    print('')
run_car(SportCar(210, 'зеленоглаза', 'такси', False))
run_car(TownCar(120, 'сбелый мустанг', 'Доменика', False))
run_car(WorkCar(180, 'серебристая', 'Де Лориан', False))