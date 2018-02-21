import logging
import sys

from pyschieber.player.random_player import RandomPlayer
from pyschieber.tournament import Tournament
from example.example_player import ExamplePlayer


def start_tournament(points):
    tournament = Tournament(point_limit=points)
    example_player = ExamplePlayer(name='ExamplePlayer')
    tournament.register_player(example_player, 1)
    [tournament.register_player(RandomPlayer(name=str(i)), i) for i in range(2, 5)]
    example_player.set_tournament(tournament)
    tournament.play()


def set_logging():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    stream_handler.setFormatter(formatter)
    root.addHandler(stream_handler)


if __name__ == "__main__":
    set_logging()
    start_tournament(points=1500)
