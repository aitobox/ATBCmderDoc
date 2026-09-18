# Capítulo 7: Ferramentas do sistema e manutenção

Um gerenciador de arquivos profissional não opera no vácuo — ele é o centro nevrálgico do seu armazenamento, memória e recursos do sistema operacional. Embora o gerenciamento de arquivos ortodoxo de painel duplo se destaque na organização, movimentação e sincronização de hierarquias de diretórios, usuários avançados, desenvolvedores e administradores de sistema enfrentam frequentemente desafios no nível do sistema: identificar qual diretório oculto consumiu silenciosamente 50 GB de espaço em disco, localizar um processo descontrolado em segundo plano sobrecarregando os núcleos da CPU, limpar gigabytes de caches de desenvolvedores abandonados e artefatos de compilação, e desinstalar completamente aplicativos legados do macOS sem deixar arquivos de preferências órfãos, launch daemons ou pastas do Application Support espalhadas por `~/Library/`.

O ATBCmder integra quatro ferramentas especializadas de diagnóstico e manutenção do sistema diretamente no menu **Ferramentas**. Equipadas com um daemon de monitoramento nativo e assíncrono, essas ferramentas operam perfeitamente ao lado dos seus painéis de arquivos sem bloquear a interface de usuário nem exigir utilitários pesados de terceiros repletos de anúncios.

---

## 1. Início rápido visual: ferramentas do sistema e HUD de status

O ATBCmder divide a manutenção do sistema em quatro instrumentos operacionais essenciais, acompanhados por uma cápsula de monitoramento sempre visível na barra de ferramentas:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       ATBCMDER SYSTEM TOOLS SUITE                                      │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                        │
│  [1] Status Capsule HUD & Popover       [2] System Status & Diagnostics (⌘⇧M)                         │
│      • Real-time CPU, RAM, and Network      • Per-core utilization bars, full process table            │
│      • Color-coded threshold styling        • Search/filter processes, send SIGTERM/SIGKILL            │
│      • Click for multi-metric popover       • Disk filesystem capacity and network interface graphs   │
│                                                                                                        │
│  [3] Disk Usage Analyzer (⌘⇧D)          [4] System Cleaner (⌘⇧C)                                      │
│      • Multi-threaded directory scanner     • Two-stage safe cleaner: scan first, review, then clean   │
│      • Interactive squarified treemap       • 6 categories: caches, logs, Xcode, dev tools, trash      │
│      • Breadcrumb drill-down navigation     • 3 risk levels (Safe, Warning, Danger) + Whitelist        │
│                                                                                                        │
│  [5] Application Uninstaller (⌘⇧U)                                                                     │
│      • Complete removal of .app bundles and deep remnant files                                         │
│      • Cleans Application Support, Preferences, Caches, LaunchAgents, and Containers                   │
│      • Dual mode: Complete Uninstall vs. Remnants Only (clean up previously deleted apps)              │
│                                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Matriz de atalhos das ferramentas do sistema em matriz dupla

| Ferramenta / Ação | Atalho do macOS | Tecla Commander Clássica | ID do comando | Localização no menu |
| :--- | :--- | :--- | :--- | :--- |
| **Painel de status do sistema** | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` | **Ferramentas ➔ Status do sistema...** |
| **Analisador de uso de disco** | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` | **Ferramentas ➔ Analisador de uso de disco...** |
| **Limpador do sistema** | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` | **Ferramentas ➔ Limpador do sistema...** |
| **Desinstalador de aplicativos** | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` | **Ferramentas ➔ Desinstalar aplicativo...** |
| **Alternar cápsula de status** | Preferências ➔ Geral | — | *(Ajustes)* | **Configuração ➔ Opções ➔ Geral** |

---

## 2. Cápsula de status HUD da barra de ferramentas e popover dinâmico

