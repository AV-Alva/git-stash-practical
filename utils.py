def validate_task(task):
    if task is None:
        return False

    if not isinstance(task, str):
        return False
    
    return bool(task.strip())