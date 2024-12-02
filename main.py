from abc import ABC


class Mario(ABC):

    def __init__(self):
        pass

    def jump(self):
        pass

    def shoot(self):
        pass

    def powerUp(self):
        pass

    def powerDown(self):
        pass


class State:
    def __init__(self, mario):
        self.mario = mario

    def jump(self):
        raise NotImplementedError("Jump method must be implemented in subclass")

    def shoot(self):
        raise NotImplementedError("Shoot method must be implemented in subclass")

    def powerUp(self):
        raise NotImplementedError("PowerUp method must be implemented in subclass")

    def powerDown(self):
        raise NotImplementedError("PowerDown method must be implemented in subclass")


class NormalState(State):
    def jump(self):
        print("Mario делает обычный прыжок")

    def shoot(self):
        print("Mario не может стрелять в обычном состоянии")

    def powerUp(self):
        print("Mario перешел в улучшенное состояние!")
        return SuperState(self.mario)

    def powerDown(self):
        print("Mario уже находится в обычном состоянии")
        return self


class SuperState(State):
    def jump(self):
        print("Mario делает высокий прыжок")

    def shoot(self):
        print("Mario не может стрелять в улучшенном состоянии")

    def powerUp(self):
        print("Mario перешел в огненное состояние")
        return FireState(self.mario)

    def powerDown(self):
        print("Mario перешел в обычное состояние")
        return NormalState(self.mario)


class FireState(State):
    def jump(self):
        print("Mario делает высокий прыжок")

    def shoot(self):
        print("Mario стреляет огненным шаром")

    def powerUp(self):
        print("Mario уже находится в огненном состоянии")
        return self

    def powerDown(self):
        print("Mario перешел в улучшенное состояние")
        return SuperState(self.mario)


class ConcreteMario(Mario):
    def __init__(self):
        self.state = NormalState(self)

    def jump(self):
        self.state.jump()

    def shoot(self):
        self.state.shoot()

    def powerUp(self):
        self.state = self.state.powerUp()

    def powerDown(self):
        self.state = self.state.powerDown()


mario = ConcreteMario()
mario.jump()
mario.shoot()
mario.powerUp()
mario.jump()
mario.powerUp()
mario.shoot()
mario.powerDown()
mario.powerDown()
