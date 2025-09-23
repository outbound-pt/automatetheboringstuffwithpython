# Automate the Boring Stuff with Python Practice Problems

This repository organizes exercises from *Automate the Boring Stuff with Python (2nd Edition)* by Al Sweigart. Solutions live alongside the official prompts so you can quickly review each challenge and the corresponding code.

## Repository Layout

```
chapters/
  chapter_##_<topic>/
    practice_questions/
      <exercise_slug>/
        README.md        # Exercise prompt (to be copied verbatim from the book)
        <exercise_slug>.py  # Solution code (if available)
```

- `chapters/` contains one directory per book chapter, ordered to match the table of contents.
- Each chapter stores a `practice_questions/` folder that groups every practice question and project.
- Within an exercise directory you will find the original prompt (in `README.md`) and any implementation files.

## Adding Prompts and Solutions

Due to outbound HTTP restrictions in this environment, the verbatim exercise text from automatetheboringstuff.com could not be populated automatically. When working locally, copy the exact wording for each practice question or project into the corresponding `README.md` file.

To add or update a solution:

1. Navigate to the appropriate exercise folder under `chapters/chapter_##_<topic>/practice_questions/`.
2. Paste the official prompt into `README.md` if it has not been added yet.
3. Implement your solution in a Python file named after the exercise slug (for example, `comma_code.py`).
4. Commit your changes so others can follow along with the prompts and solutions.

## Existing Solutions

At the moment, Chapter 4 includes Python implementations for:

- `comma_code`
- `coin_flip_streaks`
- `character_picture_grid`

The solutions reside in their respective exercise folders within `chapters/chapter_04_lists/`.

Happy automating!
