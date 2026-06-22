from rules import rules
from diagnosis import run_inference

print("\n")
print("=" * 40)
print("RULE BASED EXPERT SYSTEM")
print("=" * 40)

user_input = input(
    "\nEnter symptoms separated by commas:\n"
)

facts = {

    item.strip().lower()

    for item in user_input.split(",")
}

final_facts, logs = run_inference(
    facts,
    rules
)

print("\n")

print("Reasoning Steps")

print("-" * 30)

for step in logs:
    print(step)

print("\n")

print("Knowledge Base")

print("-" * 30)

for item in sorted(final_facts):
    print(item)