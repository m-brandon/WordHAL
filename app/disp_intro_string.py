import app.config_params as cfg


def main(curr_module_string):
    print(f"WordHAL v{cfg.ver_maj}.{cfg.ver_min}")
    print(curr_module_string)
    print("-"*30)
