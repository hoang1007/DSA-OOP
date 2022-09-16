from abc import abstractmethod
from typing import Any, Protocol, TypeVar

class _Comparable(Protocol):
    """
    Support __lt__ and __le__ methods
    """
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...

    @abstractmethod
    def __le__(self, other: Any) -> bool: ...


Comparable = TypeVar("Comparable", bound=_Comparable)