# 1. todo listekileri gostermek
# 2. todo listde neyise silmek
# 3. todo listde  neyise elave etmek
# 4. whilein icherisinde todo listi ishledirsen, sonsuz dovr olur
todo_list = []


def show_list():
    print(todo_list)


def add_task():
    task_description = input('Enter the task description: ')
    todo_list.append(task_description)
    print('Task is added to your todo list')


def delete_task():
    for i in range(len(todo_list)):
        print(f'{i}. {todo_list[i]}')

    deleted_task_index = int(input('Enter task number to delete: '))
    try:
        del todo_list[deleted_task_index]
    except IndexError:
        print(f'Index {deleted_task_index} does not exist.')


add_task()
add_task()
delete_task()
show_list()
