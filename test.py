def func(x):
    print(x)


def create_handlers(callback):
    handlers = list()
    # for step in range(5):
    #     handlers.append(lambda: callback(step))
    f = lambda x: callback(x)
    for step in range(5):
        handlers.append(f(step))
    # handlers = [f(x) for x in range(5)]
    return handlers


def execute_handlers(handlers):
    for handler in handlers:
        handler()


a = create_handlers(func)
print(a)
# execute_handlers(a)

