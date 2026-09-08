# Capítulo 5: Ferramentas avançadas e automação

No gerenciamento de arquivos de alto volume, a manipulação básica de arquivos – copiar, mover e excluir itens individuais – é apenas o começo. Engenheiros profissionais, administradores de sistemas, criadores de conteúdo e analistas de dados frequentemente enfrentam desafios operacionais complexos: reestruturar milhares de ativos digitais com nomes inconsistentes, isolar regressões sutis de código entre ramificações de lançamento paralelas, manter espelhos sincronizados em matrizes de armazenamento de rede, localizar arquivos de configuração profundamente enterrados e verificar criptograficamente a integridade dos arquivos. 

O ATBCmder transforma essas tarefas intensivas em mão-de-obra em operações rápidas e determinísticas. Em vez de exigir scripts de linha de comando externos, utilitários em lote de terceiros ou aplicativos de comparação autônomos e desajeitados, o ATBCmder integra um conjunto abrangente de automação diretamente em seu núcleo ortodoxo de painel duplo. Se você precisa executar substituições de expressões regulares em todo um arquivo de fotos, realizar uma sincronização de diretório bidirecional com hash de nível de conteúdo ou alimentar resultados de pesquisa com vários filtros em um espaço de trabalho virtual, o ATBCmder fornece as ferramentas necessárias com total eficiência de teclado. 

---

## 1. Guia de início rápido visual: o mecanismo de automação e a matriz de comando

ATBCmder divide ferramentas elétricas e automação em seis domínios funcionais especializados que interagem perfeitamente com a interface de painel duplo: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                DUAL FILE PANELS                                        │
│     Left Panel (Source / Directory A)        Right Panel (Target / Directory B)        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Batch Multi-Rename (Ctrl+M)         │  [2] Side-by-Side File Diff (Meta+Shift+F12)│
│      Tokens, RegEx, Counters, Preview    │      Line highlights, Hunk sync, In-place   │
│                                          │                                             │
│  [3] Directory Sync (Shift+F12)          │  [4] Advanced Search (Alt+F7)               │
│      Content/Date compare, Asym mirror   │      Spotlight / Deep scan ➔ Feed to Listbox│
│                                          │                                             │
│  [5] Semantic Command Bar (/)            │  [6] File Utilities & Security              │
│      Spotlight queries, AI intent, NLP   │      Split/Link, Checksum, Wipe (Alt+Del)   │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Feed to Listbox] ➔ Populates virtual panel tab for bulk operations across directories│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Folha de dicas de automação de matriz dupla

| Ação | Atalho do macOS | Chave do Comandante Clássico | ID do comando | Descrição | 
| :--- | :--- | :--- | :--- | :--- | 
| **Renomeação múltipla em lote** | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | Abre a caixa de diálogo da ferramenta Renomeação múltipla em lote. | 
| **Diferença de arquivo lado a lado** | `Meta+Shift+F12` / `⌘⇧F12` | `Meta+Shift+F12` | `cm_FileDiff` / `cm_CompareFiles` | Compara dois arquivos selecionados lado a lado (`Shift+F3` para `cm_CompareContents`). | 
| **Sincronizar diretório** | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | Compara e sincroniza diretórios de painel duplo. | 
| **Pesquisa avançada de arquivos** | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` / `cm_FileSearch` | Abre a caixa de diálogo de pesquisa de vários filtros. | 
| **Pesquisa rápida do Spotlight** | `Ctrl+Shift+F` / `⌃⇧F` | `Ctrl+Shift+F` | *(Menu Comandos)* | Inicia a pesquisa instantânea de metadados do Spotlight. | 
| **Entrada de Comando Semântico**| `/` | `/` | `cm_VisSemanticCommand` | Ativa a barra de comandos de linguagem natural incorporada. | 
| **Dividir arquivo grande** | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | Divide arquivos grandes em partes numeradas. | 
| **Combinar arquivos divididos** | Menu: Arquivos ➔ Combinar Arquivos | — | `cm_FileLinker` / `cm_Combine` | Remonta pedaços `.001`, `.002` em um único arquivo. | 
| **Calcular soma de verificação** | `Ctrl+X` / `⌃X` | `Ctrl+X` | `cm_CheckSumCalc` / `cm_CalculateChecksum` | Calcula hashes MD5, SHA-1, SHA-256 ou SHA-512. | 
| **Verificar arquivo de soma de verificação** | Menu Ferramentas | — | `cm_CheckSumVerify` / `cm_VerifyChecksum` | Verifica arquivos em relação a `.md5`, `.sha256` ou `.sfv`. | 
| **Limpeza segura (fragmentar)** | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | Substitui e exclui arquivos com segurança. | 
| **Execute o Terminal do Sistema** | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` | Gera o Terminal macOS no caminho do painel atual. | 

---

## 2. Ferramenta de multi-renomeação em lote (`Ctrl+M` / `⌃M` / `cm_MultiRename`)

Renomear dezenas ou centenas de arquivos manualmente é tedioso e sujeito a erros. A **Ferramenta de Multi-Renomeação em Lote** (`cm_MultiRename`, mapeada para `fmultirename.pas` na arquitetura clássica) permite definir padrões de nomenclatura flexíveis, aplicar contadores de sequência dinâmicos, realizar conversões de caso e executar poderosas regras de localização e substituição de Expressão Regular (RegEx) com garantias de segurança visual em tempo real. 

![Batch Multi-Rename Tool](images/multi_rename_dialog.png) 
*Figura 5.1: Ferramenta de multi-renomeação em lote com visualização ao vivo de linhas, máscaras de token, parâmetros de contador numérico e detecção de duplicatas.*

### 2.1 O fluxo de trabalho de múltiplas renomeações

1. **Selecionar arquivos**: No painel de arquivos ativos, selecione os arquivos ou diretórios que deseja renomear usando `Space`, `Insert` ou seleção curinga (`+`). Se nada for selecionado, o item sob o cursor será usado. 
2. **Iniciar Ferramenta**: Pressione **`Ctrl+M`** (`⌃M`) ou escolha **Arquivos ➔ Ferramenta Multi-Renomear...** na barra de menu. 
3. **Configurar modelos e regras**: insira máscaras de nome de arquivo/extensão, defina opções de contador ou defina strings para localizar e substituir. 
4. **Inspecionar visualização ao vivo**: a tabela de 3 colunas (`Old Name`, `New Name`, `Directory`) é atualizada instantaneamente a cada pressionamento de tecla. 
5. **Executar**: Clique em **Iniciar Renomear** (ou pressione `Enter`). ATBCmder executa as renomeações atomicamente e atualiza os painéis de arquivos. 

---

### 2.2 Tokens de modelo e divisão de intervalo

ATBCmder usa tokens entre colchetes intuitivos para fazer referência a partes dos metadados do arquivo original: 

