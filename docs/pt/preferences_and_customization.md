# Capítulo 7: Preferências e personalização

Um gerenciador de arquivos verdadeiramente eficiente deve se adaptar ao seu fluxo de trabalho, e não forçá-lo a se adaptar aos seus padrões. Cada engenheiro, administrador de sistema, arquivista digital e profissional criativo traz memória muscular, requisitos de exibição e hábitos operacionais distintos: alguns dependem estritamente das teclas de função ortodoxas do Norton Commander / Total Commander (`F1`–`F10`), enquanto outros esperam atalhos nativos do macOS (`Cmd+C`, `Cmd+V`, `Cmd+O`); alguns exigem ajuste automático de coluna dinâmico com métricas tipográficas de subpixel, enquanto outros precisam de limites de coluna fixos e rígidos; alguns exigem monitoramento agressivo de eventos do sistema de arquivos em tempo real, enquanto outros são executados em compartilhamentos de rede de alta latência, onde a pesquisa passiva é obrigatória. 

O ATBCmder foi projetado desde o início para total configurabilidade. Por meio de sua **caixa de diálogo de preferências** modular (`Cmd+,` / `⌘,` / `cm_Options`), **Editor de teclas de atalho** intuitivo com detecção de conflitos em tempo real, **Mecanismo de ajuste automático de colunas** inteligente, **Associações de arquivos** personalizáveis com macros de token externas e **Pacotes de configuração ZIP** portáteis (`cm_ExportConfiguration`), o ATBCmder permite ajustar todas as dimensões do seu ambiente de painel duplo e transportar sua configuração personalizada perfeitamente em todos os seus sistemas Mac. 

---

## 1. Guia de início rápido visual: Centro de preferências e matriz de comandos

O ATBCmder centraliza todas as configurações do usuário em uma arquitetura de preferências unificada composta por 16 páginas de configuração especializadas, um mecanismo de mapeamento de teclas de atalho isolado e uma camada de armazenamento XML atômico. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          ATBCMDER PREFERENCES CENTER (Cmd+,)                           │
├──────────────────────┬─────────────────────────────────────────────────────────────────┤
│  CATEGORY NAVIGATION │  ACTIVE CONFIGURATION PAGE                                      │
├──────────────────────┼─────────────────────────────────────────────────────────────────┤
│  • General           │  Column Auto-Fit Mode:                                          │
│  • Hotkeys           │  [ Average Mode (Smart Padding)                       ▼ ]       │
│  • Language          │                                                                 │
│  • File Views        │  Average Mode Padding Factor: [ 1.25x ]                         │
│  • Auto Refresh      │                                                                 │
│  • Operations        │  Sorting Behavior:                                              │
│  • Packer            │  [X] Natural (numeric) sorting: photo1.jpg < photo10.jpg        │
│  • Plugins           │  [X] Case-sensitive sorting                                     │
│  • Directory Hotlist │  Folder Position: [ Folders First                     ▼ ]       │
│  • Favorite Tabs     │                                                                 │
│  • Editor            │  Thumbnail Generation:                                          │
│  • Viewer            │  Default Size: [ 128 px ]   Cache: [~/.cache/atbcmder]          │
│  • Toolbar           │                                                                 │
│  • Middle Toolbar    │  Date/Time Format:                                              │
│  • Log               │  Long Format: [ %Y-%m-%d %H:%M:%S                             ] │
│  • Quick Search      │                                                                 │
│  • Semantic Filter   │  [ Revert Changes ]                   [ Apply ] [ OK ] [Cancel] │
├──────────────────────┴─────────────────────────────────────────────────────────────────┤
│  CONFIG BACKEND:  atbcmder.xml  |  atbcmder_hotkeys.xml  |  favtabs.xml  |  hotlist.xml│
│  PORTABILITY:     cm_ExportConfiguration (ZIP)  ➔  cm_ImportConfiguration (ZIP)        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Preferências de matriz dupla e folha de referências de personalização

| Ação | Atalho do macOS | Chave do Comandante Clássico | ID do comando | Descrição | 
| :--- | :--- | :--- | :--- | :--- | 
| **Abrir Preferências** | `Cmd+,` / `⌘,` | `Alt+O` / `⌥O` | `cm_Options` | Abre a caixa de diálogo principal de Preferências de várias páginas. | 
| **Configurar teclas de atalho** | `Cmd+,` ➔ Teclas de atalho | — | `cm_Options` (teclas de atalho) | Acesso direto à tabela de vinculação de atalhos de teclado. | 
| **Configurar associações de arquivos**| Menu: Configuração | — | `cm_FileAssoc` | Mapeia extensões de arquivo para visualizadores/editores internos ou externos. | 
| **Configuração da lista de procurados do diretório** | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | Edita marcadores de pastas salvas e teclas de atalho ativas (`Ctrl+D` para abrir a lista de procurados). | 
| **Configurar guias favoritas** | Menu: Configuração | — | `cm_ConfigFavoriteTabs`| Gerencia conjuntos de guias de pastas de painel duplo salvos. | 
| **Configurar arquivadores** | Menu: Configuração | — | `cm_ConfigArchivers` | Configura executáveis ​​de arquivador externo e regras de compactação. | 
| **Configuração de exportação** | Menu: Configuração | — | `cm_ExportConfiguration`| Exporta todos os arquivos XML de configuração para um pacote portátil `.zip`. | 
| **Configuração de importação** | Menu: Configuração | — | `cm_ImportConfiguration`| Restaura arquivos XML de configuração de um pacote `.zip`. | 
| **Abra o diretório de configuração** | Menu: Configuração | — | `cm_OpenConfigDirectory`| Navega no painel ativo diretamente para a pasta de configuração do ATBCmder. | 
| **Salve as configurações imediatamente** | Menu: Configuração | — | `cm_ConfigSaveSettings`| Libera todas as alterações de configuração na memória para o disco imediatamente. | 
| **Salvar posição da janela** | Menu: Configuração | — | `cm_ConfigSavePos` | Persiste a geometria da janela atual e as proporções do divisor. | 
| **Alternar dicas de ferramentas de arquivo** | Preferências: Visualizações de arquivos | — | *(Preferências)* | Ativa ou desativa dicas de ferramentas de metadados flutuantes detalhadas. | 
| **Conceder permissões do sistema** | Menu: Configuração | — | `cm_GrantFilesystemAccess`| Inicia o guia de integração do macOS App Sandbox Full Disk Access. | 

---

## 2. A caixa de diálogo de preferências, anatomia e navegação (`Cmd+,` / `cm_Options`)

