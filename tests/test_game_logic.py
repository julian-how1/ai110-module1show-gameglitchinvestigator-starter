"""Tests for the bugs found in the Game Glitch Investigator."""

import random
from pathlib import Path

from streamlit.testing.v1 import AppTest

from logic_utils import check_guess

APP_PATH = str(Path(__file__).resolve().parents[1] / "app.py")


def test_correct_guess_wins():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_too_high_says_go_lower():
    """A guess ABOVE the secret must send the player DOWN.

    The bug had this backwards -- it said "Go HIGHER!", pushing the
    player further from the answer on every turn.
    """
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_too_low_says_go_higher():
    """A guess BELOW the secret must send the player UP."""
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()


def test_string_secret_compares_as_a_number():
    """app.py turns the secret into a string on even-numbered attempts.

    Compared alphabetically, "9" > "100" is True -- which flipped the hint
    a second way. check_guess converts to int first, so 9 is correctly
    below 100.
    """
    outcome, message = check_guess(9, "100")

    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
