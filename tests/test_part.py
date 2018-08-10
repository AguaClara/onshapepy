from onshapepy.part import Config
import pint
import pytest

u = pint.UnitRegistry()

def test_get_part_params(cube):
    print(cube.params)
    assert cube.params['has_fillet']
    assert 100*u.mm == cube.params['L']
    assert 100*u.mm == cube.params['h']
    assert 'circular' == cube.params['fillet_type']
    assert 100*u.mm == cube.params['w']


def test_set_part_params(cube):
    altered = {'h': 200 * u.mm, 'L': 400*u.mm, 'w': 100*u.mm, 'has_fillet': False, 'fillet_type': "circular"}
    standard = {'h': 100 * u.mm, 'L': 100*u.mm, 'w': 100*u.mm, 'has_fillet': True, 'fillet_type': "circular"}
    cube.params = altered
    assert cube.params == altered
    # reset to original
    cube.params = standard
    assert cube.params == standard
