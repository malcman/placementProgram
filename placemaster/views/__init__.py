"""Load class-based views for each placemaster page."""
from lib.loaders import get_views


def init_views(app):
    """Initialize application views."""
    if not app:
        raise Exception('Application instance needed to instantiate views.')

    for view in get_views():
        app.add_url_rule(
            view.url,
            view_func=view.as_view(view.endpoint)
        )
