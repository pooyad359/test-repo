import sys

if __name__ == "__main__":
    previous_version = sys.argv[1]
    current_version = sys.argv[2]
    previous_tuple = tuple(int(i) for i in previous_version.split("."))
    current_tuple = tuple(int(i) for i in current_version.split("."))
    assert current_tuple > previous_tuple
    