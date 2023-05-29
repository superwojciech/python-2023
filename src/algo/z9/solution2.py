
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

print(get_latest(['1.13.0', '2.0.5', '1.1.7']))

def next_version(version: str, level: int) -> str:
    """
    :param version: Current version
    :param level: Which part should be incremented; 0: major, 1: minor, 2: patch
    :return: Properly incremented version
    """
    # todo: your code
    return '0.0.1'