# Capítulo 8: Referência mestre de atalhos de teclado

ATBCmder foi projetado desde o início como um gerenciador de arquivos que prioriza o teclado. Cada operação de arquivo, salto de diretório, transformação de visualização e utilitário em lote pode ser executado sem interação do mouse. 

Para unir as tradições ortodoxas do Commander com a ergonomia nativa da Apple, o ATBCmder emprega uma **Arquitetura de teclado de matriz dupla**: cada comando pode ser invocado usando as teclas de função clássicas do Commander (`F1`–`F12`, `Insert`, teclado numérico) ou acordes modificadores nativos do macOS (`⌘` Comando, `⌥` Opção, `⇧` Shift, `⌃` Controle). 

---

## 1. A Filosofia de Matriz Dupla e Notação Chave

Quer você tenha vinte anos de memória muscular do Total Commander e do Norton Commander ou viva inteiramente com os atalhos nativos do macOS Finder, o ATBCmder acomoda seus reflexos imediatamente, sem exigir remapeamento manual. 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      DUAL-MATRIX KEYBOARD ENGINE                            │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  CLASSIC COMMANDER PARADIGM          │  NATIVE macOS PARADIGM               │
│  • Function Key Centric (F1–F12)     │  • Modifier Chords (⌘, ⌥, ⇧, ⌃)      │
│  • Dedicated Keypad Marking (+, -, *)│  • Finder Parity (⌘C, ⌘V, ⌘⌫, ⏎)     │
│  • Zero-Modal Terminal Velocity      │  • Native Menu Bar Integration       │
│  Examples:                           │  Examples:                           │
│    F5        ➔ Copy Files            │    ⌘C ➔ ⌘V   ➔ Copy Files            │
│    F6        ➔ Move Files            │    ⌘C ➔ ⌥⌘V  ➔ Move Files            │
│    Shift+F4  ➔ Create Text File      │    ⇧⌘4       ➔ Create Text File      │
│    Alt+F7    ➔ Find Files            │    ⌥⌘F       ➔ Find Files            │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Símbolos modificadores de teclado Apple

Ao longo deste guia e nas caixas de diálogo de preferências do ATBCmder, as combinações de teclas são representadas usando glifos tipográficos padrão do macOS: 

| Glifo | Nome do modificador | Equivalente a Windows/PC | Descrição | 
| :---: | :--- | :--- | :--- | 
| **`⌘`** | **Comando** (`Cmd`) | `Win` / `Ctrl` | Chave modificadora de ação primária do macOS. | 
| **`⌥`** | **Opção** (`Alt`) | `Alt` | Modificador secundário para ações alternativas e caracteres especiais. | 
| **`⇧`** | **Mudança** | `Shift` | Estende seleções, inverte ações ou ativa modos principais. | 
| **`⌃`** | **Controle** (`Ctrl`) | `Ctrl` | Controle de terminal e modificador de acordes de comandante clássico. | 
| **`⎋`** | **Escapa** (`Esc`) | `Esc` | Cancela operações, limpa filtros ou fecha caixas de diálogo. | 
| **`⏎`** | **Retorno** (`Enter`) | `Enter` | Executa ações, abre itens ou confirma prompts de diálogo. | 
| **`⌫`** | **Excluir / Retroceder** | `Backspace` | Exclusão de caracteres para trás ou navegação no diretório pai. | 
| **`⌦`** | **Encaminhar exclusão** | `Del` | Encaminhar exclusão de caractere ou exclusão do arquivo selecionado. | 
| **`⇥`** | **Guia** | `Tab` | Alterna o foco entre os painéis de origem e de destino. | 
| **`⇞`** | **Página para cima** | `PgUp` | Rola o painel listado por uma janela de visualização. | 
| **`⇟`** | **Página abaixo** | `PgDn` | Rola a lista do painel para baixo em uma janela de visualização. | 

---

## 2. Função macOS (`Fn`) Orientação principal

> [!IMPORTANTE] 
> ### Como usar teclas de função em teclados Mac 
> 
> Por padrão, os teclados Apple (incluindo teclados MacBook integrados, Magic Keyboards e Touch Bar Macs) atribuem a linha física superior (`F1` a `F12`) aos controles de hardware, como brilho da tela, Mission Control, Spotlight, Dictation, reprodução de mídia e volume do alto-falante. 
> 
> Como os fluxos de trabalho clássicos do Commander dependem muito de `F1`–`F12`, você tem duas opções: 
> 
> #### Método A: Segure o acorde chave `Fn` (padrão pronto para uso) 
> Segure a tecla física **`Fn`** (ou tecla Globe 🌐) localizada no canto inferior esquerdo do teclado do Mac enquanto pressiona qualquer tecla de função: 
> 
> * **`Fn + F3`**: Ver arquivo no Lister 
> * **`Fn + F4`**: Editar arquivo 
> * **`Fn + F5`**: Copiar arquivos para o painel de destino 
> * **`Fn + F6`**: Mover arquivos para o painel de destino 
> * **`Fn + F7`**: Criar novo diretório 
> * **`Fn + F8`**: Excluir arquivos 
> * **`Fn + Shift + F4`**: Criar e editar novo arquivo de texto 
> * **`Fn + Alt + F7`**: Abrir pesquisa de arquivo 
> 
> #### Método B: Habilite "Teclas de função padrão" nas configurações do macOS (recomendado) 
> Se você usa ATBCmder regularmente, alterne sua linha de função para que pressionar `F1`–`F12` acione comandos de função diretamente, enquanto segurar `Fn` acione ajustes de brilho e volume: 
> 
> 1. **macOS 13 Ventura, macOS 14 Sonoma, macOS 15 Sequoia**: 
> - Abra ** Menu Apple ➔ Configurações do Sistema...** 
> - Na barra lateral esquerda, selecione **Teclado**. 
> - Clique no botão **Atalhos de teclado...**. 
> - Na barra lateral da caixa de diálogo, selecione **Teclas de função**. 
> - Alterne **"Usar as teclas F1, F2, etc. como teclas de função padrão"** para **ON**. 
> - Clique em **Concluído**. 
> 
> 2. **macOS 12 Monterey e macOS 11 Big Sur**: 
> - Abra ** Menu Apple ➔ Preferências do Sistema... ➔ Teclado**. 
> - Na guia **Teclado**, marque a caixa **"Usar as teclas F1, F2, etc. como teclas de função padrão"**. 
> 
> #### Modelos MacBook Pro com Touch Bar 
> 
> * Mantenha pressionada a tecla física **`Fn`** no canto inferior esquerdo para exibir instantaneamente a linha virtual `F1`–`F12` na Touch Bar. 
> * Alternativamente, configure **Configurações do sistema ➔ Teclado ➔ Configurações da Touch Bar...** e defina **"Touch Bar shows"** para **"F1, F2, etc. Keys"** quando ATBCmder for o aplicativo mais ativo. 
> 
> #### Teclados compactos sem linha de funções dedicadas 
> 
> * Se você estiver usando um teclado mecânico de 60% ou 65% sem teclas `F` dedicadas, não será necessário torcer os dedos. Use os acordes modificadores nativos do macOS do ATBCmder (`⌘C`, `⌥⌘V`, `⇧⌘N`, `⌘⌫`, `⌥⏎`) que fornecem 100% de paridade operacional.

