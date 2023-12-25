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

    button = Widget(
        id="but1",
        typ="button",
        value="Hello!",
        x="50%",
        y="50%",
    )

    rm.add(button)
    rm.display()
