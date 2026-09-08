# Capítulo 9: Receitas práticas e solução de problemas

Embora os gerenciadores de arquivos ortodoxos de painel duplo sejam conhecidos por sua velocidade bruta e eficiência de teclado, dominar tarefas do mundo real geralmente requer a compreensão de como subsistemas distintos – como sincronização de diretórios, renomeação de padrões de lote, sistemas de arquivos virtuais remotos, reempacotamento de arquivos e pesquisa recursiva – funcionam juntos em cenários cotidianos. Além disso, operar no macOS moderno introduz limites de segurança, restrições de sandbox e interseções de atalhos do sistema que todo usuário eventualmente encontra. 

Este capítulo está dividido em duas seções abrangentes: 

1. **Receitas práticas e fluxos de trabalho**: cinco orientações completas e completas que cobrem fluxos de trabalho de gerenciamento de arquivos de alto valor com procedimentos passo a passo, representações visuais da interface do usuário, atalhos de teclado e dicas para usuários avançados. 
2. **Guia de solução de problemas e perguntas frequentes**: explicações detalhadas e resoluções de diagnóstico para questões operacionais comuns, erros de permissão, comportamentos de atualização automática, redefinições de configuração, teclas de função do teclado Apple e mecânica de transferência de arquivos entre volumes. 

---

## 1. Visual Quickstart: Matriz de resolução de problemas diários

A matriz de decisão a seguir mapeia objetivos comuns de gerenciamento de arquivos e desafios técnicos diretamente para as ferramentas integradas e identificadores de comando do ATBCmder: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                  ROTEADOR DE TAREFAS DIÁRIAS E RESOLUÇÃO DE PROBLEMAS                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  TAREFA / OBJETIVO                         FERRAMENTA / MÉTODO      ATALHO             │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Espelhar projetos para backup/NAS     Sincronizador de pastas Shift+F12 (⇧F12)    │
│  [2] Reorganizar fotos por data em lote    Renomeação múltipla     Ctrl+M (⌃M)         │
│  [3] Montar NAS, servidor ou nuvem         Gerenciador VFS de rede cm_ManageConnections│
│  [4] Editar arquivo dentro de um .zip      VFS de arquivos + Editor Enter ➔ F4 ➔ Salvar│
│  [5] Encontrar arquivos grandes aninhados  Visualização plana      Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  PROBLEMA / SINTOMA                        CAUSA RAIZ              RESOLUÇÃO           │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  Erro "Operation not permitted"            Sandbox do macOS / TCC cm_GrantAccess       │
│  Discos externos não atualizam sozinhos    FSEvents ausente no FAT attr_poll_interval  │
│  Testar configurações sem riscos           Proteção do XML original ATBCmder_test.sh   │
│  Teclas F mudam brilho ou volume           Teclas de mídia do macOS Tecla Fn ou Ajustes│
│  Mover entre volumes demora muito          Cópia física + Exclusão Checar espaço livre │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Tabela de referência rápida de matriz dupla

| Ação/Diagnóstico | Atalho do macOS | Tecla Commander Clássica | ID do comando | Finalidade Primária | 
| :--- | :--- | :--- | :--- | :--- | 
| **Sincronizar diretório** | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | Compara e sincroniza árvores de diretórios de painel duplo. | 
| **Renomeação múltipla em lote** | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | Renomeia vários arquivos usando tokens, contadores e RegEx. | 
| **Conexões de rede** | Menu: Rede | `cm_ManageConnections`| `cm_ManageConnections`| Gerencia perfis de servidores SMB, SFTP, WebDAV e FTP salvos. | 
| **Conexão rápida de rede** | Menu: Rede | `cm_NetworkConnect` | `cm_NetworkConnect` | Diálogo de conexão ad-hoc para servidores remotos. | 
| **Edição direta no arquivo compactado** | `F4` / `Fn+F4` | `F4` | `cm_Edit` | Edita item do arquivo; aciona `RepackWorker` ao salvar. | 
| **Visualização em árvore plana (Flat Branch View)** | `Cmd+B` / `⌘B` | `Ctrl+B` | `cm_FlatView` | Exibe recursivamente todos os arquivos aninhados em uma única lista simples. | 
| **Pesquisa Avançada** | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` | Pesquisa de arquivos com vários filtros com saída "Feed to Listbox". | 
| **Conceder acesso ao sistema de arquivos**| Menu: Arquivo / Ajuda | — | `cm_GrantFilesystemAccess`| Inicia o assistente de permissão do macOS App Sandbox. | 
| **Atualização manual do painel** | `Ctrl+R` / `⌃R` ou `Cmd+R` / `⌘R` | `Ctrl+R` | `cm_Refresh` | Força uma releitura imediata do diretório do disco. | 
| **Iniciar terminal do sistema** | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` | Gera o Terminal macOS no caminho do painel atual. | 
| **Calcular espaço na pasta** | `Alt+Shift+Enter` (`Space`) | `Alt+Shift+Enter` (`Space`) | `cm_CountDirContent` / `cm_CalculateSpace` | Calcula o tamanho de bytes recursivos agregados (`Space` para único, `Ctrl+L` para o total selecionado). | 
| **Exclusão segura permanente (Wipe)** | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | Sobregravação multipassada e exclusão permanente de arquivos. | 

---

## 2. Receitas práticas e fluxos de trabalho

### 2.1 Receita 1: Comparando e Sincronizando Duas Pastas de Backup

**Objetivo**: garantir que uma unidade de backup externa ou pasta de rede contenha uma réplica exata e atualizada do diretório ativo do projeto, com visibilidade completa dos arquivos adicionados, modificados ou excluídos antes de fazer alterações. 

![Directory Synchronization](images/folder_synchronization.png) 
*Figura 9.1: A caixa de diálogo Sincronização de pastas (Sync Dirs) exibindo comparações de diretórios lado a lado, setas de cópia direcionais e opções de espelhamento assimétrico.*

#### Procedimento passo a passo

