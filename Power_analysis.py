#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 14:23:26 2025

@author: sara
"""
# power_analysis.py - AI- project 3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'hour': list(range(24)),
    'consumption_kwh': [3.1, 2.8, 2.5, 2.3, 2.7, 3.5, 5.2, 7.8, 9.1, 8.5,
                 8.2, 7.9, 8.8, 9.5, 10.2, 11.1, 12.5, 14.3, 15.8, 16.2,
                 15.5, 13.8, 10.5, 6.8]
}

df = pd.DataFrame(data)


total = df['consumption_kwh'].sum()
peak_hour = df.loc[df['consumption_kwh'].idxmax()]
avg = df['consumption_kwh'].mean()

print(f": {total:.1f} KWh")
print(f"Pick time :{peak_hour['hour']}:00 → {peak_hour['consumption_kwh']} kWh")
print(f"avg time: {avg:.1f} kWh")
cost_per_kwh = 1000
total_costv=vtotal * cost_per_kwh
print(f"cost in one day: {total_cost:,} $")
plt.figure(figsize=(10,5))
plt.plot(df['hour'], df['consumption_kwh'], marker='o', color='#00A896')
plt.title('usage in 24h', fontsize=16)
plt.xlabel('time')
plt.ylabel('usage (kWh)')
plt.grid(True, alpha=0.3)
plt.xticks(range(0,24,2))
plt.tight_layout()
plt.savefig("power_consumption.png", dpi=200)
plt.show()

