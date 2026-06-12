"""
WSGI configuration file for the Hall C RCDB web application (crcdb.org).

Gunicorn imports `application` from this module. The rcdb Flask app
(`rcdb.web.app`) is configured here for multi-database browsing: the
navbar database selector exposes every entry in AVAILABLE_DATABASES,
and DEFAULT_DATABASE is shown on first visit (see rcdb/web/__init__.py).

    Only v2-schema databases are supported (the rcdb library here is v2-only).
"""

# Databases exposed in the web UI selector. Keys are display names; values
# are the database names on the MariaDB server.
AVAILABLE_DATABASES = {
    "rsidis": "mysql+pymysql://rcdb@hallcdb.jlab.org/rsidis",
    "prex2":  "mysql+pymysql://rcdb@hallcdb.jlab.org/prex2",
    "nps":    "mysql+pymysql://rcdb@hallcdb.jlab.org/nps",
    "lad":    "mysql+pymysql://rcdb@hallcdb.jlab.org/lad",
    "vcs":    "mysql+pymysql://rcdb@hallcdb.jlab.org/vcs",
}

# Database shown on first visit (must be one of the values above).
DEFAULT_DATABASE = AVAILABLE_DATABASES["rsidis"]

import rcdb.web

rcdb.web.app.config.update(
    AVAILABLE_DATABASES=AVAILABLE_DATABASES,
    DEFAULT_DATABASE=DEFAULT_DATABASE,
    # Fallback single-DB string (used only if AVAILABLE_DATABASES is empty).
    SQL_CONNECTION_STRING=DEFAULT_DATABASE,
    # The app has no login and stores no sensitive data -- the session cookie
    # only remembers which database the visitor is browsing. A fixed key is
    # therefore fine and keeps that selection stable across restarts.
    SECRET_KEY="crcdb-db-selector",
    DEBUG=False,
)

application = rcdb.web.app
