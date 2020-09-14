from typing import List
import os


def finder(files: List[str], queries: List[str]) -> List[str]:
    file_paths = {}
    for file in files:
        if os.path.basename(os.path.normpath(file)) in file_paths:
            file_paths[os.path.basename(os.path.normpath(file))].append(file)
        else:
            file_paths[os.path.basename(os.path.normpath(file))] = [file]

    result = []
    for query in queries:
        if query in file_paths:
            result.append(file_paths[query])

    return [el for sub in result for el in sub]


if __name__ == "__main__":
    files = [
        "/usr/local/share/foo.txt",
        "/usr/bin/ls",
        "/home/davidlightman/foo.txt",
        "/bin/su",
    ]
    queries = ["ls", "foo.txt", "nosuchfile.txt"]
    print(finder(files, queries))
