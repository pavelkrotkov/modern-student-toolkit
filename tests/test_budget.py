"""Проверка учебных результатов и понятных ошибок без сторонних библиотек."""

import csv
from decimal import Decimal
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
            for row in rows:
                row["quantity"] = "5" if row["category"] == "materials" else "10"
            with path.open("w", encoding="utf-8", newline="") as target:
                writer = csv.DictWriter(target, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
            self.assertEqual(CALCULATE(path, ""), (6, Decimal("170.00")))
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

    def test_command_and_missing_file_do_not_change_inputs(self):
        original = (MATERIALS / "costs.csv").read_bytes()
        result = subprocess.run(
            [sys.executable, str(MATERIALS / "budget.py"), "costs.csv"],
            cwd=MATERIALS, text=True, capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "Покупок: 5\nИтого: 180.00 евро\n")
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
