"""Проверка учебных результатов и понятных ошибок без сторонних библиотек."""

import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
MATERIALS = ROOT / "docs" / "practice"
CALCULATE = runpy.run_path(str(MATERIALS / "budget.py"))["calculate"]


class BudgetTests(unittest.TestCase):
    def test_lesson_totals(self):
        for filename, category, count, total in [
            ("costs.csv", "", 5, "180.00"),
            ("costs.csv", "food", 2, "21.00"),
            ("costs-extra.csv", "", 6, "204.00"),
            ("costs-extra.csv", "food", 3, "45.00"),
        ]:
            with self.subTest(filename=filename, category=category):
                self.assertEqual(
                    CALCULATE(MATERIALS / filename, category),
                    (count, Decimal(total)),
                )

    def test_capstone_and_invalid_input(self):
        cache = ROOT / ".cache"
        cache.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache) as folder:
            path = Path(folder) / "exercise.csv"
            with (MATERIALS / "costs-extra.csv").open(encoding="utf-8") as source:
                reader = csv.DictReader(source)
                rows = list(reader)
                fields = reader.fieldnames
            for participants, notebooks, total in [(10, 5, "170.00"), (11, 6, "188.25")]:
                with self.subTest(participants=participants):
                    for row in rows:
                        row["quantity"] = str(
                            notebooks if row["category"] == "materials" else participants
                        )
                    with path.open("w", encoding="utf-8", newline="") as target:
                        writer = csv.DictWriter(target, fieldnames=fields)
                        writer.writeheader()
                        writer.writerows(rows)
                    self.assertEqual(CALCULATE(path, ""), (6, Decimal(total)))
            for content in [
                "wrong,header\n1,2\n",
                "item,category,quantity,unit_price\n",
                "item,category,quantity,unit_price\nx,food,0,1\n",
                "item,category,quantity,unit_price\nx,food,1,-2\n",
                "item,category,quantity,unit_price\nx,food,1,NaN\n",
                "item,category,quantity,unit_price\nx,food,1\n",
                "item,category,quantity,unit_price\nx,food,1,2,extra\n",
            ]:
                with self.subTest(content=content):
                    path.write_text(content, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        CALCULATE(path, "")
        with self.assertRaises(ValueError):
            CALCULATE(MATERIALS / "costs.csv", "unknown-category")

    def test_messy_data_can_be_reconciled_to_source(self):
        with (MATERIALS / "costs-messy.csv").open(encoding="utf-8") as source:
            rows = list(csv.DictReader(source))
        self.assertEqual(len(rows), 6)
        self.assertEqual(rows[1], rows[5])  # Повтор музея.
        self.assertEqual(rows[2]["unit_price"], "2.50 EUR")
        self.assertEqual(rows[3]["quantity"], "")
        self.assertEqual(rows[4]["category"], "Food")
        with self.assertRaises(InvalidOperation):
            CALCULATE(MATERIALS / "costs-messy.csv", "")
        result = subprocess.run(
            [sys.executable, str(MATERIALS / "budget.py"), "costs-messy.csv"],
            cwd=MATERIALS, text=True, capture_output=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Не удалось посчитать", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

        corrected = rows[:5]
        corrected[2]["unit_price"] = "2.50"
        corrected[3]["quantity"] = "12"
        corrected[4]["category"] = "food"
        with (MATERIALS / "costs.csv").open(encoding="utf-8") as source:
            self.assertEqual(corrected, list(csv.DictReader(source)))

    def test_delayed_task_checks_quantity_as_well_as_cost(self):
        with (MATERIALS / "print-order.csv").open(encoding="utf-8") as source:
            rows = list(csv.DictReader(source))
        quantities = [int(row["packs"]) * int(row["units_per_pack"]) for row in rows]
        self.assertEqual(quantities, [150, 40])
        cost = sum(Decimal(row["packs"]) * Decimal(row["price_per_pack_eur"]) for row in rows)
        self.assertEqual(cost + Decimal("4.80"), Decimal("38.00"))
        self.assertLess(quantities[0], 200)  # Дешёвый черновик не выполняет условие.
        self.assertGreaterEqual(quantities[1], 36)

        requirements = [200, 36]
        packs = [
            (required + int(row["units_per_pack"]) - 1) // int(row["units_per_pack"])
            for required, row in zip(requirements, rows)
        ]
        self.assertEqual(packs, [4, 4])
        corrected = sum(count * Decimal(row["price_per_pack_eur"]) for count, row in zip(packs, rows))
        self.assertEqual(corrected + Decimal("4.80"), Decimal("44.40"))
        self.assertEqual(Decimal("45.00") - corrected - Decimal("4.80"), Decimal("0.60"))
        self.assertEqual(corrected + Decimal("4.80") + Decimal(rows[0]["price_per_pack_eur"]), Decimal("50.80"))
        with self.assertRaises(ValueError):
            CALCULATE(MATERIALS / "print-order.csv", "")

    def test_command_and_missing_file_do_not_change_inputs(self):
        original = (MATERIALS / "costs.csv").read_bytes()
        result = subprocess.run(
            [sys.executable, str(MATERIALS / "budget.py"), "costs.csv"],
            cwd=MATERIALS, text=True, capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "Строк расходов: 5\nИтого: 180.00 евро\n")
        self.assertEqual((MATERIALS / "costs.csv").read_bytes(), original)
        missing = subprocess.run(
            [sys.executable, str(MATERIALS / "budget.py"), "missing.csv"],
            cwd=MATERIALS, text=True, capture_output=True,
        )
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("Не удалось посчитать", missing.stderr)
        self.assertNotIn("Traceback", missing.stderr)


if __name__ == "__main__":
    unittest.main()
