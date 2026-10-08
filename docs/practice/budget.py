import csv
import sys
from decimal import Decimal, InvalidOperation

# Пустая строка означает все категории; попробуй заменить её на "food".
CATEGORY = ""


def calculate(path, category):
    total = Decimal("0")
    count = 0
    with open(path, encoding="utf-8-sig", newline="") as source:
        rows = csv.DictReader(source)
        if rows.fieldnames != ["item", "category", "quantity", "unit_price"]:
            raise ValueError("Ожидаются столбцы item,category,quantity,unit_price")
        for row in rows:
            if None in row or None in row.values():
                raise ValueError("В строке должно быть четыре значения")
            quantity = int(row["quantity"])
            price = Decimal(row["unit_price"])
            if quantity <= 0 or not price.is_finite() or price < 0:
                raise ValueError("Проверь количество и цену: " + row["item"])
            if not category or row["category"] == category:
                total += quantity * price
                count += 1
    if count == 0:
        raise ValueError("Нет покупок для расчёта; проверь файл и категорию")
    return count, total


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Укажи CSV: uv run budget.py costs.csv")
    try:
        count, total = calculate(sys.argv[1], CATEGORY)
    except (OSError, ValueError, TypeError, InvalidOperation) as error:
        sys.exit(f"Не удалось посчитать: {error}")
    print(f"Покупок: {count}")
    print(f"Итого: {total:.2f} евро")
