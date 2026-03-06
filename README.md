# BookWriter

A multi-agent system that writes a novella for you. You provide a short creative brief, then guide the process with small, specific notes. Nine specialized AI agents handle everything else — theme, world, characters, plot, prose, and quality review.

---

## Quick Start

Three steps to get going:

1. **Fill out your brief** — Edit `story/brief.md` with your story idea (see examples below)
2. **Run Prompt 1** — Paste the first prompt into Claude Code to kick off the pipeline
3. **Review and steer** — The system pauses at checkpoints for your feedback

That's it. You don't need to plan the story yourself. The agents do the planning. You just say what you want to read.

---

## How It Works

The system has 9 agents that run in sequence:

| Step | Agent | What it does |
|------|-------|-------------|
| 1 | **Orchestrator** | Inspects project state, decides what to do next |
| 2 | **Genre/Theme Designer** | Sets genre, mood, themes, and style guide |
| 3 | **Worldbuilder** | Creates the setting, rules, history, atmosphere |
| 4 | **Character Architect** | Designs characters, arcs, relationships, secrets |
| 5 | **Plot Architect** | Builds conflict, structure, turning points, climax |
| 6 | **Chapter Planner** | Breaks the plot into chapter beats and briefs |
| 7 | **Chapter Writer** | Drafts prose for each chapter |
| 8 | **Continuity Editor** | Checks for plot holes, timeline issues, contradictions |
| 9 | **Literary Critic** | Evaluates prose quality, pacing, emotional impact |

All story data lives in markdown files under `story/`. The agents read and write these files as they work. Everything is transparent and editable.

---

## Your Only Job

You provide:

- A brief (once, at the start)
- Small steering notes (whenever you want to adjust direction)
- Approval at checkpoints (yes/no, with optional notes)

You do **not** need to:

- Plan the plot
- Design the characters
- Outline chapters
- Write any prose
- Know anything about story structure

The less you prescribe, the more room the agents have to create something cohesive. Give direction, not instructions.

---

## Filling Out the Brief

Open `story/brief.md` and fill in what matters to you. Leave blank what you don't care about. A good brief is **specific about feeling, vague about plot**.

### Example: Minimal but effective brief

```markdown
# Book Brief

## Core idea

- Genre: science fiction
- Subgenre: quiet literary sci-fi
- Mood: melancholic, intimate, unsettling
- Themes: memory, identity, what we owe the dead
- Setting preference: a research station on an ice moon
- Time period: near future, 2080s
- Technology / magic preference: grounded biotech, no FTL
- Type of protagonist: a scientist, competent but emotionally avoidant
- Type of conflict: internal + interpersonal, not action-driven
- Desired ending feeling: bittersweet, earned, quiet

## Things I definitely want

- A strong sense of isolation and place
- One relationship that changes the protagonist
- A reveal that recontextualizes the opening

## Things I want to avoid

- Marvel-style witty banter
- Evil corporations as the main antagonist
- Explosive action climax

## Works I like as references

- Books: Annihilation, The Remains of the Day, Klara and the Sun
- Films: Arrival, Moon, Ex Machina
- Games:
- Shows: Severance, Station Eleven

## Reader experience I want

"I want something that feels like sitting alone in a cold room remembering
someone you lost, and slowly realizing the memory is wrong."

## Target scope

- Short story / novella / novel: novella
- Approx number of chapters: 6-8
- Approx page length: 25-35 pages
```

Notice: no plot. No character names. No outline. Just taste and boundaries. The agents will build everything from this.

---

## The Prompts

Use these one at a time. Each one advances the pipeline one stage. Copy-paste them directly into Claude Code.

### Prompt 1 — Theme and Style

```
Read CLAUDE.md and act as the orchestrator. Review the book brief and current
project state. If the brief is sufficiently complete, use the genre-theme-designer
agent to produce:

- story/theme.md
- story/style-guide.md

Then summarize:
- the proposed genre direction
- emotional promise
- tone
- what should happen next

Do not write worldbuilding or plot yet unless needed for coherence.
```

**Checkpoint:** Review theme.md and style-guide.md. Add notes to `story/user-feedback.md` if anything feels off.

### Prompt 2 — World, Characters, Plot

```
Act as the orchestrator. Read all current canon files and determine whether the
project is ready for story design. Then coordinate these agents in order:

1. worldbuilder -> update story/world.md and story/timeline.md
2. character-architect -> update story/characters.md
3. plot-architect -> update story/plot.md

Make sure each file is consistent with the brief, theme, style guide, user
feedback, and constraints.

When finished:
- summarize the resulting premise
- list any weak spots or open questions
- update story/manuscript-status.md

Do not write chapters yet.
```

**Checkpoint:** This is the most important review point. Read world.md, characters.md, and plot.md carefully. These become canon. Add feedback now or it gets harder to change later.

### Prompt 3 — Chapter Outline

```
Act as the orchestrator. Read all canon files. If world, characters, plot, and
timeline are sufficiently defined, use the chapter-planner agent to create:

- story/chapter-outline.md

Target a novella-scale proof of concept with strong pacing and distinct chapter
purposes.

After creating the outline:
- identify any chapters that feel weak or redundant
- suggest 2 or 3 possible improvements if needed
- update story/manuscript-status.md

Do not draft prose yet.
```

**Checkpoint:** Review the outline. This is the structural skeleton. If a chapter feels pointless, say so now.

### Prompt 4 — Chapter Briefs

