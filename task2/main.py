import csv
import statistics
from pathlib import Path

if __name__ == "__main__":
    file_path = Path(__file__).parent / "file.csv"
    with open(file_path, mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        ages = [float(r.get("age")) for r in reader]

    print(statistics.median(ages))
