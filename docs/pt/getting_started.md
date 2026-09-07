# Capítulo 1: Fundamentos e configuração do macOS

Bem-vindo ao **ATBCmder**! Projetado nativamente para macOS 12+ no Apple Silicon (M1/M2/M3/M4, arquitetura ARM64; Intel x86_64 não é compatível atualmente), o ATBCmder traz velocidade incomparável, agilidade de teclado e precisão do gerenciamento ortodoxo de arquivos de painel duplo para o Mac. 

Este capítulo orienta você na filosofia central do painel duplo, detalha todos os principais pontos de referência da interface, orienta você na integração de permissões do macOS App Sandbox e fornece as configurações essenciais do sistema necessárias para uma experiência perfeita. 

---

## 1. Guia de início rápido visual: a filosofia do painel duplo

Se você usou o macOS Finder, está acostumado a abrir várias janelas sobrepostas, arrastar arquivos em áreas de trabalho desordenadas e esperar que os arquivos cheguem à pasta de destino pretendida, em vez de uma subpasta adjacente acidental. 

O ATBCmder substitui esse atrito pelo paradigma **Orthodox File Manager (OFM)** testado pelo tempo: dois painéis de diretório independentes e complementares colocados lado a lado. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  ACTIVE (SOURCE) PANEL                     INACTIVE (TARGET) PANEL              │
│  /Users/username/Downloads                 /Volumes/BackupDrive/Projects        │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│  Name               Size    Date    │   │  Name                Size     Date    │
│  ▸ [..]                     --:--   │ C │  ▸ [..]                       --:--   │
│  ▸ Project_Assets   <DIR>   Yesterday O │  ▸ 2025_Archive      <DIR>    May 12  │
│  ● release_notes.md 14.2 KB Today   │ P │  ▸ Website_V2        <DIR>    Aug 28  │
│  ● update_v1.7.pkg  84.5 MB Today   │ Y │  ● config.yaml       3.2 KB   Jun 04  │
│                                     │ ➔ │                                       │
│  [ Focused / Blue Accent Outline ]  │   │  [ Unfocused / Subdued Outline ]      │
└─────────────────────────────────────┴───┴───────────────────────────────────────┘
```

### O modelo ativo (fonte) vs. inativo (destino)

No ATBCmder, você nunca precisa se perguntar onde uma operação terá efeito: 

1. **O Painel Ativo (Fonte)**: 
- Este é o painel onde o foco e o cursor do teclado residem atualmente. 
- Qualquer seleção, navegação ou ação executada visa diretamente este painel. 
- **Visual Cue**: O painel ativo apresenta um anel de foco proeminente (cor de destaque do sistema macOS), texto da guia destacado e um destaque de cursor ativo distinto no item atualmente em foco. 

2. **O Painel Inativo (Alvo)**: 
- Este é o painel oposto. Permanece totalmente visível, exibindo uma hierarquia de pastas independente. 
- O painel inativo atua como **destino automático** para operações de arquivo iniciadas no painel ativo. 
- **Visual Cue**: o painel inativo exibe uma borda suave, texto ligeiramente esmaecido e títulos de guias silenciados.

### Operações direcionais: sempre origem ➔ destino

Ao iniciar uma operação no ATBCmder, o aplicativo entende automaticamente a direção: 

- **Copiar (`F5` / `Cmd+C` ➔ `Cmd+V`)**: Copia os arquivos selecionados do painel Ativo (Origem) diretamente para o diretório atualmente mostrado no painel Inativo (Destino). 
- **Mover (`F6` / `Cmd+C` ➔ `Opt+Cmd+V`)**: Move os arquivos selecionados do painel Ativo para o painel Inativo sem precisar digitar ou pesquisar o diretório de destino. 
- **Sincronização de Diretórios (`Shift+F12` / `cm_SyncDirs`)**: Compara o diretório no painel ativo com o diretório no painel inativo. 

> [!TIP] 
> **Não é necessária nenhuma suposição de arrastar e soltar**: você não precisa arrastar itens através dos limites da tela. Basta selecionar o que deseja no painel ativo, pressionar `F5` (Copiar) ou `F6` (Mover), pressionar `Enter` para confirmar o prompt e o ATBCmder transferirá os arquivos imediatamente.

### Navegação no painel e mudança de foco

| Ação | Atalho do macOS | Chave do Comandante Clássico | ID do comando | Descrição | 
| :--- | :--- | :--- | :--- | :--- | 
| **Mudar foco** | `Tab` | `Tab` | `cm_FocusSwap` | Alterna o foco do teclado entre os painéis esquerdo e direito (`cm_SwitchPanel`). | 
| **Foco reverso** | `Shift+Tab` | `Shift+Tab` | `cm_FocusSwap` | Inverte a ordem do foco nos painéis e controles. | 
| **Trocar esquerda e direita** | `Ctrl+U` | `Ctrl+U` | `cm_Exchange` | Troca caminhos de diretório entre os painéis esquerdo e direito sem perder guias ou seleção. | 
| **Proporção de equalização** | `Double-click splitter` | `Double-click splitter` | — | Redefine automaticamente o divisor intermediário para um equilíbrio limpo de 50/50. | 

---

## 2. Anatomia da interface e tour pelos pontos de referência

ATBCmder fornece uma interface macOS limpa e nativa construída com Qt6 e PySide6, projetada de acordo com as Diretrizes de Interface Humana da Apple, ao mesmo tempo que respeita os fluxos de trabalho clássicos do comandante centrados no teclado. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ [1] NATIVE MACOS MENU BAR                                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [2] TOP MAIN TOOLBAR  [ ↺ Refresh ] [ 📋 Copy ] [ ✂ Move ] [ 🗑 Delete ] ...   │
├─────────────────────────────────────┬───┬───────────────────────────────────────┤
│ [3] BREADCRUMB BAR (Left Panel)     │   │ [3] BREADCRUMB BAR (Right Panel)      │
│  / ▸ Users ▸ username ▸ Projects    │   │  /Volumes ▸ Backup ▸ Assets           │
├─────────────────────────────────────┤   ├───────────────────────────────────────┤
│ [4] FOLDER TABS: [Dev] [Docs] [+]   │[6]│ [4] FOLDER TABS: [Photos] [Backup] [+]│
├─────────────────────────────────────┤MID│───────────────────────────────────────┤
│                                     │DLE│                                       │
│ [5] DUAL FILE PANEL (Left)          │   │ [5] DUAL FILE PANEL (Right)           │
│     - Virtualized table listing     │BAR│     - Virtualized table listing       │
│     - Name, Ext, Size, Date, Attr   │ & │     - Name, Ext, Size, Date, Attr     │
│     - Real-time sort & filter       │SPL│     - Real-time sort & filter         │
│                                     │IT-│                                       │
│                                     │TER│                                       │
├─────────────────────────────────────┴───┴───────────────────────────────────────┤
│ [7] STATUS BAR & DRIVE STORAGE METER                                            │
│  3 of 28 files selected (42.8 MB / 1.2 GB)  |  Macintosh HD: 218.4 GB free      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### [1] Barra de menu nativa do macOS

Totalmente integrado à barra de menu superior do macOS. Todas as operações, alternâncias de visualização, ferramentas elétricas e preferências são categorizadas logicamente: 

- **Arquivo**: Nova guia, Fechar guia, Propriedades do arquivo, Permissões da sandbox, Sair. 
- **Marcar**: Selecionar Grupo (`Num+`), Desmarcar Grupo (`Num-`), Inverter Seleção (`Num*`), Selecionar Tudo (`Cmd+A`). 
- **Comandos**: Hotlist de diretório (`Ctrl+D`), unidades esquerda/direita (`Alt+F1/F2`), pesquisa (`Alt+F7`), sincronização de diretórios (`Shift+F12`), troca de painéis (`Ctrl+U`), terminal (`Ctrl+J`). 
- **Mostrar**: alterna o modo de visualização (breve, colunas completas, miniaturas, árvore, visualização de ramificação plana), visibilidade da barra de ferramentas, layout de painéis horizontais. 
- **Configuração**: Opções/Preferências (`Cmd+,`), Salvar Posição (`cm_ConfigSavePos`), Salvar Abas.

### [2] Barra de ferramentas principal superior

Localizado diretamente abaixo da barra de título da janela. Fornece acesso instantâneo com um clique a comandos globais: 

- **Ações padrão**: Atualizar (`Ctrl+R`), Visualização rápida (`Ctrl+Q`), Copiar (`F5`), Mover (`F6`), Nova pasta (`F7`), Excluir (`F8`), Pesquisar (`Alt+F7`) e Opções (`Cmd+,`). 
- **Personalizável**: personalize os tamanhos dos ícones (16px a 48px), alterne os rótulos de texto dos botões ou oculte a barra de ferramentas inteiramente por meio do menu **Mostrar** → **Mostrar barra de ferramentas** para maximizar o espaço da tela.

### [3] Barra de navegação interativa estilo Finder

Posicionada acima de cada painel de arquivo, a barra de caminho de navegação permite saltos de hierarquia extremamente rápidos: 

- **Navegação por segmento**: clique em qualquer pasta ancestral na cadeia de navegação (por exemplo, clicando em `username` em `/Users/username/Projects/ATBCmder`) para navegar diretamente para esse diretório. 
- **Listas suspensas de irmãos**: passe o mouse ou clique na seta em forma de cruz entre os segmentos para revelar um menu suspenso listando todas as pastas irmãs naquele nível. 
- **Menu de contexto do segmento**: clique com o botão direito em qualquer segmento de localização atual para acessar utilitários contextuais rápidos: 
- **Abrir em nova aba**: Mantém sua visualização atual enquanto abre o diretório pai em uma nova aba. 
- **Revelar no Finder**: abre o diretório no macOS Finder (`open -R`). 
- **Copiar Caminho**: Copia o caminho UNIX absoluto do segmento para a área de transferência do sistema. 
- **Abrir no Terminal**: gera o Terminal macOS diretamente dentro dessa pasta (`open -a Terminal`). 
- **Edição direta de caminho (`BreadcrumbLineEdit`)**: Clique duas vezes no espaço vazio à direita da cadeia de navegação estrutural. A barra se converte instantaneamente em um campo de texto editável onde você pode colar ou digitar qualquer caminho (por exemplo, arquivos `/var/log`, `~/Library` ou `vfs://`). Pressione `Enter` para navegar ou `Esc` para cancelar.

