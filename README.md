# BookWriter

A multi-agent system that writes a novella for you. You provide a short creative brief, then guide the process with small, specific notes. Ten specialized AI agents handle everything else — theme, world, characters, plot, prose, and quality review.

---

## Quick Start

Three steps to get going:

1. **Fill out your brief** — Edit `story/brief.md` with your story idea (see examples below)
2. **Run Prompt 1** — Paste the first prompt into Claude Code to kick off the pipeline
3. **Review and steer** — The system pauses at checkpoints for your feedback

That's it. You don't need to plan the story yourself. The agents do the planning. You just say what you want to read.

---

## How It Works

The system has 11 agents that run in sequence:

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
| 10 | **Revision Writer** | Surgically revises chapters based on review feedback |
| 11 | **Reader Agent** | Evaluates the full manuscript as a first-time reader -- emotional engagement, clarity, satisfaction |
| 12 | **Humanizer** | Final pass for natural, human-readable prose. Removes AI writing tells, fixes robotic phrasing, ensures accessibility |

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

You can also run `/interview` — a guided creative interview that asks you questions in rounds and generates the brief for you.

### Example: The brief used for this project

```markdown
# Book Brief

## Core Idea
I want a mythic, psychological, and emotionally immersive story about a young
woman named Ada who takes psychedelic mushrooms in a forest and enters a liminal
state where the boundaries between herself and nature begin to dissolve. As she
tries to find her way out of the forest, she is forced to confront her inner
demons, which appear in the form of different animals. Along the way, she
receives guidance from her spirit animal, the frog, and gradually realizes that
the forest is not only a physical place but a reflection of her inner world. In
the end, her journey is not about escape, but about integration, acceptance, and
unity with everything around her.

## Genre
- Main genre: psychological fantasy
- Subgenre: mystical coming-of-consciousness / symbolic nature tale

## Tone / Mood
- dreamlike
- eerie
- introspective
- mystical
- emotionally raw
- ultimately peaceful

## Themes I Want
- unity with nature
- ego dissolution
- inner transformation
- fear and acceptance
- healing through surrender
- the self as part of a greater whole
- confronting inner darkness
- peace through integration rather than escape

## Themes I Do Not Want
- cynical nihilism
- simplistic good-versus-evil morality
- heavy-handed anti-drug moralizing
- purely literal storytelling with no symbolic depth

## Worldbuilding Preferences
- setting: an ancient, lush, mysterious forest that feels alive and spiritually
  charged
- time period: ambiguous or timeless, possibly contemporary but with mythic
  qualities
- technology / magic level: mostly naturalistic, but the psychedelic experience
  reveals a magical-symbolic layer beneath reality
- atmosphere: damp earth, moonlight, moss, insects, glowing fungi, shifting
  paths, whispering leaves, hidden ponds
- political / social texture: minimal; the focus should be intimate and personal
  rather than societal
- anything visually or emotionally important:
  - the forest should feel both beautiful and unsettling
  - the line between hallucination, spirit realm, and psychological truth should
    remain blurred
  - animals should feel archetypal, symbolic, and emotionally meaningful

## Character Preferences
- protagonist type: sensitive, intelligent, introspective, emotionally burdened,
  searching for meaning
- protagonist name: Ada
- antagonist or opposing force type: her own inner fears, traumas, guilt, shame,
  and fragmentation, expressed through animal encounters and the forest itself
- important relationship dynamics:
  - Ada and the frog as guide / spirit companion
  - Ada and the animal-demons as reflections of parts of herself
  - Ada and the forest as both adversary and teacher
- traits I want:
  - vulnerability
  - curiosity
  - emotional depth
  - capacity for wonder
  - gradual courage
- traits I want to avoid:
  - shallow "strong female character" cliches
  - excessive sarcasm
  - passive blank-slate behavior
  - melodrama without psychological depth

## Plot Preferences
- kind of conflict: an inward spiritual and psychological journey disguised as a
  struggle to survive and escape the forest
- pacing: immersive and measured, with moments of fear, awe, and revelation
- mystery / romance / action / philosophy balance:
  - mostly psychological mystery and spiritual philosophy
  - some suspense and symbolic confrontation
  - little or no romance
  - action should be meaningful and surreal rather than constant
- ending feeling: peaceful, transcendent, emotionally earned, and quietly
  profound
- any structural preferences:
  - the animal encounters should escalate in emotional intensity
  - each creature should represent a different inner demon or unresolved wound
  - the frog should appear more than once, sometimes subtly, sometimes directly
    guiding Ada
  - the ending should reveal that the forest was also inside Ada all along

## Things To Avoid
- cliche "it was all just a dream" ending
- preachy spirituality
- random fantasy elements with no symbolic meaning
- generic horror for its own sake
- too many side characters
- overly clinical discussion of psychedelics
- a fake-deep tone with vague philosophical language
- excessive exposition explaining every symbol

## Works I Like As References
- books:
  - Siddhartha
  - The Alchemist
  - Piranesi
  - Women Who Run With the Wolves
- films:
  - Annihilation
  - Princess Mononoke
  - The Green Knight
- games:
  - Journey
  - Gris
- what I like about them:
  - symbolic storytelling
  - emotional depth
  - mystical atmosphere
  - beautiful but unsettling nature imagery
  - stories that feel personal and spiritual without overexplaining themselves

## Symbolic Elements I Want
- frog as spirit guide, renewal, adaptability, and passage between worlds
- different animals representing different psychological demons
- mushrooms as threshold rather than simple plot device
- the forest as a living mirror of Ada's mind and soul
- water, mud, roots, spores, and moonlight as recurring motifs
- moments where Ada feels fear dissolve into connection

## Possible Inner Demons / Animal Forms
- wolf: fear, rage, survival instinct
- stag: pride, avoidance, false control
- snake: shame, temptation, transformation
- owl: knowledge that wounds, seeing too much
- boar: brute pain, stubbornness, unprocessed anger
- swarm of insects: anxiety, intrusive thoughts, overwhelm

## Target Length
- format: novella
- approximate chapters: 6 to 8
- approximate page count: 25 to 40 pages

## Reader Experience I Want
I want the book to feel like entering a strange, sacred, and frightening dream
that slowly becomes healing. I want the reader to feel lost with Ada at first,
then increasingly drawn into a deeper understanding of her inner world. The
story should feel sensory, symbolic, and emotionally honest, ending in a way
that feels peaceful, expansive, and deeply human.

## What Makes This Story Special
This is not just a story about being lost in a forest. It is a story about
discovering that the things we run from live inside us, and that peace comes not
from domination or escape, but from accepting our place within the living whole.
Ada's journey should feel personal, mythic, feminine, and transformative.
```

