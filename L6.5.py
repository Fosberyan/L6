class Stationary:

    def __init__(self, title="мемчики"):
        self.title = title

    def draw(self):
        print(f'Нарисую {self.title}')

class Pen(Stationary):
    def draw(self):
        print(f'Ручкой нарисую  {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'Окрась в черное {self.title}')

class Marker(Stationary):
    def draw(self):
        print(f'Ногой нарисую {self.title}')

stat = Stationary()
stat.draw()

mark = Marker()
pencil = Pencil()

mark.draw()
pencil.draw()
