import os
import json

def strip_quotes(s):
    if s.startswith("'") and s.endswith("'") or s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    else:
        return s


def generate_tree(path):
    tree = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        tree['type'] = 'directory'
        tree['children'] = [generate_tree(os.path.join(path, child)) for child in os.listdir(path)]
    else:
        tree['type'] = 'file'
    return tree

def unicode_safe_repr(obj):
    """ Return a unicode-safe string representation of an object """
    try:
        return repr(obj)
    except UnicodeEncodeError:
        return repr(obj).encode('unicode-escape').decode('ascii')

def to_unicode(tree):
    """ Convert all string values in a dictionary to unicode """
    if isinstance(tree, dict):
        return {to_unicode(key): to_unicode(value) for key, value in tree.items()}
    elif isinstance(tree, list):
        return [to_unicode(element) for element in tree]
    elif isinstance(tree, str):
        return strip_quotes(unicode_safe_repr(tree))
    else:
        return tree

if __name__ == '__main__':
    root_path = os.getcwd()
    tree = generate_tree(root_path+'/allSticker/')
    unicode_tree = to_unicode(tree)
    unicode_tree['name'] = 'all'
    with open('stickerFileTree.json', 'w', encoding='utf-8') as f:
        json.dump(unicode_tree, f, ensure_ascii=False, indent=4)
