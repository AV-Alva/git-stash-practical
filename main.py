from task_manager import add_task, display_tasks


def main():
    print("=== Employee Task Manager ===")

    add_task("Prepare project report")
    add_task("Attend team meeting")

    display_tasks()


if __name__ == "__main__":
    main()