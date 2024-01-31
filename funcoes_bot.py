def query_renovacao_status_type(id_old, id_new, id_user, status_antg, type_antg):
  tabela_renew_sga = 'operational_policy_renew'
  tabela_operational_policy_sga = 'operational_policy'
  colum_status =  'status'
  column_solicitation = 'id_enum_type_solicitation'
  query = f"""
INSERT INTO {tabela_renew_sga} (id_policy_old, id_policy_new, id_user, status, dt_create)
VALUES ({id_old}, {id_new}, {id_user}, 4, NOW());
-- ROLLBACK DELETE FROM {tabela_renew_sga} WHERE id_policy_old = {id_old} AND id_policy_new = {id_new} AND id_user = {id_user} AND status = 4;

UPDATE {tabela_operational_policy_sga} SET {colum_status} = 18 WHERE id = {id_old};
-- ROLLBACK UPDATE {tabela_operational_policy_sga} SET {colum_status} = {status_antg} WHERE id = {id_old};

UPDATE {tabela_operational_policy_sga} SET {column_solicitation} = 108 WHERE id = {id_new};
-- ROLLBACK UPDATE {tabela_operational_policy_sga} SET {column_solicitation} = {type_antg} WHERE id = {id_new};"""
  return query[1:]

def query_renovacao_status(id_old, id_new, id_user, status_antg):
  tabela_renew_sga = 'operational_policy_renew'
  tabela_operational_policy_sga = 'operational_policy'
  colum_status =  'status'
  column_solicitation = 'id_enum_type_solicitation'
  query = f"""
INSERT INTO {tabela_renew_sga} (id_policy_old, id_policy_new, id_user, status, dt_create)
VALUES ({id_old}, {id_new}, {id_user}, 4, NOW());
-- ROLLBACK DELETE FROM {tabela_renew_sga} WHERE id_policy_old = {id_old} AND id_policy_new = {id_new} AND id_user = {id_user} AND status = 4;

UPDATE {tabela_operational_policy_sga} SET {colum_status} = 18 WHERE id = {id_old};
-- ROLLBACK UPDATE {tabela_operational_policy_sga} SET {colum_status} = {status_antg} WHERE id = {id_old};"""
  return query[1:]

def query_renovacao_type(id_old, id_new, id_user, type_antg):
  tabela_renew_sga = 'operational_policy_renew'
  tabela_operational_policy_sga = 'operational_policy'
  colum_status =  'status'
  column_solicitation = 'id_enum_type_solicitation'
  query = f"""
INSERT INTO {tabela_renew_sga} (id_policy_old, id_policy_new, id_user, status, dt_create)
VALUES ({id_old}, {id_new}, {id_user}, 4, NOW());
-- ROLLBACK DELETE FROM {tabela_renew_sga} WHERE id_policy_old = {id_old} AND id_policy_new = {id_new} AND id_user = {id_user} AND status = 4;

UPDATE {tabela_operational_policy_sga} SET {column_solicitation} = 108 WHERE id = {id_new};
-- ROLLBACK UPDATE {tabela_operational_policy_sga} SET {column_solicitation} = {type_antg} WHERE id = {id_new};"""
  return query[1:]

def query_renovacao(id_old, id_new, id_user):
  tabela_renew_sga = 'operational_policy_renew'
  tabela_operational_policy_sga = 'operational_policy'
  colum_status =  'status'
  column_solicitation = 'id_enum_type_solicitation'
  query = f"""
INSERT INTO {tabela_renew_sga} (id_policy_old, id_policy_new, id_user, status, dt_create)
VALUES ({id_old}, {id_new}, {id_user}, 4, NOW());
-- ROLLBACK DELETE FROM {tabela_renew_sga} WHERE id_policy_old = {id_old} AND id_policy_new = {id_new} AND id_user = {id_user} AND status = 4;"""
  return query[1:]

def trata_branch_name(branch_name):
  tratando_caracteres = {'ç' : 'c', 'á' : 'a', 'à' : 'a', 'â' : 'a', 'ã' : 'a', 'é' : 'e', 'ê' : 'e', 'í' : 'i', 'ó' : 'o', 'ô' : 'o', 'õ' : 'o', 'ò' : 'o', ' ' : '-', 'ú' : 'u', ':' : '-', '\'' : ''}
  branch_name = branch_name.lower()

  for caracter, letra in tratando_caracteres.items():
    if caracter in branch_name:
      branch_name = branch_name.replace(caracter, letra)
  return branch_name

def trata_head_query_title(title):
  tratando_caracteres = {'ç' : 'c', 'á' : 'a', 'à' : 'a', 'â' : 'a', 'ã' : 'a', 'é' : 'e', 'ê' : 'e', 'í' : 'i', 'ó' : 'o', 'ô' : 'o', 'õ' : 'o', 'ò' : 'o', 'ú' : 'u', ':' : ' ', '\'' : ''}
  title = title.lower()

  for caracter, letra in tratando_caracteres.items():
    if caracter in title:
      title = title.replace(caracter, letra)
  return title