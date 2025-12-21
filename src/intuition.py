"""
Gut-instinct helpers: log flags, recap patina, and gate fold actions.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class GutFlag:
    timestamp: float
    thread: str
    flag: str  # e.g., "unease", "pull", "clarity"
    note: str


def log_flag(flags: List[GutFlag], flag: GutFlag) -> List[GutFlag]:
    """Append a gut flag and return the list."""
    flags.append(flag)
    return flags


def patina_recap(last_thread_notes: List[str]) -> str:
    """
    Short recap to re-establish tone after a reset.
    Stub: join notes; in practice, summarize with capsule framing.
    """
    return " | ".join(last_thread_notes)
