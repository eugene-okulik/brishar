from time import sleep
from datetime import datetime


def main():
    print("Hello from your Docker container!")

    # Выводим текущее время
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {current_time}")

    # Задержка на 5 секунд
    print("Waiting for 5 seconds...")
    sleep(5)

    print("Program finished. Goodbye!")


if __name__ == "__main__":
    main()
