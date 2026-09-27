import csv
from pathlib import Path
from framework.config_reader import PROJECT_ROOT

class CSVDataReader:
    @staticmethod
    def read_rows(filename):
        path = PROJECT_ROOT / "testdata" / filename
        with path.open(mode="r", newline="", encoding="utf-8-sig") as csv_file:
            return list(csv.DictReader(csv_file))

    @staticmethod
    def read_column(filename, column):
        return [row[column] for row in CSVDataReader.read_rows(filename)]
