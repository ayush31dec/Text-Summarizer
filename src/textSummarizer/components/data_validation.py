import os
from textSummarizer.config.configuration import DataValidationConfig

class DataValidation:

    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config

    def validate_all_files_exists(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_files:

                if file not in self.config.all_required_files:
                    validation_status = False
                    
                else:
                    validation_status = True
            with open(self.config.status_filepath, "w") as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status 

        except Exception as e:
            raise e