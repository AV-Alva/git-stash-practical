tasks = []


def add_task(task, priority="Medium"):
    tasks.append({
        "task": task,
        "priority": priority
    })

    print(f"Task added: {task} | Priority: {priority}")


def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nTask List")

    for index, task in enumerate(tasks, start=1):
        print(
            f"{index}. {task['task']} "
            f"[Priority: {task['priority']}]"
        )