tasks = []

def add(tasks):
	tasks.append(task)
	print(f"Added: {task}")

def show():
	for i, t in enumerate(tasks, 1):
		print(i, t)

if _name_ == "_main_":
	add("Learn Git")
	show()