1. **Alinhar origem e destino em painéis duplos**: 
- No **Painel Esquerdo**, navegue até seu diretório de trabalho local principal (por exemplo, `~/Documents/Projects/AppAlpha`). 
- Pressione **`Tab`** para alternar para o **Painel direito** e navegue até o destino de backup de destino (por exemplo, `/Volumes/BackupDrive/Backups/AppAlpha`). 
2. **Iniciar sincronização de diretório**: 
- Pressione **`Shift+F12`** (`⇧F12`) ou selecione **Comandos ➔ Sincronizar Dirs...** na barra de menu. 
- A caixa de diálogo Sincronizar diretórios é aberta com o caminho esquerdo e o caminho direito preenchidos automaticamente. 
3. **Configurar parâmetros de comparação**: 
- Marque **Comparar subdiretórios** para percorrer todas as pastas aninhadas recursivamente. 
- Marque **Comparar por conteúdo** se precisar de certeza criptográfica (verificando bytes de arquivo via `filecmp`) em vez de depender apenas de tamanhos de arquivo e carimbos de data/hora de modificação. 
- Certifique-se de que **Tolerância de carimbo de data/hora FAT/SMB (2,0 segundos)** esteja ativada se o destino de backup usar FAT32, exFAT ou um compartilhamento de rede SMB, evitando falsos sinalizadores de incompatibilidade causados ​​pelo arredondamento de carimbo de data/hora do sistema de arquivos de 2 segundos. 
4. **Iniciar a comparação**: 
- Clique em **Comparar** (ou pressione `Alt+C` / `⌥C`). 
- ATBCmder executa um trabalhador de comparação em segundo plano (`SyncCompareWorker`) e preenche a tabela de comparação com indicadores de ação direcionais: 
* **`->` (da esquerda para a direita)**: O arquivo local é mais recente ou existe apenas à esquerda. Ação: copie da esquerda para a direita. 
* **`<-` (Right to Left)**: The backup file is newer, or only exists on the right. Action: copy right to left.
     * **`=` (Equal)**: Both files are identical in size and timestamp/content. These are hidden from the pending action list by default.
     * **`!=` (Conflict)**: Incompatible directory-versus-file collision or timestamp mismatch requiring manual inspection.
5. **Select Your Synchronization Strategy**:
   - **Two-Way Symmetric Sync (Default)**: Copies newer files in both directions (`->` e `<-`). No files are deleted on either side. Ideal for syncing collaborative folders between machines.
   - **Asymmetric Mirroring (`Asymmetric` Checkbox Enabled)**: Makes the Right directory an exact binary replica of the Left directory. Any file on the Right that does not exist on the Left is **permanently deleted from the backup target**.
6. **Review and Execute**:
   - Inspect the summary count at the bottom: *e.g., "Left to Right: 42 files (128.4 MB) | Right to Left: 0 files | Deletes: 3 files"*.
   - Click **Synchronize** to launch the non-blocking background transfer queue. Progress bars reflect active transfer volume and remaining item counts.

> [!CAUTION] 
> **Perigo de perda de dados de espelhamento assimétrico**: 
> Quando o modo **Assimétrico** estiver marcado, os arquivos presentes na unidade de destino que foram excluídos ou renomeados na origem serão **removidos permanentemente** sem serem movidos para a Lixeira do macOS. Sempre revise a tabela de comparação direcional antes de clicar em Sincronizar! 

> [!TIP] 
> **⚡ Dica profissional: verificação em nível de conteúdo para mídia e código**: 
> Ao fazer backup de imagens de vídeo ou repositórios Git, os tamanhos dos arquivos podem corresponder, embora existam corrupções sutis de bytes internos. Sempre verifique **Comparar por conteúdo** para arquivos de missão crítica. Embora a comparação byte a byte demore mais em USB ou Wi-Fi, ela garante 100% de integridade dos dados. 

---

### 2.2 Receita 2: Renomeação em lote de fotos de câmeras com datas e números de sequência

**Objetivo**: transformar centenas de arquivos de câmera desorganizados (por exemplo, `DSC_0012.JPG`, `DSC_0013.JPG`, `IMG_4901.CR3`) em nomes de arquivos limpos e classificáveis, como `2026-09-06_Vacation_001.jpg` com contadores de sequência preenchidos com zeros e visualizações de segurança ao vivo. 

![Batch Multi-Rename Tool](images/multi_rename_dialog.png) 
*Figura 9.2: Ferramenta de multi-renomeação em lote com visualização em tempo real de linhas, tokens de metadados, controles de contador numérico e detecção de colisão.*

#### Procedimento passo a passo

1. **Selecione as fotos**: 
- Navegue até o diretório de importação da câmera no painel ativo. 
- Selecione todas as fotos usando **`Cmd+A`** (`⌘A`) ou pressione **`+`** no teclado para inserir uma máscara curinga como `*.jpg;*.jpeg;*.cr3;*.arw`. 
2. **Inicie a ferramenta de multi-renomeação em lote**: 
- Pressione **`Ctrl+M`** (`⌃M`) ou **`Cmd+M`** (`⌘M`), ou escolha **Arquivos ➔ Ferramenta de Multi-Renomeação...** na barra de menu. 
3. **Defina a máscara de nome de arquivo**: 
- No campo **File Name Mask**, insira a estrutura desejada usando tokens de metadados: 
     ```
     [Y]-[M]-[D]_Vacation_[C]
     ```


- **Explicação do token**: 
* `[Y]`: Ano de modificação do arquivo com 4 dígitos (por exemplo, `2026`). 
* `[M]`: Mês de 2 dígitos (por exemplo, `09`). 
* `[D]`: Dia de 2 dígitos (por exemplo, `06`). 
* `Vacation`: Texto descritivo estático. 
* `[C]`: Contador numérico sequencial. 
4. **Configure a sequência do contador**: 
- No cartão **Configurações do contador**: 
* **Início em**: `1` 
* **Etapa**: `1` 
* **Dígitos**: `3` (isso impõe preenchimento de zeros: `001`, `002`, `003`... até `999`). 
5. **Retirar prefixos de câmera com localizar e substituir (opcional)**: 
- Se você quiser preservar parte do nome do arquivo original sem o prefixo da câmera (por exemplo, mantendo o número de sequência da câmera de `DSC_8941.JPG`): 
* Defina **Máscara de nome de arquivo** como: `[YMD]_[N5-]` 
* `[N5-]` extrai caracteres do índice 5 até o final do nome, eliminando `DSC_` inteiramente. 
- Alternativamente, use os campos **Pesquisar e Substituir**: 
* **Encontrar**: `DSC_` 
* **Substituir**: `Photo_` 
* Marque **RegEx** se estiver usando padrões de expressão complexos como `^IMG_(\d+)`. 
6. **Inspecione a tabela de visualização ao vivo**: 
- A tabela de 3 colunas (`Old Name`, `New Name`, `Directory`) é atualizada instantaneamente a cada pressionamento de tecla. 
- Verifique a coluna **Status**: ATBCmder destaca nomes de alvos duplicados em negrito vermelho com um indicador de colisão, evitando substituições acidentais. 
7. **Execute a Renomeação**: 
- Pressione **`Enter`** ou clique em **Iniciar Renomear**. ATBCmder executa as renomeações atomicamente no disco e atualiza a visualização do painel. 

