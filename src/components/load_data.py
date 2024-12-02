import pandas as pd

data_location = (
    "E:/test/42_1-241030-092508/analysis/fiber_data_20241030_092533_32_623.csv"
)


def load_data():
    df = pd.read_csv(data_location)
    return df.iloc[:2000]
