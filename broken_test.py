# broken test that imports non-existent module

import nonexistmodule

def test_it():
    assert nonexistmodule.do_thing() == 42
