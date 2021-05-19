from waitress import serve

import __init__
serve(__init__.create_app(None))
