# Sistema-ONG-AVASP
Projeto do sistema para a ONG Associação Verbo Amar

1 INTRODUÇÃO
  1.1 Objetivo
    1.1.1 Objetivo Geral
    1.1.2 Objetivos Específicos
  1.2 Justificativa
  1.3 Organização do Trabalho
2 LEVANTAMENTO DE REQUISITOS
  2.1 Contextualização
  2.2 Descrição
    2.2.1 Requisitos Funcionais
    2.2.2 Requisitos não funcionais
  2.3 Arquitetura
  2.4Cronograma

1.INTRODUÇÃO
  1.1.Objetivo
    1.1.1.Objetivo Geral - Objetivo geral - Agilidade nos processos de prestação de
contas e gestão eficiente com foco na captação de recursos (voluntariado e
sustentabilidade) e gestão financeira e de projetos.
1.1.2 Objetivos Específicos - Automatizar o cadastro de beneficiários,
facilitando acompanhamento e avaliação das atividades realizadas; Implementar um
módulo de captação de recursos online, permitindo doações e parcerias de forma
eficiente; Facilitar a gestão financeira da organização, incluindo: controle orçamentário
de projetos, geração de relatórios financeiros e prestação de contas; Fornecer
indicadores e comprovantes quantitativos de metas e status, incluindo plano de
marketing; Oferecer funcionalidades para a organização de documentos; Permitir o
registro e acompanhamento de doadores, otimizando o engajamento da comunidade na
causa;
  1.2 Justificativa - A motivação do projeto vem da vontade de impactar
positivamente a sociedade, facilitando o gerenciamento dessas informações, teremos
um maior controle da Associação Verbo Amar (AVA). Assim, ajudando e impactando
positivamente todas as áreas e processos que os funcionários têm, até combater o
analfabetismo funcional e digital.
  1.3 Organização do Trabalho - O trabalho será desenvolvido em etapas, da
etapa 1 à etapa 7. Sendo elas - 
  Etapa 1: Escolher a ONG e elaborar os requisitos;
  Etapa 2: Apresentação da introdução do projeto e fazer o levantamento de requisitos;
  Etapa 3: Criação do modelo conceitual;
  Etapa 4: Criação do modelo lógico;
  Etapa 5: Inicialização do desenvolvimento do sistema;
  Etapa 6: Finalização do Sistema
  Etapa 7: Entrega e Apresentação do sistema;

2.0 LEVANTAMENTO DE REQUISITOS
  2.1 Contextualização
  Entidades:
    1. Cliente/Organização
    - Atributos: Nome da Organização, Responsável, E-mail do Responsável, Telefone do
    Responsável.
    2. Projeto
    - Atributos: Breve Histórico, Projetos Principais.
    3. Público-Alvo
    - Atributos: Quem você atende, Importância na Comunidade.
4. Detalhes do Projeto
- Atributos: Tipo de Atendimento, Quantidade de Beneficiários, Objetivos do Sistema,
Material Disponível, Imagem a ser Transmitida, Treinamento.
Relacionamentos:
1. Participação
  - A Organização participa de projetos.
  - Um projeto pode envolver várias organizações.
2. Atendimento
  - Um projeto atende um público-alvo.
  - Um público-alvo pode ser atendido por vários projetos.
3. Gestão de Recursos
  - Um projeto requer gestão de recursos.
  - A Organização realiza a gestão de recursos para seus projetos.
4. Treinamento
  - A equipe de gestão recebe treinamento para utilização do software.
  - O treinamento é fornecido pela Organização.
  2.2 Descrição:
    2.2.1 Requisitos Funcionais :
      ● Gestão Financeira Eficiente:
Permitir o controle orçamentário detalhado de projetos, acompanhando
receitas e despesas relacionadas a cada atividade da organização.
Gerar relatórios financeiros automatizados que detalham a utilização
dos recursos e o status financeiro da organização.
Facilitar a prestação de contas, fornecendo informações claras e
transparentes sobre o uso dos recursos financeiros.

      ● Cadastro Automatizado de Beneficiários:
O sistema deve permitir o cadastro automatizado de novos
beneficiários, capturando informações relevantes para facilitar o
acompanhamento e a avaliação das atividades realizadas.
Deve fornecer formulários intuitivos e personalizáveis para coletar
dados dos beneficiários.

      ● Módulo de Captação de Recursos Online:
Implementar um módulo online para facilitar doações e parcerias,
permitindo que os doadores façam contribuições de forma eficiente e segura.
Deve incluir opções de pagamento online e integração com plataformas
de pagamento reconhecidas.

      ● Indicadores de Desempenho e Metas:
