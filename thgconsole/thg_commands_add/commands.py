def thg_command_use(self, module_path, *args, **kwargs):
    if module_path.startswith("extra_"):
        module_path = pythonize_path(module_path)
    else:
        module_path = pythonize_path(module_path)
        module_path = ".".join(("thgconsole", "modules", module_path))
    # module_path, _, exploit_name = module_path.rpartition('.')
    try:
        self.current_module = import_exploit(module_path)()
    except THGtException as err:
        print_error(str(err))