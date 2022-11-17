import sys

class VersionError(Exception):
    pass

if __name__ == "__main__":
    previous_version = sys.argv[1]
    current_version = sys.argv[2]
    previous_tuple = tuple(int(i) for i in previous_version.split("."))
    current_tuple = tuple(int(i) for i in current_version.split("."))
    if not current_tuple > previous_tuple:
        raise VersionError(f"Current version (`{current_version}`) must be greater than old version (`{previous_version}`)")
