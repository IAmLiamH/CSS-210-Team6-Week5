from  import word

# Unharmed parachute [0]
print("  ___  \n /___\ \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^")
# [1]
print("       \n /___\ \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^")
# [2]
print("       \n       \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^")
# [3]
print("       \n       \n       \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^")
# Fail state [4]
print("       \n       \n       \n       \n   x   \n  /|\  \n  / \  \n\n^^^^^^^")


class Director():
    """-"""
    
    def __init__(self):
        """Constructs a new Director
        
        Args:
            self (Director): an instance of Director"""
            
        self._jumper = Jumper()
        self._isplaying = True
        self._word = word()
        
        
    def start_game(self):
        """-"""
        
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            
    def _get_inputs(self):
        """-"""
        
    def _do_updates(self):
        """-"""
    
    def _do_outputs(self):
        """-"""
    
    
class Jumper():
    """-"""
    
    def __init__(self):
        """-"""
