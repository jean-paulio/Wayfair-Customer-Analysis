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

<details>
<summary> product_catalog.csv (preview) </summary>

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

### 2. Quality Control & Transformation
### 3. Operational Database Simulation
### 4. Cohort Analytics
