import pandas as pd


class DataSchema:
    RAW_405nm = "raw_405nm"
    RAW_465nm = "raw_465nm"
    DFF = "dff"


def load_data(data_path: str) -> pd.DataFrame:
    df = pd.read_csv(
        data_path,
        dtype={
            DataSchema.RAW_405nm: float,
            DataSchema.RAW_465nm: float,
            DataSchema.DFF: float,
        },
    )
    return df.iloc[:2000]
