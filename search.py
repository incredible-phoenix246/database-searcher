import os
import fnmatch


def find_files(directory, pattern):
    """
    Search for files matching a specified pattern in a directory and its subdirectories.

    Args:
    - directory (str): The root directory to start the search.
    - pattern (str): The file pattern to match (e.g., '*.txt' for all text files).

    Returns:
    - List[str]: A list of file paths matching the pattern.
    """
    matching_files = []

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for filename in files:
            if fnmatch.fnmatch(filename, pattern):
                file_path = os.path.join(root, filename)
                matching_files.append(file_path)

    return matching_files


if __name__ == "__main__":
    # Prompt the user for the directory path
    search_directory = input("Enter the directory path to search in: ")

    # Prompt the user for the file pattern (filename)
    file_pattern = input("Enter the file pattern (e.g., '*.txt'): ")

    found_files = find_files(search_directory, file_pattern)

    if found_files:
        print("Found matching files:")
        for file_path in found_files:
            print(file_path)
    else:
        print("No matching files found.")
