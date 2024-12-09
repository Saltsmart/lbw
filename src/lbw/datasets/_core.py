from typing import Any, Iterable
from textwrap import dedent
from lbw.samples import Sample


class Dataset(object):
    """
    所有dataset类的基类
    """

    def __init__(
        self,
        title: str = "",
        ver: str = "",
        description: str = "",
        license: str = "",
        tags: list[str] = [],
        samples: list[Sample] = [],
        **kuargs,
    ) -> None:
        """
        标题、版本号、描述、协议、标签等信息
        初始化Sample sequence
        """
        self.title = title
        self.ver = ver
        self.description = description
        self.license = license
        self.tags: list[str] = []
        self.tags.extend(tags)
        # TODO:要不要对metadata使用type hint？
        self.other_metadata = kuargs

        # Sample sequence和数目
        self.samples: list[Sample] = []
        self.samples.extend(samples)
        self.n_sample = len(self.samples)

    def __len__(self) -> int:
        return self.n_sample

    def __repr__(self) -> str:
        return (
            self.title
            + "\nVersion: "
            + self.ver
            + "\nNumber of Samples: "
            + str(self.n_sample)
            + "\nOther Metadata: "
            + str(self.other_metadata)
        )

    def __str__(self) -> str:
        info = f"""
        Title: {self.title}
        Version: {self.ver}
        ----------------------------
        Description: {self.description}
        License: {self.license}
        Tags: {self.tags}
        Number of Samples: {self.n_sample}
        """
        return dedent(info).strip()

    def __getitem__(self, sample_id: int | slice) -> Sample | list[Sample]:
        """取出对应Sample"""
        return self.samples[sample_id]

    def __setitem__(self, sample_id: int | slice, new_sample: Sample) -> None:
        """修改对应Sample"""
        self.samples[sample_id] = new_sample

    def append(self, sample: Sample) -> None:
        """追加一个Sample"""
        self.samples.append(sample)
        self.n_sample += 1

    def extend(self, samples: Iterable[Sample]) -> None:
        """追加一组Samples"""
        self.samples.extend(samples)
        self.n_sample += len(samples)

    def pop(self, sample_id: int) -> Sample:
        self.n_sample -= 1
        return self.samples.pop(sample_id)

    def select(
        self, key: str, value: Any | list[Any], return_index: bool = False
    ) -> list[Sample] | tuple[list[Sample], list[int]]:
        if isinstance(value, list):
            if return_index:
                sample_lst, index_lst = zip(
                    *(
                        (s, i)
                        for i, s in enumerate(self.samples)
                        if s.metadata[key] in value
                    )
                )
                return list(sample_lst), list(index_lst)
            else:
                return [s for s in self.samples if s.metadata[key] in value]
        else:
            if return_index:
                sample_lst, index_lst = zip(
                    *(
                        (s, i)
                        for i, s in enumerate(self.samples)
                        if s.metadata[key] == value
                    )
                )
                return list(sample_lst), list(index_lst)
            else:
                return [s for s in self.samples if s.metadata[key] == value]

    # TODO:增加运算符（非原地追加）
    #           '__new__': <function list.__new__(*args, **kwargs)>,
    #           '__hash__': None,
    #           '__getattribute__': <slot wrapper '__getattribute__' of 'list' objects>,
    #           '__lt__': <slot wrapper '__lt__' of 'list' objects>,
    #           '__le__': <slot wrapper '__le__' of 'list' objects>,
    #           '__eq__': <slot wrapper '__eq__' of 'list' objects>,
    #           '__ne__': <slot wrapper '__ne__' of 'list' objects>,
    #           '__gt__': <slot wrapper '__gt__' of 'list' objects>,
    #           '__ge__': <slot wrapper '__ge__' of 'list' objects>,
    #           '__iter__': <slot wrapper '__iter__' of 'list' objects>,
    #           '__delitem__': <slot wrapper '__delitem__' of 'list' objects>,
    #           '__add__': <slot wrapper '__add__' of 'list' objects>,
    #           '__mul__': <slot wrapper '__mul__' of 'list' objects>,
    #           '__rmul__': <slot wrapper '__rmul__' of 'list' objects>,
    #           '__contains__': <slot wrapper '__contains__' of 'list' objects>,
    #           '__iadd__': <slot wrapper '__iadd__' of 'list' objects>,
    #           '__imul__': <slot wrapper '__imul__' of 'list' objects>,
    #           '__reversed__': <method '__reversed__' of 'list' objects>,
    #           '__sizeof__': <method '__sizeof__' of 'list' objects>,
    #           'clear': <method 'clear' of 'list' objects>,
    #           'copy': <method 'copy' of 'list' objects>,
    #           'insert': <method 'insert' of 'list' objects>,
    #           'remove': <method 'remove' of 'list' objects>,
    #           'index': <method 'index' of 'list' objects>,
    #           'count': <method 'count' of 'list' objects>,
    #           'reverse': <method 'reverse' of 'list' objects>,
    #           'sort': <method 'sort' of 'list' objects>,
    #           '__class_getitem__': <method '__class_getitem__' of 'list' objects>,
    #           '__doc__': 'Built-in mutable sequence.
