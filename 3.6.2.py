import requests
from pathlib import Path


# function read incoming file, parse it and return first link
def parse_from_file(filename: Path, path: Path) -> str:
    with open(path / filename) as file:
        return file.read().splitlines()[0]


# function write your answer in file
def write_file(filename: Path, path: Path, url: str):
    with open(path / filename, "w") as file:
        file.write(requests.get(url).text)


def main():
    file_first: Path = Path("dataset_3378_3.txt")
    file_path: Path = Path.cwd()  # get current dir
    link_path: str = r"https://stepic.org/media/attachments/course67/3.6.3/"
    next_filename: str = parse_from_file(file_first, file_path).split("/")[-1]
    count: int = 0

    while True:
        r: str = requests.get(link_path + next_filename).text.splitlines()[0]
        if r.split()[0] == "We":
            write_file(Path(next_filename), file_path, link_path + next_filename)
            print(f"File found: {link_path}{next_filename}. Copy the text below or upload {file_path}{next_filename}")
            print(requests.get(link_path + next_filename).text)
            break
        next_filename = r.split("/")[-1]
        count += 1
        print(f"End of {count} iteration. Wait, please.")


if __name__ == '__main__':
    main()
