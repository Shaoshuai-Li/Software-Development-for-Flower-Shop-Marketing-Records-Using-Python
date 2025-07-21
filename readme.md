# SDPA / SEMTM0024 – Coursework Repository  
*Author : **Shaoshuai Li***  
*UoB User: **bf24104***  
*Module  : Software Development – Programming and Algorithms*  
*GitHub repository:**https://github.com/Shaoshuai-Li/bf24104_SEMTM0024.git***
---

## 1 FlowerShop Simulator-Part 1 

### Project Description

FlowerShop Simulator is a text-based, object-oriented simulation of a flower shop that manages bouquet sales, employee scheduling, greenhouse inventory, and finances. The goal is to maximize profit and avoid bankruptcy by making strategic decisions each month.

The program allows users (the shop owner) to:
- Hire/fire florists (with optional bouquet specialities)
- Decide how many bouquets of each type to produce/sell
- Purchase supplies from different vendors at varying prices
- Track income, expenses, and greenhouse stock
- React to realistic business constraints (labour, supply, demand)

---

## Code Design


#### Structure

| File         | Description                                                                                              |
|--------------|----------------------------------------------------------------------------------------------------------|
| main.py      | Main entry point; handles user interaction and monthly simulation loop                                   |
| bouquet.py   | Contains the Bouquet class, defines bouquet types and requirements                                       |
| florist.py   | Contains the Florist class (employee data, and florists who specialise in a particular type of bouquet.) |
| vendor.py    | Contains the Vendor class (supplier prices, info display)                                                |
| flowershop.py| FlowerShop class; handles inventory, cash, employee management, logic                                    |

## Key Classes & Methods

### 1. `bouquet.py` — Bouquet Types and Requirements

**Class`Bouquet`**

* **types** — *Static* dict defining each bouquet’s requirements –greenery, roses, daisies, prep‑time (min), price and monthly demand.

---

### 2. `florist.py` — Florist Management

**Class`Florist`**

**Attributes**

* **name** — Unique florist name (English letters only).
* **speciality** *(optional)* — Bouquet type this florist specialises in.

**Methods**

* **`__repr__()`** — Readable string showing the florist’s name and, if applicable, their speciality.

---

### 3. `vendor.py` — Supply Vendors

**Class`Vendor`**

* **vendor\_prices** — *Static* dict of supplier prices for each ingredient.

**Methods**

* **`show_prices()`** — Prints a neatly formatted price list when the user enters `i` at the restock prompt.

---

### 4. `flowershop.py` — Shop Management

**Class`FlowerShop`**

**Persistent state**

* **cash** — Starts at £ 7500 and changes constantly.
* **inventory** — Bunch counts for Roses, Daisies and Greenery.
* **florists** — List of live `Florist` objects.

**Key services**

* **Staffing** — `add_florist()`, `remove_florist()`.
* **Finance** — `pay_florists()`, `pay_rent()`, `pay_storage_costs()`.
* **Inventory life‑cycle** — `depreciate_inventory()`, `restock()`.
* **Sales** — `calculate_income()`, `fulfill_orders()`.
* **Labour feasibility** — `can_fulfill_orders_with_specialists()` — minute‑by‑minute allocation that gives each specialist a ½‑time advantage, returning `True`/`False` so `main.py` can stop the user before overselling.

All cost‑deduction methods raise **`RuntimeError`** if cash would go negative; `main.py` traps this to declare bankruptcy and end the game.

---

### 5. `main.py` — User Interface & Simulation Driver

* Manages the full month‑by‑month loop:

  1. Hire / fire florists (ensuring at least one remains).
  2. Collect bouquet sales targets; validate demand, inventory and labour capacity.
  3. Apply income; pay wages, rent and storage.
  4. Depreciate leftover stock.
  5. Offer restocking with per‑ingredient vendor choice (type **`i`** to view prices).
  6. Print a summary and repeat for the chosen number of months or until cash < 0.

* Helper **`input_int()`** enforces numeric safety, politely re‑prompting on any invalid entry throughout the process.

---

### Design Choices

- Each main business concept (Bouquet, Florist, Vendor, Shop) is an independent class in its own file, improving readability and maintainability.
- Extension: Florists can have a bouquet speciality, affecting production time and labour allocation.
- All user interaction and validation is handled in `main.py`, keeping business logic separate.

---

## User Instructions

- **Run**: `python main.py`
- At the start, enter the number of months to simulate (default: 6).
- Each month, decide how many florists to hire/fire, input their (unique, English) names, and assign (optionally) their bouquet speciality.
When entering the florist's speciality, if they have one, please enter the full name of the bouquet they specialise in (e.g. Fern-tastic); if they do not have a speciality, leave the field blank and press Enter.
- Enter bouquet sales for each type (respecting demand, labour, and supply constraints).
- Purchase supplies from vendors to restock inventory after each month.
The supply options indicate the corresponding number of each supplier as 0 or 1. For each type of material(roses, daisies, greenery), entering 0 or 1 means selecting a specific supplier to purchase material . Entering i displays the supplier's price, which helps users choose the most cost-effective supplier.
- Simulation ends upon bankruptcy or after the specified months.

### Input Validation & Error Handling

- All user input is validated:  
  - Only English letters for names; no duplicates allowed.
  - Only integers for counts; out-of-range entries are rejected with friendly prompts.
  - Supply choices must be 0 or 1, or 'i' to display vendor prices.
- Program will **not crash** on invalid input, but will re-prompt the user.


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
