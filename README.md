# Song Duration Analysis

## Overview

This project investigates how the average duration of the top 20 US songs changed by decade, from the 1970s through the 2020s.

## Data Sources

- [MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page) for the Billboard Year-End Hot 100 rankings from Wikipedia's "Billboard Year-End Hot 100 singles of YYYY" pages ([usage etiquette](https://www.mediawiki.org/wiki/API:Etiquette)). Wikipedia text is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- [iTunes Search API](https://performance-partners.apple.com/search-api) for track durations.

## Setup

Requires Python 3.12. With [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Or with pip:

```bash
pip install -r requirements.txt
```

## Running

Run the notebooks in the `notebooks/` folder in numbered order (`01_...`, `02_...`, etc.). Launch Jupyter from the project root:

```bash
uv run jupyter notebook
```

## Project Structure

```
data/raw/         Raw data as collected (never modified)
data/processed/   Cleaned and transformed data
notebooks/        Analysis notebooks, run in numbered order
docs/             Project documentation
poster/           Poster materials
```

## Summary Statistics

Song duration by decade, in minutes (110 songs after cleaning):

| Decade | Count | Average | Median | Shortest | Longest | Range |
|--------|-------|---------|--------|----------|---------|-------|
| 1970s  | 20    | 4.14    | 3.85   | 2.99     | 5.90    | 2.91  |
| 1980s  | 20    | 4.08    | 4.00   | 3.02     | 5.90    | 2.88  |
| 1990s  | 19    | 4.44    | 4.33   | 3.19     | 6.57    | 3.38  |
| 2000s  | 19    | 3.85    | 3.80   | 3.10     | 4.92    | 1.82  |
| 2010s  | 20    | 3.82    | 3.89   | 2.62     | 4.69    | 2.07  |
| 2020s  | 12    | 3.33    | 3.37   | 2.73     | 4.19    | 1.46  |

## Team Members

- William Jijon
- Shahla T Meem
- Sahithi Attada
- Kaley Santoncito
- Imandi Kathriarachchi
