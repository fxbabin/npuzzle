from npuzzle import NPuzzle
from setting import Setting


def main():
    setting = Setting()
    npuzzle = NPuzzle(setting)
    npuzzle.report()

if __name__ == "__main__":
    main()