| Ficha | Descrição | Exemplo de entrada | Valor resultante | 
| :--- | :--- | :--- | :--- | 
| **`[N]`** | Nome do arquivo original sem extensão | `report_2026.pdf` | `report_2026` | 
| **`[E]`** | Extensão do arquivo original (sem ponto) | `archive.tar.gz` | `gz` | 
| **`[C]`** | Contador numérico sequencial | *(Arquivo 3 na lista)* | `003` (depende da configuração dos dígitos) | 
| **`[Y]`** | Ano de modificação do arquivo com 4 dígitos | `2026-09-06` | `2026` | 
| **`[M]`** | Mês de modificação do arquivo com 2 dígitos | `September` | `09` | 
| **`[D]`** | Dia da modificação do arquivo com 2 dígitos | `6th` | `06` | 
| **`[h]`** | Hora de 2 dígitos (relógio de 24 horas) | `14:30:15` | `14` | 
| **`[m]`** | Minuto de 2 dígitos | `14:30:15` | `30` | 
| **`[s]`** | Segundo de 2 dígitos | `14:30:15` | `15` |

#### Fatiamento de intervalo de caracteres (`[Na-b]` / `[Ea-b]`)

Você pode extrair intervalos de caracteres específicos do nome ou extensão original usando fatiamento de índice baseado em 1: 

- **`[N1-4]`**: Extrai os 4 primeiros caracteres do nome. Para `Document_Final.txt`, isso produz `Docu`. 
- **`[N5-]`**: Extrai do 5º caractere até o final do nome. Para `DSC_0982.jpg`, isso produz `0982`. 
- **`[N-5]`**: Extrai até o 5º caractere. 
- **`[E1-2]`**: Extrai os 2 primeiros caracteres da extensão. Para `archive.html`, isso produz `ht`. 

---

### 2.3 Controles de contador e sequências numéricas

O grupo **Configurações do contador** permite controle granular sobre a indexação numérica: 

- **Iniciar em**: O número inteiro inicial para a sequência do contador (padrão: `1`). 
- **Etapa**: O valor de incremento adicionado para cada arquivo subsequente (padrão: `1`). Definir Step como `2` gera `1, 3, 5, 7...`. 
- **Dígitos**: A largura do preenchimento de zeros (intervalo: `1` a `10`). Definir dígitos como `3` formata números como `001`, `002`, `003`. Definir dígitos como `1` desativa zeros à esquerda (`1`, `2`, `3`). 

---

### 2.4 Localizar e Substituir e Expressões Regulares

O grupo **Localizar e Substituir** permite substituições de texto em todos os itens selecionados: 

- **Localizar**: substring de destino ou padrão de expressão regular. 
- **Substituir por**: String de substituição. Quando RegEx está habilitado, as referências anteriores (`$1`, `$2` ou `\1`, `\2`) referem-se a grupos de captura. 
- **Usar expressões regulares (Regex)**: Alterna a análise de expressões regulares da biblioteca padrão do Python. 
- **Diferenciar maiúsculas de minúsculas**: quando desmarcada, a correspondência ignora maiúsculas e minúsculas (por exemplo, correspondência de `.JPG` e `.jpg`).

#### Exemplos poderosos de substituição de RegEx

```
Example 1: Strip unwanted tracking or release tags from filenames
Input File:      Album_Artist_-_Track_01_[Lossless_24bit_96kHz].flac
Find Pattern:    \s*\[.*?\]
Replace with:    (leave empty)
Output File:     Album_Artist_-_Track_01.flac

Example 2: Reorder dates from YYYY-MM-DD to DD-MM-YYYY
Input File:      Invoice_2026-09-06_Acme.pdf
Find Pattern:    (\d{4})-(\d{2})-(\d{2})
Replace with:    $3-$2-$1
Output File:     Invoice_06-09-2026_Acme.pdf

Example 3: Convert spaces and underscores to standardized hyphens
Input File:      my new blog post_draft.md
Find Pattern:    [ _]+
Replace with:    -
Output File:     my-new-blog-post-draft.md
```
 

---

### 2.5 Modos de conversão de caso

ATBCmder fornece normalização instantânea de revestimento sem exigir padrões complexos: 

- **Sem alteração**: preserva a capitalização original. 
- **minúsculas**: Converte todo o nome do arquivo e extensão em minúsculas (`PHOTO_001.JPG` ➔ `photo_001.jpg`). 
- **MAIÚSCULAS**: Converte todos os caracteres para letras maiúsculas (`readme.txt` ➔ `README.TXT`). 
- **Primeira letra maiúscula**: Coloca em maiúscula o caractere inicial de cada palavra (`war and peace.epub` ➔ `War And Peace.epub`). 

---

### 2.6 Grade de visualização ao vivo e proteção contra colisão

Renomear centenas de arquivos sem pré-visualização pode resultar em substituições desastrosas de dados. ATBCmder implementa uma **Arquitetura de Segurança com Zero Acidentes**: 

1. **Visualização instantânea do Debounce**: À medida que você digita nas entradas do modelo ou ajusta as caixas giratórias, a tabela calcula imediatamente os nomes dos arquivos resultantes. 
2. **Detecção de alvo duplicado**: ATBCmder verifica todos os nomes de arquivos de saída computados dentro da pasta de destino. Se dois ou mais arquivos resolverem exatamente o mesmo nome ou se um nome de arquivo resolver uma string vazia: 
- As linhas em colisão são imediatamente destacadas em vermelho proeminente (`#FFEBEB` / `#D70000` no modo claro, `#4A1515` / `#FF8080` no modo escuro). 
- O botão **Iniciar Renomeação** é automaticamente **desativado**. 
- Uma dica avisa: *"Colisões de nomes detectadas. Resolva duplicatas antes de renomear."* 
3. **Autorização de colisão**: depois de ajustar seu contador, modelo ou regex para tornar todos os nomes de arquivos de destino exclusivos, o aviso é apagado e o botão **Iniciar renomeação** é reativado. 

---

### 2.7 Receitas práticas passo a passo

#### Receita A: renomeando fotos de câmeras digitais com carimbos de data e hora

Transforme nomes de câmeras criptografadas (`IMG_4092.JPG`, `IMG_4093.JPG`) em ativos organizados cronologicamente: 

1. Selecione os arquivos de fotos e pressione **`Ctrl+M`**. 
2. Defina **Modelo de nome de arquivo** como: `Photo_[Y][M][D]_[C]`. 
3. Defina **Modelo de extensão** como: `[E]`. 
4. Defina **Dígitos** como `3`, **Iniciar em** como `1`. 
5. Defina **Conversão de caso** como `lowercase`. 
6. Visualize o resultado: `photo_20260906_001.jpg`, `photo_20260906_002.jpg`. 
7. Pressione `Enter` para aplicar.

#### Receita B: Adicionar um prefixo preservando o nome e a extensão

Prefixe um lote de documentos com um código de projeto: 

1. Selecione os documentos e pressione **`Ctrl+M`**. 
2. Em **Modelo de nome de arquivo**, insira: `PRJ-ALPHA_[N]`. 
3. Deixe **Modelo de extensão** como `[E]`. 
4. Clique em **Iniciar renomeação**. 

---

## 3. Diferença de arquivo visual lado a lado (`Meta+Shift+F12` / `⌘⇧F12` / `cm_FileDiff`)