A sala de controle central do ATBCmder é a **Diálogo de Preferências**. Você pode invocá-lo a qualquer momento pressionando **`Cmd+,`** (`⌘,`) no macOS, escolhendo **ATBCmder ➔ Preferências...** no menu do aplicativo ou executando `cm_Options` através da Barra de Comando Semântica (`/`).

### 2.1 Layout de diálogo e modelo de interação

A caixa de diálogo Preferências utiliza um layout dividido com detalhes mestres projetado para maior clareza e acessibilidade do teclado: 

1. **Lista de navegação por categoria (esquerda)**: um seletor vertical com uma fonte de interface legível de 14 pontos e uma barra lateral fixa de 195 pixels. Navegue entre as categorias usando as teclas de seta `Up` e `Down` ou clique com o mouse. 
2. **Área de rolagem de página empilhada (direita)**: Um amplo painel de configuração fechado em um `QScrollArea` sem moldura. À medida que você alterna as categorias, a página de configurações correspondente aparece suavemente, sem causar redimensionamento da caixa de diálogo ou oscilação da janela. 
3. **Matriz de botões de ação (inferior)**: 
- **OK**: valida todos os campos de entrada em todas as páginas, grava as configurações modificadas no disco (`atbcmder.xml`), aciona a retradução e atualizações do tema e fecha a caixa de diálogo. 
- **Aplicar**: confirma todos os parâmetros modificados imediatamente sem descartar a caixa de diálogo. Isso é ideal para testar fontes de interface do usuário, variações de tema, preenchimento de colunas e intervalos de atualização automática em tempo real. 
- **Cancelar**: Descarta quaisquer alterações não salvas feitas na sessão atual. Se você visualizou um tema sem aplicá-lo, o ATBCmder reverterá automaticamente a interface para o tema anterior. 

```
┌────────────────────────────────────────────────────────────────────────────┐
│ Preferences Dialog Sidebar Navigation                                      │
├────────────────────────────────────────────────────────────────────────────┤
│  [ General ]         Basic UI, file lists, confirmation prompts, theme     │
│  [ Hotkeys ]         Keyboard shortcuts, context scoping, conflict manager │
│  [ Language ]        30+ real-time GUI translations without restart        │
│  [ File Views ]      Sorting rules, column auto-fitting, datetime formats  │
│  [ Auto Refresh ]    File monitoring events, polling, background sleep     │
│  [ Operations ]      Collision defaults (overwrite/rename), permissions    │
│  [ Packer ]          Archive formats (ZIP, 7Z, TAR), external binaries     │
│  [ Directory Hotlist]Bookmarks management, target panels, drag-and-drop    │
│  [ Favorite Tabs ]   Dual-panel workspace sets, layout persistence         │
│  [ Editor ]          Internal code editor typography, external editor CLI  │
│  [ Viewer ]          Universal Lister fonts, image rendering, external CLI │
│  [ Toolbar ]         Main button bar layout, custom commands, icon picker  │
│  [ Middle Toolbar ]  Middle splitter button bar, quick actions             │
│  [ Log ]             Operation audit trails, file logging, rotation        │
│  [ Quick Search ]    In-panel letter search, matching algorithms           │
│  [ Semantic Filter ] Natural language command input, spotlight integration │
│  [ Tabs ]            Folder tab bar styling, close buttons, locking rules  │
└────────────────────────────────────────────────────────────────────────────┘
```
 

---

### 2.2 Diretório abrangente de páginas de configuração

Cada página na caixa de diálogo Preferências aborda um domínio funcional específico:

| Página | Módulo de Implementação | Controles de configuração primária | 
| :--- | :--- | :--- | 
| **Geral** | `page_general.py` | Visibilidade de arquivos ocultos, ícones de arquivos, caixas de diálogo de confirmação de exclusão/substituição, integração com a Lixeira do sistema, tamanho do buffer de copiar/mover (4 KB a 10 MB), seleção de tema, tamanho de fonte global, alternância de minimizar para bandeja e tecla de atalho global para mostrar/ocultar janela (`Cmd+Opt+H`). | 
| **Teclas de atalho** | `page_hotkeys.py` | Pesquisa de comandos multicontexto, vinculação de acordes de atalho primário e secundário, avisos automatizados de colisão de atalhos e redefinição de padrão de fábrica. | 
| **Idioma** | `page_language.py` | Seletor de localização dinâmico com suporte para mais de 30 idiomas (inglês, alemão, francês, chinês simplificado, japonês, russo, espanhol, etc.) com tradução instantânea da interface do usuário ao vivo. | 
| **Visualizações de arquivos** | `page_fileview.py` | Classificação numérica natural e com distinção entre maiúsculas e minúsculas, posicionamento de classificação de pastas (pastas primeiro, arquivos primeiro, mistos), posicionamento de arquivos novos/atualizados, modos de ajuste automático de coluna (Fixo, Médio, Máx.), controle deslizante de fator de preenchimento e formatos de data e hora personalizados. | 
| **Atualização automática** | `page_auto_refresh.py` | Monitoramento de criação/exclusão/renomeação do sistema de arquivos, monitoramento de alteração de atributos de arquivo, intervalo de fallback de pesquisa de timer, alternância de desativação quando em segundo plano e lista de filtros de exclusão de diretório. | 
| **Operações** | `page_operations.py` | Políticas padrão de colisão de arquivos (Ask, Overwrite, Skip, Overwrite Older, Auto-Rename Target), políticas de colisão de diretórios (Ask, Merge, Overwrite, Skip), pré-alocação de espaço livre, manipulação de link simbólico, preservação de permissão/timestamp e verificação. | 
| **Embalador** | `page_packer.py` | Formato de arquivo de compactação padrão (`zip`, `7z`, `tar.gz`, `tar.bz2`, `tar.xz`, `tar`), caminhos executáveis externos para 7-Zip, GNU Tar, Gzip, Utilitários Bzip2 e XZ. | 
| **Lista de favoritos do diretório**| `page_hotlist.py` | Gerenciador de favoritos interativo: adicione, remova e reordene (`Drag & Drop`) diretórios favoritos, especifique caminhos de destino de painel duplo e atribua teclas de acesso rápido. | 
| **Guias favoritas** | `page_favorite_tabs.py` | Gerenciador de instantâneos do espaço de trabalho: salve, renomeie, reordene e restaure layouts de diretório de painel duplo com várias guias. | 
| **Editor** | `page_editor.py` | Família de fontes do editor de código interno, tamanho da fonte, largura da parada de tabulação, quebra de linha e alternância de número de linha; caminho executável do editor externo e argumentos de linha de comando. | 
| **Visualizador** | `page_viewer.py` | Tipografia de texto Universal Lister, paradas de tabulação, margens, quebra de linha, visibilidade de cursor, opções de renderização de imagem (rotação automática EXIF, modos de zoom, grade de transparência) e ferramenta CLI de visualizador externo. | 
| **Barra de ferramentas** | `page_toolbar.py` | Personalização da barra de botões superior: controle deslizante de tamanho do ícone (16–64 px), controle deslizante de tamanho da barra, estilo de botão plano, alternância de legendas, árvore de hierarquia de comandos e caixa de diálogo de seletor de ícones personalizado. | 
| **Barra de ferramentas do meio** | `page_toolbar.py` | Configuração da barra de ferramentas do divisor vertical central: tamanhos de ícones, botões de ação e reordenação de layout. | 
| **Registro** | `page_log.py` | Registro de auditoria operacional: destino do arquivo de log, substituição de caminho de token, tamanho máximo do arquivo de log, comportamento de rotação de log e filtros de eventos de operação específicos (copiar, mover, excluir, descompactar). | 
| **Pesquisa rápida** | `page_quicksearch.py` | Modo de pesquisa rápida do teclado (correspondência exata, início, fim, curingas), distinção entre maiúsculas e minúsculas e tempo limite de fechamento automático. | 
| **Filtro Semântico** | `page_semantic_filter.py` | Comportamento da barra de comando de linguagem natural incorporada (`/`), back-ends do provedor de pesquisa e rejeição de sugestões. | 
| **Guias** | `page_tabs.py` | Aparência da guia da pasta: visibilidade do botão fechar, layout da guia com várias linhas versus guias de rolagem, comportamento de navegação da guia bloqueada e confirmações de fechamento da guia. |

