import re

from decimal import Decimal
from typing import Callable, Generator

def generator_numbers(text: str):
    for word in text.split():
        if re.match(r"\d+\.\d+", word):
            yield Decimal(word)

def sum_profit(text: str, func: Callable):
    total = 0
    for income in func(text):
        total += income
    return total        

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 i 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == "__main__":
    main()