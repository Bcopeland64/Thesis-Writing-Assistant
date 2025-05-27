# utils/time_management.py
import matplotlib.pyplot as plt

def create_timeline(tasks):
    if not tasks or all(not task.strip() for task in tasks):
        raise ValueError("Tasks cannot be empty.")
    timeline = []
    total_days = 0
    for i, task in enumerate(tasks, 1):
        duration = len(task.split()) * 2  # Example heuristic: 2 days per word in task
        priority = "High" if "urgent" in task.lower() else "Medium"
        timeline.append(f"Task {i}: {task} (Duration: {duration} days, Priority: {priority})")
        total_days += duration
    return "\n".join(timeline), total_days

def visualize_timeline(tasks):
    if not tasks or all(not task.strip() for task in tasks):
        raise ValueError("Tasks cannot be empty.")
    durations = [len(task.split()) * 2 for task in tasks]
    priorities = ["High" if "urgent" in task.lower() else "Medium" for task in tasks]
    colors = ["red" if p == "High" else "skyblue" for p in priorities]
    plt.figure(figsize=(10, 6))
    plt.barh(tasks, durations, color=colors)
    plt.xlabel("Duration (Days)")
    plt.title("Thesis Timeline")
    plt.savefig("timeline.png")
    return "timeline.png"