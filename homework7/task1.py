import sys


def my_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    str_args = [str(arg) for arg in args]
    output = sep.join(str_args)
    output += end
    file.write(output)
    if flush:
        file.flush()


print('Hello, world!')

if __name__ == '__main__':
    my_print('Hello, world!')
