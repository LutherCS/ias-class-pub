#!/usr/bin/env python3
"""
Password cracking testing

@authors: Roman Yasinovskyy
@version: 2025.4
"""

import importlib
import pathlib
import sys
import tomllib
from typing import Generator

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")


DATA_DIR = pathlib.Path("src/projects/passwords/")
TIME_LIMIT = 1


@pytest.fixture
def solution():
    """Read all solutions"""
    all_users = dict()
    with open(DATA_DIR / pathlib.Path("solution.txt")) as solution_file:
        for line in solution_file:
            username, password = line.strip().split(":")
            all_users[username] = password
    return all_users


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), "rb") as file:
        all_cases = tomllib.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "username, password",
    get_cases("test_case", "username", "password"),
)
def test_solution(username: str, password: str, solution):
    """Testing the solution"""
    if password:
        assert solution[username] == password
    else:
        assert False


if __name__ == "__main__":
    pytest.main(["-v", __file__])
