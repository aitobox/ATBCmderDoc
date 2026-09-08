# Capítulo 10: Download e instalação

Obrigado pelo seu interesse no ATBCmder! Fornecemos dois métodos diferentes de download e instalação para atender às suas necessidades. 

> [!IMPORTANT] 
> **Requisitos de sistema e arquitetura** 
> 
> - **Sistema operacional**: macOS 12.0 (Monterey) ou posterior (incluindo macOS 13 Ventura, macOS 14 Sonoma e macOS 15 Sequoia). 
> - **Arquitetura de hardware suportada**: **Apple Silicon (M1/M2/M3/M4, ARM64)**. 
> - **Compatibilidade com Intel (x86_64)**: Macs baseados em Intel **não são suportados** no momento.

## 1. Mac App Store (recomendado)

Esta é a forma recomendada de instalar o ATBCmder. **ATBCmder agora está oficialmente disponível na Mac App Store!** O download através da Mac App Store oficial garante que você obtenha atualizações automáticas perfeitas, proteção nativa de sandbox do macOS e a melhor integração de sistema. 

- **Mac App Store**: [Baixe ATBCmder na Mac App Store](https://apps.apple.com/app/atbcmder/id6792398333)

## 2. Download do instalador DMG

Se você não conseguir acessar a Mac App Store ou preferir downloads diretos, fornecemos um pacote de instalação DMG independente desenvolvido nativamente para Apple Silicon (ARM64). 

- **Link para download do DMG**: [Clique aqui para baixar o ATBCmder DMG](https://storage.aitobox.com/@s/bNAshV6G/ATBCmder) *(somente Apple Silicon / ARM64)* 

*Observação: ao instalar via DMG, os recursos de segurança do macOS podem exigir que você permita explicitamente o aplicativo em "Configurações do sistema > Privacidade e segurança" na primeira vez que você o abrir. Macs Intel (x86_64) não são suportados.*

### ⚠️ Conceda acesso total ao disco

ATBCmder é uma ferramenta de gerenciamento de arquivos e requer permissões explícitas de gerenciamento de disco do usuário. Siga estas etapas: 

1. Clique no ícone da Apple no canto superior esquerdo da tela e selecione **Configurações do Sistema** (ou "Preferências do Sistema" em versões mais antigas do macOS). 
2. Navegue até **Privacidade e segurança** no menu esquerdo ou direito. 
3. Role para baixo e selecione **Acesso total ao disco**. 
4. Encontre o aplicativo (**ATBCmder**) na lista e alterne o botão para ativá-lo. Se o aplicativo não estiver na lista, clique no botão **+** na parte inferior para adicioná-lo manualmente. 
5. O sistema solicitará que você insira sua senha de login do Mac ou use o Touch ID para confirmar as alterações.

## Notas de versão

### 1.7.0 (06/09/2026)

- Universal File Viewer e Office Preview Suite: Adicionados mecanismos de visualização nativos para planilhas do Excel (com carregamento virtual lento), documentos do Word (com paginação e renderização de imagem incorporada) e apresentações do PowerPoint (visualização de cartão de slide); visualizações adicionadas para bancos de dados SQLite, Markdown (com TOC), Jupyter Notebooks, fontes, arquivos, áudio e EML; implementou rolagem infinita de streaming instantâneo para arquivos de texto grandes 
- Visualizador de comparação de arquivos lado a lado: ferramenta integrada de comparação bidirecional no estilo vimdiff com destaque de comparação em nível de caractere, cópia de pedaços, edição ao vivo, desfazer/refazer e preservação de codificação 
- Mecanismo avançado de pesquisa de arquivos: subsistema de pesquisa reescrito com correspondência de substring difusa padrão, suporte a regex e um modo de guia "Feed to Listbox"; a otimização da interface do usuário em lote elimina congelamentos da interface do usuário em resultados de pesquisa massivos 
- Operações de arquivo e fortalecimento da interface do usuário: foram corrigidos prompts de substituição duplicados durante movimentações entre dispositivos e bloqueios de fila de transferência; adicionados carimbos de data e hora de criação de arquivo na caixa de diálogo de propriedades; barra de ferramentas central vertical habilitada por padrão e indicadores visuais do painel ativo refinados

### 1.6.2 (03/09/2026)

- Seleção e interação de arrastar com elástico: Adicionada seleção de arrastar com elástico do mouse na visualização de tabela de arquivos e na visualização de miniaturas, além de clicar no espaço vazio para desmarcar tudo 
- Tecla de atalho e tecla de atalho global da janela: Adicionada uma tecla de atalho global configurável para mostrar/ocultar a janela do aplicativo; entrada fixa de combinações de modificadores de 4 teclas nas configurações de teclas de atalho 
- Correção de restauração do Dock e da bandeja do macOS: resolvido um problema em que clicar no ícone do Dock enquanto minimizado na bandeja poderia falhar ao restaurar a janela principal ou mostrar um quadro em branco 
- Melhorias no fortalecimento e estabilidade do núcleo: possíveis falhas de ciclo de vida corrigidas, back-ends VFS fortalecidos e desmontagem de thread estabilizada e suítes de teste

### 1.6.1 (27/08/2026)

- Revisão abrangente da interface do usuário/UX do macOS: baseado no Apple HIG com paletas claras/escuras refinadas, contraste de realce do painel estilo Finder, dicas de ferramentas de cartão nativas e animações de controle segmentadas suaves 
- Mecanismo de ícones vetoriais e widgets modernos: adicionado um gerador de ícones vetoriais independente de resolução inspirado em símbolos SF e barras de unidade, trilhas de navegação e caixas de combinação modernizadas 
- Interação e polimento de layout: renomeação múltipla redesenhada com layout de 2 colunas e detecção de colisão de nomes em tempo real; A visualização em miniatura suporta zoom dinâmico `Cmd + Wheel`; visualizações unificadas de estado vazio adicionadas

### 1.6.0 (27/08/2026)

- Pipeline de distribuição dupla: fluxos de trabalho de construção automatizados separados e adaptados para distribuição independente de DMG e lançamento na Mac App Store (MAS) 
- Conformidade com a política da App Store: ajusta dinamicamente os menus da interface do usuário em compilações MAS, removendo itens de verificação de atualização externa para atender estritamente às diretrizes de revisão da Apple, preservando as verificações manuais de atualização em compilações DMG 
- `itms-services` Binary Patcher: Adicionado um scanner binário automatizado e um patcher seguro para eliminar strings de protocolo privado em artefatos PySide6/Qt compilados, garantindo uma validação automatizada perfeita do App Store Connect

### 1.5.6 (22/08/2026)

- Modos de visualização independentes por guia: cada guia agora mantém seu próprio layout de visualização independente (modo de visualização plana/árvore), sincronizando automaticamente o estado do menu e persistindo perfeitamente nas restaurações da sessão 
- Abertura inteligente de arquivos e fallback do sistema: adicionado um detector de tipo de arquivo multicamadas (bytes mágicos / MIME / extensão) para abrir mídia e documentos suportados no visualizador / editor integrado, ao mesmo tempo em que retorna de forma limpa aos aplicativos padrão do sistema operacional para arquivos não suportados

### 1.5.5 (21/08/2026)

- Otimização da política de verificação de atualização: verificações automáticas de atualização desativadas na inicialização do aplicativo por padrão; as atualizações agora podem ser verificadas manualmente via `Help` -> `Check for Updates...`, melhorando a velocidade de inicialização e a privacidade offline

### 1.5.4 (21/08/2026)

- Foco do painel e polimento de seleção: Corrigidos contornos de foco persistentes em painéis divididos inativos ao alternar entre painéis; lógica de redefinição de seleção aprimorada após mover arquivos entre painéis para evitar operações acidentais

### 1.5.3 (19/08/2026)

- Breadcrumb Cascading Submenu Polish: Alinha com precisão a posição vertical dos menus de subpastas em cascata com a linha destacada, eliminando saltos de layout e suavizando a travessia profunda de pastas

### 1.5.2 (19/08/2026)

- Correção de notas de inicialização e versão: corrigido um problema em que a caixa de diálogo Notas de versão aparecia repetidamente em cada inicialização do aplicativo; tratamento de fallback padrão `Config.get` aprimorado para garantir que as notas de lançamento sejam solicitadas apenas no lançamento inicial ou atualizações de versão

### 1.5.1 (19/08/2026)

- Notas de versão multilíngues: Adicionadas 7 novas notas de versão em idiomas convencionais (zh_TW, ja, ko, de, fr, ru, es) com descoberta dinâmica e fallback hierárquico de 5 camadas 
- macOS Code Signing & Build Polish: scripts de empacotamento refatorados com direcionamento binário Mach-O e wrappers de repetição de carimbo de data/hora, eliminando falhas de assinatura e limitação

### 1.5.0 (17/08/2026)

- Gerenciador de sessão global: implementação de persistência de sessão em nível de aplicativo que restaura perfeitamente todas as guias, caminhos, modos de visualização (plano/árvore) do painel esquerdo/direito, proporções do painel e limites de janela de vários monitores após a reinicialização 
- Importação/exportação de configurações: Adicionada exportação e importação ZIP com 1 clique para todas as configurações e dados do aplicativo, simplificando a migração entre dispositivos 
- Melhorias no Editor de Imagens: Adicionado redimensionamento de imagem personalizado com bloqueio de proporção e resoluções predefinidas rápidas

### 1.4.9 (17/08/2026)

- Editor de imagem avançado: adicionado corte de imagem, rotação fina, ajustes de filtro e um módulo de remoção e pintura interna de marca d'água de IA com tecnologia OpenCV 
- Visualizador de imagens aprimorado: suporte completo para GIFs animados, zoom, panorâmica, rotação, extração de metadados EXIF e modo de apresentação de slides 
- Integração de pesquisa com Spotlight: Spotlight nativo do macOS profundamente integrado para pesquisa instantânea de arquivos e navegação aprimorada com foco nos resultados da pesquisa

### 1.4.8 (16/08/2026)

- Localização abrangente (i18n): auditoria completa e conclusão da tradução na UI, no visualizador F3 e no editor F4, melhorando significativamente a localização de reprodutores de mídia e componentes de visualização 
- Otimizações do visualizador F3: Melhor manipulação de links externos e lógica envolvente de pesquisa no leitor EPUB substituto (SimpleEpubPanel); simplificou a barra de ferramentas do visualizador de PDF removendo botões de rotação redundantes

### 1.4.7 (16/08/2026)

- Melhorias no Media Player: UI, UX e estabilidade significativamente melhoradas dos players de áudio e vídeo integrados 
- Refatoração do sistema de compilação: renomeado sinalizador env `BUILD_EPUB` para `BUILD_WEBENGINE` para refletir com precisão o comportamento do pacote 
- Correção de dependências de empacotamento: garantido que `ebooklib` seja sempre empacotado em compilações DMG leves para o leitor EPUB substituto

### 1.4.6 (16/08/2026)

- Leitor EPUB leve (SimpleEpubPanel): Adicionado um leitor EPUB substituto sem WebEngine com navegação e pesquisa de capítulos, além de um argumento CLI `--epub-reader` para substituir o mecanismo padrão 
- Menus de localização atual em cascata: refatoração do menu suspenso de localização atual em um layout rolável de coluna única com submenus em cascata infinitos, corrigindo problemas de sobreposição e travamento do mouse

### 1.4.5 (15/08/2026)

- Advanced Code Viewer (F3): Adicionado destaque de sintaxe (Pygments), rastreamento de arquivo ao vivo, pesquisa de regex e números de linha 
- Editor de código avançado (F4): Adicionada codificação dinâmica/conversão EOL, economia atômica segura, recuo inteligente e localização/substituição 
- Arrastar e soltar externo global: arraste arquivos perfeitamente, incluindo conteúdos de arquivo profundamente aninhados, diretamente para o desktop macOS ou editores de terceiros (por exemplo, VSCode)

### 1.4.4 (15/08/2026)

- Melhorias de tipografia: tamanhos de fonte aumentados em menus, botões, dicas de ferramentas e caixas de diálogo de configurações para melhor legibilidade 
- Correções de redimensionamento de cursores: cursores de redimensionamento de mouse ausentes restaurados nas bordas das janelas, divisores e cabeçalhos de colunas de tabelas 
- Correções de UI do macOS: fundos de seleção pretos resolvidos em menus suspensos e overflows de títulos corrigidos em caixas de grupo

### 1.4.3 (14/08/2026)

- Nova UI nativa do macOS (tema Aqua Blue): introduzida como o novo tema padrão, com navegação de navegação interativa (com detalhamento de subpastas em cascata), medidor de armazenamento estilo Mac (excesso de TB fixo) e seleção de cápsula arredondada 
- Deep UI Polish: layout refinado do botão de fechamento da guia, sobreposição fixa de prompt de comando e fundos de barra de ferramentas unificados, divisórias e bordas de painel em todos os temas 
- i18n e atualização de aplicativos: auditoria completa de cobertura do projeto i18n concluída; adicionado suporte à API de compartilhamento AList/OpenList no módulo de atualização automática

### 1.4.2 (13/08/2026)

- Filtro semântico AI aprimorado: suporte para análise de extensões mais comuns, formas plurais e totalmente integrado ao i18n 
- UX de pesquisa semântica: substituiu o cursor de espera por QProgressBar e melhorou o comportamento da tecla Enter para conclusões 
- Análise semântica central: detecção aprimorada de tipo de alvo e remoção de palavras-chave para pesquisa em linguagem natural mais precisa

### 1.4.1 (13/08/2026)

- Revisão e refatoração abrangente da base de código (Lotes A-D) 
- Aprimoramentos de segurança: Corrigidas possíveis vulnerabilidades de passagem e acesso de caminho 
- Simultaneidade e desempenho: Melhor segurança do thread em segundo plano e eficiência de execução 
- Arquitetura: Estabilidade aprimorada e gerenciamento de recursos em componentes principais

### 1.4.0 (12/08/2026)

- Correções profundas de rede VFS: suporte a múltiplas codificações, drivers de protocolo, montagem de arquivos encadeados e resolução de conflitos 
- Módulo aprimorado de atualização de aplicativos: correções de verificação SSL, validação de download DMG e integração de UI 
- UI da nota de lançamento: exibe o histórico completo da versão durante atualizações automáticas

### 1.3.9 (12/08/2026)

- Adicionado leitor EPUB integrado (visualização rápida F3) 
- Implementado mecanismo de detecção de atualização de aplicativo 
- Corrigido o congelamento do trabalhador VFS durante a resolução de conflitos de arquivo

### 1.3.8 (08/08/2026)

- Refinamento da UI do Tree View 
- Integração de rede fsspec refatorada 
- Melhor tratamento de caracteres de arquivo inválidos

### 1.3.7 (06/08/2026)

- Arquitetura VFS de rede: revisão de sistemas de arquivos de rede (FTP/WebDAV/SMB) usando `fsspec`, implementando `VfsTableModel` assíncrono, streaming `StreamCopyWorker`, operações remotas de arquivos (mkdir/renomear/excluir/sobrescrever) e visualização/edição remota F3/F4 
- Bandeja do sistema e teclas de atalho: suporte para minimização na bandeja do sistema, atalho global (`Option+Cmd+H`), alternância de ícone do macOS Dock e integração de ícone de modelo nativo 
- Configuração LLM: introdução do recurso `default_llm.xml` e singleton para filtragem semântica de IA e interface de opções 
- Aprimoramentos de navegação: suporte a atalhos de navegação PageUp / PageDown / Home / End / Fn em painéis de arquivos e pop-ups de lista de procurados 
- Internacionalização: envolva todas as mensagens de erro VFS, rótulos do painel Quick View e sequências de menu da bandeja com catálogos de tradução i18n

### 1.3.6 (04/08/2026)

- Aprimoramentos de VFS de rede: adição de detecção automática UTF-8/GBK, atualização dinâmica de codificação makefile, tratamento de fallback e redefinição de soquete para FTP; resolver tempo limite e dessincronização de resposta 
- Correções de WebDAV e SMB: correção de remoção de caminho raiz de WebDAV/SMB, propagação de last_error, confiabilidade de conexão, ícones VFS e exibições de títulos de guias 
- Navegação em miniatura: implemente uma navegação suave por setas em grade 2D para visualização em miniatura 
- i18n e qualidade de código: corrige traduções corrompidas de Close Tab em catálogos zh_CN/zh_TW e completa auditoria de otimização de base de código

### 1.3.5 (03/08/2026)

- Painel de visualização rápida: implemente o recurso Quick View (`cm_QuickView`, `Cmd+Q`/`Ctrl+Q`) com suporte para visualizações de vários formatos, propriedades de arquivo substituto, inversão simétrica, integração de menu Mostrar e i18n completo 
- Widgets de visualização rápida: adicione `QuickViewContainer` e `QuickViewPropertiesWidget` integrados ao FilePanel 
- UI Polish: corrige o alinhamento do cabeçalho da guia e problemas de esmagamento da página de diálogo de opções no tema claro

### 1.3.4 (02/08/2026)

- UI do painel de arquivos: adicione seleção de lote Shift+PageUp / Shift+PageDown nas visualizações do painel de arquivos 
- Operações de arquivo: corrija defeitos de cópia F5 e movimentação de arquivo/diretório F6 
- Construir scripts: defina nomes exatos de identidade de certificado, adicione carimbo de data/hora ao codesign e lide com status inválido de reconhecimento de firma normalmente

### 1.3.3 (01/08/2026)

- Transfer Engine: calcule a velocidade de transferência precisa em tempo real e o ETA no ProcessTransferWorker 
- Permissões e sandbox: verificações separadas do sandbox do macOS do fluxo de detecção de acesso total ao disco 
- Scripts de compilação: atualize a configuração do script de compilação para compilações assinadas pelo DMG 1.3.3

### 1.3.2 (01/08/2026)

- Trabalhador de transferência de subprocesso: corrige falha de congelamento/inicialização no modo de pacote autônomo da App Store do Nuitka 
- Habilidades do agente: adicionar verificação de auditoria de integridade i18n à habilidade de revisão de código-otimização-auditoria

### 1.3.1 (01/08/2026)

- macOS Sandbox: corrige o falso estado de 'Acesso total ao disco concedido' causado pela verificação `os.access` 
- Tarefas simultâneas: resolva interferências de estado para operações simultâneas em segundo plano 
- i18n: adicionar tradução chinesa para caixa de seleção em lote na caixa de diálogo de exclusão permanente 
- Habilidades do agente: adicionar e atualizar habilidade de auditoria de otimização de revisão de código

### 1.3.0 (01/08/2026)

- Mecanismo de transferência isolado de processo: implemente ProcessTransferWorker e ProcessIOEngine para descarregar E/S de cópia/mover arquivo do thread de UI 
Desempenho e capacidade de resposta de transferência: limitação de taxa IPC de 10 Hz, buffer adaptativo e otimização macOS `F_NOCACHE` para evitar travamentos da GUI 

- Auditoria e fortalecimento de código: refatoração em 4 fases, incluindo bloqueios mutex de simultaneidade, fortalecimento de segurança e limpezas de arquitetura 
- Correções de interface do usuário: correção de erro de exclusão do Shiboken C++, layout do modo de painel horizontal e sinais indicadores de progresso de tarefas em segundo plano

### 1.2.0 (30/07/2026)

- Implementar um pool de processos de E/S global (IoWorkerPool) para isolar o bloqueio de operações de E/S de arquivos e evitar congelamentos de GUI 
- Controle de versão de configuração: leitura/gravação de app_version no nó raiz XML e adição de registro de executor de migração automatizado 
- Arrastar e soltar / área de transferência: integre ponte nativa do macOS Finder, pastas com mola e máquina de estado da área de transferência 
- Expansão do caminho: adicione o utilitário `expand_path` compartilhado com suporte a `~`, `$VAR`, `%VAR%` e `%COMMANDER_PATH%` 
- Hotlist: implementar singleton HotlistConfig independente e configuração de hotlist padrão

### 1.1.0 (29/07/2026)

- Corrigida a ordem de entrada das notas de lançamento para garantir a classificação cronológica reversa abaixo do cabeçalho da nota de lançamento 
- Correção do script do gerenciador de versão para suportar o nó XML System/LastVersion em default_config.xml 
- Teclas de atalho: adicione atalhos padrão Meta+Tab e Meta+Shift+Tab para navegação por guias 
- Guias favoritas: adicione migração automática e limpeza para guias favoritas herdadas da configuração principal 
- Visualizador de arquivos: otimize o desempenho de carregamento de arquivos grandes e o uso de memória

### 1.0.1 (22/07/2026)

> Corrigir falha de visualização de texto F3 em ambientes sandbox da App Store

### 1.0.0 (18/07/2026)

> Implementação inicial da porta Python do TotalCommander.