### [4] Barra de guias de pastas

Cada painel mantém um conjunto independente de guias: 

- Abra novas abas com `Cmd+T` (`cm_NewTab`), feche abas com `Cmd+W` (`cm_CloseTab`). 
- Arraste e solte para reordenar as guias em um painel. 
- Clique com o botão direito nas guias para bloquear caminhos, renomear títulos, fechar duplicatas ou duplicar guias no painel oposto.

### [5] Painéis de arquivos duplos

Listas de arquivos virtualizados de alto desempenho, capazes de renderizar pastas com centenas de milhares de entradas sem problemas na interface do usuário: 

- Classificação de colunas: clique em qualquer cabeçalho (Nome, Ext, Tamanho, Data, Atributos) para classificar em ordem crescente ou decrescente. 
- Vários modos de visualização: visualização de detalhes completos, visualização de grade resumida, visualização de galeria de miniaturas, visualização de árvore e visualização recursiva de ramificação plana (`Cmd+B`).

### [6] Barra de ferramentas central e divisor arrastável

Posicionada diretamente entre os painéis de arquivos esquerdo e direito, a barra de ferramentas intermediária é um recurso exclusivo do ATBCmder que combina gerenciamento de arquivos com um clique com um divisor de painel ajustável: 

![Middle Toolbar](images/middle_toolbar.png) 

