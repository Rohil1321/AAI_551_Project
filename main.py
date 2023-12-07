import traceback
from GameEngine import GameEngine

def handle_game():
    #Function to instantiate and initialize the GameEngine object.
    eng = GameEngine()
    eng.initializeGame()
    eng.intro()

    return eng

def play_game(engine):
    #Function to play the game loop
    remaining_vegetables = engine.remainingVeggies()

    while remaining_vegetables > 0:
        try:
            print(f"Remaining Vegetables: {remaining_vegetables}")
            print(f"Your Score: {engine.getScore()}")
            engine.printField()
            engine.moveRabbits()
            engine.moveCaptain()
            remaining_vegetables = engine.remainingVeggies()
        except Exception as e:
            print(f"An error occurred during the game: {e}")
            traceback.print_exc()
            break

    engine.gameOver()
    engine.highScore()

def main():
    #Main Function
    try:
        game_engine = handle_game()
        play_game(game_engine)
    except Exception as e:
        print(f"The game encountered an error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()