Detectar diferenças entre revisões de configuração, arquivos de código-fonte ou despejos de dados é uma tarefa diária para usuários avançados. O ATBCmder inclui um **Visual File Diff Viewer** (`DiffViewerDialog`) integrado lado a lado que elimina a necessidade de iniciar ferramentas externas pesadas. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Side-by-side Diff: config.py (Left)  vs.  config.py.new (Right)                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [💾 Save Left] [💾 Save Right] | [Copy to Right →] [← Copy to Left] | [Prev] [Next]    │
│ [🔄 Re-compare] | [✔] Ignore whitespace  [ ] Ignore case  [ ] Ignore blank lines       │
├─────────────────────────────────────────────┬──────────────────────────────────────────┤
│ config.py (Left)                            │ config.py.new (Right)                    │
├─────────────────────────────────────────────┼──────────────────────────────────────────┤
│ 12: DEBUG = False                           │ 12: DEBUG = False                        │
│ 13: LOG_LEVEL = "INFO"                      │ 13: LOG_LEVEL = "DEBUG"      [CHANGED]   │
│ 14: PORT = 8080                             │ 14: PORT = 8080                          │
│ 15: # Deprecated database setting           │ 15:                                      │
│ 16: DB_TIMEOUT = 30              [REMOVED]  │ 16: DB_TIMEOUT = 10          [CHANGED]   │
│ 17:                                         │ 17: SSL_ENABLED = True       [ADDED]     │
├─────────────────────────────────────────────┴──────────────────────────────────────────┤
│  Difference 2 of 4  │  Ln 16, Col 1 (Left)  │  Ln 16, Col 1 (Right)                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Iniciando comparação de arquivos

- **Comparar dois arquivos selecionados**: Em um único painel, selecione exatamente dois arquivos e pressione **`Meta+Shift+F12`** (`⌘⇧F12`) ou escolha **Comandos ➔ Comparar por conteúdo...**. 
- **Comparar arquivos opostos**: destaque um arquivo no painel esquerdo, destaque o arquivo correspondente no painel direito e acione `cm_CompareContents`. 
- **Comandos suportados**: `cm_CompareContents`, `cm_FileDiff` e `cm_CompareByContent` todos roteados para o mecanismo de comparação lado a lado. 

---

### 3.2 Destaque de diferenças visuais e códigos de cores

O mecanismo diff analisa o texto linha por linha usando um algoritmo Hunt-Szymanski LCS otimizado (`TextDiffer`), dividindo as diferenças em pedaços codificados por cores: 

| Tipo de diferença | Destaque de tema claro | Destaque de tema escuro | Descrição | 
| :--- | :--- | :--- | :--- | 
| **Linhas adicionadas** | Esmeralda Suave (`#e6ffed`) | Verde Floresta Escuro (`#234b2d`) | Linhas presentes apenas no arquivo Right. | 
| **Linhas removidas** | Carmesim Suave (`#ffeef0`) | Vermelho Carmesim Escuro (`#552328`) | Linhas presentes no arquivo Esquerdo, mas ausentes no arquivo Direito. | 
| **Linhas alteradas** | Âmbar suave (`#fff5b1`) | Ouro âmbar escuro (`#50461e`) | Linhas modificadas entre as versões Esquerda e Direita. | 
| **Pedaço Ativo** | Sombra de contraste vívido | Sombra de contraste vívido | O bloco de diferença atualmente focado pelo cursor. | 

Cada painel apresenta uma medianiz esquerda dedicada (`LineNumberArea`) exibindo números de linha baseados em 1 sincronizados com posições diferentes. 

---

### 3.3 Rolagem sincronizada e segurança de reentrada

Ao comparar arquivos de origem longos contendo milhares de linhas, navegar pelo código requer coordenação passo a passo: 

- Rolar a barra de rolagem vertical ou horizontal de qualquer editor ajusta instantaneamente o editor oposto pelo deslocamento de pixel idêntico. 
- ATBCmder implementa um **bloqueio de reentrada** interno (`_syncing_vscroll`, `_syncing_hscroll`) evitando loops de feedback de eventos, gagueira ou desvio do cursor. 

---

### 3.4 Navegação Hunk e Mesclagem Bidirecional

Você pode navegar pelas diferenças sem usar o mouse: 

- **Próxima diferença**: Pressione **`Alt+Down`** / `⌥↓` (ou `Ctrl+Down`). 
- **Diferença anterior**: Pressione **`Alt+Up`** / `⌥↑` (ou `Ctrl+Up`). 
- **Pular para o pedaço**: clicar diretamente em qualquer linha destacada em qualquer painel define automaticamente esse pedaço como ativo.

#### Mesclagem bidirecional (compatibilidade com Vimdiff `dp` / `do`)

Mesclar diferenças entre arquivos com pressionamentos de tecla únicos: 

- **Copiar da esquerda para a direita (`→`)**: Pressione **`Alt+Right`** / `⌥→` (ou `Ctrl+Alt+Right` ou Vimdiff `dp` via **`Alt+P`**). O pedaço ativo no editor Esquerdo substitui a seção correspondente no editor Direito. 
- **Copiar da direita para a esquerda (`←`)**: Pressione **`Alt+Left`** / `⌥←` (ou `Ctrl+Alt+Left` ou Vimdiff `do` via **`Alt+O`**). O pedaço ativo no editor Direito substitui a seção correspondente no editor Esquerdo. 

---

### 3.5 Edição no local e salvamento atômico

Ao contrário dos visualizadores de diferenças que tratam o texto como somente leitura, ambos os painéis no ATBCmder são editores de código totalmente funcionais: 

- Digite, cole ou exclua texto diretamente em qualquer um dos editores. 
- Sempre que as edições manuais alterarem as linhas, pressione **`F5`** (ou `Ctrl+R`) para executar novamente o cálculo da diferença nos buffers atualizados. 
- Salvar arquivo esquerdo: Clique em **💾 Salvar esquerdo** (ou pressione `Cmd+S` / `Ctrl+S` enquanto o editor esquerdo estiver em foco). 
- Salvar arquivo direito: Clique em **💾 Salvar direito** (ou pressione `Cmd+S` / `Ctrl+S` enquanto o editor direito estiver em foco). 

---

### 3.6 Opções de filtragem de comparação

A barra de ferramentas do visualizador de diferenças permite isolar alterações lógicas genuínas do ruído de formatação: 

- **Ignorar espaços em branco (`_cb_ws`)**: ignora alterações em tabulações, espaços à direita e recuo de espaços versus tabulações. 
- **Ignorar maiúsculas e minúsculas (`_cb_case`)**: Executa comparações de caracteres que não diferenciam maiúsculas de minúsculas. 
- **Ignorar linhas em branco (`_cb_blank`)**: Recolhe adições e exclusões de linhas vazias, concentrando-se estritamente em alterações substantivas de código. 

---

### 3.7 Detecção de diferença de arquivo binário

Se qualquer arquivo selecionado para comparação contiver bytes nulos ou assinaturas MIME binárias (por exemplo, imagens, executáveis, arquivos compilados), o ATBCmder invoca automaticamente `BinaryDiffer`: 

- Exibe tamanhos de arquivo e hashes criptográficos SHA-256 lado a lado. 
- Indica claramente se os arquivos binários são idênticos em bytes ou divergentes. 

---

## 4. Sincronização de diretório (`Shift+F12` / `⇧F12` / `cm_SyncDirs`)

