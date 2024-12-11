# Learning Benchmark Workshop (lbw)

Welcome to the Learning Benchmark Workshop (lbw) repository! This project aims to provide a unified data interface for machine learning (ML) and deep learning (DL) models.

## Features

- **Unified Data Interface**: Simplify data preprocessing and handling with a consistent and modular interface.

## Installation

You can install the `lbw` package via pip:

```bash
pip install git+https://github.com/Saltsmart/lbw
```

## Getting Started

Here is a quick example to help you get started:

```python
from lbw.samples import TimeSeries
from lbw.datasets import TimeSeriesDataset

# Load your dataset
dataset = TimeSeriesDataset()
df_lst = [
    pd.DataFrame(
        {
            "time": pd.date_range(start=f"2023-0{i}-01", periods=10, freq="D"),
            "value": np.random.randn(10)
        }
    ) for i in range(4)
]
covar_lst = [i for i in range(4)]


for df, covariate in zip(df_lst, covar_lst):
    series = TimeSeries(
        df,
        {
            "covariate": covariate
        },
    )
    dataset.append(series)
```

## Contributing

We welcome contributions from the community! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the BSD License. See the `LICENSE` file for details.

## Contact

For questions or feedback, please reach out to us via the issue tracker.