> [!NOTE] 
> **Segurança de extensão**: 
> Por padrão, a **Máscara de extensão** é definida como `[E]`, preservando a extensão do arquivo original sem modificações. Nunca exclua `[E]` a menos que você pretenda explicitamente remover extensões de seus arquivos.

> [!TIP] 
> **⚡ Dica profissional: fluxo de trabalho do editor externo (`⌘I`)**: 
> Se você tiver uma lista irregular de nomes de clientes ou títulos de faixas, pressione **`Cmd+I`** (`⌘I` / Editar no Editor Externo) dentro da ferramenta Multi-Renomear. ATBCmder exporta os nomes de destino para seu editor de texto padrão. Edite a lista no Vim, VS Code ou TextEdit, salve o documento e o ATBCmder importa imediatamente os nomes revisados ​​para a grade de visualização. 

---

### 2.3 Receita 3: Conectando-se a um NAS doméstico/de escritório via SMB, SFTP ou WebDAV

**Objetivo**: Montar um pool de armazenamento TrueNAS ou Synology local, um servidor AWS EC2 Linux ou um repositório de nuvem Nextcloud WebDAV em uma guia de painel duplo sem fazer malabarismos com comandos de terminal separados ou folhas de conexão do Finder. 

![Remote VFS Connection](images/smb_sftp_ftp_remote_access.png) 
*Figura 9.3: Configurando compartilhamentos de rede remotos seguros entre protocolos SMB, SFTP e WebDAV.*

#### Procedimento passo a passo

1. **Abra o Gerenciador de conexões de rede**: 
- Escolha **Rede ➔ Gerenciar conexões de rede...** na barra de menu nativa ou execute o comando **`cm_ManageConnections`**. 
2. **Crie um novo perfil de conexão**: 
- Clique no botão **`➕ New`** no canto inferior esquerdo. 
- No campo **Label**, insira um identificador reconhecível (por exemplo, `Synology Office NAS` ou `AWS Production Web`). 
3. **Configurar protocolo e detalhes do host**: 
- **Protocolo**: Selecione seu protocolo de destino no menu suspenso: 
* **SMB/CIFS**: Porta `445` (Padrão para Synology, QNAP, Windows Server, TrueNAS). 
* **SFTP (SSH File Transfer)**: Porta `22` (padrão para instâncias de nuvem Linux/UNIX). 
* **WebDAV/WebDAVS**: Porta `80` ou `443` (Padrão para Nextcloud, ownCloud). 
* **FTP / FTPS**: Porta `21` ou `990` (hosts de arquivos legados). 
- **Host**: Insira o endereço IP ou nome de domínio (por exemplo, `192.168.1.100` ou `sftp.mycompany.com`). 
- **Porta**: Configurada automaticamente quando o protocolo é escolhido; ajuste se o seu servidor usa uma porta não padrão. 
- **Nome de usuário**: Digite o nome de usuário da sua conta do sistema remoto. 
- **Caminho remoto**: Defina o diretório de destino padrão (por exemplo, `/volume1/Media` ou `/var/www/html`). 
4. **Armazenamento seguro de credenciais**: 
- Digite sua senha ou chave de acesso. 
- Marque **Lembrar senha no macOS Keychain**. 
- **Garantia de segurança**: ATBCmder nunca armazena credenciais de texto simples em arquivos de configuração XML. Todos os segredos são selados criptograficamente dentro do Apple Keychain nativo (`com.aitobox.atbcmder.vfs`). 
5. **Teste a conexão**: 
- Clique em **`🔍 Test Connection`**. 
- ATBCmder despacha um trabalhador em segundo plano (`ConnectionTestWorker`) que valida a acessibilidade da rede, verifica chaves de host SSH ou certificados TLS, verifica credenciais e exibe um alerta de sucesso sem fechar a caixa de diálogo. 
6. **Conecte-se e navegue**: 
- Clique em **`🔗 Connect`** (ou pressione `Enter`). 
- Uma nova guia de pasta é aberta no painel ativo, exibindo o caminho remoto formatado como um URI VFS unificado: 
     ```
     vfs://smb://admin@192.168.1.100/volume1/Media/
     vfs://sftp://ubuntu@aws.prod.internal:22/var/www/html/
     ```


- Agora você pode navegar, pesquisar, copiar (`F5`), mover (`F6`) e excluir (`F8`) arquivos em discos locais e servidores remotos com agilidade idêntica de painel duplo. 
7. **Reconexão rápida na barra de menu**: 
- Todos os perfis salvos aparecem automaticamente em **Rede ➔ Conexões salvas**. Basta clicar em qualquer servidor salvo para montá-lo instantaneamente. 

> [!TIP] 
> **⚡ Dica profissional: autenticação baseada em chave SSH para SFTP**: 
> Para acesso automatizado ao servidor em nuvem, configure a autenticação de chave pública. No seu perfil de conexão SFTP, deixe o campo de senha em branco e aponte para sua chave privada local (por exemplo, `~/.ssh/id_ed25519`). Se a chave estiver protegida por uma senha longa, o ATBCmder a solicitará uma vez e a salvará com segurança nas chaves do macOS. 

---

### 2.4 Receita 4: Editando um arquivo diretamente dentro de um arquivo sem extrair

**Objetivo**: Modificar um arquivo de configuração aninhado (`settings.json` ou `config.yaml`) dentro de um arquivo `.zip`, `.tar.gz` ou `.7z` de vários gigabytes no armazenamento local ou em um servidor remoto sem descompactar o arquivo inteiro em seu disco rígido. 

