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

## Team Members

- William Jijon
- Shahla T Meem
- Sahithi Attada
- Kaley Santoncito
- Imandi Kathriarachchi
