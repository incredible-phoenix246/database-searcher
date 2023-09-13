# File Search Script

This Python script allows you to search for files in a directory and its subdirectories based on a specified file pattern.

## Usage

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
Navigate to the Script Directory

Use the cd command to move into the directory where the script is located:

bash
Copy code
cd your-repo
Run the Script

Run the script by executing the following command:

bash
Copy code
python file_search.py
Enter Directory and File Pattern

The script will prompt you to enter the directory path and the file pattern (filename) you want to search for. For example:

javascript
Copy code
Enter the directory path to search in: /path/to/your/directory
Enter the file pattern (e.g., '*.txt'): *.txt
Directory Path: Enter the full path to the directory where you want to start the search. You can use both relative and absolute paths.
File Pattern: Specify the file pattern (e.g., *.txt for all text files). The script will search for files that match this pattern.
View Search Results

The script will display a list of file paths that match the specified file pattern within the chosen directory and its subdirectories.

Exit the Script

To exit the script, press Ctrl+C or follow the on-screen instructions.

Example
Here's an example of how to use the script:

bash
Copy code
Enter the directory path to search in: /path/to/your/directory
Enter the file pattern (e.g., '*.txt'): *.txt

Found matching files:
/path/to/your/directory/file1.txt
/path/to/your/directory/subdirectory/file2.txt
/path/to/your/directory/another_subdir/file3.txt