- **Faixa de ação rápida**: abriga botões verticais para operações comuns: 
- `cm_Copy` (Cópia) 
- `cm_Move` (Mover / Cortar) 
- `cm_Delete` (Excluir para a Lixeira) 
- `cm_MkDir` (Novo Diretório) 
- `cm_Rename` (renomeação rápida inline) 
- `cm_View` (Listador Universal) 
- `cm_Edit` (Editor interno de texto/código) 
- `cm_Exchange` (trocar painéis esquerdo e direito) 
- `cm_SyncDirs` (sincronizador de pastas) 
- `cm_FileSearch` (Pesquisa Avançada) 
- **Arrastar Contínuo do Divisor**: Mover o cursor do mouse sobre a barra do meio altera o ponteiro para um cursor de divisão horizontal (`SplitHCursor`). Clique e arraste horizontalmente para ajustar suavemente a proporção da largura entre os dois painéis. 
- **Predefinições de proporção de tema elegante**: ao usar o tema "Elegante" moderno, a barra central exibe controles segmentados, permitindo ajuste instantâneo para distribuição de largura do painel **50/50**, **70/30** ou **30/70**. 
- **Preferências da barra de ferramentas do meio**: ative ou desative a barra de ferramentas do meio, ajuste os tamanhos dos ícones ou alterne entre botões planos modernos e divisores rebaixados clássicos em **Preferências** (`Cmd+,`) → **Barras de ferramentas** → **Barra de ferramentas do meio**.