O ATBCmder possui uma **Cápsula de status do sistema** integrada diretamente no lado direito da barra de ferramentas principal. Isso fornece uma percepção imediata e periférica da integridade do sistema, sem exigir que você alterne para o Monitor de Atividade ou abra um terminal separado.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [Left Panel Tabs]                   [Right Panel Tabs]          [ CPU 18% | RAM 44% | ↓1.2M ↑340K ]│
└───────────────────────────────────────────────────────────────────────────┬────────────┘
                                                                            │ Click Capsule
                                                                            ▼
                                                ┌───────────────────────────────────────┐
                                                │ SYSTEM METRICS SUMMARY                │
                                                ├───────────────────────────────────────┤
                                                │ CPU Usage:     [████░░░░░░░░░░]   18% │
                                                │ Memory:        [████████░░░░░░]   44% │
                                                │ GPU Load:      [██░░░░░░░░░░░░]   12% │
                                                │ Battery:       [████████████░░]   88% │
                                                ├───────────────────────────────────────┤
                                                │ Storage:                              │
                                                │  Macintosh HD:  312.4 GB / 994.6 GB   │
                                                │  External SSD:  842.1 GB / 2.0 TB     │
                                                ├───────────────────────────────────────┤
                                                │ Top Processes:                        │
                                                │  • ATBCmder         PID: 54102  CPU: 2%│
                                                │  • WindowServer     PID: 284    CPU: 8%│
                                                │  • Xcode            PID: 88120  CPU: 4%│
                                                ├───────────────────────────────────────┤
                                                │ [ Open Full System Monitor (⌘⇧M) ➔ ] │
                                                └───────────────────────────────────────┘
