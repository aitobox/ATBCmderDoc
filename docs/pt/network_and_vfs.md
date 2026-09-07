# Capítulo 6: Sistemas de arquivos virtuais e rede

O gerenciamento moderno de arquivos raramente para no limite de um único disco rígido físico. Os desenvolvedores de software mantêm ambientes de teste remotos por SFTP; administradores de sistema gerenciam compartilhamentos de arquivos empresariais por meio de SMB/CIFS; os criadores de conteúdo acessam armazenamento em nuvem e servidores de mídia via WebDAV; e usuários avançados inspecionam, editam e empacotam rotineiramente arquivos compactados em escala de gigabytes. 

Os ambientes de desktop tradicionais forçam os usuários a lidar com aplicativos desarticulados: um utilitário de arquivamento independente para descompactar e recomprimir arquivos zip, um cliente FTP/SFTP externo para gerenciar ativos do servidor e caixas de diálogo de montagem do sistema operacional que espalham volumes remotos em janelas desconectadas do Finder. 

O ATBCmder elimina essa fragmentação por meio de seu mecanismo **Virtual File System (VFS)**. Construído sobre uma camada de abstração de URI `vfs://` unificada, o ATBCmder trata servidores remotos e arquivos compactados exatamente como pastas locais padrão. Você pode navegar em um arquivo `.tar.gz`, visualizar arquivos de código com `F3`, editar um arquivo de configuração aninhado com `F4` (com reempacotamento automático ao vivo ao salvar) e copiar ativos diretamente em uma sessão SFTP segura para um NAS SMB local usando a chave `F5` padrão - tudo sem extrair arquivos intermediários para o disco ou alternar entre ferramentas separadas. 

---

## 1. Guia de início rápido visual: arquitetura VFS e matriz de comandos