---

### 2.3 Tema em tempo real e troca dinâmica de idioma

Ao contrário dos utilitários legados que exigem fechar e reiniciar o aplicativo após alterar as configurações de aparência, o ATBCmder apresenta **Temas e localização hot-swappable**: 

1. **Visualizações de tema**: Abra **Geral**, escolha entre `Classic`, `Light`, `Dark` ou `macOS Native (Stylish)` e observe a mudança de estilo da janela instantaneamente por meio da injeção de folha de estilo Qt. Se você pressionar **Cancelar**, o tema anterior será restaurado perfeitamente. 
2. **Tradução instantânea**: abra **Idioma**, selecione seu dialeto preferido na lista de mais de 30 localidades traduzidas e clique em **Aplicar**. O título da janela, a barra lateral da categoria, os menus, os botões, as barras de status e os prompts de diálogo são renderizados imediatamente no idioma de destino por meio do pipeline de tradução dinâmico `tr()` do ATBCmder. 

![Language Settings](images/language_settings.png) 
*Figura 7.1: A página Preferências de idioma que permite localização instantânea e sem reinicialização em mais de 30 idiomas suportados.* 

---

## 3. Personalização de atalhos de teclado e gerenciamento de conflitos

A eficiência do teclado é a filosofia central do gerenciamento de arquivos em painel duplo. O **Editor de teclas de atalho** (`page_hotkeys.py`) do ATBCmder fornece controle total sobre acordes de atalho, ao mesmo tempo em que impõe estrito isolamento de contexto e prevenção de colisões. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              HOTKEY CONFIGURATION PAGE                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Hotkey Context: [ FilePanel                                                 ▼ ]       │
│  Filter Commands: [ copy                                                     ] ⌧       │
├──────────────────────┬────────────────────────┬───────────────────┬────────────────────┤
│ Command ID           │ Description            │ Primary Shortcut  │ Secondary Shortcut │
├──────────────────────┼────────────────────────┼───────────────────┼────────────────────┤
│ cm_Copy              │ Copy Files or Folders  │ F5                │ Cmd+C              │
│ cm_CopySamePanel     │ Duplicate File in Pane │ Shift+F5          │ Cmd+D              │
│ cm_CopyRightPanel     │ Copy to Right Panel    │ Alt+F5            │                   │
│ cm_CopyFullNamesToClip│ Copy Full Path Names   │ Ctrl+Shift+C      │ Cmd+Opt+C         │
├──────────────────────┴────────────────────────┴───────────────────┴────────────────────┤
│  [ Edit Shortcut... ]           [ Clear Shortcuts ]            [ Reset to Defaults ]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Isolamento e escopo de contexto

Para evitar o esgotamento dos atalhos, o ATBCmder separa as combinações de teclas em **Escopos de Contexto**. Um atalho definido em um contexto não interfere com teclas idênticas em janelas não relacionadas: 

- **Principal**: Atalhos globais de aplicativos disponíveis em todas as janelas (por exemplo, `Cmd+,` para Preferências, `Cmd+Q` para Sair). 
- **FilePanel**: Ativo sempre que a lista de arquivos esquerda ou direita tiver o foco do teclado (por exemplo, `F5` copia, `Space` calcula o tamanho do diretório, `Backspace` navega para o pai). 
- **Visualizador**: Ativo dentro do Universal Lister (`F3`): controla codificações de texto, alternância de visualização hexadecimal (`2` / Modo hexadecimal), zoom de imagem e reprodução de mídia. 
- **Editor**: Ativo dentro do editor de texto integrado (`F4`): controla realce de sintaxe, recuo, localização/substituição (`Cmd+F`) e salvamento de arquivo (`Cmd+S`). 
- **Diferente**: Ativo dentro da diferença de arquivo lado a lado: navegação de pedaço (`F7`/`F8`), sincronização de linha e operações de mesclagem. 
- **FindFiles**: Ativo na caixa de diálogo Pesquisa Multifiltro: acionando novas pesquisas, navegando pelos resultados e alimentando a caixa de listagem. 
- **MultiRename**: Ativo na ferramenta Batch Multi-Rename: manipulação de contador, inserção de token e execução. 

---

### 3.2 Arquitetura de ligação dupla (atalhos primários e secundários)

ATBCmder permite atribuir **duas combinações de atalhos distintas** a cada comando: 

- **Atalho principal**: Seu acorde de memória muscular principal (por exemplo, `F5` para usuários clássicos do Commander). 
- **Atalho secundário**: um acorde alternativo (por exemplo, `Cmd+C` para ergonomia nativa do macOS). 

Ambos os atalhos permanecem ativos simultaneamente no contexto especificado. Ao navegar nos menus, o ATBCmder exibe automaticamente o atalho principal próximo ao texto do item de menu para uma referência visual clara. 

---

### 3.3 Receita passo a passo: Personalizando um atalho de teclado

Siga este passo a passo prático para religar um comando existente ou atribuir um atalho secundário: 

