class Task:
    def __init__(self, description, priority='None', deadline=None):
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def __str__(self):
        status = 'DONE' if self.completed else 'TODO'
        due_str = f" Due: {self.due}" if self.due else ''
        return f"[{status}] {self.description} - Priority: {self.priority} - Deadline: {self.deadline}"

    def mark_done(self):
        self.completed = True

    def set_due(self, deadline):
        self.deadline = deadline

    def set_priority(self, priority):
        self.priority = priority
    