Notice: no plot outline. No chapter plan. Just taste, boundaries, and emotional direction. The agents will build everything from this.

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
- revision-writer to revise story/chapters/ch01.md based on both reviews
- humanizer to do a final pass on the prose (see story/humanizer-checklist.md):
  remove AI writing tells, fix robotic phrasing, ensure readability and
  natural sentence flow

Then summarize:
- what was revised and why
- whether chapter 1 is safe to proceed with
- any canon that should be updated

Do not write chapter 2 yet unless I ask.
```

Repeat Prompt 5 for each subsequent chapter, changing the chapter number.

### The "Just Keep Going" Prompt

Once you're confident in the quality and want to move faster:

```
Continue writing. Draft the next 2 chapters following the same process:
write, continuity review, literary review, revision, humanizer pass.
Pause after both are done. Update manuscript-status.md.
```

### The Final Compile Prompt

```
Act as the orchestrator. Run a final continuity pass across all chapters.
Then run a final literary pass. Summarize all issues found.
Use the revision-writer to address critical issues in each chapter.
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

## Commands

These are slash commands you can run directly in Claude Code.

### `/interview` — Create a Book Brief

A guided creative interview that asks you questions in 6 rounds (seed, world, characters, story shape, taste/boundaries, experience) and generates a complete `story/brief.md` from your answers. Use this instead of writing the brief by hand.

### `/build-chapter` — Write the Next Chapter

Automatically detects the next unwritten chapter and runs the full pipeline: draft, continuity review, literary review, revision, humanizer pass, and running-state update. One command, one complete chapter.

### `/next-stage` — Run the Next Pipeline Stage

Automatically determines where the project is in the pipeline and executes the next stage. Tracks progress through all 7 stages:

