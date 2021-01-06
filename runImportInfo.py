import importInfo

print('paths:', importInfo.get_paths())

test_dict = importInfo.ModuleOrigins(["tokenize", "sys", "importlib", "pyspark"])
print('modules:', test_dict.get_modules(True))
print('origins:', test_dict.get_origins(False))

test_dict = importInfo.ModuleOrigins()
print('modules:', test_dict.get_modules())
print('origins:', test_dict.get_origins(False))