1. Pressione **`Cmd+,`** (`⌘,`) para abrir Preferências e selecione **Teclas de atalho** na barra lateral esquerda. 
2. Selecione o **Contexto de tecla de atalho** apropriado no menu suspenso (por exemplo, `FilePanel`). 
3. Digite o nome do comando ou uma palavra-chave na caixa **Comandos de filtro** (por exemplo, `Wipe` ou `Terminal`). A tabela filtra as entradas correspondentes em tempo real. 
4. Clique duas vezes na linha de comando ou selecione a linha e clique em **Editar...**. 
5. Na caixa de diálogo **Editar tecla de atalho**: 
- Clique dentro da caixa **Atalho principal** e pressione a combinação de teclas desejada (por exemplo, `Ctrl+Alt+T`). ATBCmder captura o acorde de forma limpa, restringindo as sequências a um único acorde simultâneo. 
- (Opcional) Clique dentro da caixa **Atalho secundário** e pressione uma combinação alternativa (por exemplo, `Cmd+Shift+T`). 
6. Clique em **Salvar**. 

```
┌────────────────────────────────────────────────────┐
│ Edit Hotkey Dialog                                 │
├────────────────────────────────────────────────────┤
│ Command:             cm_RunTerm - Run Terminal     │
│ Primary Shortcut:    [ Ctrl+J                    ] │
│ Secondary Shortcut:  [ Cmd+Opt+T                 ] │
│                                                    │
│                           [ Cancel ]    [ Save ]   │
└────────────────────────────────────────────────────┘
```
 

---

### 3.4 Detecção automatizada de colisões e avisos de conflito

Se você tentar atribuir um acorde de tonalidade que já foi reivindicado por outro comando dentro do mesmo contexto, o mecanismo de detecção de colisão do ATBCmder intervém imediatamente. Uma caixa de diálogo de alerta exibe a atribuição conflitante: 

> [!WARNING] 
> **Conflito de atalho detectado** 
> O atalho `Ctrl+M` já está atribuído a `cm_MultiRename` no contexto `FilePanel`. 
> Deseja sobrescrevê-lo e reatribuir `Ctrl+M` para `cm_MarkCurrentExtension`? 

- Clicar em **Sim** desvincula automaticamente `Ctrl+M` do comando antigo e o aplica ao comando recém-selecionado. 
- Clicar em **Não** cancela a edição, preservando as vinculações existentes sem modificação. 

---

### 3.5 Tecla de atalho global para mostrar/ocultar janela (`Cmd+Opt+H` / `Ctrl+Alt+H`)

Para usuários avançados que preferem manter o ATBCmder funcionando discretamente em segundo plano: 

1. Abra **Preferências ➔ Geral**. 
2. Marque **Minimizar para bandeja do sistema**. 
3. Localize **Tecla de atalho Mostrar/Ocultar janela** (padrão: `Ctrl+Alt+H` / `⌘⌥H`). 
4. Clique na caixa de sequência para registrar qualquer acorde de tecla de atalho global personalizado. 
5. Clique em **Aplicar**. 

Agora você pode chamar instantaneamente o ATBCmder para a frente ou dispensá-lo para segundo plano de qualquer lugar no macOS, mesmo ao trabalhar em outros aplicativos de tela cheia. 

---

## 4. Visualizações de arquivos, modos de coluna e gerenciamento de miniaturas

A página **Visualizações de arquivos** (`page_fileview.py`) controla como os diretórios são renderizados, medidos, classificados e apresentados nos painéis duplos. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              FILE VIEWS CONFIGURATION                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Sorting Rules:                                                                        │
│  [X] Case-sensitive sorting             [X] Natural (numeric) sorting                  │
│  [ ] Special sorting rules                                                             │
│  Folder sort mode:        [ Folders first                                    ▼ ]       │
│  New files position:      [ Sorted                                           ▼ ]       │
│  Updated files position:  [ Top                                              ▼ ]       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Column Widths & Auto-Fit Engine:                                                      │
│  Column auto-fit mode:    [ Average mode                                     ▼ ]       │
│  Average mode padding:    [ 1.20x ]  (Range: 1.00x - 5.00x)                            │
│  Hint: In Fixed mode, drag column dividers to save exact pixel widths per side.        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Date/Time Formatting:                                                                 │
│  Long datetime format:    [ %Y-%m-%d %H:%M:%S                                ]         │
│  Sync dirs format:        [ %Y.%m.%d %H:%M:%S                                ]         │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Motor de ajuste automático de coluna: os três modos

Os gerenciadores de arquivos de painel duplo geralmente enfrentam dificuldades com comprimentos variados de nomes de arquivos: colunas excessivamente largas causam rolagem horizontal, enquanto colunas excessivamente estreitas truncam extensões de arquivo críticas. ATBCmder resolve isso com três comportamentos distintos de ajuste automático: 

1. **Modo Fixo (`fixed`)**: 
- Desativa o recálculo automático. 
- As larguras das colunas permanecem exatamente onde você as posiciona. 
- **Arrastar manualmente**: quando você arrasta a borda vertical entre os cabeçalhos das colunas (por exemplo, entre `Name` e `Ext`), o ATBCmder captura a largura exata do pixel e a persiste separadamente para cada lado do painel (`column_widths_left` e `column_widths_right` em `atbcmder.xml`). 
2. **Modo médio (`average` — Padrão recomendado)**: 
- Avalia a largura tipográfica média (`QFontMetrics`) de todos os nomes de arquivos visíveis no diretório. 
- Multiplica a largura média pelo **Fator de preenchimento** configurado (controle deslizante ajustável de `1.0x` a `5.0x`, padrão `1.0x`–`1.25x`), adicionando 40 pixels para ícones de tipo de arquivo e espaço visual para respirar. 
- Impede que nomes de arquivos extremos (como um único nome de arquivo de log de 120 caracteres) empurrem todas as outras colunas para fora da tela. 
3. **Modo de largura máxima (`max`)**: 
- Verifica as entradas do diretório e expande a coluna para corresponder ao nome de arquivo único mais amplo, além do preenchimento de segurança (+50 px). 
- Garante que zero nomes de arquivos sejam truncados com reticências (`...`), ideal para arquivos de mídia e conjuntos de dados científicos. 

> [!TIP] 
> **Otimização de diretórios grandes**: 
> Em diretórios contendo dezenas de milhares de itens, medir cada string individual congelaria a interface. O ATBCmder aplica automaticamente a amostragem inteligente de etapas (`_MAX_SAMPLE = 200`), avaliando um subconjunto de linhas distribuído uniformemente para calcular métricas de tipografia em menos de 2 milissegundos, ignorando os marcadores do diretório pai (`..`). 

---

### 4.2 Opções de classificação de arquivos

Ajuste como os itens se ordenam nas visualizações de tabela: 

