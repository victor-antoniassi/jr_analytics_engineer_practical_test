# Teste prático de contratação de Analytics Engineer Júnior | Empresa de E-Commerce

## Aviso

Este repositório contém a minha solução para o teste prático realizado durante um processo seletivo para o cargo de **Analytics Engineer Júnior** em uma empresa de e-commerce. Algumas partes do texto original da proposta foram omitidas ou modificadas para manter a confidencialidade do processo seletivo.

## Resumo da proposta do teste técnico (leia a proposta completa [aqui](proposta_desafio_tecnico.md))

Este é um desafio prático para o processo seletivo de Analytics Engineer Júnior em uma empresa de e-commerce. O cenário envolve o planejamento para o início do ano letivo escolar na cidade de São Paulo, com foco na venda de produtos do setor de materiais escolares. O objetivo do desafio é desenvolver um projeto simplificado de preparação de dados para entregar um banco de dados que será utilizado em análises e outros projetos durante o planejamento de vendas. Os dados devem ser disponibilizados em uma estrutura e qualidade semelhantes à camada Silver da Arquitetura Medallion. Os dados para o desafio incluem informações agregadas de estudantes e detalhes sobre as escolas. Importante: utilize apenas os dados de perfis de alunos e escolas da cidade de São Paulo referentes aos anos de 2021 e 2022.

## Etapas da Preparação de Dados

1. Análise inicial da qualidade dos dados e das estruturas dos arquivos .csv utilizando o Python + Pandas e Google Sheets.
2. Desenvolvimento de um [script](data_preparation/scripts/compare_delimited_file_headers) em Python para comparar os cabeçalhos dos arquivos (educandos e escolas) com cabeçalhos corretos baseados nos respectivos dicionários de dados.
3. Correção manual dos problemas identificados utilizando o Google Sheets (correção nos nomes dos campos, mudança de posições das colunas para posições corretas e exclusão de colunas totalmente vazias ou que não existem no dicionários de dados).
4. Desenvolvimento de um [script](data_preparation/scripts/datasets_to_sqlite) em Python que aplica algumas etapas de preparação/limpeza nos dados, necessário para os dados serem armazenados de forma correta no banco de dados SQLite.
5. Desenvolvimento de um [script](data_preparation/scripts/datasets_to_sqlite) em Python que cria o [banco de dados SQLite](sqlite_db) e que faz a ingestão de dados dos arquivos para as tabelas 'educandos' (dados dos perfis de alunos matriculados nos anos de 2021 e 2022), 'escolas' (dados sobre as escolas municipais referente aos anos de 2021 e 2022) e 'escolas_educandos' (tabela que faz a junção das tabelas 'escolas' e 'educandos').

## Sugestões de Análises

1. **Análise Demográfica**: Analisar a distribuição dos alunos com base em características demográficas, como raça, gênero e idade. Isso pode ajudar a empresa a entender melhor a diversidade de seus clientes potenciais e a desenvolver produtos que atendam às necessidades de diferentes grupos demográficos.

2. **Análise de Necessidades Educacionais Especiais**: Analisar a distribuição de alunos com necessidades educacionais especiais. Isso pode ajudar a empresa a desenvolver produtos específicos para esse segmento, o que pode ser uma consideração importante para muitos pais.

3. **Análise de Tendências**: Comparar os dados de 2021 e 2022 para identificar tendências. Isso pode ajudar a empresa a prever a demanda futura e a se preparar adequadamente para atender às necessidades dos pais.

4. **Análise de Cluster**: Agrupar escolas com base em características semelhantes (como localização e tamanho) e analisar as diferenças nas tendências de vendas entre os diferentes grupos. Isso pode ajudar a empresa a entender melhor as necessidades específicas de diferentes comunidades escolares.

5. **Análise de Segmentação de Mercado**: Identificar segmentos de mercado com base nas características dos alunos e das escolas. Isso pode ajudar a empresa a personalizar seus produtos e estratégias de marketing para diferentes segmentos, permitindo que ela atenda melhor às necessidades dos pais.