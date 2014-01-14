import logging
logging.basicConfig(level=logging.DEBUG)

from orderme.commands import manager
from orderme import create_app


if __name__ == '__main__':
    manager.app = create_app()
    manager.run()
