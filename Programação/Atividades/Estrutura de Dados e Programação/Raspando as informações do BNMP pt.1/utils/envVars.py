from fake_useragent import UserAgent

fieldnames = ['id', 'dataExpedicao', 'dataCriacao', 'numeroPeca', 'tipoPeca_id', 'tipoPeca_descricao', 'status_id',
              'status_descricao', 'numeroProcesso', 'numeroPecaAnterior', 'pessoa_id', 'pessoa_enderecos',
              'pessoa_outrasAlcunhas', 'pessoa_outrosNomes', 'pessoa_nomePai', 'pessoa_nomeMae',
              'pessoa_dataNascimento', 'pessoa_foto', 'pessoa_telefone', 'pessoa_documento', 'pessoa_sinaisMarcas',
              'pessoa_numeroIndividuo', 'pessoa_dadosGeraisPessoa_paisNascimento_nome',
              'pessoa_dadosGeraisPessoa_paisNascimento_id', 'pessoa_dadosGeraisPessoa_naturalidade_id',
              'pessoa_dadosGeraisPessoa_naturalidade_nome', 'pessoa_dadosGeraisPessoa_sexo_id',
              'pessoa_dadosGeraisPessoa_sexo_descricao', 'pessoa_dadosGeraisPessoa_profissao', 'orgaoUsuarioCriador_id',
              'orgaoUsuarioCriador_nome', 'orgaoUsuarioCriador_municipio_id', 'orgaoUsuarioCriador_municipio_nome',
              'orgaoUsuarioCriador_municipio_uf_id', 'orgaoUsuarioCriador_municipio_uf_nome',
              'orgaoUsuarioCriador_municipio_uf_sigla', 'orgaoUsuarioCriador_municipio_codIbge',
              'orgaoUsuarioCriador_municipio_flgDistrito', 'orgaoUsuarioCriador_municipio_idCorporativo',
              'orgaoUsuarioCriador_orgaoTribunal_id', 'orgaoUsuarioCriador_orgaoTribunal_nome',
              'orgaoUsuarioCriador_orgaoTribunal_ativoFormatado', 'orgaoUsuarioCriador_ativoFormatado',
              'orgaoJudiciario_id', 'orgaoJudiciario_nome', 'orgaoJudiciario_municipio_id',
              'orgaoJudiciario_municipio_nome', 'orgaoJudiciario_municipio_uf_id', 'orgaoJudiciario_municipio_uf_nome',
              'orgaoJudiciario_municipio_uf_sigla', 'orgaoJudiciario_municipio_codIbge',
              'orgaoJudiciario_municipio_flgDistrito', 'orgaoJudiciario_municipio_idCorporativo',
              'orgaoJudiciario_orgaoTribunal_id', 'orgaoJudiciario_orgaoTribunal_nome',
              'orgaoJudiciario_orgaoTribunal_ativoFormatado', 'orgaoJudiciario_ativoFormatado', 'sinteseDecisao',
              'magistrado', 'dataValidade', 'especiePrisao', 'cumprimento', 'observacao', 'localOcorrencia',
              'tempoPena', 'tempoPenaAno', 'tempoPenaMes', 'tempoPenaDia', 'regimePrisional', 'recaptura',
              'outrasPecas', 'tipificacaoPenal', 'pessoa_dadosGeraisPessoa_naturalidade_uf_id',
              'pessoa_dadosGeraisPessoa_naturalidade_uf_nome', 'pessoa_dadosGeraisPessoa_naturalidade_uf_sigla']

ua = UserAgent()
cookie = "portalbnmp=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJndWVzdF9wb3J0YWxibm1wIiwiYXV0aCI6IlJPTEVfQU5PTllNT1VTIiwiZXhwIjoxNjI5MjQ2MDEzfQ.nwmD_Do48uHjfm1CmmxvrtETeve7Ve04LnlEfcn5KDri0gq3A_imK7Lu9LvL3fIlj09JM77mEg8p3IJRfkh9Tw"
headers = {
    'authority': 'portalbnmp.cnj.jus.br',
    'accept': 'application/json',
    'user-agent': ua.random,
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://portalbnmp.cnj.jus.br',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://portalbnmp.cnj.jus.br/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': cookie,
}
