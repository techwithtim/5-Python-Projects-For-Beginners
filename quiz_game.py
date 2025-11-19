#!/usr/bin/env python3
"""
advanced_quiz.py

Advanced terminal-based quiz:
- Multiple choice
- Randomized questions/options
- Difficulty levels
- Optional timed questions (Unix only)
- Stores scores to quiz_scores.json (leaderboard)
- Easy to extend with external question bank (see QUESTIONS list)
"""

import json
import os
import random
import sys
import time
import datetime
import platform

# Optional colored output (nice but optional)
try:
    from colorama import init as colorama_init, Fore, Style
    colorama_init(autoreset=True)
except Exception:
    class _C:
        def __getattr__(self, _): return ""
    Fore = Style = _C()

SCORES_FILE = "quiz_scores.json"

# ---- Sample question bank (replace / load from JSON/CSV if you want) ----
QUESTIONS = [
    {
        "q": "What does CPU stand for?",
        "choices": ["Central Processing Unit", "Computer Primary Unit", "Central Power Unit", "Control Processing Unit"],
        "answer": "Central Processing Unit",
        "difficulty": "easy"
    },
    {
        "q": "What does GPU stand for?",
        "choices": ["Graphics Processing Unit", "General Processing Unit", "Graphical Program Unit", "Global Processing Unit"],
        "answer": "Graphics Processing Unit",
        "difficulty": "easy"
    },
    {
        "q": "What does RAM stand for?",
        "choices": ["Random Access Memory", "Readily Available Memory", "Random Active Memory", "Rapid Access Memory"],
        "answer": "Random Access Memory",
        "difficulty": "easy"
    },
    {
        "q": "Which sorting algorithm has average time complexity O(n log n) and is often used for large datasets?",
        "choices": ["Bubble sort", "Selection sort", "Merge sort", "Insertion sort"],
        "answer": "Merge sort",
        "difficulty": "medium"
    },
    {
        "q": "In Python, what does GIL (Global Interpreter Lock) affect?",
        "choices": ["I/O performance only", "Ability to use multiple cores for CPU-bound Python bytecode", "Memory allocation", "Garbage collection timing"],
        "answer": "Ability to use multiple cores for CPU-bound Python bytecode",
        "difficulty": "medium"
    },
    {
        "q": "Which of the following is a non-relational (NoSQL) database?",
        "choices": ["PostgreSQL", "MySQL", "MongoDB", "SQLite"],
        "answer": "MongoDB",
        "difficulty": "easy"
    },
    {
        "q": "What is the main idea behind Docker?",
        "choices": ["Virtual machines with full OS", "Containerization for lightweight, portable runtime environments", "A new programming language", "A database engine"],
        "answer": "Containerization for lightweight, portable runtime environments",
        "difficulty": "medium"
    },
    {
        "q": "Which neural network architecture is best suited for sequence data like time series or text?",
        "choices": ["Convolutional Neural Network (CNN)", "Recurrent Neural Network (RNN)", "K-Means", "PCA"],
        "answer": "Recurrent Neural Network (RNN)",
        "difficulty": "hard"
    },
    {
        "q": "Which Big O gives worst-case time complexity for QuickSort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "answer": "O(n^2)",
        "difficulty": "hard"
    },
]

# ---- Utility: timed input (Unix-only using signal). Fallback to normal input on Windows ----
def timed_input(prompt, timeout):
    """
    Returns input string if user types within timeout seconds.
    If platform doesn't support alarm (Windows), returns normal input (no timeout).
    """
    if platform.system() == "Windows":
        # Windows: fallback to normal input (no reliable cross-platform builtin)
        return input(prompt)
    else:
        import signal

        def handler(signum, frame):
            raise TimeoutError

        old = signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        try:
            val = input(prompt)
            signal.alarm(0)
            return val
        except TimeoutError:
            print("\n" + Fore.YELLOW + "Time's up!")
            return None
        finally:
            signal.signal(signal.SIGALRM, old)


# ---- Persistence functions ----
def load_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_score(entry):
    data = load_scores()
    data.append(entry)
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def show_leaderboard(top_n=5):
    data = load_scores()
    if not data:
        print(Fore.CYAN + "No previous results found.")
        return
    data_sorted = sorted(data, key=lambda x: x.get("percentage", 0), reverse=True)
    print(Fore.GREEN + f"\nTop {min(top_n, len(data_sorted))} Leaderboard:")
    for i, e in enumerate(data_sorted[:top_n], start=1):
        time_str = e.get("timestamp", "unknown time")
        print(f"{i}. {e['user']} — {e['score']}/{e['total']} ({e['percentage']:.2f}%) — {time_str}")


