"""Data source connectors for Deep Research."""

from chinntu.connectors._stubs import (
    Attachment,
    BaseConnector,
    Document,
    SyncStatus,
)
from chinntu.connectors.store import KnowledgeStore

__all__ = ["Attachment", "BaseConnector", "Document", "KnowledgeStore", "SyncStatus"]

# Auto-register built-in connectors
import chinntu.connectors.obsidian  # noqa: F401

try:
    import chinntu.connectors.gmail  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.gmail_imap  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.gdrive  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import chinntu.connectors.notion  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.granola  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.gcontacts  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.imessage  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.apple_notes  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.apple_music  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.apple_contacts  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.apple_calendar  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.slack_connector  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.outlook  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.imap  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.gcalendar  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.dropbox  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import chinntu.connectors.whatsapp  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.oura  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.apple_health  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.strava  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.spotify  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.google_tasks  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.weather  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.github_notifications  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.hackernews  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.connectors.news_rss  # noqa: F401
except ImportError:
    pass
