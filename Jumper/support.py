import random


class word:


    def __init__(self):
        with open("Jumper\words.txt") as f:
            lines = f.readlines()

            temp_list = []
            for line in lines:
        
                temp_list.append((line.strip("\n")).upper())
        self.words_list = temp_list
        self.word = list(random.choice(self.words_list))


    def formulate_printable_word(self, guessed_letters):
        """ 
        
        Call this into a variable. "variable = formulate_printable_word(guessed_letters)
        guessed_letters variable should be a list of capital letters that the player has guessed.

        Output example: list, ["E", "X", "_", "M", "P", "_", "E"]
        Args:
            self (word): an instance of word
            guessed_letters (list): A list of the guessed letters so far.
        """

        final_print = []
        for i in self.word:
            if guessed_letters.count(i) > 0:
                final_print.append(i)
            elif guessed_letters.count(i) <= 0:
                final_print.append("_")
            else:
                print("An error occured in checking the guessed letters against the letters in the word. - Support.py->class word->def formulate_printable_word")

        return final_print


class TerminalService():
    """A service that handles terminal operations
    
    The responsibility of the TerminalService is to provide input and output operations for the terminal"""
    
    def read_text(self, prompt):
        return input(prompt)

    def write_text(self, text):
        print(text)
        
    def clear_and_print_screen(self):
        pass