![Archive VFS](images/archive_vfs.png) 
*Figura 9.4: Navegando e editando dentro de arquivos compactados por meio do sistema de arquivos virtual unificado `vfs://`.*

#### Procedimento passo a passo

1. **Insira o Arquivo como Diretório Virtual**: 
- Destaque o arquivo compactado (por exemplo, `production_backup.zip`) no painel ativo. 
- Pressione **`Enter`** (ou clique duas vezes). 
- ATBCmder intercepta a navegação e monta o arquivo como um sistema de arquivos virtual: 
     ```
     vfs:///Users/brain/Downloads/production_backup.zip/
     ```
 

2. **Navegue até o arquivo de destino**: 
- Navegue pelos diretórios virtuais aninhados (`etc`, `nginx`, `conf.d`) da mesma forma que faria em um volume físico. 
- Localize o arquivo que você precisa atualizar (por exemplo, `nginx.conf` ou `app_settings.json`). 
3. **Abra no Editor de Texto Integrado**: 
- Pressione **`F4`** (`Fn+F4` / `cm_Edit`). 
- ATBCmder transmite o membro compactado em um buffer isolado temporário e o abre diretamente no editor de texto realçado pela sintaxe. 
4. **Faça edições e salve**: 
- Faça as modificações de configuração necessárias. 
- Pressione **`Cmd+S`** (`⌘S`) para salvar o buffer. 
5. **Ciclo de vida de reembalagem automática (`RepackWorker`)**: 
- Quando você salva ou fecha o editor, o mecanismo de reempacotamento em segundo plano do ATBCmder (`RepackWorker`) é ativado automaticamente: 
1. Calcula o delta entre o membro compactado original e o buffer modificado. 
2. Ele verifica o tamanho geral do arquivo em relação ao limite de aviso configurado (`ArchiveRepackWarningMB`). 
3. Ele recompacta o arquivo modificado e reconstrói a estrutura do arquivo em um arquivo temporário. 
4. Ele substitui atomicamente o arquivo original no disco, garantindo que nenhuma corrupção ocorra se o sistema perder energia no meio da gravação. 
5. A visualização do painel ativo é atualizada automaticamente para exibir tamanhos de bytes de membros e carimbos de data/hora atualizados.

> [!IMPORTANT] 
> **Proteção de reembalagem de arquivos grandes (`ArchiveRepackWarningMB`)**: 
> A atualização de um único arquivo de texto de 2 KB dentro de um arquivo de 15 GB requer a reescrita de todo o arquivo compactado no disco. Para evitar picos inesperados de CPU e desgaste de SSD, o ATBCmder verifica o tamanho do arquivo. Se o arquivo exceder `ArchiveRepackWarningMB` (padrão: 500 MB), uma caixa de diálogo de aviso solicitará: *"Este arquivo tem 1,4 GB. A reembalagem reescreverá o arquivo inteiro. Deseja continuar?"* Você pode personalizar esse limite em **Configuração ➔ Opções ➔ Arquivos**. 

---

### 2.5 Receita 5: Encontrar e excluir arquivos grandes e inchados em diretórios aninhados

**Objetivo**: recuperar a valiosa capacidade do SSD localizando rapidamente e removendo com segurança renderizações de vídeo 4K abandonadas, pastas `node_modules` inchadas, imagens de disco virtual do Docker ou instaladores DMG desatualizados espalhados em estruturas de diretórios de vários níveis. 

![Flat Branch View](images/branch_view.png) 
*Figura 9.5: Visualização de ramificação plana (`Cmd+B`) exibindo conteúdos profundamente aninhados em uma única tabela achatada para classificação instantânea por tamanho.*

#### Método A: nivelamento instantâneo por meio da visualização plana de ramificação (`Cmd+B`)

1. **Navegue até a pasta raiz pai**: 
- Destaque a pasta pai de nível superior que você deseja auditar (por exemplo, `~/Projects` ou `~/Downloads`). 
2. **Ativar visualização de ramificação plana**: 
- Pressione **`Cmd+B`** (`⌘B`) ou **`Ctrl+B`** (`cm_FlatView`) ou selecione **Mostrar ➔ Branch View (Flat View)**. 
- ATBCmder verifica recursivamente todos os subdiretórios e exibe todos os arquivos aninhados em uma **lista simples e simples**, eliminando os limites da pasta do diretório. 
3. **Classificar por tamanho decrescente**: 
- Clique no cabeçalho da coluna **Tamanho** ou pressione **`Ctrl+F6`** (`cm_SortBySize`) para classificar os arquivos maiores no topo. 
- Arquivos ISO gigantes, despejos de banco de dados e imagens de máquinas virtuais flutuam imediatamente no topo do seu painel. 
4. **Calcular espaço no diretório**: 
- Para subpastas visíveis nas visualizações padrão, coloque o cursor em qualquer pasta e pressione **`Space`** (`␣` / `cm_CalculateSpace`). ATBCmder calcula o espaço total de bytes recursivos e o exibe no lugar do rótulo padrão `<DIR>`. 
5. **Sair da visualização da filial**: 
- Pressione **`Cmd+B`** novamente ou pressione `Esc` / `Backspace` em `..` para retornar à navegação hierárquica normal do diretório. 

---

#### Método B: Filtragem direcionada por meio de pesquisa avançada (`Alt+F7`) e "Feed to Listbox"

![Advanced Search](images/advanced_search_dialog.png) 
*Figura 9.6: Caixa de diálogo Pesquisa Avançada com critérios de filtro de tamanho e o botão "Feed to Listbox".* 