Manter as árvores de diretórios sincronizadas em discos locais, unidades de backup e armazenamento em rede é a base de sistemas confiáveis. O **Sincronizador de diretórios** do ATBCmder (`SyncDirsDialog`, mapeado para `fsyncdirsdlg.pas`) compara hierarquias de pastas inteiras, determina operações direcionais exatas e visualiza cada cópia e exclusão de arquivo antes de tocar em seu armazenamento. 

![Directory Synchronization](images/folder_synchronization.png) 
*Figura 5.2: Caixa de diálogo Sincronização de diretórios exibindo status de comparação recursiva, setas de sincronização direcionais e controles de espelho assimétricos.*

### 4.1 Iniciando a sincronização de diretório

1. Abra o **Diretório de origem** no painel esquerdo e o **Diretório de destino** no painel direito. 
2. Pressione **`Shift+F12`** (`⇧F12`) ou escolha **Comandos ➔ Sincronizar Dirs...**. 
3. A caixa de diálogo Sincronizar diretórios aparece com ambos os caminhos pré-preenchidos nos cartões de cabeçalho. 

---

### 4.2 Métodos de comparação e precisão

Antes de sincronizar, configure seus critérios de comparação no cartão **Configurações de sincronização**: 

| Configuração | Padrão | Descrição | 
| :--- | :--- | :--- | 
| **Comparar subdiretórios** | `Enabled` | Percorre recursivamente todos os diretórios aninhados. | 
| **Comparar por conteúdo** | `Disabled` | Lê e verifica os bytes do arquivo diretamente usando `filecmp.cmp`. Garante 100% de precisão para arquivos com carimbos de data/hora idênticos, mas com dados modificados. | 
| **Ignorar data** | `Disabled` | Compara arquivos exclusivamente por tamanho de byte, ignorando os carimbos de data e hora de modificação do sistema de arquivos. | 
| **Tolerância de carimbo de data/hora FAT/SMB** | `2.0 sec` | Considera automaticamente resoluções de carimbo de data/hora FAT/FAT32/exFAT de 2 segundos, evitando falsos sinalizadores de incompatibilidade ao sincronizar entre macOS e unidades externas. | 

---

### 4.3 Análise Direcional e Indicadores de Status

Clique em **Comparar** para iniciar um trabalhador de comparação em segundo plano sem bloqueio (`SyncCompareWorker`). A tabela de comparação é preenchida com linhas direcionais codificadas por cores: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Relative Path             │ Operation │ Reason            │ Details                    │
├───────────────────────────┼───────────┼───────────────────┼────────────────────────────┤
│ assets/banner.png         │    ->     │ Left is newer     │ 2026-09-06 > 2026-08-15    │
│ docs/manual.pdf           │    ->     │ Right missing     │ File exists only on left   │
│ config/settings.json      │    <-     │ Right is newer    │ 2026-09-06 > 2026-09-01    │
│ vendor/legacy_lib.so      │    <-     │ Left missing      │ File exists only on right  │
│ build/cache.db            │    !=     │ Conflict          │ Timestamp / type mismatch  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

- **`->` (da esquerda para a direita)**: O arquivo à esquerda é mais recente ou existe apenas à esquerda. Ação padrão: copiar para a direita. 
- **`<-` (da direita para a esquerda)**: O arquivo da direita é mais recente ou existe apenas na direita. Ação padrão: copiar para a esquerda (no modo bidirecional). 
- **`=` (Igual)**: Os arquivos correspondem em tamanho e carimbo de data/hora/conteúdo. Filtrado da lista de sincronização ativa para economizar tempo. 
- **`!=` (Conflito)**: Colisão incompatível entre diretório e arquivo ou conflito de carimbo de data/hora insolúvel. Ignorado durante a sincronização em massa automatizada para segurança dos dados. 

---

### 4.4 Espelhamento Assimétrico vs. Sincronização Simétrica Bidirecional

ATBCmder suporta duas filosofias de sincronização fundamentalmente diferentes:

#### 1. Sincronização simétrica bidirecional (padrão)

- **Objetivo**: Alinhar os dois diretórios para que ambos tenham as versões mais recentes de cada arquivo. 
- **Ação**: Arquivos marcados como `->` são copiados para a esquerda ➔ para a direita. Arquivos marcados como `<-` são copiados para a direita ➔ para a esquerda. 
- **Segurança**: Nenhum arquivo é excluído em nenhum dos lados.

#### 2. Espelhamento assimétrico (`Asymmetric` caixa de seleção habilitada)

- **Objetivo**: Tornar o diretório Direito uma réplica exata e idêntica do diretório Esquerdo. 
- **Ação**: Arquivos marcados como `->` são copiados para a esquerda ➔ para a direita. Arquivos à Direita que *não* existem à Esquerda (`<- Right missing on Left`) são **removidos permanentemente do diretório Direita**. 
- **Caso de uso**: Criação de espelhos de backup originais em discos de backup externos ou compartilhamentos NAS. 

---

### 4.5 Registro de Segurança e Auditoria Pré-Execução

- **Inspecionar antes de sincronizar**: revise a tabela preenchida com cuidado. Você pode ver os caminhos relativos exatos e os motivos operacionais de cada transferência. 
- **Parar controle**: se um grande trabalho de comparação ou sincronização precisar ser abortado, clique em **Parar**. O thread em segundo plano termina com segurança sem deixar arquivos parciais corrompidos. 
- **Log de auditoria automatizado**: cada cópia, substituição e exclusão executada durante a sincronização é registrada no **Log de operações** interno do ATBCmder (`LogCategory.COPY_MOVE_LINK`, `LogCategory.DELETE`). 

---

## 5. Pesquisa avançada de arquivos e alimentação para caixa de listagem (`Alt+F7` / `⌥F7` / `cm_Search`)

Localizar arquivos específicos em estruturas de pastas aninhadas é um gargalo administrativo comum. ATBCmder fornece uma caixa de diálogo de pesquisa avançada de arquivos ** de alto desempenho (`SearchDialog`, mapeada para `fFindDlg.pas`), combinando indexação nativa do macOS Spotlight com um mecanismo de verificação profunda do sistema de arquivos e o recurso indispensável **Feed to Listbox**. 

![Advanced File Search](images/advanced_search_dialog.png) 
*Figura 5.3: Caixa de diálogo Pesquisa avançada de arquivos com parâmetros de vários filtros, controles de varredura profunda e o botão Feed to Listbox.*

### 5.1 Iniciando a pesquisa

- Pressione **`Alt+F7`** (`⌥F7`) em qualquer painel ou escolha **Comandos ➔ Pesquisar arquivos...**. 
- A caixa de diálogo de pesquisa é aberta com o campo **Pesquisar no diretório** pré-preenchido com o caminho atual do painel ativo. 

---

### 5.2 Back-ends de pesquisa dupla: Spotlight vs. Deep Scan

ATBCmder apresenta dois mecanismos de pesquisa especializados: 

```
                  ┌───────────────────────────────────────────────┐
                  │          Search Query Triggered               │
                  └───────────────────────┬───────────────────────┘
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
    ┌───────────────────────────┐                   ┌───────────────────────────┐
    │  Spotlight Engine         │                   │  Deep Scan Engine         │
    │  (SpotlightSearchWorker)  │                   │  (DeepScanWorker)         │
    ├───────────────────────────┤                   ├───────────────────────────┤
    │ • Uses macOS mdfind       │                   │ • Recursive os.scandir    │
    │ • Millisecond results     │                   │ • Scans unindexed drives  │
    │ • APFS metadata indexed   │                   │ • Network shares (SMB/NFS)│
    │ • Standard local storage  │                   │ • Raw text/regex parsing  │
    └───────────────────────────┘                   └───────────────────────────┘
```
 

