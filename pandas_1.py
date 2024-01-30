#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:14:07 2024

@author: user
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)
print(file.info())
print(file.describe())
file = pandas.read_csv("iris.csv")
print(file)
print(file.info())

print(file.describe())

file = pandas.read_csv("insurance_data.csv",skiprows=5)

print(file)