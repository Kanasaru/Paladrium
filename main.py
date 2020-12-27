#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

import os
import paladrium

def main():
    game = paladrium.game.Game(os.path.dirname(__file__))

if __name__ == "__main__":
    main()
