"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer",
]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = ""

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True   # True or False

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "placeholder"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://placehold.co/1200x628/1a1a2e/eaeaea?text=The+Haymarket+Vaults+%7C+160+guests&id=2ef939fbbaf6"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography"

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
Because the tool always returns success=True with a valid image URL no matter what. Whether it uses a real image model or the placeholder fallback, the
agent gets back the same shape of response. So when Nebius removed FLUX the agent didn't even notice — it just got a placeholder URL instead of a real
image and kept going as normal.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The tool came back saying The Bow Bar has capacity 80 and status full with meets_all_constraints false. The agent didn't stop or ask me what to do — it
just went ahead and checked The Haymarket Vaults on its own. Nobody told it to try another venue, it just figured out that it should.
"""

SCENARIO_1_FALLBACK_VENUE = "The Haymarket Vaults"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
The agent went through all four known venues one by one — The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar. Every single one came
back with meets_all_constraints false because none of them can hold 300 people. The agent then said honestly that there is no venue in the list that
works and suggested looking elsewhere or splitting across multiple venues. It didn't make up a pub name.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False  # True or False

SCENARIO_3_RESPONSE = "The agent said it doesn't have a tool for train schedules and can only help with venue booking, weather, catering, and flyers. It suggested checking National Rail or another travel service instead."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
I think this is the right thing to do. If the agent made up a train time and someone missed their actual train that would be really bad. It's better to
just say I don't know and point the person to the right place. I learned from this that a good agent should know the limits of its tools and be honest when
something is outside what it can do rather than trying to be helpful and getting it wrong.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
The LangGraph diagram is just one loop — start, agent, tools, end. The model decides everything at runtime so the graph looks super simple even though the
agent can do complex things. But when I looked at flows.yml for Rasa it's completely different. Every flow is written out explicitly with specific steps
like collect guest_count, collect vegan_count, collect deposit, then run the validation action. The LLM only picks which flow to start and after that Rasa
follows the steps exactly. So LangGraph is flexible but you can't predict what it will do, while Rasa is rigid but you can read exactly what will happen.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The thing that surprised me most was in Task C Scenario 1 when the agent pivoted from The Bow Bar to The Haymarket Vaults completely on its own. I
expected it to just report that Bow Bar doesn't work and stop. But instead it went and checked another venue without anyone telling it to. That's when it
clicked for me what "autonomous" actually means — the agent can recover from problems by itself. I was also surprised in Scenario 2 that it checked all
four venues systematically before saying none of them work. It could have given up after two or just made something up but it was thorough and honest
about the result.
"""