Fornecer indicadores quantitativos e comprovantes de metas
alcançadas, permitindo avaliar o progresso e o impacto das atividades da
organização.
Incluir um plano de marketing para promover as atividades da
organização e atrair mais doadores e parceiros.

      ● Organização de Documentos:
Oferecer funcionalidades para organização eficiente de documentos,
permitindo o armazenamento, compartilhamento e recuperação fácil de
informações importantes para a organização.
● Registro e Acompanhamento de Doadores:
Permitir o registro detalhado de doadores, incluindo informações sobre
doações anteriores, preferências de comunicação e histórico de engajamento.
Facilitar o acompanhamento das interações com os doadores, otimizando o
envolvimento da comunidade na causa da organização.

      2.2.2 Requisitos não funcionais :
      ● Desempenho e Escalabilidade:
O sistema deve ser capaz de lidar com um grande volume de dados e
usuários simultâneos sem comprometer o desempenho. Deve ser
escalável para acompanhar o crescimento da organização e o aumento
na demanda por serviços.

      ● Disponibilidade:
O sistema deve estar disponível continuamente, com um tempo de
inatividade mínimo planejado para manutenção. Deve ser resiliente a
falhas e ter mecanismos de recuperação de desastres para garantir a
continuidade das operações.

      ● Usabilidade e Acessibilidade:
A interface do usuário deve ser intuitiva e fácil de usar, garantindo uma
experiência positiva para os usuários de diferentes níveis de habilidade.
Além disso, o sistema deve ser acessível para pessoas com deficiências,
seguindo as diretrizes de acessibilidade da Web.

      ● Compatibilidade:
O sistema deve ser compatível com uma variedade de dispositivos e
navegadores para garantir uma experiência consistente para todos os
usuários. Além disso, deve ser capaz de integrar-se com outros sistemas
utilizados pela AVA-SP, facilitando a troca de dados e informações.

      ● Manutenção e Suporte:
O sistema deve ser fácil de manter e atualizar, com documentação clara e
procedimentos de suporte disponíveis para os administradores. Deve ter
um processo eficiente para aplicar patches de segurança e correções de
bugs.

      ● Confiabilidade:
O sistema deve ser confiável, evitando erros e falhas que possam
comprometer a integridade dos dados ou interromper as operações da
organização. Deve ter mecanismos de monitoramento para detectar e
responder rapidamente a problemas técnicos.

    ● Performance:
O sistema deve ser responsivo e rápido, garantindo tempos de resposta
adequados mesmo durante períodos de alta demanda. Deve ser
otimizado para minimizar o tempo de carregamento de páginas e
processos.

      ● Localização e Internacionalização:
O sistema deve suportar múltiplos idiomas e ser adaptável a diferentes
contextos culturais, garantindo uma experiência inclusiva para todos os
usuários, independentemente da sua localização geográfica.

    ● Documentação e Treinamento:
Deve haver documentação abrangente disponível para usuários e
administradores, incluindo manuais de usuário, guias de treinamento e FAQs.
Treinamento adequado deve ser fornecido para garantir que os usuários possam
utilizar todas as funcionalidades do sistema de forma eficaz.

  2.3 Arquitetura
Python é uma linguagem de programação de alto nível, interpretada de script,
imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
Na ciência da computação, a Tkinter é a interface padrão da linguagem de
programação Python

Flask é um pequeno framework web escrito em Python. É classificado como um
microframework porque não requer ferramentas ou bibliotecas particulares,
mantendo um núcleo simples, porém, extensível.

O MySQL é um sistema de gerenciamento de banco de dados, que utiliza a
linguagem SQL como interface.

  2.4.Cronograma

