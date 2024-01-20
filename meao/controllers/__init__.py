import importlib
import os


def load_controllers():
    """
    Load controllers from controllers/ directory
    """

    controllers = {}
    for filename in os.listdir("controllers"):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3] # Remove ".py" extension and obtain module name
            module = importlib.import_module(f"controllers.{module_name}")
            class_name = f"{module_name.capitalize()}Controller"
            controllers[class_name] = getattr(module, class_name)

    return controllers
