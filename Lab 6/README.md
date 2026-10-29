# L6_L7_24_pizza_order — Pizza Order

## Lab 6: Code and Branch Coverage

The completed test suite covers all three functions without changing the supplied application logic.

### Run

From this folder:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

If Python uses the Windows launcher, replace `python` with `py`.

The pytest configuration measures branch coverage, generates reports, and fails below 100%.

### Verified results

- 37 tests passed.
- 34 of 34 executable statements covered (100%).
- 24 of 24 branch outcomes covered (100%).
- No missing statements or partial branches.
- Verified with Python 3.13.14, pytest 9.2.0, pytest-cov 7.1.0, and coverage 7.17.0.

| Function | Cases covered |
| --- | --- |
| `pizza_price` | All sizes; zero, one, three, four, and five toppings; cheese burst for medium/large; unknown size, negative toppings, and small cheese-burst errors |
| `order_discount` | Below/at the 300 threshold; Tuesday; both weekend days; other weekdays; students/non-students; integer rounding |
| `delivery_status` | On time, late, free pizza; 30/31 and 45/46 minute boundaries; distance 10/10.1 km; distance rejection takes precedence |

### Reports

- `test_results.txt`: captured test execution output.
- `coverage.json`: machine-readable statement and branch evidence.
- `htmlcov/index.html`: open in a browser to inspect covered lines.

Coverage measures execution of the supplied code. The tests check its existing rules; they do not add requirements for inputs such as negative delivery times.

The repository contains only Lab 6 material. No separate Lab 7 handout or implementation was present.
