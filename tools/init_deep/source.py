from dataclasses import dataclass
from pathlib import Path
import re

FLAG_PATTERN = re.compile(r"`(--[^`]+)`")


@dataclass(frozen=True)
class CanonicalSource:
    raw: str
    flags: tuple[str, ...]


def load_canonical_source(path: Path) -> CanonicalSource:
    raw = path.read_text(encoding="utf-8")
    flags = tuple(dict.fromkeys(FLAG_PATTERN.findall(raw)))
    return CanonicalSource(raw=raw, flags=flags)
