# Data Lineage

```text
Archived Wikipedia table
        |
        v
extract()
        |
        v
Name + MC_USD_Billion
        |
        +-------------------- Exchange-rate CSV
        |                              |
        v                              v
                 transform()
                        |
                        v
Name + USD + GBP + EUR + INR
             |                 |
             v                 v
      Largest_banks_data.csv  Banks.db/Largest_banks
                                      |
                                      v
                              run_query()
```

## Transformations

1. The first table on the archived page is selected.
2. The bank name is extracted from the second table cell.
3. Market capitalization text is cleaned by removing commas and the dollar symbol.
4. The cleaned value is converted to `float`.
5. The USD value is multiplied by each exchange rate and rounded to two decimals.

