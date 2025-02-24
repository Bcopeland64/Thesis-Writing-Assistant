# utils/time_management.py

def create_timeline(tasks):
    timeline = []
    for i, task in enumerate(tasks, 1):
        timeline.append(f"Task {i}: {task}")
    return "\n".join(timeline)