from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit


class GameEngine:

    def __init__(self):
        """
            This function initializes the game engine with default values for vegetable and rabbit counts, high score file,
            field, rabbits, captain, list of all possible veggies, and the initial score.
        """
        self.NUMBEROFVEGGIES = 30
        self.NUMBEROFRABBITS = 5
        self.HIGHSCOREFILE = 'highscore.data'
        self._field = []
        self._rabbits = []
        self._captain = None
        self._all_veggies = []
        self._score = 0

    def initVeggies(self):
        """
            This function initializes the game field with vegetables based on the input from a file.
            It prompts the user to enter the name of the vegetable point file.
            Once the file is provided and validated:
                - It initializes a 2D field array, setting each slot to None.
                - It creates Veggie objects based on the content of the file.
                - It populates the 2D field list with Veggie objects at random locations.
        """
        input_file = input("Please enter the name of the vegetable point file: ")

        while not os.path.exists(input_file):
            input_file = input(f"{input_file} does not exist!\nPlease enter the name of the vegetable point file: ")

        with open(input_file, 'r') as f:
            lines = f.readlines()

        #The height and width of the field
        field_size_height = int(
            lines[0].strip().split(',')[1])
        field_size_width = int(
            lines[0].strip().split(',')[2])

        for height in range(field_size_height):
            row = []
            for width in range(field_size_width):
                row.append(None)
            self._field.append(row)

        # The remaining lines in the files should be used to create new Veggie objects that are
        # added to the List of possible vegetables
        for line in lines[1:]:
            data = line.strip().split(',')
            v_name = data[0]
            vFieldInhabitant = data[1]
            v_points = int(data[2])
            obj = Veggie(v_name, vFieldInhabitant, v_points)
            self._all_veggies.append(obj)

        counter = self.NUMBEROFVEGGIES

        while counter > 0:
            location_h = random.randrange(0, field_size_height)
            location_w = random.randrange(0, field_size_width)

            # If a chosen random location is occupied by another Veggie object, repeatedly
            # choose a new location until an empty location is found
            while self._field[location_h][location_w] != None:
                location_h = random.randrange(0, field_size_height)
                location_w = random.randrange(0, field_size_width)

            self._field[location_h][location_w] = random.choice(self._all_veggies)
            counter -= 1

    def initCaptain(self):
        """
            This function initializes the Captain on the game field at a random location.
            If the chosen random location is occupied by other objects, it repeats the process until an empty location is found.
            Once a suitable location is found, it creates a Captain object and places it at the chosen location in the game field.
            """

        field_size_height = len(self._field)
        field_size_width = len(self._field[0])

        location_h = random.randrange(0, field_size_height)
        location_w = random.randrange(0, field_size_width)

        # If a chosen random location is occupied by other Veggie objects, repeatedly
        # choose a new location until an empty location is found
        while self._field[location_h][location_w] != None:
            location_h = random.randrange(0, field_size_height)
            location_w = random.randrange(0, field_size_width)

        self._captain = Captain(location_h, location_w)
        self._field[location_h][location_w] = self._captain

    def initRabbits(self):
        counter = self.NUMBEROFRABBITS
        field_size_height = len(self._field)
        field_size_width = len(self._field[0])

        while counter > 0:
            location_h = random.randrange(0, field_size_height)
            location_w = random.randrange(0, field_size_width)

            # If a chosen random location is occupied by another object, repeatedly
            # choose a new location until an empty location is found
            while self._field[location_h][location_w] != None:
                location_h = random.randrange(0, field_size_height)
                location_w = random.randrange(0, field_size_width)

            rabbit = Rabbit(location_h, location_w)
            self._field[location_h][location_w] = rabbit
            self._rabbits.append(rabbit)
            counter -= 1