```

### 2.1 Componentes da cápsula e estilo visual

A cápsula de status (`320px` de largura) exibe três métricas de telemetria em tempo real atualizadas uma vez por segundo:

1. **Utilização da CPU**: Porcentagem agregada de uso do processador em tempo real com codificação visual dinâmica por cores:
   - **Normal (< 75%)**: Azul de destaque / primeiro plano do tema.
   - **Elevado (75% – 90%)**: Laranja de aviso.
   - **Crítico (> 90%)**: Vermelho de alerta.
2. **Utilização de memória (RAM)**: Pressão de memória atual ativa e presa (wired) expressa como uma porcentagem da RAM física.
3. **Taxa de transferência de rede**: Velocidades agregadas de upload e download em tempo real em todos os adaptadores de rede ativos formatadas de forma compacta (ex.: `↓2.4 MB/s ↑512 KB/s`).

### 2.2 Popover interativo (`StatusPopup`)

Clicar em qualquer ponto da cápsula de status abre um **Popover de status** flutuante não modal:

- **Telemetria de hardware**: Visualize porcentagens combinadas de CPU, memória, GPU e status da bateria (incluindo porcentagem de carga e estado de carregamento).
- **Montagens do sistema de arquivos**: Lista todos os recipientes APFS locais montados e unidades externas com barras de espaço livre e capacidade total.
- **5 principais processos**: Destaca os cinco processos que mais consomem recursos por porcentagem de CPU e volume de memória.
- **Botão de detalhamento**: Clique em **"Abrir monitor completo do sistema"** (ou pressione `⌘⇧M`) para iniciar a janela abrangente de diagnósticos.

### 2.3 Como configurar a visibilidade da cápsula

Se preferir uma barra de ferramentas livre de distrações, contendo apenas os controles de navegação de arquivos:

1. Abra as **Preferências** (`⌘,` / **Configuração ➔ Opções...**).
2. Selecione **Geral** na barra lateral esquerda.
3. Em **Exibição e layout**, marque ou desmarque a caixa de seleção:
   `[X] Mostrar cápsula de status do sistema na barra de ferramentas`
4. Clique em **Aplicar** ou **OK**. A cápsula aparecerá ou desaparecerá imediatamente da barra de ferramentas principal.

---

## 3. Status do sistema e diagnósticos (`cm_SystemStatus` / `⌘⇧M`)

Pressionar **`⌘⇧M`** (ou **`Ctrl+Shift+M`**) abre o **Painel de status do sistema** completo. Este utilitário serve como um console de diagnóstico integrado feito sob medida para administradores de sistema, desenvolvedores e resolução de problemas de desempenho.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             SYSTEM STATUS & DIAGNOSTICS                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CPU USAGE: Apple M3 Max (14 Cores)                                                     │
│ Core 01: [██████░░░░] 60%    Core 05: [██░░░░░░░░] 20%    Core 09: [███░░░░░░░] 30%    │
│ Core 02: [████░░░░░░] 40%    Core 06: [████░░░░░░] 42%    Core 10: [█░░░░░░░░░] 10%    │
│ Core 03: [████████░░] 80%    Core 07: [█░░░░░░░░░] 12%    Core 11: [░░░░░░░░░░]  5%    │
│ Core 04: [███░░░░░░░] 30%    Core 08: [██░░░░░░░░] 18%    Core 12: [░░░░░░░░░░]  4%    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ MEMORY: Total 36.0 GB  |  Used: 16.2 GB (45%)  |  App: 9.4 GB  |  Wired: 4.1 GB       │
│ SWAP:   Total 2.0 GB   |  Used: 0 MB (0%)                                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ PROCESS LIST                                 Filter: [ node                     ] [x]  │
│ PID      Name             User           CPU %       Memory      Threads    Action     │
│ ────────────────────────────────────────────────────────────────────────────────────── │
│ 72841    node (dev-srv)   brain          48.2%       612.4 MB    28         [ Kill ✕ ] │
│ 72910    node (esbuild)   brain          12.1%       184.2 MB    14         [ Kill ✕ ] │
│ 73104    node (lsp)       brain           1.4%        98.5 MB     8         [ Kill ✕ ] │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Update Interval: [ 1.0s ▼ ]       [ Pause Monitoring ]              [ Close (Esc) ]    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Recursos de diagnóstico e seções de métricas

1. **Monitor de processador multi-core**:
   - Visualiza a carga geral do sistema e a distribuição entre os núcleos individuais de Desempenho (Performance) e Eficiência (Efficiency).
   - Medidores de progresso individuais por núcleo destacam a saturação de processamento durante compilações ou renderizações com várias threads.
2. **Detalhamento de memória e pressão de swap**:
   - Categoriza a alocação da memória física em Memória de Aplicativos (App Memory), Memória Presa (Wired Memory), Memória Comprimida (Compressed Memory) e Arquivos em Cache (Cached Files).
   - Monitora o uso do espaço de troca virtual (swap) para ajudar a identificar quando vazamentos de memória estão causando paginação em disco.
3. **Visão geral de armazenamento e pontos de montagem**:
   - Métricas em tempo real de taxa de transferência de leitura/gravação em disco ao lado dos dados de capacidade do ponto de montagem.
4. **Gerenciador interativo de processos**:
   - Tabela classificável em tempo real contendo todos os processos em execução do sistema e do usuário.
   - **Busca e filtro**: Digite qualquer nome de processo ou PID na caixa de busca para filtrar os resultados instantaneamente.
   - **Encerramento de processos**:
     - Clique em **Kill** ou selecione um processo e pressione `Delete`.
     - Exibe uma caixa de diálogo de confirmação oferecendo **Encerrar (`SIGTERM`)** para um desligamento normal e seguro ou **Forçar encerramento (`SIGKILL`)** para tarefas que não respondem.

---

## 4. Analisador de uso de disco (`cm_DiskUsageAnalyzer` / `⌘⇧D`)

Quando uma unidade de estado sólido (SSD) começa a ficar sem espaço livre, encontrar onde gigabytes de dados estão escondidos pode ser extremamente demorado. As listas de arquivos padrão do Finder não calculam os tamanhos das pastas automaticamente, e a inspeção manual exige navegar de forma cansativa por hierarquias aninhadas.

O **Analisador de uso de disco** (`cm_DiskUsageAnalyzer`, atalho **`⌘⇧D`** / **`Ctrl+Shift+D`**) verifica árvores inteiras de diretórios de forma assíncrona usando um mecanismo de varredura multithread e visualiza seu armazenamento tanto por meio de uma lista de árvore hierárquica tradicional quanto por um **Treemap retangular interativo** (Squarified Treemap).

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DISK USAGE ANALYZER: /Users/brainzhang                                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Path: /Users/brainzhang ➔ Developer ➔ Projects                                        │
├──────────────────────────────────────┬─────────────────────────────────────────────────┤
│ DIRECTORY HIERARCHY                  │ INTERACTIVE SQUARIFIED TREEMAP                  │
│ Folder Name      Size       Percent  │ ┌───────────────────────────┬─────────────────┐ │
│ ──────────────────────────────────── │ │                           │ node_modules    │ │
│ ▼ Developer      142.6 GB   58.2%    │ │ target/debug              │ 28.4 GB         │ │
│   ► Projects     118.2 GB   48.2%    │ │ 64.2 GB                   │ (Rust build)    │ │
│   ► Caches        24.4 GB   10.0%    │ │                           ├─────────────────┤ │
│ ▼ Library         64.2 GB   26.2%    │ │                           │ DerivedData     │ │
│   ► Caches        38.1 GB   15.5%    │ │                           │ 18.2 GB         │ │
│   ► App Support   22.4 GB    9.1%    │ ├───────────────────────────┴─────────────────┤ │
│ ► Downloads       24.1 GB    9.8%    │ │ Video Footage (4K Prores)                   │ │
│ ► Pictures        14.2 GB    5.8%    │ │ 31.8 GB                                     │ │
├──────────────────────────────────────┴─┴───────────────────────────────────────────────┤
│ [ Zoom Out (..) ]  [ Reveal in Dual Panel ]  [ Move to Trash (⌘⌫) ]  [ Export CSV... ]  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Arquitetura e recursos principais

- **Varredura multithread assíncrona**: Examina centenas de milhares de arquivos em recipientes APFS sem travar a interface principal do ATBCmder. Uma barra de progresso exibe os diretórios verificados por segundo.
- **Visualização em Treemap retangular (Squarified Treemap)**:
  - Pastas e arquivos são representados como blocos retangulares aninhados cuja área de superfície bidimensional é estritamente proporcional ao seu tamanho no disco.
  - As cores refletem automaticamente a profundidade do diretório, tornando os grandes consumidores de armazenamento imediatamente identificáveis à primeira vista.
- **Sincronização bidirecional**:
  - Selecionar um item na árvore de diretórios destaca seu bloco correspondente no treemap.
  - Clicar em qualquer retângulo no treemap destaca a linha correspondente na exibição em árvore e mostra o caminho de arquivo completo e o tamanho exato em bytes.

### 4.2 Navegação interativa e fluxos de trabalho

1. **Aprofundar (Drill Down)**: Dê um clique duplo em qualquer linha de pasta ou bloco do treemap para ampliar esse subdiretório e recalcular a exibição em relação à nova raiz.
2. **Reduzir zoom (Zoom Out)**: Clique no botão **Reduzir zoom** na barra de ferramentas ou clique em qualquer segmento na barra estrutural (breadcrumbs) na parte superior para retornar aos diretórios pai.
3. **Inspecionar em painéis duplos**: Clique em **Mostrar no painel duplo** para navegar instantaneamente o painel de arquivos ativo do ATBCmder para o diretório selecionado.
4. **Limpeza instantânea**: Selecione qualquer pasta ou arquivo obsoleto grande e pressione **`⌘⌫`** (ou clique em **Mover para o Lixo**). O item é enviado com segurança para a Lixeira do macOS, e a árvore de varredura é atualizada automaticamente.
5. **Exportar relatórios de armazenamento**: Clique em **Exportar** para gerar auditorias abrangentes de uso de disco formatadas como CSV estruturado ou resumos em texto sem formatação para planejamento de armazenamento.

---

## 5. Limpador do sistema (`cm_CleanSystem` / `⌘⇧C`)

Ao longo de meses de uso diário, o macOS acumula gigabytes de dados temporários: caches obsoletos de aplicativos, artefatos de compilação do Xcode, downloads de gerenciadores de pacotes, registros de diagnóstico órfãos e caches de navegadores web. Embora alguns caches acelerem os fluxos de trabalho, itens obsoletos desperdiçam o valioso espaço de armazenamento SSD de alta velocidade.

O **Limpador do sistema** (`cm_CleanSystem`, atalho **`⌘⇧C`** / **`Ctrl+Shift+C`**) fornece um limpador de sistema determinístico em dois estágios projetado com garantias de segurança corporativa.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              SYSTEM CLEANER: DRY RUN AUDIT                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Scan System ]  Scanned: 48,192 items in 2.1s        Total Reclaimable: 34.8 GB        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CATEGORY                          ITEMS       SIZE        RISK LEVEL     SELECTION     │
│ ────────────────────────────────────────────────────────────────────────────────────── │
│ [X] Application Caches            12,410      14.2 GB     Safe (Green)   [ Select All] │
│ [X] System & User Logs             4,218       1.8 GB     Safe (Green)   [ Select All] │
│ [X] Xcode Derived Data             8,940      12.4 GB     Warning (Org)  [ Select All] │
│ [ ] Homebrew & CocoaPods Caches    1,420       3.6 GB     Warning (Org)  [ Select All] │
│ [ ] Web Browser Caches            21,200       2.8 GB     Safe (Green)   [ Select All] │
│ [ ] Trash Bin Container                4       8.2 GB     Danger (Red)   [ Unselected] │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Selected for Cleanup: 28.4 GB across 25,568 files                                     │
│ Whitelist: ~/.config/atbsys/whitelist (4 rules active)                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Whitelist Editor... ]      [ Export Log ]       [ Clean Selected Items (28.4 GB) ]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 A arquitetura de segurança em dois estágios

Ao contrário dos "limpadores de um clique" imprudentes que excluem arquivos silenciosamente em segundo plano, o ATBCmder impõe um rigoroso **Protocolo de segurança em dois estágios**:

1. **Estágio 1: Varredura de simulação (Dry-Run) e avaliação**:
   - O limpador realiza um levantamento somente leitura em locais padronizados do sistema.
   - Calcula a contagem exata de arquivos e o tamanho em bytes sem modificar ou excluir um único byte sequer.
   - Agrupa os resultados em categorias transparentes com classificações explícitas de risco.
2. **Estágio 2: Exclusão seletiva revisada pelo usuário**:
   - Você revisa a lista categorizada e marca ou desmarca itens individuais ou categorias inteiras.
   - Clicar em **"Limpar itens selecionados"** executa a exclusão apenas nos destinos explicitamente marcados.
   - Cada evento de exclusão é gravado em um registro atômico de auditoria em `~/Library/Preferences/atbcmder/operations.log`.

### 5.2 Seis domínios principais de limpeza

| Categoria | Localização típica | Nível de risco | Descrição |
| :--- | :--- | :---: | :--- |
| **Caches de aplicativos** | `~/Library/Caches/` | **Seguro (Safe)** | Caches obsoletos gerados por aplicativos de mesa que são recriados automaticamente quando necessário. |
| **Logs de usuário e do sistema** | `~/Library/Logs/`, `/var/log/` | **Seguro (Safe)** | Relatórios antigos de falhas, dumps de diagnóstico e logs de atualização de software não mais necessários para solução de problemas. |
| **Caches de navegadores** | Safari, Chrome, Edge, Firefox | **Seguro (Safe)** | Páginas da web em cache, buffers de mídia e artefatos de script nos navegadores de mesa instalados. |
| **Dados derivados do Xcode** | `~/Library/Developer/Xcode/DerivedData` | **Aviso (Warning)** | Arquivos de objetos intermediários, caches de módulos e dados de indexação de compilações anteriores de desenvolvedores Apple. |
| **Caches de gerenciadores de pacotes** | Homebrew, CocoaPods, NPM, Yarn | **Aviso (Warning)** | Arquivos tarball baixados, arquivos compactados de fórmulas e diretórios de cache de pacotes. |
| **Lixeira** | `~/.Trash`, `.Trashes` | **Perigo (Danger)** | Itens movidos anteriormente para a Lixeira do macOS que ainda não foram esvaziados permanentemente. |

### 5.3 Níveis de risco e lista de permissões de segurança

- 🟢 **Seguro (Verde / Safe)**: Caches temporários e metadados descartados que podem ser removidos com zero perda de configuração ou interrupção do fluxo de trabalho.
- 🟡 **Aviso (Laranja / Warning)**: Artefatos de desenvolvedor ou caches de pacotes. Excluí-los é seguro, mas as compilações subsequentes do projeto ou os downloads de pacotes levarão mais tempo à medida que os itens forem baixados novamente.
- 🔴 **Perigo (Vermelho / Danger)**: Contém arquivos que exigem confirmação explícita (por exemplo, esvaziar permanentemente a Lixeira).
- **Regras personalizadas de lista de permissões (Whitelist)**:
  - Adicione caminhos específicos, extensões ou nomes de pastas que o ATBCmder **nunca** deve tocar em `~/.config/atbsys/whitelist`.
  - Regras integradas de proteção impedem automaticamente a verificação de arquivos críticos do sistema operacional macOS, diretórios das chaves de acesso do usuário (Keychain) e pastas de sincronização offline de armazenamento em nuvem.

---

## 6. Desinstalador de aplicativos (`cm_UninstallApp` / `⌘⇧U`)

No macOS, arrastar um aplicativo de `/Applications` para a Lixeira remove apenas o pacote `.app` em si. Aplicativos modernos frequentemente espalham centenas de arquivos auxiliares pela sua unidade: plists de preferências, bancos de dados do Application Support, agentes de inicialização (launch agents) em segundo plano, contêineres sandbox e mídias em cache. Com o tempo, esses resíduos órfãos consomem gigabytes de armazenamento e podem manter processos desnecessários em segundo plano sendo executados no início da sessão.

O **Desinstalador de aplicativos** (`cm_UninstallApp`, atalho **`⌘⇧U`** / **`Ctrl+Shift+U`**) oferece varredura profunda de dependências para erradicar completamente os aplicativos e seus resíduos associados.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             APPLICATION DEEP UNINSTALLER                               │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Filter: Docker                     ]  Found: 142 Applications (Total: 48.2 GB)       │
├──────────────────────────────────────┬─────────────────────────────────────────────────┤
│ INSTALLED APPLICATIONS               │ ASSOCIATED REMNANTS & SUPPORT FILES             │
│ App Name          Version    Size    │ File Path / Component               Size        │
│ ──────────────────────────────────── │ ─────────────────────────────────────────────── │
│ [X] Docker.app    4.28.0     1.8 GB  │ [X] /Applications/Docker.app        1.8 GB (.app│
│ [ ] Figma.app     116.15     240 MB  │ [X] ~/Library/Application Support/Docker 14.2 GB│
│ [ ] Slack.app     4.36.0     310 MB  │ [X] ~/Library/Caches/com.docker.docker   2.1 GB │
│ [ ] Visual Studio 1.87.0     450 MB  │ [X] ~/Library/Preferences/com.docker...  12 KB  │
│ [ ] Xcode.app     15.3      12.4 GB  │ [X] ~/Library/LaunchAgents/com.docker...  4 KB  │
│                                      │ [X] ~/Library/Containers/com.docker...  380 MB  │
├──────────────────────────────────────┴─────────────────────────────────────────────────┤
│ Mode: (•) Complete Uninstall (.app + remnants)     ( ) Remnants Only (clean orphans)   │
│ Total Selected for Removal: 18.48 GB across 6 items                                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Refresh Applications ]       [ Cancel ]              [ Uninstall Application (18.5G)│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 6.1 Locais de descoberta de resíduos

Ao procurar por componentes de aplicativos, o ATBCmder examina os seguintes locais padronizados dos subsistemas do macOS usando correspondência exata do identificador de pacote (Bundle ID):

1. **Pacote do aplicativo**: `/Applications/<Nome>.app` e `~/Applications/<Nome>.app`.
2. **Suporte a aplicativos (Application Support)**: `~/Library/Application Support/<Nome>` e `<BundleID>`.
3. **Caches de aplicativos**: `~/Library/Caches/<BundleID>`.
4. **Preferências e padrões (Preferences)**: `~/Library/Preferences/<BundleID>.plist`.
5. **Estado salvo (Saved State)**: `~/Library/Saved Application State/<BundleID>.savedState`.
6. **Launch Daemons e Agents**: `~/Library/LaunchAgents/<BundleID>.plist`.
7. **Contêineres de sandbox**: `~/Library/Containers/<BundleID>/` e `~/Library/Group Containers/`.
8. **Logs de aplicativos**: `~/Library/Logs/<Nome>/`.

### 6.2 Modos operacionais duplos

- **Desinstalação completa (padrão)**:
  - Destinado a remover um aplicativo instalado que está presente atualmente no seu Mac.
  - Exclui tanto o pacote executável `.app` de `/Applications` quanto todos os arquivos auxiliares de suporte associados em uma única ação atômica.
- **Apenas resíduos**:
  - Destinado a limpar arquivos remanescentes de aplicativos que foram excluídos anteriormente de forma manual pelo Finder ou por ferramentas de terceiros.
  - Examina `~/Library/` procurando pastas de suporte órfãs cujo pacote `.app` pai não esteja mais presente no sistema.

### 6.3 Integridade do sistema Apple e proteções de segurança

Para evitar a desestabilização acidental do sistema:

- **Proteção de aplicativos do sistema**: Aplicativos integrados do sistema macOS (Safari, Finder, Pré-Visualização, Música, Ajustes do Sistema, etc.) são protegidos com um ícone de cadeado somente leitura e não podem ser desinstalados.
- **Detecção de processos em execução**: Se um aplicativo ou seu daemon auxiliar estiver ativo no momento, o ATBCmder solicitará que você encerre o aplicativo normalmente antes que a desinstalação continue.
- **Protocolo de Lixeira primeiro**: Todos os itens desinstalados são movidos para a Lixeira do macOS por padrão, em vez de serem desvinculados imediatamente do disco, permitindo recuperação total se necessário.

---

## 7. Alertas do sistema e de manutenção

> [!NOTE]
> **Sobrecarga mínima de recursos do sistema**  
> O daemon de monitoramento de status em segundo plano é desenvolvido em código nativo compilado e é executado em um intervalo de sondagem de 1,0 segundo. Ele consome menos de 0,1% de CPU durante a navegação ativa de arquivos e suspende a sondagem automaticamente quando o ATBCmder é minimizado ou ocultado.

> [!TIP]
> **Como combinar o Analisador de uso de disco com a Visualização em árvore ramificada (Branch View)**  
> Se o Analisador de uso de disco sinalizar um diretório contendo milhares de arquivos temporários dispersos, selecione esse diretório e pressione **Mostrar no painel duplo**. Em seguida, pressione **`Cmd+B`** (`cm_DirBranch`) para nivelar toda a árvore aninhada em uma única lista onde você pode classificar, selecionar e excluir itens em lote com precisão do teclado.

> [!IMPORTANT]
> **Sempre revise as seleções do limpador antes de confirmar**  
> Embora o Limpador do sistema defina os caches como **Seguro (Verde)**, algumas ferramentas de desenvolvedor (como DerivedData do Xcode ou volumes locais do Docker) podem levar algum tempo para recompilar ou baixar dados novamente na próxima inicialização do projeto. Revise as categorias marcadas para garantir que não esteja limpando caches de uma sprint ativa.

> [!CAUTION]
> **Como forçar o encerramento de processos do sistema (`SIGKILL`)**  
> No Gerenciador de Processos do Status do Sistema, o envio do sinal `SIGKILL` (Forçar encerramento) interrompe o processo de destino imediatamente, sem permitir que ele descarregue buffers de arquivos abertos ou salve estados de documentos. Sempre tente um encerramento normal e seguro com `SIGTERM` primeiro.

> [!WARNING]
> **Remoção de contêineres sandbox de aplicativos**  
> Ao desinstalar aplicativos da Mac App Store, os arquivos auxiliares armazenados em `~/Library/Containers/<BundleID>` costumam incluir bancos de dados de documentos em sandbox. Certifique-se de ter exportado quaisquer arquivos de projeto locais essenciais antes de confirmar a exclusão do contêiner.

---

## 8. Tabela de referência mestra das ferramentas do sistema em matriz dupla

| Categoria | Descrição da ação | Atalho do macOS | Tecla Commander Clássica | ID do comando |
| :--- | :--- | :--- | :--- | :--- |
| **Monitor do sistema** | Abrir painel completo de diagnósticos do sistema | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` |
| **Monitor do sistema** | Abrir popover leve de status | Clicar na cápsula da barra de ferramentas | — | *(Ação da interface)* |
| **Monitor do sistema** | Filtrar lista do gerenciador de processos | `Cmd+F` (no painel) | `F7` | — |
| **Monitor do sistema** | Encerrar processo (`SIGTERM`) | `Delete` / `⌫` | `Delete` | — |
| **Monitor do sistema** | Forçar encerramento do processo (`SIGKILL`) | `Shift+Delete` / `⇧⌫` | `Shift+Delete` | — |
| **Analisador de disco** | Abrir caixa de diálogo do analisador de uso de disco | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` |
| **Analisador de disco** | Aprofundar na pasta selecionada | `Enter` / `Return` | `Enter` | — |
| **Analisador de disco** | Reduzir zoom para o diretório pai | `Backspace` / `⌫` | `Backspace` | — |
| **Analisador de disco** | Mover item destacado para o Lixo | `Cmd+Delete` / `⌘⌫` | `F8` / `Delete` | — |
| **Analisador de disco** | Mostrar item selecionado no painel duplo | `Cmd+Return` / `⌘⏎` | `Ctrl+Enter` | — |
| **Limpador do sistema** | Abrir caixa de diálogo segura do limpador do sistema | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` |
| **Limpador do sistema** | Executar varredura de simulação somente leitura | `Cmd+R` / `⌘R` | `Ctrl+R` | — |
| **Limpador do sistema** | Alternar seleção da categoria | `Espaço` | `Espaço` | — |
| **Desinstalador de apps** | Abrir desinstalador de aplicativos | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` |
| **Desinstalador de apps** | Mudar para o modo apenas resíduos | `Cmd+2` / `⌘2` | `Alt+2` | — |
| **Preferências** | Alternar exibição da cápsula HUD na barra de ferramentas | Preferências ➔ Geral | — | *(Configuração)* |

---

<div align="center">
  <p>Pronto para personalizar atalhos de teclado, visualizações de painel e comportamento do aplicativo?</p>
  <p><strong><a href="preferences_and_customization.md">Avançar para o Capítulo 8: Preferências e personalização &rarr;</a></strong></p>
</div>
