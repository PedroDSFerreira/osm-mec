import importlib.util
import os


def load_callback_functions():
    callbacks = {}
    callback_dir = os.path.dirname(__file__)
    for filename in os.listdir(callback_dir):
        if filename != "__init__.py" and filename.endswith(".py"):
            module_name = filename[:-3]
            spec = importlib.util.spec_from_file_location(
                module_name, os.path.join(callback_dir, filename)
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "callback"):
                callbacks[module_name] = module.callback
    return callbacks
