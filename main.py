import argparse

from core import *


def createParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='Task CLI',
        description='A program for managing tasks inside the CLI',
        epilog='Created by Etsellon'
    )
    subparsers = parser.add_subparsers(dest='command',
                                       help='Available commands')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task', type=str, help='Task description to add')

    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('task_id', type=int, help='ID of the task to update')
    update_parser.add_argument('new_task', type=str, help='New task description')

    delete_parser = subparsers.add_parser('delete', help='Delete an existing task')
    delete_parser.add_argument('task_id', type=int, help='ID of the task to delete')

    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark task in progress')
    mark_in_progress_parser.add_argument('task_id', type=int, help='ID of the task to mark in progress')

    mark_done_parser = subparsers.add_parser('mark-done', help='Mark task in done')
    mark_done_parser.add_argument('task_id', type=int, help='ID of the task to mark done')

    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', nargs='?', choices=['done', 'todo', 'in-progress'],
                             help='Filter tasks by status (done, todo, in-progress)')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    if namespace.command == 'add':
        add(namespace.task)

    if namespace.command == 'update':
        update(namespace.task_id, namespace.new_task)

    if namespace.command == 'delete':
        delete(namespace.task_id)

    if namespace.command == 'mark-in-progress':
        mark_in_progress(namespace.task_id)

    if namespace.command == 'mark-done':
        mark_done(namespace.task_id)

    if namespace.command == 'list':
        task_list(namespace.status)
