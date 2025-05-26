# 🧠 OCI Quiz App

A Python-based CLI quiz application to help you study. It generates randomized quizzes based on category distribution and supports two learning modes:

- ✅ **Flashcard Mode** – Recall and self-grade
- ✅ **Multiple Choice Mode** – Select from shuffled answers

---

## 📦 Features

- Interactive terminal-based testing
- Randomized question and option order
- Deduplication of question variations (same ID)
- Self-evaluation (flashcards)
- Balanced quiz by category

---

## 📁 Files

| File            | Purpose                                             |
|-----------------|-----------------------------------------------------|
| `quiz.py`       | Main Python script to run the test                  |
| `testOrg.json`  | Number of questions per category                    |
| `questions.json`| Question bank with options, answers, and metadata   |

---

## 🚀 How to Run

### 1. Prerequisites

- Python 3

### 2. Setup

Ensure all files (`quiz.py`, `testOrg.json`, and `questions.json`) are in the same directory.

### 3. Run the script

```bash
python quiz.py
```

### 4. Choose the test mode

```
Copy code
📘 Select test mode:
1 - Flashcard mode (no options shown)
2 - Multiple Choice mode
Enter 1 or 2:
```

### 5. Answer the questions
In Flashcard Mode, press Enter to reveal the answer and then type 1 if correct or 0 if wrong.

In Multiple Choice Mode, select the option number corresponding to your answer.

**💡 Example**
Flashcard Mode

```
Copy code
Q1: Which is the right dummy answer?
💡 Think about your answer. Press Enter to reveal it...
✅ Correct answer: Dummy answer
Did you get it right? (1 = Yes, 0 = No): 1
```

**Multiple Choice Mode**
```
Q2: Which is the right dummy answer?
  1. Dummy wrong answer
  2. Dummy wrong answer
  3. Dummy wrong answer
  4. Dummy answer

Your answer (number): 3
✅ Correct!
```

## 🧩 JSON Structure
**testOrg.json**

```
{
    "Math":"1",
    "English":"2",
    "Science":"1",
    "Administration":"1"
}
```

This is used to balance the test

**questions.json**
This file is used to get the questions

```
{
    "Questions" :[
        {
            "id":"01",
            "question":"Dummy question?",
            "options": [
                "Dummy answer",
                "Dummy wrong answer",
                "Dummy wrong answer",
                "Dummy wrong answer"
            ],
            "answer": "Dummy answer", 
            "type":"Services"
        },
        // more questions
    ]
}
```

✅ Future Improvements
* Add a timer for each question
* Save results to file (CSV/JSON)
