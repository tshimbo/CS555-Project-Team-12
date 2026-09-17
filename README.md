# Meals4Kidz — CS555 Agile Methods (Team 12)

A command-line meal-planning app for kids, built by a student team at Stevens Institute of Technology over four Scrum sprints.

## What it does
- Browse recipes and view ingredient measurements
- Record ingredient likes and dislikes
- Track a child's weight history by age (saved to `weightsFile.json`)
- Validates input (e.g., recipe and ingredient names can't be numbers; every recipe needs at least one ingredient)

## Process
Work was planned as user stories and split into sprint tasks, with unit tests (`unittest`) written alongside each story.

## Run it
```bash
cd meals4kidz
python3 meals4kidz.py
```

## Tests
```bash
cd meals4kidz
python3 -m unittest meals4kidz.py
```