```
Act as the orchestrator. Based on the approved chapter outline, use the
chapter-planner agent to create chapter briefs for all chapters under:

- story/chapter-briefs/

Each chapter brief must include:
- objective
- POV
- setting
- characters present
- scene sequence
- emotional progression
- canon facts to preserve
- desired ending energy

Update story/manuscript-status.md when done.
Do not write full chapter prose yet.
```

### Prompt 5 — Write One Chapter

```
Act as the orchestrator. Read all canon files, the chapter outline, previous
chapters if any, and the brief for chapter 1. Then use the chapter-writer agent
to draft:

- story/chapters/ch01.md

After drafting, use:
- continuity-editor to create story/reviews/continuity-ch01.md
- literary-critic to create story/reviews/literary-ch01.md

Then summarize:
- whether chapter 1 is safe to proceed with
- top revision suggestions
- any canon that should be updated

Do not write chapter 2 yet unless I ask.
```

Repeat Prompt 5 for each subsequent chapter, changing the chapter number.

### The "Just Keep Going" Prompt

Once you're confident in the quality and want to move faster:

```
Continue writing. Draft the next 2 chapters following the same process:
write, continuity review, literary review. Pause after both are done.
Update manuscript-status.md.
```

### The Final Compile Prompt

```
Act as the orchestrator. Run a final continuity pass across all chapters.
Then run a final literary pass. Summarize all issues found.
After revisions are complete, compile the manuscript to output/manuscript.md.
```

---

## Steering the Story

You don't need to rewrite the brief. Just add notes to `story/user-feedback.md`. The agents check this file before every major action.

### Good feedback (specific, actionable)

```markdown
## 2026-03-06

- The world feels too clean. Add more decay, moisture, failing systems.
- The protagonist is too stoic. Let them crack in chapter 3.
- The dialogue between Sera and Kael feels too formal. Make it wary, not polite.
- Cut the flashback in chapter 2. Show the memory through objects instead.
- The ending should feel like relief, not victory.
```

### Bad feedback (vague, unhelpful)

```
- Make it better.
- More interesting characters.
- The pacing is off.
- Needs more tension.
```

The more specific your feedback, the better the result. Point to concrete things: a character, a scene, a feeling, a line of dialogue.

### When to intervene

- **After Prompt 2** — This is the highest-leverage moment. World, characters, and plot are set here. Speak up now.
- **After chapter 1** — If the prose voice feels wrong, fix it before 5 more chapters sound the same.
- **When something bugs you** — Don't wait. Add a note to user-feedback.md immediately.

### When to stay hands-off

- During theme/style creation — let the agent interpret your brief first
- During chapter briefs — these are internal planning docs
- During continuity/literary review — let the editors do their job

---

## Utility Scripts

Check progress:
```bash
python3 scripts/chapter_status.py
```

Validate story files:
```bash
python3 scripts/validate_story.py
```

Compile all chapters into one manuscript:
```bash
python3 scripts/compile_manuscript.py
# Output: output/manuscript.md
```

---

## Project Structure

```
BookWriter/
├── CLAUDE.md                    # System instructions (agents read this)
├── README.md                    # This file (for you)
├── .claude/agents/              # Agent definitions
│   ├── orchestrator.md
│   ├── genre_theme_designer.md
│   ├── worldbuilder.md
│   ├── character_architect.md
│   ├── plot_architect.md
│   ├── chapter_planner.md
│   ├── chapter_writer.md
│   ├── continuity_editor.md
│   └── literary_critic.md
├── story/
│   ├── brief.md                 # YOUR INPUT — fill this out
│   ├── goals.md                 # Project scope
│   ├── theme.md                 # Genre, mood, themes
│   ├── style-guide.md           # Prose voice contract
│   ├── world.md                 # Setting, rules, history
│   ├── characters.md            # Cast, arcs, relationships
│   ├── plot.md                  # Conflict, structure, climax
│   ├── timeline.md              # Chronology
│   ├── chapter-outline.md       # Chapter-by-chapter plan
│   ├── constraints.md           # Hard rules
│   ├── user-feedback.md         # YOUR STEERING — add notes here
│   ├── manuscript-status.md     # Progress tracker
│   ├── chapter-briefs/          # Detailed brief per chapter
│   ├── chapters/                # Prose drafts (ch01.md, ch02.md...)
│   └── reviews/                 # Continuity and literary reviews
├── scripts/
│   ├── validate_story.py
│   ├── compile_manuscript.py
│   └── chapter_status.py
└── output/                      # Final compiled manuscript
```

---

## Tips for a Better Book

**Start small.** Aim for 6 chapters and one contained story. If it works, scale up. A tight novella beats a bloated novel.

**Be opinionated about feeling, not plot.** "I want dread that builds slowly" is better than "I want a twist where the villain is actually the mentor." Let the agents find the plot. You define the experience.

**Reference specific works.** "Like Arrival meets The Remains of the Day" gives the agents more to work with than "literary sci-fi."

**Say what you hate.** "No witty banter, no chosen-one narratives, no info-dumps" is extremely useful guidance. The agents will actively avoid these patterns.

**Review after Prompt 2.** This is the make-or-break moment. World, characters, and plot become canon. Everything downstream builds on them. If something feels wrong here, fix it before moving on.

**Give feedback through contrast.** "Chapter 2 felt rushed compared to chapter 1" or "The world description is too clinical — I want it to feel more like Roadside Picnic than a Wikipedia article."

**Don't over-steer.** If you find yourself rewriting the agents' output, you're working too hard. Add a note to user-feedback.md and re-run the prompt. Let the system do the work.

**Read your book.** Once the first draft compiles, read it straight through in `output/manuscript.md`. Your gut reaction after reading it as a whole is worth more than any per-chapter feedback.
