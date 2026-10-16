# Data Dictionary

## Final table: `Largest_banks`

| Column | Type | Description | Example |
|---|---|---|---|
| `Name` | text | Name of the bank. | `JPMorgan Chase` |
| `MC_USD_Billion` | real | Market capitalization in billions of US dollars. | `432.92` |
| `MC_GBP_Billion` | real | Market capitalization converted to billions of British pounds. | `346.34` |
| `MC_EUR_Billion` | real | Market capitalization converted to billions of euros. | `402.62` |
| `MC_INR_Billion` | real | Market capitalization converted to billions of Indian rupees. | `35910.71` |

## Exchange-rate input

| Column | Description |
|---|---|
| `Currency` | Currency code used to identify the exchange rate. |
| `Rate` | Value used to convert the USD market capitalization into the selected currency. |

The input rates used by the project are GBP `0.80`, EUR `0.93`, and INR `82.95`.

