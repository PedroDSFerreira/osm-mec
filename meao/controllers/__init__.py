import os
import importlib

def load_controllers():
    """
    Load controllers from controllers/ directory
    """
    # Load controllers from controllers directory
    controllers = {}
    for filename in os.listdir("controllers"):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module = importlib.import_module(f"controllers.{module_name}")
            controllers[module_name] = getattr(module, f"{module_name.capitalize()}Controller")

    return controllers