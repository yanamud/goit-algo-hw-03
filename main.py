import argparse
from pathlib import Path
import shutil


def parse_argv():
    parser = argparse.ArgumentParser(description='Копіювання файлів до нової директорії')
    parser.add_argument('-s','--sourse', type = Path, required = True, help = 'Папка з вихідними даними')
    parser.add_argument('-o','--output', type = Path, default = 'dist', help = 'Папка для копіювання')
    return parser.parse_args()


def recursiv_copy(sourse: Path, output: Path):
    for el in sourse.iterdir():
        try:
            if el.is_dir():
                recursiv_copy(el, output)
            else:
                el_split = el.name.split('.')
                folder = el_split[-1]
                folder = output / folder
                folder.mkdir(exist_ok = True, parents = True)
                shutil.copy(el, folder)
        except PermissionError:
            pass

def main():
    args = parse_argv()
    recursiv_copy(args.sourse, args.output)
    print(args)

if __name__ == '__main__':
    main()