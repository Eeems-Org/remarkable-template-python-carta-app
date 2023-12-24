from carta import ReMarkable, Widget


def main():
    rm = ReMarkable()

    button = Widget(
        id="but1",
        typ="button",
        value="Hello!",
        x="50%",
        y="50%",
    )

    rm.add(button)
    rm.display()
