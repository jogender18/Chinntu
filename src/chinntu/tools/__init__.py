"""Tools primitive — tool system with ABC interface and built-in tools."""

from __future__ import annotations

from chinntu.tools._stubs import BaseTool, ToolExecutor, ToolSpec

# Import built-in tools to trigger @ToolRegistry.register() decorators.
# Each is wrapped in try/except so the package loads even before the
# individual tool modules are created.
try:
    import chinntu.tools.calculator  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.think  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.retrieval  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.llm_tool  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.file_read  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.web_search  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.weather  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.fx_macro  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.code_interpreter  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.code_interpreter_docker  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.repl  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.storage_tools  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.mcp_adapter  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.channel_tools  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.http_request  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.docker_shell_exec  # noqa: F401
    import chinntu.tools.shell_exec  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.memory_manage  # noqa: F401
except ImportError:
    pass
try:
    import chinntu.tools.user_profile_manage  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.skill_manage  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.file_write  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.apply_patch  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.git_tool  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.db_query  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.pdf_tool  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.image_tool  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.audio_tool  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.knowledge_tools  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.text_to_speech  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.digest_collect  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.scan_chunks  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.knowledge_sql  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.apple_calendar  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.knowledge_search  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.browser  # noqa: F401
    import chinntu.tools.browser_axtree  # noqa: F401
except ImportError:
    pass

try:
    import chinntu.tools.proactive_tools  # noqa: F401
except ImportError:
    pass

__all__ = ["BaseTool", "ToolExecutor", "ToolSpec"]
