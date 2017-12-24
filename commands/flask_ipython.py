import code
import sys

import click
from flask import json
from flask.cli import with_appcontext

name = 'shell_plus'


@with_appcontext
def command():
    """Runs a shell in the app context.
    Runs an interactive Python shell in the context of a given
    Flask application. The application will populate the default
    namespace of this shell according to it's configuration.
    This is useful for executing small snippets of management code
    without having to manually configuring the application.
    """

    from flask.globals import _app_ctx_stack
    from common.utils import import_to_context
    app = _app_ctx_stack.top.app

    banner1 = '''Python %s on %s
App: %s%s
Instance: %s
Db: %s''' % (
        sys.version,
        sys.platform,
        app.import_name,
        app.debug and ' [debug]' or '',
        app.instance_path,
        json.dumps(app.config['DATABASE'], indent=2)
    )
    shell_name_space = app.make_shell_context()

    # import models
    print 'from models import db'
    from models import db
    import_to_context('models', shell_name_space)
    shell_name_space.update(db=db)

    try:
        import IPython
        from IPython.terminal.ipapp import load_default_config
        config = load_default_config()
        config.TerminalInteractiveShell.banner1 = banner1
        IPython.embed(
            user_ns=shell_name_space,
            config=config,
        )
    except ImportError:
        sys.exit(code.interact(banner=banner1, local=shell_name_space))


command.name = name