1. **Iniciar pesquisa avançada**: 
- Pressione **`Alt+F7`** (`⌥F7`) ou selecione **Comandos ➔ Pesquisar...**. 
2. **Definir filtros de tamanho e tipo**: 
- No campo **Pesquisar em**, confirme seu diretório raiz. 
- Verifique o filtro **Tamanho**: selecione **`>`** e insira `100` com unidade **`MB`** (ou `1` **`GB`**). 
- No campo **Máscara de arquivo**, especifique as extensões de destino (por exemplo, `*.dmg;*.iso;*.mp4;*.mov;*.zip`) ou deixe como `*` para encontrar qualquer item inchado. 
- Na guia **Data**, opcionalmente, restrinja os resultados aos arquivos não modificados nos últimos 180 dias. 
3. **Execute a pesquisa**: 
- Clique em **Iniciar pesquisa**. 
4. **Alimente os resultados em uma guia do painel virtual ("Feed to Listbox")**: 
- Depois que os resultados forem preenchidos, clique no botão **Feed to listbox**. 
- Todo o conjunto de resultados da pesquisa é transferido para uma **guia virtual dedicada** em seu painel ativo. 
- Ao contrário de uma caixa de diálogo modal estática, os arquivos nesta guia se comportam como itens normais do painel de arquivos: você pode visualizá-los com Quick View (`Ctrl+Q` / `⌘Q`), inspecioná-los no Universal Lister (`F3`) ou marcar vários arquivos com `Insert` / `Space`. 
5. **Revisar e excluir**: 
- Selecione os arquivos indesejados e pressione **`F8`** (`Fn+F8` / `cm_Delete`) para movê-los com segurança para a Lixeira do macOS. 
- Se você precisar de eliminação permanente e irrecuperável de dados (por exemplo, limpeza de dados confidenciais do cliente), pressione **`Alt+Delete`** (`⌥⌫` / `cm_Wipe`) para acionar a destruição segura de arquivos em múltiplas passagens. 

> [!TIP] 
> **⚡ Dica profissional: identificação de arquivos duplicados idênticos por meio de somas de verificação**: 
> Se você suspeitar que vários arquivos grandes são duplicatas exatas, selecione-os e pressione **`Ctrl+X`** (`⌃X` / `cm_CheckSumCalc`). Escolha **SHA-256** e clique em Calcular. Os resumos de hash correspondentes confirmam 100% de duplicatas binárias, permitindo excluir cópias supérfluas com total confiança. 

---

## 3. Guia de solução de problemas e perguntas frequentes (FAQs)

### 3.1 "Operação não permitida"/erros de permissão negada do macOS

#### Causa raiz

No macOS moderno (macOS 12 Monterey até macOS 15 Sequoia), a Apple impõe limites de privacidade rígidos de **App Sandbox** e **TCC (Transparência, Consentimento e Controle)**. Os aplicativos em área restrita não podem acessar unidades externas, pastas do sistema ou até mesmo diretórios de usuários padrão (`~/Documents`, `~/Downloads`, `~/Desktop`) sem um token de permissão criptográfica explícito concedido pelo usuário, conhecido como **Marcador com escopo de segurança**. 

Se ATBCmder não tiver acesso ao sistema de arquivos, você poderá enfrentar: 

- Diálogos de operação de arquivo exibindo: `"Error: Operation not permitted"`. 
- Diretórios aparecendo vazios mesmo que existam arquivos no Finder. 
- Unidades USB externas ou Thunderbolt em `/Volumes` mostrando erros de acesso negado.

#### Solução 1: use o App Sandbox Onboarding Assistant (`cm_GrantFilesystemAccess`)

ATBCmder inclui um assistente de integração integrado projetado para registrar marcadores de segurança persistentes com macOS: 

```
┌─────────────────────────────────────────────────────────────┐
│  Conceder Acesso ao Disco (Filesystem Access)           [x] │
├─────────────────────────────────────────────────────────────┤
│  Como o ATBCmder executa na Sandbox segura do macOS, ele    │
│  precisa de sua autorização para ler e gravar em pastas     │
│  críticas e discos externos.                                │
│                                                             │
│  [  Conceder acesso ao diretório raiz (/)  ]                │
│                                                             │
│  [  Conceder acesso a discos externos (/Volumes)  ]         │
│                                                             │
│  [  Abrir Ajustes de Acesso Total ao Disco…  ]              │
│                                                             │
│  O acesso à raiz é exigido pela Sandbox do aplicativo.      │
│  O Acesso Total ao Disco protege dados pessoais seguros.    │
│                                              [ Concluído ]  │
└─────────────────────────────────────────────────────────────┘
```
 

1. Na barra de menu, escolha **Arquivo** (ou **Ajuda**) ➔ **Conceder acesso ao sistema de arquivos…** ou acione o comando **`cm_GrantFilesystemAccess`**. 
2. Clique em **"Conceder acesso ao diretório raiz (/)"**. 
* Quando a planilha nativa Apple `NSOpenPanel` aparecer apontando para `Macintosh HD` (`/`), clique em **Conceder acesso** (ou **Abrir**). 
* **Por que isso funciona**: A autorização de `/` gera um marcador com escopo de segurança raiz armazenado em `sandbox_bookmarks.plist`. Como os caminhos filhos herdam tokens de segurança para baixo, conceder acesso a `/` desbloqueia permanentemente todas as pastas de usuário padrão (`~/Documents`, `~/Downloads`, `/Applications`, `~/Projects`). 
3. Clique em **"Conceder acesso a discos externos (/Volumes)"**. 
* Na planilha aberta, clique em **Conceder acesso** para `/Volumes`. 
* Isso autoriza todas as unidades flash USB conectadas, SSDs externos, cartões SD, imagens de disco (DMG) e montagens SMB de rede. 
4. Clique em **Concluído**. Suas permissões são salvas permanentemente nas reinicializações do aplicativo.

#### Solução 2: conceda acesso total ao disco (FDA) nas configurações do sistema macOS

Se você precisar gerenciar locais protegidos do sistema, como `~/Library/Mail`, `~/Library/Messages`, caches de navegação do Safari ou árvores de backup do Time Machine, o macOS TCC requer uma autorização adicional no nível do sistema: 

1. Abra **Configurações do sistema** (menu Apple  ➔ Configurações do sistema). 
2. Navegue até **Privacidade e segurança ➔ Acesso total ao disco**. 
3. Localize **ATBCmder** na lista de aplicativos e alterne a chave para **On**. 
4. Se ATBCmder não estiver listado: 
* Clique no botão **`+`** na parte inferior. 
* Autentique com sua senha do Mac ou Touch ID. 
* Selecione `/Applications/ATBCmder.app` e clique em **Abrir**. 
5. Quando solicitado a reiniciar o aplicativo, clique em **Sair e Reabrir**.

#### Solução 3: redefinindo permissões de privacidade TCC corrompidas via terminal

Se as permissões forem corrompidas após uma atualização do sistema operacional macOS ou um evento de nova assinatura do aplicativo, redefina o banco de dados TCC usando a ferramenta de linha de comando macOS `tccutil`: 

