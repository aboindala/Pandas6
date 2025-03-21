import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich_customers = store[store['amount'] > 500]
    count = len(set(rich_customers['customer_id']))
    count = rich_customers['customer_id'].nunique()
    answer = pd.DataFrame({'rich_count' : [count]})
    return answer