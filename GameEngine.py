import os
import random
import pickle

from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
from Snake import Snake

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
        self._snake = None

    def initVeggies(self):
        """
            This function initializes the game field with vegetables based on the input from a file.
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
        """
            This function initializes rabbits on the game field at random locations.
        """
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

    def initializeGame(self):
        """
            This function initializes the game by populating the game field with vegetables, placing the captain, and initializing rabbits.
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        self.initSnake()

    def remainingVeggies(self):
        """
            This function calculates the remaining number of vegetables on the game field.
        """
        count = 0
        for row in self._field:
            for item in row:
                if isinstance(item, Veggie):
                    count += 1
        return count

    def intro(self):
        """
            Displays the introduction and game instructions for the Captain Veggie Game.
        """
        print("Welcome to the Veggie Harvest Game!")
        print("The goal of the game is to harvest as many vegetables as you can while avoiding rabbits.")
        print("Here are the possible vegetables and their symbols:")
        for veggie in self._all_veggies:
            print(f"Symbol: {veggie.get_symbol()}, Name: {veggie.get_name()}, Points: {veggie.get_points()}")
        print(f"Captain Veggie symbol: {self._captain.get_symbol()}")
        print("Rabbit symbol: R")
        print(f"Snake symbol: S")
        print("Let the harvest begin!")

    def printField(self):
        """
            This function prints the game field
        """
        field_width = len(self._field[0])

        # Print the top border
        print("+-" + "--" * field_width + "+")

        for row in self._field:
            # Print the left border
            print("| ", end="")
            for item in row:
                if item is None:
                    print(' ', end=' ')
                else:
                    print(item.get_symbol(), end=' ')
            # Print the right border
            print("|")

        # Print the bottom border
        print("+-" + "--" * field_width + "+")

    def getScore(self):
        """
            This function returns the score when called
        """
        return self._score

    def moveRabbits(self):
        """
            This function is used to move each Rabbit object in the game to a random position.
        """
        for rabbit in self._rabbits:
            current_x = rabbit.get_x()
            current_y = rabbit.get_y()

            new_x = current_x + random.choice([-1, 0, 1])
            new_y = current_y + random.choice([-1, 0, 1])

            # Check if the new location is within the field boundaries
            if 0 <= new_x < len(self._field) and 0 <= new_y < len(self._field[0]):
                if self._field[new_x][new_y] is None:
                    self._field[current_x][current_y] = None
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)
                    self._field[new_x][new_y] = rabbit

    def moveCptVertical(self, vertical_movement):
        """
            This function is used to move the Captain vertically by the specified amount.
        """
        captain = self._captain
        current_x, current_y = captain.get_x(), captain.get_y()
        new_x, new_y = current_x + vertical_movement, current_y

        if 0 <= new_x < len(self._field) and 0 <= new_y < len(self._field[0]):
            if self._field[new_x][new_y] is None:
                captain.set_x(new_x)
                captain.set_y(new_y)
                self._field[current_x][current_y] = None
                self._field[new_x][new_y] = captain
            elif isinstance(self._field[new_x][new_y], Veggie):
                self.col_Veggie((current_x, current_y), (new_x, new_y))
            else:
                print("Oops! Movement would cause a collision.")
        else:
            print("Oops! Movement would go beyond field boundaries.")

    def moveCptHorizontal(self, horizontal_movement):
        """
            This function is used to move the Captain horizontally by the specified amount.
        """
        captain = self._captain
        current_x, current_y = captain.get_x(), captain.get_y()
        new_x, new_y = current_x, current_y + horizontal_movement

        if 0 <= new_x < len(self._field) and 0 <= new_y < len(self._field[0]):
            if self._field[new_x][new_y] is None:
                captain.set_x(new_x)
                captain.set_y(new_y)
                self._field[current_x][current_y] = None
                self._field[new_x][new_y] = captain
            elif isinstance(self._field[new_x][new_y], Veggie):
                self.col_Veggie((current_x, current_y), (new_x, new_y))
            else:
                print("Oops! Movement would cause a collision.")
        else:
            print("Oops! Movement would go beyond field boundaries.")

    def col_Veggie(self, current_location, new_location):
        """
            This function is used to handle the interaction when the Captain collects a Veggie.
        """
        # Update Captain's member variables
        self._captain.set_x(new_location[0])
        self._captain.set_y(new_location[1])

        # Collect Veggie details
        veggie = self._field[new_location[0]][new_location[1]]
        v_name = veggie.get_name()
        v_points_value = veggie.get_points()

        # Output message
        print(f"Delicious vegetable found: {v_name}! You earned {v_points_value} points.")

        # Add Veggie to Captain's List of Veggies
        self._captain.addVeggie(veggie)

        # Increment the score
        self._score += v_points_value

        # Update field
        self._field[current_location[0]][current_location[1]] = None
        self._field[new_location[0]][new_location[1]] = self._captain

    def moveCaptain(self):
        """
            This function is used to handle when the Captain collects a Veggie.
        """
        direction = input("Enter the direction to move the Captain (W/A/S/D): ").lower()

        if direction == 'w':
            self.moveCptVertical(-1)  # Move up
        elif direction == 's':
            self.moveCptVertical(1)  # Move down
        elif direction == 'a':
            self.moveCptHorizontal(-1)  # Move left
        elif direction == 'd':
            self.moveCptHorizontal(1)  # Move right
        else:
            print("Invalid input. Please enter W, A, S, or D.")

    def initSnake(self):
        """
        Instantiate a new Snake object in a random, unoccupied slot in the field.
        This function should be called after initializing the rabbits.
        """
        if not self._field:
            print("Error: Field not initialized.")
            return

        field_size_height = len(self._field)
        field_size_width = len(self._field[0])

        # Find a random, unoccupied position for the snake
        while True:
            location_h = random.randrange(0, field_size_height)
            location_w = random.randrange(0, field_size_width)

            if self._field[location_h][location_w] is None:
                break

        # Instantiate the Snake object and store it in the member variable
        self._snake = Snake(location_h, location_w)
        self._field[location_h][location_w] = self._snake

    def moveSnake(self):
        """
        Attempt to move the snake on the field.
        The snake moves closer to the captain's position.
        If the snake attempts to move into the same position as the captain,
        the captain loses the last five vegetables, and the snake is reset to a new position.
        """
        if self._snake is None:
            print("Error: Snake not initialized.")
            return

        captain_position = (self._captain.get_x(), self._captain.get_y())
        snake_position = (self._snake.get_x(), self._snake.get_y())

        # Calculate the direction for the snake to move towards the captain
        direction_x = 0 if captain_position[0] == snake_position[0] else (
            1 if captain_position[0] > snake_position[0] else -1)
        direction_y = 0 if captain_position[1] == snake_position[1] else (
            1 if captain_position[1] > snake_position[1] else -1)

        new_x = snake_position[0] + direction_x
        new_y = snake_position[1] + direction_y

        # Check if the new location is within the field boundaries
        if 0 <= new_x < len(self._field) and 0 <= new_y < len(self._field[0]):
            if self._field[new_x][new_y] is None:
                # Move the snake to the new position
                self._field[snake_position[0]][snake_position[1]] = None
                self._snake.set_x(new_x)
                self._snake.set_y(new_y)
                self._field[new_x][new_y] = self._snake

                # Check if the snake is in the same position as the captain
                if (new_x, new_y) == captain_position:
                    # If the snake is in the captain's position, the captain loses the last five vegetables
                    self._captain.loseLastFiveVeggies()

                    # Reset the snake to a new random, unoccupied position
                    self.initSnake()
            else:
                print("Oops! Snake movement would cause a collision.")
        else:
            print("Oops! Snake movement would go beyond field boundaries.")

    def gameOver(self):
        """
            This function is used to display information when the game is over.
        """
        print("Game Over!")

        # Output harvested vegetables
        veggies_collected = self._captain.get_veggies_collected()
        if not veggies_collected:
            print("You didn't harvest any vegetables.")
        else:
            print("You harvested the following vegetables:")
            for veggie in veggies_collected:
                print(f"- {veggie.get_name()}")

        # Output player's score
        print(f"Your final score is: {self._score}")

    def highScore(self):
        """
            This function is used to handle high scores functionality.
        """
        high_scores = []

        # Check if the highscore.data file exists
        if os.path.exists(self.HIGHSCOREFILE):
            try:
                # Open the file for binary reading
                with open(self.HIGHSCOREFILE, 'rb') as file:
                    # Unpickle the file into the List of high scores
                    high_scores = pickle.load(file)
            except Exception as e:
                print(f"Error reading high scores: {e}")

        # Prompt the user for their initials and extract the first 3 characters
        player_initials = input("Enter your initials: ")[:3]

        # Create a Tuple with the player’s initials and score
        player_score = (player_initials, self._score)

        if not high_scores:
            # If there are no high scores yet recorded, add the Tuple to the List
            high_scores.append(player_score)
        else:
            # Add the Tuple to the correct position in the List to maintain descending order
            index_to_insert = 0
            for index, (initials, score) in enumerate(high_scores):
                if self._score > score:
                    index_to_insert = index
                    break
                else:
                    index_to_insert = index + 1

            high_scores.insert(index_to_insert, player_score)

        # Output all of the high scores
        print("High Scores:")
        for rank, (initials, score) in enumerate(high_scores, start=1):
            print(f"{rank}. {initials}: {score}")

        try:
            # Open the highscore.data file for binary writing
            with open(self.HIGHSCOREFILE, 'wb') as file:
                # Pickle the List of high scores to the file
                pickle.dump(high_scores, file)
        except Exception as e:
            print(f"Error writing high scores: {e}")
