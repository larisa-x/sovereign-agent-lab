"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
I noticed that all three formats gave correct answers, but, interestingly, not the same answer. Plain text picked The Haymarket Vaults, while XML and sandwich both picked The Albanach. At first, I thought one must be wrong, but both actually meet all three constraints (capacity >= 160, vegan, available). So the format changed which correct answer the model landed on, but didn't cause any mistakes. I guess with only seven short lines of data, the model doesn't struggle to find the right answer regardless of how you present it.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
I think The Holyrood Arms is the trickiest one because it looks almost perfect, as it has exactly 160 capacity and vegan, so if you just glance at it you
might think it works. The only thing wrong is that it's full. The New Town Vault is easier to catch because it says vegan no, which is a more obvious
fail. I can see how a weaker model might get tricked by Holyrood Arms.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = None   # True or False

PART_C_PLAIN_ANSWER    = "Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
The small Gemma 2 2B model also got the right answer every time, which I didn't expect. But I noticed a couple of things. First, it always picked Haymarket Vaults while the bigger 70B model picked Albanach in the XML and sandwich formats. Maybe the smaller model just grabs the first venue that fits? Also in the plain text condition it returned "Haymarket Vaults" without the "The", which is a bit sloppy — the structured formats gave back the full name "The Haymarket Vaults". So even though nothing fully broke, the format did seem to affect how carefully the small model answered.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when things get harder for the model. In this exercise everything was short and clean so all formats worked fine, even on
the small model. But I can see how it would start to matter if the prompt was much longer, if more venues look almost right, or if you use an even cheaper model. The sandwich format repeating the question at the end makes sense to me now — if the context is long the model might forget what it was asked. For agents specifically I think this matters a lot because every tool call adds more text to the conversation and at some point the model could lose track
of the original task if the context is not well structured.
"""