1. **Mecanismo de pesquisa Spotlight (`SpotlightSearchWorker`)**: no macOS, clicar em **Iniciar pesquisa** (ou pressionar `Enter`) utiliza o índice de metadados Spotlight do sistema (`mdfind`). Ele recupera milhares de caminhos correspondentes em gigabytes de armazenamento em uma fração de segundo. 
2. **Deep Scan Engine (`DeepScanWorker`)**: Clicar em **Deep Scan** ignora a indexação do sistema e executa uma travessia direta e recursiva do sistema de arquivos. Isso é essencial ao pesquisar: 
- Unidades USB externas ou cartões SD com indexação Spotlight desativada. 
- Compartilhamentos remotos de arquivos em rede (SMB, SFTP, FTP, WebDAV). 
- Diretórios de compilação do desenvolvedor excluídos por meio de `.metadata_never_index`. 

---

### 5.3 Critérios de pesquisa multifiltro

Ajuste as consultas de pesquisa usando parâmetros granulares nos grupos **Geral** e **Filtros Avançados**: 

- **Padrão de nomes de arquivos**: 
- *Cartões curinga*: curingas de shell padrão, como `*.py`, `invoice_2026_*.pdf` ou `test_??.go`. 
- *Substrings*: Digitar `draft` encontra qualquer arquivo ou pasta contendo "rascunho". 
- *Expressões regulares*: marque **Expressão regular** para ativar a sintaxe regex completa (por exemplo, `^v\d+\.\d+\.(json|xml)$`). 
- **Pesquisa por texto (pesquisa no arquivo)**: 
- Pesquisa conteúdo de string UTF-8 e ASCII em texto, código-fonte e arquivos de documentos. 
- Verifique **Pesquisa de conteúdo com distinção entre maiúsculas e minúsculas** para correspondências exatas de maiúsculas e minúsculas. 
- **Faixa de tamanho de arquivo**: 
- Defina **Tamanho mínimo** e **Tamanho máximo** em quilobytes (`KB`). Definir o tamanho máximo como `0` deixa os limites superiores ilimitados. 
- **Período**: 
- Especifique **Modificado nos últimos N dias** (por exemplo, `7` dias para encontrar trabalho da semana anterior). 

---

### 5.4 Inspeção rápida nos resultados da pesquisa

Ao navegar pelos resultados da pesquisa na lista de resultados: 

- **Ver arquivo (`F3`)**: Abre instantaneamente o resultado da pesquisa destacado no Universal Lister. 
- **Editar Arquivo (`F4`)**: Abre o arquivo diretamente no Editor de Texto integrado. 
- **Ir para Arquivo (`Enter` / `Go to File`)**: Fecha a caixa de diálogo de pesquisa, navega no painel principal até o diretório pai do arquivo e coloca o cursor diretamente no arquivo. 

---

### 5.5 O poder do “Feed to Listbox”

O recurso mais transformador dos gerenciadores de arquivos ortodoxos é **Feed to Listbox**: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ SEARCH RESULTS (Flat Virtual Panel Tab)             OPPOSING PANEL (Destination)       │
│ [Search: *.log modified < 30 days]                 /Volumes/ArchiveStorage/Logs        │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Name                         Size   Folder  │   │  Name                        Size   │
│  ▸ [..]                              --:--   │   │  ▸ [..]                             │
│  ✔ app_server.log            14 MB   /var/log│ C │  ▸ archive_2025             <DIR>   │
│  ✔ auth_audit.log             2 MB   /etc/sec│ O │                                     │
│  ✔ worker_3.log              88 KB   /opt/app│ P │                                     │
│  ● access.log               512 KB   /var/log│ Y │                                     │
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [3 items selected] ➔ Press F5 to copy all matching files into destination folder!     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

1. Na caixa de diálogo Pesquisar, quando os arquivos correspondentes forem encontrados, clique no botão **Feed to listbox**. 
2. ATBCmder fecha a caixa de diálogo e abre uma nova **guia de resultados de pesquisa virtual** no painel ativo. 
3. Em vez de navegar para cada pasta individualmente, todos os arquivos correspondentes de diferentes profundidades de diretório aparecem em uma única tabela plana. 
4. **Executar qualquer ação do comandante**: 
- Selecione todos ou itens específicos (`Space`, `+`, `Cmd+A`). 
- **Copiar (`F5`)** ou **Mover (`F6`)** arquivos correspondentes em diversas pastas para uma única pasta de destino no painel oposto. 
- **Renomeação múltipla em lote (`Ctrl+M`)** todos os resultados de pesquisa correspondentes simultaneamente. 
- **Exclua com segurança (`F8` ou `Alt+Delete`)** arquivos temporários indesejados em toda a hierarquia do projeto de uma só vez. 

---

## 6. Integração Spotlight e sistema de comando semântico (`/` e `Ctrl+Shift+F`)

Os fluxos de trabalho modernos exigem consultas ágeis, além de diálogos de filtros rígidos. ATBCmder integra a indexação do macOS Spotlight diretamente com um **Sistema de Comando Semântico de Linguagem Natural** acessível na barra de comando incorporada na parte inferior da janela principal. 

![Semantic Command Bar](images/semantic_command.png) 
*Figura 5.4: A barra de comando semântica analisando uma consulta em linguagem natural com modelos de preenchimento automático em tempo real.* 

![Semantic Search](images/semantic_search_bar.png) 
*Figura 5.5: Resultados da Pesquisa Semântica exibidos diretamente dentro do painel ativo.*

### 6.1 Ativando Comandos Semânticos

- **Pressione `/`**: No painel de arquivos ativo, basta pressionar a tecla de barra (`/`). ATBCmder concentra imediatamente a barra de edição de comando inferior, preenchendo-a previamente com `/`. 
- **Atalho de pesquisa do Spotlight**: pressione **`Ctrl+Shift+F`** (`⌃⇧F`) ou `Cmd+Shift+F` para abrir a interface do filtro semântico. 
- **Dispensar**: pressione `Escape` para limpar o filtro e restaurar a listagem de diretório padrão. 

---

### 6.2 Escopos: Local (`/`) vs. Global (`//`)

ATBCmder diferencia entre filtragem em nível de pasta e descoberta em todo o sistema usando convenções de prefixo:

#### 1. Escopo do diretório local (`/<query>`)

Consultas que começam com uma única barra operam exclusivamente no diretório aberto no painel ativo (e em suas subpastas se opções recursivas forem especificadas): 

- `/larger than 10MB`: Mostra apenas arquivos maiores que 10 Megabytes na pasta atual. 
- `/> 50MB`: Abreviação numérica para filtragem de tamanho. 
- `/today modified pdf`: Filtros para documentos PDF modificados nas últimas 24 horas. 
- `/images`: Exibe apenas formatos de imagem raster e vetorial. 
- `/source code`: Mostra Python, C++, Rust, Go, JavaScript e outros arquivos de origem. 
- `/contains "API_KEY"`: Filtros para arquivos de texto contendo a string "API_KEY". 
- `/hide *.log`: Oculta arquivos de log da exibição ativa.