1. **Theme & Style** — generates theme.md and style-guide.md (checkpoint: user review)
2. **World, Characters, Plot** — generates world.md, characters.md, plot.md (checkpoint: user review)
3. **Chapter Outline** — generates chapter-outline.md (checkpoint: user review)
4. **Chapter Briefs** — generates all chapter briefs
5. **Write Chapters** — drafts, reviews, revises, and humanizes one chapter at a time (checkpoint: every 2 chapters)
6. **Full Reviews & Revisions** — full-manuscript continuity, literary, and reader passes + revisions (checkpoint: user review)
7. **Compile** — assembles manuscript and exports EPUB

Just keep running `/next-stage` to advance through the entire book-writing pipeline. The command pauses at checkpoints for your review before continuing.

### `/destroy` — Reset for a New Book

Clears all story-specific content so you can start a fresh book. **Requires explicit confirmation** before proceeding. This will:

- Delete all chapters, chapter briefs, reviews, output files, and images
- Reset all story files (brief, theme, world, characters, plot, etc.) to empty templates
- Preserve the project structure, agents, commands, scripts, README, and CLAUDE.md

Run `/interview` or edit `story/brief.md` after destroying to begin a new book.

### `/export` — Export to EPUB

Generates an EPUB file from the compiled manuscript with cover art and chapter images.

```bash
# Basic usage (uses default title and author)
/export

# The script can also be run directly with custom options:
.venv/bin/python3 scripts/export_epub.py --title "My Book Title" --author "Author Name"
```

The export will:
1. Read the compiled manuscript from `output/manuscript.md`
2. Include the cover image from `ImageAssets/Book_cover.png` (if present)
3. Include chapter images from `ImageAssets/` (resized for e-readers, if present)
4. Output to `output/the-forest-inside.epub`

If no images exist, it generates a text-only EPUB.

**Requirements:** Python virtual environment with `ebooklib`, `markdown`, and `Pillow`:
```bash
python3 -m venv .venv
.venv/bin/pip install ebooklib markdown Pillow
```

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

## Running State -- How Continuity Scales

As the book grows past 4-5 chapters, reading every prior chapter in full before writing the next one becomes impractical -- context limits, agent focus, and token costs all suffer. The running state file solves this.

**What it is:** A cumulative state tracker (`story/running-state.md`) that records everything that has happened in the story -- Ada's physical condition, injuries, objects, psychological state, lessons learned, motifs, foreshadowing, unresolved threads, and chapter summaries.

**Why it exists:** By chapter 10, you'd have ~50,000 words of prior prose plus ~20,000 words of canon files. The running state file lets agents access all continuity-critical information without re-reading everything. It stays at ~1,000-2,000 words regardless of how many chapters exist.

**How it works:** After each chapter is revised, the orchestrator updates `running-state.md` from the chapter's Continuity Notes. The chapter writer reads this file + the 2 most recent full chapters (for voice continuity) instead of all prior chapters. The continuity editor reads it + the 3 most recent chapters + Continuity Notes sections from all earlier chapters.

**The rule:** When in doubt, include the detail. A minor detail from Chapter 3 might be critical in Chapter 9. The cost of an extra line is near zero; the cost of a missed detail is a broken continuity.

**For you:** If you notice something in the running state that's wrong or missing, edit it directly. The agents trust this file as ground truth alongside the canon files.

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
│   ├── literary_critic.md
│   ├── reader_agent.md
│   └── revision_writer.md
├── .claude/commands/              # Slash commands
│   ├── interview.md
│   ├── build-chapter.md
│   ├── next-stage.md
│   ├── destroy.md
│   └── export.md
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
│   ├── running-state.md         # Cumulative state tracker
│   ├── constraints.md           # Hard rules
│   ├── humanizer-checklist.md   # Final-pass agent checklist
│   ├── user-feedback.md         # YOUR STEERING — add notes here
│   ├── manuscript-status.md     # Progress tracker
│   ├── chapter-briefs/          # Detailed brief per chapter
│   ├── chapters/                # Prose drafts (ch01.md, ch02.md...)
│   └── reviews/                 # Continuity and literary reviews
├── scripts/
│   ├── validate_story.py
│   ├── compile_manuscript.py
│   ├── chapter_status.py
│   └── export_epub.py
├── ImageAssets/                   # Cover and chapter images
└── output/                        # Final manuscript and EPUB
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
