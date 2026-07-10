"""
Subscription API Routes
All route modules are imported here for easy access.
"""

import os


SKIP_PAYMENT = os.getenv("SKIP_PAYMENT", "false").lower() == "true"

from . import (
    usage,
    plans,
    subscriptions,
    alerts,
    dashboard,
    logs,
    preflight,
    disputes,
)

if not SKIP_PAYMENT:
    from . import payment

__all__ = [
    "usage",
    "plans",
    "subscriptions",
    "alerts",
    "dashboard",
    "logs",
    "preflight",
    "disputes",
]

if not SKIP_PAYMENT:
    __all__.append("payment")