import pandas as pd
data = {
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-01', '2025-01-02'],
    'Product': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 200, 150, 180, 120],
    'Region': ['North', 'South', 'North', 'South', 'North']
}

df = pd.DataFrame(data)
print(df)

pivot_table = df.pivot_table(values='Sales', 
                             index='Date' , 
                             columns='Product', 
                             aggfunc='sum', 
                             fill_value=0)
print(pivot_table)
