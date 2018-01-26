
import mpy as mv


def test_names():
    assert mv.dictionary.__name__ == mv.dictionary.__qualname__ == 'dictionary'
    assert mv.dictionary.__module__ == 'mpy'
