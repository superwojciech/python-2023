
"""
Semantic versioning
https://devopedia.org/images/article/279/7179.1593248779.png
{Major}.{Minor}.{Patch}
np.
'1.3.6' oznacza major=1, minor=3, path=6
"""


def get_latest(versions: list[str]) -> str:
    for i in range(len(versions)):
        return max(versions)

def next_version(version: str, level: int) -> str:
    x, y, z = version.split('.')
    if level == 0:
        x = str(int(x) + 1)
        y = "0"
        z = "0"
    elif level == 1:
        y = str(int(y) + 1)
        z = "0"
    elif level == 2:
        z = str(int(z) + 1)
    return '.'.join([x, y, z])