### [7] Barra de status e medidor de armazenamento da unidade

Ancorado na parte inferior da janela: 

- **Estatísticas de seleção**: mostra métricas em tempo real para o painel ativo: 
- Contagem total de itens e tamanho total da pasta. 
- Número de itens selecionados e tamanho de byte selecionado combinado. 
- **Medidor de armazenamento da unidade**: indicador visual de uso do disco exibindo o nome do volume atualmente montado (por exemplo, `Macintosh HD`), capacidade total, armazenamento usado e porcentagem de espaço livre restante. 

---

## 3. Receita passo a passo: sandbox do aplicativo macOS e permissões do sistema de arquivos

O macOS moderno emprega sandboxing de segurança de aplicativos rigoroso para proteger os dados do usuário contra acesso não autorizado. Ao executar o ATBCmder (especialmente quando instalado pela Mac App Store ou distribuído com sandbox ativado), o aplicativo é isolado em seu próprio diretório de contêiner seguro: 
`~/Library/Containers/com.aitobox.atbcmder/Data` 

Por padrão, os aplicativos em sandbox não podem inspecionar ou modificar arbitrariamente arquivos fora de seu contêiner, a menos que o usuário conceda permissão explicitamente por meio dos painéis abertos nativos da Apple. 

O ATBCmder simplifica esse processo de integração com **Favoritos com escopo de segurança**, permitindo que você conceda permissão uma vez e desfrute de acesso persistente e irrestrito em todas as sessões futuras.

### Noções básicas sobre marcadores com escopo de segurança

Ao autorizar um caminho de pasta usando macOS `NSOpenPanel`: 

1. O macOS emite um **Marcador com escopo de segurança** criptográfico (`NSURLBookmarkCreationWithSecurityScope`). 
2. ATBCmder serializa e salva este marcador em seu diretório de configuração: 
`~/Library/Application Support/ATBCmder/sandbox_bookmarks.plist` 

3. A cada inicialização do aplicativo, o ATBCmder resolve e ativa automaticamente esses marcadores via `startAccessingSecurityScopedResource()`. 
4. Uma vez concedido, você nunca mais precisará autorizar novamente esses diretórios.

### Passo a passo de configuração guiada: usando `cm_GrantFilesystemAccess`

Para configurar suas permissões na primeira inicialização ou a qualquer momento posteriormente, siga estas etapas:

#### Etapa 1: abra o assistente de integração de permissões

Na barra de menu nativa, selecione **Arquivo** (ou **Ajuda**) → **Conceder acesso ao sistema de arquivos…** ou acione o comando interno `cm_GrantFilesystemAccess`. A caixa de diálogo de integração é exibida: 

```
┌─────────────────────────────────────────────────────────────┐
│  Grant Filesystem Access                                [x] │
├─────────────────────────────────────────────────────────────┤
│  Because this version of ATBCmder runs inside a secure      │
│  macOS Sandbox, it needs your permission to access          │
│  critical folders.                                          │
│                                                             │
│  [  Grant Access to Root Directory (/)  ]                   │
│                                                             │
│  [  Grant Access to External Disks (/Volumes)  ]            │
│                                                             │
│  [  Open Full Disk Access Settings…  ]                      │
│                                                             │
│  Root directory access is required by the App Sandbox.      │
│  Full Disk Access is a separate macOS permission for        │
│  protected user data.                                       │
│                                                   [ Done ]  │
└─────────────────────────────────────────────────────────────┘
```

#### Etapa 2: conceder acesso ao diretório raiz (`/`)

1. Clique em **"Conceder acesso ao diretório raiz (/)"**. 
2. ATBCmder invoca a planilha `NSOpenPanel` nativa do macOS, apontando para o disco raiz `Macintosh HD` (`/`). 
3. Clique em **"Conceder acesso"** (ou **Abrir**). 
4. O botão é atualizado imediatamente para **"Acesso ao diretório raiz concedido ✓"** e fica desativado. 
5. **O que isso permite**: Autorizar o caminho raiz `/` cobre automaticamente todos os diretórios de usuários (`~/Documents`, `~/Downloads`, `~/Desktop`, `~/Projects`, `/Applications`, etc.) porque Os marcadores com escopo de segurança herdam automaticamente permissões descendentes para todos os subcaminhos filhos.

