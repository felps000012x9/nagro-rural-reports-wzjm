import os
import logging

log = logging.getLogger(__name__)

PORT = int(os.getenv("APP_PORT", "8030"))
ENV = os.getenv("APP_ENV", "development")


def main() -> None:
    log.info("starting on port %s (%s)", PORT, ENV)


if __name__ == "__main__":
    main()
