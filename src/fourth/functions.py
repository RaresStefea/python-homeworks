from __future__ import annotations
import re


def file_copy(file_path_og: str, file_path_copy) -> None:
    file_to_read = open(file_path_og, "r")
    file_to_copy = open(file_path_copy, "w")

    content = file_to_read.read()
    file_to_read.close()

    file_to_copy.write(content)

    file_to_copy.close()


def word_count(file_path: str) -> None:
    file_to_read = open(file_path, "r")

    final_sum = 0
    for line in file_to_read:
        splitted_line = [
            word for word in re.split(r"[,;\s?.!\n]+", line.strip()) if word != ""
        ]
        final_sum += len(splitted_line)

    print(f"Your file's word count is {final_sum}.")

    file_to_read.close()
