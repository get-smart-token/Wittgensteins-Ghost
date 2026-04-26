import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List

DATA_DIR = Path(__file__).parent / "data"


@dataclass
class Trap:
    row_index: int
    gl_trap: str
    bait_text: str
    pivot_trigger: str
    target_vocab: List[str]


@dataclass
class Dataset:
    language: str
    traps: List[Trap]

    def __iter__(self):
        return iter(self.traps)

    def __len__(self):
        return len(self.traps)


def load_dataset(language: str) -> Dataset:
    path = DATA_DIR / f"antagonistic_v1_{language}.csv"
    traps: List[Trap] = []
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            vocab = [v.strip() for v in row["target_vocab"].split(",") if v.strip()]
            traps.append(
                Trap(
                    row_index=int(row["row_index"]),
                    gl_trap=row["gl_trap"],
                    bait_text=row["bait_text"],
                    pivot_trigger=row["pivot_trigger"],
                    target_vocab=vocab,
                )
            )
    return Dataset(language=language, traps=traps)
