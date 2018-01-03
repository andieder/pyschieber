import pytest

from pyschieber.card import Card
from pyschieber.player import Player
from pyschieber.stich import PlayedCard
from pyschieber.suit import Suit


@pytest.fixture(scope="session", autouse=True)
def players():
    return [Player(), Player(), Player(), Player()]


@pytest.fixture(scope="session", autouse=True)
def played_cards(players):
    return [PlayedCard(player=players[0], card=Card(Suit.BELL, 10)),
            PlayedCard(player=players[1], card=Card(Suit.ACORN, 14)),
            PlayedCard(player=players[2], card=Card(Suit.BELL, 13)),
            PlayedCard(player=players[3], card=Card(Suit.BELL, 9))]