#### 2. Escopo Global do Sistema (`//<query>`)

Consultas que começam com uma barra dupla consultam todo o volume do sistema macOS via Spotlight: 

- `//today modified pdf`: Encontra todos os documentos PDF modificados hoje em todo o seu Mac. 
- `//larger than 1GB dmg`: localiza todos os instaladores de imagem de disco que excedem 1 GB. 
- `//code contains "OAuth2Handler"`: Encontra todos os arquivos de origem em todo o sistema contendo "OAuth2Handler". 

---

### 6.3 Consultas semânticas assistidas por IA (`?` ou `/?`)

Quando configurado com um provedor de IA (Google Gemini, OpenAI, Anthropic Claude ou Ollama local) em *Preferências ➔ Filtro Semântico*: 

- Prefixar uma consulta com `?` ou `/?` roteia a instrução de linguagem natural por meio de um analisador LLM. 
- Exemplo: `/? find all final invoices sent to client Acme last quarter over $5000` 
- A IA traduz frases humanas complexas em atributos precisos de metadados do Spotlight (`kMDItemFSSize`, `kMDItemContentModificationDate`, `kMDItemTextContent`), exibindo arquivos correspondentes instantaneamente no painel. 

---

### 6.4 Preenchimento Automático, Catálogo (`/help`) e Histórico (`/history`)

Conforme você digita na caixa de edição do comando semântico: 

- **Popup de conclusão interativa**: um menu suspenso (`SemanticCompletionPopup`) exibe sugestões de modelos contextuais com base no catálogo integrado (`semantic-command-templates.xml`). Use as setas `Down` e `Up` para destacar sugestões e pressione `Tab` ou `Enter` para aceitar. 
- **Catálogo de Ajuda (`/help`)**: digitar `/help` abre a **Caixa de diálogo de Ajuda do Comando Semântico**, listando dezenas de exemplos pesquisáveis ​​em categorias (Tamanho, Data, Tipo de arquivo, Conteúdo, Marcação). Clicar duas vezes em qualquer entrada a insere na linha de comando. 
- **Histórico de comandos (`/history`)**: Digitar `/history` exibe um registro cronológico de todos os comandos semânticos executados anteriormente com carimbos de data e hora de execução, permitindo recuperação instantânea. 

---

### 6.5 Modificadores de ação do painel instantâneo

A barra de comando semântica também pode manipular as seleções e classificação do painel sem tocar no mouse: 

| Comando Semântico | Ação executada | 
| :--- | :--- | 
| `/select all visible` | Seleciona todos os itens exibidos atualmente após a filtragem. | 
| `/clear selection` | Desmarca todos os itens no painel. | 
| `/invert selection` | Inverte o estado atual de seleção de arquivo. | 
| `/select images` | Adiciona todos os arquivos de imagem do painel à seleção atual. | 
| `/sort by size descending` | Classifica a tabela de arquivos por tamanho, do maior para o menor. | 
| `/reset sort` | Restaura a classificação alfabética padrão dos nomes. | 
| `/group by date` | Agrupa arquivos dinamicamente por colchetes de data de modificação. | 
| `/clear filter` | Remove todos os filtros semânticos ativos e restaura a lista completa de diretórios. | 

---

## 7. Utilitários de arquivos essenciais e integridade de dados

Além da pesquisa e da renomeação em lote, o ATBCmder integra um conjunto de utilitários de sistema essenciais projetados para gerenciar arquivos grandes, auditar a segurança e verificar a integridade criptográfica.

### 7.1 Divisor de arquivos grandes (`cm_FileSpliter` / `cm_Split` / `Alt+F6`)

Ao transferir grandes imagens de disco, arquivos de vídeo ou contêineres de máquinas virtuais entre dispositivos de armazenamento com limites de tamanho de sistema de arquivos (como o limite de 4 GB do FAT32) ou limites de anexo de e-mail, o **Divisor de Arquivos** (`SplitWorker`) divide os arquivos em segmentos sequenciais numerados: 

1. Selecione o arquivo grande no painel ativo. 
2. Escolha **Arquivos ➔ Dividir arquivo...** (ou acione `cm_Split`). 
3. Escolha o diretório de destino (o padrão é o painel oposto). 
4. Selecione uma predefinição de tamanho de bloco padrão ou insira um tamanho de byte personalizado: 
- **1,44 MB**: disquete legado de 3,5". 
- **700 MB**: Capacidade padrão de CD-R. 
**4,7 GB**: capacidade de DVD-R de camada única. 

- **100 MB**: bloco de upload padrão. 
- **Tamanho personalizado**: limite de byte, KB, MB ou GB definido pelo usuário. 
5. Clique em **OK**. ATBCmder divide o arquivo de origem em um thread de trabalho em segundo plano, criando arquivos de sequência `.001`, `.002`, `.003`.... 

---

### 7.2 Vinculador e combinador de arquivos (`cm_FileLinker` / `cm_Combine` / `Alt+F7`)

A remontagem de pedaços de arquivo divididos no arquivo original intacto é perfeita: 

1. No painel de arquivos, destaque a **primeira parte dividida** (deve terminar com a extensão `.001`). 
2. Escolha **Arquivos ➔ Combinar arquivos...** (ou acione `cm_Combine`). 
3. O ATBCmder detecta automaticamente todas as partes sequenciais (`.001`, `.002`, `.003`... até `.999`). 
4. Selecione o nome do arquivo de saída e o diretório de destino. 
5. Clique em **OK**. O trabalhador em segundo plano (`CombineWorker`) concatena sequencialmente as partes de volta em uma réplica binária exata byte por byte. 

---

### 7.3 Checksums criptográficos e verificação (`cm_CheckSumCalc`, `cm_CheckSumVerify`)

Verificar se os arquivos baixados, imagens de disco ou backups de arquivos não foram corrompidos ou adulterados é vital para a integridade dos dados. ATBCmder inclui uma **Calculadora e verificador de soma de verificação** (`ChecksumDialog`) integrado. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Checksum Calculator                                                                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Hash Algorithm: [ SHA256           ▾]                                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3a491d90bc1f42013149db82a890471b67823f40d12e8424e6a00a120894fe83  arch_linux.iso       │
│ 8f14e45fceea167a5a36dedd4bea25431846b9a898492efd727402c3ef30b65a  rootfs.tar.gz        │
│ e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  empty_manifest.txt   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Progress: 100%] Hashing completed.                                                   │
│  [Calculate]    [Stop]    [💾 Save to File]                                 [Close]    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Calculando Hashes (`cm_CheckSumCalc` / `Ctrl+X`)

1. Selecione um ou mais arquivos no painel. 
2. Escolha **Arquivos ➔ Calcular soma de verificação...** (ou pressione `Ctrl+X`). 
3. Selecione o algoritmo desejado: **MD5**, **SHA1**, **SHA256** ou **SHA512**. 
4. Clique em **Calcular**. O trabalhador transmite arquivos por meio de blocos de 64 KB em segundo plano sem bloquear a interface. 
5. Clique em **Salvar em arquivo** para exportar os hashes para um arquivo de manifesto padrão `.sha256` ou `.md5`.

