import logging
import subprocess
import sys
from typing import Any, Dict

# Configure logger for AWS Lambda
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    try:
        # Validate required event parameters
        if not isinstance(event, dict):
            error_msg = "Event must be a dictionary"
            logger.error(error_msg)
            return {"statusCode": 400, "body": error_msg}
        
        if "data_type" not in event:
            error_msg = "Missing required parameter: 'data_type'"
            logger.error(error_msg)
            return {"statusCode": 400, "body": error_msg}
        
        if "congress_value" not in event:
            error_msg = "Missing required parameter: 'congress_value'"
            logger.error(error_msg)
            return {"statusCode": 400, "body": error_msg}
        
        data_type = event["data_type"]
        congress_value = event["congress_value"]
        
        # Validate types
        if not isinstance(data_type, str):
            error_msg = "Parameter 'data_type' must be a string"
            logger.error(error_msg)
            return {"statusCode": 400, "body": error_msg}
        
        if not isinstance(congress_value, (str, int)):
            error_msg = "Parameter 'congress_value' must be a string or integer"
            logger.error(error_msg)
            return {"statusCode": 400, "body": error_msg}
        
        # Convert congress_value to string for the command
        congress_str = str(congress_value)
        
        logger.info(f"Starting congress scraper with data_type={data_type}, congress={congress_str}...")
        result = subprocess.run(
            ["python3", "-m", "congress.run", data_type, f"--congress={congress_str}"],
            capture_output=True,
            text=True
        )
        if result.stdout:
            logger.info(result.stdout)
        if result.stderr:
            logger.error(f"Subprocess errors: {result.stderr}")
        logger.info("Congress scraper completed successfully.")
        return {"statusCode": 200, "body": "Scrape complete"}
    except Exception as e:
        logger.error(f"Error running scraper: {e}", exc_info=True)
        return {"statusCode": 500, "body": f"Internal error: {str(e)}"}

