import sys
from typing import TYPE_CHECKING
from typing import Optional

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol


class SupportsRead(Protocol):
    def read(self, amount: Optional[int] = 0) -> str:
        ...
