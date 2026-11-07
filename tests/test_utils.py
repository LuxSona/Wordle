from src.server.utils import getFrequencies
import pytest 

def test_frequencies():
    assert getFrequencies("chess") == {'c':1,'h':1,'s':2,'e':1}
    assert getFrequencies("WoWOw") == {'w':3,'o':2}
    assert getFrequencies("hEEllOO") == {'h':1,'e':2,'l':2,'o':2}
    assert getFrequencies("hi1") == {}
