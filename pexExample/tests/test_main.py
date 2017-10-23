from ..main import fct_1 as one
import pytest


@pytest.fixture(params=[1, 9999])
def example_fixture(request):
    return request.param


def test_main():
    assert one() == 10


def test_nothing(example_fixture):
    pass
