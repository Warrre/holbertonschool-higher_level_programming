import importlib.machinery
import importlib.util
import os


def load_module_from_path(name, filepath):
    loader = importlib.machinery.SourceFileLoader(name, filepath)
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def test_module(file_path, path):
    print(f"Testing {file_path} -> {path}")
    if not os.path.exists(file_path):
        print('  ERROR: file not found:', file_path)
        return
    mod = load_module_from_path('mod_under_test', file_path)
    app = getattr(mod, 'app', None)
    if app is None:
        print('  ERROR: module has no app variable')
        return
    client = app.test_client()
    resp = client.get(path)
    print('  status:', resp.status_code)
    data = resp.get_data(as_text=True)
    print('  snippet:', data.strip()[:200].replace('\n',' '))

if __name__ == '__main__':
    base = os.path.dirname(__file__)
    test_module(os.path.join(base, 'task_02_logic.py'), '/items')
    test_module(os.path.join(base, 'task_03_files.py'), '/products?source=json')
