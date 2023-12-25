import argparse

from carta import ReMarkable, Widget


def main():
    parser = argparse.ArgumentParser(
        prog="myapp",
        description="Example carta application",
    )
    parser.add_argument(
        "--simple-executable",
        help="Path to the simple application",
        action="store",
        default=None,
        dest="simple",
    )
    args = parser.parse_args()

    rm = ReMarkable(simple=args.simple) if args.simple is not None else ReMarkable()

    rm.eclear()

    button = Widget(
        id="back",
        typ="button",
        value="back",
        justify="left",
        x="0",
        y="0",
    )
    text = Widget(
        id="hello",
        typ="label",
        value="Hello World!",
        x="50%",
        y="50%",
    )
    rm.add(text)
    rm.add(button)

    while True:
        clicked = rm.display()
        if clicked and clicked[0] == button.id:
            print("Quitting...")
            break