# ---- Core quiz logic ----
def run_quiz(user, difficulty="all", timed=False, per_question_time=15, num_questions=None):
    # Filter questions by difficulty
    pool = [q.copy() for q in QUESTIONS if difficulty == "all" or q.get("difficulty") == difficulty]
    if not pool:
        print(Fore.RED + "No questions match that difficulty.")
        return

    random.shuffle(pool)
    if num_questions:
        pool = pool[:num_questions]

    total = len(pool)
    score = 0
    details = []

    print(Fore.CYAN + f"Starting quiz for {user} — {total} questions. Timed mode: {timed}.\n")

    for i, q in enumerate(pool, start=1):
        # shuffle choices
        choices = q["choices"].copy()
        random.shuffle(choices)

        print(Style.BRIGHT + f"Q{i}/{total}: {q['q']}")
        for idx, ch in enumerate(choices, start=1):
            print(f"  {idx}. {ch}")

        # get answer (timed or not)
        prompt = f"Your answer (1-{len(choices)}): "
        if timed:
            ans = timed_input(prompt, per_question_time)
            if ans is None:
                # timed out
                user_choice = None
            else:
                user_choice = ans.strip()
        else:
            user_choice = input(prompt).strip()

        # Validate user input
        chosen_text = None
        correct = False
        if user_choice and user_choice.isdigit():
            idx = int(user_choice) - 1
            if 0 <= idx < len(choices):
                chosen_text = choices[idx]
                correct = (chosen_text == q["answer"])
        else:
            # allow direct text match fallback
            if user_choice:
                user_choice_text = user_choice.lower()
                for ch in choices:
                    if ch.lower() == user_choice_text:
                        chosen_text = ch
                        correct = (ch == q["answer"])
                        break

        if correct:
            print(Fore.GREEN + "✔ Correct!\n")
            score += 1
            details.append({"question": q["q"], "your": chosen_text, "correct": q["answer"], "result": "correct"})
        else:
            print(Fore.RED + f"✖ Incorrect. Correct answer: {q['answer']}\n")
            details.append({"question": q["q"], "your": chosen_text if chosen_text else "No valid answer", "correct": q["answer"], "result": "incorrect"})

        # small pause to improve UX
        time.sleep(0.5)

    percentage = (score / total) * 100 if total else 0.0

    print(Style.BRIGHT + Fore.BLUE + "\nQuiz Completed!")
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")
    accuracy = sum(1 for d in details if d["result"] == "correct") / total * 100
    print(f"Accuracy: {accuracy:.2f}%")

    # Save result
    entry = {
        "user": user,
        "score": score,
        "total": total,
        "percentage": percentage,
        "timestamp": datetime.datetime.now().isoformat(),
        "details": details
    }
    save_score(entry)
    print(Fore.CYAN + f"\nResult saved to {SCORES_FILE}.")
    return entry


# ---- Interactive launcher ----
def main():
    print(Style.BRIGHT + "Welcome to the Advanced Quiz!\n")

    user = input("Enter your name (or nickname): ").strip() or "Anonymous"

    # Difficulty selection
    print("\nChoose difficulty: [1] Easy  [2] Medium  [3] Hard  [4] All")
    diff_choice = input("Select (1-4): ").strip()
    diff_map = {"1": "easy", "2": "medium", "3": "hard", "4": "all"}
    difficulty = diff_map.get(diff_choice, "all")

    # Timed mode?
    tm = input("Enable timed questions? (y/N): ").strip().lower()
    timed = tm == "y"

    per_q_time = 15
    if timed and platform.system() != "Windows":
        tval = input(f"Seconds per question (default {per_q_time}): ").strip()
        if tval.isdigit():
            per_q_time = max(3, int(tval))
    elif timed and platform.system() == "Windows":
        print(Fore.YELLOW + "Timed mode is not supported on Windows reliably. Continuing without timeout.")

    # how many questions
    max_q = len([q for q in QUESTIONS if difficulty == "all" or q["difficulty"] == difficulty])
    nq = input(f"How many questions? (max {max_q}, press Enter for all): ").strip()
    num_q = None
    if nq.isdigit():
        num_q = min(int(nq), max_q)

    # Show previous leaderboard
    lb = input("Show leaderboard before starting? (y/N): ").strip().lower()
    if lb == "y":
        show_leaderboard()

    # Run quiz
    run_quiz(user, difficulty=difficulty, timed=timed and platform.system() != "Windows", per_question_time=per_q_time, num_questions=num_q)

    # After quiz, option to view leaderboard
    view_lb = input("\nView leaderboard now? (y/N): ").strip().lower()
    if view_lb == "y":
        show_leaderboard()

    print("\nThanks for playing! Goodbye.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye.")
        sys.exit(0)