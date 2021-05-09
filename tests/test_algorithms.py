from typing import Dict, List

import pytest

from algobot.algorithms import get_sma, get_wma


@pytest.fixture(name='dummy_data')
def get_dummy_data():
    return [
               {
                   'open': 1,
                   'close': 5
               },
               {
                   'open': 2,
                   'close': 3
               },
               {
                   'open': 3,
                   'close': 2
               },
               {
                   'open': 4,
                   'close': 7
               },
           ]


@pytest.mark.parametrize(
    'prices, parameter, expected',
    [
        (4, 'open', 2.5),
        (4, 'close', 4.25)
    ]
)
def test_sma(dummy_data: List[Dict[str, float]], prices: int, parameter: str, expected: float):
    assert get_sma(data=dummy_data, prices=prices, parameter=parameter) == expected


@pytest.mark.parametrize(
    'prices, parameter, desc, expected',
    (
        (4, 'open', False, 3.0),
        (4, 'close', False, 4.5)
    )
)
def test_wma(dummy_data: List[Dict[str, float]], prices: int, parameter: str, desc: bool, expected: float):
    assert get_wma(data=dummy_data, prices=prices, parameter=parameter, desc=desc) == expected


def test_ema():
    pass


def test_accumulation_distribution_indicator():
    pass


def test_normal_volume_oscillator():
    pass


def test_intraday_intensity_indicator():
    pass


def test_normalized_intraday_intensity():
    pass
