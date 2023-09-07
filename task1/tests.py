import pytest


from solution import strict


@strict
def has_access(is_admin: bool, is_moderator: bool) -> bool:
	return is_admin or is_moderator 

@strict
def sum_two(a: int, b: int) -> int:
	return a + b

@strict
def concat(str_1: str, str_2: str):
	return "{0}{1}".format(str_1, str_2)


def test_has_access_True_False_target_True():	
	assert has_access(True, False) == True

def test_has_access_True_target_TypeError():	
	assert has_access(True) == TypeError

def test_sum_two_1_2_target_3():
	assert sum_two(1, 2) == 3

def test_sum_two_1_2p4_target_TypeError():
	assert sum_two(1, 2.4) == TypeError

def test_sum_two_1_target_TypeError():
	assert sum_two(1) == TypeError

def test_concat_abc_ba_target_abcba():
	assert concat("abc", "ba") == "abcba"

def test_concat_abc_2_target_TypeError():
	assert concat("abc", "ba") == TypeError
