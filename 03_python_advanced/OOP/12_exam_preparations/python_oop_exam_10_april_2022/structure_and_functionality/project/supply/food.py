from project.supply.supply import Supply


class Food(Supply):
    INITIAL_ENERGY = 25

    def __init__(self, name: str, energy=INITIAL_ENERGY):
        super().__init__(name, energy)