#### Etapa 3: conceder acesso a discos externos (`/Volumes`)

1. Clique em **"Conceder acesso a discos externos (/Volumes)"**. 
2. Quando o painel nativo exibir `/Volumes`, clique em **"Conceder acesso"**. 
3. O botão é atualizado para **"Acesso a discos externos concedido ✓"**. 
4. **O que isso permite**: Acesso irrestrito de leitura/gravação a unidades USB externas, unidades Thunderbolt, cartões SD, montagens de imagem de disco DMG e volumes SMB/NFS/AFP montados em rede.

#### Etapa 4: acesso seletivo pasta por pasta (alternativa)

Se preferir não conceder acesso root amplo ao ATBCmder, não é necessário clicar em acesso root: 

- Quando você navega em qualquer pasta não autorizada (como uma pasta externa ou repositório de projeto), o ATBCmder detecta o limite de permissão e exibe um prompt sob demanda: 
`ATBCmder requires your permission to access: /Users/username/SecretProject` 

- Clique em **"Conceder acesso à pasta"**, aprove a caixa de diálogo nativa e esse diretório específico será marcado permanentemente.

#### Etapa 5: Acesso total ao disco (FDA) para dados protegidos do sistema

> [!IMPORTANTE] 
> **Marcadores de sandbox versus acesso total ao disco (FDA)**: 
> 
> - **Marcadores de Sandbox** concedem acesso geral ao sistema de arquivos para pastas de usuário padrão, arquivos e unidades externas. 
> - **Acesso total ao disco (FDA)** é uma permissão de privacidade adicional de Transparência, Consentimento e Controle (TCC) do macOS necessária para inspecionar dados pessoais confidenciais do macOS (como histórico do Safari, anexos de e-mail, mensagens, backups do Time Machine e caches do sistema). 
> 
> Se você precisar gerenciar essas pastas protegidas: 
> 
> 1. Clique em **"Abrir configurações de acesso total ao disco…"** na caixa de diálogo de integração. 
> 2. O macOS abre **Configurações do sistema** → **Privacidade e segurança** → **Acesso total ao disco**. 
> 3. Clique no cadeado ou autentique com Touch ID/senha. 
> 4. Certifique-se de que a chave seletora ao lado de **ATBCmder** esteja ligada **ON**.

### Revogando e redefinindo permissões

Se você precisar redefinir ou revogar os favoritos do sandbox: 

1. Abra o diretório de configuração do ATBCmder através do menu **Configuração** → **Abrir diretório de configuração** (`cm_OpenConfigDirectory`). 
2. Exclua o arquivo `sandbox_bookmarks.plist`. 
3. Reinicie o ATBCmder. 
4. Para redefinir as permissões TCC no nível do sistema macOS, execute o seguinte comando no Terminal macOS: 
   ```bash
   tccutil reset SystemPolicyAllFiles com.aitobox.atbcmder
   ```
 

---

## 4. Configurações de idioma e personalização de aparência

ATBCmder está localizado para fluxos de trabalho globais e integra-se perfeitamente às preferências de aparência do macOS.

### Internacionalização e substituições de idioma

ATBCmder oferece suporte a **mais de 30 idiomas**, incluindo inglês, chinês simplificado (简体中文), chinês tradicional (繁體中文), alemão (Deutsch), francês (Français), espanhol (Español), russo (Русский), japonês (日本語), italiano, polonês, coreano e muito mais. 

![Language Settings](images/language_settings.png) 

- **Seguimento automático do idioma do sistema**: por padrão, o ATBCmder detecta a localidade do sistema macOS (`AppleLanguages`) na inicialização e aplica a tradução correspondente automaticamente. 
- **Seleção manual de idioma**: 
1. Abra Preferências pressionando `Cmd+,` ou executando `cm_Options`. 
2. No painel de navegação esquerdo, selecione **Idioma**. 
3. Escolha seu idioma preferido na lista suspensa. 
- **Live Reload (não é necessário reiniciar)**: Ao contrário da maioria dos utilitários Mac tradicionais que exigem encerrar e reiniciar o aplicativo, o ATBCmder retraduz dinamicamente toda a interface (menus, barras de ferramentas, caixas de diálogo, dicas de botões e mensagens de status) em tempo real no momento em que você seleciona um novo idioma.

