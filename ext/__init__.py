"""
Initiate all extension that are available
Lazy-loaded to avoid missing dependency errors for unused sites.
"""

def get_extension(name):
    if name == "abema":
        from ext.abematv import AbemaTV
        return AbemaTV
    elif name == "gyao":
        from ext.gyao import GYAO
        return GYAO
    elif name == "aniplus":
        from ext.aniplus import Aniplus
        return Aniplus
    elif name == "unext":
        from ext.unext import UNext
        return UNext
    raise ImportError(f"Unknown extension: {name}")