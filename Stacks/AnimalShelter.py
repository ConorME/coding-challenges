class AnimalShelter:
    def __init__(self, cats, dogs):
        self.cats = deque(cats)
        self.dogs = deque(dogs)

    def adopt(self, animal_type):
        if animal_type == "dog":
            self.dogs.popleft()
        
        if animal_type == "cat":
            self.cats.popleft()

    def add(self, animal, animal_type):
        if animal_type = "dog":
            self._add_dog(animal)

        if animal_type = "cat":
            self._add_cat(animal)

    def _add_dog(self, animal):
        self.dogs.append(animal)

    def _add_cat(self, animal):
        self.cats.append(animal)