```bash
# Reset all Full Disk Access permissions for ATBCmder
tccutil reset SystemPolicyAllFiles com.aitobox.atbcmder

# Reset Desktop, Documents, and Downloads folder permissions
tccutil reset SystemPolicyDocumentsFolder com.aitobox.atbcmder
tccutil reset SystemPolicyDownloadsFolder com.aitobox.atbcmder
tccutil reset SystemPolicyDesktopFolder com.aitobox.atbcmder
```
 

Depois de executar esses comandos, reinicie o ATBCmder e execute novamente **`cm_GrantFilesystemAccess`**. 

---

### 3.2 Atualização automática não detectando alterações de arquivo no disco

#### Causa raiz

ATBCmder usa um mecanismo de monitoramento de arquivos em várias camadas: 

1. **Kernel `FSEvents`**: em volumes Apple APFS e HFS+ nativos, o kernel do macOS emite eventos instantâneos de mutação de diretório quando arquivos são adicionados, modificados ou excluídos por ferramentas externas. 
2. **Limitações do sistema de arquivos**: sistemas de arquivos que não são da Apple (por exemplo, pen drives USB externos formatados como **FAT32** ou **exFAT**) e montagens de rede remotas (**SMB**, **NFS**, **SFTP**, **WebDAV**) **não suportam notificações `FSEvents` do kernel**. Quando um aplicativo de terceiros cria ou exclui um arquivo em um compartilhamento SMB, o kernel do macOS não recebe nenhum evento de notificação.

#### Etapas de resolução

1. **Ajuste o intervalo de fallback de pesquisa (`attr_poll_interval`)**: 
- Abra Preferências via **`Cmd+,`** (`⌘,`) ou **Configuração ➔ Opções...**. 
- Navegue até a página **Atualização automática**. 
- Verifique se **Assistir à alteração do nome do arquivo** e **Assistir à alteração dos atributos** estão ativados. 
- Ajuste o **Intervalo de pesquisa (`attr_poll_interval`)**: 
* Padrão: `5 seconds`. 
* Para testes locais rápidos ou desenvolvimento de rede ativa: diminua para `1` ou `2 seconds`. 
* Para compartilhamentos Wi-Fi de alta latência: aumente para `10` ou `15 seconds` para minimizar a sobrecarga da rede. 
2. **Verifique a lista de diretórios excluídos**: 
- Na mesma página de preferências de **Atualização automática**, revise a tabela **Diretórios excluídos**. 
- Se o seu caminho ativo (ou uma pasta pai) foi adicionado à lista de exclusão, o ATBCmder suprimirá deliberadamente o monitoramento de arquivos para conservar os ciclos da CPU. Remova o caminho se desejar reativar o monitoramento. 
3. **Verifique as configurações de atualização em segundo plano**: 
- Se os painéis de arquivos só falharem na atualização quando o ATBCmder estiver minimizado ou atrás de outras janelas, marque a opção: 
`[ ] Disable auto-refresh when ATBCmder is in the background` 

- Desmarque esta opção se desejar que o ATBCmder reflita continuamente as saídas de construção em segundo plano e downloads externos. 
4. **Forçar uma atualização manual imediata**: 
- A qualquer momento, pressione **`Ctrl+R`** (`⌃R`) ou **`Cmd+R`** (`⌘R`) (`cm_Refresh`). 
- Isso ignora todas as camadas de cache, libera modelos de diretório internos e relê imediatamente o conteúdo do diretório do controlador de armazenamento. 

---

### 3.3 Redefinição segura da configuração ou teste no modo de teste isolado

#### Testando novas configurações com segurança com `scripts/ATBCmder_test.sh`

Ao testar layouts experimentais de atalhos de teclado, novos temas de cores ou comandos de script automatizados, evite modificar o XML de configuração de produção. 

ATBCmder fornece um script de inicialização de teste em sandbox: 
```bash
# Run ATBCmder in an isolated test environment
./scripts/ATBCmder_test.sh
```
 

**Como funciona**: 

1. O script cria um diretório temporário dedicado: `tests/.test_config/`. 
2. Ele copia a configuração de teste de linha de base limpa (`src/atbcmder/resources/test_config.xml`) para `tests/.test_config/atbcmder.xml`. 
3. Exporta a variável de ambiente: 
   ```bash
   export ATBCMDER_CONFIG_PATH="$(pwd)/tests/.test_config"
   ```
 

4. Quando iniciado, o ATBCmder lê todas as configurações exclusivamente desta pasta de teste. Quaisquer alterações, modificações de guias ou experimentos com teclas de atalho estão contidos inteiramente em `tests/.test_config/`, deixando suas preferências pessoais completamente intocadas.

#### Restaurando a configuração padrão de fábrica

Se sua configuração de produção for corrompida ou você quiser começar do zero: 

1. **Saia do ATBCmder** completamente (**`Cmd+Q`** / `⌘Q`). 
2. Abra o macOS Terminal e localize seu diretório de configuração: 
* Instalação padrão: `~/Library/Preferências/atbcmder/` 
* Substituição Linux/XDG: `~/.config/atbcmder/` 
3. Faça backup ou remova os arquivos de configuração ativos: 
   ```bash
   # Move configuration files to a backup location
   mv ~/Library/Preferences/atbcmder/atbcmder.xml ~/Library/Preferences/atbcmder/atbcmder.xml.bak
   mv ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml.bak
   ```
 

4. Reinicie o ATBCmder. 
5. Na inicialização, o ATBCmder detecta os arquivos de configuração ausentes e regenera automaticamente configurações XML limpas e validadas preenchidas com padrões oficiais de fábrica.

#### Exportando e importando configurações portáteis

Para migrar sua configuração entre vários Macs ou criar um backup externo: 

- **Exportar**: Escolha **Configuração ➔ Exportar configuração...** (comando **`cm_ExportConfiguration`**) para salvar um instantâneo `.zip` ou `.xml` consolidado contendo suas teclas de atalho, colunas, guias favoritas e paletas de cores. 
- **Importar**: Escolha **Configuração ➔ Importar configuração...** (comando **`cm_ImportConfiguration`**) em sua máquina de destino para restaurar as configurações instantaneamente. 

---

