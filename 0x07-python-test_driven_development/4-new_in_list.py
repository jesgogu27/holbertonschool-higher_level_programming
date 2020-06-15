#!/usr/bin/python3

def new_in_list(my_list, idx, element):
	if idx < 0:
		return my_list

	if idx > len(my_list):
		copy = my_list
		return copy

	coppy = my_list[:]
	coppy[idx] = element
	return coppy

