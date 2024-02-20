import os


def get_abs_path(rel_path='data/svg/gaussian_blur.svg'):

    abs_path = os.path.abspath(rel_path)

    print(abs_path)

    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"The file {abs_path} does not exist.")

    return abs_path
