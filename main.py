import os

LINE = "Tests pass because they run in a universe where I finished the features; production lives in this one."


def main():
    # Write the single excuse line for the grader.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
