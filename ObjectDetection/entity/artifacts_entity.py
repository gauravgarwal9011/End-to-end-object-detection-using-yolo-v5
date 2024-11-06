from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    data_zip_file_path:str
    feature_store_path:str


@dataclass
class DataValidationArtifact:
    validation_status: bool