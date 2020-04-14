#!/usr/bin/env python3
"""
duck:$6$PxmNcUBe$rQEHrYBukE9KGv4Zr4QcI6hbn9OMyHxDZpd/gAELYE0hUYZir1zpzjSniih68R/gVvL1fRy96UHkV0/03Y8.Y/:18366:0:99999:7:::
"""

import crypt

uname = "duck"
upasswd = "secret"
usalt = "$6$PxmNcUBe"
uhash = crypt.crypt(upasswd, usalt)
print(uhash)

uhash2 = crypt.crypt(upasswd, crypt.METHOD_SHA512)
print(uhash2)

with open("shadow", "w") as f:
    f.write(f"{uname}:{uhash2}:1:0:99999:7:::")
