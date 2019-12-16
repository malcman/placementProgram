"""Load class-based views for each google_auth page."""
from lib.loaders import get_views


def init_views(app, module_base):
    """Initialize application views."""
    if not app:
        raise Exception('Application instance needed to instantiate views.')

    # add all views in google_login.views
    for view in get_views(module_base):
        app.add_url_rule(
            view.url,
            view_func=view.as_view(view.endpoint)
        )