---

## 3. Arquitetura de atalho com escopo contextual

Para evitar colisões de teclas de atalho entre diferentes áreas de aplicação (por exemplo, pesquisar dentro da lista de arquivos principal versus pesquisar dentro de um visualizador de arquivos de texto), o ATBCmder segmenta todos os atalhos em contextos hierárquicos distintos: 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          APPLICATION SCOPE: Main                            │
│  Global commands, panel navigation, window management, toolbar, power tools │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  PANEL SCOPE: FilePanel       │  MODAL TOOLS SCOPES                         │
│  Active during directory      │  • Viewer      (Lister preview window)      │
│  table and thumbnail browsing │  • Editor      (Built-in code editor)       │
│  (marking, range selection,   │  • Differ      (Side-by-side diff viewer)   │
│  inline editing, space count) │  • FindFiles   (Multi-threaded file search) │
│                               │  • MultiRename (Batch rename engine)        │
└───────────────────────────────┴─────────────────────────────────────────────┘
```
 

Quando você pressiona um acorde de tecla, o mecanismo **`HotkeyManager`**: 

1. Avalia o contexto ativo focado (por exemplo, `Viewer` ou `FilePanel`). 
2. Se uma ligação exata corresponder, o comando `cm_*` associado será executado imediatamente. 
3. Se não existir nenhuma ligação no contexto local, o pressionamento de tecla volta normalmente para o contexto `Main`. 
4. Se ainda não estiver vinculado, a edição de texto padrão ou o manuseio de teclas do sistema assumem o controle. 

---

## 4. Tabelas de matriz dupla categorizadas mestres

As tabelas de referência a seguir documentam todos os comandos suportados pelo ATBCmder, categorizados por fluxo de trabalho funcional.

### 4.1 Operações de Arquivo

As operações de arquivo constituem a espinha dorsal do trabalho diário. Cada operação usa como padrão o paradigma **Origem ➔ Destino**: os itens selecionados no painel ativo são processados ​​no diretório aberto no painel oposto inativo.

| ID do comando | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_View` | Ver arquivo usando Universal Lister (visualização somente leitura) | `⌘3` / `Space` *(Visualização rápida)* | `F3` / `Shift+F3` | Principal | 
| `cm_Edit` | Abra o arquivo no editor de texto integrado | `⌘4` | `F4` | Principal | 
| `cm_EditNew` | Crie e edite imediatamente um novo arquivo de texto | `⇧⌘4` / `⇧F4` | `Shift+F4` | Principal | 
| `cm_Copy` | Copiar arquivos selecionados do painel ativo para o painel de destino | `⌘C` *(para a área de transferência)* / `F5` | `F5` | Principal | 
| `cm_CopySamePanel` | Duplicar/clonar arquivo selecionado no mesmo diretório | `⇧F5` | `Shift+F5` | Principal | 
| `cm_Move` | Mover arquivos selecionados do painel ativo para o painel de destino | `⌥⌘V` *(colar mover)* / `F6` | `F6` | Principal | 
| `cm_RenameOnly` | Renomeação rápida em linha do arquivo sob o cursor | `⏎` *(Retorno)* / `F2` | `F2` / `Shift+F6` | Principal | 
| `cm_Rename` | Renomeie o arquivo selecionado via caixa de diálogo | `⇧F6` | `Shift+F6` | Principal | 
| `cm_MkDir` | Crie um novo diretório/pasta | `⇧⌘N` / `F7` | `F7` | Principal | 
| `cm_Delete` | Excluir itens selecionados para a Lixeira do macOS | `⌘⌫` *(Cmd+Excluir)* / `⌦` | `F8` / `Delete` | Principal | 
| `cm_Wipe` | Exclua arquivos com segurança (ignore a Lixeira permanentemente) | `⌥⇧⌫` / `⌥⌦` | `Alt+Delete` / `Shift+Delete` | Painel de arquivos | 
| `cm_Open` | Abra o arquivo com o aplicativo padrão ou entre no diretório | `⌘↓` / `⏎` *(Retorno)* | `Enter` | Principal | 
| `cm_SetFileProperties` | Inspecione e edite metadados de arquivos, datas e permissões UNIX | `⌥⏎` *(Opção+Retorno)* / `⌘I` | `Alt+Enter` | Principal | 
| `cm_CountDirContent` | Calcular o tamanho em bytes do diretório sob o cursor | `⌥⇧⏎` *(Opção+Shift+Return)* | `Alt+Shift+Enter` | Painel de arquivos | 
| `cm_CalculateSpace` | Calcule o tamanho total de todos os diretórios selecionados | `⌃L` / `⌘L` | `Ctrl+L` | Principal | 
| `cm_SymLink` | Crie link simbólico no painel de destino | `⌥⌘S` | *(Menu: Arquivos ➔ Link simbólico)* | Principal | 
| `cm_HardLink` | Criar link físico do sistema de arquivos no painel de destino | `⌥⌘H` | *(Menu: Arquivos ➔ Hardlink)* | Principal | 
| `cm_PackFiles` | Compactar / compactar arquivos selecionados em arquivo (`.zip`, `.tar`, `.7z`) | `⌥F5` / `⌥⌘P` | `Alt+F5` | Principal | 
| `cm_ExtractFiles` | Extraia o conteúdo do arquivo diretamente no painel de destino | `⌥F9` / `⌥⌘E` | `Alt+F9` | Principal | 
| `cm_ArchiveView` | Digite archive como um diretório de sistema de arquivos virtual (`vfs://`) | `⌃⇟` *(Ctrl+PgDn)* / `⌘↓` | `Ctrl+PgDn` | Principal | 
| `cm_CompareContents` | Compare o conteúdo de dois arquivos selecionados | `⇧F3` | `Shift+F3` | Principal |

