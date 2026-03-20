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
- Treat `story/guide.md` as the author's detailed creative direction — character profiles, dialogue pairings, ending direction, style rules, avoidance list, and motifs. Consult it alongside the brief for all planning and writing stages.
- Treat `story/user-feedback.md` as the latest human guidance.
- Treat `story/constraints.md` as hard constraints.
- Treat `story/style-guide.md` as the prose and voice contract.
- Treat `story/world.md`, `story/characters.md`, `story/plot.md`, and `story/timeline.md` as canon.
- Treat `story/running-state.md` as the cumulative state tracker -- ground truth for everything that has happened in the story so far.
- Treat `story/chapter-outline.md` as the approved structural plan.
- Before writing any new chapter, review canon files, running state, and the most recent chapters.
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
12. reader-agent (full-manuscript reading-experience review)
13. humanizer (final pass: readability, AI-tell removal, natural prose) -- see `story/humanizer-checklist.md`
14. compile manuscript

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
- `story/guide.md`: author's detailed creative direction — character profiles, frog profiles, dialogue pairings, ending direction, writing style rules, things to avoid, symbolic motifs. **Must be consulted alongside the brief when building chapter outline, plot, characters, world, and writing chapters.**
- `story/goals.md`: target scope and creative objectives
- `story/theme.md`: themes, mood, genre, promise to the reader
- `story/world.md`: setting, rules, institutions, technology, geography
- `story/characters.md`: character sheets, arcs, relationships
- `story/plot.md`: act structure, core conflict, reveals, climax, ending
- `story/timeline.md`: chronology of important events
- `story/chapter-outline.md`: chapter-by-chapter map
- `story/running-state.md`: cumulative state tracker (physical, psychological, environmental, motifs, foreshadowing, threads, summaries)
- `story/chapter-briefs/`: one brief per chapter
- `story/chapters/`: prose drafts
- `story/reviews/`: continuity, critique, revision notes
- `story/user-feedback.md`: user steering and preferences
- `story/manuscript-status.md`: progress tracker
- `story/humanizer-checklist.md`: final-pass agent instructions for natural, human-readable prose
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

## Current project target

- format: novel (~80,000-85,000 words)
- 26 chapters (22 plot + 4 character-development/world-exploration)
- 5-person human ensemble with 1 soft protagonist (Quill)
- 6 core frog characters
- 1 central conflict (cyclical, world-ending)
- 1 rich hidden civilization (frog society in the Amazon, pockets worldwide)

## Operating style

Be structured. Be decisive. Offer options when needed. Prefer maintainable markdown outputs. Do not improvise chaos. Build the book step by step.
