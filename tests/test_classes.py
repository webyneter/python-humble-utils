from python_humble_utils.classes import get_all_subclasses
from tests.conftest import Foo, Boo, Moo


def test_no_subclasses_given__get_all_subclasses_succeeds():
    assert set(get_all_subclasses(Moo, False)) == set()
    assert set(get_all_subclasses(Moo, True)) == {Moo}


def test_self_included__get_all_subclasses_succeeds():
    assert set(get_all_subclasses(Foo, True)) == {Foo, Boo, Moo}


def test_self_excluded__get_all_subclasses_succeeds():
    assert set(get_all_subclasses(Foo, False)) == {Boo, Moo}