### Aparência e Temas

ATBCmder oferece suporte total aos modos de aparência Claro e Escuro do macOS: 

- **Sincronização da aparência do sistema**: transita automaticamente entre os modos Claro e Escuro sempre que a aparência do sistema macOS muda (por exemplo, ao pôr do sol ou por meio do Centro de Controle). 
- **Opções de tema**: 
- **Fusion / macOS nativo**: estética clássica e limpa da área de trabalho que respeita as cores acentuadas do macOS e a vibração das janelas. 
- **Tema elegante**: estética moderna com controles segmentados arredondados, separadores de gradientes sutis e barras de guias em forma de pílula. 
- **Paleta de modo escuro**: usa superfícies de carvão escuro (`#2C2C2E` / `#242426`) com texto de alto contraste e ícones de pasta personalizados, reduzindo o cansaço visual em ambientes com pouca luz. 
- **Paleta de modo claro**: fundo branco nítido com divisórias cinza suaves (`#FAFBFD` / `#EEF2F7`) e bordas de contraste claras. 

---

## 5. ⚡ Dicas profissionais e configurações avançadas de layout

Aproveite ao máximo o mecanismo de layout flexível do ATBCmder para personalizar seu espaço de trabalho para configurações de gerenciamento de dados especializados, ultra-amplos ou de vários monitores.

### Dica 1: salvando a posição da janela e proporções de layout (`cm_ConfigSavePos`)

Ao organizar seu espaço de trabalho – personalizando as dimensões da janela, maximizando em um monitor externo ou definindo uma proporção específica do divisor intermediário – você pode bloquear essa configuração para que ela seja sempre restaurada de forma idêntica: 

1. Organize a janela principal do ATBCmder e ajuste o divisor do meio para sua proporção preferida. 
2. Selecione o menu **Configuração** → **Salvar posição e layout** ou execute o comando interno: 
   ```
   cm_ConfigSavePos
   ```
 

3. O tamanho da janela, as coordenadas da tela, o estado maximizado e as proporções do painel são gravados diretamente em `atbcmder.xml`. 
4. Em **Preferências** → **Layout**, certifique-se de que **"Salvar posição da janela ao sair"** esteja marcado para atualizações automáticas contínuas.

### Dica 2: Alternando o layout horizontal de painel duplo (`cm_HorizontalFilePanels`)

Embora os painéis verticais lado a lado sejam padrão para operações de arquivo, os painéis horizontais empilhados (Painel Superior e Painel Inferior) são excepcionalmente úteis quando: 

- Trabalhar com nomes de arquivos ultralongos que exigem largura de tela inteira. 
- Comparação de colunas amplas de metadados de arquivos (permissões, proprietários, somas de verificação, dimensões). 
- Trabalhando em monitores ou tablets verticais girados. 

Para mudar de layout: 

1. Selecione o menu **Mostrar** → **Painéis horizontais**, ou acione o comando interno: 
   ```
   cm_HorizontalFilePanels
   ```
 

2. Quando o modo horizontal está ativo: 
- Os painéis são empilhados verticalmente (Painel Superior e Painel Inferior). 
- A barra de ferramentas central gira automaticamente em uma faixa horizontal entre os painéis superior e inferior. 
- O cursor de arrastar se adapta a um ponteiro de divisão vertical (`SplitVCursor`), permitindo redimensionar a proporção de altura entre os painéis superior e inferior sem esforço.

### Dica 3: encaixe do divisor intermediário com um clique

- **Saldo 50/50 instantâneo**: Clique duas vezes em qualquer lugar na barra divisória do meio ou na linha separadora. Os painéis voltam imediatamente para uma divisão exata de 50%/50%. 
- **Predefinições de proporção**: No tema "Elegante", clicar nos botões segmentados do meio ajusta o layout para `50:50`, `70:30` (enfatizando o painel de origem) ou `30:70` (enfatizando o painel de destino).

### Dica 4: Restauração automática de sessão e persistência do espaço de trabalho

ATBCmder possui um subsistema inteligente de gerenciamento de sessões (`SessionManager`) que garante que seu ambiente de trabalho seja sempre preservado: 

