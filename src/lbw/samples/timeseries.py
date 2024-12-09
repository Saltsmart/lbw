from numpy import ndarray
from pandas import DataFrame
from lbw.samples import Sample


class TimeSeries(Sample):
    """
    单一时间序列：时间轴只有一组的时间序列
    data尺寸：[T, D]
    """

    data: DataFrame

    def __init__(
        self,
        data: DataFrame | ndarray,
        covariate: dict | None = None,  # 与时间序列相关的不变量
        metadata: dict | None = None,
        columns: dict | None = None,
    ) -> None:
        super().__init__(data=data, _metadata=metadata)
        if isinstance(data, DataFrame):
            self.from_dataframe(data, covariate, metadata)
        elif isinstance(data, ndarray):
            self.from_ndarray(data, covariate, metadata, columns)
        else:
            raise NotImplementedError("data must be pandas.DataFrame or numpy.ndarray.")

    def from_dataframe(
        self,
        data: DataFrame,
        covariate: dict | None,
        metadata: dict | None,
    ) -> None:
        """
        从DataFrame中新建时间序列
        """
        self.data = data

        if covariate is None:
            self.covariate = (
                data.attrs.copy()
            )  # attrs is experimental and may change without warning.
        elif isinstance(covariate, dict):
            self.covariate = covariate.copy()
        else:
            raise TypeError

        self._metadata = {}
        if metadata is None:
            pass
        elif isinstance(metadata, dict):
            self._metadata.update(metadata)
        else:
            raise TypeError

    @property
    def metadata(self):
        return {**self._metadata, **self.covariate}  # coveriate也算在metadata里

    def from_ndarray(
        self,
        data: ndarray,
        covariate: dict | None,
        metadata: dict | None,
        columns: list | None,
    ) -> None:
        """
        从ndarray中新建时间序列
        ndarray尺寸：[T, D]
        """
        if columns is None:
            df_data = DataFrame(data, columns=[i for i in range(data.shape[0])])
        else:
            df_data = DataFrame(data, columns=columns)

        self.from_dataframe(df_data, covariate, metadata)
