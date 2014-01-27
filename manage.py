# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG)

from orderme import create_app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        from orderme.commands import manager
        manager.app = app
        manager.run()
