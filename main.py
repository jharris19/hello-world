import os


def hello(name):
    print(f"hello, {name}!")


if __name__ == '__main__':
    hello(os.getenv('HELLO_NAME', 'pyCharm'))
