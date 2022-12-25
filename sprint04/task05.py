class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if not self.words:
            self.words.append(word)
        elif word not in self.words:
            if word[0] == self.words[-1][-1]:
                self.words.append(word)
            else:
                self.game_over = True
                return 'game over'
        else:
            self.game_over = True
            return 'game over'
        return self.words
    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'


my_gallows = Gallows()
my_gallows.play('apple')# ➞ ['apple']
my_gallows.play('ear')# ➞ ['apple', 'ear']
my_gallows.play('rhino')# ➞ ['apple', 'ear', 'rhino']
my_gallows.words# ➞ ['apple', 'ear', 'rhino']
my_gallows = Gallows()
print(my_gallows.game_over)
print(my_gallows.play('apple'))
print(my_gallows.words)
print(my_gallows.play('ear'))
print(my_gallows.play('rhino'))
print(my_gallows.play('ocelot'))
print(my_gallows.game_over)
print(my_gallows.play('oops'))
print(my_gallows.game_over)
print(my_gallows.words)