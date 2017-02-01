class Cookie:
    counter = 0

    def __init__(self):
        self.counter = Cookie.counter
        Cookie.counter += 1

    @classmethod
    def count(cls):
        return Cookie.counter

    @classmethod
    def reset_counter(cls):
        Cookie.counter = 0
        return Cookie.counter

c1 = Cookie()

print(Cookie.count())