### 3.4 Teclas de função que acionam brilho/volume do macOS em vez de comandos

#### Causa raiz

Por padrão, os teclados Apple (teclados integrados do MacBook, Magic Keyboards) atribuem funções especiais de hardware à linha superior de teclas: 

- `F1` / `F2`: Diminuir/aumentar o brilho da tela 
- `F3`: Controle da Missão 
- `F4`: Destaque / Launchpad 
- `F7` / `F8` / `F9`: Controles de reprodução de mídia (retroceder, reproduzir/pausar, avançar) 
- `F10` / `F11` / `F12`: Áudio mudo, diminuir volume, aumentar volume 

Quando você pressiona `F5` na esperança de copiar um arquivo, o macOS intercepta o pressionamento de tecla e não faz nada (ou ajusta a iluminação do teclado).

#### Solução 1: use o acorde modificador `Fn`

Mantenha pressionada a tecla **`Fn`** (Function) ou **Globe (`🌐`)** no canto inferior esquerdo do teclado enquanto pressiona a tecla de função: 

- **`Fn+F3`**: Lista Universal (`cm_View`) 
- **`Fn+F4`**: Editor de texto (`cm_Edit`) 
- **`Fn+F5`**: Copiar arquivos (`cm_Copy`) 
- **`Fn+F6`**: Mover/Renomear arquivos (`cm_Rename`) 
- **`Fn+F7`**: Criar nova pasta (`cm_MakeDir`) 
- **`Fn+F8`**: Excluir para a Lixeira (`cm_Delete`) 
- **`Fn+Shift+F12`**: Sincronizar diretórios (`cm_SyncDirs`)

#### Solução 2: habilitar teclas de função padrão em todo o sistema nas configurações do macOS

Se você usa ATBCmder regularmente, configurar o macOS para tratar as teclas de função como teclas `F1`-`F12` padrão é a configuração recomendada: 

1. Abra **Configurações do sistema** (menu Apple  ➔ Configurações do sistema). 
2. Selecione **Teclado** na barra lateral esquerda. 
3. Clique no botão **Atalhos de teclado...**. 
4. Selecione **Teclas de função** na lista esquerda da planilha modal. 
5. Ligue a chave seletora: 
**"Use as teclas F1, F2, etc. como teclas de função padrão"** 

6. Clique em **Concluído**. 

```
┌─────────────────────────────────────────────────────────────┐
│  Atalhos de Teclado                                         │
├──────────────────────────────┬──────────────────────────────┤
│  Navegação por Teclado       │  Usar teclas F1, F2, etc.    │
│  Teclas Modificadoras        │  como tecla padrão      [SIM]│
│  Teclas de Função       ◄─── │                              │
│  Spotlight                   │  Com esta opção ativada,     │
│  Mission Control             │  pressione a tecla Fn para   │
│  Atalhos de Aplicativos      │  usar os recursos impressos  │
│                              │  em cada tecla.              │
│                              │                [ Concluído ] │
└──────────────────────────────┴──────────────────────────────┘
```
 

*Resultado*: Pressionar `F5` agora aciona diretamente a cópia no ATBCmder. Para ajustar o brilho ou volume, segure `Fn` enquanto pressiona a tecla.

#### Solução 3: use equivalentes de chave nativos do macOS `Cmd`

Se você preferir não alterar as configurações do teclado do sistema, o ATBCmder fornece atalhos de teclado nativos do macOS para cada operação principal: 

- **Cópia**: `Cmd+C` / `Cmd+V` (ou padrão `F5`) 
- **Mover**: `Cmd+C` ➔ `Cmd+Option+V` (`⌥⌘V` mover e colar) 
- **Excluir**: `Cmd+Delete` (`⌘⌫`) 
- **Nova pasta**: `Shift+Cmd+N` (`⇧⌘N`) 
- **Renomear**: `F2` ou `Return` 
- **Renomeação múltipla em lote**: `Ctrl+M` (`⌃M`) ou `Cmd+M` (`⌘M`) 
- **Preferências**: `Cmd+,` (`⌘,`) 
- **Fechar guia**: `Cmd+W` (`⌘W`) 

---

### 3.5 Movendo arquivos entre unidades diferentes versus a mesma unidade

Uma pergunta frequente dos usuários é por que mover um arquivo de 20 GB dentro da mesma pasta leva uma fração de segundo, enquanto mover o mesmo arquivo para uma unidade externa ou compartilhamento de rede leva vários minutos.

#### Movimentação intra-volume (mesma unidade/partição APFS)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        MOVER NO MESMO VOLUME (EM MILISSEGUNDOS)                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Origem: /Users/brain/Downloads/BigFile.iso ➔ Destino: /Users/brain/Movies/           │
│                                                                                        │
│   1. A chamada de sistema POSIX rename() apenas atualiza o registro do inode.          │
│   2. Os blocos de dados físicos no SSD NUNCA são lidos ou copiados.                    │
│   3. Tempo de execução: < 5 milissegundos. Espaço livre necessário: 0 bytes.           │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

Quando os caminhos de origem e destino residem no **mesmo volume físico do sistema de arquivos**, o ATBCmder emite uma chamada de sistema POSIX `rename()` atômica. O sistema operacional simplesmente atualiza as entradas de ponteiro no catálogo de diretórios do sistema de arquivos. Os clusters de dados físicos no seu SSD não são movidos.

#### Movimentação entre volumes (diferentes unidades/partições/montagens de rede)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                     MOVER ENTRE VOLUMES DIFERENTES (FLUXO FÍSICO)                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Origem: /Users/brain/Downloads/BigFile.iso ➔ Destino: /Volumes/ExternalSSD/Movie/    │
│                                                                                        │
│   Etapa 1: Cópia do fluxo binário (Leitura do SSD interno ➔ Gravação no SSD externo)   │
│   Etapa 2: Verificação e gravação física (fsync garante a gravação completa na mídia)  │
│   Etapa 3: Exclusão segura da origem (o arquivo original só é removido após sucesso)   │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

Ao transferir através de diferentes limites do sistema de arquivos (por exemplo, do SSD interno do Mac para uma unidade USB externa, compartilhamento SMB de rede ou imagem de disco), uma atualização de ponteiro atômico é fisicamente impossível. ATBCmder executa um pipeline **Copy-Verify-Delete** de vários estágios: 

