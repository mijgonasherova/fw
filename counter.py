class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.count == 0:
            raise Exception("Counter was not used correctly.")


with Counter() as count:
    count.add()
