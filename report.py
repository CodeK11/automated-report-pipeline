#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import datetime

data = {
    'date': ['2026-10-01', '2026-10-02', '2026-10-03'],
    'orders': [120, 150, 130],
    'revenue': [2400, 3000, 2600]
}
df = pd.DataFrame(data)

total_orders = df['orders'].sum()
total_revenue = df['revenue'].sum()
avg_order_value = total_revenue / total_orders

report = f"""
# Automated Operations Report
Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

- Total Orders: {total_orders}
- Total Revenue: ${total_revenue}
- Average Order Value: ${avg_order_value:.2f}
"""

with open('report.md', 'w') as f:
    f.write(report)

print("Report generated: report.md")


# In[ ]:




