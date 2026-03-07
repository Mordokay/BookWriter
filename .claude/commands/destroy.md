This command resets the project for a new book. It is DESTRUCTIVE and requires explicit user confirmation before proceeding.

## Step 1: Confirm

Before doing ANYTHING, use AskUserQuestion to ask:

"This will permanently delete all story content, chapters, reviews, chapter briefs, images, and output files. The project structure, agents, commands, scripts, and process files (humanizer-checklist.md) will be preserved. Are you sure you want to destroy the current story and start fresh? (yes/no)"

If the user does not confirm with "yes", stop immediately.

## Step 2: Clear generated content directories

Remove all files inside these directories (keep the directories themselves):

    rm -f story/chapters/*.md
    rm -f story/chapter-briefs/*.md
    rm -f story/reviews/*.md
    rm -f output/*
    rm -rf ImageAssets/*

## Step 3: Reset story files to empty templates

Overwrite each of these files with just their heading (clearing all story-specific content):

- `story/brief.md` -> "# Book Brief\n"
- `story/goals.md` -> "# Project Goals\n"
- `story/theme.md` -> "# Theme\n"
- `story/style-guide.md` -> "# Style Guide\n"
- `story/world.md` -> "# World\n"
- `story/characters.md` -> "# Characters\n"
- `story/plot.md` -> "# Plot\n"
- `story/timeline.md` -> "# Timeline\n"
- `story/chapter-outline.md` -> "# Chapter Outline\n"
- `story/running-state.md` -> "# Running State\n"
- `story/constraints.md` -> "# Constraints\n"
- `story/user-feedback.md` -> "# User Feedback\n"

Reset `story/manuscript-status.md` to its initial template:

```markdown
# Manuscript Status

## Current phase

setup

## Progress

- [ ] brief completed
- [ ] theme created
- [ ] style guide created
- [ ] world created
- [ ] characters created
- [ ] plot created
- [ ] timeline created
- [ ] chapter outline created
- [ ] outline approved
- [ ] chapter briefs created
- [ ] continuity pass completed
- [ ] literary pass completed
- [ ] reader review completed
- [ ] revisions completed
- [ ] manuscript compiled

## Notes

- Project reset for new book.
```

## Step 4: Do NOT modify

- `CLAUDE.md`
- `README.md`
- `.claude/agents/*`
- `.claude/commands/*`
- `.claude/settings.local.json`
- `scripts/*`
- `.venv/`
- `story/humanizer-checklist.md` (this is a process file, not story content)

## Step 5: Report

After cleanup, report:
- What was cleared
- What was preserved
- Suggest the user run `/interview` or edit `story/brief.md` to begin a new book
