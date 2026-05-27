"""
Build a navigation tree from the nav_items table.

Used by the side drawer (`surface='menu'`) and the home tiles
(`surface='home'`). Tree is built once per request — small enough that
we don't bother caching yet.
"""
from typing import List, Dict, Any
from ..models import NavItem


def _node_to_dict(n: NavItem, children: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "id": n.id,
        "label_en": n.label_en,
        "label_te": n.label_te,
        "icon": n.icon,
        "action_type": n.action_type,
        "action_ref": n.action_ref,
        "url": _resolve_url(n.action_type, n.action_ref),
        "children": children,
    }


def _resolve_url(action_type: str | None, action_ref: str | None) -> str | None:
    """Translate (action_type, action_ref) into a real URL path."""
    if not action_type:
        return None
    if action_type == "route":
        return action_ref
    if action_type == "subject":
        return f"/subject/{action_ref}"
    if action_type == "chapter":
        return f"/chapter/{action_ref}"
    if action_type == "exam":
        return f"/exam/{action_ref}"
    if action_type == "page":
        return f"/p/{action_ref}"
    if action_type == "url":
        return action_ref
    return None


def build_tree(surface: str) -> List[Dict[str, Any]]:
    """Return ordered list of top-level nav items with nested children."""
    all_items = (
        NavItem.query
        .filter_by(surface=surface, visible=True)
        .order_by(NavItem.sort_order)
        .all()
    )
    by_parent: Dict[int | None, List[NavItem]] = {}
    for item in all_items:
        by_parent.setdefault(item.parent_id, []).append(item)

    def build(parent_id: int | None) -> List[Dict[str, Any]]:
        return [
            _node_to_dict(n, build(n.id))
            for n in by_parent.get(parent_id, [])
        ]

    return build(None)
