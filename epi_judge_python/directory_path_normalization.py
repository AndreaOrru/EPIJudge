from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    path_stack = []

    for token in path.split('/'):
        if token in ('.', ''):
            continue
        elif token == '..' and path_stack and path_stack[-1] != '..':
            path_stack.pop()
        else:
            path_stack.append(token)

    return ('/' if path[0] == '/' else '') + '/'.join(path_stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
