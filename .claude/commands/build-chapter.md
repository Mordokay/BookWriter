Act as the orchestrator. Determine the next chapter to write by scanning story/chapters/ for existing chapter files and finding the first gap (e.g., if ch01.md through ch04.md exist, the next chapter is ch05).

Let N be that chapter number, zero-padded to two digits (e.g., "05").

Read all canon files:
- story/brief.md
- story/theme.md
- story/style-guide.md
- story/constraints.md
- story/world.md
- story/characters.md
- story/plot.md
- story/timeline.md
- story/chapter-outline.md
- story/running-state.md
- story/user-feedback.md

Read the chapter brief: story/chapter-briefs/chN.md

Read the 2 most recent existing chapters in full (for voice/tone continuity).

Then execute the full chapter pipeline:

1. **chapter-writer agent** -- Draft story/chapters/chN.md
2. **continuity-editor agent** -- Create story/reviews/continuity-chN.md
3. **literary-critic agent** -- Create story/reviews/literary-chN.md
4. **revision-writer agent** -- Revise story/chapters/chN.md based on both reviews
5. **humanizer pass** -- Final pass on the prose (see story/humanizer-checklist.md): remove AI writing tells, fix robotic phrasing, ensure readability and natural sentence flow
6. **Update story/running-state.md** from the chapter's Continuity Notes
7. **Update story/manuscript-status.md**

After the full pipeline completes, summarize:
- What was revised and why
- Whether the chapter is safe to proceed from
- Any canon that should be updated

Do not write the following chapter unless asked.