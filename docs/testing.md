# Testing and Verification

The project was verified in the IBM lab through the following checks:

- `extract()` returned ten rows with `Name` and `MC_USD_Billion`.
- `transform()` returned five final columns and the expected conversion for JPMorgan Chase.
- The CSV contained ten rows and five columns without an extra index column.
- The SQLite query returned ten rows from `Largest_banks`.
- Currency-specific queries returned the GBP, EUR, and INR columns.
- `code_log.txt` recorded the ETL stages with timestamps.

## Manual verification commands

```bash
python src/banks_project.py
python -c "import pandas as pd; print(pd.read_csv('Largest_banks_data.csv').head())"
```

For a database check:

```python
import sqlite3
import pandas as pd

connection = sqlite3.connect("Banks.db")
print(pd.read_sql_query("SELECT COUNT(*) FROM Largest_banks", connection))
connection.close()
```

Expected row count: `10`.

