from insta_clone.celery import app


@app.task(name='sum_two_numbers')  # we can have request, the task will have info about current request
# max_retries, it  helps retry the task, using self.retry etc.
def add(x, y):
    print("On line 6")
    return x+y
