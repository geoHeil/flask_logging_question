import logging
logger = logging.getLogger('root')

def log_ome_stuff_in_other_module():
    logger.info("other info")
    logger.debug("other debug")
    logger.error("other error")