from .. import misc
from .._typing import AbstractQueryAPI
from . import eudict, vcom_funny, youdao

apis: dict[str, type[AbstractQueryAPI]] = {
    youdao.API.name: youdao.API,
    eudict.API.name: eudict.API,
    vcom_funny.API.name: vcom_funny.API,
}

default_api = youdao.API


def load_usr_mod():
    "load user modules in user_files/queryApi"
    for mod in misc.load_all_modules('..user_files.queryApi', __package__):
        if hasattr(mod, 'API') and isinstance(mod.API, type) and issubclass(mod.API, AbstractQueryAPI):
            apis.setdefault(mod.API.name, mod.API)