#### Verificando manifestos de soma de verificação (`cm_CheckSumVerify`)

1. Escolha **Arquivos ➔ Verificar somas de verificação...**. 
2. Selecione um arquivo de soma de verificação existente (`.sha256`, `.md5`, `.sha1`, `.sha512` ou `.sfv`). 
3. ATBCmder analisa automaticamente o manifesto, localiza os arquivos correspondentes no mesmo diretório, recalcula hashes no disco e apresenta um relatório de status codificado por cores: 
- **`OK`**: O arquivo corresponde perfeitamente à soma de verificação. 
- **`FAILED`**: Corrupção ou modificação de dados detectada! 
- **`MISSING`**: Arquivo referenciado não encontrado no diretório. 

---

### 7.4 Destruição/limpeza segura de arquivos (`cm_Wipe` / `Alt+Delete` / `⌥⌫`)

A exclusão padrão de arquivos apenas desvincula as entradas do diretório, deixando intactos os blocos de dados brutos no disco, onde os utilitários de recuperação podem extraí-los. Ao lidar com chaves confidenciais, credenciais ou código-fonte proprietário, use **Secure Delete/Wipe** (`cm_Wipe`): 

1. Selecione os arquivos ou diretórios confidenciais. 
2. Pressione **`Alt+Delete`** (`⌥⌫`) ou escolha **Arquivo ➔ Exclusão segura (limpar)...**. 
3. Confirme o prompt de alerta de segurança. 
4. **A sequência criptográfica de destruição multipassagem (`wipe_path`)**: 
- **Pass 1**: Substitui todo o comprimento de bytes do arquivo por bytes pseudo-aleatórios criptograficamente seguros (`os.urandom`). 
- **Pass 2**: Substitui o arquivo inteiro por zero bytes nulos (`\x00`). 
- **Pass 3**: Substitui por novos bytes aleatórios. 
- **Sincronização de hardware**: chama `os.fsync()` no descritor de arquivo subjacente para forçar o sistema operacional e o cache do controlador de armazenamento a gravar dados na mídia física. 
- **Truncamento e desvinculação**: trunca o arquivo para 0 bytes antes de chamar `os.unlink()`. 
- **Esfregando diretórios**: limpa recursivamente todos os arquivos contidos antes de desvincular os diretórios pais. 

---

### 7.5 Terminal de Sistema Embarcado (`Ctrl+J` / `⌃J` / `cm_RunTerm`)

Embora o ATBCmder seja excelente em fluxos de trabalho gráficos de painel duplo, o acesso ao shell geralmente é necessário para compilação, ramificações git ou gerenciamento de servidor: 

- Pressione **`Ctrl+J`** (`⌃J`) ou escolha **Comandos ➔ Executar Terminal**. 
- ATBCmder abre imediatamente o macOS **Terminal.app** (ou seu emulador de terminal padrão configurado) com seu diretório de trabalho inicializado no caminho exato aberto no painel ativo. 
- Não é necessário digitar `cd /Users/...` ou arrastar pastas para as janelas do terminal. 

---

## 8. ⚡ Dicas profissionais e fluxos de trabalho de automação aprofundados

### 8.1 Receita: Pesquisa Recursiva ➔ Feed to Listbox ➔ Multi-Renomeação

**Objetivo**: Remover números de versão de centenas de arquivos de ativos espalhados em 50 subpastas aninhadas. 

1. Abra a raiz do projeto no painel esquerdo. 
2. Pressione **`Alt+F7`** para abrir a Pesquisa. 
3. Em Padrão de nomes de arquivos, insira: `*_v[0-9]*.png`. 
4. Clique em **Iniciar pesquisa**. Assim que os ativos correspondentes aparecerem, clique em **Feed to listbox**. 
5. Na guia do painel virtual resultante, selecione todos os arquivos com **`Cmd+A`**. 
6. Pressione **`Ctrl+M`** para iniciar a ferramenta Multi-Rename. 
7. Em **Localizar**, insira: `_v\d+`. Ative **Usar expressões regulares (Regex)**. 
8. Deixe **Substituir por** vazio. 
9. Verifique se a tabela de visualização ao vivo mostra nomes de arquivos limpos, sem sufixos de versão. 
10. Clique em **Iniciar renomeação**. ATBCmder renomeia todos os arquivos em todas as 50 subpastas instantaneamente! 

---

### 8.2 Receita: Espelhamento seguro de backup em nuvem e NAS com sincronização assimétrica

**Objetivo**: Manter um espelho externo idêntico de seus documentos em um SSD externo ou unidade NAS SMB sem acumular arquivos duplicados. 

1. Abra `~/Documents` local no painel esquerdo. 
2. Abra `/Volumes/BackupSSD/Documents` no painel direito. 
3. Pressione **`Shift+F12`** (`cm_SyncDirs`). 
4. Em Configurações, certifique-se de que **Comparar subdiretórios** esteja marcado. 
5. Marque **Assimétrico (Excluir destino se estiver faltando na origem)**. 
6. Clique em **Comparar**. 
7. Revise a lista: 
- Setas azuis/verdes (`->`) indicam arquivos que serão copiados para o backup. 
- Exclusões em vermelho (`<-`) indicam arquivos desatualizados no disco de backup que você excluiu localmente desde então. 
8. Clique em **Sincronizar**. Sua unidade de backup agora é um espelho da sua pasta local. 

---

### 8.3 Receita: Manifestos Hash Forenses Antes do Armazenamento de Arquivos de Longo Prazo

**Objetivo**: calcular e armazenar somas de verificação criptográficas para um projeto de vários terabytes antes de movê-lo para fita fria ou armazenamento em nuvem glaciar. 

1. Navegue até o diretório que contém as entregas do projeto. 
2. Selecione todos os itens (`Cmd+A`) e pressione **`Ctrl+X`** (`cm_CheckSumCalc`). 
3. Defina o algoritmo como **SHA256**. 
4. Clique em **Calcular**. O trabalhador de hash de streaming processa os arquivos em segundo plano. 
5. Clique em **Salvar em arquivo** e nomeie-o como `MANIFEST-SHA256.txt`. 
6. Sempre que você recuperar os arquivos anos depois, basta selecionar `MANIFEST-SHA256.txt` e executar **Verify Checksums** para garantir zero podridão de bits ou corrupção silenciosa. 

---

### 8.4 Receita: Combinando Filtragem Semântica de Linguagem Natural com Visualização de Ramificação Plana (`Cmd+B`)

**Objetivo**: encontrar e organizar todos os arquivos de mídia em uma estrutura de diretórios profunda e complexa sem abrir caixas de diálogo de pesquisa. 

1. Destaque a pasta do projeto de nível superior e pressione **`Cmd+B`** (`cm_FlatView`) para nivelar todo o conteúdo da subpasta em uma única lista. 
2. Pressione **`/`** para focar a barra de comando semântica. 
3. Digite: `/images larger than 5MB`. 
4. A lista nivelada isola instantaneamente imagens de alta resolução em cada diretório aninhado. 
5. Pressione `/select all visible` e, em seguida, pressione **`F5`** para copiá-los todos em um diretório de destino organizado no painel oposto. 
6. Pressione `Cmd+B` novamente para restaurar a navegação normal na árvore hierárquica. 

