import os


def ft_progress(lst):
    length = len(lst)
    for i, elem in enumerate(lst):
        os.system('clear')
        progress = (i + 1) * 100 // length
        print("[{:3}%]".format(progress), end=' ')
        print("[{:25}]".format("=" * (24 * progress // 100) + ">"), end=' ')
        print(f"{i + 1}/{length}")
        yield elem
