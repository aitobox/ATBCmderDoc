# Bem-vindo ao ATBCmder

[![macOS](https://img.shields.io/badge/platform-macOS%2012%2B-blue.svg)](download.md) 
[![Architecture](https://img.shields.io/badge/arch-Apple%20Silicon%20(ARM64)-orange.svg)](download.md) 
[![Release](https://img.shields.io/badge/release-latest-green.svg)](download.md) 
[![Privacy](https://img.shields.io/badge/telemetry-zero%20tracking-brightgreen.svg)](privacy_policy.md) 

Bem-vindo ao portal de documentação oficial do **ATBCmder** — o gerenciador de arquivos rápido, com teclado duplo e painel duplo, projetado especificamente para macOS. ATBCmder une a herança de velocidade e comando de gerenciadores de arquivos ortodoxos (Total Commander, Double Commander, Norton Commander) com design moderno do macOS, integração de sistema nativo e ferramentas elétricas avançadas. 

---

## A filosofia do painel duplo

Os gerenciadores de arquivos tradicionais de janela única para desktop, como o macOS Finder, forçam os usuários a um ciclo interminável de abertura de janelas sobrepostas, perda de controle das pastas de origem e destino e risco de quedas acidentais em subpastas erradas. 

```
Traditional File Browsing (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Folder A (Where was I?)│ ──?  │ Folder B (Which one?)  │  → Clutter, lost focus,
└────────────────────────┘      └────────────────────────┘    and accidental drops

The ATBCmder Way (Orthodox Dual-Panel):
┌───────────────────────────────┬───────────────────────────────┐
│     ACTIVE PANEL (Source)     │    INACTIVE PANEL (Target)    │
│  Files waiting for action     │  Predictable destination      │
│  [ Copy / Move / Diff / Sync  ═════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘
```
 

ATBCmder resolve isso por meio do **Paradigma de Painel Duplo Fonte-Target**: 

- **Orientação constante**: Duas visualizações de diretório independentes ficam sempre visíveis lado a lado. 
- **Operações direcionais previsíveis**: quando você aciona Copiar (`F5`) ou Mover (`F6`), o ATBCmder transfere automaticamente itens do **Painel Ativo** (onde está o cursor) para o **Painel Inativo** (a visualização oposta). Sem arrastar, sem adivinhar, sem procurar janelas de destino ocultas. 
- **Velocidade do teclado**: Mantenha as mãos no teclado. Percorra diretórios, selecione arquivos com curingas, inspecione arquivos e execute transformações em lote em milissegundos. 
- **Zero confusão na janela do Finder**: uma janela cuida de tudo: volumes locais, servidores de rede (FTP, SFTP, SMB, WebDAV), conteúdo de arquivo (`.zip`, `.7z`, `.tar`) e filas de transferência em segundo plano. 

---

## Tour e pontos de referência da interface visual

O ATBCmder organiza o poder em um layout limpo e intuitivo, projetado para fornecer consciência situacional instantânea de ambos os diretórios. 

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] Menu Bar: File   Mark   Commands   Show   Configuration   Help                       │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] Main Toolbar:  [🔍 Search]  [⚡ Queue]  [⚙️ Preferences]  [📁 Drive Bar]             │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] Breadcrumbs: 🏠 > Users > brain > work  │ [3] Breadcrumbs: 💾 > Volumes > Backup     │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] Tab Bar: [Project Alpha ✕] [Docs] [+]   │ [4] Tab Bar: [2026 Archive ✕] [+]          │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] Left Panel (Active / Source)     │ [6]  │ [5] Right Panel (Inactive / Target)        │
│ 📁 .. [Parent Directory]             │  M   │ 📁 .. [Parent Directory]                   │
│ 📁 assets                            │  I   │ 📁 archive_2025                            │
│ 📁 src                               │  D   │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  D   │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  L   │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │  E   │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] Status Bar: 6 items | 2 selected (10.5 KB)   │ Drive: 142.6 GB free / 494.3 GB total │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

### Referência de marco da UI

1. **Integração com barra de menu e macOS nativo (`[1]`)**: suporte completo ao menu do aplicativo macOS, atalhos padrão (`⌘,`, `⌘Q`, `⌘W`) e acesso completo ao menu para todos os comandos internos do Commander (`cm_*`). 
2. **Barra de ferramentas principal e iniciadores rápidos (`[2]`)**: acesso imediato com um clique à Pesquisa (`Alt+F7`), Fila de transferência em segundo plano (`cm_OperationsPanel`), Preferências (`Cmd+,`) e seletores de unidade. 
3. **Barra de caminho de navegação atual (`[3]`)**: Clique em qualquer segmento de diretório no caminho para pular diretamente para cima na hierarquia. Clique na seta suspensa do segmento para navegar pelos subdiretórios. 
4. **Guias de pastas e espaços de trabalho (`[4]`)**: abra guias ilimitadas em cada painel (`Cmd+T`), feche guias (`Cmd+W`), bloqueie locais favoritos e salve espaços de trabalho inteiros com guias de painel duplo (`cm_SaveFavoriteTabs`). 
5. **Painéis de arquivos duplos (`[5]`)**: Tabelas de arquivos independentes. O painel ativo exibe uma borda de destaque distinta e um cursor focado. Mude o foco instantaneamente com `Tab`. 
6. **Barra de ferramentas do meio e divisor arrastável (`[6]`)**: Uma faixa vertical de ação rápida colocada diretamente no divisor do painel. Fornece gatilhos de um clique para visualizar (`F3`), editar (`F4`), copiar (`F5`), mover (`F6`), nova pasta (`F7`), excluir (`F8`), limpar e trocar painéis (`cm_Exchange`). Arraste o divisor para a esquerda ou direita para redimensionar os painéis. 
7. **Barra de status e medidor de armazenamento da unidade (`[7]`)**: mostra contagens de arquivos em tempo real, estatísticas de itens selecionados, tamanhos de bytes agregados e um medidor de capacidade de armazenamento de volume ativo com cálculo de espaço livre. 

---

## Vitrine de interface

Explore os recursos do ATBCmder por meio dos principais destaques dos recursos: 

| Painéis duplos e visualização em árvore | Barra de ferramentas de ação rápida central | 
| :---: | :---: | 
| ![Tree View and Thumbnail Display](images/treeview+thumbview.png) | ![Middle Toolbar](images/middle_toolbar.png) | 
| *Layout de painel duplo com árvore de diretórios e visualização de miniaturas.* | *Faixa de ação rápida: Visualizar, Editar, Copiar, Mover, MkDir, Excluir, Limpar.* | 

| Comandos de linguagem natural | Visualização de ramificação plana recursiva | 
| :---: | :---: | 
| ![Natural Language File Search](images/semantic_command.png) | ![Flat View of Nested Directories](images/branch_view.png) | 
| *Pesquisa instantânea com tecnologia macOS Spotlight e análise de consulta semântica.* | *Visualização de ramificação (`Cmd+B`) exibindo conteúdo aninhado em uma única lista simples.* | 

| Rede e VFS remoto | Arquivar VFS (sem necessidade de extração) | 
| :---: | :---: | 
| ![Network VFS](images/network_vfs.png) | ![Archive VFS](images/archive_vfs.png) | 
| *Conecte-se a compartilhamentos de rede FTP, SFTP, WebDAV e SMB/Samba.* | *Navegue e edite dentro de arquivos ZIP, TAR, 7z como pastas padrão.* | 

---

## Escolha o seu caminho

Quer você nunca tenha tocado em uma ferramenta de painel duplo antes ou tenha passado duas décadas usando o Total Commander, o ATBCmder oferece um caminho otimizado a seguir:

### 🟢 Faixa A: Novo em gerenciadores de arquivos de painel duplo?

*Bem-vindo a uma maneira mais rápida e limpa de gerenciar arquivos no macOS.* 

Se você vier do Finder ou de sistemas operacionais de desktop padrão, os gerenciadores de arquivos ortodoxos podem parecer estranhos à primeira vista. Depois de aprender os padrões principais, você nunca mais vai querer voltar a arrastar arquivos por janelas espalhadas: 

1. **Comece com os conceitos principais**: leia o [Capítulo 1: Fundamentos e configuração do macOS](getting_started.md) para entender os painéis Ativo versus Inativo, a barra de ferramentas intermediária e a concessão de permissões de disco do macOS. 
2. **Domine as operações diárias**: aprenda como copiar, mover, renomear e excluir sem tocar no mouse no [Capítulo 3: Operações diárias e fila de arquivos](file_operations.md). 
3. **Visualizar tudo instantaneamente**: descubra como visualizar imagens, ouvir arquivos de áudio, ler códigos e inspecionar PDFs com um único toque de tecla no [Capítulo 4: Lista universal e editores](viewers_and_editors.md). 
4. **Siga os guias práticos**: confira fluxos de trabalho práticos do dia a dia e perguntas comuns no [Capítulo 9: Receitas e solução de problemas do mundo real](faq_howtos.md). 

---

### ⚡ Faixa B: Migrando do Total Commander/Double Commander?

*Toda a potência e reflexos do teclado que você conhece, projetados nativamente para macOS.* 

ATBCmder foi criado para trazer a experiência autêntica do Commander para o macOS moderno sem executar o X11 desajeitado, wine wrappers ou portas legadas sem manutenção: 

1. **Domine os atalhos de teclado de matriz dupla**: revise nossa matriz de atalhos lado a lado completa (`macOS Cmd` vs `Commander Fn`) no [Capítulo 8: Domine os atalhos de teclado](keyboard_shortcuts.md). 
2. **Aproveite ferramentas elétricas avançadas**: use a ferramenta de multi-renomeação em lote (`Ctrl+M`), comparação de arquivos lado a lado (`Meta+Shift+F12`), sincronização de pasta (`Shift+F12`) e pesquisa avançada no [Capítulo 5: Ferramentas elétricas e automação](power_tools.md). 
3. **Conecte-se a sistemas remotos e virtuais**: navegue e edite diretamente nos arquivos `.zip` e `.tar` com reempacotamento em tempo real ou gerencie servidores remotos via SFTP, SMB e WebDAV no [Capítulo 6: Rede e sistemas de arquivos virtuais](network_and_vfs.md). 
4. **Personalizar e portar sua configuração**: Revincule comandos, configure o comportamento de atualização automática e exporte seu XML de configuração no [Capítulo 7: Preferências e Personalização](preferences_and_customization.md). 

---

## Índice mestre

Explore o conjunto completo de documentação do ATBCmder:

### 🚀 [Capítulo 1: Fundamentos e configuração do macOS](getting_started.md)

Entenda a filosofia de painel duplo, explore a anatomia da interface, configure as permissões do macOS App Sandbox por meio do assistente de integração (`cm_GrantFilesystemAccess`), defina substituições de idioma do sistema em mais de 30 localidades e personalize temas claros/escuros.

### 🧭 [Capítulo 2: Guias de navegação e pastas](navigation_and_tabs.md)

Mova-se facilmente pelas árvores de diretórios usando trilhas interativas, saltos de teclado (`Ctrl+\`, `Backspace`), organização com várias guias (`Cmd+T`, `Cmd+W`), conjuntos de espaços de trabalho favoritos de painel duplo (`cm_SaveFavoriteTabs`), marcadores da lista de favoritos do diretório (`Ctrl+D`) e modos de visualização flexíveis (resumido, colunas completas, miniaturas, visualização em árvore e visualização de ramificação plana `Cmd+B`).

### 📁 [Capítulo 3: Operações diárias de arquivos e fila](file_operations.md)

Execute operações de arquivo rápidas e sólidas: copiar (`F5`), mover (`F6`), nova pasta (`F7`), excluir para a lixeira (`F8`) e renomeação rápida embutida (`F2`). Seleções mestres de caracteres curinga e atributos, interoperabilidade de arrastar e soltar, resolução de conflitos de colisão, permissões octais UNIX (`Alt+Enter`) e monitoramento de transferência assíncrona por meio da fila de operações em segundo plano (`cm_OperationsPanel`).

### 👁️ [Capítulo 4: Lista universal e editores integrados](viewers_and_editors.md)

Inspecione arquivos sem iniciar software pesado de terceiros. Use o Quick View (`Ctrl+Q` / `Cmd+Q`) para visualizações ao vivo do painel lateral e o Universal Lister (`F3`) para documentos do Word, planilhas, bancos de dados SQLite, blocos de notas Jupyter, EPUBs, código realçado por sintaxe, inspeção de byte hexadecimal bruto (`2`), anotações de imagem e marca d'água (`F4`), leitor de documentos PDF e reprodutores de mídia de áudio/vídeo integrados com reprodução de áudio em segundo plano. Edite arquivos diretamente com o editor de texto integrado (`F4`).

### ⚡ [Capítulo 5: Ferramentas elétricas e automação](power_tools.md)

Automatize desafios complexos de gerenciamento de arquivos: multi-renomeação em lote (`Ctrl+M`) com tokens e substituição RegEx, comparação visual de arquivos lado a lado (`Meta+Shift+F12`), sincronização de diretório bidirecional (`Shift+F12`), pesquisa multifiltro avançada (`Alt+F7`) com "Feed to Listbox", Spotlight & Natural Comandos semânticos de linguagem (`/`), divisor e vinculador de arquivos, verificação de soma de verificação (MD5, SHA-256, CRC32), limpeza multipass segura (`cm_Wipe`) e terminal incorporado (`Ctrl+J`).

### 🌐 [Capítulo 6: Rede e sistemas de arquivos virtuais](network_and_vfs.md)

Trate servidores remotos e arquivos compactados como pastas locais comuns usando URIs `vfs://` unificados. Navegue dentro dos arquivos `.zip`, `.tar` e `.7z` sem descompactar, edite arquivos no local com reempacotamento automático ao vivo, crie arquivos criptografados (`Alt+F5`) e gerencie conexões persistentes através de FTP, SFTP (chaves SSH), WebDAV e compartilhamentos de rede SMB/Samba.

### ⚙️ [Capítulo 7: Preferências e Personalização](preferences_and_customization.md)

Configure o ATBCmder para corresponder exatamente ao seu estilo de trabalho. Pesquise e vincule teclas de atalho primárias/secundárias com avisos de conflito em tempo real, personalize colunas de tabelas de arquivos e regras de ajuste automático, ajuste a sensibilidade de atualização automática do observador de arquivos, defina associações de extensão de arquivo personalizadas e exporte/importe perfis de configuração portáteis (`cm_ExportConfiguration`).

### ⌨️ [Capítulo 8: Atalhos de teclado mestres](keyboard_shortcuts.md)

Guia abrangente de referência de atalhos de matriz dupla comparando atalhos nativos do macOS (modificadores `Cmd`) com teclas de função clássicas do Commander (`F1`-`F12`). Inclui instruções dedicadas para o comportamento do modificador `Fn` do teclado Apple e a configuração das "teclas de função padrão" do macOS.

### ❓ [Capítulo 9: Receitas e solução de problemas do mundo real](faq_howtos.md)

Orientações práticas e passo a passo para tarefas comuns do mundo real: sincronização de backups de diretório, renomeação em lote de bibliotecas de fotos de câmeras com carimbos de data e hora, montagem de unidades NAS de rede, atualização de arquivos de configuração em arquivos remotos e diagnóstico de erros de permissão de sandbox do macOS ou problemas de atualização automática.

### 📥 [Capítulo 10: Download e instalação](download.md)

Opções de instalação para macOS 12.0+ Monterey por meio do Sequoia. Baixe diretamente da Mac App Store ou obtenha pacotes de instalação DMG independentes criados nativamente para Apple Silicon (arquitetura M1/M2/M3/M4, ARM64). *Nota: Macs Intel (x86_64) não são suportados atualmente.* 

---

### 🔒 [Apêndice: Política de Privacidade e Segurança de Dados](privacy_policy.md)

Nosso compromisso fundamental com a privacidade do usuário: ATBCmder inclui zero rastreamento, zero registro telemétrico e zero análise de histórico. Todas as operações de arquivo, credenciais de rede e índices de pesquisa permanecem estritamente locais no seu Mac. 

--- 

<div align="center"> 
<p>Pronto para começar?</p> 
<p><strong><a href="getting_started.md">Prossiga para o Capítulo 1: Fundamentos e configuração do macOS &rarr;</a></strong></p> 
</div>