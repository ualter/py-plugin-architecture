from typing import Any, Callable, Dict
from .cypher_protocol import Cypher

cypher_plugin_creation_funcs: Dict[str, Callable[..., Cypher]] = {}

def register(cypher_type: str, creator_fn: Callable[..., Cypher]) -> None:
    """Register a new Cypher type."""
    cypher_plugin_creation_funcs[cypher_type] = creator_fn

def unregister(cypher_type: str) -> None:
    """Unregister a Cypher type."""
    cypher_plugin_creation_funcs.pop(cypher_type, None)

def instantiate(arguments: Dict[str, Any]) -> Cypher:
    """Create a Cypher of a specific type"""
    args        = arguments.copy()
    cypher_type = args.pop("type")
    try:
        creator_func = cypher_plugin_creation_funcs[cypher_type]
    except KeyError:
        raise ValueError(f"error creating cypher type, unknown type: {cypher_type}") from None
    return creator_func(**args)
