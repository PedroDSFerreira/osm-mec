import importlib
import os


def load_controllers():
    """
    Load controllers from controllers/ directory
    """

    controllers = {}
    for filename in os.listdir("controllers"):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module = importlib.import_module(f"controllers.{module_name}")
            module_name = [name.capitalize() for name in module_name.split("_")]
            class_name = f"{''.join(module_name)}Controller"
            controllers[class_name] = getattr(module, class_name)

    return controllers