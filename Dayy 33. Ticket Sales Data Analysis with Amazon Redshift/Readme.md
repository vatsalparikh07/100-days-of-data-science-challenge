# Day 33. 100 Days of Data Science Challenge - 03/05/2025

# Ticket Sales Data Analysis with Amazon Redshift
[![Redshift](https://img.shields.io/badge/Amazon_Redshift-Data_Warehouse-%23FF9900)](https://aws.amazon.com/redshift/) 
[![Data Integrity](https://img.shields.io/badge/Data_Quality-96%25-success)]()

## 🎯 Project Focus  
Analyze a 2008 ticketing platform dataset (192K+ listings) to uncover market patterns, operational anomalies, and revenue opportunities using **cloud-native analytics** in Amazon Redshift.

---

## 📊 Dataset Profile  
- **Scope**: 8,798 events across 79 cities (Jan-Nov 2008)  
- **Key Tables**:
```
event: Concerts (63%), Shows (37%)
sales: $22.8-$259.5 price range | 17s-60d sale cycles
users: 48K+ buyers/sellers
```
- **Temporal Coverage**:  
- Peak sales week: 2008-02-18 ($2.6M revenue)  
- Fastest sale: 17 seconds (Las Vegas events)

---

## 🔍 Strategic Insights  

### 🌆 Geographic Hotspots  
| City          | Events | Avg Price | Top Category      |  
|---------------|--------|-----------|-------------------|  
| New York City | 2,647  | $229      | Concerts (63%)    |  
| Las Vegas     | 300    | $232      | Shows (58%)       |  
| Chicago       | 209    | $221      | Concerts (71%)    |  

**Pattern**: Coastal cities show 28% higher ticket velocity than inland markets.

---

### ⚠️ Data Quality Alerts  
- **2,965 listings** had sales recorded before listing creation  
- **7.4% price outliers** beyond IQR ranges (concert tickets)  

---

### 💰 Revenue Drivers  
**Top Performers**:  
- **Nayda Hood (Frisco)**: 46 tickets sold ($8.2K revenue)  
- **Scott Simmons (Carson)**: 41 tickets ($7.3K)  

**Unrealized Potential**:  
| Seller         | Lost Revenue | Root Cause         |  
|----------------|--------------|--------------------|  
| Jaime Wagner   | $58,395      | Overpriced listings|  
| Macey Ortiz    | $53,086      | Poor visibility    |  

---

## 🛠️ Technical Approach  

### 1️⃣ Data Pipeline  
- **Schema Design**: Star schema with `sales` fact table  
- **Key Joins**:
```
event → venue (location context)
sales → users (buyer/seller profiles)
```

### 2️⃣ Analytical Toolkit  
- **Temporal Analysis**: DATEDIFF('hour', listing → sale)  
- **Cohort Filtering**:  
```df = sales.query('listtime < saletime') # 96% valid transactions```
- **Price Elasticity**: 45% variance in concert ticket prices  

---

## 📈 Market Dynamics  
![image](https://github.com/user-attachments/assets/08e4f03b-93a4-472c-ae97-c2c2215009d7)
**Key Trend**: February 2008 peak (Super Bowl XLII + Grammy Awards) drove 42% Q1 revenue.

---

## 💡 Operational Takeaways  
1. **Inventory Risks**:  
 - 12% listings remained unsold after 60 days  
 - Recommendation: Dynamic pricing alerts after 7-day stagnation  

2. **User Engagement**:  
 - Top 0.1% sellers drive 18% of total revenue  
 - Action: Loyalty program for power sellers  

3. **Tech Debt**:  
 - 2.8% transactions had invalid timestamps  
 - Solution: Blockchain-based timestamp validation  

*"In ticketing analytics, every second of latency translates to lost opportunities"* 🎫⏳  
