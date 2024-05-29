# Задание №2

# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция

def repeat_me(func):
    def wrapper(*args, count=1, **kwargs):
        for _ in range(count):
            func(*args, **kwargs)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
