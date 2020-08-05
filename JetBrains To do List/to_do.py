from datetime import datetime, timedelta

from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# creating a database file NOTE: check_same_thread=False allows for connecting to the
# database from another thread
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default="default_value")
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


# Creates the table in the database according to the columns above
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class ToDoFunctions:
    def __init__(self):
        self.prompt = (
            "1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit\n")
        self.today = datetime.today()

    def today_task(self):
        # Returns the current date in "Today %b %d: TODAY TASK"
        print(f"Today {self.today.strftime('%b')} {self.today.day}:")
        rows = session.query(Table).filter(
            Table.deadline == datetime.today().date()).all()
        if rows:
            for row in rows:
                print(f"{row.id}. {row.task}")
        else:
            print("Nothing to do!\n")
        print("\n")

    def week_task(self):
        # Needs to print all tasks from 7 days from today
        for x in range(8):
            count = 1
            day_of_week = self.today + timedelta(x)
            day_of_week_task = session.query(Table).filter(
                Table.deadline == day_of_week.date()).order_by(Table.deadline).all()
            print(
                f"{day_of_week.strftime('%A')} {day_of_week.strftime('%b')} {day_of_week.day}:")
            if day_of_week_task:
                for task in day_of_week_task:
                    print(f"{count}. {task}")
                    count += 1
            else:
                print("Nothing to do")
            print('\n')

    def all_task(self):
        # Prints all tasks sorted by deadline
        print("\nAll tasks:")
        all_tasks = session.query(Table).order_by(Table.deadline).all()
        count = 1
        for task in all_tasks:
            print(
                f"{count}. {task}. {task.deadline.day} {task.deadline.strftime('%b')}")
            count += 1
        print('\n')

    def missed_task(self):
        # Filters out all tasks past the current date and lists them
        missed_tasks = session.query(Table).filter(
            Table.deadline < self.today.date()).all()
        count = 1
        if missed_tasks:
            print("Missed tasks:")
            for task in missed_tasks:
                print(
                    f"{count}. {task} {task.deadline.day} {task.deadline.strftime('%b')}")
                count += 1
        else:
            print("Nothing is missed!")
        print("\n")

    def add_task(self):
        new_input = input("What task would you like to add?")
        new_deadline = input("Enter deadline (YYYY-MM-DD): ")
        new_row = Table(task=new_input,
                        deadline=datetime.strptime(
                            new_deadline, '%Y-%m-%d').date()
                        )
        session.add(new_row)
        session.commit()
        print("The task has been added!")

    def delete_task(self):
        list_tasks = session.query(Table).order_by(Table.deadline).all()
        print("Choose the number of the task you want to delete:")
        count = 1
        for task in list_tasks:
            print(
                f"{count}. {task} {task.deadline.day} {task.deadline.strftime('%b')}")
            count += 1
        user_input = input()
        specific_task = list_tasks[int(user_input) - 1]
        session.delete(specific_task)
        print("Deleted the task!")
        session.commit()


todo = ToDoFunctions()

while True:
    choice = input(todo.prompt)

    if choice == '1':  # Today's Task
        todo.today_task()

    if choice == '2':  # Week's tasks
        todo.week_task()

    if choice == '3':  # All tasks
        todo.all_task()

    if choice == '4':  # Missed task
        todo.missed_task()

    if choice == '5':  # Add task
        todo.add_task()

    if choice == '6':  # Delete task
        todo.delete_task()

    if choice == '0':  # Exit
        print("Bye!")
        break