- **Classificação natural (numérica)**: Quando ativado, os números dentro das strings são comparados matematicamente: `file1.txt`, `file2.txt`, `file10.txt` (em vez de `file1.txt` alfabético, `file10.txt`, `file2.txt`). 
- **Classificação com distinção entre maiúsculas e minúsculas**: quando marcada, os caracteres maiúsculos precedem os caracteres minúsculos de acordo com os valores ordinais ASCII/Unicode (`File.txt` classifica antes de `apple.txt`). Quando desmarcada, a classificação não diferencia maiúsculas de minúsculas. 
- **Modo de classificação de pasta**: 
- `Folders first`: Os diretórios são agrupados na parte superior do painel acima de todos os arquivos. 
- `Files first`: Os arquivos são listados primeiro, com os diretórios colocados na parte inferior. 
- `Mixed`: Arquivos e pastas são classificados em ordem alfabética em uma sequência unificada. 
- **Posição de arquivos novos e atualizados**: controle onde os arquivos recém-criados ou modificados aparecem durante as atualizações do sistema de arquivos ao vivo (`Sorted`, `Top` ou `Bottom`). 

---

### 4.3 Visualização de grade em miniatura e mecânica de cache

Para fotógrafos, designers e editores de vídeo, o ATBCmder fornece uma **Visualização em grade de miniaturas** integrada (`cm_ThumbnailsView`), substituindo linhas tabulares por visualizações de imagens visuais. 

![Thumbnail Grid View](images/thumbnails_grid_view.png) 
*Figura 7.2: Visualização de miniaturas de alto desempenho exibindo visualizações de imagens com espaçamento de grade personalizado.*

#### Dimensionamento e zoom dinâmico

- **Tamanho padrão da miniatura**: configurável de 48 px a 512 px (padrão: 128 px). 
- **Pinch-to-Zoom interativo**: nos trackpads da Apple, use gestos padrão de pinçar com dois dedos ou segure **`Ctrl`** enquanto rola a roda do mouse para dimensionar miniaturas dinamicamente em tempo real.

#### Arquitetura de cache multicamadas

A geração de miniaturas para fotos RAW de alta resolução de 48 megapixels ou SVGs vetoriais complexos exige muito da CPU. ATBCmder emprega uma arquitetura robusta de cache de duas camadas: 

1. **Cache LRU na memória**: retém 500 objetos `QPixmap` descompactados na RAM para rolagem instantânea e suave de 60fps. 
2. **Cache de disco permanente**: armazenado localmente no diretório de cache do usuário: 
- caminho macOS/Linux: `~/.cache/atbcmder/thumbnails/` 
- As chaves de cache são geradas por meio de hashes criptográficos SHA-256 combinando caminho do arquivo, carimbo de data/hora de modificação do arquivo (`mtime`), tamanho de pixel solicitado e versão do esquema de cache: 
$$\text{Chave de cache} = \text{SHA256}(\text{caminho do arquivo} + \text{mtime} + \text{tamanho} + \text{versão})$$ 

- Se um arquivo de imagem for editado ou atualizado no disco, seu carimbo de data/hora muda, invalidando imediatamente entradas de cache obsoletas e acionando a nova renderização automatizada em segundo plano. 
3. **Threads de trabalho em segundo plano**: o processamento de imagens é transferido para um pool de trabalhadores `QThread` dedicado utilizando pipelines Pillow (PIL) ou `QImage` acelerados por hardware, garantindo que a interface de painel duplo nunca gagueje durante importações de lotes pesados. 

---

### 4.4 Formatação personalizada de data e hora

ATBCmder permite que você defina strings de formatação de carimbo de data/hora personalizadas usando a sintaxe `strftime` padrão do Python: 

- **Formato de data e hora longo** (padrão: `%Y-%m-%d %H:%M:%S`): Controla a exibição da data na visualização de coluna completa (`2026-09-06 14:30:00`). 
- **Formato de diretórios de sincronização** (padrão: `%Y.%m.%d %H:%M:%S`): controla a apresentação do carimbo de data/hora na caixa de diálogo do Sincronizador de diretório. 

| Ficha | Descrição | Exemplo de saída | 
| :--- | :--- | :--- | 
| `%Y` | Ano de 4 dígitos | `2026` | 
| `%m` | Mês de 2 dígitos (`01`–`12`) | `09` | 
| `%d` | Dia do mês com 2 dígitos (`01`–`31`) | `06` | 
| `%H` | Hora de 2 dígitos no formato de 24 horas (`00`–`23`) | `14` | 
| `%I` | Hora de 2 dígitos no formato de 12 horas (`01`–`12`) | `02` | 
| `%p` | Designação AM/PM | `PM` | 
| `%M` | Minuto de 2 dígitos (`00`–`59`) | `30` | 
| `%S` | Segundo de 2 dígitos (`00`–`59`) | `15` | 

---

## 5. Atualização automática do sistema de arquivos e sensibilidade de monitoramento

Ao colaborar em bases de código compartilhadas, baixar recursos do navegador ou executar tarefas de compilação em segundo plano, o conteúdo do diretório muda constantemente. A página **Atualização automática** (`page_auto_refresh.py`) equilibra a precisão da IU em tempo real com o consumo de CPU e bateria. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              AUTO-REFRESH CONFIGURATION                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [X] Refresh file list:                                                                │
│      [X] When files are created, deleted or renamed                                    │
│      [X] When size, date or attributes change                                          │
│      Polling interval (seconds): [ 5 ]                                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Disable auto-refresh:                                                                 │
│      [X] When application is in the background                                         │
│      [X] For the following paths and their subdirectories:                             │
│          ┌──────────────────────────────────────────────────────────────────────────┐  │
│          │ /Volumes/NetworkShare/LargeMediaArchive                                  │  │
│          │ /Users/username/Developer/linux-kernel/                                  │  │
│          │ /Users/username/work/heavy_project/node_modules/                         │  │
│          └──────────────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Gatilhos de eventos versus substituto de pesquisa

ATBCmder combina monitoramento de eventos do sistema operacional nativo com um substituto de pesquisa inteligente: 

- **Monitoramento de eventos (`watch_file_name_change`)**: aproveita notificações nativas do kernel do sistema operacional (macOS `FSEvents` / `kqueue`) para detectar criações, exclusões e renomeações de arquivos sem sobrecarga de CPU. 
- **Monitoramento de atributos (`watch_attributes_change`)**: rastreia expansões de tamanho de arquivo, atualizações de carimbo de data/hora e ajustes de modo de permissão. 
- **Intervalo de Fallback de Polling (`attr_poll_interval`)**: Configurável de 1 a 60 segundos (padrão: 5 segundos). 
*Por que a pesquisa é necessária?* Montagens de armazenamento de rede remota (SMB, CIFS, NFS, SFTP VFS) frequentemente falham ao emitir eventos de sistema de arquivos do sistema operacional nativo quando clientes remotos fazem alterações. O cronômetro de pesquisa em segundo plano garante que suas listagens de painel remoto nunca fiquem desatualizadas. 

