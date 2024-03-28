from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_filepath: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_filepath: str
    all_required_files: list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_dir: Path
    tokenizer_name: Path