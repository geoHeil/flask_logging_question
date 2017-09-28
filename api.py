from flask import Flask

from my_pkg.second import log_ome_stuff_in_other_module
from settings.settings import configure_logger

app = Flask(__name__)
logger = configure_logger(log_path='./logs/')
app.logger.addHandler(logger)


@app.route("/api/foo/", methods=["GET"])
def log_feedback():
    app.logger.info('flask logging')
    # but not using my configuration
    logger.info('my logger - but not in flask')
    logger.info('other module not logged properly')
    log_ome_stuff_in_other_module()

    return ('', 204)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
