from __future__ import annotations
import os, csv


def init_db(filepath: str) -> None:
    if os.path.exists(filepath):
        print("Error: Database already exists!")
    else:
        file = open(filepath, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "City"])
        file.close()


def add_record(filepath: str, id: int, name: str, age: str, city: str) -> None:
    csv_file = open(filepath, "a", newline="")
    writer = csv.writer(csv_file)
    writer.writerow([id, name, age, city])
    print("Record added!")
    csv_file.close()


def view_records(filepath: str) -> None:
    csv_file = open(filepath, "r", newline="")
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        print(row)
    csv_file.close()


def search_record(filepath: str, search_term: str) -> None:
    csv_file = open(filepath, "r", newline="")
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        if search_term in row:
            print(row)


def delete_record(filepath: str, delete_term: str) -> None:
    csvfile = open(filepath, "r", newline="")
    reader = csv.reader(csvfile)
    header = next(reader)
    rows = [row for row in reader if delete_term not in row]
    csvfile.close()

    new_csv = open(filepath, "w", newline="")
    writer = csv.writer(new_csv)
    writer.writerow(header)
    writer.writerows(rows)
    new_csv.close()
