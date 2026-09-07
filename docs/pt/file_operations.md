# Capítulo 3: Operações de arquivos e fila em segundo plano

Todos os dias, os gerenciadores de arquivos são julgados por uma métrica: a rapidez, a precisão e a segurança com que você pode manipular os dados. No ATBCmder, você nunca precisa lidar com várias janelas sobrepostas, sofrer erros de queda acidental ou esperar indolentemente enquanto grandes transferências de arquivos congelam sua tela. 

Este capítulo cobre o espectro completo de operações de arquivos: fluxos de trabalho de cópia e movimentação direcionais, renomeação in-line no local, marcação poderosa com curingas, interoperabilidade de arrastar e soltar do sistema, tratamento granular de colisões, permissões e links simbólicos UNIX e fila de operações em segundo plano multithread. 

---

## 1. Guia de início rápido visual: o modelo de operação direcional

Os gerenciadores de arquivos ortodoxos usam um modelo direcional **Origem ➔ Destino**. Quando você inicia uma transferência de arquivo ou criação de link, o ATBCmder pega os itens selecionados no **Painel Ativo** (Fonte) e executa a operação diretamente no diretório aberto no **Painel Inativo** (Destino). 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  ACTIVE PANEL (Source)                              INACTIVE PANEL (Target)            │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Size   Date    │   │  Name                        Size   │
│  ▸ [..]                              --:--   │   │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ C │  ▸ client_portal            <DIR>   │
│  ✔ schema_migration.sql      42 KB   14:12   │ O │  ▸ microservices            <DIR>   │
│  ● notes.txt                  4 KB   09:30   │ P │  ● .env.production          2.1 KB  │
│                                              │ Y │                                     │
│  [2 files selected: 1.8 GB]                  │ ➔ │  [Destination ready for ingest]     │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│                         ▼ Press F5 (Copy) or F6 (Move) ▼                               │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ Copy file(s)                                                                     │  │
│  │ Copy selected 2 files?                                                           │  │
│  │ To: [/Volumes/ExternalSSD/Projects                                          ] […]│  │
│  │ [Options ▼]        [Add To Queue #1 ▾]       [Cancel]               [Start (⏎)]  │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Folha de referências de operações principais de matriz dupla

| Ação | Atalho do macOS | Chave do Comandante Clássico | ID do comando | Descrição | 
| :--- | :--- | :--- | :--- | :--- | 
| **Copiar para destino** | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Copia os itens selecionados para o painel oposto. | 
| **Copiar no mesmo painel** | `Shift+F5` / `⇧F5` | `Shift+F5` | `cm_CopySamePanel` | Duplica itens no painel ativo com prompt de renomeação. | 
| **Mover para destino** | `F6` / `Fn+F6` | `F6` | `cm_Move` | Move os itens selecionados para o painel oposto. | 
| **Nova pasta (MkDir)** | `F7` / `Fn+F7` | `F7` | `cm_MkDir` | Cria um novo diretório no painel ativo. | 
| **Excluir para a Lixeira** | `F8` / `⌘⌫` | `F8` / `Delete` | `cm_Delete` | Move os itens selecionados para a Lixeira do macOS. | 
| **Exclusão permanente** | `Shift+Delete` / `⇧⌦` | `Shift+F8` | `cm_Delete` | Ignora a Lixeira e desvincula arquivos permanentemente. | 
| **Renomeação rápida embutida**| `F2` / `Shift+F6` | `Shift+F6` | `cm_RenameOnly` | Renomeia o item ativo diretamente dentro da linha da tabela. | 
| **Propriedades do arquivo** | `Alt+Enter` / `⌥⏎` | `Alt+Enter` | `cm_SetFileProperties` | Abre caixas de diálogo de permissões, carimbos de data/hora e metadados do UNIX. | 
| **Calcular espaço na pasta**| `Alt+Shift+Enter` / `⌥⇧⏎` | `Alt+Shift+Enter` | `cm_CountDirContent` | Calcula bytes recursivos para diretórios (`Ctrl+L` / `cm_CalculateSpace` para o total selecionado). | 
| **Fila em segundo plano** | `Toolbar ⚡` | — | `cm_OperationsPanel` | Abre o monitor de transferência em segundo plano de 3 filas. |

### Marco visual: a barra de ferramentas do meio

ATBCmder apresenta uma barra de ferramentas vertical dedicada de ação rápida incorporada diretamente na divisória central que separa os dois painéis: 

![Middle Toolbar](images/middle_toolbar.png) 
*A barra de ferramentas central central fornece acesso instantâneo do mouse para Exibir (F3), Editar (F4), Copiar (F5), Mover (F6), Nova Pasta (F7), Excluir (F8) e Troca de Painel.* 

---

## 2. Operações principais: copiar, mover, MkDir e excluir

O gerenciamento diário de arquivos gira em torno de quatro ações principais: copiar, mover, criar diretórios e excluir arquivos indesejados.

### 2.1 Copiando Arquivos (`F5` / `cm_Copy`)

Para copiar arquivos ou diretórios: 

1. **Selecione** um ou mais itens no painel ativo usando o teclado ou mouse. 
2. **Pressione `F5`** (ou `Fn+F5` em teclados Apple ou clique em **Copiar** na barra de ferramentas central). 
3. A **caixa de diálogo Copiar** aparece: 
- **Linha de Destino**: Preenchida automaticamente com o caminho do diretório atual do painel oposto. Você pode editar este caminho manualmente, anexar um novo nome de subpasta para copiar e criar simultaneamente ou clicar em `...` para navegar. 
- **Iniciar (`Enter`)**: Inicia a cópia imediata em primeiro plano com uma caixa de diálogo de progresso em tempo real. 
- **Adicionar à fila (`F2`)**: Coloca a transferência na fila para ser executada em segundo plano (consulte [Seção 7.4](#74-background-operations-queue-cm_operationspanel)). 
- **Opções**: Expande regras avançadas de conflito, preservação de atributos e verificações de soma de verificação. 

```
┌────────────────────────────────────────────────────────┐
│ Copy file(s)                                           │
│ Copy selected 3 files?                                 │
│ To: [/Volumes/Backup/Assets                          ] │
│ [Options ▼]   [Add To Queue #1 ▾]   [Cancel]   [Start] │
└────────────────────────────────────────────────────────┘
```

#### Duplicação no painel (`Shift+F5` / `cm_CopySamePanel`)

Para clonar rapidamente um arquivo no diretório atual (por exemplo, criando um backup antes de editar `nginx.conf`): 

- Destaque o item e pressione `Shift+F5` (ou `⇧F5`). 
- ATBCmder solicita um caminho de destino no *mesmo* diretório, permitindo que você insira um novo nome (por exemplo, `nginx.conf.bak`).

#### Área de transferência padrão do macOS (`Cmd+C` ➔ `Cmd+V`)

ATBCmder integra-se totalmente aos atalhos da área de transferência do sistema macOS: 

- **`Cmd+C` (`⌘C`)**: Copia os caminhos dos arquivos selecionados para a área de transferência (`cm_CopyToClipboard`). 
- **`Cmd+V` (`⌘V`)**: Cola arquivos da área de transferência no painel ativo (`cm_PasteFromClipboard`). 
- **`Cmd+Option+V` (`⌥⌘V`)**: Move os arquivos da área de transferência para o painel ativo (`cm_PasteAsMove`). 

---

### 2.2 Movendo arquivos (`F6` / `cm_Move`)

Mover arquivos de transferência do diretório de origem para o diretório de destino: 

1. Selecione os itens e pressione **`F6`** (ou `Fn+F6` / clique em **Mover** na barra de ferramentas central). 
2. A **caixa de diálogo Mover** é aberta, exibindo o caminho do painel de destino. 
3. Pressione **`Enter`** para executar: 
- **Movimento no mesmo sistema de arquivos**: Instantâneo e atômico em volumes APFS/HFS+, atualizando referências de catálogo do sistema de arquivos sem mover blocos de disco brutos. 
- **Movimento entre sistemas de arquivos**: transmite dados entre volumes até o destino, verifica a conclusão de bytes e remove com segurança a origem após a chegada verificada. 
4. Se um arquivo existente com o mesmo nome residir no destino, o ATBCmder pausa e invoca a **Diálogo Sobrescrever** (consulte a [Seção 6](#6-collision-handling-conflict-resolution)). 

---

### 2.3 Criando Novos Diretórios (`F7` / `cm_MkDir`)

Precisa criar uma estrutura de pastas dinamicamente? 

1. Pressione **`F7`** (ou `Fn+F7` / `Shift+Cmd+N` / `cm_MkDir`). 
2. Um prompt leve é ​​exibido: `Enter folder name:`. 
3. Digite o nome da pasta e pressione `Enter`. 

```
┌──────────────────────────────────────────────┐
│ Create Directory                             │
│ Enter folder name:                           │
│ [2026-09-Q3_Reports                        ] │
│                      [Cancel]      [OK (⏎)]  │
└──────────────────────────────────────────────┘
```

#### Encadeamento de subdiretórios

Você pode criar hierarquias de pastas aninhadas em uma única etapa. Digitar `deep/nested/project/assets` cria todos os quatro níveis de hierarquia instantaneamente (equivalente a `mkdir -p`).

#### Posicionamento de foco automático

Após a criação, o ATBCmder coloca automaticamente o cursor do painel diretamente na nova pasta, pronto para entrada imediata (`Enter`) ou transferência de arquivo. 

---

### 2.4 Excluindo arquivos: Lixeira do macOS vs. Limpeza permanente

Segurança e capacidade de recuperação são fundamentais. ATBCmder oferece suporte a fluxos de trabalho de exclusão dupla: 

```
                  ┌────────────────────────────────────────┐
                  │          File Deletion Trigger         │
                  └───────────────────┬────────────────────┘
                                      │
                 ┌────────────────────┴───────────────────┐
                 ▼                                        ▼
    [ F8 / Delete / Cmd+Backspace ]             [ Shift+Delete / Shift+F8 ]
                 │                                        │
                 ▼                                        ▼
    macOS System Trash (.Trash)                  Permanent Unlink
      • Fully recoverable                         • Bypasses Trash
      • Put Back support in Finder                • Zero disk footprint
      • Volume .Trashes directory                 • Unrecoverable without deep carve
```

#### Exclusão para a lixeira do macOS (`F8` / `Delete` / `Cmd+Backspace`)

- Os arquivos selecionados são roteados por meio de APIs macOS `send2trash` para a Lixeira do sistema. 
- Os arquivos podem ser inspecionados ou restaurados a qualquer momento através do macOS Finder ("Colocar de volta"). 
- As caixas de diálogo de confirmação podem ser ativadas ou suprimidas em **Preferências** (`operations.confirm_delete`).

#### Exclusão permanente imediata (`Shift+Delete` / `Shift+F8`)

- Ignora totalmente a Lixeira, desvinculando arquivos imediatamente e liberando espaço de armazenamento. 
- Ideal para limpar máquinas virtuais de vários gigabytes ou imagens de disco onde os limites do buffer de lixo ou o esgotamento do disco impediriam a preparação.

#### Volumes sem suporte para lixo (detecção `trash_unavailable`)

Ao excluir determinados compartilhamentos de rede (SMB, NFS), sistemas de arquivos virtuais (`vfs://`) ou unidades externas formatadas com sistemas de arquivos FAT/exFAT herdados sem um diretório `.Lixeiraes`, o macOS não pode enviar itens para a Lixeira. 

Nesses casos, o ATBCmder aciona um alerta de segurança inteligente: 
```
┌────────────────────────────────────────────────────────┐
│ Trash Unavailable                                      │
│ The volume containing '/Volumes/NAS/backup.iso' does   │
│ not support Trash.                                     │
│ Would you like to permanently delete this file?        │
│                                                        │
│ [✔] Apply to all remaining items                       │
│              [Skip]               [Delete Permanently] │
└────────────────────────────────────────────────────────┘
```
 
Você pode optar por **Excluir permanentemente**, **Pular** ou marcar **Aplicar a todos os itens restantes** para lidar com exclusões em grandes lotes de forma autônoma.

#### Destruição segura de múltiplas passagens (`Alt+Delete` / `cm_Wipe`)

Para documentos confidenciais, credenciais ou chaves privadas que não devem permanecer recuperáveis por meio de ferramentas de recuperação flash brutas: 

- Destaque o item e selecione **Menu Arquivo** → **Wipe** (`Alt+Delete` / `cm_Wipe`). 
- ATBCmder executa uma substituição multipassagem com padrões de bits aleatórios e zeros antes de desvincular o inode. 

---

## 3. Renomeação Rápida Inline e Edição de Nome

Renomear um único arquivo não deve exigir menus complexos ou janelas pop-up. ATBCmder fornece edição rápida e local de linhas da tabela. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Name                                  Ext      Size      Date Modified         │
│  ▸ [..]                                         --:--     drwxr-xr-x            │
│  ● Annual_Financial_Report_2025        .pdf     4.2 MB    Today, 11:20          │
│    ▲                                                                            │
│    └── [Editable Text Box: Stem highlighted, .pdf extension preserved]          │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Acionando Renomeação Inline

1. Destaque qualquer arquivo ou diretório no painel. 
2. Pressione **`F2`** ou **`Shift+F6`** (`cm_RenameOnly`) ou clique uma vez no nome do arquivo já destacado. 
3. A célula da tabela se transforma em um editor embutido (`QLineEdit`).

### Preservação Inteligente de Extensão

Ao renomear um arquivo como `invoice_september.pdf`: 

- ATBCmder pré-seleciona automaticamente apenas o nome do arquivo base (`invoice_september`). 
- A extensão do arquivo (`.pdf`) permanece desmarcada e intacta, evitando a remoção acidental da extensão que quebraria as associações de arquivos do macOS. 
- Se desejar modificar a extensão, basta usar as setas do teclado ou pressionar `Cmd+A` dentro da caixa de edição.

### Atalhos de teclado dentro da renomeação embutida

- **`Enter` (`Return`)**: Confirma o novo nome e reindexa o painel. 
- **`Esc`**: Cancela a edição e restaura o nome original sem alterações. 
- **`Tab`**: Confirma o nome atual e imediatamente começa a renomear o *próximo* arquivo na lista, permitindo a renomeação rápida e sequencial de arquivos sem sair do teclado. 

---

## 4. Técnicas de seleção: arquivos de marcação avançada

Em gerenciadores de arquivos tradicionais, a posição do cursor e a seleção estão fortemente acopladas: mover o cursor desmarca os arquivos anteriores, a menos que você mantenha pressionado `Cmd`. No ATBCmder, **foco do cursor** e **seleções marcadas** são dissociadas, permitindo preparação precisa em lote. 

```
  Status Column:
  [ ]  Unselected (cursor may or may not be on row)
  [✔]  Marked / Selected (accumulated into operation payload)
```

### 4.1 Ações de Seleção Global

| Ação | Atalho do macOS | Chave Clássica | ID do comando | Descrição | 
| :--- | :--- | :--- | :--- | :--- | 
| **Selecionar tudo** | `Cmd+A` / `⌘A` | `Ctrl+A` / `Ctrl+Num+` | `cm_MarkMarkAll` | Marca todos os arquivos e pastas no painel ativo. | 
| **Desmarcar tudo** | `Cmd+Shift+A` / `⇧⌘A`| `Ctrl+Shift+A` / `Ctrl+L` | `cm_MarkUnmarkAll` | Limpa todas as marcas no painel ativo. | 
| **Inverter seleção**| `Num*` / `⌥⌘I` | `Num*` | `cm_MarkInvert` | Inverte o estado de seleção: marcado torna-se desmarcado e vice-versa. | 

---

### 4.2 Seleção de padrão e curinga

A seleção de curinga permite direcionar centenas de arquivos específicos em um diretório de milhares com apenas algumas teclas. 

```
┌────────────────────────────────────────────────────────┐
│ Mark Files by Pattern                                  │
│ Pattern: [*.jpg;*.png;*.webp                        ]  │
│                                                        │
│ [✔] Case sensitive       [ ] Regular expression        │
│                      [Cancel]                 [OK (⏎)] │
└────────────────────────────────────────────────────────┘
```

#### Grupo de marcas (`Num+` / `cm_MarkPlus`)

- Pressione **`Num+`** (Keypad Plus ou acione no Menu **Marca** → **Selecionar Grupo**). 
- Insira curingas de shell padrão: 
- `*.log`: Marca todos os arquivos que terminam em `.log`. 
- `*.jpg;*.png;*.webp`: lista separada por ponto e vírgula para corresponder a várias extensões ao mesmo tempo. 
- `data_2026_??.csv`: Corresponde a arquivos mensais de dois dígitos (`01` até `12`). 
- `*draft*`: Corresponde a qualquer arquivo que contenha a palavra "rascunho". 
- Pressione `Enter` para selecionar todas as entradas correspondentes instantaneamente.

#### Desmarcar grupo (`Num-` / `cm_MarkMinus`)

- Pressione **`Num-`** (Teclado Menos). 
- Insira um padrão para remover itens correspondentes de uma seleção existente (por exemplo, `*test*`).

#### Marcar tudo com a mesma extensão (`Shift+Num+` / `cm_MarkCurrentExtension`)

- Posicione o cursor em qualquer arquivo (por exemplo, `app.tsx`). 
- Pressione **`Shift+Num+`**. 
- Cada arquivo `.tsx` no diretório atual é selecionado instantaneamente. 

---

### 4.3 Seleção de Faixa e Ponto

- **Seleção de bloco contínua (`Shift+Up` / `Shift+Down`)**: Manter pressionado `Shift` enquanto navega com as teclas de seta expande um bloco de seleção contíguo para cima ou para baixo. 
- **Alternância de item único (`Space` / `Insert` / `cm_SelectOrDeselectFile`)**: 
- Pressionar `Space` marca ou desmarca o item sob o cursor e calcula imediatamente o tamanho do diretório se estiver em uma pasta. 
- Pressionar `Insert` (ou `Fn+Return` em alguns teclados Mac) marca o item e move automaticamente o cursor para a próxima linha, permitindo passagens rápidas de seleção com um dedo. 
- **Mouse e Trackpad**: 
- `Cmd+Click`: Alterna a seleção em linhas individuais sem alterar outras seleções. 
- `Shift+Click`: Estende a seleção da linha âncora atual para a linha clicada.

### Telemetria de seleção ao vivo na barra de status

Sempre que os arquivos são marcados, a barra de status inferior é atualizada imediatamente: 
```
[ 48 items | 12 selected (284.6 MB) ]   [ Volume Free: 184.2 GB / 494.3 GB ]
```
 
Você obtém conhecimento situacional em tempo real de cargas exatas de bytes antes de se comprometer com grandes cópias ou exclusões. 

---

## 5. Interoperabilidade de arrastar e soltar

ATBCmder trata o recurso arrastar e soltar como um cidadão de primeira classe, ao mesmo tempo que mantém total compatibilidade com fluxos de trabalho ortodoxos e o ecossistema de desktop macOS. 

```
       Dual-Panel Transfer                       External macOS Desktop
 ┌──────────────┐   ┌──────────────┐       ┌──────────────┐   ┌──────────────┐
 │ Left Panel   │══►│ Right Panel  │       │ ATBCmder     │══►│ Finder / App │
 │ (Source)     │   │ (Target)     │       │ Panel        │   │ (Desktop)    │
 └──────────────┘   └──────────────┘       └──────────────┘   └──────────────┘
```

### Arrastando entre painéis

- Clique e arraste os itens marcados do painel ativo através do divisor central para o painel inativo. 
- Solte em qualquer lugar da tabela de arquivos para iniciar a transferência para a pasta de destino. 
- **Soltando em uma subpasta**: Se você soltar diretamente em uma linha de subdiretório específica, o ATBCmder roteia a carga para essa subpasta em vez de para a raiz do painel.

### Interagindo com o macOS Finder, desktop e aplicativos externos

- **Arrastar para o ATBCmder**: Arraste arquivos do Finder, do seu Desktop ou de downloads do AirDrop diretamente para qualquer painel do ATBCmder para copiá-los ou movê-los. 
- **Arrastar para fora do ATBCmder**: Arraste arquivos para fora do ATBCmder diretamente para o VS Code, Terminal (que cola o caminho do arquivo), Slack, Apple Mail ou caixas de upload do navegador da web.

### Teclas modificadoras durante o arrasto

| Chave modificadora | Arrastar Ação | Ícone do cursor do mouse | Descrição | 
| :--- | :--- | :--- | :--- | 
| **Sem modificador** | Ação padrão | Seta Padrão | Cópias entre volumes; move-se dentro do mesmo volume. | 
| **Opção (`⌥`)** | **Forçar cópia** | Emblema `+` verde | Sempre copia itens, deixando os arquivos de origem intactos. | 
| **Comando (`⌘`)** | **Forçar movimento** | Emblema de seta curvada | Sempre move itens, desvinculando os arquivos de origem na chegada. |

### Pastas carregadas por Spring

Ao arrastar arquivos sobre um diretório aninhado no ATBCmder: 

- Passe o cursor do mouse sobre a pasta de destino por **750 milissegundos**. 
- A pasta pisca automaticamente e se abre, navegando por dentro. 
- Você pode navegar em vários níveis em subdiretórios aninhados sem soltar o botão do mouse e, em seguida, soltar sua carga exatamente onde desejar. 

---

## 6. Tratamento de colisões e resolução de conflitos

As colisões de nomes são o momento mais perigoso no gerenciamento de arquivos. Substituir o arquivo errado pode destruir horas de trabalho. ATBCmder implementa um mecanismo de resolução de conflitos de nível empresarial que inspeciona arquivos antes de sobrescrevê-los e fornece controles de segurança granulares. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Confirm File Overwrite                                                                 │
│                                                                                        │
│ File already exists at the destination.                                                │
│                                                                                        │
│ Source:      /Users/brain/Downloads/build_artifacts.zip                                │
│ Source info: 124,518,400 bytes, 2026-09-06 14:15                                       │
│                                                                                        │
│ Destination: /Volumes/Backup/build_artifacts.zip                                       │
│ Dest info:   118,204,112 bytes, 2026-09-01 09:30                                       │
│                                                                                        │
│ Would you like to overwrite it?                                                        │
│                                                                                        │
│ [Skip All]   [Overwrite All]   [Rename]   [Auto-rename]                                │
│                                                                                        │
│ [Cancel]                                        [Skip]               [Overwrite (⏎)]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### O detalhamento da caixa de diálogo Substituir

Quando ocorre uma colisão de alvos, o ATBCmder exibe a caixa de diálogo **Confirmar substituição de arquivo**: 

1. **Inspeção de metadados lado a lado**: 
- Compara tamanhos exatos de arquivos até um único byte. 
- Compara datas de modificação e carimbos de data/hora. Destaca visivelmente se o arquivo de origem é mais recente, mais antigo ou de tamanho idêntico. 
2. **Botões de decisão do item atual**: 
- **Substituir (`Enter`)**: Substitui o arquivo de destino conflitante pelo arquivo de origem. 
- **Pular**: deixa o arquivo de destino existente intacto e continua para o próximo item no lote de transferência. 
- **Cancel (`Esc`)**: Aborta a operação restante imediatamente, preservando todos os arquivos já transferidos. 
3. **Ações de lote e segurança**: 
- **Substituir tudo**: substitui silenciosamente todos os arquivos conflitantes subsequentes neste trabalho de transferência. 
- **Pular tudo**: ignora silenciosamente todos os arquivos conflitantes restantes sem avisar novamente. 
- **Renomear**: solicita que você insira um novo nome personalizado para o arquivo copiado antes de gravar. 
- **Renomeação automática**: anexa automaticamente um contador incremental (por exemplo, `build_artifacts_1.zip`, `build_artifacts_2.zip`), garantindo que ambas as versões sejam preservadas lado a lado sem intervenção manual. 

---

### Políticas de colisão pré-configuradas na caixa de diálogo Copiar

Para grandes trabalhos em lote automatizados ou backups autônomos, você pode pré-configurar o comportamento de conflito antecipadamente no painel expansível **Opções** da caixa de diálogo Copiar/Mover: 

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Copy Options Panel                                                           │
│ ┌─ Conflict Resolution ─────────────────┐ ┌─ Attributes & Behaviors ──────┐  │
│ │ When file exists:      [Ask          ▾]│ │ [✔] Check free space          │ │
│ │ When directory exists: [Merge        ▾]│ │ [✔] Copy date/time            │ │
│ │ When cannot set attr:  [Skip         ▾]│ │ [✔] Copy attributes           │ │
│ └───────────────────────────────────────┘ │ [ ] Drop readonly flag        │  │
│ ┌─ Filters ─────────────────────────────┐ │ [✔] Copy ownership (POSIX)     │ │
│ │ [ ] Exclude empty directories         │ │ [✔] Verify after copy: [SHA256]│ │
│ └───────────────────────────────────────┘ └───────────────────────────────┘  │
│ [Save these options as default]                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```
 

- **Quando o arquivo existe**: 
- `Ask`: Solicita a caixa de diálogo Substituir em cada colisão (padrão). 
- `Overwrite`: Substitui arquivos existentes automaticamente. 
- `Skip`: Ignora arquivos conflitantes automaticamente. 
- `Overwrite older`: Substitui o destino somente se o horário de modificação da origem for mais recente. 
- `Rename copied`: Acrescenta sufixo de contador (`_1`, `_2`) aos arquivos copiados. 
- `Auto-rename target`: Renomeia o arquivo de destino existente e grava o novo arquivo com o nome original. 
- **Quando o diretório existe**: 
- `Merge`: Une o conteúdo da pasta recursivamente. Os subarquivos não conflitantes são copiados nas pastas existentes. 
- `Ask` / `Overwrite` / `Skip`. 
- **Verificação e atributos avançados**: 
- **Verificar espaço livre/Espaço reservado**: Pré-calcula os bytes de origem e garante que o volume de destino tenha capacidade adequada antes de iniciar. 
- **Verificar após cópia**: calcula somas de verificação criptográficas (`SHA-256`, `MD5`, `SHA-1`, `CRC32`) em arquivos de origem e de destino gravados para garantir 100% de integridade dos dados contra corrupção silenciosa de armazenamento. 
- **Seguir links**: controla se os links simbólicos são copiados como referências de ponteiro ou desreferenciados em cópias físicas completas. 
- **Copiar data/hora e propriedade**: preserva datas de criação POSIX, carimbos de data/hora de modificação e IDs de propriedade de usuário/grupo. 

---

## 7. ⚡ Dicas profissionais e aprofundamento: poder avançado do sistema de arquivos

Dominar o gerenciamento de painel duplo significa compreender o substrato UNIX subjacente do macOS. Aqui estão recursos avançados projetados para desenvolvedores, administradores de sistema e profissionais de armazenamento.

### 7.1 Links simbólicos e links físicos (`cm_SymLink`, `cm_HardLink`)

O macOS é baseado no Darwin UNIX, fornecendo dois tipos de links distintos: 

```
  Symbolic Link (Symlink):
  [ Symlink File ] ──(Path Pointer)──► [ Target File / Directory ]
  • Can cross volume boundaries
  • Can point to directories
  • Breaks if target is moved

  Hard Link:
  [ Hard Link Entry ] ──┐
                        ├──(Direct Inode Reference)──► [ Raw Disk Blocks ]
  [ Original Entry  ] ──┘
  • Cannot cross filesystem boundaries (same APFS container)
  • Files only (no directory hard links on macOS)
  • Data persists until all hard links are deleted
```

#### Criando Links Simbólicos (`cm_SymLink`)

1. Realce um ou mais arquivos/pastas no painel ativo. 
2. Selecione **Arquivo de Menu** → **Criar Link Simbólico...** (`cm_SymLink`). 
3. ATBCmder gera automaticamente um link simbólico no painel oposto apontando para o caminho absoluto do item de origem. 
4. Os links simbólicos exibem um sinalizador de atributo `l` distinto (por exemplo, `lrwxr-xr-x`) no painel.

#### Criando links físicos (`cm_HardLink`)

1. Realce arquivos em um volume APFS/HFS+ local. 
2. Selecione **Arquivo de menu** → **Criar link físico...** (`cm_HardLink`). 
3. ATBCmder cria uma entrada de diretório adicional no painel de destino compartilhando exatamente o mesmo inode. 
4. As alterações gravadas em qualquer arquivo são refletidas instantaneamente em ambos. A exclusão de um arquivo não exclui dados até que a contagem de links chegue a zero. 

> [!NOTA] 
> **Restrições de limite de link**: links físicos não podem cruzar limites de volume ou ser criados em compartilhamentos de rede (`vfs://`). Os links simbólicos devem ser usados ​​sempre que houver links entre unidades diferentes ou pontos de montagem remotos. 

---

### 7.2 Permissões e atributos de arquivo (`Alt+Enter` / `cm_SetFileProperties`)

Inspecione e modifique os atributos do arquivo POSIX usando a **Diálogo de Propriedades** abrangente: 

```
┌────────────────────────────────────────────────────────┐
│ Properties - production_api.py                         │
│ ┌─ Metadata ─────────────────────────────────────────┐ │
│ │ Full Path:     /Users/brain/work/production_api.py │ │
│ │ Size:          84,210 bytes                        │ │
│ │ Created:       2026-03-12 10:14:22                 │ │
│ │ Last Modified: 2026-09-06 13:45:01                 │ │
│ │ Last Accessed: 2026-09-06 15:30:10                 │ │
│ └────────────────────────────────────────────────────┘ │
│ ┌─ Permissions (UNIX) ───────────────────────────────┐ │
│ │ Octal Mode: [ 755 ]                                │ │
│ │ ┌─ Owner ──┐   ┌─ Group ──┐   ┌─ Others ─┐         │ │
│ │ │ [✔] Read │   │ [✔] Read │   │ [✔] Read │         │ │
│ │ │ [✔] Write│   │ [ ] Write│   │ [ ] Write│         │ │
│ │ │ [✔] Exec │   │ [✔] Exec │   │ [✔] Exec │         │ │
│ │ └──────────┘   └──────────┘   └──────────┘         │ │
│ └────────────────────────────────────────────────────┘ │
│                             [Cancel]         [OK (⏎)]  │
└────────────────────────────────────────────────────────┘
```
 

1. **Gatilho**: Realce qualquer arquivo ou diretório e pressione **`Alt+Enter`** (`⌥⏎` / `cm_SetFileProperties`). 
2. **Revisão de metadados**: Visualize o caminho completo do arquivo, bytes exatos, hora de criação (`btime`), hora de modificação (`mtime`) e hora do último acesso (`atime`). 
3. **Matriz de permissões UNIX**: 
- **Caixas de seleção interativas**: alterne as permissões de leitura (`r`), gravação (`w`) e execução (`x`) independentemente para **Proprietário**, **Grupo** e **Outros**. 
- **Entrada octal bidirecional**: digite números octais diretamente no campo **Modo octal** (por exemplo, `755` para executáveis, `644` para documentos padrão, `600` para chaves SSH privadas). As caixas de seleção são atualizadas em tempo real e vice-versa. 
4. Pressione `OK` (`Enter`) para aplicar as alterações via POSIX `chmod`. 

---

### 7.3 Cálculo de Espaço Ocupado (`cm_CountDirContent` / `cm_CalculateSpace` / `Space`)

Por padrão, os gerenciadores de arquivos mostram tamanhos de diretório como `<DIR>` ou `--` porque calcular tamanhos de pastas recursivas em milhões de arquivos degradaria o desempenho do sistema de arquivos. ATBCmder oferece cálculo instantâneo sob demanda: 

- **Tamanho de pasta única (`Space` / `Insert` / `cm_SelectOrDeselectFile`)**: Pressione `Space` enquanto descansa em qualquer pasta. ATBCmder calcula o total de bytes recursivos da pasta em segundo plano e substitui `<DIR>` pelo tamanho exato (por exemplo, `14.2 GB`). 
- **Todas as pastas no painel ativo (`Alt+Shift+Enter` / `⌥⇧⏎` / `cm_CountDirContent`)**: 
- Verifica todos os diretórios visíveis no painel atual. 
- Atualiza linhas da tabela com totais de bytes precisos. 
- **Tamanho cumulativo do diretório selecionado (`Ctrl+L` / `⌃L` / `cm_CalculateSpace`)**: 
- Acumula o total de bytes recursivos para pastas selecionadas e resume a contagem de arquivos, a contagem de pastas e o tamanho de armazenamento na barra de status. 

---

### 7.4 Fila de operações em segundo plano (`cm_OperationsPanel`)

Copiar grandes gravações de vídeo de 50 GB ou transferir centenas de milhares de pequenos arquivos de código-fonte nunca deve congelar seu gerenciador de arquivos. ATBCmder incorpora um **Mecanismo de transferência assíncrona de 3 filas**. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Background Operations                                                                  │
│ ┌─ [Queue #1 (Active)] ───────────┬─ [Queue #2 (Idle)] ───┬─ [Queue #3 (Idle)] ──────┐ │
│ │                                                                                    │ │
│ │ [RUNNING] Copy: 14 items -> /Volumes/BackupDrive/Media                             │ │
│ │   Current: RED_4K_Clip_0042.r3d (2.4 GB / 8.6 GB)                                  │ │
│ │   Speed: 428.5 MB/s | ETA: 00:01:14                                                │ │
│ │   [████████████████████████████████░░░░░░░░░░░░░░░░░░] 64%                         │ │
│ │                                                                                    │ │
│ │ [QUEUED] Move: 4 items -> /Volumes/BackupDrive/RAW_Audio                           │ │
│ │ [COMPLETED] Copy: 28 items -> /Users/brain/Projects/Website                        │ │
│ │                                                                                    │ │
│ └────────────────────────────────────────────────────────────────────────────────────┘ │
│                                         [Cancel Task]   [Clear Completed]   [Close]    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Por que três filas independentes?

- **Serializado dentro de cada fila**: As tarefas dentro da **Fila #1** são executadas uma após a outra em ordem FIFO estrita. Isso evita o desgaste da cabeça do disco em discos rígidos mecânicos e evita gargalos de contenção. 
- **Parallel Across Queues**: **Queue #1**, **Queue #2** e **Queue #3** operam simultaneamente em threads de segundo plano separados (`QThread`). Você pode atribuir transferências direcionadas ao **NVMe SSD A** para a Fila nº 1, transferências direcionadas à **Unidade USB externa B** para a Fila nº 2 e uploads de NAS de rede para a Fila nº 3, alcançando a máxima taxa de transferência de barramento agregada.

#### Enviando trabalhos para a fila

1. No painel ativo, selecione seus arquivos e pressione `F5` (Copiar) ou `F6` (Mover). 
2. Em vez de clicar em Iniciar, clique em **Adicionar à fila nº 1** (ou clique na divisa suspensa para selecionar **Fila nº 2** ou **Fila nº 3**). 
3. A caixa de diálogo é imediatamente encerrada, liberando a janela principal para navegação e navegação contínuas.

#### Gerenciando a janela da fila (`cm_OperationsPanel`)

- Clique no botão **⚡ Fila** na barra de ferramentas principal ou selecione **Comandos de menu** → **Operações em segundo plano** (`cm_OperationsPanel`). 
- **Telemetria em tempo real**: inspecione tarefas ativas, arquivos em transferência atuais, velocidades de transferência de streaming (por exemplo, `428.5 MB/s`) e contagens regressivas de ETA calculadas. 
- **Status codificados por cores**: 
- `[QUEUED]`: Esperando na fila. 
- `[RUNNING]`: Transferindo dados ativamente. 
- `[COMPLETED]`: Concluído com sucesso com contagens de bytes verificadas. 
- `[FAILED]`: Foi encontrado um erro de E/S (mensagem de erro exibida em linha). 
- `[CANCELLED]`: Abortado pelo usuário. 
- **Ações de controle**: 
- **Cancelar tarefa**: encerra com segurança a transferência selecionada na fila ou em execução. 
- **Limpar concluídos**: remove trabalhos concluídos, com falha e cancelados da lista. 
- **Resolução de conflitos em segundo plano**: se uma tarefa em segundo plano encontrar um conflito de substituição, o ATBCmder gera uma notificação permitindo que você resolva o problema sem abortar outras tarefas simultâneas. 

---

## 8. Receitas práticas passo a passo

### Receita 1: Backup seguro de vários volumes com verificação de soma de verificação

**Objetivo**: fazer backup de um arquivo de fotos de alto valor do seu Mac para uma unidade APFS externa, garantindo zero corrupção silenciosa e resolvendo possíveis duplicatas com segurança. 

```
Step 1: Open source in Left Panel (~/Pictures/2026_Photos).
Step 2: Open backup destination in Right Panel (/Volumes/SanDiskPro/Photo_Backup).
Step 3: Press Cmd+A (Select All) in Left Panel.
Step 4: Press F5 (Copy).
Step 5: Click [Options ▼] to expand advanced parameters:
        • Set 'When file exists' to: [Auto-rename target]
        • Check [✔] Verify after copy: [SHA-256]
        • Check [✔] Copy date/time
        • Check [✔] Check free space
Step 6: Click [Start].
```
 
*Resultado: ATBCmder calcula hashes SHA-256 durante o fluxo de cópia, confirma a integridade exata do bloco no disco externo e numera automaticamente quaisquer instantâneos conflitantes sem intervenção humana.* 

---

### Receita 2: Preparação de precisão: seleção de curinga, inversão e implantação de link simbólico

**Objetivo**: Em um repositório misto contendo código e artefatos compilados, selecione todos os arquivos JavaScript, TypeScript e JSON enquanto ignora as saídas compiladas `.map` e `.log` e, em seguida, vincule-as simbolicamente em uma pasta de teste. 

```
Step 1: Navigate Left Panel to /Users/brain/dev/app/src.
Step 2: Navigate Right Panel to /Users/brain/dev/testbed/lib.
Step 3: Press Num+ (Select Group).
Step 4: Enter pattern: *.ts;*.tsx;*.js;*.json and press Enter.
Step 5: Notice you also matched *.test.ts files. Press Num- (Unmark Group).
Step 6: Enter pattern: *.test.ts and press Enter.
Step 7: Check your status bar: 84 files selected.
Step 8: Select Menu File → Create Symbolic Link... (cm_SymLink).
```
 
*Resultado: Oitenta e quatro links simbólicos são criados instantaneamente na pasta testbed, apontando claramente para seus arquivos de origem ativos.* 

---

### Receita 3: ingestão paralela de alto rendimento usando filas em segundo plano

**Objetivo**: Descarregue dois cartões de câmera de mídia grandes simultaneamente no RAID da sua estação de trabalho sem bloquear a interface do usuário ou diminuir a velocidade de qualquer leitor de cartão. 

```
Step 1: Mount Card A (/Volumes/CFexpress_A) in Left Panel.
Step 2: Select all raw footage (Cmd+A), press F5 (Copy).
Step 3: Click [Add To Queue #1]. Transfer begins streaming in background.
Step 4: Open Card B (/Volumes/SD_Card_B) in Left Panel (Cmd+T for a new tab).
Step 5: Select all audio tracks (Cmd+A), press F5 (Copy).
Step 6: Click the queue dropdown chevron and choose [Queue #2].
Step 7: Press Toolbar ⚡ (cm_OperationsPanel) to watch both queues stream concurrently.
```
 
*Resultado: ambos os cartões são alimentados simultaneamente com saturação total do barramento de hardware enquanto você continua navegando em arquivos, editando notas ou renomeando ativos.* 

---

## 9. Alertas de segurança e sistema

> [!AVISO] 
> **Exclusão permanente em unidades externas e de rede**: 
> Unidades externas formatadas com FAT32, exFAT ou NTFS (por meio de drivers de terceiros) e compartilhamentos de rede remotos (SMB/SFTP) geralmente não possuem um diretório do sistema macOS `.Lixeiraes`. Ao excluir itens desses volumes, o ATBCmder irá alertá-lo de que a Lixeira não está disponível. Confirmar esta ação **exclui permanentemente** os arquivos. Sempre verifique os cabeçalhos dos caminhos antes de confirmar. 

> [!CUIDADO] 
> **Substituindo arquivos em operações em lote**: 
> Ao usar **Overwrite All** na caixa de diálogo de colisão, o ATBCmder suprime outros alertas de colisão para todo o trabalho. Se o seu diretório de origem contiver nomes de arquivos duplicados acidentalmente, os arquivos de destino existentes serão substituídos irreversivelmente. Considere usar **Renomear automaticamente** ou **Substituir mais antigo** para cópias em lote autônomas. 

> [!IMPORTANTE] 
> **Limitações do link físico APFS**: 
> Links físicos não podem abranger diferentes volumes APFS, partições de disco ou imagens de disco. Se você tentar criar um link físico entre dois pontos de montagem diferentes (como `/Users/...` a `/Volumes/ExternalDrive/...`), a operação falhará. Use **Links Simbólicos** (`cm_SymLink`) sempre que vincular diferentes volumes de armazenamento. 

> [!TIP] 
> **Otimizando velocidades de transferência NVMe**: 
> ATBCmder é otimizado para memória unificada Apple Silicon moderna e SSDs PCIe 4.0/5.0 NVMe. Por padrão, as operações de arquivo utilizam um **buffer de cópia de 1 MB** de alto desempenho (`operations.copy_buffer_size`). Você pode ajustar esse buffer em **Preferências** → **Operações de arquivo** para corresponder a interfaces de rede 10GbE de última geração ou matrizes de armazenamento especializadas. 

---

## 10. Tabela de referência do teclado de matriz dupla

| Categoria | Ação | Atalho do macOS | Chave Clássica | ID do comando | Descrição | 
| :--- | :--- | :--- | :--- | :--- | :--- | 
| **Operações de arquivos principais** | Copiar para destino | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Copia os itens selecionados para o painel inativo. | 
| | Copiar no mesmo painel | `Shift+F5` / `⇧F5` | `Shift+F5` | `cm_CopySamePanel` | Clona o arquivo no painel ativo com prompt para renomear. | 
| | Mover para o alvo | `F6` / `Fn+F6` | `F6` | `cm_Move` | Move os itens selecionados para o painel inativo. | 
| | Novo diretório | `F7` / `Fn+F7` | `F7` | `cm_MkDir` | Cria um novo diretório ou árvore aninhada. | 
| | Excluir para a Lixeira | `F8` / `⌘⌫` | `F8` / `Delete` | `cm_Delete` | Envia itens selecionados para a Lixeira do macOS. | 
| | Exclusão permanente | `Shift+Delete` / `⇧⌦` | `Shift+F8` | `cm_Delete` | Desvincula arquivos imediatamente sem a Lixeira. | 
| | Limpeza segura | `Alt+Delete` / `⌥⌦` | `Alt+Delete` | `cm_Wipe` | Substitui arquivos por dados aleatórios antes de desvincular. | 
| **Renomeando** | Renomeação rápida embutida | `F2` / `Shift+F6` | `Shift+F6` | `cm_RenameOnly` | Renomeia o item ativo diretamente na linha da tabela. | 
| | Caixa de diálogo Renomear | *Arquivo de Menu* | — | `cm_Rename` | Abre a caixa de diálogo de texto modal para renomear. | 
| **Seleção** | Selecionar tudo | `Cmd+A` / `⌘A` | `Ctrl+A` / `Ctrl+Num+` | `cm_MarkMarkAll` | Seleciona todos os arquivos e pastas. | 
| | Desmarcar tudo | `Cmd+Shift+A` / `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+L` | `cm_MarkUnmarkAll` | Limpa todas as seleções. | 
| | Seleção Invertida | `Num*` / `⌥⌘I` | `Num*` | `cm_MarkInvert` | Inverte o estado de seleção de todos os itens. | 
| | Grupo Marca | `Num+` | `Num+` | `cm_MarkPlus` | Seleciona itens por curinga ou padrão RegEx. | 
| | Desmarcar grupo | `Num-` | `Num-` | `cm_MarkMinus` | Desmarca itens por padrão curinga. | 
| | Mesma Extensão | `Shift+Num+` | `Shift+Num+` | `cm_MarkCurrentExtension`| Seleciona todos os itens com a mesma extensão de arquivo. | 
| | Alternar seleção | `Space` / `Insert` | `Insert` / `Space` | `cm_SelectOrDeselectFile` | Alterna a seleção de itens e desce. | 
| **Área de transferência** | Copiar para a área de transferência | `Cmd+C` / `⌘C` | `Ctrl+C` | `cm_CopyToClipboard` | Copia caminhos de arquivos para a área de transferência do sistema. | 
| | Cortar para a área de transferência | `Cmd+X` / `⌘X` | `Ctrl+X` | `cm_CutToClipboard` | Corta caminhos de arquivos para a área de transferência do sistema. | 
| | Colar área de transferência | `Cmd+V` / `⌘V` | `Ctrl+V` | `cm_PasteFromClipboard` | Cola os arquivos da área de transferência no painel ativo. | 
| | Colar como Mover | `Cmd+Option+V` / `⌥⌘V`| `Ctrl+Alt+V` | `cm_PasteAsMove` | Move os arquivos da área de transferência para o painel ativo. | 
| | Copiar caminho completo | *Editar Menu* | — | `cm_CopyFullPath` | Copia o caminho absoluto do UNIX para a área de transferência. | 
| | Copiar nome do arquivo | *Editar Menu* | — | `cm_CopyFileNameToClip` | Copia o nome do arquivo para a área de transferência. | 
| **Links e Espaço** | Criar link simbólico | *Arquivo de Menu* | — | `cm_SymLink` | Cria um link simbólico no painel de destino. | 
| | Criar link físico | *Arquivo de Menu* | — | `cm_HardLink` | Cria link físico no painel de destino. | 
| | Propriedades / Chmod | `Alt+Enter` / `⌥⏎` | `Alt+Enter` | `cm_SetFileProperties` | Abre permissões, chmod octal e carimbos de data/hora. | 
| | Calcular Espaço | `Alt+Shift+Enter` / `⌥⇧⏎` | `Alt+Shift+Enter` | `cm_CountDirContent` | Calcula tamanhos de diretório recursivos (`Ctrl+L` / `cm_CalculateSpace` para o total selecionado). | 
| **Fila de transferência**| Fila de fundo | `Toolbar ⚡` | — | `cm_OperationsPanel` | Abre o monitor de transferência em segundo plano de 3 filas. |

--- 

<div align="center"> 
<p>Agora que você domina as operações diárias de arquivos, técnicas de seleção e transferências em segundo plano:</p> 
<p><strong><a href="viewers_and_editors.md">Prossiga para o Capítulo 4: Lista universal e editores integrados &rarr;</a></strong></p> 
</div>