---

### 4.2 Seleção e Marcação

Os gerenciadores de arquivos ortodoxos são excelentes na seleção rápida de vários arquivos. ATBCmder permite selecionar itens individuais, padrões curinga, grupos de extensão ou blocos contínuos sem usar o mouse.

| ID do comando | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_MarkMarkAll` | Selecione todos os arquivos e pastas no painel ativo | `⌘A` | `Ctrl+A` / `Ctrl+Num+` | Principal | 
| `cm_MarkUnmarkAll` | Desmarque todos os arquivos e pastas no painel ativo | `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+Num-` | Principal | 
| `cm_MarkInvert` | Inverter o estado de seleção atual no painel ativo | `⌘I` / `⌃I` | `Num*` *(Teclado `*`)* | Painel de arquivos | 
| `cm_MarkPlus` | Selecione o padrão curinga correspondente ao grupo (por exemplo, `*.ts`) | `⌘+` / `⌃+` | `Num+` *(Teclado `+`)* | Painel de arquivos | 
| `cm_MarkMinus` | Desmarque o padrão curinga de correspondência de grupo (por exemplo, `*.log`) | `⌘-` / `⌃-` | `Num-` *(Teclado `-`)* | Painel de arquivos | 
| `cm_MarkCurrentExtension` | Selecione todos os arquivos que compartilham a extensão do arquivo do cursor | `⇧⌘E` / `⌥F8` | `Shift+Num+` / `Alt+Num+` | Principal | 
| `cm_UnmarkCurrentExt` | Desmarque todos os arquivos que compartilham a extensão do arquivo do cursor | `⌥⇧Num-` | `Shift+Num-` / `Alt+Num-` | Principal | 
| `cm_MarkCurrentName` | Selecione todos os arquivos que compartilham o nome de arquivo base do cursor | `⌥⌘N` | *(Menu: Marcar ➔ Mesmo Nome)* | Principal | 
| `cm_SelectOrDeselectFile` | Alternar seleção de item e avançar o cursor para baixo | `Space` | `Insert` / `Space` | Painel de arquivos | 
| `Shift+Up / Shift+Down` | Expandir ou contrair faixa de seleção contínua | `⇧↑` / `⇧↓` | `Shift+↑` / `Shift+↓` | Painel de arquivos | 
| `Shift+PageUp / Shift+PageDown` | Expandir a seleção contínua pela página completa da janela de visualização | `⇧⇞` / `⇧⇟` | `Shift+PgUp` / `Shift+PgDn` | Painel de arquivos | 
| `cm_ClearAll` | Limpar todas as marcas de seleção e destaques de pesquisa | `⌃L` | `Ctrl+L` | Principal | 
| `cm_CopyToClipboard` | Copie os arquivos selecionados para a área de transferência do sistema macOS | `⌘C` | `Ctrl+C` | Principal | 
| `cm_CutToClipboard` | Cortar arquivos selecionados para a área de transferência do sistema macOS | `⌘X` | `Ctrl+X` | Principal | 
| `cm_PasteFromClipboard` | Cole os arquivos da área de transferência no diretório ativo | `⌘V` | `Ctrl+V` | Principal | 
| `cm_PasteAsMove` | Colar arquivos da área de transferência como uma operação Mover | `⌥⌘V` | `Ctrl+Alt+V` | Principal | 
| `cm_CopyNamesToClip` | Copiar nome(s) de arquivo apenas para a área de transferência | `⇧⌘X` | `Ctrl+Shift+X` | Principal | 
| `cm_CopyFullNamesToClip` | Copiar caminho(s) absoluto(s) completo(s) para a área de transferência | `⇧⌘C` | `Ctrl+Shift+C` | Principal | 
| `cm_CompareDirectories` | Marcar arquivos que existem em um painel, mas não no outro | `⌥⇧C` | *(Menu: Marcar ➔ Comparar Dirs)* | Principal |

---

### 4.3 Navegação e marcadores no painel

Mova-se facilmente entre pastas, volumes locais, montagens de rede e histórico de navegação.

| ID do comando | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_FocusSwap` / `cm_SwitchPanel` | Foco alternativo do teclado entre os painéis esquerdo e direito | `⇥` *(Aba)* | `Tab` | Principal | 
| `cm_Refresh` | Atualizar/reler o conteúdo do Active Directory | `⌘R` / `⌃R` | `Ctrl+R` | Principal | 
| `cm_ChangeDirToParent` | Navegue até o diretório pai (`..`) | `⌘↑` / `⌫` *(Backspace)* | `Backspace` / `Ctrl+PgUp` | Principal | 
| `cm_ChangeDirToRoot` | Vá diretamente para a raiz do sistema de arquivos (`/`) | `⌘\` | `Ctrl+\` | Principal | 
| `cm_ChangeDirToHome` | Ir diretamente para a pasta pessoal do usuário (`~`) | `⇧⌘H` | `Ctrl+Shift+Home` / `Alt+Home` | Painel de arquivos | 
| `cm_ViewHistoryPrev` | Navegue de volta no histórico de navegação do diretório | `⌘[` / `⌥←` | `Alt+Left` / `Ctrl+[` | Principal | 
| `cm_ViewHistoryNext` | Navegue para frente no histórico de navegação do diretório | `⌘]` / `⌥→` | `Alt+Right` / `Ctrl+]` | Principal | 
| `cm_DirHistory` | Abra o menu suspenso do histórico do diretório interativo | `⌥↓` / `⌃↓` | `Alt+Down` / `Alt+F8` | Principal | 
| `cm_Drives` | Abra a unidade e pop-up do seletor de volume montado | `⌥D` | `Alt+D` | Principal | 
| `cm_LeftOpenDrives` | Abra o menu de seleção de unidade para painel esquerdo | `⌥F1` | `Alt+F1` | Principal | 
| `cm_RightOpenDrives` | Abra o menu de seleção de unidade para painel direito | `⌥F2` | `Alt+F2` | Principal | 
| `cm_Exchange` | Trocar painéis esquerdo e direito (diretórios, abas, estados) | `⌘U` | `Ctrl+U` | Principal | 
| `cm_TargetEqualSource` | Defina o diretório do painel inativo para corresponder ao diretório ativo | `⌥Z` / `⌃←` / `⌃→` | `Alt+Z` / `Ctrl+Left` / `Ctrl+Right` | Principal | 
| `cm_SyncSlaveDir` | Bloquear a navegação do painel de destino para espelhar o painel de origem | `⌥S` | *(Menu: Comandos ➔ Navegação Sincronizada)* | Principal | 
| `cm_DirHotList` | Abra o menu Hotlist / Favoritos do diretório | `⌘D` | `Ctrl+D` | Principal | 
| `cm_ConfigDirHotList` | Abra a caixa de diálogo de configuração da Hotlist do Diretório | `⇧⌘D` | `Ctrl+Shift+D` | Principal | 
| `cm_GoToFirst` | Pule o cursor para o primeiro item no painel ativo | `⌘↑` / `Fn+←` *(Página inicial)* | `Home` | Principal | 
| `cm_GoToLast` | Salta o cursor para o último item do painel ativo | `⌘↓` / `Fn+→` *(Fim)* | `End` | Principal | 
| `PageUp / PageDown` | Role o painel ativo para cima ou para baixo em uma janela de visualização completa | `⇞` *(Fn+↑)* / `⇟` *(Fn+↓)* | `PageUp` / `PageDown` | Painel de arquivos |

---

### 4.4 Modos de visualização e classificação

Alterne perfeitamente entre listas compactas, colunas de metadados detalhados, grades visuais de miniaturas, nivelamento recursivo de diretórios e visualizações de árvore sincronizadas.

| ID do comando | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_BriefView` | Mudar para visualização resumida (nomes compactos de várias colunas) | `⌃F1` | `Ctrl+F1` | Principal | 
| `cm_ColumnsView` | Mudar para visualização de colunas/detalhes (nome, tamanho, data, permissões) | `⌃F2` | `Ctrl+F2` | Principal | 
| `cm_ThumbnailsView` | Mudar para visualização em grade de miniaturas (imagens, mídia, PDFs) | `⌃⇧F1` | `Ctrl+Shift+F1` | Principal | 
| `cm_FlatView` | Alternar visualização plana/ramificação (listagem de diretório recursiva) | `⌘B` | `Ctrl+B` | Principal | 
| `cm_FlatViewSel` | Visualização plana/ramificação apenas dos diretórios selecionados | `⇧⌘B` | `Ctrl+Shift+B` | Principal | 
| `cm_TreeView` | Visualização em árvore (substitua o painel ativo pela árvore de diretórios) | `⌃⇧F8` | `Ctrl+Shift+F8` | Principal | 
| `cm_TreeViewSplit` | Visualização em árvore (Painel dividido: árvore superior/esquerda, arquivos inferior/direita) | `cm_TreeViewSplit` | *(Menu: Mostrar ➔ Divisão da visualização em árvore)* | Principal | 
| `cm_TreeViewBoth` | Visualização em árvore (ambos os painéis mostram árvores de diretórios) | `cm_TreeViewBoth` | *(Menu: Mostrar ➔ Visualização em árvore ambos)* | Principal | 
| `cm_QuickView` | Alternar painel Quick View (visualização ao vivo no painel oposto) | `⌘Q` / `⌃Q` | `Ctrl+Q` | Principal | 
| `cm_SortByName` | Classificar itens por nome (alternar crescente / decrescente) | `⌃F3` | `Ctrl+F3` | Principal | 
| `cm_SortByExt` | Classificar itens por extensão | `⌃F4` | `Ctrl+F4` | Principal | 
| `cm_SortByDate` | Classificar itens por data/hora de modificação | `⌃F5` | `Ctrl+F5` | Principal | 
| `cm_SortBySize` | Classificar itens por tamanho de arquivo | `⌃F6` | `Ctrl+F6` | Principal | 
| `cm_SortByAttr` | Classificar itens por atributos/permissões UNIX | `cm_SortByAttr` | *(Menu: Classificar ➔ Atributos)* | Principal | 
| `cm_ShowHiddenFiles` | Alternar a visibilidade de arquivos ocultos (`.` dotfiles) | `⌘H` / `⇧⌘.` | `Ctrl+H` | Principal | 
| `cm_ShowSysFiles` | Alternar visibilidade do sistema macOS e arquivos protegidos | `⇧⌘.` | `Ctrl+.` | Principal | 
| `cm_QuickSearch` | Abra a barra de pesquisa rápida no painel (digite letras para filtrar) | `⌥S` / `⌃S` *(ou digitando)* | `Ctrl+S` / *(digitação de letras)* | Principal | 
| `cm_SemanticFilter` | Abra a barra de filtro inteligente semântico de linguagem natural | `⌘F` | `Ctrl+F` | Principal | 
| `cm_HorizontalFilePanels` | Alternar layout horizontal de painel duplo (empilhado verticalmente) | `⇧⌘H` | `Ctrl+Shift+H` | Principal |

