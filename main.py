from npuzzle import NPuzzle
from setting import Setting
from graphic import Graphic


def main():
    setting = Setting()
    npuzzle = NPuzzle(setting)
    if setting.graphic:
        Graphic(npuzzle)
    else:
        npuzzle.report()

if __name__ == "__main__":
    main()
