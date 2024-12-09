from dataclasses import dataclass
from typing import Any


@dataclass(repr=False)
class Sample:
    data: Any
    _metadata: dict

    def __repr__(self) -> str:
        return str(self._metadata)

    def __str__(self) -> str:
        info = ""
        for k, v in self._metadata.items():
            info += f"{k}: {v}"
        return info

    @property
    def metadata(self) -> dict:
        return {**self._metadata}
