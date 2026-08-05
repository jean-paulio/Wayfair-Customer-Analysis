# E-Commerce Customer Segmentation Sandbox

## 💬 Introduction
In modern e-commerce, top-line growth is heavily dictated by the critical unit economic ratio of Customer Lifetime Value (LTV) to Customer Acquisition Cost (CAC). Any business knows acquiring new customers significantly costs more than retaining an existing one. Thus, optimizing customer retention is paramount to retaining efficient profitability.

Despite this, many retail brands still rely on a flat, "spray-and-pray" marketing approach where all they run discount campaigns across their whole consumer base. This approach isn't tailored to the individual customer at all, which causes the following:
- **Margin Erosion**: Giving unnecessary discounts to top-tier buyers who would have paid full price.
- **Ad Fatigue & Churn**: Spamming new or occasional buyers with irrelevant, high-frequency messaging, driving unsubscribes.
- **Inefficient Capital Allocation**: Wasting high-cost paid advertising dollars on cold, inactive customer segments.

In order to solve this, I will be segmenting a customer base in order to understand their behavior and tailor our advertising accordingly. **This will be done via the implementation of an automated RFM segmentation pipeline to classify customers into distinct behavioral cohorts.** This allows a business to surgically target audiences with tailored marketing playbooks, preserving margin where possible and deploying high-incentive retention offers precisely where they are needed most.

## 📦 Sandbox
The company of choice for this project will be **Wayfair**. This project includes data scraping the company's product inventory, just with one caveat. In a live corporate setting, customer transaction histories contain highly sensitive, proprietary data protected by strict global privacy regulations like GDPR and CCPA.

To solve this constraint, this project is architected as an enterprise-grade staging sandbox.
- Real-World Anchor: We utilize web scraping to ingest authentic product inventory and pricing structures from the active retail platform.
- Synthetic Staging Ledger: We programmatically simulate 12 months of transactional behaviors for 500 virtual customers.

This structure allows us to build, test, and run a complete analytical pipeline exactly how a data professional would test code in a secure corporate staging environment before deploying it to production.

## ⚙️ Process
### 1. Data Ingestion
Our first step is to retrieve the catalog data from Wayfair. We're using a specific category of products from Wayfair - that being area rugs. The data will come from the HTML webpage *"https://www.wayfair.com/rugs/sb0/area-rugs-c215386.html?keyword=rugs"*. 

Now we create our first file **scraper.py** to act as an HTML parsing engine using BeautifulSoup to extract the live catalog items, real product names, and current prices directly from the e-commerce interface. The file produces a **product_catalog.csv** file containing the product names and authentic prices directly from the live web.

