# Fasthunter Optimizer


## Descrição

Este é um sistema de otimização de computadores Windows, desenvolvido em Python utilizando a biblioteca Tkinter para criar uma interface amigável. O software aplica técnicas eficazes de limpeza e otimização nativa do sistema operacional, permitindo que os usuários melhorem o desempenho geral de seus dispositivos de forma rápida e segura.

## Funcionalidades

O software executa as seguintes técnicas de otimização:

### 1. Remoção de Arquivos Temporários do Sistema

- **Descrição**: Remove arquivos temporários gerados por aplicativos e processos do sistema que não são mais necessários.
- **Importância**: Libera espaço no disco, reduz a fragmentação e pode melhorar a velocidade de leitura/escrita.

### 2. Habilitação do Desempenho Máximo no Plano de Energia

- **Descrição**: Altera o plano de energia para o máximo desempenho, priorizando a utilização dos recursos de hardware para tarefas intensivas.
- **Importância**: Útil para melhorar o desempenho em aplicações e jogos que demandam alto processamento.

### 3. Liberação de Cache e Busca de Informações DNS Atualizadas

- **Descrição**: Limpa o cache DNS, garantindo que o sistema obtenha informações de DNS atualizadas.
- **Importância**: Resolve problemas de conexão de rede e melhora a navegação na internet.

### 4. Configurar o provedor de controle de congestionamento como Compound TCP

- **Descrição**: O Compound TCP (CTCP) é uma tecnologia desenvolvida pela Microsoft para otimizar a transmissão de dados em redes de alta largura de banda e alta latência.
- **Importância**: Melhor aproveitamento da largura de banda disponível.
- **Pontos de Atenção**: Se o desempenho de aplicativos em tempo real for crítico, observe o comportamento antes e depois de habilitar o CTCP.
- **Quando usar essa configuração**:
    Sim: Conexões de alta largura de banda e alta latência (ex.: transferências de arquivos em servidores internacionais ou redes de alta capacidade).
    Talvez: Redes domésticas rápidas (ex.: fibra óptica de 500 Mbps ou superior). Os ganhos podem ser limitados.
    Não: Redes lentas, antigas ou sensíveis a latência (ex.: ADSL, 3G/4G, ou jogos online).

### 5. Configurar o DCA para o protocolo TCP

- **Descrição**: DCA (Direct Cache Access) é uma tecnologia que permite que dados de entrada e saída sejam enviados diretamente para a memória cache do processador, em vez de passarem pela memória principal primeiro.
- **Importância**: Reduz a latência da rede e o uso de memória, acelerando a comunicação TCP.

### 6. Esvaziar lixeira

- **Descrição**: Deleta tudo que tiver na lixeira.
- **Importância**: Apagar arquivos, inclusive esvaziar a lixeira ajuda a liberar espaço físico de armazenamento no PC.


## Como Utilizar

1. Abra o aplicativo de otimização Fasthunter Optimizer.
2. Na aba "Otimizar" clique no botão de iniciar otimização e aguarde até que os processos sejam concluídos.
3. Reinicie o computador para garantir que todas as alterações tenham efeito.
Obs: 
    Caso queira deixar a otimização mais robusta, você pode habilitar opções de otimização "extra" na aba de configurações, porém é crucial saber oque cada processo faz antes de habilitar!
    Certifique-se de salvar as configurações após habilitar/desabilitar alguma opção.


## Requisitos

- Sistema operacional Windows 10 ou superior.
- Python 3.13.1 ou superior.
- Permissões de administrador para executar algumas ações do sistema.


## Aviso

Algumas funções deste software podem causar alterações no comportamento do sistema. Utilize com cautela e certifique-se de que compreende as ações que estão sendo aplicadas.


## Contribuições

Sinta-se à vontade para contribuir com melhorias ou reportar problemas no repositório oficial do projeto.