ATBCmder roteia todo o acesso ao sistema de arquivos através de uma camada de abstração unificada. Quer um caminho aponte para uma partição SSD APFS da Apple, um membro dentro de um arquivo `.zip` aninhado ou um diretório remoto hospedado em um servidor Linux SFTP do outro lado do mundo, a interface de painel duplo fornece um modelo operacional idêntico. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              ATBCMDER DUAL-PANEL GUI                                   │
│            Left Panel (Active)                  Right Panel (Inactive / Target)        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Local File System                   │  [2] Archive Virtual File System (VFS)      │
│      file:///Users/brain/projects/       │      vfs:///Users/brain/backup.tar.gz/src/  │
│      Direct POSIX / APFS access          │      In-place browse, F3 view, F4 live edit │
│                                          │                                             │
│  [3] Remote Network VFS (SFTP/SSH)       │  [4] Remote Storage VFS (SMB / WebDAV)      │
│      vfs://sftp://deploy@aws.prod/app/   │      vfs://smb://admin@truenas/Pool/Media/  │
│      Paramiko / SSH Keys / Keychain      │      Kernel mount_smbfs / WebDAVClient3     │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                          UNIFIED VFS DISPATCH ENGINE (vfs://)                          │
│     FileSystemModel ➔ VFSManager ➔ SessionCache ➔ StreamCopyWorker / RepackWorker      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Folha de dicas de rede e VFS de matriz dupla

| Ação | Atalho do macOS | Chave do Comandante Clássico | ID do comando | Descrição | 
| :--- | :--- | :--- | :--- | :--- | 
| **Compactar arquivos em arquivo** | `Alt+F5` / `⌥F5` | `Alt+F5` | `cm_PackFiles` | Abre a caixa de diálogo Archive Pack com opções de formato, compactação e senha. | 
| **Extrair arquivos do arquivo** | `Alt+F9` / `⌥F9` | `Alt+F9` | `cm_ExtractFiles` | Descompacta os arquivos selecionados com resolução de colisão. | 
| **Conexão rápida de rede** | Menu: Rede | `cm_NetworkConnect` | `cm_NetworkConnect` | Abre a caixa de diálogo de conexão ad-hoc rápida. | 
| **Gerenciador de conexões** | Menu: Rede | `cm_ManageConnections`| `cm_ManageConnections`| Abre o gerenciador de rede CRUD completo com perfis de conexão salvos. | 
| **Conexão FTP** | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_FTPConnect` | Atalho rápido para acionar sessão de conexão FTP. | 
| **Insira arquivo/pasta** | `Enter` / `⏎` | `Enter` | `cm_Open` | Navega diretamente dentro de um `.zip`, `.tar`, `.7z` ou diretório remoto. | 
| **Ascender para pasta pai** | `Backspace` / `⌫` | `Backspace` | `cm_GoToParent` | Sai do arquivo ou diretório remoto de volta ao nível pai. | 
| **Ver arquivo virtual/remoto**| `F3` / `Fn+F3` | `F3` | `cm_View` | Transmite arquivo remoto ou compactado para o Universal Lister. | 
| **Editar arquivo virtual/remoto**| `F4` / `Fn+F4` | `F4` | `cm_Edit` | Abre arquivo no editor; reembala automaticamente ou carrega de volta ao salvar. | 
| **Cópia entre painéis/VFS** | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Copia itens selecionados em endpoints locais, de arquivo ou de rede. | 
| **Painel de operações em segundo plano**| Menu: Mostrar | `cm_OperationsPanel` | `cm_OperationsPanel` | Monitora filas de transferência em segundo plano, velocidades e threads ativos. | 

---

## 2. A abstração unificada de `vfs://` URI

Os gerenciadores de arquivos tradicionais tratam servidores e arquivos remotos como cidadãos de segunda classe, exigindo utilitários de montagem externos, pastas de extração temporárias ou clientes de transferência de terceiros. ATBCmder unifica todas as fontes de arquivo em uma especificação de URI única e bem definida: 

```
vfs://[protocol]://[user]@[host]:[port]/[remote_path]
```

### 2.1 Anatomia dos Caminhos Virtuais

Dependendo do domínio operacional, os URIs `vfs://` assumem um dos dois formatos padrão: 

1. **Arquivar caminhos virtuais**: 
   ```
   vfs:///Users/brain/Documents/release_v1.7.zip/src/main.py
   ```
 

- **Prefixo externo**: `vfs://` instrui `FileSystemModel` a interceptar a travessia do caminho. 
- **Caminho do contêiner**: `/Users/brain/Documents/release_v1.7.zip` identifica o arquivo do contêiner físico no armazenamento local. 
- **Membro Interno**: `src/main.py` identifica o recurso virtual aninhado dentro do arquivo. 

2. **Caminhos do servidor de rede**: 
   ```
   vfs://sftp://developer@staging.internal.net:2222/var/www/html/index.php
   vfs://smb://admin@192.168.1.50/StoragePool/Backups/2026/
   vfs://webdavs://user@cloud.mycompany.com:443/remote.php/dav/files/user/
   ```
 

- **Especificador de esquema**: Identifica o driver de transporte (`sftp`, `ftp`, `ftps`, `smb`, `webdav`, `webdavs`, `gdrive`). 
- **Autenticação**: codifica as credenciais do usuário e a porta de destino. 
- **Destino remoto**: Resolve diretórios absolutos e caminhos de arquivos no host remoto. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              VFS URI ROUTING IN ACTION                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Input URI: vfs://sftp://deploy@aws.infra:22/var/log/nginx/access.log                 │
│                 │      │        │        │   └────────────────────► Remote Path        │
│                 │      │        │        └────────────────────────► Port (Default 22)  │
│                 │      │        └─────────────────────────────────► Host / Server      │
│                 │      └──────────────────────────────────────────► Username           │
│                 └─────────────────────────────────────────────────► Protocol Scheme    │
│                                                                                        │
│   Input URI: vfs:///Volumes/Data/Archive.zip/docs/manual.pdf                           │
│                 │                      │        └─────────────────► Archive Member     │
│                 │                      └──────────────────────────► Physical Archive   │
│                 └─────────────────────────────────────────────────► Virtual Scheme     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Integração perfeita de painel duplo

Como os caminhos virtuais estão em conformidade com as estruturas de diretório padrão dentro do ATBCmder, você desfruta de paridade total de painel duplo: 

- **Áreas de trabalho virtuais com guias**: abra uma pasta SFTP remota na guia 1, um arquivo ZIP local criptografado na guia 2 e sua pasta `~/Downloads` local na guia 3. 
- **Cópia direcional (`F5`)**: Selecione os arquivos em seu painel ativo local e pressione `F5` para carregá-los diretamente no servidor remoto ou arquivo compactado exibido no painel inativo. 
- **Interoperabilidade de arrastar e soltar**: arraste itens entre painéis entre discos locais, compartilhamentos de rede e hierarquias de arquivos sem preparação intermediária. 
- **Barra de localização atual**: a barra de caminho de localização atual analisa URIs virtuais em segmentos clicáveis. Clique em qualquer pasta pai ou no emblema do servidor raiz para subir na árvore instantaneamente. 

---

## 3. Arquivar VFS: navegação e inspeção no local

Abrir um arquivo no ATBCmder não requer extração manual ou ferramenta de descompactação de terceiros. Basta destacar qualquer arquivo suportado e pressionar **`Enter`** (ou clicar duas vezes). ATBCmder monta o arquivo no local, transformando o painel em um navegador de diretório virtual de alta velocidade. 

![Archive VFS In-Place Navigation](images/archive_vfs.png) 
*Figura 6.1: Navegando dentro de um arquivo compactado multi-aninhado como uma pasta virtual, mostrando tamanhos não compactados, carimbos de data/hora e subdiretórios.*

### 3.1 Formatos de arquivo suportados

ATBCmder possui drivers integrados para todos os formatos de compactação e arquivamento padrão da indústria: 

| Formato | Extensões de arquivo | Leia Suporte | Escrever / Embalar | Suporte à criptografia | 
| :--- | :--- | :---: | :---: | :--- | 
| **CEP** | `.zip` | Sim | Sim | Padrão e AES-256 (`pyzipper`) | 
| **Tarball GZip** | `.tar.gz`, `.tgz` | Sim | Sim | Streaming tar padrão POSIX | 
| **Tarball BZip2**| `.tar.bz2`, `.tbz2` | Sim | Sim | Compressão de bloco bzip2 de alta proporção | 
| **XZ Tarball** | `.tar.xz`, `.txz` | Sim | Sim | Compressão LZMA2 de alta eficiência | 
| **TAR simples** | `.tar` | Sim | Sim | Arquivo de fita UNIX não compactado | 
| **7-Zip** | `.7z` | Sim | Sim (através de `py7zr`)| Compressão sólida LZMA / LZMA2 |

### 3.2 Fluxos de trabalho de navegação no local

Ao navegar dentro de um arquivo: 

1. **Insira os subdiretórios**: pressione `Enter` em qualquer pasta dentro do arquivo para explorar árvores aninhadas. 
2. **Ascender para Pai (`..`)**: Pressione `Backspace` (`⌫`) ou clique duas vezes na entrada `.. [Parent Directory]` para ascender. Depois de chegar à raiz do arquivo, pressionar `Backspace` retorna você de forma limpa ao diretório físico que contém o arquivo morto. 
3. **Visualização instantânea (`F3` / `Fn+F3`)**: Destaque qualquer documento, imagem ou arquivo de origem dentro do arquivo e pressione `F3`. ATBCmder extrai automaticamente o arquivo de destino para uma sandbox temporária segura e o renderiza dentro do Universal Lister. 
4. **Cópia seletiva (`F5` / `Fn+F5`)**: Em vez de descompactar um arquivo inteiro de vários gigabytes apenas para recuperar um ou dois arquivos, selecione os membros específicos necessários e pressione `F5`. ATBCmder descompacta apenas os itens escolhidos diretamente no painel inativo. 

> [!NOTA] 
> Ao visualizar ou copiar arquivos individuais de um arquivo, o ATBCmder transmite apenas os bytes do arquivo solicitados diretamente do fluxo do contêiner. Ele não desperdiça espaço em disco ou tempo descompactando arquivos irmãos não selecionados. 

---

## 4. Reempacotamento ao vivo: edição no local dentro dos arquivos

Um dos fluxos de trabalho mais poderosos no ATBCmder é o **Live Repacking**. Historicamente, a modificação de um único arquivo aninhado dentro de um arquivo compactado exigia uma sequência tediosa de seis etapas: extrair o arquivo inteiro, localizar o arquivo de destino, editá-lo e salvá-lo, recompactar o diretório em um novo arquivo, excluir o arquivo original e limpar pastas temporárias. 

ATBCmder torna a edição de arquivos dentro de arquivos tão fácil quanto a edição de arquivos locais padrão. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              LIVE REPACKING LIFECYCLE                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  1. User presses F4 on "config.json" inside "package.zip"                              │
│     │                                                                                  │
│     ├──► ATBCmder extracts "config.json" to sandbox: /tmp/dc_repack_xyz/config.json    │
│     └──► Opens internal EditorDialog with window title: "config.json — Editor"         │
│                                                                                        │
│  2. User modifies file and presses Cmd+S (Save)                                        │
│     │                                                                                  │
│     ├──► Editor emits file_saved signal                                                │
│     └──► RepackWorker checks original archive size vs ArchiveRepackWarningMB threshold │
│                                                                                        │
│  3. Atomic Repack Execution                                                            │
│     │                                                                                  │
│     ├──► Writes modified stream to staging archive: /tmp/package.zip.tmp               │
│     ├──► Validates container integrity via archive driver                              │
│     ├──► Atomic swap: os.replace("/tmp/package.zip.tmp", "/original/package.zip")      │
│     └──► Refreshes active file panel and cleans up sandbox /tmp/dc_repack_xyz/         │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Passo a passo: Editando um arquivo de configuração arquivado

1. Navegue até o arquivo (por exemplo, `application_bundle.zip`) pressionando `Enter`. 
2. Localize o arquivo que deseja modificar (por exemplo, `settings.yaml`). 
3. Pressione **`F4`** (`Fn+F4`). ATBCmder extrai o arquivo em um cache temporário e inicia o Editor integrado. 
4. Faça suas modificações no editor. 
5. Pressione **`Cmd+S`** (`⌘S`) para salvar. 
6. Feche o editor com `Cmd+W` (`⌘W`) ou `Esc`. 
7. O `RepackWorker` do ATBCmder atualiza automaticamente o membro interno, compacta a estrutura atualizada em um arquivo temporário, substitui atomicamente o arquivo original e atualiza a visualização do painel. 

> [!CUIDADO] 
> **Proteção de segurança de arquivo grande (`ArchiveRepackWarningMB`)** 
> Reembalar um arquivo compactado requer descompactar e recodificar fluxos de contêiner. Modificar um arquivo de 10 KB dentro de um arquivo de vídeo `.tar.gz` de 20 GB forçaria o computador a reescrever todos os 20 GB de dados. 
> 
> Para evitar congelamentos acidentais do disco, o ATBCmder inclui um limite de segurança de proteção (`ArchiveRepackWarningMB`, padrão: **100 MB** em `atbcmder.xml`). Se você tentar editar ou excluir um arquivo dentro de um arquivo maior que esse limite, o ATBCmder exibirá um prompt de confirmação: 
> *"A modificação deste arquivo requer a recompactação de todo o arquivo, o que pode levar muito tempo. Deseja continuar?"* 

---

## 5. Criação e extração de arquivos (`Alt+F5` / `Alt+F9`)

ATBCmder fornece trabalhadores em segundo plano dedicados para criar e extrair arquivos, garantindo que seus painéis de arquivos permaneçam responsivos mesmo durante trabalhos de compactação de longa duração. 

![Pack and Extract Archives](images/archive_pack_extract.png) 
*Figura 6.2: A caixa de diálogo Parâmetros de arquivo (Alt+F5 / cm_PackFiles) mostrando o caminho de destino, seleção de formato, níveis de compactação e criptografia de senha.*

### 5.1 Compactando Arquivos (`Alt+F5` / `⌥F5` / `cm_PackFiles`)

Para criar um novo arquivo: 

1. No painel ativo, selecione os arquivos ou diretórios que deseja agrupar. 
2. Pressione **`Alt+F5`** (`⌥F5`) ou escolha **Arquivos ➔ Pacote...** na barra de menu. 
3. A caixa de diálogo **Compactar arquivos** é exibida: 
- **Criar arquivo morto**: Caminho do arquivo de destino. Por padrão, ATBCmder sugere colocar o arquivo no diretório do painel inativo, nomeado após o item em foco. 
- **Formato de arquivo**: Escolha entre `ZIP`, `TAR`, `TAR.GZ`, `TAR.BZ2`, `TAR.XZ` ou `7Z`. 
- **Nível de compressão**: 
- `Store`: Compressão zero; empacotamento instantâneo para mídia pré-compactada (MP4, JPEG). 
- `Fast`: Baixa sobrecarga de CPU; ideal para transferências rápidas. 
- `Normal (Deflated)`: Velocidade e taxa de compressão balanceadas (recomendado para uso geral). 
- `Maximum`: Compressão de densidade mais alta (utiliza LZMA/Bzip2 quando aplicável). 
- **Senha (somente ZIP)**: Digite uma senha secreta para criptografar o arquivo. 
4. Clique em **Iniciar** (ou pressione `Enter`). A operação é executada em um thread em segundo plano sem bloqueio, com uma barra de progresso e um indicador de status arquivo por arquivo.

#### Criptografia de senha AES-256 de nível militar

A criptografia ZIP padrão (ZipCrypto legado) é criptograficamente quebrada e vulnerável a ataques de dicionário de texto simples. Quando você especifica uma senha para um arquivo ZIP, o ATBCmder utiliza **criptografia AES-256** fornecida por `pyzipper` (`pyzipper.AESZipFile` com padrão `WZ_AES`). Isso garante compatibilidade com macOS, WinZip e 7-Zip, ao mesmo tempo que protege dados confidenciais contra descriptografia de força bruta.

#### Dividindo arquivos enormes em conjuntos de vários volumes

Se você precisar distribuir um arquivo entre anexos de e-mail, unidades FAT32 ou limites de upload na nuvem com limites de tamanho de arquivo: 

1. Agrupe seus arquivos usando `Alt+F5` (`cm_PackFiles`). 
2. Destaque o arquivo `.zip` ou `.tar` resultante e acione o Divisor de Arquivos via **`Alt+F6`** (`cm_FileSpliter`). 
3. Selecione um tamanho de divisão predefinido (por exemplo, `100 MB`, `4.7 GB DVD`, `CD 700 MB` ou tamanho de byte personalizado). 
4. ATBCmder gera partes divididas numeradas (`archive.zip.001`, `archive.zip.002`, etc.) junto com um manifesto de verificação CRC32. Os destinatários podem remontar o contêiner original a qualquer momento usando **`cm_FileLinker`** (`cm_Combine`). 

---

### 5.2 Extraindo Arquivos (`Alt+F9` / `⌥F9` / `cm_ExtractFiles`)

Para extrair arquivos para o disco: 

1. Destaque um ou mais arquivos no painel ativo. 
2. Pressione **`Alt+F9`** (`⌥F9`) ou escolha **Arquivos ➔ Extrair...** na barra de menu. 
3. A caixa de diálogo **Extrair arquivos** é exibida: 
- **Arquivar para extrair**: caminho de origem do contêiner selecionado. 
- **Extrair para diretório**: Diretório de destino (o padrão é o painel inativo). 
- **Conteúdo de visualização**: uma caixa de listagem interativa que carrega membros do arquivo em tempo real. 
- **Senha**: Campo de entrada para arquivos protegidos por senha. 
4. Clique em **Iniciar**. Se já existir algum arquivo de destino na pasta de destino, o ATBCmder pausa o trabalhador e apresenta uma caixa de diálogo de colisão interativa: 
- **Substituir**: Substitui o arquivo de destino conflitante. 
- **Pular**: deixa o arquivo existente intacto e avança para o próximo item. 
- **Substituir tudo**: substitui silenciosamente todos os conflitos subsequentes. 
- **Pular tudo**: Ignora automaticamente todos os arquivos de destino existentes. 
- **Cancelar**: Interrompe com segurança o processo de extração. 

---

## 6. VFS de rede remota: protocolos e armazenamento remoto

ATBCmder inclui um mecanismo cliente de rede multiprotocolo capaz de montar, navegar e manipular servidores remotos diretamente dentro do espaço de trabalho de painel duplo. 

![Network VFS Client](images/network_vfs.png) 
*Figura 6.3: Navegando em diretórios de servidores Linux remotos por meio de SFTP seguro com atributos de arquivo ativos, permissões de propriedade e transferência de painel duplo.* 

![Remote Connection Overview](images/smb_sftp_ftp_remote_access.png) 
*Figura 6.4: Tipos de conexão de rede suportados: FTP/FTPS, SFTP seguro, armazenamento em nuvem WebDAV e compartilhamentos de rede SMB.*

### 6.1 Protocolos de Rede Suportados

| Esquema de Protocolo | Porta padrão | Camada de Transporte | Modos de autenticação | Melhor usado para | 
| :--- | :---: | :--- | :--- | :--- | 
| **`sftp://`** | `22` | SSH-2 (Paramiko) | Senha, chave SSH (`id_rsa`, `id_ed25519`) | Servidores Linux, instâncias em nuvem, hosts de teste | 
| **`ftp://`** | `21` | Simples RFC 959 | Nome de usuário e senha anônimos e em texto simples | Hospedagem na web legada, dispositivos de laboratório local | 
| **`ftps://`** | `990` | FTP criptografado por TLS | Nome de usuário e senha com SSL/TLS | Servidores FTP comerciais seguros | 
| **`smb://`** | `445` | CIFS/SMB3 | Windows NT/Kerberos/Conta local | Compartilhamentos Windows, dispositivos NAS, servidores Samba | 
| **`webdav://`** | `80` | HTTP WebDAV | Autenticação básica e resumida | Servidores Web, armazenamento em rede local | 
| **`webdavs://`** | `443` | HTTPS WebDAV | Autenticação básica/digest criptografada por SSL | Nextcloud, ownCloud, armazenamento em nuvem comercial | 
| **`gdrive://`** | `443` | API do Google Drive | Autorização de token OAuth2 | Unidades de nuvem e pastas compartilhadas do Google Drive | 

---

### 6.2 Capacidades de protocolo e aprofundamento

#### SFTP (protocolo de transferência de arquivos SSH)

Apoiado pelo mecanismo SSH `paramiko` padrão da indústria, o driver SFTP do ATBCmder estabelece túneis criptografados na porta 22: 

- **Host Key Safety (`WarningPolicy`)**: Em conformidade com requisitos rígidos de segurança, o ATBCmder consulta automaticamente seu arquivo `~/.ssh/known_hosts` local. Ao conectar-se a um host conhecido, as chaves do host são verificadas criptograficamente. Se um servidor desconhecido for encontrado, o ATBCmder emite um aviso de segurança em vez de confiar silenciosamente em chaves públicas inesperadas. 
- **Autenticação de chave SSH**: Além da autenticação de senha padrão, o ATBCmder oferece suporte a arquivos de chave privada SSH (`~/.ssh/id_rsa`, `~/.ssh/id_ed25519`). 
- **Mapeamento de atributos UNIX**: preserva modos de arquivo octais remotos (`chmod`), strings de propriedade de usuário/grupo e carimbos de data/hora exatos de modificação POSIX.

#### FTP e FTPS (SSL explícito/implícito)

Impulsionado pelo `ftplib` do Python, o driver FTP suporta: 

- **Modo Passivo (PASV)**: ativado por padrão para garantir conexões confiáveis por meio de roteadores NAT restritivos e firewalls de consumo. 
- **Codificações configuráveis**: Resolve problemas de exibição de nomes de arquivos não ASCII, permitindo alternar entre conjuntos de caracteres `UTF-8`, `ISO-8859-1`, `GB18030` e `Windows-1252`.

#### SMB/Samba (compartilhamentos Windows e dispositivos NAS)

Ao contrário das bibliotecas SMB Python de espaço de usuário ingênuo que sofrem com velocidades de transferência lentas, o ATBCmder emprega uma arquitetura híbrida: 

- **Aceleração nativa do kernel do macOS (`mount_smbfs`)**: no macOS, o `SambaMounter` do ATBCmder aproveita o subsistema `/sbin/mount_smbfs` nativo da Apple. Ele monta o compartilhamento remoto diretamente na árvore VFS do macOS (`/Volumes/` ou em um diretório de montagem isolado), desbloqueando a taxa de transferência completa de leitura/gravação SMB3 acelerada por hardware. 
- **Detecção de montagem existente**: se o macOS Finder ou um script do sistema já tiver montado o compartilhamento SMB de destino, o ATBCmder detectará automaticamente o ponto de montagem ativo da tabela OS `mount` e navegará até ele instantaneamente, evitando conexões de rede redundantes. 

> [!IMPORTANTE] 
> **Requisito de nome de compartilhamento SMB** 
> Um servidor SMB não pode ser navegado no nível do nome de host simples. Um URI SMB **deve** incluir o compartilhamento de destino ou o nome de exportação no caminho: 
> 
> - ❌ Inválido: `vfs://smb://nas.local/` 
> - ✅ Válido: `vfs://smb://nas.local/StoragePool` ou `vfs://smb://192.168.1.100/Media`

#### WebDAV e WebDAVS (Nextcloud/armazenamento em nuvem)

Construído em `webdavclient3`, este driver fornece sincronização bidirecional de arquivos com soluções modernas de armazenamento em nuvem: 

- **Verificação de certificado SSL**: suporta validação rigorosa de certificado SSL para hosts WebDAVS públicos, com uma alternância de substituição para certificados autoassinados em configurações de homelab privadas. 
- **Criação de diretório recursivo (`makedirs`)**: cria automaticamente caminhos de diretório remoto aninhados ausentes durante operações de upload em massa. 

---

## 7. Conexão rápida vs. Gerenciador de conexões

O ATBCmder fornece dois mecanismos flexíveis para conexão com hosts remotos: **Quick Connect** para sessões rápidas e temporárias e **Connection Manager** para marcadores de servidor categorizados e persistentes.

### 7.1 Conexão rápida (`cm_NetworkConnect`)

Quando você precisar acessar rapidamente um servidor sem sobrecarregar sua configuração permanente: 

1. Escolha **Rede ➔ Conexão Rápida...** (ou execute o comando `cm_NetworkConnect`). 
2. O prompt de conexão leve é exibido: 
- **Protocolo**: Selecione `sftp`, `ftp`, `ftps`, `smb`, `webdav`, `webdavs` ou `gdrive`. 
- **Host e Porta**: Insira o endereço do servidor (a porta preenche automaticamente os valores padrão). 
- **Nome de usuário e senha**: Insira credenciais de conexão. 
- **Caminho remoto**: Iniciando diretório remoto (padrão: `/`). 
- **Lembrar senha**: Deixe desmarcado para uma conexão efêmera de sessão única. 
3. Clique em **Testar conexão** para verificar o handshake e as credenciais da rede antes de conectar. 
4. Clique em **Conectar**. ATBCmder abre imediatamente uma nova aba no painel ativo apontando para o servidor remoto. 

---

### 7.2 Gerenciador de conexões (`cm_ManageConnections`)

Para servidores que você acessa regularmente, o **Connection Manager** fornece um painel de configuração completo: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              CONNECTION MANAGER DIALOG                                 │
├──────────────────────────────┬─────────────────────────────────────────────────────────┤
│  Saved Connections           │  Connection Details                                     │
│  ┌────────────────────────┐  │  Label:        [ Staging Web Server (AWS)             ] │
│  │ 🔐 AWS Staging Server  │  │  Protocol:     [ SFTP (port 22)                     ▼ ] │
│  │ 🖧 Synology Office NAS │  │  Host:         [ ec2-54-210-10-2.compute.amazonaws.com] │
│  │ 🌐 Nextcloud Personal  │  │  Port:         [ 22                                   ] │
│  │ 📂 Legacy Archive FTP  │  │  Username:     [ ubuntu                               ] │
│  │                        │  │  Password:     [ ••••••••••••••••••                   ] │
│  │                        │  │  Remote Path:  [ /var/www/production                  ] │
│  │                        │  │  [✓] Remember password in macOS Keychain                │
│  └────────────────────────┘  │                                                         │
│  [➕ New] [⧉ Dup] [🗑 Del]    │  [🔍 Test Connection]          [💾 Save]  [🔗 Connect] │
└──────────────────────────────┴─────────────────────────────────────────────────────────┘
```

#### Gerenciando perfis de servidor

- **Criar Novo (`➕ New`)**: Limpa o formulário à direita para definir uma nova configuração do servidor. 
- **Duplicar (`⧉ Duplicate`)**: Clona o perfil de conexão selecionado. Ideal ao gerenciar vários ambientes (desenvolvimento, preparação, produção) em configurações de host idênticas. 
- **Excluir (`🗑 Delete`)**: remove o perfil de conexão e exclui as credenciais associadas das chaves do sistema. 
- **Testar conexão (`🔍 Test Connection`)**: envia um trabalhador em segundo plano (`ConnectionTestWorker`) para conectar, autenticar e desconectar normalmente, verificando a capacidade de resposta do servidor sem sair dele. 
- **Conectar (`🔗 Connect`)**: Salva quaisquer edições de campo pendentes, estabelece a sessão remota e carrega o diretório remoto em uma nova guia do painel ativo.

#### Menu Conexões Salvas Dinâmicas

As conexões salvas são automaticamente integradas na barra de menu superior em **Rede ➔ Conexões Salvas**. Você pode montar qualquer servidor marcado com um único clique: 

- `Network ➔ Saved Connections ➔ 🔐 AWS Staging Server` 
- `Network ➔ Saved Connections ➔ 🖧 Synology Office NAS` 

---

## 8. Segurança de credenciais e integração de chaveiro

Os arquivos de configuração do gerenciador de arquivos são o principal alvo do malware de coleta de credenciais. Muitos gerenciadores de arquivos legados armazenam senhas FTP/SFTP em arquivos de configuração XML ou INI de texto simples localizados no diretório inicial do usuário. 

**ATBCmder garante zero armazenamento de credenciais em texto não criptografado.**

### 8.1 A Arquitetura de Segurança

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                           CREDENTIAL STORAGE ARCHITECTURE                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Connection Configuration XML                    Apple System Keychain                │
│   (~/.config/atbcmder/atbcmder.xml)               (service: "ATBCmder_VFS")            │
│   ┌─────────────────────────────────────┐         ┌──────────────────────────────────┐ │
│   │ <connection>                        │         │ Label: "AWS Staging Server"      │ │
│   │   <label>AWS Staging</label>        │         │ Key:   Encrypted Secret          │ │
│   │   <scheme>sftp</scheme>             │         │ Access: Controlled by macOS      │ │
│   │   <host>aws.infra.net</host>        │         │         Hardware Security Enclave│ │
│   │   <user>deploy</user>               │         └──────────────────────────────────┘ │
│   │   <password></password>             │                           ▲                  │
│   │ </connection>                       │                           │                  │
│   └─────────────────────────────────────┘                           │                  │
│         ▲                                                           │                  │
│         │ Password stripped on save                                 │ Stored via       │
│         └─────────────────── ConnectionManager ─────────────────────┘ Python keyring   │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

1. **Esfregação XML de texto claro**: sempre que os perfis de conexão são serializados no disco (`atbcmder.xml`), a rotina `ConnectionManager.save()` força explicitamente `d["password"] = ""` antes da gravação. Mesmo que alguém não autorizado inspecione seu XML de configuração, nenhuma senha do servidor será revelada. 
2. **Criptografia de chaveiro do sistema macOS**: quando a caixa de seleção **Lembrar senha** é marcada, as senhas são salvas diretamente no chaveiro do macOS por meio da API `keyring` do sistema sob o identificador de serviço seguro `ATBCmder_VFS`. A derivação e o armazenamento de chaves são protegidos pelo Secure Enclave de hardware da Apple. 
3. **Sessões efêmeras na memória**: Se "Lembrar senha" estiver desmarcado, as credenciais serão mantidas estritamente na memória dinâmica (`VFSSessionCache`) durante o ciclo de vida atual do aplicativo e serão apagadas no momento em que o ATBCmder terminar. 

---

## 9. ⚡ Dicas profissionais: operações remotas de alto desempenho

### Dica 1: fila de transferência em segundo plano sem bloqueio (`cm_OperationsPanel`)

Ao copiar diretórios grandes em servidores remotos ou baixar ISOs de vários gigabytes por SFTP, nunca congele seu espaço de trabalho. Todas as operações de arquivos de rede no ATBCmder se integram automaticamente à **Fila de operações em segundo plano**: 

- Pressione **`F5`** para iniciar uma transferência e clique em **Background** (ou deixe-o na fila automaticamente). 
- Abra o painel de operações por meio de **Mostrar ➔ Painel de Operações** (`cm_OperationsPanel`) para monitorar gráficos de largura de banda ao vivo, contagens de bytes por arquivo e estimativas de transferência restantes. 
- Você pode pausar, retomar ou reordenar transferências de rede na fila enquanto continua a navegar pelos arquivos locais em ambos os painéis.

### Dica 2: Cópia de fluxo em protocolos heterogêneos

O mecanismo `stream_copy_file` do ATBCmder permite **streaming direto de servidor para servidor**. Se você arrastar uma pasta de um servidor SFTP no painel esquerdo para um compartilhamento de rede SMB no painel direito: 

- ATBCmder **não** baixa o diretório inteiro para o disco rígido local do Mac antes de reenviar. 
- Os dados são agrupados por meio de um anel de buffer na memória, transmitindo bytes do soquete de origem diretamente para o soquete de destino. Isso elimina o desgaste do disco local e acomoda transferências maiores que a capacidade disponível do SSD local.

### Dica 3: manutenção da rede e prevenção de quedas de conexão

Firewalls de rede com estado e gateways NAT frequentemente interrompem conexões TCP ociosas após 60 a 300 segundos de inatividade. Para evitar sessões desconectadas ao navegar em grandes árvores remotas: 

- A camada `BaseNetworkVFS` do ATBCmder mantém automaticamente os batimentos cardíacos da sessão em conexões ociosas. 
- Se ocorrer uma queda momentânea da rede, o mecanismo interno `_retry()` executa até **3 novas tentativas** usando espera exponencial (`2^attempt` intervalos de segundos) antes de relatar uma falha de conexão.

### Dica 4: Editando arquivos remotos com ciclo de vida de upload automático

Precisa editar um script `nginx.conf` ou Python diretamente em um servidor remoto? 

1. Realce o arquivo remoto na visualização do painel SFTP ou WebDAV. 
2. Pressione **`F4`** (`Fn+F4`). 
3. ATBCmder baixa o arquivo para uma sandbox temporária isolada (`/tmp/`) e o abre no Editor integrado. 
4. Cada vez que você pressiona **`Cmd+S`** (`⌘S`), o ATBCmder aciona `_upload_vfs_temp()`, transmitindo o arquivo atualizado de volta para o servidor remoto de forma assíncrona e exibindo uma confirmação na barra de status. 
5. Ao fechar o editor, o arquivo temporário é desvinculado com segurança de `/tmp/`. 

---

## 10. Alertas de sistema e segurança

> [!AVISO] 
> **Incompatibilidade de verificação de chave de host SSH** 
> Se um servidor SFTP regenerar suas chaves de host (por exemplo, após uma reinstalação do sistema operacional) ou se for tentada uma interceptação de rede man-in-the-middle, o ATBCmder detecta que a chave do servidor não corresponde à impressão digital registrada em `~/.ssh/known_hosts`. 
> Nunca ignore avisos de chave de host em redes Wi-Fi públicas não confiáveis ​​sem verificar de forma independente a impressão digital da chave pública do servidor com o administrador do sistema. 

> [!IMPORTANTE] 
> **Espaço de cache temporário para arquivos remotos grandes** 
> Ao visualizar (`F3`) ou editar (`F4`) arquivos de vários gigabytes armazenados em servidores VFS remotos, o ATBCmder transmite o item de destino para seu volume `/tmp` local. Certifique-se de que o contêiner APFS principal do seu Mac tenha espaço de armazenamento livre suficiente antes de abrir grandes arquivos remotos de vídeo ou banco de dados. 

> [!CUIDADO] 
> **Desmontando compartilhamentos de rede remotos** 
> Para compartilhamentos SMB montados via macOS `mount_smbfs`, encerrar a conectividade de rede sem desconectar pode deixar identificadores de montagem obsoletos em `/Volumes/`. Sempre use o menu da unidade do painel ou a ação de desconexão antes de fechar seu laptop ou mudar de rede Wi-Fi. 

---

## 11. Tabela de referência do teclado mestre de matriz dupla

| Categoria | Descrição da ação | Atalho do macOS | Chave do Comandante Clássico | ID do comando | 
| :--- | :--- | :--- | :--- | :--- | 
| **Operações de arquivo** | Empacotar arquivos/pastas selecionados | `Alt+F5` / `⌥F5` | `Alt+F5` | `cm_PackFiles` | 
| **Operações de arquivo** | Extrair arquivo(s) selecionado(s) | `Alt+F9` / `⌥F9` | `Alt+F9` | `cm_ExtractFiles` | 
| **Operações de arquivo** | Navegue dentro do contêiner de arquivo | `Enter` / `⏎` | `Enter` | `cm_Open` | 
| **Operações de arquivo** | Sair do arquivo para o diretório pai | `Backspace` / `⌫` | `Backspace` | `cm_ChangeDirToParent` | 
| **Operações de arquivo** | Visualizar arquivo dentro do arquivo | `F3` / `Fn+F3` | `F3` | `cm_View` | 
| **Operações de arquivo** | Editar arquivo dentro do arquivo (ao vivo) | `F4` / `Fn+F4` | `F4` | `cm_Edit` | 
| **Operações de arquivo** | Extrair apenas itens selecionados | `F5` / `Fn+F5` | `F5` | `cm_Copy` | 
| **Operações de arquivo** | Divida arquivos grandes em volumes | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | 
| **Operações de arquivo** | Remontar peças de volume dividido | Menu: Arquivos ➔ Combinar Arquivos | — | `cm_FileLinker` / `cm_Combine` | 
| **Conexões de rede**| Caixa de diálogo Conexão rápida de rede | Menu: Rede | — | `cm_NetworkConnect` | 
| **Conexões de rede**| Gerenciar conexões de rede | Menu: Rede | — | `cm_ManageConnections` | 
| **Conexões de rede**| Conexão rápida ao servidor FTP | `Ctrl+S` / `⌃S` | `Ctrl+S` | `cm_FTPConnect` | 
| **Conexões de rede**| Desconectar compartilhamento de rede remota | Menu: Rede | — | `cm_NetworkDisconnect` | 
| **Gerenciamento de transferências**| Fila de transferência de operações abertas | Menu: Mostrar | — | `cm_OperationsPanel` | 
| **Gerenciamento de transferências**| Pausar/retomar fila ativa | `Space` (na fila)| `Space` | — |

--- 

<div align="center"> 
<p>Pronto para personalizar teclas de atalho, visualizações de painel e comportamento de aplicativos?</p> 
<p><strong><a href="preferences_and_customization.md">Prossiga para o Capítulo 7: Preferências e personalização &rarr;</a></strong></p> 
</div>