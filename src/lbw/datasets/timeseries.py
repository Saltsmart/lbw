from lbw.datasets import Dataset
from lbw.samples import TimeSeries


class TimeSeriesDataset(Dataset):
    samples: list[TimeSeries]
