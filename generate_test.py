import json
import random

# Load question categories (testOrg)
with open("testOrg_private.json", "r") as f:
    category_counts = json.load(f)

# Load questions
with open("questions_private.json", "r") as f:
    all_questions = json.load(f)["Questions"]

# Deduplicate by question id (keep only one variation per id)
question_map = {}
for q in all_questions:
    if q["id"] not in question_map:
        question_map[q["id"]] = []
    question_map[q["id"]].append(q)

# Randomly select one version per question ID
unique_questions = [random.choice(variations) for variations in question_map.values()]

# Group questions by category
category_question_map = {}
for q in unique_questions:
    category_question_map.setdefault(q["type"], []).append(q)

# Build the test based on category_counts
test_questions = []
for category, count in category_counts.items():
    questions_in_category = category_question_map.get(category, [])
    if len(questions_in_category) < int(count):
        raise ValueError(f"Not enough questions in category '{category}'. Required: {count}, Available: {len(questions_in_category)}")
    selected = random.sample(questions_in_category, int(count))
    test_questions.extend(selected)

# Ask user which test mode to use
print("📘 Select test mode:")
print("1 - Flashcard mode (no options shown)")
print("2 - Multiple Choice mode")
while True:
    mode_input = input("Enter 1 or 2: ").strip()
    if mode_input in {"1", "2"}:
        flashcard_mode = (mode_input == "1")
        break
    else:
        print("❌ Invalid input. Please enter 1 or 2.")

# Shuffle final test order
random.shuffle(test_questions)

# Run the interactive test
score = 0
print("\n🔍 Starting the Test...\n")

for idx, q in enumerate(test_questions, 1):
    print(f"Q{idx}: {q['question']}")

    if flashcard_mode:
        input("💡 Think about your answer. Press Enter to reveal it...")
        print(f"✅ Correct answer: {q['answer']}")
        while True:
            mark = input("Did you get it right? (1 = Yes, 0 = No): ").strip()
            if mark in {"1", "0"}:
                score += int(mark)
                print()
                break
            else:
                print("Please enter 1 (correct) or 0 (incorrect).")
    else:
        options = q["options"].copy()
        random.shuffle(options)
        for i, opt in enumerate(options):
            print(f"  {i + 1}. {opt}")
        while True:
            try:
                choice = int(input("Your answer (number): "))
                if 1 <= choice <= len(options):
                    break
                else:
                    print("Invalid option. Try again.")
            except ValueError:
                print("Please enter a number.")
        selected_answer = options[choice - 1]
        if selected_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. Correct answer: {q['answer']}\n")

# Final score
print(f"🎉 Test Completed. Your Score: {score} / {len(test_questions)}")
