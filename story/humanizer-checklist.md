# Humanizer Agent Checklist

Final-pass agent. Runs after the revision-writer, before a chapter is marked complete. The goal is to make the prose read as if written by a skilled human novelist. Fix anything that feels machine-generated, overly precise, unnaturally structured, or inaccessible to a general reader.

**Only modify the prose/Draft section. Do not touch Continuity Notes, Revision Log, or Chapter Intent.**

---

## 1. Em-dash and punctuation habits

- [ ] Zero em-dashes ("--" or "---") in prose. Replace with commas, periods, colons, semicolons, or restructure the sentence.
- [ ] Semicolons used sparingly (no more than 5-8 per chapter). Most readers experience semicolons as academic. Prefer periods or commas.
- [ ] Colons used sparingly for elaboration. Not every list or explanation needs a colon. Sometimes a period and a new sentence is more natural.
- [ ] Ellipsis used only for interrupted or trailing thought, not as a general pause device.

## 2. AI-tell words and phrases

Flag and replace any of these (they appear frequently in AI writing and rarely in published fiction):

**Single words:** delve, tapestry, myriad, whilst, amidst, amongst, furthermore, moreover, nonetheless, interplay, nuance (as adjective), juxtaposition, visceral (overused), palpable, ethereal, ephemeral, testament, cacophony, symphony (when not about music), gossamer, iridescent, luminescent (check frequency), ineffable, corporeal, primordial, eldritch, uncanny (check frequency), liminal (check frequency)

**Phrases:** "a testament to," "a symphony of," "a tapestry of," "a dance of," "the interplay between," "sent a shiver down," "in the grand scheme," "it was as if," "seemed to (verb) with," "couldn't help but," "found herself (verb)ing," "the weight of (abstraction)," "hung heavy in the air," "cut through the silence," "washed over her," "the world seemed to," "time stood still," "her heart sank," "a knowing look," "spoke volumes," "the silence was deafening," "pregnant pause," "steeled herself"

**Note:** Some of these words are fine in the right context. The issue is density. If "visceral" appears once in a chapter, it might work. If it appears three times, it's a tell. Use judgment.

## 3. Sentence structure patterns

- [ ] No more than 3 consecutive sentences starting with "She" or "Her." Break clusters with environmental subjects, body-part subjects, participial openings, sentence fragments, or dialogue.
- [ ] No more than 2 consecutive sentences using the same structure (e.g., compound with "and," or subject-verb-object). Vary rhythm.
- [ ] Watch for artificially balanced constructions: "Not X but Y. Not A but B. Not C but D." One pair is powerful. Two is a pattern. Three is a machine.
- [ ] Watch for triple-stacked parallel phrases: "the X of Y, the A of B, the C of D." One set per page maximum.
- [ ] Avoid overly symmetrical paragraphs where the last sentence mirrors or answers the first. Humans don't write in such tidy loops.
- [ ] **Choppy comma-staccato sequences.** Watch for runs of short sentences packed with commas that create a robotic, instructional rhythm. Example: "You moved, not the forest. You are disoriented. Stop, breathe, reorient." This reads like a list of commands, not natural prose. Fix by combining short sentences into longer ones, varying clause length, or replacing comma-separated imperatives with flowing thought. A natural interior voice might say: "She had moved, not the forest. She was disoriented and needed to stop and breathe and find her bearings." The goal is sentence-length variety within every paragraph — short sentences gain power from contrast with longer ones, not from being stacked together.

## 4. Vocabulary accessibility

- [ ] No Latin species names in prose (use common names or descriptions).
- [ ] No word that a typical adult reader would need to look up, unless the context makes its meaning clear. Unusual words are fine if the sentence teaches the reader what they mean.
- [ ] Technical/botanical terms are acceptable only if they're common enough that most readers have encountered them (e.g., "moss," "fern," "cedar," "toadstool" are fine; "sporophyte," "rhizomorph," "basidiocarp" are not).
- [ ] If the protagonist recognizes a species, describe what they see. Don't name the taxonomy.

## 5. Description and metaphor

- [ ] No stacked metaphors (two different metaphors for the same thing in the same paragraph).
- [ ] No metaphors that explain themselves: "like a door closing, shutting out the light" (the second clause explains the first).
- [ ] Similes should be concrete and unexpected. Flag any simile that could appear in any novel without modification.
- [ ] "The way" as a simile connector: maximum 3 per chapter. Prefer "like" or restructure.
- [ ] "As if" hedging: maximum 3 per chapter. When the description is vivid enough, state it directly.
- [ ] Avoid describing emotions with abstract nouns: "a wave of dread," "a surge of panic," "a flood of relief." Show the physical sensation instead.

## 6. Filter words and distancing

- [ ] Remove "she felt," "she noticed," "she realized," "she could see," "she could hear," "she could feel," "she was aware of." Present the sensation directly.
- [ ] Remove "seemed to," "appeared to," "began to" (when the action simply happens).
- [ ] Remove "found herself" constructions.
- [ ] Remove "something like" and "something that was almost" unless genuine ambiguity is the point.

## 7. Dialogue and interior voice

- [ ] Interior thoughts should sound like a real person thinking, not like polished prose. Short. Fragmented. Sometimes grammatically rough.
- [ ] If the protagonist has an interior monologue beat, it should be distinct from the narrator's voice. Each internal register should have its own quality.
- [ ] Non-human or fantastical dialogue should feel alien and strange, never like a therapist or self-help book.

## 8. Pacing and padding

- [ ] Flag any sentence that restates what the previous sentence already established.
- [ ] Flag any paragraph where the last 1-2 sentences could be cut without losing information or impact.
- [ ] Flag any description that goes on longer than the moment warrants (a two-sentence action shouldn't be followed by a six-sentence sensory elaboration).
- [ ] Physical actions should take roughly proportional prose-space to their real-time duration. A glance shouldn't take a paragraph.

## 9. Read-aloud test

- [ ] Read the prose mentally as if speaking it aloud. Flag any sentence that feels unnatural to say: too many nested clauses, too many commas forcing pauses, or rhythms that trip the tongue.
- [ ] Flag any paragraph where the rhythm is monotonously even (all medium-length sentences) or monotonously choppy (all fragments). Good prose varies.

## 10. Overall naturalness

- [ ] Does this read like a chapter from a published novel you'd find in a bookstore?
- [ ] Would a reader who is suspicious of AI-generated text flag anything?
- [ ] Is there anything that feels "too perfect," too symmetrical, too neatly constructed? Humans are messier. Good prose has controlled imperfection.
- [ ] Are there any moments where the writing is clearly showing off rather than serving the story?

---

## Output format

The humanizer agent should:
1. Read the full chapter prose
2. Make all fixes directly using Edit calls (do not just report issues)
3. After all fixes, write a brief summary of changes made to the chapter's Revision Log section
4. Report a final count of changes made

## What NOT to change

- Do not flatten the literary voice into generic commercial fiction. The prose should remain rich and careful.
- Do not remove all unusual words. Remove only the ones that break immersion or scream "AI."
- Do not simplify complex sentences that are complex for a reason (building tension, mirroring disorientation).
- Do not touch the Continuity Notes, Revision Log headers, or Chapter Intent sections.
- Do not change character voice, plot details, or factual content.
- Preserve the story's existing motifs and callbacks. If a phrase is deliberately echoing an earlier chapter, do not alter it without understanding the callback.
