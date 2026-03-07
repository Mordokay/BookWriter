Act as the orchestrator. Determine which pipeline stage should run next, execute it, and pause at the appropriate checkpoint.

## Step 1: Read project state

Read these files to determine current progress:
- story/manuscript-status.md
- story/brief.md
- story/user-feedback.md

## Step 2: Determine next stage

Based on manuscript-status.md, identify the next incomplete step and execute it:

### Stage 1: Theme and Style
**Condition:** brief completed is checked, but theme and style guide are not.
**Action:** Read CLAUDE.md and act as the orchestrator. Review the book brief and current project state. If the brief is sufficiently complete, use the genre-theme-designer agent to produce:
- story/theme.md
- story/style-guide.md

Update goals.md and constraints.md as needed. Update manuscript-status.md.

Then summarize:
- the proposed genre direction
- emotional promise
- tone
- what should happen next

Do not write worldbuilding or plot yet unless needed for coherence.

**CHECKPOINT: Pause and ask the user to review theme.md and style-guide.md. Suggest they add notes to story/user-feedback.md if anything feels off. Do not proceed until the user says to continue.**

### Stage 2: World, Characters, Plot
**Condition:** theme and style guide exist, but world/characters/plot do not.
**Action:** Read all current canon files and determine whether the project is ready for story design. Then coordinate these agents in order:
1. worldbuilder -> produce story/world.md and story/timeline.md
2. character-architect -> produce story/characters.md
3. plot-architect -> produce story/plot.md and update timeline.md

Make sure each file is consistent with the brief, theme, style guide, user feedback, and constraints. Do not write chapters yet.

When finished:
- summarize the resulting premise
- list any weak spots or open questions
- update story/manuscript-status.md

**CHECKPOINT: This is the most important review point. Pause and ask the user to review world.md, characters.md, and plot.md carefully. These become canon. Add feedback now or it gets harder to change later. Do not proceed until the user says to continue.**

### Stage 3: Chapter Outline
**Condition:** world, characters, and plot exist, but chapter outline does not.
**Action:** Read all canon files. If world, characters, plot, and timeline are sufficiently defined, use the chapter-planner agent to create:
- story/chapter-outline.md

Target strong pacing and distinct chapter purposes. Do not draft prose yet.

After creating the outline:
- identify any chapters that feel weak or redundant
- suggest 2 or 3 possible improvements if needed
- update story/manuscript-status.md

**CHECKPOINT: Pause and ask the user to review the outline. This is the structural skeleton -- if a chapter feels pointless, now is the time to say so. Do not proceed until the user says to continue.**

### Stage 4: Chapter Briefs
**Condition:** chapter outline exists and is approved, but chapter briefs do not exist.
**Action:** Based on the approved chapter outline, use the chapter-planner agent to create chapter briefs for all chapters under:
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

Do not write full chapter prose yet. Update story/manuscript-status.md.

**After completion, report what was created and suggest the user proceed to chapter writing.**

### Stage 5: Write Chapters
**Condition:** chapter briefs exist, but not all chapters are drafted.
**Action:** Execute the `/build-chapter` command. This handles the full chapter pipeline automatically: detect the next unwritten chapter, draft it, run continuity and literary reviews, revise, humanize, and update running state and manuscript status.

Do not write the following chapter unless asked.

**CHECKPOINT: After every 2 chapters, pause and ask the user to review. Do not proceed until the user says to continue.**

If all chapters are drafted, move to Stage 6.

### Stage 6: Full Reviews and Revisions
**Condition:** all chapters are drafted, but full passes are not complete.
**Action:**
1. Run continuity-editor as a full-manuscript pass -> story/reviews/continuity-full-pass-01.md
2. Run literary-critic as a full-manuscript pass -> story/reviews/literary-full-pass-01.md
3. Run reader-agent for a reading-experience review -> story/reviews/reader-review.md
4. Run revision-writer to address issues found in all three reviews
5. Update manuscript-status.md

**CHECKPOINT: Pause and ask the user to review the findings. Do not proceed until the user says to continue.**

### Stage 7: Compile
**Condition:** all reviews and revisions are complete, but manuscript is not compiled.
**Action:**
1. Compile manuscript to output/manuscript.md (prose only, no metadata)
2. Run the EPUB export: .venv/bin/python3 scripts/export_epub.py
3. Update manuscript-status.md to mark compilation complete

**Report final word count, file locations, and that the pipeline is complete.**

## Step 3: Report

After executing the current stage, report:
- What stage was executed
- What was produced
- What the next stage will be
- Whether a checkpoint pause is in effect
