from Jumper.support import word
from Jumper.support import TerminalService

class JumperGraphic():
    
   
    def display_jumper_graphic(self, parachute_damage = 0):
        """Contains the jumper graphics of losing the parachute, 0 being undamaged and 4 being a fail state. """
        if parachute_damage == 0:
            # Unharmed parachute [0]
            parachute_graphic = "  ___  \n /___\ \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^"
        elif parachute_damage == 1:
            # [1]
            parachute_graphic = "       \n /___\ \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^"
        elif parachute_damage == 2:
            # [2]
            parachute_graphic = "       \n       \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^"
        elif parachute_damage == 3:
            # [3]
            parachute_graphic = "       \n       \n       \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^"
        elif parachute_damage == 4:
            # Fail state [4]
            parachute_graphic = "       \n       \n       \n       \n   x   \n  /|\  \n  / \  \n\n^^^^^^^"
        return parachute_graphic


class Director():
    """-"""
    
    def __init__(self):
        """Constructs a new Director
        
        Args:
            self (Director): an instance of Director"""
            
        self._jumper = JumperGraphic()
        self._is_playing = True
        self._word = word()
        self._terminal_service = TerminalService()
        
        
    def start_game(self):
        """Starts the game by running the main loop.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self._is_playing:
            playerGuess = self._get_inputs()
            self._do_updates(playerGuess)
            self._do_outputs()
            
    def _get_inputs(self):
        """Asks the player to guess a letter from a-z. 
        
        Args:
            self (Director): An instance of Director.
        """
        playerGuess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        return playerGuess
        
    def _do_updates(self, playerGuess):
        """Puts the guessed letters in a list.
        Calls the formulate_printable_word to check the guessed letters against the letters in the word.
        
        Args: 
            self (Director): An instance of Director.
        """
        guessedLetters = list(playerGuess.upper())
        self._word.formulate_printable_word(guessedLetters)
        
    
    def _do_outputs(self):
        """Displays jumper graphic, and """
        self._jumper.display_jumper_graphic(0)
    
    
# class Jumper():
#     """-"""
    
#     def __init__(self):
#         """-"""
