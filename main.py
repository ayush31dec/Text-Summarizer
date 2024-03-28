from textSummarizer.logging import logger
from textSummarizer.pipeline.stg01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stg02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stg03_data_transformation import DataTransformationPipeline

# if __name__ == "__main__":
#     logger.info("Starting")
#     # print("Starting")   


STAGE_NAME = "Data Ingestion STAGE"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation STAGE"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
    

STAGE_NAME = "Data Transformation STAGE"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
    