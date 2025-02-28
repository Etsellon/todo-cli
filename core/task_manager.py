from datetime import datetime, timezone

from utils import *

mark_status = ['done', 'in-progress', 'todo']


def add(task: str):
    if not task:
        print("Error: Task description cannot be empty")
        return
    tasks = load_tasks()
    current_id = max(task['id'] for task in tasks) + 1 if tasks else 1
    new_task = ({'id': current_id,
                 'name': task,
                 'progress_state': 'todo',
                 'created_at': datetime.now(timezone.utc).strftime('%H:%M:%S %d.%m.%Y'),
                 'updated_at': datetime.now(timezone.utc).strftime('%H:%M:%S %d.%m.%Y')
                 })
    tasks.append(new_task)
    save_tasks(tasks)


def update(id: int, new_name: str):
    tasks = load_tasks()

    if not tasks:
        print('no tasks')
        return

    task_to_update = next((task for task in tasks if task['id'] == id), None)
    if task_to_update:
        task_to_update['name'] = new_name
        save_tasks(tasks)
        print(f'Task with ID {id} updated successfully')
        return

    print(f'Task with ID {id} not found')


def delete(id: int):
    tasks = load_tasks()

    if not tasks:
        print('no tasks')
        return

    task_to_delete = next((task for task in tasks if task['id'] == id), None)
    if task_to_delete:
        tasks.remove(task_to_delete)
        save_tasks(tasks)
        print(f'Task with ID {id} deleted successfully')
    else:
        print(f'Task with ID {id} not found')


def mark_in_progress(id: int):
    mark_task(id, mark_status[1])


def mark_done(id: int):
    mark_task(id, mark_status[0])


def task_list(status: str | None = None):
    tasks = load_tasks()

    if not tasks:
        print('no tasks')
        return

    if status is None:
        print_tasks(tasks)
        return

    current_tasks = [task for task in tasks if task['progress_state'] == status]
    print_tasks(current_tasks)


def print_tasks(tasks: list[dict]):
    for task in tasks:
        print(f'{task['id']}. {task['name']} - {task['progress_state']} - {task['created_at']} - {task['updated_at']}')


def mark_task(id: int, status: str):
    tasks = load_tasks()

    if not tasks:
        print('no tasks')
        return

    task_to_mark = next((task for task in tasks if task['id'] == id), None)

    if task_to_mark:
        if status in mark_status:
            task_to_mark['progress_state'] = status
            save_tasks(tasks)
            print(f'Task with ID {id} marked {status} successfully')
        else:
            print(f'Invalid status: {status}')
    else:
        print(f'Task with ID {id} not found')
