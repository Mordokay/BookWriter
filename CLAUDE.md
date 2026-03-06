# AI Book Studio

This project is a structured multi-agent storytelling system for creating a novella or book.

## Core mission

Create a compelling, coherent, emotionally satisfying manuscript through a staged workflow:

1. interpret the user's creative brief
2. define theme and tone
3. build the world
4. develop characters
5. design plot and structure
6. create chapter outline
7. draft chapter briefs
8. write chapters
9. run continuity and literary review
10. revise and compile manuscript

## Non-goals

- Do not immediately start writing chapters before planning is approved.
- Do not overwrite major story files casually.
- Do not introduce major lore, character, or plot changes in later stages without recording them in the correct story files.
- Do not produce generic filler content when specifics are missing; instead propose options.

## General workflow rules

- Treat `story/brief.md` as the source of the user's desired reading experience.
- Treat `story/user-feedback.md` as the latest human guidance.
- Treat `story/constraints.md` as hard constraints.
- Treat `story/style-guide.md` as the prose and voice contract.
- Treat `story/world.md`, `story/characters.md`, `story/plot.md`, and `story/timeline.md` as canon.
- Treat `story/chapter-outline.md` as the approved structural plan.
- Before writing any new chapter, review canon files and earlier chapters.
- When making a significant story decision, update the relevant canon file.

## Order of operations

Preferred sequence:

1. orchestrator
2. genre-theme-designer
3. worldbuilder
4. character-architect
5. plot-architect
6. chapter-planner
7. user review checkpoint
8. chapter-writer
9. continuity-editor
10. literary-critic
11. revision-writer
12. compile manuscript

## Human-in-the-loop rule

Pause at these checkpoints unless the user explicitly says to continue automatically:

- after theme/style creation
- after world + characters + plot
- after chapter outline
- after every 2 chapters
- after full draft
- after major critique pass

## Story quality rules

The manuscript should aim for:

- emotional coherence
- meaningful character arcs
- internal world consistency
- increasing tension
- earned resolution
- distinct scene purpose
- minimal repetition
- controlled exposition
- strong chapter endings
- prose that is readable and intentional rather than purple or bloated

## Continuity rules

Everything written must remain consistent with:

- established world rules
- established technology or magic rules
- character motivations and relationships
- timeline order
- known injuries, objects, secrets, and locations

If a contradiction is necessary, flag it and propose a repair.

## File usage

- `story/brief.md`: user's initial creative request
- `story/goals.md`: target scope and creative objectives
- `story/theme.md`: themes, mood, genre, promise to the reader
- `story/world.md`: setting, rules, institutions, technology, geography
- `story/characters.md`: character sheets, arcs, relationships
- `story/plot.md`: act structure, core conflict, reveals, climax, ending
- `story/timeline.md`: chronology of important events
- `story/chapter-outline.md`: chapter-by-chapter map
- `story/chapter-briefs/`: one brief per chapter
- `story/chapters/`: prose drafts
- `story/reviews/`: continuity, critique, revision notes
- `story/user-feedback.md`: user steering and preferences
- `story/manuscript-status.md`: progress tracker
- `output/`: final compiled manuscript

## Writing guidelines

- Prefer specificity over vague drama.
- Dialogue should reveal character, tension, or information.
- Scenes must contain change.
- Exposition should be woven into action, perception, and conflict.
- Avoid repetitive chapter openings.
- Avoid generic cinematic filler.
- Avoid summarizing emotional beats that could be dramatized.
- Give each important character a distinct internal logic.

## Revision guidelines

When reviewing a chapter:

1. identify contradictions
2. identify pacing issues
3. identify weak dialogue or flat exposition
4. identify emotional misses
5. suggest concrete fixes
6. preserve the intended tone

## Default target for the proof of concept

- format: novella
- 6 to 10 chapters
- 20 to 35 pages equivalent
- 1 main protagonist
- 1 central conflict
- 1 contained but rich world

## Operating style

Be structured. Be decisive. Offer options when needed. Prefer maintainable markdown outputs. Do not improvise chaos. Build the book step by step.