- **Armazenamento XML da sessão**: o estado da sessão é persistido automaticamente em `atbcmder_session.xml` dentro do seu diretório de configuração (`~/Library/Application Support/ATBCmder/`). 
- **Memória de geometria de janela**: restaura as coordenadas exatas da janela (`x`, `y`), dimensões (`width`, `height`), estado maximizado e a proporção do divisor intermediário (`splitter_ratio`). 
- **Restauração da guia de painel duplo**: 
- Restaura todas as guias abertas nos painéis esquerdo e direito após a inicialização. 
- Lembra o índice da guia ativa em cada painel. 
- Carrega automaticamente o diretório de trabalho exato para cada guia, eliminando o atrito de navegar novamente manualmente para pastas profundas do projeto. 
- **Bloqueio de posição padrão**: Você também pode bloquear permanentemente a geometria da janela atual e a proporção do divisor como a configuração de inicialização padrão usando **Configuração ➔ Salvar posição** (`cm_ConfigSavePos`). 

---

## 6. Alertas de segurança e do sistema: configuração da tecla de função macOS (Fn)

Se você usou Total Commander, Double Commander ou Norton Commander em um teclado de PC, seus dedos são treinados para usar as teclas de função da linha superior (`F3` Exibir, `F4` Editar, `F5` Copiar, `F6` Mover, `F7` MkDir, `F8` Excluir). 

No entanto, os teclados Apple lidam com a linha de funções de maneira diferente quando prontos para uso. 

> [!AVISO] 
> ### 🍎 Conflito de hardware de chave de função do macOS 
> Em teclados Apple (teclados integrados do MacBook, Apple Magic Keyboard), as teclas da linha superior são padronizadas como **Recursos especiais de hardware do macOS** (Brilho da tela, Controle de missão, Spotlight, Ditado, Não perturbe, Controles de mídia e Volume de áudio). 
> 
> Se você pressionar `F5` em um MacBook sem configuração, o macOS tentará ajustar a iluminação do teclado ou acionar o Ditado em vez de copiar seus arquivos!

### Opção A: mantenha pressionada a tecla `Fn` (Globo 🌐) (configuração padrão do macOS)

Se você preferir manter intactas as chaves de mídia padrão da Apple: 

- Mantenha pressionada a tecla **`Fn`** (ou Globo 🌐) enquanto pressiona qualquer tecla de função: 
- `Fn+F3`: Lista Universal 
- `Fn+F4`: Editor Interno 
- `Fn+F5`: Copiar arquivos 
- `Fn+F6`: Mover arquivos 
- `Fn+F7`: Criar pasta 
- `Fn+F8`: Excluir para a Lixeira

### Opção B: ativar teclas de função padrão em todo o sistema (recomendado)

Se você deseja reflexos de comandante de tecla única autênticos e de alta velocidade sem segurar o modificador `Fn`: 

1. Abra **Configurações do sistema** no menu Apple (). 
2. Clique em **Teclado** na barra lateral. 
3. Clique no botão **Atalhos de teclado…**. 
4. Na lista de navegação à esquerda, selecione **Teclas de função**. 
5. Ative a alternância: **"Use as teclas F1, F2, etc. como teclas de função padrão"**. 

```
┌─────────────────────────────────────────────────────────────┐
│  Keyboard Shortcuts                                         │
├──────────────────┬──────────────────────────────────────────┤
│  Launchpad & Dock│  Use F1, F2, etc. keys as standard       │
│  Display         │  function keys                           │
│  Mission Control │                                          │
│  Keyboard        │  [ ON ───● ]                             │
│  Input Sources   │                                          │
│  Screenshots     │  When this option is selected, press the │
│ ▸ Function Keys  │  Fn key to use the special features      │
│  App Shortcuts   │  printed on each key.                    │
└──────────────────┴──────────────────────────────────────────┘
```
 

Uma vez ativado: 

- Pressionar `F1`–`F12` aciona diretamente os comandos ATBCmder imediatamente. 
- Para usar os controles de brilho ou volume, basta segurar `Fn` enquanto pressiona a tecla. 

---

## 7. Referência rápida de atalhos essenciais de matriz dupla

ATBCmder fornece suporte completo para teclado de matriz dupla: use atalhos nativos do macOS (`Cmd ⌘`), teclas clássicas do Commander (`Fn`) ou ambos de forma intercambiável.