1. **Leitura/gravação de fluxo binário**: os dados são transmitidos em partes do controlador de armazenamento de origem através da memória do sistema e gravados no controlador de armazenamento de destino. A duração da transferência depende inteiramente da velocidade do barramento físico (por exemplo, USB 3.0 a ~100 MB/s vs. Thunderbolt 4 a ~2.800 MB/s). 
2. **Liberação e verificação de buffer**: ATBCmder chama `fsync()` no identificador do arquivo de destino para garantir que todos os dados armazenados em cache foram gravados na mídia física e verifica a equivalência de contagem de bytes. 
3. **Exclusão segura da fonte**: Somente após o arquivo de destino ter sido completamente gravado e verificado o ATBCmder exclui o arquivo de origem do disco original.

#### Implicações críticas e garantias de segurança

* **Requisito de espaço livre**: A unidade de destino **deve ter capacidade livre suficiente** para armazenar a carga completa do arquivo *antes* de a operação começar. Se você tentar mover um arquivo de 30 GB para uma unidade externa com apenas 10 GB livres, a transferência falhará. 
* **Garantia de perda zero de dados**: Se uma unidade externa for acidentalmente desconectada ou se o armazenamento de destino ficar sem espaço durante a transferência, o ATBCmder aborta imediatamente a operação, deixa o arquivo de origem **completamente intacto e ileso**, remove qualquer arquivo de destino parcial e relata uma caixa de diálogo de erro clara. 
* **Monitoramento de fila em segundo plano (`cm_OperationsPanel`)**: movimentações de volume cruzado de longa execução são executadas em threads de trabalho assíncronos em segundo plano (`FileOpWorker`). Você pode monitorar velocidades de transferência em tempo real, tempos restantes, pausar/retomar transferências ou enfileirar operações subsequentes sem bloquear a interface do usuário. 

---

### 3.6 Perguntas Frequentes Adicionais

#### P1: Como alterno o foco entre os painéis Esquerdo e Direito?

Pressione a tecla **`Tab`** (`⇥`). O Focus alterna instantaneamente entre as tabelas de arquivos ativos e inativos. O painel ativo exibe um destaque de borda acentuado e um texto em foco na barra de status.

#### P2: Como troco o conteúdo dos painéis Esquerdo e Direito?

Pressione **`Ctrl+U`** (`⌃U`) ou execute o comando **`cm_Exchange`**. Os diretórios, guias de pastas e posições do cursor dos painéis esquerdo e direito são trocados instantaneamente. Para equalizar as larguras dos painéis para uma divisão exata de 50/50, clique duas vezes em qualquer lugar na barra divisora ​​central vertical.

#### P3: Como seleciono arquivos usando padrões curinga?

Pressione a tecla **`+`** no teclado (ou escolha **Marcar ➔ Selecionar grupo...** / `cm_MarkPlus`). Insira um padrão curinga como `*.pdf` ou `photo_2026_*.jpg`. Para desmarcar os arquivos que correspondem a um padrão, pressione a tecla **`-`** (`cm_MarkMinus`). Para inverter sua seleção atual, pressione **`*`** (`cm_MarkInvert`).

#### Q4: Como alterno a visibilidade de dotfiles ocultos?

Pressione **`Cmd+H`** (`⌘H`) ou **`Cmd+Shift+Period`** (`⇧⌘.`) ou execute o comando **`cm_ShowSysFiles`**. Arquivos Unix ocultos (arquivos começando com um ponto, como `.zshrc`, `.gitignore`, `.env`) alternam entre os estados visível e oculto imediatamente.

#### P5: Como abro uma janela do Terminal macOS no diretório atual?

Pressione **`Ctrl+J`** (`⌃J`) ou execute o comando **`cm_RunTerm`**. ATBCmder gera uma nova sessão do macOS Terminal (ou iTerm2) com seu diretório de trabalho atual definido para o caminho exato do seu painel de arquivos ativo.

#### P6: O ATBCmder oferece suporte a Macs Intel (x86_64)?

Atualmente, o ATBCmder é compilado nativamente e exclusivamente para Macs **Apple Silicon (M1/M2/M3/M4, arquitetura ARM64)** para aproveitar totalmente a memória unificada da Apple, a aceleração de hardware Metal e os subsistemas Neural Engine. **Macs Intel (x86_64) não são suportados no momento.** 

---

## 4. Dicas profissionais e lista de verificação de manutenção do sistema

Para manter o desempenho do ATBCmder em velocidade máxima em todos os fluxos de trabalho corporativos: 

- **Manutenção semanal de cache**: se você navega frequentemente em cartões de câmera de alta resolução, limpe caches temporários de miniaturas periodicamente em **Configuração ➔ Opções ➔ Miniaturas ➔ Limpar cache de miniaturas** para recuperar espaço em disco. 
- **Auditoria de Chaves**: Se você alternar senhas em servidores SFTP ou SMB remotos, atualize suas credenciais no ATBCmder via **Rede ➔ Gerenciar conexões de rede...**. Editar e salvar atualiza o item de credencial correspondente em suas Chaves do macOS perfeitamente. 
- **Otimização de fila em segundo plano**: para transferências de vários gigabytes em redes de 1 Gbps ou 10 Gbps, ajuste os tamanhos de buffer de blocos em **Configuração ➔ Opções ➔ Operações de arquivo** para maximizar a saturação do barramento. 
- **Preservar permissões UNIX**: ao copiar scripts ou binários compilados entre unidades macOS APFS, certifique-se de que **Preservar atributos e permissões de arquivo** esteja marcado na caixa de diálogo Copiar (`F5`), mantendo os sinalizadores de execução (`chmod +x`) automaticamente. 

--- 

<div align="center"> 
<p><strong>ATBCmder Guia do usuário e portal de documentação</strong></p> 
<p> 
<a href="index.md">&larr; Retornar ao Portal de Documentação</a> &nbsp;&bull;&nbsp; 
<a href="getting_started.md">Capítulo 1: Fundamentos</a> &nbsp;&bull;&nbsp; 
<a href="keyboard_shortcuts.md">Capítulo 8: Atalhos</a> &nbsp;&bull;&nbsp; 
<a href="download.md">Capítulo 10: Download e instalação &rarr;</a> 
</p> 
</div>