---

### 4.5 Guias e gerenciamento de janelas

ATBCmder permite abrir guias ilimitadas em qualquer painel, bloquear locais de trabalho favoritos e gerenciar sessões multi-guias em painel duplo.

| ID do comando | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_NewTab` | Abra uma nova guia de pasta no painel ativo | `⌘T` | `Ctrl+T` | Principal | 
| `cm_CloseTab` | Fechar guia da pasta atualmente ativa | `⌘W` | `Ctrl+W` | Principal | 
| `cm_NextTab` / `cm_NextTabCtrl` | Mude para a próxima guia à direita | `⌃⇥` *(Ctrl+Tab)* / `⌘⇧]` | `Ctrl+Tab` | Principal | 
| `cm_PrevTab` / `cm_PrevTabCtrl` | Mudar para a guia anterior à esquerda | `⌃⇧⇥` *(Ctrl+Shift+Tab)* / `⌘⇧[` | `Ctrl+Shift+Tab` | Principal | 
| `cm_ShowTabsList` | Mostrar menu pop-up de todas as abas abertas no painel ativo | `⇧⌘L` | `Ctrl+Shift+L` | Principal | 
| `cm_CloseAllTabs` | Feche todas as abas do painel ativo, exceto a última | `⌥⌘W` | *(Menu de contexto da guia: Fechar tudo)* | Principal | 
| `cm_CloseOtherTabs` | Feche todas as guias exceto a guia atualmente ativa | `⇧⌘W` | *(Menu de contexto da guia: Fechar outros)* | Principal | 
| `cm_Duplicatetab` | Duplicar guia da pasta ativa | `⌘D` / `cm_Duplicatetab` | *(Menu de contexto da guia: Duplicar)* | Principal | 
| `cm_MoveTabLeft` | Mover a guia ativa uma posição para a esquerda | `⌃⇧←` | *(Menu de contexto da guia: Mover para a esquerda)* | Principal | 
| `cm_MoveTabRight` | Mover a guia ativa uma posição para a direita | `⌃⇧→` | *(Menu de contexto da guia: Mover para a direita)* | Principal | 
| `cm_CopyTabToOtherPanel` | Clone a guia ativa diretamente no painel oposto | `⌥⌘T` | *(Menu de contexto da guia: Copiar para outro)* | Principal | 
| `cm_SaveTab` / `cm_SaveTabs` | Salvar o layout da guia atual na configuração | `cm_SaveTab` | *(Menu: Guias ➔ Salvar guias)* | Principal | 
| `cm_LoadTab` / `cm_LoadTabs` | Restaurar layout de guia salvo da configuração | `cm_LoadTab` | *(Menu: Abas ➔ Carregar Abas)* | Principal | 
| `cm_OptionsFavorites` | Configurar conjuntos de guias favoritas e áreas de trabalho persistentes | `cm_OptionsFavorites` | *(Menu: Abas ➔ Abas Favoritas)* | Principal | 
| `cm_FullScreen` | Alternar janela do aplicativo em tela cheia | `⌃⌘F` / `F11` | `F11` | Principal |

---

### 4.6 Ferramentas elétricas e utilitários

Inicie ferramentas avançadas de automação, utilitários em lote e ferramentas de sistema incorporadas diretamente dos acordes do teclado.

| ID do comando | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_FileSearch` / `cm_Search` | Abrir caixa de diálogo de pesquisa avançada de vários filtros | `⌥F7` / `⌥⌘F` | `Alt+F7` | Principal | 
| `cm_FileDiff` / `cm_CompareFiles` | Abra o visualizador de diferenças de arquivos visuais lado a lado | `⌘⇧F12` | `Meta+Shift+F12` | Principal | 
| `cm_SyncDirs` | Abra a ferramenta de sincronização de diretório bidirecional | `⇧F12` | `Shift+F12` | Principal | 
| `cm_MultiRename` | Ferramenta de multi-renomeação em lote aberto (RegEx e tokens) | `⌘M` | `Ctrl+M` | Principal | 
| `cm_Split` | Divida um arquivo grande em segmentos uniformes | `⌥F6` | `Alt+F6` | Principal | 
| `cm_Combine` | Combine segmentos numerados divididos de volta ao arquivo original | `⌥F7` | `Alt+F7` | Principal | 
| `cm_CalculateChecksum` | Calcular hash criptográfico (MD5, SHA-1, SHA-256) | `⌃X` / `⌘K` | `Ctrl+X` | Principal | 
| `cm_VerifyChecksum` | Verifique os arquivos em relação ao arquivo de soma de verificação (`.md5`, `.sha256`) | `cm_VerifyChecksum` | *(Menu: Arquivos ➔ Verificar soma de verificação)* | Principal | 
| `cm_RunTerm` | Inicie o Terminal do sistema no diretório do painel ativo | `⌃J` / `F9` | `Ctrl+J` / `F9` | Principal | 
| `cm_FocusCmdLine` | Mude o foco do teclado diretamente para a linha de comando inferior | `⇧F2` | `Shift+F2` | Principal | 
| `cm_ShowCmdLineHistory` | Abrir lista suspensa de histórico de comandos shell anteriores | `⌥↓` / `⌃↓` | `Alt+F8` / `Ctrl+Down` | Principal | 
| `cm_AddPathToCmdLine` | Anexe o caminho do diretório ativo à linha de comando | `⌘P` | `Ctrl+P` | Principal | 
| `cm_ShowCommandLine` | Alternar linha de comando inferior/barra de entrada do console | `⌘O` | `Ctrl+O` | Principal | 
| `cm_DiskBenchmark` | Execute o benchmark de desempenho de leitura/gravação da unidade de armazenamento | `cm_DiskBenchmark` | *(Menu: Comandos ➔ Benchmark)* | Principal | 
| `cm_VisSemanticCommand` | Abrir pesquisa semântica e barra de comandos de linguagem natural | `/` / `⇧⌘P` | `/` | Principal |

---

### 4.7 Sistema, Configuração e Ajuda

Acesse preferências de aplicativos, gerenciamento de configuração, atualizações de software e documentação do usuário. 

| ID do comando | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_Options` | Abra a caixa de diálogo Preferências/Configurações do aplicativo | `⌘,` | `Ctrl+,` | Principal | 
| `cm_HelpContents` / `cm_HelpIndex` | Documentação e guia do usuário interativo aberto | `⌘?` / `F1` | `F1` | Principal | 
| `cm_HelpKeyboard` | Abra o cartão de referência de atalhos de teclado rápidos | `cm_HelpKeyboard` | *(Menu: Ajuda ➔ Teclado)* | Principal | 
| `cm_Exit` | Sair/Sair do ATBCmder | `⌘Q` | `F10` / `Alt+F4` / `Alt+X` | Principal | 
| `cm_About` | Exibir versão, licença e créditos do ATBCmder | `cm_About` | *(Menu: ATBCmder ➔ Sobre)* | Principal | 
| `cm_OpenConfigDirectory` | Revelar pasta de configuração (`atbcmder.xml`) no painel | `cm_OpenConfigDirectory` | *(Menu: Configuração ➔ Abrir Configuração)* | Principal | 
| `cm_ExportConfiguration` | Exporte todas as preferências para um pacote ZIP portátil | `cm_ExportConfiguration` | *(Menu: Configuração ➔ Exportar)* | Principal | 
| `cm_ImportConfiguration` | Importar preferências do pacote ZIP portátil | `cm_ImportConfiguration` | *(Menu: Configuração ➔ Importar)* | Principal | 
| `cm_CheckForUpdate` | Verifique se há atualizações de software de aplicativo | `cm_CheckForUpdate` | *(Menu: Ajuda ➔ Verificar atualizações)* | Principal | 

---

## 5. Atalhos de contexto de ferramenta modal

Ao abrir ferramentas especializadas, como Universal Lister, o editor de texto integrado, a diferença lado a lado ou caixas de diálogo em lote, o ATBCmder ativa mapas de teclado específicos do contexto. Esses atalhos operam diretamente em cada janela de ferramenta, em vez de por meio de comandos de registro `cm_*` globais em todo o aplicativo.

### 5.1 Lista Universal (`Viewer` Contexto)

Ativo ao visualizar documentos, texto, código, imagens, áudio, vídeo ou bytes hexadecimais brutos.

| Ação/Recurso | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| Selecionar tudo | Selecione todo o texto/conteúdo no visualizador | `⌘A` | `Ctrl+A` | Visualizador | 
| Modo de texto simples | Mudar para o modo Texto Simples | `1` | `1` | Visualizador | 
| Modo Binário | Mudar para o modo binário | `2` | `2` | Visualizador | 
| Modo hexadecimal bruto | Mudar para o modo de inspeção de bytes hexadecimais brutos | `3` | `3` | Visualizador | 
| Modo Decimal | Mudar para o modo decimal | `4` | `4` | Visualizador | 
| Visualização do livro | Mudar para o modo Livro Paginado | `5` | `5` | Visualizador | 
| Visualização de imagem | Mudar para o modo visualizador de imagens | `6` | `6` | Visualizador | 
| Plug-ins personalizados | Mudar para visualizador de plug-in personalizado | `7` | `7` | Visualizador | 
| PDF / Visualização do Office | Mudar para o modo leitor de documentos PDF / Office | `8` | `8` | Visualizador | 
| Modo de código | Mudar para o modo de código destacado pela sintaxe | `9` | `9` | Visualizador | 
| Centralizar imagem | Centralizar imagem na janela do visualizador | `C` | `C` | Visualizador | 
| Ajustar à janela | Ajustar imagem às dimensões da janela | `F` | `F` | Visualizador | 
| Ajuste apenas grande | Reduzir a escala apenas se a imagem exceder as dimensões da janela | `L` | `L` | Visualizador | 
| Alternar envoltório | Ativar/desativar quebra de linha | `W` | `W` | Visualizador | 
| Alternar cursor | Alternar cursor de texto visível | `F6` | `F6` | Visualizador | 
| Encontrar texto | Encontre texto no documento | `⌘F` / `F7` | `F7` | Visualizador | 
| Encontre o próximo | Ir para a próxima correspondência de pesquisa | `⌘G` / `F3` | `F3` | Visualizador | 
| Encontrar anterior | Ir para a correspondência de pesquisa anterior | `⇧⌘G` / `⇧F3` | `Shift+F3` | Visualizador | 
| Ampliar | Ampliar imagem ou PDF | `⌘+` / `Num+` | `Num+` | Visualizador | 
| Diminuir zoom | Diminuir imagem ou PDF | `⌘-` / `Num-` | `Num-` | Visualizador | 
| Tela cheia | Alternar modo de visualização em tela cheia | `⌃⌘F` / `⌥⏎` | `Alt+Enter` | Visualizador | 
| Fechar visualizador | Fechar janela do visualizador do Lister | `⎋` *(Esc)* / `Q` | `Escape` / `Q` | Visualizador |

---

### 5.2 Editor de texto integrado (`Editor` Contexto)

Ativo ao criar ou modificar arquivos de texto e código-fonte. 

| Ação/Recurso | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| Salvar arquivo | Salvar arquivo modificado no disco | `⌘S` / `F2` | `F2` | Editor | 
| Encontrar texto | Encontre texto no documento do editor | `⌘F` / `F7` | `F7` | Editor | 
| Encontre o próximo | Ir para a próxima correspondência de pesquisa | `⌘G` / `F3` | `F3` | Editor | 
| Encontrar anterior | Ir para a correspondência de pesquisa anterior | `⇧⌘G` / `⇧F3` | `Shift+F3` | Editor | 
| Corte | Cortar o texto selecionado para a área de transferência | `⌘X` | `Ctrl+X` | Editor | 
| Copiar | Copiar o texto selecionado para a área de transferência | `⌘C` | `Ctrl+C` | Editor | 
| Colar | Colar texto da área de transferência | `⌘V` | `Ctrl+V` | Editor | 
| Desfazer | Desfazer a última ação de digitação | `⌘Z` | `Ctrl+Z` | Editor | 
| Refazer | Refazer a última ação desfeita | `⇧⌘Z` | `Ctrl+Shift+Z` | Editor | 
| Selecionar tudo | Selecione todo o texto do documento | `⌘A` | `Ctrl+A` | Editor | 
| Fechar Editor | Fechar janela do editor de texto | `⎋` *(Esc)* / `⌘W` | `Esc` / `Alt+X` | Editor | 

---

### 5.3 Diferença visual lado a lado (`Differ` Contexto)

Ativo dentro da ferramenta de comparação visual de diferenças. 

| Ação/Recurso | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| Encontrar texto | Pesquisar texto nos painéis de diferença | `⌘F` / `F7` | `F7` | Diferente | 
| Encontre o próximo | Ir para a próxima ocorrência de pesquisa | `⌘G` / `F3` | `F3` | Diferente | 
| Encontrar anterior | Ir para a ocorrência de pesquisa anterior | `⇧⌘G` / `⇧F3` | `Shift+F3` | Diferente | 
| Próxima diferença | Pule o cursor para o próximo bloco de diferença | `⌥↓` *(Opção+Para Baixo)* | `Alt+Down` | Diferente | 
| Diferença Anterior | Saltar o cursor para o bloco de diferença anterior | `⌥↑` *(Opção+Para cima)* | `Alt+Up` | Diferente | 
| Primeira Diferença | Vá diretamente para a primeira diferença nos arquivos | `⌥Fn+←` *(Opt+Home)* | `Alt+Home` | Diferente | 
| Última diferença | Vá diretamente para a última diferença nos arquivos | `⌥Fn+→` *(Opt+End)* | `Alt+End` | Diferente | 
| Copiar da direita para a esquerda | Copiar bloco de diferença do painel direito para o painel esquerdo | `⌥←` *(Opção+Esquerda)* | `Alt+Left` | Diferente | 
| Copiar da esquerda para a direita | Copiar bloco de diferença do painel esquerdo para o painel direito | `⌥→` *(Opção+Direita)* | `Alt+Right` | Diferente | 
| Atualizar/nova varredura | Releia os arquivos do disco e execute novamente a comparação de diferenças | `⌘R` | `Ctrl+R` | Diferente | 
| Fechar Difere | Fechar janela de comparação de diferenças | `⎋` *(Esc)* / `⌘W` | `Alt+X` / `Esc` | Diferente | 

---

### 5.4 Caixa de diálogo de pesquisa avançada de arquivos (`FindFiles` Contexto)

Ativo dentro da caixa de diálogo de pesquisa multithread em segundo plano. 

| Ação/Recurso | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| Iniciar pesquisa | Iniciar a execução da pesquisa | `⏎` *(Retorno)* / `F9` | `F9` | Localizar arquivos | 
| Cancelar/Fechar | Cancelar a pesquisa em execução ou fechar a caixa de diálogo | `⎋` *(Esc)* | `Esc` | Localizar arquivos | 
| Ver Selecionado | Ver o resultado da pesquisa selecionado no Lister | `⌘3` / `F3` | `F3` | Localizar arquivos | 
| Editar selecionado | Abra o resultado da pesquisa selecionado no Editor | `⌘4` / `F4` | `F4` | Localizar arquivos | 
| Nova pesquisa | Redefinir consulta de pesquisa e preparar nova pesquisa | `⌘N` | `Ctrl+N` | Localizar arquivos | 
| Limpar filtros | Nova pesquisa com todos os filtros de data/tamanho/atributo limpos | `⇧⌘N` | `Ctrl+Shift+N` | Localizar arquivos | 
| Relembrar Anterior | Recuperar parâmetros da pesquisa anterior | `⌘L` | `Ctrl+L` | Localizar arquivos | 

---

### 5.5 Ferramenta de multi-renomeação em lote (`MultiRename` Contexto)

Ativo dentro do espaço de trabalho de renomeação em lote. 

| Ação/Recurso | Descrição | Atalho primário do macOS (com glifos ⌘/⌥/⇧/⌃) | Atalho clássico do Commander (com teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| Redefinir regras | Redefinir as regras de renomeação de máscara e padrão para o padrão | `⌘R` | `Ctrl+R` | MultiRenomear | 
| Editar nomes no Editor | Abra a lista de nomes de arquivos de destino no editor externo para edição manual | `⌘I` | `Ctrl+I` | MultiRenomear | 
| Carregar arquivo de nomes | Carregar nomes substitutos de um arquivo de texto externo | `F3` | `F3` | MultiRenomear | 

---

## 6. Dicas profissionais e otimização de teclas de atalho do sistema

### 6.1 Resolvendo colisões globais de atalhos do macOS

Certas teclas de atalho padrão do sistema macOS interceptam os pressionamentos de tecla antes que cheguem aos aplicativos de desktop. Para desbloquear a agilidade total do Commander, você pode personalizar ou desativar atalhos conflitantes do macOS: 

1. **Pesquisa Spotlight (`⌘Space` vs Pesquisa Rápida)**: 
- Por padrão, `⌘Space` ativa o Spotlight. Se você preferir usar `⌘Space` para marcação de arquivos ou pesquisa no painel, remapeie o Spotlight para `⌥Space` em **Configurações do sistema ➔ Teclado ➔ Atalhos de teclado... ➔ Spotlight**. 
2. **Controle de Missão (`⌃↑`) e Exposição de Aplicativo (`⌃↓`)**: 
- macOS usa `⌃↑` e `⌃↓` para Controle de Missão. No ATBCmder, `⌃↓` abre o menu suspenso Histórico do diretório. Você pode reatribuir o Controle da Missão em **Configurações do Sistema ➔ Teclado ➔ Atalhos de Teclado... ➔ Controle da Missão**. 
3. **Ocultação de aplicativo (`⌘H`)**: 
- No macOS, `⌘H` oculta o aplicativo frontal. ATBCmder usa `⌘H` ou `⇧⌘.` para alternar arquivos de pontos ocultos. Se você deseja que `⌘H` alterne estritamente os arquivos ocultos, desative "Ocultar aplicativo" no macOS ou use o `⇧⌘.` padrão do Finder (`Cmd+Shift+Period`). 
4. **Minimização de janela (`⌘M`)**: 
- o macOS atribui `⌘M` para minimizar a janela do Dock. ATBCmder atribui `⌘M` à ferramenta de multi-renomeação em lote (`cm_MultiRename`). ATBCmder captura `⌘M` em sua janela principal, mas você também pode acionar Multi-Rename via `Ctrl+M` ou na barra de ferramentas. 

---

### 6.2 Ergonomia do trackpad e do mouse

Para usuários de laptop sem teclado externo, o ATBCmder combina atalhos de teclado com gestos intuitivos do trackpad: 

* **Aperte para ampliar miniaturas**: na visualização de miniaturas (`cm_ThumbnailsView`), aperte para dentro ou para fora no trackpad do seu MacBook (ou segure `⌃` e role) para redimensionar as visualizações de miniaturas continuamente de `48 px` até `512 px`. 
* **Deslizar com dois dedos para trás/para frente**: deslize para a esquerda ou para a direita com dois dedos na tabela de arquivos para navegar para trás (`cm_ViewHistoryPrev`) e para frente (`cm_ViewHistoryNext`) no histórico da pasta. 
* **Divisor de clique duplo**: Clique duas vezes em qualquer lugar na barra divisória central vertical para redefinir os painéis para uma divisão horizontal exata de 50/50. 
* **Clique com o botão do meio nas guias**: Clique com o botão do meio (ou toque com três dedos) em qualquer guia da pasta para fechá-la imediatamente sem pressionar `⌘W`. 

---

### 6.3 Personalizando atalhos de teclado em preferências

Cada atalho documentado acima pode ser personalizado ou recuperado: 

1. Pressione **`⌘,`** (ou selecione **Configuração ➔ Opções...**) para abrir a caixa de diálogo Preferências. 
2. Selecione **Teclas de atalho** na barra lateral. 
3. Use o menu suspenso **Contexto** para escolher qual área você deseja configurar (`Main`, `FilePanel`, `Viewer`, etc.). 
4. Use a caixa de filtro de pesquisa para localizar qualquer comando por nome ou ID `cm_*`. 
5. Clique na caixa de atalho e pressione a combinação de teclas desejada. O detector de colisão integrado irá avisá-lo imediatamente se aquele acorde já estiver atribuído em outro lugar. 
6. Clique em **Aplicar** para ativar as alterações instantaneamente sem reiniciar o aplicativo. 

Os atalhos de teclado do usuário são salvos em `~/.config/atbcmder/atbcmder_hotkeys.xml` (ou `~/Library/Preferências/atbcmder/` no macOS). Você pode exportar e transferir este arquivo entre máquinas usando **`cm_ExportConfiguration`**. 

--- 

<div align="center"> 
<p>Procurando receitas práticas para o dia a dia, fluxos de trabalho de montagem de NAS ou dicas para solução de problemas?</p> 
<p><strong><a href="faq_howtos.md">Prossiga para o Capítulo 9: Receitas do mundo real e solução de problemas &rarr;</a></strong></p> 
</div>