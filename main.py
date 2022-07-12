from suit import Suit
from player import Player
from card import Card
from deck import Deck
from war_card_game import WarCardGame

player = Player("labib", Deck(is_empty=True))
computer = Player("computer", Deck(is_empty=True), is_computer=True)
deck = Deck()

game = WarCardGame(player, computer, deck)
game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input(
        "are you ready for the next round ? press Enter to continue , press X to stop")
    if answer.lower() == 'x':
        break