---

### 5.2 Conservação de bateria e CPU: Desativar quando em segundo plano

Em laptops macOS que funcionam com bateria, os observadores ativos do sistema de arquivos podem consumir energia desnecessária. 

- A verificação de **Quando o aplicativo está em segundo plano** (`watch_only_foreground`) suspende automaticamente todos os temporizadores de pesquisa e observadores de eventos ativos no momento em que o ATBCmder perde o foco da janela. 
- Quando você volta para o ATBCmder, os painéis executam imediatamente uma única atualização coordenada, atualizando instantaneamente todas as listagens de diretórios. 

---

### 5.3 Filtros de exclusão de caminho

Diretórios com alta rotatividade — como `node_modules`, repositórios de metadados Git (`.git`), caches de artefatos de compilação (`target/`, `build/`) e arquivos de banco de dados locais — geram milhares de eventos de disco por minuto. 

1. Verifique **Para os seguintes caminhos e seus subdiretórios** (`watch_exclude_dirs`). 
2. Insira um caminho de diretório absoluto por linha na área de texto de exclusão: 
   ```text
   /Users/username/Developer/project/node_modules
   /Users/username/Developer/linux/.git
   /Volumes/ProductionNAS/RenderingQueue
   ```
 

3. Clique em **Aplicar**. O ATBCmder ignora eventos do sistema de arquivos que ocorrem dentro dessas árvores de caminho, eliminando atualizações indesejadas da interface do usuário e picos de CPU. 

---

## 6. Associações de arquivos personalizados e integração de ferramentas externas

Clicar duas vezes em um arquivo ou pressionar **`Enter`** normalmente o abre usando o aplicativo padrão do sistema. O **Sistema de associações de arquivos** do ATBCmder (`cm_FileAssoc` / `file_associations.py`) permite definir ações personalizadas para padrões de arquivos específicos, mapeando-os para comandos internos ou aplicativos de terminal/GUI externos.

### 6.1 Arquitetura e especificidade de padrões

As associações de arquivos são avaliadas em ordem de especificidade do padrão: o padrão glob mais longo e específico é correspondido primeiro: 

