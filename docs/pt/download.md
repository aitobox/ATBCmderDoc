# Capítulo 11: Download e instalação

Obrigado pelo seu interesse no ATBCmder! Fornecemos dois métodos diferentes de download e instalação para atender às suas necessidades. 

> [!IMPORTANT] 
> **Requisitos de sistema e arquitetura** 
> 
> - **Sistema operacional**: macOS 12.0 (Monterey) ou posterior (incluindo macOS 13 Ventura, macOS 14 Sonoma e macOS 15 Sequoia). 
> - **Arquitetura de hardware suportada**: **Universal (Apple Silicon ARM64 & Intel x86_64)**. Suporte completo para computadores Apple Silicon (M1 / M2 / M3 / M4) e Macs baseados em Intel.  
> - **Compatibilidade com Intel (x86_64)**: Totalmente compatível a partir da versão 1.8.0 por meio de pacotes binários universais.

## 1. Mac App Store (recomendado)

Esta é a forma recomendada de instalar o ATBCmder. **ATBCmder agora está oficialmente disponível na Mac App Store!** O download através da Mac App Store oficial garante que você obtenha atualizações automáticas perfeitas, proteção nativa de sandbox do macOS e a melhor integração de sistema. 

- **Mac App Store**: [Baixe ATBCmder na Mac App Store](https://apps.apple.com/app/atbcmder/id6792398333)

## 2. Download do instalador DMG

Se você não puder acessar a Mac App Store ou preferir downloads diretos, fornecemos pacotes de instalação DMG independentes criados nativamente para macOS com suporte de arquitetura dupla (Universal / ARM64 & Intel x86_64).

- **Link de download do DMG**: [Clique aqui para baixar o DMG do ATBCmder](https://storage.aitobox.com/@s/atbcenter/ATBCmder) *(Universal: Apple Silicon & Intel x86_64)*

*Observação: ao instalar via DMG, os recursos de segurança do macOS podem exigir que você permita explicitamente o aplicativo em "Configurações do sistema > Privacidade e segurança" na primeira vez que você o abrir.*

### ⚠️ Conceda acesso total ao disco

ATBCmder é uma ferramenta de gerenciamento de arquivos e requer permissões explícitas de gerenciamento de disco do usuário. Siga estas etapas: 

1. Clique no ícone da Apple no canto superior esquerdo da tela e selecione **Configurações do Sistema** (ou "Preferências do Sistema" em versões mais antigas do macOS). 
2. Navegue até **Privacidade e segurança** no menu esquerdo ou direito. 
3. Role para baixo e selecione **Acesso total ao disco**. 
4. Encontre o aplicativo (**ATBCmder**) na lista e alterne o botão para ativá-lo. Se o aplicativo não estiver na lista, clique no botão **+** na parte inferior para adicioná-lo manualmente. 
5. O sistema solicitará que você insira sua senha de login do Mac ou use o Touch ID para confirmar as alterações.

## Notas de versão

### 2.4.5 (31/10/2026)

- Solicitações inteligentes de autenticação de rede e retenção de credenciais de sessão na memória: Introduzida uma caixa de diálogo dedicada (`NetworkPasswordDialog`) com alternância de visibilidade da senha e opção de armazenamento nas Chaves do sistema; implementado um resolvedor de credenciais prévio (`resolve_or_prompt_network_credentials`) que intercepta com fluidez a navegação para conexões SFTP, FTP, SMB e WebDAV não memorizadas para solicitar credenciais com cancelamento seguro; corrigida a perda de senhas temporárias ao editar conexões no Gerenciador de conexões, retendo com segurança as credenciais em `VFSSessionCache` durante toda a sessão atual do aplicativo
- Ordenação de colunas em tabelas VFS de rede e sincronização bidirecional de indicadores no cabeçalho: Implementado o método `sort()` completo no `VfsTableModel` correspondendo às colunas do painel local (Nome, Extensão, Tamanho, Data de modificação, Atributos) mantendo os diretórios sempre no topo; ativado o clique nas seções do cabeçalho em `DividerHeaderView` (`sectionsClickable`) e sincronizados os indicadores de ordenação bidirecionalmente com o menu principal e comandos de atalho
- Auditoria abrangente do VFS de rede, tratamento robusto de erros e configurações avançadas: Eliminada a recursão mútua entre `VFSSessionCache.disconnect` e `VFSManager.remove_from_cache` durante desconexões reentrantes; aprimorados os uploads em streaming no WebDAV com `Content-Length` explícito, fechamento seguro de respostas e limpeza proativa de arquivos parciais em cancelamentos; reforçadas as verificações de status e contextos de erro em workers de download, upload, exclusão e montagem Samba; opções avançadas padronizadas (verificação SSL/TLS, modo passivo PASV) com catálogos atualizados em 31 idiomas

### 2.4.4 (31/10/2026)

- Blindagem do ciclo de vida de QThread e prevenção de falhas por Coletor de Lixo: Implementadas proteções universais de ciclo de vida para `QThread` baseadas na ressurreição de objetos (PEP 442), eliminando completamente falhas críticas `SIGABRT` («QThread: Destroyed while thread is still running») causadas pela coleta de lixo prematura de threads ativas em segundo plano (varredura de pastas, verificação de caminhos, transferência de arquivos); aprimoradas rotinas de encerramento em `FileSystemModel` e carregadores com `safe_qthread_cleanup`
- Teclas de atalho globais via Carbon sem permissões e normalização da tecla Option: Reformulação do tratamento de atalhos globais no macOS migrando para a API nativa Carbon `RegisterEventHotKey`, permitindo a ativação imediata de atalhos globais sem exigir permissões de Acessibilidade nos Ajustes do Sistema do macOS; normalizados os mapeamentos da tecla Option (⌥) para eliminar conflitos com teclas mortas e caracteres acentuados, com captura em tempo real e detecção de conflitos nas Preferências
- Ícone do aplicativo em alta resolução no Dock do macOS em pacotes distribuídos: Correção de problema em que o ícone do aplicativo no Dock do macOS aparecia borrado devido à redução de resolução do Qt; injeção nativa de recursos de ícone em alta resolução via `NSApplication.setApplicationIconImage_` do AppKit, garantindo perfeita nitidez visual
- Restauração de compatibilidade com macOS 12 (Monterey) e ajuste fino de dependências: Ajustados os limites de dependência do PySide6 para restaurar e garantir a retrocompatibilidade com o macOS 12 (Monterey), oferecendo máxima estabilidade em versões modernas e anteriores do macOS

### 2.4.3 (30/10/2026)

- Ferramenta avançada para busca de alterações recentes em arquivos e pastas: Nova ferramenta de sistema integrada «Alterações Recentes» baseada em comandos nativos da bridge, oferecendo filtros de tempo flexíveis (1 hora, 24 horas, 7 dias, 30 dias) e filtros de tamanho mínimo (>1 MB, >10 MB, >100 MB, >1 GB); aproveita os metadados do macOS Spotlight para acelerar varreduras profundas; os resultados contam com filtragem instantânea, navegação por clique duplo para o Finder ou painel e envio em lote para a Lixeira
- Renomeação automática segura em conflitos de colagem e confiabilidade em nuvem: Adiciona automaticamente um sufixo numérico incremental (ex.: `nome (1).ext`) ao colar arquivos ou pastas com nomes conflitantes, evitando sobrescritas acidentais (Fixes #92); restaurada a descoberta de dados no Google Drive em sistemas de arquivos virtuais (Fixes #87, #91); inclusão completa das dependências essenciais do Dropbox nas compilações do macOS (Fixes #90)
- Auditoria abrangente em 31 idiomas e padronização de terminologia: Revisão minuciosa e refinamento das traduções em todos os 31 idiomas suportados, corrigindo problemas de quebra de linha com escape em arquivos PO e eliminando imprecisões de tradução automática (Fixes #88, #93); padronizada a terminologia profissional do gerenciador de arquivos e recompilados os catálogos binários `.mo`
- Polimento da experiência nativa do macOS e refinamento visual: Botões de diálogos de confirmação padronizados de acordo com as convenções do macOS («Sim/Confirmar» antes de «Não/Cancelar»); remoção de linhas divisórias supérfluas nas abas de caminho para um design em cápsula mais limpo; corrigido o desfoque do ícone no Dock do macOS causado pela redução de resolução do Qt, melhorado o contraste dos divisores de cabeçalho e corrigida condição de corrida no encerramento da verificação de caminhos

### 2.4.2 (26/10/2026)

- Reformulação da limpeza do sistema e limpeza por aplicativo: Adicionados modos duplos de agrupamento (por aplicativo ou por categoria) para inspecionar e limpar caches e logs por aplicativo (Fixes #85); cálculo preciso do tamanho dos grupos excluindo entradas desconhecidas, verificações prévias de permissão e indicadores de status em tempo real (0 B limpos, dicas de falha); adicionados botões na barra de ferramentas «Revelar no Finder» e «Abrir no ATBCmder» com suporte a clique duplo; geometria da janela alinhada com o Analisador de Espaço em Disco
- Reforço da ponte privilegiada atbsys e contabilidade de armazenamento: Sincronizada a verificação de segurança Mole para planos de limpeza e desinstalação (Fixes #80), garantindo que a execução corresponda estritamente aos planos confirmados, proteja dados pessoais/compartilhados e respeite locais graváveis no Sandbox da App Store; reforçada a contabilidade do sistema de arquivos para hard links, rastreamento de clones APFS, amostragem de CPU e tempos limites de comandos
- Pipeline de empacotamento macOS e fortalecimento multiarquitetura: Alinhamento de metadados de versão e compilação entre módulos; toolchains de Go e Qt fixadas com compatibilidade para macOS 12+; correção na verificação de fatias Mach-O em hosts x86_64 passando `-arch all` para otool; proteção da análise de plist de codesign contra bytes de preenchimento e interrupção estrita da compilação em falhas de empacotamento ou assinatura
- Interação do painel, ícones contextuais e polimento da localização: Correção do problema em que excluir arquivos ou atualizar fazia o painel retornar ao topo da lista (Fixes #81, #82), deslocando suavemente o foco para as linhas adjacentes e mantendo a posição da rolagem; configurados ícones vetoriais semânticos para todas as ações do menu de contexto (Fixes #83, #84); polimento do status das células do visualizador CSV e da tradução de termos em todos os 31 idiomas suportados

### 2.4.1 (24/10/2026)

- Reformulação da interação com cabeçalhos e divisores de coluna estilo Finder: Introduzida uma `DividerHeaderView` dedicada para cabeçalhos de tabela de arquivos, desenhando divisores verticais sutis e centralizados entre as colunas para separação visual nítida sem bordas grossas; reprojetado `HeaderResizeCursorController` com uma zona de tolerância de 8px e separação clara entre ordenação e redimensionamento de colunas, eliminando tremulação do cursor e conflitos de arrasto
- Antioscilação de tema no diálogo de opções e otimização de desempenho: Refinamento do comportamento de cancelamento no diálogo de opções para que a reversão global do tema seja invocada apenas se o tema ativo tiver sido realmente alterado durante a pré-visualização; eliminação da recompilação desnecessária de folhas de estilo e renderização de widgets ao fechar as preferências sem mudanças de tema, removendo travamentos ao fechar modais
- Ícones de aplicativo em alta resolução e correção na pipeline de empacotamento macOS: Atualização de recursos oficiais do logotipo em maior resolução; correção de falha nos scripts de compilação macOS DMG/PKG e Nuitka em que `AppIcon.icns` era inadvertidamente removido durante a limpeza de ativos; detecção de ícones expandida para localizar diretamente do caminho padrão `.app/Contents/Resources/AppIcon.icns`, garantindo renderização nítida no Dock e no Finder

### 2.4.0 (23/10/2026)

- Reformulação das abas do painel de arquivos com design nativo em cartões/cápsulas para macOS: Barras de abas de caminho completamente reprojetadas em cápsulas de cartão arredondadas com fundo rebaixado e divisores finos, corrigindo bordas irregulares e cortes; estabelecida a hierarquia de foco ativo/inativo (indicador azul vibrante para o painel ativo, cinza neutro para o inativo); introduzidos ícones vetoriais semânticos (cadeados trancados, Início, Raiz, resultados de busca); altura padronizada em 28px alinhada com precisão de pixel aos seletores de unidades (Fixes #78, #79)
- Detecção automática inteligente de codificação no Visualizador e no Editor: Desenvolvido mecanismo dedicado de detecção de codificação (`encoding_utils`) combinando inspeção de BOM, análise chardet e heurísticas de codepages comuns; resolução completa de caracteres corrompidos ao abrir arquivos GBK, GB18030, Big5, Shift-JIS e EUC-KR no Visualizador universal (F3) e Editor (F4)
- Arquitetura leve e redução drástica no tamanho do pacote: Remoção completa da dependência pesada `opencv-python-headless` (economizando mais de 70 MB), reimplementando o processamento de imagens e remoção de marcas d'água com Pillow e Apple CoreImage; eliminação de bibliotecas de transcodificação não utilizadas (libtesseract, libx265), reduzindo sensivelmente o instalador DMG/PKG e o consumo de memória em tempo de execução
- Auditoria de segurança do núcleo e robustez geral de estabilidade: Eliminado o risco de truncamento do arquivo de origem ao copiar para arquivos físicos idênticos entre caminhos ou camadas VFS; preservação segura de links simbólicos no editor de texto, permissões de somente leitura e sincronização de substituição multibyte/Emoji; reforço do escape de caminhos para comandos `cd`, resolução de conflitos na renomeação múltipla, cancelamento imediato de cálculos de checksum, extração 7z e correções de falhas de alinhamento em scanlines de imagens

### 2.3.9 (22/10/2026)

- Refinamento do tema padrão e arquitetura de interface moderna: Introdução de tokens semânticos de aparência e regras de contraste com adaptação perfeita aos modos claro e escuro; restauração de ícones coloridos, detalhes clássicos em azul nos painéis e estados unificados de alto contraste para itens ativos, marcados e cursor translúcido; barra de ferramentas padrão expandida com menu de transbordamento nativo, preservando configurações personalizadas; seletor de unidades ligeiramente alargado com barras verdes de capacidade e exibição clara de capacidade desconhecida; barra de comandos semântica oculta por padrão para um visual mais limpo, popups de favoritos restritos aos painéis e emblemas de atalhos padronizados no rodapé
- Detecção automática de codificação de arquivos e cópia a partir de painéis ZIP: Resolução completa de nomes de arquivos corrompidos não-UTF-8 (GBK, GB18030, CP936, Shift-JIS) na compactação e extração (Fixes #74); integração de detecção inteligente de conjunto de caracteres na navegação e extração de arquivos ZIP; suporte total à cópia de entradas selecionadas diretamente de painéis virtuais ZIP
- Limite de largura para a janela de sincronização de diretórios e robustez: Adicionados limites razoáveis de largura máxima à caixa de diálogo de sincronização de diretórios, evitando que tabelas se expandam indefinidamente na horizontal durante grandes comparações (Fixes #76); aprimoramento da lógica de comparação e estabilidade de testes em executores ARM64 e x86_64
- Aprimoramentos de acessibilidade (a11y) e ação de terminal no menu de contexto: Nomes acessíveis atribuídos a todas as ações da barra de ferramentas e suporte completo à navegação por teclado; adição da ação «Terminal do sistema» aos menus de contexto dos painéis de arquivos para abrir o terminal diretamente na pasta ativa; atualização de todos os 31 catálogos de idiomas para novos controles de tema e resumos de capacidade de disco

### 2.3.8 (20/10/2026)

- Reformulação da interação no painel de arquivos e hierarquia visual: Redesenho dos delegados de linhas para renderizar destaque translúcido suave com bordas arredondadas ao passar o mouse, separando claramente o estado de cursor (Hover) da seleção ativa de arquivos (Fixes #72); eliminação de atrasos no clique com botão direito garantindo a preservação das seleções atuais (Fixes #60); adição das ações «Novo arquivo» (Shift+F4) e «Nova pasta» (F7) diretamente no menu de contexto do painel de arquivos com suporte completo a 31 idiomas (Fixes #61, #70); redefinição automática da seleção de arquivos ao trocar de diretório para evitar operações acidentais entre pastas (Fixes #67)
- Execução no terminal via linha de comando e navegação fluida de caminhos: Ao pressionar Enter sobre qualquer comando shell externo na linha de comando inferior, o terminal padrão do sistema (Terminal.app / iTerm2) é iniciado automaticamente e executado na pasta do painel ativo (Fixes #63); inserção de caminhos ou comandos `cd` navega diretamente com escape robusto de espaços e caracteres especiais
- Gestão profunda de memória e buffers circulares para status do sistema: Aplicação de `WA_DeleteOnClose` e destruição determinística no Visualizador universal (F3), Editor (F4) e em todas as caixas de diálogo modais para eliminar o acúmulo de memória em ciclos repetidos; migração de dispatchers i18n para `weakref.WeakMethod`, quebra de ciclos de referência em `DiskTreeNode` e introdução de cache LRU para QIcon; atualização do Painel de status do sistema e AtbSysBridge com buffers circulares fixos de 120 amostras e reutilização de widgets no local para zerar o consumo excessivo de memória e estilos em telemetria frequente
- Correção na configuração da barra de ferramentas e alinhamento do guia de sandbox: Resolução de problema em que botões recém-adicionados na barra central podiam ser sobrescritos e perdidos ao salvar configurações (Fixes #62); sincronização dos indicadores de Acesso total ao disco (FDA) na barra de status com as ações do menu Configuração

### 2.3.7 (16/10/2026)

- Integridade de runtime no macOS e encerramento seguro do aplicativo: Correção de importações ausentes de `os`, `sys` e `traceback` em módulos de plataforma e registro de logs, eliminando riscos de `NameError` em inicializações headless ou standalone; simplificação de `MainWindow.closeEvent` removendo desconexões redundantes de sinais para assegurar encerramento suave sem falhas de segmentação `SIGSEGV`
- Simplificação da autorização de Acesso total ao disco (FDA) e fallback seguro: Aprimoramento da caixa de diálogo inicial para ocultar automaticamente o botão redundante «Abrir ajustes de Acesso total ao disco» quando o recurso nativo de arrastar para conceder for suportado, estabelecendo um ponto de entrada único que muda para «Acesso total ao disco concedido ✓» quando ativo; adição de fallback defensivo que exibe dinamicamente o botão de ajustes caso o painel Cocoa nativo não responda, garantindo a concessão de permissões em qualquer ambiente

### 2.3.6 (16/10/2026)

- Fixação da versão do compilador Nuitka e eliminação de falhas no Apple Silicon (ARM64): Fixação do compilador Nuitka na versão estável 4.2.2 em todos os fluxos de CI, prevenindo uma corrupção crítica na freelist do compilador PySide6/Shiboken (`SIGSEGV / EXC_BAD_ACCESS`) introduzida pelo Nuitka 4.3; inclusão de asserções de integridade de sinais/slots Qt e da freelist do compilador em `smoke_test.py`; alinhamento dos scripts de compilação locais com as etapas de lançamento da CI
- Robustez no ciclo de vida de janelas e bandeja do sistema no macOS 15 Sequoia: Reformulação na restauração de janelas, ativação (`activate_app`) e alternância do ícone do Dock para evitar chamadas inválidas de `FocusWindowEvent` no WindowServer e travamentos em ambientes headless ou de teste; encerramento seguro e isolamento de threads receptoras de atalhos globais pynput para prevenir vazamentos em segundo plano e ganchos `CGEventTap` pendentes; limpeza da área de transferência ao sair para evitar travamentos no destruidor estático de `QMimeData`
- Estabilidade da suíte de testes e otimização do fluxo de CI: Resolução de falhas de segmentação esporádicas durante o encerramento de testes pytest com bandeja e janelas, melhorando a confiabilidade de testes sem interface gráfica; fluxos de CI simplificados para ignorar compilações redundantes de pacotes em alterações exclusivas da documentação

### 2.3.5 (15/10/2026)

- Integração nativa de VFS em nuvem para Google Drive e Dropbox com OAuth 2.0: Suporte nativo a sistemas de arquivos virtuais para Google Drive (`gdrive://`) e Dropbox (`dropbox://`); inclusão de perfis dedicados no Gerenciador de conexões com suporte a credenciais personalizadas de Client ID / Client Secret e autorização OAuth 2.0 em navegador com um clique; otimização de caminhos rápidos para cópia direta em streaming, cache TTL de cotas e listagem sob demanda de diretórios com salvamento automático do perfil
- Segurança consolidada das Chaves do macOS e exportação/importação criptografada de credenciais: Limpeza dos namespaces de serviço das Chaves para eliminar caixas de diálogo repetitivas na inicialização e garantir persistência robusta de credenciais e licenças; introdução de exportação e importação criptografadas de credenciais salvas, protegidas por senha definida pelo usuário para migração segura entre dispositivos, com suporte completo a 31 idiomas
- Robustez do runtime Nuitka e melhorias no streaming de Zip: Resolução de falhas raras de inicialização em pacotes independentes do Nuitka e expansão da cobertura de testes de fumaça na CI para todos os artefatos; aprimoramento do mecanismo de streaming de Zip e correção de potencial esvaziamento do painel durante a invalidação de cache em nuvem
- Correção de concorrência na ordenação e guia abrangente de configuração em nuvem: Resolução de condições de corrida de threads nos testes de ordenação natural e pastas no topo (Fixes #58); ampliação do Capítulo 6 do Guia do Usuário com instruções passo a passo para configuração das APIs do Google Drive e Dropbox, tela de consentimento OAuth e recomendações de segurança

### 2.3.4 (13/10/2026)

- Reformulação do fluxo de permissões no Sandbox e autorização unificada: Restauração e unificação da autorização da pasta pessoal do usuário (`~`) e de unidades externas (`/Volumes`) em um fluxo de trabalho simplificado de botão único «Conceder permissões»; introdução da elevação inteligente de caminhos que promove automaticamente solicitações de acesso a subpastas para a pasta pessoal ou raiz do volume salvando favoritos com escopo de segurança, eliminando completamente solicitações repetitivas no Sandbox da Mac App Store
- Internacionalização de botões padrão de diálogo e aprofundamento do catálogo em 31 idiomas: Implementação do tradutor `_GettextQtTranslator` para interceptar e traduzir dinamicamente via gettext botões padrão do Qt (Sim, Não, OK, Cancelar, Salvar, Descartar, Aplicar, Fechar, Abrir, Redefinir) com remoção automática de aceleradores de atalho (`&`); inclusão de recarregamento dinâmico de interface (`retranslate_ui`) nas páginas de preferências (Barra de ferramentas, Teclas de atalho, Abas favoritas, Atualização automática), no Gerenciador de conexões e no Visualizador de filas; atualização e compilação dos catálogos `.po`/`.mo` em todos os 31 idiomas com novos testes automatizados

### 2.3.3 (10/10/2026)

- Reformulação do compactador, arquivamento separado e progresso em streaming: Adicionada a opção «Criar um arquivo compactado separado para cada item selecionado» no diálogo de arquivamento para compactação em lote individual; implementado acompanhamento de progresso em streaming para arquivos grandes (≥1 MB) nos drivers Zip, Tar e 7z; resolução de colisões segura para threads (Substituir, Ignorar, Renomear automaticamente, Cancelar), tolerância a falhas aprimorada e preservação robusta de links simbólicos com traduções sincronizadas em 31 idiomas
- Geometria da bandeja do sistema e atalho global do macOS blindados: Restauração perfeita de posição, dimensões e estado maximizado da janela ao reativar a partir da bandeja do sistema; menus de contexto da bandeja não trazem mais a janela principal indevidamente para primeiro plano; reformulação do atalho global de exibição/ocultação no macOS normalizando teclas Option e armazenando o contexto de teclas na thread principal para eliminar asserções no macOS Sequoia; alternância dinâmica de minimizar para a bandeja nas Preferências
- Seletor de unidades e dicas de capacidade do disco enriquecidas: Barra de seleção de unidades atualizada com rótulos de volume nativos e ícones de disco de hardware; dicas de contexto enriquecidas com ponto de montagem, tipo de sistema de arquivos, espaço livre e capacidade total
- Integridade de compilação Nuitka e testes de fumaça automatizados no pacote: Inclusão de `--include-package=atbcmder` em todos os scripts de compilação Nuitka para eliminar erros `ModuleNotFoundError` em diálogos carregados sob demanda; introduzido modo headless `--smoke-test` integrado aos fluxos de geração de DMG, Mac App Store PKG e CI para garantir pacotes de aplicativos estáveis e sem falhas
- Lançamento da página oficial multilíngue do produto: Lançamento do site oficial moderno de apresentação do produto com roteador inteligente de idiomas no cliente (suportando português, inglês, chinês, japonês, coreano e outros), destacando a produtividade do painel duplo e o design nativo para macOS

### 2.3.2 (07/10/2026)

- Otimização avançada de memória em tempo de execução PySide6 e compactação de heap no macOS: Implementação de proxy sob demanda para diálogos secundários pesados (`_make_lazy_dialog`) e exportações de módulos PEP 562 para reduzir drasticamente a memória residente; encapsulamento de chamadas Cocoa/PyObjC em `objc.autorelease_pool()` para eliminar acúmulo de memória durante a verificação de etiquetas de cores do Finder; integração da compactação nativa de heap Darwin via `malloc_zone_pressure_relief` em períodos ociosos e no fechamento de diálogos; ThumbnailManager limitado a 4 threads de trabalho com decodificação segura e cache multinível de ícones
- Restauração do cursor piscante e foco automático no visualizador F3 e editor F4: Correção da perda de foco ao abrir o visualizador de arquivos ou o editor com foco automático no buffer de texto para interação imediata pelo teclado; recuperação do cursor piscante visível de 1px, desacoplamento das configurações de cursor entre visualizador e editor e adição do atalho F6 (`cm_ShowCaret`) para alternar a visibilidade do cursor no Visualizador universal
- Reforço do ciclo de vida de recursos e documentação atualizada: Adicionado `WA_DeleteOnClose` ao Visualizador universal para garantir a destruição completa do componente e liberação de memória ao fechar; guias de usuário e ilustrações da documentação atualizados

### 2.3.1 (06/10/2026)

- Guia de permissões no Sandbox e reposicionamento inteligente de janelas: Ao solicitar acesso total ao disco (FDA) e abrir os Ajustes do Sistema, o diálogo de integração se redimensiona e se move automaticamente para a esquerda da tela, organizando-se lado a lado com os Ajustes do Sistema do macOS sem sobreposições
- Instruções passo a passo claras e lembrete de reinício: Mensagens reformuladas com um guia intuitivo em 4 etapas (localizar ou adicionar o ATBCmder, ativar o botão, fechar e reiniciar o aplicativo) com lembretes claros de que o acesso FDA passa a valer após o reinício
- Tradução em 31 idiomas e sincronização do glossário: Glossário de localização atualizado e catálogos de mensagens recompilados em todos os 31 idiomas suportados, garantindo mensagens acolhedoras e naturais em todo o mundo

### 2.3.0 (05/10/2026)

- Etiquetas de cores nativas do macOS Finder e sincronização em tempo real: Integração profunda com as APIs macOS Foundation (`NSURLTagNamesKey`) e `NSWorkspace` para exibir etiquetas de pontos coloridos nativos do Finder nos painéis de arquivos; oferece suporte à ordenação pela ordem nativa de cores do Finder com verificação de viewport a cada 2 segundos para sincronização imediata; inclui visibilidade de coluna personalizável nas Preferências e nomes de cores totalmente localizados
- Reformulação da sincronização de diretórios (`cm_SyncDirs`): Painel de sincronização de diretórios totalmente reprojetado para eliminar bloqueios de interface e inclusão de um diálogo dedicado a erros (`SyncErrorsDialog`); introduzidos Inverter diretórios, exclusão bidirecional (`OP_DELETE_BOTH`), sintaxe de exclusão por curinga com barra vertical `|`, estatísticas de seleção em tempo real, exportação para CSV, submenus de seleção, «Revelar no Finder» e persistência da geometria da janela e largura das colunas
- Dicas de contexto interativas em vidro fosco Apple HIG: Desenvolvida uma arquitetura centralizada de tooltips com cartões em vidro fosco translúcido a 80% adaptados às aparências Clara e Escura do macOS; dicas unificadas na barra de ferramentas, divisores, caminhos breadcrumb, teclas de função Fx e caixas de diálogo com emblemas de atalhos nativos do macOS, suprimindo dicas Qt duplicadas
- Conformidade com atalhos nativos do macOS e desduplicação automática de conflitos: Descrições e símbolos de atalhos padronizados de acordo com as convenções oficiais do macOS, sincronizando rigorosamente menus e ações da barra de ferramentas; eliminação de conflitos históricos 1 para 1 com desduplicação automática em diálogos de configurações, registro de comandos e armazenamento XML
- Cobertura de tradução de 100% em 31 idiomas e expansão de demonstrações: Atingida cobertura total de 100% na localização com tratamento gramatical preciso de plurais em todos os 31 idiomas suportados; visualizador universal de arquivos (F3) aprimorado com opção «Abrir em modo texto» e suporte a dicas ao passar o mouse sobre nomes de arquivos truncados; scripts de demonstração expandidos para filtro rápido, renomeação em lote, VFS transparente de arquivos compactados, sincronização de diretórios e exibição em árvore

### 2.2.0 (03/10/2026)

- Ergonomia da barra de ferramentas principal e gradientes Apple HIG: Ícones da barra principal ampliados para 38px e altura da barra aumentada para 42px, eliminando gráficos achatados e proporcionando áreas confortáveis de clique em telas Retina; ícones renovados com gradientes coloridos vibrantes no estilo Apple HIG e contraste aprimorado, harmonizando as proporções entre a barra principal e a central
- Conexão completa de preferências e configurações do editor de código: Conectadas totalmente configurações antes desconectadas (zoom de fonte, padrões de compactação de arquivos, recuo automático, largura máxima de texto no visualizador); corrigida a persistência do tamanho de tabulação (`tab_size`) e do recuo no `CodeEditorWidget` via carregamento confiável de configurações em tempo de execução
- Gerenciamento global de memória e otimização profunda de desempenho: Reformulação do cache de ícones e metadados de arquivos com inicialização lenta (lazy loading) para componentes pesados; ciclo de vida dos widgets e limpeza de referências fracas fortalecidos para eliminar vazamentos de memória, mantendo a navegação rápida em diretórios grandes
- Prevenção de travamentos em diálogos modais e estabilidade de foco na visualização em árvore: Corrigidos travamentos potenciais ao fechar `ArchiveDialog` e `SplitLinkDialog`; garantida a preservação estável do foco do teclado na aba ativa durante a alternância do modo de árvore e a navegação em pastas
- Otimizações de empacotamento Nuitka e prevenção de falhas: Pipelines de compilação de aplicativos independentes e DMG aprimoradas para reduzir o consumo de memória na compilação e o tamanho do pacote; sinalizadores do compilador refinados para erradicar falhas de inicialização causadas por importações de teste em versões empacotadas

### 2.1.0 (02/10/2026)

- Redesenho Apple HIG para barra de unidades e abas: Redesenhada a barra de unidades e os botões de navegação com controles sem bordas no estilo Apple; modernizada a barra de caminho breadcrumb e as abas de arquivos usando superfícies tonais Apple HIG para uma estética nativa e refinada no macOS
- Steppers modernos HIG, dicas em cápsula e paginação: Controles numéricos (QSpinBox / QDoubleSpinBox) atualizados com steppers integrados ao macOS HIG; introduzidas dicas de ferramentas translúcidas em formato de cápsula no estilo Apple posicionadas inteligentemente sob os ícones; paginação e ícones de configurações adaptados aos padrões HIG
- Barra de ferramentas vertical e hierarquia de miniaturas: Adicionado um ícone dedicado para «Igualar destino à origem (`cm_TargetEqualSource`)» na barra central vertical; corrigida a ordem z das marcas de seleção em miniaturas para renderização confiável sobre as imagens; resolvido o transbordamento do botão de zoom na barra de status do editor de imagens
- Localização abrangente e revisão terminológica em 31 idiomas: Auditoria e refinamento minucioso de termos da interface, dicas de ferramentas e textos de diálogos em todos os 31 idiomas suportados, eliminando chaves ausentes e frases inadequadas para uma experiência nativa autêntica
- Aprimoramentos nas ferramentas e na infraestrutura de automação: Padronizados os fluxos de trabalho de catálogos localizados (`atb-python-i18n`), otimizada a resolução de tokens para utilitários de lançamento e reforçado o isolamento de testes para entregas robustas em CI/CD

### 2.0.0 (28/09/2026)

- 🎉 Marco arquitetural principal do ATBCmder 2.0: Celebra a maturidade definitiva da arquitetura moderna do gerenciador de arquivos de painel duplo, unindo o lendário fluxo centrado no teclado do Double Commander ao desempenho e design nativos do macOS moderno
- Localização global completa em 31 idiomas: Tradução nativa integral de todo o fluxo de concessão de permissões e do painel flutuante «Arrastar para autorizar» (Drag-to-Grant) em todos os 31 idiomas suportados; recompilados todos os catálogos .mo e adicionados testes automatizados de regressão multilíngue
- Concessão revolucionária de Acesso Total ao Disco «Arrastar para autorizar»: Baseado no Cocoa NonactivatingPanel nativo para permitir que os usuários arrastem o ícone do aplicativo diretamente para os Ajustes do Sistema sem roubar o foco da janela; o diálogo de orientação se acopla suavemente ao lado dos Ajustes do Sistema com a opção «Encerrar e reabrir», eliminando temporizadores automáticos incômodos
- Refinamento do fluxo de painel duplo e interface humana: Dê um clique duplo na barra ou divisor central para redefinir instantaneamente os painéis para a proporção equilibrada de 50:50 com dicas de ferramentas localizadas; a barra de ferramentas principal inclui por padrão uma cápsula de status do sistema elegante com botão de fechamento rápido e menu de contexto; aperfeiçoada a ordenação mista de pastas em todas as colunas
- Editor de texto moderno e suíte ATBSys de alto desempenho: O editor integrado agora oferece navegação completa com as teclas Home/End do macOS e posicionamento de linha Smart Home; totalmente integrado ao daemon nativo em Go `atbsys` para limpeza de resíduos com precisão de 64 bits e desinstalação profunda de aplicativos

### 1.9.9 (27/09/2026)

- Acesso Total ao Disco «Arrastar para autorizar» e experiência de introdução reformulada: Introduzido um inovador painel flutuante baseado em Cocoa NonactivatingPanel que permite arrastar o ícone do app diretamente para os Ajustes do Sistema sem perder o foco; a janela de orientação se posiciona automaticamente ao lado dos Ajustes do Sistema e disponibiliza a opção «Encerrar e reabrir» após a concessão de FDA, eliminando temporizadores forçados de reinicialização
- Equalização 5:5 de painel duplo e aprimoramento do divisor central: Clicar duas vezes na barra de ferramentas central ou divisor iguala instantaneamente as dimensões dos painéis na proporção 50:50 com dicas de ferramentas localizadas; corrigidos vazamentos em assinaturas i18n, eliminada retenção indevida do cursor do mouse e aprimorado o estilo do visualizador e de diálogos
- Ergonomia do teclado no editor (Home/End e Smart Home): O editor de texto integrado agora suporta totalmente a navegação padrão pelas teclas Home e End no macOS, incluindo o comportamento Smart Home (alternando entre o primeiro caractere não vazio e a coluna zero da linha)
- Controle da cápsula de status do sistema na barra de ferramentas e menu de contexto: A cápsula de status do sistema na barra de ferramentas principal agora vem ativada por padrão com botão de fechamento rápido (×); adicionado menu de contexto com clique direito para alternar facilmente componentes da barra de ferramentas e monitores
- Paridade na ordenação mista de pastas e aceleração da renderização de fontes: O modo de ordenação mista (`sort_folder_mode = mixed`) intercala de forma contínua arquivos e pastas em todas as ordenações de colunas com aplicação imediata em tempo de execução; removidas declarações de pseudo-fontes para eliminar sobrecarga no CoreText, unificadas as alturas dos cartões do tutorial e prevenido o clique indesejado em menus nativos

### 1.9.8 (24/09/2026)

- Precisão de 64 bits (>2 GB) nas ferramentas do sistema e melhorias no desinstalador: Corrigido o estouro de sinal inteiro de 32 bits do Qt e a perda de precisão de 64 bits ao relatar contagens de bytes de limpeza superiores a 2 GB; adicionada a exibição e ordenação por data de instalação de aplicativos no Desinstalador de Aplicativos
- Conformidade com o sandbox da Mac App Store e propagação do diretório pessoal real: Propagado o diretório pessoal real do usuário (`real_home`) pela ponte `atbsys` para limpeza precisa de disco e detecção de resíduos dentro do App Sandbox; reforçadas as interfaces de elevação de privilégios, execução de terminal e scripts para estrita conformidade com as diretrizes de revisão da App Store
- Controles de layout nas preferências e correções na Lista de Favoritos de Diretórios (Hotlist): Adicionados controles de alternância de layout da janela principal nas Preferências Gerais com sincronização em tempo real do `MainWindow` e `ThemeManager`, e desativada a cápsula de status do sistema na barra de ferramentas principal por padrão para um espaço de trabalho inicial mais limpo; corrigidos menus suspensos vazios e retradução dinâmica de idioma nas configurações da Lista de Favoritos de Diretórios
- Padronização terminológica e aprimoramento do seletor de idioma: Padronizada a tradução chinesa de "Directory Hotlist" para "路径收藏夹" em todas as interfaces e aprimorado o seletor de idioma nas Preferências com exibição dupla (nome no idioma nativo e nome traduzido)
- Preservação de ACL das Chaves do macOS e confiabilidade de cópia em fluxo: Preservadas as listas de controle de acesso (ACLs) existentes das Chaves do macOS (Keychain) e eliminadas gravações redundantes na inicialização para evitar solicitações repetidas de autorização; garantida a emissão determinística do sinal `operation_completed` antes da conclusão da thread no `StreamCopyWorker`

### 1.9.7 (23/09/2026)

- Aplicação imediata de configurações em tempo de execução (Hot Reload): Todas as configurações em 7 páginas principais de opções (Operações de Arquivo, Editor, Visualizador, Pesquisa Rápida e Filtro, Abas, Ícones do Painel de Arquivos e Ordenação) agora entram em vigor imediatamente após salvar, sem necessidade de reiniciar o aplicativo; adicionado o parâmetro configurável `sort_folder_mode` com suporte para Pastas Primeiro, Arquivos Primeiro e Ordenação Mista
- Segurança e paridade na sincronização de diretórios: Auditoria abrangente da Sincronização de Diretórios (`cm_SyncDirs`) alinhando o comportamento diretamente ao clássico Double Commander; fortalecidas a validação de estado bidirecional e as verificações de segurança para eliminar riscos de sincronização assimétrica
- Dicas de ferramentas inteligentes para nomes de arquivos truncados com precisão CJK: Adicionadas dicas de ferramentas (tooltips) inteligentes ao passar o mouse e selecionar que aparecem exclusivamente quando nomes de arquivos longos são truncados com reticências, mantendo a interface limpa para itens totalmente visíveis; integrados cálculos de alta precisão de largura de caracteres CJK para eliminar discrepâncias métricas de fontes
- Refinamento do fluxo de trabalho de painel duplo e interações: A compactação e extração de arquivos via clique com o botão direito definem por padrão o diretório do painel oposto como destino, com foco padrão no botão Iniciar; refinada a ordem dos botões e a ação padrão do teclado na caixa de diálogo de confirmação de exclusão; restaurados os cursores de ponteiro para os botões de ação da barra de ferramentas central
- Diretório pessoal real no sandbox da Mac App Store e reforço de FDA: Implementado o motor de resolução `real_home` para resolver com precisão os diretórios pessoais do usuário e Listas de Favoritos sob contêineres App Sandbox; corrigidos falsos alarmes de Acesso Total ao Disco (FDA) com fechamento automático de diálogos após autorização; migradas as métricas de CPU do sistema para Mach host statistics para conformidade com o sandbox

### 1.9.6 (21/09/2026)

- Modo de redimensionamento personalizado no editor de imagens: Introduzido o modo "Tamanho Personalizado (Custom Size)" na caixa de diálogo de redimensionamento de imagem, permitindo a entrada direta de pixels para largura e altura com bloqueio opcional de proporção, oferecendo aos usuários controle preciso sobre o dimensionamento
- Reforço de segurança no Sandbox e conformidade para Mac App Store: Cumprimento rigoroso das Diretrizes de Revisão da Apple App Store 2.4.5(v) e 2.5.2; remoção de solicitações de autorização de diretório raiz em compilações em sandbox e desativação da interface e lógica de encerramento de processos (SIGKILL/SIGTERM) no modo sandbox da MAS, eliminando riscos de violação e rejeição
- Transbordamento adaptativo da barra de ferramentas e estabilidade do visualizador Diff: Adicionado tratamento automático de transbordamento à barra de ferramentas principal para recolher botões de ação em um menu suspenso em telas menores; resolvido travamento intermitente na suíte de testes do visualizador Diff no macOS x86
- Localização do menu em 30 idiomas: Concluídas traduções abrangentes para o menu de nível superior "Ferramentas (Tools)" e ações relacionadas em todos os 30 idiomas suportados
- Desempenho da interface e resiliência do pipeline CI/CD: Limpeza de referências residuais a widgets no painel de texto para acelerar significativamente a troca de temas e a velocidade de redesenho; fluxos de trabalho de CI/CD atualizados para suportar seleção parametrizada de executores ARM64 (auto-hospedados vs. nuvem) com espera exponencial e repetição no envio de artefatos

### 1.9.5 (19/09/2026)

- Herança de sandbox para executáveis auxiliares na Mac App Store: Adicionadas permissões dedicadas (`com.apple.security.app-sandbox` e `com.apple.security.inherit`) para todos os executáveis secundários (como o binário de ferramentas do sistema `atbsys`) em `Contents/MacOS/`, garantindo que os processos auxiliares herdem corretamente o contêiner App Sandbox e as políticas de segurança do aplicativo principal para total conformidade com a Mac App Store
- Assinatura de código Hardened Runtime para auxiliares DMG: Habilitado o Hardened Runtime (`--options runtime`) com os direitos apropriados para todos os executáveis Mach-O auxiliares em pacotes de distribuição DMG, garantindo total conformidade com os requisitos de assinatura de código e notarização do Apple Developer ID
- Limpeza da estrutura do pacote e testes de integração de empacotamento: Remoção automatizada de diretórios de binários de recursos redundantes (`Contents/Resources/bin`) para uma estrutura de pacote mais limpa e em conformidade com a App Store; adição de testes de integração de empacotamento automatizados abrangendo direitos de auxiliares, Hardened Runtime e scripts de compilação multiarquitetura

### 1.9.4 (19/09/2026)

- Suíte de ferramentas do sistema e manutenção ATBSys: Integração completa do conjunto nativo de utilitários do sistema, com Cápsula de Status do Sistema na barra de ferramentas principal (monitoramento em tempo real de CPU, memória, disco e tráfego de rede com menu de pausa/intervalo/ocultação e alternância nas preferências), Painel Completo de Status do Sistema (métricas de hardware e gerenciamento/finalização de processos com clique com o botão direito), Analisador de Espaço em Disco (visualização hierárquica Treemap, ordenação interativa de colunas, ações de revelar no Finder/mover para a lixeira e exportação de relatórios em CSV/TXT), Limpador de Sistema seguro em duas etapas (varredura e limpeza de caches do usuário, registros de aplicativos, arquivos residuais, categorias Homebrew, CocoaPods e Docker com proteção de lista permitida `~/.config/mole/whitelist`) e Desinstalador Profundo de Aplicativos com detecção de sobras
- Motor bridge nativo em Go de alto desempenho e logs de auditoria: Desenvolvido sobre o binário nativo em Go leve e independente `atbsys`, comunicando-se via QProcess assíncrono e não bloqueante; empacotado como Universal Binary com automação de empacotamento e integração ao pipeline de CI/CD; todas as operações de limpeza e desinstalação são estruturadas e registradas em logs de auditoria no diretório de logs do ATBCmder
- Tutorial interativo para iniciantes expandido para 27 etapas: Currículo de integração para iniciantes aprimorado com orientações práticas para ferramentas de monitoramento e manutenção do sistema; reprojetado o posicionamento do destaque da barra de menus para precisão independente do idioma na barra de menus nativa do macOS
- Localização abrangente em 30 idiomas e documentação oficial: Traduções completas para todos os componentes do ATBSys, opções da cápsula de status, configurações e etapas do tutorial em todos os 30 idiomas suportados; guia oficial do usuário em inglês enriquecido com o Capítulo 7: Ferramentas do Sistema e Manutenção
- Refinamento de interface e fortalecimento de empacotamento: Alargamento da cápsula da barra de status e dos rótulos de taxa de rede para eliminar o truncamento de texto durante transferências de alta taxa; refinamento do layout da cápsula alinhada à direita e sincronização de desvinculação de atalhos; fortalecimento da verificação de injeção de dylibs e binários de arquitetura única e universais em executores macOS 12 x86_64

### 1.9.3 (17/09/2026)

- Suporte a pré-visualização de arquivos .ini no visualizador universal: Adicionado suporte nativo a pré-visualização em texto simples para arquivos de configuração `.ini` no Visualizador Universal (F3) e na Visualização Rápida (`Ctrl+Q` / `⌘Q`), permitindo inspeção instantânea de configurações sem abrir editores externos
- Empacotamento para App Store e assinatura de frameworks: Compilação e injeção automatizadas de `libATBLicenseKit.dylib` em `Contents/Frameworks/` para compilações de lançamento da Mac App Store e DMG; adicionadas assinatura de código estrita e notarização para bibliotecas dinâmicas, aprimoramento da descoberta de pacotes em tempo de execução e fusão protegida de binários universais
- Estabilidade do mecanismo do tutorial interativo: Resolução de tempos limites de navegação de etapas no currículo de favoritos (Hotlist), redefinição adequada de sinalizadores de transição pendentes na alternância de etapas e desconexão de sinais de eventos pendentes para eliminar vazamento de sinais durante a integração

### 1.9.2 (17/09/2026)

- Sistema de licença e avaliação StoreKit 2: Sistema nativo de compra definitiva e licenciamento da Mac App Store baseado em Swift StoreKit 2, com contagem de avaliação por dias do calendário local, validação de recibos offline e restauração de compras; emblema de licença na barra de ferramentas, diálogo de paywall e suporte a binários universais (macOS 12+, Apple Silicon e Intel)
- Execução de comandos Shell incorporada: A barra de linha de comando inferior agora executa comandos de shell diretamente no terminal do sistema (Terminal / iTerm2); oferece suporte ao preenchimento de caminhos com Tab e comandos `cd` puros navegam diretamente nos painéis ativos
- Reformulação da sincronização de diretórios e Diff em linha por palavra: Sincronização de pastas (`cm_SyncDirs`) reprojetada em uma grade clássica de 7 colunas com integração de Diff por clique duplo, eliminando riscos de sincronização assimétrica; o visualizador Diff adiciona destaque detalhado de palavras/caracteres em linha e navegação para a primeira/última diferença
- Alinhamento de armazenamento nativo do macOS e reforço do VFS: Exibição da capacidade do drive e do espaço livre alinhada às especificações de "Armazenamento" dos Ajustes do Sistema do macOS; VFS de rede (SFTP/FTP/Samba/WebDAV) reforçado com verificações de conectividade, reconexão automática e FTPS; ícone da bandeja do sistema atualizado para um ícone minimalista monocromático

### 1.9.1 (14/09/2026)

- Etapa de busca rápida no tutorial interativo: Currículo expandido para 25 etapas com treinamento prático para busca e filtragem rápida (`⌘S` / `Ctrl+S`); adicionada entrada de busca rápida no menu Comandos e aprimorada a limpeza de sobreposição durante as transições de etapas
- Pipeline de empacotamento de CI e reforço de dependências: Restaurada a dependência `ebooklib` nas compilações de lançamento para garantir suporte completo à pré-visualização de EPUB; melhorada a limpeza da área de trabalho para evitar conflitos de permissões

### 1.9.0 (13/09/2026)

- Sistema de tutorial interativo para novatos: Adicionado currículo introdutório interativo de 24 etapas para novos usuários com diálogo de boas-vindas na primeira inicialização (acessível a qualquer momento em "Ajuda → Tutorial Interativo"); apresenta máscara de destaque estilo holofote, cartões flutuantes adaptativos e exibição dupla de caminho de menu e atalhos nativos
- Atualização de segurança de rede SFTP: Substituição do aceite automático inseguro de chave de host por uma política rigorosa de verificação TOFU (Trust-On-First-Use); a conexão a hosts SFTP desconhecidos agora exibe uma caixa de diálogo interativa para confirmação da impressão digital SHA-256, salvando as chaves com segurança em `~/.ssh/known_hosts` contra ataques MITM
- Atalhos nativos do macOS e aprimoramento de navegação: Correção do tratamento de teclas modificadoras em `Command+Cima` (navegar para a pasta superior) e `Command+Shift+F1` (alternar visualização de miniaturas), padronizando todos os atalhos com símbolos nativos do macOS (⌘, ⌥, ⌃, ⇧)
- Desempenho do núcleo e pipeline de compilação: Otimização da correspondência de modelos semânticos e da capacidade de resposta do preenchimento automático; reestruturação dos fluxos de trabalho automatizados de lançamento no GitHub Actions com proteção contra falhas da sandbox do AppKit

### 1.8.0 (11/09/2026)

- Suporte a pacotes universais: Suporte para pacotes universais nas arquiteturas x86_64 e ARM
- Pipeline de build automatizado: Compilação e empacotamento automáticos via GitHub Actions
- Associações inteligentes de arquivos e apps externos: Novo sistema de gerenciamento de associações (`extassoc.xml`) para configurar ações personalizadas, editores e visualizadores externos por extensão; alternância inteligente com macOS LaunchServices e diálogo dedicado "Abrir com"
- Transferência de arquivos grandes e proteção contra estouro de 64 bits: Eliminação completa de estouros de inteiros de 32 bits em sinais de progresso e controles de texto, garantindo transferências estáveis e exibição precisa de progresso para arquivos acima de 2 GB em volumes montados e compartilhamentos de rede
- Hierarquia unificada de saída ESC no visualizador: Padronização do tratamento da tecla ESC em todos os painéis de visualização com saídas em camadas (barra de pesquisa → filtro ativo → tela cheia → fechar janela), eliminando conflitos de atalhos e otimizando a troca rápida de arquivos
- Localização dinâmica em tempo real: A barra inferior de teclas de função (F3–F8) agora é retraduzida instantaneamente ao alterar o idioma nas Preferências, sem a necessidade de reiniciar o aplicativo

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