# SDPA / SEMTM0024 – Coursework Repository  
*Author : **Shaoshuai Li***  
*UoB User: **bf24104***  
*Module  : Software Development – Programming and Algorithms*  
*GitHub repository:**https://github.com/Shaoshuai-Li/bf24104_SEMTM0024.git***
---

## 0 Repository Structure
???
---

## 2.1 Overview of Part 2

The notebook **`Part2.ipynb`** demonstrates an end‑to‑end data‑science pipeline that answers the question  
> *“What factors drive user engagement (number of comments) on r/technology posts?”*

It follows precisely the five steps set out in the coursework brief:

| Step | Brief description                                                                                                                                                                                                                            | Where?          |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| 1 | **Data scraping** – 200 hot posts from r/technology collected via Reddit API (`praw`). Saved as `reddit_technology_posts.csv`.                                                                                                               | Notebook Step 1 |
| 2 | **Data preparation & cleaning** – Handles missing `selftext`, removes negative scores, parses `created_utc`, engineers `hour`, `weekday`, `text_length`. Each action explained in markdown.                                                  | Notebook Step 2 |
| 3 | **Exploratory analysis** – Prints descriptive stats & plots histograms, scatter plots, time‑of‑day and weekday charts – each with interpretation.                                                                                            | Notebook Step 3 |
| 4 | **Complex question** – Main question plus 4 sub‑questions (timing, score‑comments, post‑type, regression). Includes correlation (r = 0.76), bar/line charts and a multiple linear‑regression (R² = 0.58). All graphs labelled and explained. | Notebook Step 4 |
| 5 | **Summary & conclusion** – Summarises five key findings and proposes future‑work directions (larger dataset, richer features, ensemble models).                                                                                                                                                                      | Notebook Step 5 |

All code cells contain **docstrings** and inline comments; every step is accompanied by a markdown interpretation as required.


---

## 2.2 Quick Start

### Set‑up

```bash
git clone https://github.com/Shaoshuai-Li/bf24104_SEMTM0024.git
cd bf24104_SEMTM0024

python -m venv .venv
.venv\Scripts\activate # Windows

pip install pandas numpy matplotlib scikit-learn praw
