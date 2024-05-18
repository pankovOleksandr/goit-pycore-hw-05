import sys

from pathlib import Path
from datetime import datetime
from collections import Counter

def read_file(file_path: str):
    path = Path(file_path)
    if not path.is_file():
            raise ValueError(f"Path '{path}' is not a file.")

    if not path.exists():
        raise ValueError(f"Provided path '{path}' is not found")

    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip()

def load_logs(file_path: str) -> list:
    logs = []
    for log in read_file(file_path):
        logs.append(parse_log_line(log))
    return logs            

def parse_log_line(line: str) -> dict:
    try: 
        date, time, log_level, *message = line.split()
        message = " ".join(message)

        parsed_log = {
            "date": datetime.strptime(f"{date} {time}", '%Y-%m-%d %H:%M:%S'),
            "log_level": log_level,
            "message": message
        }
        
        return parsed_log
    except(ValueError):
        raise ValueError("Failed to read log")

def count_logs_by_level(logs: list) -> dict:
    counts = Counter(log["log_level"] for log in logs)
    return dict(counts)

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["log_level"] == level]

def display_log_counts(counts: dict):
    log_level_title = "Рівень логування"
    quantity_title = "Кількість"
    separator = " | "
    print(f"{log_level_title}{separator}{quantity_title}")
    print(f"{'-' * len(log_level_title)}{separator}{'-' * len(quantity_title)}")

    for level, count in counts.items():
        print(f"{level:<{len(log_level_title)}}{separator}{count}")


def main():
    if len(sys.argv) < 2:
        raise ValueError("Enter the log file path")

    log_file_path = sys.argv[1]
    log_level = sys.argv[2].upper() if len(sys.argv) == 3 else None

    try:
        logs = load_logs(log_file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if log_level:
            print(f"\nДеталі логів для рівня '{log_level}':")
            for log in filter_logs_by_level(logs, log_level):
                print(f"{log["date"]} - {log["message"]}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()