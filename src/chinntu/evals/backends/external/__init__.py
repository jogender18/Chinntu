"""External-framework subprocess backends (Hermes Agent, OpenClaw)."""

from chinntu.evals.backends.external.hermes_agent import HermesBackend
from chinntu.evals.backends.external.openclaw import OpenClawBackend

__all__ = ["HermesBackend", "OpenClawBackend"]
