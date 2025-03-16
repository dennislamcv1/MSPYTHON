import logging
from datetime import datetime
import time

# Set up logging
logging.basicConfig(filename='task_manager.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_action(func):
    """Decorator to log task actions.

    This decorator logs the function name and its arguments 
    to the 'task_manager.log' file whenever the decorated 
    function is called.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapper function.
    """
    def wrapper(*args, **kwargs):
        current_datetime = datetime.now()
        logging.info(f"{current_datetime}: Executing function: {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def timer(func):
    """Decorator to measure execution time of a function.

    This decorator calculates and logs the time taken 
    for the decorated function to execute.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapper function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        logging.info(f"Function {func.__name__} took {total_time:.4f} seconds to execute.")
        return result
    return wrapper