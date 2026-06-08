import geom2_analysis as ga
import pytest

def test_bond_check_negative():
    distance = -1
    with pytest.raises(ValueError):
        calculated = ga.bond_check(distance)

def test_open_xyz_wrong_extension():
    fname = "hello.txt"
    with pytest.raises (ValueError):
        ga.open_xyz(fname)