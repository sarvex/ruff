# Error (`from unittest import mock`)
import mock

import mock, sys

from mock import *

# Error (`from unittest import mock`)
import mock.mock

# Error (`from unittest import mock`)
import contextlib, mock, sys

# Error (`from unittest import mock`)
import mock, sys
x = "This code should be preserved one line below the mock"

# Error (`from unittest import mock`)
from mock import mock

# Error (keep trailing comma)
from mock import (
    mock,
    a,
    b,
    c,
)
from mock import (
    a,
    b,
    c,
    mock,
)

# Error (avoid trailing comma)
from mock import (
    mock,
    a,
    b,
    c
)
from mock import (
    a,
    b,
    c,
    mock
)
from mock import mock, a, b, c
from mock import a, b, c, mock

# OK
import os, io

# Error (`from unittest import mock`)
import mock, mock

# Error (`from unittest import mock as foo`)
import mock as foo

# Error (`from unittest import mock as foo`)
from mock import mock as foo

# This should yield multiple, aliased imports.
import mock as foo, mock as bar, mock

# This should yield multiple, aliased imports, and preserve `os`.
import mock as foo, mock as bar, mock, os

# This should yield multiple, aliased imports.
from mock import mock as foo, mock as bar, mock


# OK.
x = mock.Mock()

# Error (`mock.Mock()`).
x = mock.mock.Mock()
