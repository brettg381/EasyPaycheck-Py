"""
Backwards-compatible URLconf for existing django-registration
installs; this allows the standard ``include('registration.urls')`` to
continue working, but that usage is deprecated and will be removed for
django-registration 1.0. For new installs, use
``include('registration.backends.default.urls')``.

"""

import warnings

warnings.warn("include('payroll.apps.registration.urls') is deprecated; use include('payroll.apps.registration.backends.default.urls') instead.",
              PendingDeprecationWarning)

from payroll.app.registration.backends.default.urls import *
