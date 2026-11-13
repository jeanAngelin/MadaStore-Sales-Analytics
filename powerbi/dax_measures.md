# Mesures DAX

```DAX
Total Revenue = SUMX(Sales, Sales[quantity] * Sales[unit_price] * (1 - Sales[discount_rate]))
Total Profit = SUMX(Sales, Sales[quantity] * (Sales[unit_price] * (1 - Sales[discount_rate]) - Sales[unit_cost]))
Total Orders = DISTINCTCOUNT(Sales[order_id])
Total Quantity = SUM(Sales[quantity])
Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
Profit Margin = DIVIDE([Total Profit], [Total Revenue], 0)
Monthly Revenue = [Total Revenue]
Yearly Revenue = [Total Revenue]
Revenue Growth = DIVIDE([Total Revenue] - CALCULATE([Total Revenue], DATEADD('Calendar'[Date], -1, YEAR)), CALCULATE([Total Revenue], DATEADD('Calendar'[Date], -1, YEAR)), 0)
```

Formater Profit Margin et Revenue Growth en pourcentage.
