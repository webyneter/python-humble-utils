import pytest

from python_humble_utils.strings import (
    camel_or_pascal_case_to_snake_case,
    camel_or_pascal_case_to_space_delimited,
)


@pytest.mark.parametrize(
    "s,expected",
    [
        (
            "IAmInCamelCase_but_i_am_not_AndHereAmIOnceAgain",
            "i_am_in_camel_case_but_i_am_not__and_here_am_i_once_again",
        ),
        (
            "iAmInPascalCase_but_i_am_not_andHereAmIOnceAgain",
            "i_am_in_pascal_case_but_i_am_not_and_here_am_i_once_again",
        ),
    ],
)
def test_convert_camel_or_pascal_case_to_snake_case(s: str, expected: str):
    assert camel_or_pascal_case_to_snake_case(s) == expected


@pytest.mark.parametrize(
    "s,expected",
    [
        ("iAmASTRANGECamelCase", "i Am ASTRANGE Camel Case"),
        (
            "YetAnotherOneBUTNOWWhilebeingastrangeOneIamStillAProperPascalCase",
            "Yet Another One BUTNOW Whilebeingastrange One Iam Still A Proper Pascal Case",
        ),
    ],
)
def test_convert_camel_or_pascal_case_to_space_delimited(s: str, expected: str):
    assert camel_or_pascal_case_to_space_delimited(s) == expected