<br>[scraper.py](https://github.com/jean-paulio/Wayfair-Customer-Analysis/blob/main/scraper.py)

<br>The full output from the product_catalog.csv file produces 49 rows of unique products. The following preview shows the first 10:

<details>
<summary> Preview - product_catalog.csv </summary>

| Product_ID | Product_Name | Price | Source |
| :--- | :--- | :--- | :--- |
| PROD_163bd914 | Disney Mickey Mouse Tropical Sand Dollar Havana Brown/ Sand Flatweave Indoor/ | $ 208.84 | scraped |
| PROD_ef361fba | Radiant Oriental Multicolor Hand Knotted Wool Blue, Pink, Navy Traditional Area | $3,399.99 | scraped |
| PROD_f03852cf | Lahjar Speckled Wool Blend Area Rug | $ 519.99 | scraped |
| PROD_a39a8d2b | Rinoa Indoor / Outdoor Rug | $ 202.99 | scraped |
| PROD_fd0cd8cf | Non-Slip Washable Stain Resistant Area Rug For Living Room Bedroom Dining Room | $ 97.99 | scraped |
| PROD_15009179 | Maust Sunshine Rainbow Shag Rug | $ 109.99 | scraped |
| PROD_96a0055d | Loloi Botanical Ivory / Multi Area Rug | $ 32.99 | scraped |
| PROD_03533587 | Hand Hooked Wool Oriental Indoor Rug | $ 49.99 | scraped |
| PROD_9d77c7b9 | Rifle Paper Co. x Loloi Rosa Sky Area Rug | $ 110.66 | scraped |
| PROD_28b95f59 | Mendota Geometric Tan Indoor/Outdoor Area Rug | $ 139.99 | scraped |

</details>

### 2. Data Cleaning & Quality Control

Our next file **clean_data.py** is part of our validation step which uses Pandas to identify and strip out web-scraping anomalies, layout clutter, and duplicate price captures. This stage ensures a clean database schema and enforces data integrity before injecting the catalog into downstream systems. 

<br>[clean_data.py](https://github.com/jean-paulio/Wayfair-Customer-Analysis/blob/main/clean_data.py)

<br>In this instance, our run of scraper.py produced output clean enough that clean_data.py made no alrerations. Of course, we still keep this file as part of our pipeline to guarantee that regardless of what the craper pulls from any other potential runs, only validated and proper schema-compliant data reaches our database.

### 3. Operational Database Simulation

After verifying our product catalog is clean, we run our last file **simulator.py**. This file acts as an engine to generate our **raw_sales_data.csv** file -- a historical ledger of 2500 simulated sales transactions using a real scraped product catalog and simulated customers. It employs weighted random distributions to model realistic consumer patterns (such as order frequencies, varying basket sizes, and transaction dates over a 365-day timeline).

<br>[simulator.py](https://github.com/jean-paulio/Wayfair-Customer-Analysis/blob/main/simulator.py)

<br> The full output from the raw_sales_data.csv file produces 2500 rows of unique transactions. The following preview shows the first 10:

<details>
<summary> Preview - raw_sales_data.csv </summary>

| InvoiceNo | CustomerID | CustomerName | ProductID | ProductName | UnitPrice | Quantity | InvoiceDate
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| INV_668950 | CUST_1206 | Stacey Arias | PROD_7cb7c01e | Achilles Cream/Gray Rug | $ 121.88 | 2 | 6/1/2025 |
| INV_945687 | CUST_1362 | Melissa Brewer | PROD_81ed29d6 | Soft Washable Vintage Distressed Beige Area Rug with Non-Slip Backing | $ 136.26 | 1 | 6/1/2025 |
| INV_320392 | CUST_1207 | Zachary Brooks | PROD_16a4bedb | Aitken Machine Woven Geometric Indoor and Outdoor Rug | $ 69.60 | 2 | 6/1/2025 |
| INV_969659 | CUST_1231 | Michele Lewis | PROD_f03852cf | Lahjar Speckled Wool Blend Area Rug | $ 536.25 | 1 | 6/1/2025 |
| INV_352249 | CUST_1149 | David Medina | PROD_81ed29d6 | Soft Washable Vintage Distressed Beige Area Rug with Non-Slip Backing | $ 137.55 | 5 | 6/1/2025 |
| INV_960622 | CUST_1495 | Curtis Watson | PROD_a39a8d2b | Rinoa Indoor / Outdoor Rug | $ 207.12 | 1 | 6/1/2025 |
| INV_911329 | CUST_1086 | Madison Poole | PROD_1ad08862 | Scalloped Washable Rug Area Rugs for Living Room Modern Rugs Abstract Non-Slip | $ 72.93 | 1 | 6/1/2025 |
| INV_612340 | CUST_1472 | Samuel Suarez | PROD_7ef65a00 | Jules Checkered Area Rug | $ 136.33 | 1 | 6/1/2025 |
| INV_548580 | CUST_1225 | Heather Bolton | PROD_20bbb110 | Ainswick Memory Foam Large Rug | $ 598.02 | 1 | 6/1/2025 |
| INV_696474 | CUST_1135 | Brooke Alexander | PROD_885c587d | Paseo Gurseerit All-Weather Flatweave Indoor/Outdoor Area Rug, Brown Black | $ 94.18 | 2 | 6/1/2025 |

</details>

### 4. Cohort Analytics
