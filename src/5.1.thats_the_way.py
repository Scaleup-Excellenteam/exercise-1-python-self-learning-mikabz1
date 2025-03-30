import os

SUFFIX = "deep"
def thats_the_way(directory_path):
    """Returns a list of all file names starting with a SUFFIX in the given directory."""
    try:
        return [f for f in os.listdir(directory_path) if (os.path.isfile(os.path.join(directory_path, f))and f.startswith(SUFFIX))]
    except FileNotFoundError:
        print("Error: Directory not found.")
        return []
    except PermissionError:
        print("Error: Permission denied.")
        return []



if __name__ == "__main__":
    directory = os.getcwd()
    print(thats_the_way(directory))