![image](https://github.com/HugoHlebetz/Sistema-ONG-AVASP/assets/132224339/d03dcd5e-b03c-4c67-8174-0d4929a4a7e2)

3.0.Análise

3.1Diagrama de Classe Conceitual 

![image](https://github.com/HugoHlebetz/Sistema-ONG-AVASP/assets/132224339/1228054c-edef-4c1c-afe1-a0792cce9ff9)

3.2.Diagrama de Caso de Uso

![image](https://github.com/HugoHlebetz/Sistema-ONG-AVASP/assets/132224339/2028e5c1-768e-4e69-83a4-9e829cb72d64)

3.3 Lista de Eventos
	3.3.1.Descrição de Caso de uso
		3.3.1.2.Caso de Uso: Exemplo
	Caso de uso número 1 - Cadastro de Beneficiários no Sistema
		3.3.1.3.Descrição

Nome do Caso de Uso: Cadastro de Beneficiários

Ator Principal: Funcionário da ONG

Objetivo: Garantir que os beneficiários da ONG sejam cadastrados de maneira precisa e completa no sistema, permitindo a organização e acompanhamento das assistências oferecidas.
		
		3.3.1.4.Pré Condições
Pré condição número um: O usuário do sistema deve garantir que tem as permissões necessárias para realizar o cadastro no sistema;
		
		3.3.1.5.Fluxo Básico
			1- Funcionário escolhe opção de cadastro de beneficiários;
			2- Funcionário insere os dados do beneficiário;
			3- Sistema valida os dados do beneficiário;
			4- Sistema retorna os dados do beneficiário;
			5- Funcionário confirma o cadastro do beneficiário;
			6- Funcionário encerra caso de uso;
		3.3.1.6.Pós Condições
Pós condição número um: O usuário do sistema deve garantir que o cadastro foi realizado com sucesso;
Pós condição número dois: O sistema deverá atualizar os cadastros já existentes e adicionar o novo cadastro;
Pós condição número três: Todos os dados do beneficiário estão disponíveis para consulta e gerenciamento;
		3.3.1.7.Fluxos Alternativos
Cadastro Incompleto:

Se o funcionário não possui todas as informações necessárias no momento do cadastro, ele pode salvar o cadastro como "Rascunho".
O Sistema permite a edição e complementação dos dados posteriormente.
O Funcionário é notificado para completar o cadastro em um prazo específico.
Erro no Cadastro:

Se o Sistema detecta dados incorretos ou incompletos, exibe uma mensagem de erro ao Funcionário.
O funcionário corrige os dados e tenta salvar novamente.

  3.3.1 Descrição de Caso de Uso Número 2
    3.3.1.2 Caso de Uso: Exemplo
 Caso de Uso Número 2: Consulta de Documentos e Relatórios
    3.3.1.3 Descrição

Nome do Caso de Uso: Consulta de Documentos e Relatórios

Ator Principal: Administrador

Objetivo: Permitir que o administrador consulte documentos e relatórios sobre os beneficiários e atividades da ONG de maneira eficiente e precisa.

    3.3.1.4 Pré-condições
Pré-condição Número Um: O administrador deve ter uma conta e permissões adequadas no Sistema de Gerenciamento de Beneficiários.
Pré-condição Número Dois: O Sistema de Gerenciamento de Beneficiários deve estar operacional.
    3.3.1.5.Fluxo Básico
1- Administrador escolhe a opção de consulta de documentos e relatórios;
2- Administrador insere os parâmetros de busca (por exemplo, nome do beneficiário, data de cadastro, tipo de documento);
3- Sistema executa a busca com base nos parâmetros fornecidos;
4- Sistema exibe uma lista de documentos e relatórios correspondentes;
5- Administrador seleciona um documento ou relatório específico para visualização;
6- Sistema exibe o conteúdo completo do documento ou relatório selecionado;
7- Administrador encerra caso de uso;

    3.3.1.6.Pós-condições
Pós-condição Número Um: Os documentos e relatórios consultados estão disponíveis para visualização e download pelo administrador.
Pós-condição Número Dois: O histórico de consultas pode ser registrado no sistema para auditoria e referência futura.
Pós-condição Número Três: O sistema mantém a integridade e a segurança dos dados acessados.
    3.3.1.7 Fluxos Alternativos
Nenhum Documento Encontrado:

Se nenhum documento ou relatório correspondente aos parâmetros de busca for encontrado, o sistema exibe uma mensagem informando que não há resultados correspondentes.
O administrador pode modificar os parâmetros de busca e tentar novamente.
Erro no Sistema:

Se ocorrer um erro no sistema durante a consulta, o sistema exibe uma mensagem de erro.
O administrador pode tentar realizar a consulta novamente ou entrar em contato com o suporte técnico.
Permissões Insuficientes:

Se o administrador não tiver permissões adequadas para acessar determinados documentos ou relatórios, o sistema exibe uma mensagem informando sobre a falta de permissão.
O administrador pode solicitar acesso ao administrador do sistema ou ajustar os parâmetros de busca para acessar documentos permitidos.

Caso de uso número 3 - Atualização de dados		
  3.3.1.3.Descrição
Nome do Caso de Uso: Atualização de dados

Ator Principal: Funcionário da ONG

Objetivo: Garantir que todos os dados presentes no banco possam ser atualizados ou modificados pelo administrador.

		
		3.3.1.4.Pré Condições
Pré condição número um: O usuário do sistema deve garantir que tem as permissões necessárias para realizar a atualização no sistema;
		
		3.3.1.5.Fluxo Básico
      1- Funcionário escolhe o que desejar atualizar;
			2- Funcionário insere os novos dados no banco;
			3- Sistema valida os novos dados;
			4- Sistema retorna os dados atualizados;
			5- Funcionário confirma a atualização;
			6- Funcionário encerra caso de uso;
		3.3.1.6.Pós Condições
Pós condição número um: O usuário do sistema deve verificar se o processo foi realizado com sucesso;
Pós condição número dois: O sistema deverá atualizar os já existentes
;
Pós condição número três: Todos os dados atualizados estão disponíveis para consulta e gerenciamento;
		3.3.1.7.Fluxos Alternativos
Atualização Incompletoa:

Se o funcionário não possuir todas as informações necessárias no momento da atualização , ele pode salvar-la como "Rascunho".
O Sistema permite a edição e complementação dos dados posteriormente.
Erro na Atualização :

Se o Sistema detecta dados incorretos ou incompletos, exibe uma mensagem de erro ao Funcionário.
O funcionário corrige os dados e tenta salvar novamente.
 
	
Caso de Uso Número 4: Captação de Recursos Online
    3.3.1.3 Descrição

Nome do Caso de Uso: Captação de Recursos Online

Ator Principal: Usuário
Objetivo: Permitir que os usuários realizem doações e contribuições financeiras para a ONG de forma segura e conveniente pela internet.

    3.3.1.4 Pré-condições:

Pré-condição Número Um: O usuário deve ter acesso a um dispositivo com conexão à internet.
Pré-condição Número Dois: O sistema de captação de recursos online da ONG deve estar operacional.
    3.3.1.5 Fluxo Básico:

1- Usuário acessa a plataforma de captação de recursos online da ONG;
2- Usuário seleciona a opção de doação ou contribuição financeira;
3- Usuário insere o valor da doação e suas informações de pagamento;
4- Sistema processa o pagamento de forma segura;
5- Sistema confirma a transação bem-sucedida e fornece um recibo ao usuário;
6- Usuário encerra o caso de uso.

    3.3.1.6 Pós-condições:

Pós-condição Número Um: O sistema registra a transação de doação ou contribuição financeira.

Pós-condição Número Dois: O valor da doação é adicionado aos fundos da ONG para uso em atividades e projetos.

Pós-condição Número Três: O recibo da transação é enviado ao e-mail do usuário para referência futura.

    3.3.1.7 Fluxos Alternativos:

Erro no Processamento de Pagamento:

Se ocorrer um erro durante o processamento do pagamento, o sistema exibe uma mensagem de erro ao usuário.

O usuário pode tentar novamente ou entrar em contato com o suporte técnico para assistência.

Caso de Uso Número 5: Papel de Transparência
    3.3.1.3 Descrição

Nome do Caso de Uso: Papel de Transparência

Ator Principal: Administrador de Relacionamento

Objetivo: Fornecer aos stakeholders e à comunidade em geral informações transparentes sobre as atividades, finanças e impacto da ONG.
    3.3.1.4 Pré-condições:

Pré-condição Número Um: O administrador de relacionamento deve ter acesso às informações relevantes da ONG.

Pré-condição Número Dois: O sistema de gerenciamento de informações da ONG deve estar atualizado.

    3.3.1.5 Fluxo Básico:

1- Administrador de relacionamento acessa o sistema de gerenciamento de informações da ONG;
2- Administrador seleciona a opção de visualização de informações de transparência;
3- Sistema exibe relatórios, dados financeiros e outras informações relevantes sobre as atividades da ONG;
4- Administrador verifica e analisa as informações apresentadas;
5- Administrador encerra o caso de uso.


    3.3.1.6 Pós-condições:

Pós-condição Número Um: As informações de transparência são acessíveis aos stakeholders e à comunidade.

Pós-condição Número Dois: A reputação e credibilidade da ONG são fortalecidas por meio da transparência nas operações.

Pós-condição Número Três: O sistema registra o acesso e visualização das informações de transparência para auditoria e referência futura.

    3.3.1.7 Fluxos Alternativos:

Nenhuma Informação Disponível:

Se não houver informações disponíveis para visualização, o sistema exibe uma mensagem informativa.
O administrador pode revisar as políticas de divulgação de informações ou atualizar os dados no sistema.








