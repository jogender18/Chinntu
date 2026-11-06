"""Skill source resolvers — Hermes, OpenClaw, generic GitHub."""

from chinntu.skills.sources.base import ResolvedSkill, SourceResolver
from chinntu.skills.sources.github import GitHubResolver
from chinntu.skills.sources.hermes import HERMES_REPO_URL, HermesResolver
from chinntu.skills.sources.openclaw import OPENCLAW_REPO_URL, OpenClawResolver

__all__ = [
    "GitHubResolver",
    "HERMES_REPO_URL",
    "HermesResolver",
    "OPENCLAW_REPO_URL",
    "OpenClawResolver",
    "ResolvedSkill",
    "SourceResolver",
]
