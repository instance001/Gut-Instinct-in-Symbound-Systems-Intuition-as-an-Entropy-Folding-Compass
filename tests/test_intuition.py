from src import intuition


def test_patina_recap():
    recap = intuition.patina_recap(["line1", "line2"])
    assert "line1" in recap and "line2" in recap
