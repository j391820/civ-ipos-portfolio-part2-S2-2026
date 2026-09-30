from pick import pick


title = 'Task Manager CLI'
choices = ['Add Task', 'Delete Task', 'List Tasks', 'Exit']
test = pick(choices)
print(test)