| Ação Central | ID do comando | macOS nativo (`Cmd ⌘`) | Comandante Clássico (`Fn`) | Descrição | 
| :--- | :--- | :--- | :--- | :--- | 
| **Lista de favoritos do diretório** | `cm_DirHotList` | `Cmd+D` / `⌘D` | `Ctrl+D` / `⌃D` | Abre pop-up de favoritos de diretório com pesquisa difusa instantânea. | 
| **Lista de direção (esquerda/direita)** | `cm_LeftOpenDrives` / `cm_RightOpenDrives` | `⌥F1` / `⌥F2` (`⌥D`) | `Alt+F1` / `Alt+F2` (`Alt+D`) | Abre o menu de unidade e volume para o painel esquerdo ou direito (`Alt+D` para o painel ativo). | 
| **Copiar arquivos** | `cm_Copy` | `Cmd+C` ➔ `Cmd+V` | `F5` (ou `Fn+F5`) | Copia itens selecionados do painel ativo para o painel inativo. | 
| **Mover arquivos** | `cm_Move` | `Cmd+C` ➔ `Opt+Cmd+V` | `F6` (ou `Fn+F6`) | Move os itens selecionados do painel ativo para o painel inativo. | 
| **Ver no Lister** | `cm_View` | `Space` / `Cmd+Y` | `F3` (ou `Fn+F3`) | Abre arquivo no Universal Lister (código, hexadecimal, imagem, pdf, áudio). | 
| **Visualização rápida** | `cm_QuickView` | `Cmd+Q` / `Ctrl+Q` | `Ctrl+Q` | Exibe visualização instantânea ao vivo no painel oposto. | 
| **Editar arquivo** | `cm_Edit` | `Cmd+E` | `F4` (ou `Fn+F4`) | Abre o arquivo no editor de código/texto integrado. | 
| **Novo diretório** | `cm_MkDir` | `Shift+Cmd+N` | `F7` (ou `Fn+F7`) | Cria uma nova pasta no painel ativo. | 
| **Excluir para a Lixeira** | `cm_Delete` | `Cmd+Backspace` | `F8` (ou `Fn+F8`) | Move com segurança os arquivos selecionados para a Lixeira do macOS. | 
| **Renomeação embutida** | `cm_Rename` | `Return` | `F2` / `Shift+F6` | Renomeia o arquivo destacado no local. | 
| **Painel de interruptores** | `cm_FocusSwap` | `Tab` | `Tab` | Muda o foco do teclado para o painel oposto (`cm_SwitchPanel`). | 
| **Trocar Esquerda/Direita** | `cm_Exchange` | `Ctrl+U` | `Ctrl+U` | Troca caminhos de diretório entre os painéis esquerdo e direito. | 
| **Nova guia** | `cm_NewTab` | `Cmd+T` | `Ctrl+T` | Abre uma nova guia de pasta no painel atual. | 
| **Fechar guia** | `cm_CloseTab` | `Cmd+W` | `Ctrl+W` | Fecha a guia ativa. | 
| **Modo Horizontal** | `cm_HorizontalFilePanels` | Menu: Mostrar ➔ Horizontal | Menu: Mostrar ➔ Horizontal | Alterna o layout empilhado lado a lado e empilhado superior e inferior. | 
| **Salvar layout** | `cm_ConfigSavePos` | Menu: Configuração ➔ Salvar Pos | Menu: Configuração ➔ Salvar Pos | Salva as dimensões atuais da janela e as proporções do painel. | 
| **Acesso à área restrita** | `cm_GrantFilesystemAccess` | Menu: Arquivo ➔ Permissões | Menu: Arquivo ➔ Permissões | Inicia o assistente de integração do macOS App Sandbox. | 
| **Preferências** | `cm_Options` | `Cmd+,` | `Alt+O` | Abre a caixa de diálogo de configuração do ATBCmder. |

---

## Próximas etapas

Agora que você domina a base do painel duplo e configurou seu ambiente macOS, vá para **[Capítulo 2: Navegação e guias de pastas](navigation_and_tabs.md)** para aprender como navegar em árvores de diretório com velocidade, dominar espaços de trabalho com várias guias, salvar conjuntos de diretórios favoritos, usar listas de acesso instantâneas e aproveitar visualizações recursivas de ramificação plana.