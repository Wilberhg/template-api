import constants as const
from ..model.banco_sqlite import Banco

def get_cpf(tel):
    obj = Banco()
    cpf = obj.do_select(const.CPF_QUERY.format(tel=tel))
    return cpf