$$\text{Ordem de especificidade: } \texttt{*.min.js} \longrightarrow \texttt{*.js} \longrightarrow \texttt{text/*} \longrightarrow \texttt{*}$$ 

Cada associação pode conter múltiplas ações (por exemplo, "Abrir em VS Code", "Visualizar Hex", "Executar em Python"), com uma designada como a ação padrão primária acionada em `Enter`. 

---

### 6.2 Substituições de macro de token para comandos externos

Ao iniciar ferramentas externas ou scripts de linha de comando, o ATBCmder substitui automaticamente as macros de token pelos metadados do arquivo ativo: 

| Token Macro | Significado | Valor de exemplo | 
| :--- | :--- | :--- | 
| **`%f`** | Caminho absoluto completo do arquivo selecionado | `/Users/username/Documents/report.pdf` | 
| **`%d`** | Caminho do diretório que contém o arquivo | `/Users/username/Documents` | 
| **`%n`** | Nome de arquivo base sem extensão | `report` | 
| **`%e`** | Extensão de arquivo sem ponto inicial | `pdf` | 

---

### 6.3 Receitas Práticas de Associação

#### Receita 1: Abra scripts Python no código do Visual Studio

- **Padrão**: `*.py` 
- **Etiqueta**: `Edit in VS Code` 
- **Comando**: `code %f` 
- **Tipo de ação**: Comando Shell Externo

#### Receita 2: execute o script Python no terminal

- **Padrão**: `*.py` 
- **Etiqueta**: `Execute Script` 
- **Comando**: `python3 %f` 
- **Tipo de ação**: Comando Shell Externo

#### Receita 3: Visualizar Markdown no Pré-visualizador Dedicado

- **Padrão**: `*.md` 
- **Etiqueta**: `Preview in Typora` 
- **Comando**: `open -a Typora %f` 
- **Tipo de ação**: Comando Shell Externo

#### Receita 4: Compare o arquivo com o painel oposto no Beyond Compare

- **Padrão**: `*` 
- **Etiqueta**: `Compare with Target` 
- **Comando**: `bcomp %f %d` 
- **Tipo de ação**: Comando Shell Externo 

---

## 7. Personalização da barra de ferramentas e da barra de ferramentas intermediária

ATBCmder fornece duas barras de ferramentas personalizáveis: a **Barra de ferramentas principal** situada abaixo da barra de menu, e a **Barra de ferramentas intermediária** incorporada verticalmente no divisor que separa os dois painéis de arquivos. 

![Middle Toolbar](images/middle_toolbar.png) 
*Figura 7.3: A página de opções da barra de ferramentas central configurando botões divisores e gatilhos de ação rápida.*

### 7.1 Personalizando a aparência da barra de ferramentas

Abra **Preferências ➔ Barra de Ferramentas** ou **Preferências ➔ Barra de Ferramentas Central**: 

- **Controle deslizante de tamanho da barra**: ajusta a altura/largura da barra de ferramentas de 16 px a 64 px. 
- **Controle deslizante de tamanho do ícone**: dimensiona os ícones dos botões de 16 px a 64 px (padrão: 24 px). 
- **Botões planos**: alterna entre botões planos modernos sem bordas e botões elevados clássicos. 
- **Mostrar legendas**: exibe rótulos de texto abaixo ou ao lado dos ícones da barra de ferramentas. 

---

### 7.2 Adicionando itens e o seletor de ícones integrado

Os itens da barra de ferramentas são organizados em uma árvore hierárquica que suporta três tipos de elementos: 

1. **Separador**: Insere uma linha divisória visual ou espaçador entre grupos de botões. 
2. **Comando Interno**: Selecione qualquer um dos mais de 230 comandos `cm_*` do ATBCmder usando o campo de comando de preenchimento automático. 
3. **Comando Externo**: Especifique um comando shell externo, diretório de trabalho e tokens de parâmetro (`%f`, `%d`).

#### O seletor de ícones integrado (`IconPickerDialog`)

Ao configurar botões personalizados, clique no botão de visualização do ícone para abrir o **Seletor de ícones** integrado: 

- Apresenta um filtro de pesquisa instantânea em centenas de ícones SVG e PNG agrupados. 
- Exibe ícones em uma grade uniforme com visualização em alta resolução e nomes de hastes de ativos. 

```
┌────────────────────────────────────────────────────────────────────────┐
│ Icon Picker Dialog                                                     │
├────────────────────────────────────────────────────────────────────────┤
│ Search: [ terminal                                                   ] │
├──────────────────────────────────────────────────────┬─────────────────┤
│  ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐ │ PREVIEW:        │
│  │ 💻 │   │ 🖥️ │   │ ⌨️ │   │ ⚙️ │   │ 📁 │   │ 🔍 │ │                  │
│  └────┘   └────┘   └────┘   └────┘   └────┘   └────┘ │      💻         │
│  cm_RunTerm  console  terminal  bash   sh      zsh   │                 │
│  ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐ │ Name: cm_RunTerm│
│  │ 📄 │   │ ✏️ │   │ ✂️ │   │ 📋 │   │ 🗑️ │   │ 🔒 │ │ Size: 48x48     │
│  └────┘   └────┘   └────┘   └────┘   └────┘   └────┘ │ Format: SVG/PNG │
├──────────────────────────────────────────────────────┴─────────────────┤
│                                                [ Cancel ]  [ Select ]  │
└────────────────────────────────────────────────────────────────────────┘
```
 

---

### 7.3 Personalização da lista de favoritos do diretório e das guias favoritas

- **Lista de diretórios (`page_hotlist.py`)**: Gerencie seus favoritos `Ctrl+D`. Adicione caminhos atuais, reordene marcadores usando arrastar e soltar, configure a sincronização do painel de destino e atribua teclas de acesso. 
- **Guias favoritas (`page_favorite_tabs.py`)**: salve layouts completos de espaço de trabalho com várias guias e painel duplo. Restaure seus conjuntos exatos de diretórios de revelação ou edição de fotos com um clique. 

![Directory Hotlist](images/quick_access_paths.png) 
*Figura 7.4: Gerenciando marcadores e caminhos da lista de favoritos do diretório.* 

---

## 8. Portabilidade de configuração e modo de teste isolado

Seja migrando para um novo Mac, provisionando uma frota de máquinas de desenvolvimento ou compartilhando atalhos de teclado personalizados com colegas, o ATBCmder torna o backup de configuração e a implantação triviais.

### 8.1 Arquitetura de armazenamento de configuração

O ATBCmder armazena todas as configurações do usuário em arquivos XML legíveis e estruturados de forma limpa, localizados no diretório de configuração padrão do sistema operacional: 

- **Caminho padrão do macOS**: 
`~/Library/Preferências/atbcmder/` 

- **Caminho da sandbox do aplicativo macOS**: 
`~/Library/Containers/com.aitobox.atbcmder/Data/Library/Preferências/atbcmder/` 

- **Caminho Linux/UNIX**: 
`~/.config/atbcmder/` 

- **Comando de acesso direto**: 
Execute **`cm_OpenConfigDirectory`** (ou escolha **Configuração ➔ Abrir diretório de configuração** no menu) para navegar instantaneamente no painel ativo diretamente para esta pasta. 

```
~/Library/Preferences/atbcmder/
├── atbcmder.xml          # Core application configuration, geometry, themes, view rules
├── atbcmder_hotkeys.xml  # User keyboard shortcut overrides and custom bindings
├── favtabs.xml           # Saved favorite folder tab layouts and paths
├── hotlist.xml           # Directory Hotlist (Ctrl+D) bookmarks hierarchy
└── history.xml           # Recent directory jumps, command line history, search history
```
 

---

### 8.2 Exportando pacotes de configuração (`cm_ExportConfiguration`)

Para criar um backup portátil completo do seu ambiente ATBCmder: 

1. Escolha **Configuração ➔ Exportar configuração...** na barra de menu (ou execute `cm_ExportConfiguration`). 
2. Selecione seu diretório de destino e escolha um nome de arquivo (padrão: `atbcmder-config.zip`). 
3. Clique em **Salvar**. 

ATBCmder libera todas as alterações de memória pendentes no disco, reúne todos os arquivos XML de configuração (`atbcmder.xml`, `atbcmder_hotkeys.xml`, `favtabs.xml`, `hotlist.xml`) e os empacota em um arquivo ZIP atômico compactado. 

---

### 8.3 Importando pacotes de configuração (`cm_ImportConfiguration`)

Para restaurar um backup de configuração em uma nova máquina ou reverter para um estado bom conhecido: 

1. Escolha **Configuração ➔ Importar configuração...** na barra de menu (ou execute `cm_ImportConfiguration`). 
2. Selecione seu arquivo `atbcmder-config.zip` exportado anteriormente. 
3. Confirme o aviso: 
> A importação substituirá todas as configurações atuais pelo conteúdo do arquivo selecionado. Continuar? 
4. Clique em **Sim**. 

O ATBCmder descompacta o arquivo com segurança, verifica se todos os arquivos extraídos são configurações XML válidas, substitui os arquivos do disco ativo, recarrega o singleton interno `Config()` e atualiza os painéis de arquivos e os layouts de colunas imediatamente - tudo sem exigir a reinicialização do aplicativo. 

> [!IMPORTANT] 
> **Segurança Empresarial: Proteção Anti-Traversal** 
> ATBCmder impõe validação estrita de passagem de caminho durante a importação de configuração (sanitização `zipfile`). Qualquer membro de arquivo contendo separadores de caminho (`/`, `\`), travessias de diretório (`..`) ou extensões de arquivo não XML é rejeitado imediatamente, protegendo seu sistema operacional contra adulteração maliciosa de arquivo. 

---

### 8.4 Modo de teste isolado (`ATBCmder_test.sh`)

Ao desenvolver plug-ins personalizados, experimentar religações agressivas de teclas de atalho ou testar configurações beta, você deve evitar modificar a configuração diária do driver. 

ATBCmder oferece suporte ao redirecionamento completo de configuração por meio da variável de ambiente `ATBCMDER_CONFIG_PATH`. Um script de teste dedicado está incluído no repositório do projeto: 

```bash
# Launch ATBCmder in completely isolated test mode:
./scripts/ATBCmder_test.sh
```

#### Como funciona o modo de teste isolado:

1. Provisiona um diretório de teste temporário e limpo em `tests/.test_config/`. 
2. Copia as configurações de linha de base de fábrica de `src/atbcmder/resources/test_config.xml` para `tests/.test_config/atbcmder.xml`. 
3. Conjuntos `export ATBCMDER_CONFIG_PATH="$(pwd)/tests/.test_config"`. 
4. Gera ATBCmder em Python. Qualquer configuração modificada ou excluída durante a sessão afeta apenas o diretório de teste temporário, deixando seus arquivos pessoais `~/Library/Preferências/atbcmder/` 100% intactos. 

---

## 9. ⚡ Dicas profissionais e aprofundamento: personalização avançada

### Dica profissional 1: provisionamento automatizado de Dotfile via Chezmoi/Ansible

Como o ATBCmder serializa todos os estados em arquivos XML UTF-8 padrão, você pode verificar sua configuração em um repositório Git dotfiles e gerenciá-la por meio de ferramentas como Chezmoi, GNU Stow ou Ansible: 

```bash
# Example: Adding ATBCmder configuration to Chezmoi dotfiles manager
chezmoi add ~/Library/Preferences/atbcmder/atbcmder.xml
chezmoi add ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml
```

### Dica profissional 2: ajuste do observador de rede de alto desempenho

Ao trabalhar em servidores de arquivos corporativos SMB/NFS contendo milhões de arquivos, o monitoramento ativo de eventos recursivos pode causar congestionamento na rede. 

1. Abra **Preferências ➔ Atualização automática**. 
2. Desmarque **Quando o tamanho, a data ou os atributos mudam**. 
3. Defina **Intervalo de pesquisa** como `15` ou `30` segundos. 
4. Adicione a raiz de montagem de rede (`/Volumes/EnterpriseShare`) à **Lista de exclusão de caminho**. 
5. Use a atualização manual do painel (**`Ctrl+R`** / `⌘R`) quando a sincronização imediata for necessária.

### Dica profissional 3: variáveis ​​de ambiente de comando externo

Ao configurar botões de barra de ferramentas externos personalizados ou associações de arquivos, o ATBCmder herda automaticamente seu ambiente de shell de usuário (`PATH`, `HOME`, `USER`). Você pode invocar utilitários de linha de comando instalados via Homebrew (`/opt/homebrew/bin/`) diretamente, sem fornecer caminhos executáveis ​​absolutos completos.

### Dica profissional 4: configuração de dicas de ferramentas de arquivo flutuante

ATBCmder inclui dicas de ferramentas de metadados flutuantes que exibem dimensões de arquivo, dados EXIF, taxa de bits de áudio e contagens de membros de arquivo ao passar o mouse sobre os itens. Você pode ativar ou desativar as dicas de ferramentas em **Preferências ➔ Visualizações de arquivos**. 

![Helpful Tooltips](images/helpful_tooltips.png) 
*Figura 7.5: Dicas de metadados avançados exibindo propriedades detalhadas do arquivo ao passar o mouse.* 

---

## 10. Alertas de segurança e sistema

> [!CAUTION] 
> **Verificação de substituição de atalho** 
> Substituir um atalho primário no contexto `Main` ou `FilePanel` o desvincula do comando original imediatamente. Se você acidentalmente desvincular comandos essenciais como `F5` (Copiar) ou `Enter` (Abrir), use o botão **Redefinir para padrões** no Editor de teclas de atalho para restaurar os atalhos de teclado de fábrica. 

> [!WARNING] 
> **A importação de configuração substitui todas as configurações** 
> Restaurar um pacote de configuração por meio de `cm_ImportConfiguration` substitui completamente seus arquivos `atbcmder.xml`, `favtabs.xml` e `hotlist.xml` atuais. Sempre exporte um backup da sua configuração existente antes de importar um arquivo externo. 

> [!IMPORTANT] 
> **Sandbox do aplicativo macOS e acesso total ao disco** 
> Se o ATBCmder estiver em execução no macOS App Sandbox, ele não poderá ler arquivos de configuração ou diretórios fora de seu contêiner sem permissão explícita do usuário. Se você encontrar erros de permissão ao acessar unidades externas, execute **`cm_GrantFilesystemAccess`** para concluir o fluxo de integração do macOS Full Disk Access. 

---

## 11. Referência mestre de personalização e preferências de matriz dupla

| Categoria | Descrição da ação | Atalho do macOS | Chave do Comandante Clássico | ID do comando | 
| :--- | :--- | :--- | :--- | :--- | 
| **Preferências** | Abra a caixa de diálogo de preferências principais | `Cmd+,` / `⌘,` | `Alt+O` / `⌥O` | `cm_Options` | 
| **Preferências** | Salvar configurações em XML agora | Menu: Configuração | — | `cm_ConfigSaveSettings` | 
| **Preferências** | Salvar posição e tamanho da janela | Menu: Configuração | — | `cm_ConfigSavePos` | 
| **Preferências** | Alternar dicas de ferramentas de arquivo | Preferências ➔ Visualizações de arquivos | — | *(Preferências)* | 
| **Preferências** | Conceda permissões completas de disco | Menu: Configuração | — | `cm_GrantFilesystemAccess` | 
| **Teclas de atalho** | Abra a página do editor de teclas de atalho | `Cmd+,` ➔ Teclas de atalho | — | `cm_Options` | 
| **Teclas de atalho** | Tecla de atalho global para mostrar/ocultar janela | `Ctrl+Alt+H` / `⌘⌥H` | `Ctrl+Alt+H` | *(Tecla de atalho do sistema global)* | 
| **Associações** | Abra o Gerenciador de Associações de Arquivos | Menu: Configuração | — | `cm_FileAssoc` | 
| **Marcadores** | Gerenciador de lista de favoritos do diretório | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | 
| **Marcadores** | Adicionar diretório atual à lista de favoritos | Menu: Favoritos | — | `cm_AddDirToHotlist` | 
| **Guias de pastas** | Gerenciador de guias de pastas favoritas | Menu: Configuração | — | `cm_ConfigFavoriteTabs` | 
| **Guias de pastas** | Salvar guias atuais como conjunto favorito | Menu: Guias | — | `cm_SaveFavoriteTabs` | 
| **Arquivadores** | Configurar binários do arquivador | Menu: Configuração | — | `cm_ConfigArchivers` | 
| **Portabilidade** | Exportar configuração para ZIP | Menu: Configuração | — | `cm_ExportConfiguration` | 
| **Portabilidade** | Importar configuração do ZIP | Menu: Configuração | — | `cm_ImportConfiguration` | 
| **Portabilidade** | Abra a pasta de configuração | Menu: Configuração | — | `cm_OpenConfigDirectory` | 
| **Modos de visualização** | Alternar visualização de grade de miniaturas | `Ctrl+Shift+F1` / `⌃⇧F1` | `Ctrl+Shift+F1` | `cm_ThumbnailsView` | 
| **Modos de visualização** | Atualizar listagem de painel ativo | `Ctrl+R` / `⌃R` | `Ctrl+R` | `cm_Refresh` |

--- 

<div align="center"> 
<p>Pronto para dominar todos os atalhos de teclado e matrizes de comando em todo o aplicativo?</p> 
<p><strong><a href="keyboard_shortcuts.md">Prossiga para o Capítulo 8: Atalhos de teclado mestre &rarr;</a></strong></p> 
</div>