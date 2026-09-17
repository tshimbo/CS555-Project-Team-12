# Meals4Kidz: CS555 Agile Methods (Team 12)

[![Tests](https://github.com/tshimbo/CS555-Project-Team-12/actions/workflows/tests.yml/badge.svg)](https://github.com/tshimbo/CS555-Project-Team-12/actions/workflows/tests.yml)

A command-line meal-planning app for kids, built by a student team at Stevens Institute of Technology over four Scrum sprints.

## What it does
- Browse recipes and view ingredient measurements
- Record ingredient likes and dislikes
- Track a child's weight and height history by age (saved as JSON next to the script)
- Validates input (e.g., recipe and ingredient names can't be numbers; every recipe needs at least one ingredient)

## Process
Work was planned as user stories and split into sprint tasks, with unit tests (`unittest`) written alongside each story.

## Run the test suite
Requires Python 3.8+ and no extra packages. Works from any directory:
```bash
python3 meals4kidz/meals4kidz.py
```
