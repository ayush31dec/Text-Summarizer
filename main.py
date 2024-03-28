from textSummarizer.logging import logger
from textSummarizer.pipeline.stg01_data_ingestion import DataIngestionPipeline

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
    