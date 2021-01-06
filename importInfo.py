import sys
import pkgutil
import importlib.util


def get_paths(p_reverse=None):
    path_list = sys.path
    if p_reverse is not None:
        path_list.sort(reverse=bool(p_reverse))
    return path_list


class ModuleOrigins:
    def __init__(self, p_module_list=[]):
        self.module_dict = {}
        module_set = set()
        self.module_list = []
        if p_module_list:
            self.module_list = p_module_list
        else:
            for x in pkgutil.iter_modules(path=sys.path):
                module_set.add(x[1])
            self.module_list = list(module_set)

        for module in self.module_list:
            self.module_dict[module] = importlib.util.find_spec(module).origin

    def get_origins(self, p_reverse=None):
        module_dict = self.module_dict
        if p_reverse is not None:
            module_dict = dict((dkey, self.module_dict[dkey])
                               for dkey in sorted(self.module_dict.keys(), reverse=bool(p_reverse)))
        return module_dict

    def get_modules(self, p_reverse=None):
        module_list = self.module_list
        if p_reverse is not None:
            module_list.sort(reverse=bool(p_reverse))
        return module_list
