"""
Tests for the measure module.
"""
import numpy as np
import pytest
import molecool

def test_calculate_angle():

    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])

    expected_value = 90
    calculated_value = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert expected_value == calculated_value


def test_calculate_distance():
    """Test that the calculate distance function calculates what we expect"""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    observed_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == observed_distance


@pytest.mark.parametrize(
    "p1, p2, p3, expected_value",
    [
        (
            np.array([np.sqrt(2) / 2, np.sqrt(2) / 2, 0]),
            np.array([0, 0, 0]),
            np.array([1, 0, 0]),
            45,
        ),
        (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
        (
            np.array([np.sqrt(3) / 2, (1 / 2), 0]),
            np.array([0, 0, 0]),
            np.array([1, 0, 0]),
            30,
        ),
    ],
)
def test_calculate_angle_many(p1, p2, p3, expected_value):

    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)
    assert expected_value == pytest.approx(
        calculated_angle
    ), f"{calculated_angle} {expected_value}"