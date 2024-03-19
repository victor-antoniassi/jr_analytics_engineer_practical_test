# Desafio prático | Projeto de Preparação de Dados | Analytics Engineer Jr

Prezado(a) candidato(a),

Seja bem-vindo(a) à fase do desafio prático para o processo seletivo para o cargo de Analytics Engineer Júnior em nossa empresa de e-commerce! Neste desafio, você terá a oportunidade de aplicar suas habilidades de Analytics Engineer em um cenário de um projeto de preparação de dados.

## Cenário
Imagine que nossa empresa está em pleno planejamento para o início do ano letivo escolar na cidade de São Paulo. Nosso foco é a venda de produtos do setor de materiais escolares. Para garantir o sucesso dessa operação, precisamos de dados bem preparados e estruturados.

## Objetivo do desafio
Desenvolver um projeto simplificado de preparação de dados em que o objetivo final é entregar um banco de dados que será utilizado em análises e outros projetos por analistas de dados, analistas de negócios, cientistas de dados e outros stakeholders durante o planejamento de vendas. Seu foco é disponibilizar os dados em uma estrutura e qualidade semelhantes à camada Silver da Arquitetura Medallion.

## Dados para utilização no desafio

### Perfis Agregados de Estudantes
Esses dados contêm informações sobre estudantes, agrupados por série, turno, sexo, idade, necessidades educacionais especiais e raça/cor. Cada registro nos dados dos educandos representa um número de alunos por perfil.
Acesse os dados dos perfis dos estudantes [aqui](http://dados.prefeitura.sp.gov.br/dataset/perfil-dos-educandos-cor-raca-idade-sexo-necessidades-educacionais-especiais).
### Informações sobre Escolas
Esses dados fornecem detalhes sobre as escolas, incluindo localização, tipo de escola e outras informações relevantes.
Acesse os dados das escolas [aqui](http://dados.prefeitura.sp.gov.br/dataset/cadastro-de-escolas-municipais-conveniadas-e-privadas).

#### *Aviso Importante*
Utilize apenas os dados de perfis de alunos e escolas da cidade de São Paulo referentes aos anos de 2021 e 2022. A seleção desses anos específicos deve-se ao fato de que os dados de 2023 dos educandos não está incluído o campo raça, um atributo que consideramos relevante para esse tipo de projeto. Embora estejamos atualmente no ano de 2024, o cenário foi projetado para refletir as condições e desafios que uma empresa poderia enfrentar ao planejar suas operações para o ano seguinte, com base nos dados disponíveis dos anos anteriores.


## Instruções:

- Elabore scripts ou notebooks empregando Python e SQL (sinta-se à vontade para usar as bibliotecas de sua preferência).
- Faça uso extensivo de comentários em seus códigos.
- Adote o princípio KISS "Keep it simple, stupid!" (em português: Mantenha simples, estúpido!) na elaboração do seu projeto.
- A simplicidade é um elemento-chave no projeto. Em nossa empresa, damos prioridade a processos simplificados e eficazes, e essa filosofia se estende aos nossos processos seletivos. Assim como vocês, candidatos, não apreciamos processos seletivos prolongados, especialmente para uma posição de nível júnior.
- Em resumo, nosso objetivo é avaliar suas habilidades atuais em: solucionar problemas utilizando SQL e o ecossistema Python, escolher quais técnicas e processos aplicar na preparação de dados, planejar, priorizar e executar tarefas, e na organização e documentação do seu trabalho.
- Aconselhamos que não se preocupe em empregar ferramentas e bibliotecas destinadas à automatização do processamento de dados (como ETL e orquestração).  Além disso, sugerimos não replicar a estrutura da Arquitetura Medallion, queremos que você apenas utilize de inspiração o conceito da camada Silver.
- Utilize um banco de dados SQLite como repositório final dos dados do projeto.