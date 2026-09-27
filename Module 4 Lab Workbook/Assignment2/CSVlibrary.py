import csv
class CSVlibrary:
    def read_test_data(self, file_path):
        """Read test cases from an external CSV file."""
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [
                [row["username"], row["password"], row["expected"]]
                for row in reader
            ]