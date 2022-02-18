from dataclasses import dataclass
from typing import Callable


class _RequestManager:
    get_headers: Callable[[], dict[str, str]]
    _make: Callable[[str, str, dict | None], dict[str,] | None]
    rget: Callable[[str], dict[str,] | None]
    rpost: Callable[[str, dict | None], dict[str,] | None]
    rpatch: Callable[[str, dict | None], dict[str,] | None]
    rput: Callable[[str, dict | None], dict[str,] | None]
    rdelete: Callable[[str], dict[str,] | None]
    on_receive: Callable[[dict[str,]], None]
    on_debug: Callable[[str], None]


class _PteroApp:
    domain: str
    auth: str
    options: None
    ready_at: float
    ping: float
    connect: Callable[[], bool]
    requests: _RequestManager


@dataclass
class NodeLocation:
    id: int
    long: str
    short: str
    created_at: str
    updated_at: str | None

    def __repr__(self) -> str:
        return '<NodeLocation id=%d long=%s short=%s>' \
            % (self.id, self.long, self.short)