from python_humble_utils.classes import get_all_subclasses
from tests.conftest import Foo, BooFoo, MooBooFoo


def test_no_subclasses_given__get_all_subclasses_succeeds():
    assert set(get_all_subclasses(MooBooFoo, False)) == set()
    assert set(get_all_subclasses(MooBooFoo, True)) == {MooBooFoo}


def test_self_included__get_all_subclasses_succeeds():
    assert set(get_all_subclasses(Foo, True)) == {Foo, BooFoo, MooBooFoo}


def test_self_excluded__get_all_subclasses_succeeds():
    assert set(get_all_subclasses(Foo, False)) == {BooFoo, MooBooFoo}