---

## 9. Alertas de segurança, desempenho e sistema

> [!CAUTION] 
> **Irreversibilidade da sincronização de diretório assimétrica** 
> Habilitar a opção **Assimétrica** na Sincronização de diretório (`Shift+F12`) faz com que os arquivos no diretório de destino que não existem na origem sejam **excluídos permanentemente**. Sempre realize uma inspeção visual da tabela de visualização de comparação antes de clicar em **Sincronizar**. 

> [!WARNING] 
> **Substituições RegEx com múltiplas renomeações** 
> Ao realizar substituições de expressões regulares com referências anteriores (`$1`, `$2`), certifique-se de que os números do seu grupo de captura correspondam aos parênteses no seu padrão. Teste seu padrão nas linhas da tabela de visualização ao vivo antes de clicar em **Iniciar renomeação**. Se nomes duplicados de destino aparecerem, o ATBCmder bloqueará a execução para protegê-lo contra perda de dados. 

> [!IMPORTANT] 
> **Limitações de destruição da unidade de estado sólido (SSD)** 
> O utilitário Secure Wipe (`cm_Wipe` / `Alt+Delete`) substitui os dados do arquivo com múltiplas passagens de bytes aleatórios e zero, seguidas por uma chamada `fsync`. No entanto, as unidades de estado sólido (SSDs) modernas utilizam algoritmos de nivelamento de desgaste e superprovisionamento no nível do controlador que podem redirecionar gravações para blocos flash alternativos. Para descarte de SSD de alta segurança, combine a destruição de arquivos com a criptografia de disco completo do macOS FileVault. 

> [!NOTE] 
> **Disponibilidade em destaque em volumes de rede e FAT** 
> Fast Spotlight Search (`Ctrl+Shift+F`) depende de índices de metadados do macOS, que estão ativos por padrão em unidades APFS internas. Montagens de rede remotas (SMB, SFTP) e unidades exFAT externas podem não ser indexadas pelo Spotlight. Se uma consulta Spotlight não retornar resultados em uma unidade externa, use **Deep Scan** (`Alt+F7`) ou habilite a verificação recursiva de diretório. 

> [!TIP] 
> **Teclas de função Apple (`Fn`) Compatibilidade** 
> Em Apple Magic Keyboards e MacBooks, as teclas de função (`F1`-`F12`) são padronizadas para ações de hardware (brilho, volume). Para pressionar `Shift+F12` ou `Alt+F7`, mantenha pressionada a tecla **`Fn`**: `Fn+Shift+F12`, `Fn+Alt+F7`. Como alternativa, ative **"Usar as teclas F1, F2, etc. como teclas de função padrão"** no macOS *Configurações do sistema ➔ Teclado ➔ Atalhos de teclado ➔ Teclas de função*. 

---

## 10. Tabela de referência do teclado mestre de matriz dupla

| Área Funcional | Descrição da ação | Atalho do macOS | Chave do Comandante Clássico | ID do comando | 
| :--- | :--- | :--- | :--- | :--- | 
| **Renomeação múltipla** | Iniciar ferramenta de renomeação múltipla em lote | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | 
| **Renomeação múltipla** | Executar / Iniciar Renomear | `Enter` / `⏎` | `Enter` | — | 
| **Renomeação múltipla** | Ferramenta Cancelar/Fechar | `Esc` | `Esc` | — | 
| **Diferença de arquivo** | Comparar arquivos/painéis selecionados | `Meta+Shift+F12` / `⌘⇧F12` | `Meta+Shift+F12` | `cm_FileDiff` / `cm_CompareFiles` | 
| **Diferença de arquivo** | Ir para a próxima diferença | `Alt+Down` / `⌥↓` | `Ctrl+Down` | — | 
| **Diferença de arquivo** | Ir para a diferença anterior | `Alt+Up` / `⌥↑` | `Ctrl+Up` | — | 
| **Diferença de arquivo** | Copiar pedaço da esquerda para a direita | `Alt+Right` / `⌥→` / `Alt+P` | `Ctrl+Alt+Right` | — | 
| **Diferença de arquivo** | Copiar pedaço da direita para a esquerda | `Alt+Left` / `⌥←` / `Alt+O` | `Ctrl+Alt+Left` | — | 
| **Diferença de arquivo** | Salvar alterações no editor em destaque | `Cmd+S` / `⌘S` | `Ctrl+S` | — | 
| **Diferença de arquivo** | Recalcular diferenças | `F5` / `Fn+F5` | `Ctrl+R` | — | 
| **Sincronização de diretório**| Abra Sincronizar diretórios | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | 
| **Sincronização de diretório**| Iniciar comparação de diretórios | `Alt+C` / `⌥C` | `Enter` | — | 
| **Sincronização de diretório**| Cancelar comparação/sincronização | Clique em `Stop` | `Esc` | — | 
| **Pesquisa de arquivos** | Abrir caixa de diálogo de pesquisa avançada | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` / `cm_FileSearch` | 
| **Pesquisa de arquivos** | Ver resultado no Lister Universal | `F3` / `Fn+F3` | `F3` | `cm_View` | 
| **Pesquisa de arquivos** | Editar resultado no editor de texto | `F4` / `Fn+F4` | `F4` | `cm_Edit` | 
| **Pesquisa de arquivos** | Vá para Arquivo no Painel Ativo | `Enter` / `⏎` | `Enter` | — | 
| **Pesquisa de arquivos** | Alimentar resultados para painel virtual | Clique em `Feed to listbox` | Clique em `Feed to listbox` | — *(Ação de diálogo)* | 
| **Destaque e PNL**| Pesquisa rápida em destaque | `Ctrl+Shift+F` / `⌃⇧F` | `Ctrl+Shift+F` | *(Menu Comandos)* | 
| **Destaque e PNL**| Ativar barra de comandos semânticos | `/` | `/` | `cm_VisSemanticCommand` | 
| **Destaque e PNL**| Dispensar filtro semântico | `Esc` | `Esc` | — | 
| **Utilitários de arquivo**| Dividir arquivo em pedaços | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | 
| **Utilitários de arquivo**| Combine pedaços divididos numerados | Menu: Arquivos ➔ Combinar Arquivos | — | `cm_FileLinker` / `cm_Combine` | 
| **Utilitários de arquivo**| Calcular soma de verificação (hash) | `Ctrl+X` / `⌃X` | `Ctrl+X` | `cm_CheckSumCalc` / `cm_CalculateChecksum` | 
| **Utilitários de arquivo**| Verifique o arquivo de manifesto de soma de verificação | Menu Ferramentas | Menu Ferramentas | `cm_CheckSumVerify` / `cm_VerifyChecksum` | 
| **Utilitários de arquivo**| Limpeza multipassagem segura (fragmentar) | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | 
| **Utilitários de arquivo**| Abra o terminal nativo do macOS | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` |

--- 

<div align="center"> 
<p>Pronto para se conectar a servidores remotos e explorar arquivos virtuais?</p> 
<p><strong><a href="network_and_vfs.md">Prossiga para o Capítulo 6: Sistemas de arquivos virtuais e rede &rarr;</a></strong></p> 
</div>