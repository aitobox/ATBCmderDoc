# Capítulo 5: Herramientas avanzadas y automatización

En la gestión de archivos de gran volumen, la manipulación básica de archivos (copiar, mover y eliminar elementos individuales) es sólo el comienzo. Los ingenieros profesionales, administradores de sistemas, creadores de contenido y analistas de datos frecuentemente enfrentan desafíos operativos complejos: reestructurar miles de activos digitales con nombres inconsistentes, aislar regresiones de código sutiles entre ramas de lanzamiento paralelas, mantener espejos sincronizados en matrices de almacenamiento de red, localizar archivos de configuración profundamente enterrados y verificar criptográficamente la integridad de los archivos. 

ATBCmder transforma estas tareas que requieren mucha mano de obra en operaciones rápidas y deterministas. En lugar de requerir secuencias de comandos de línea de comandos externas, utilidades por lotes de terceros o aplicaciones de diferenciación independientes y torpes, ATBCmder integra un conjunto de automatización integral directamente en su núcleo ortodoxo de doble panel. Ya sea que necesite ejecutar sustituciones de expresiones regulares en un archivo fotográfico completo, realizar una sincronización de directorios bidireccional con hash a nivel de contenido o alimentar resultados de búsqueda con múltiples filtros en un espacio de trabajo virtual, ATBCmder proporciona las herramientas que necesita con total eficiencia de teclado. 

---

## 1. Inicio rápido visual: motor de automatización y matriz de comandos

ATBCmder divide las herramientas eléctricas y la automatización en seis dominios funcionales especializados que interactúan perfectamente con la interfaz de panel dual: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                PANEL DUAL DE ARCHIVOS                                  │
│          Panel izquierdo (Origen / Carpeta A)          Panel derecho (Destino / Carpeta B)│
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                          │                                             │
│  [1] Renombrado masivo (Ctrl+M)          │  [2] Comparador de diferencias Diff (⌘⇧F12) │
│      Comodines, RegEx, Contadores, Vista │      Resaltado de líneas, Fusión, Edición   │
│                                          │                                             │
│  [3] Sincronización de carpetas (⇧F12)   │  [4] Búsqueda avanzada (Alt+F7)             │
│      Contenido/Fecha, Espejo asimétrico  │      Spotlight / Escaneo ➔ Enviar a lista   │
│                                          │                                             │
│  [5] Barra de comandos semánticos (/)    │  [6] Utilidades de archivos y seguridad     │
│      Búsqueda Spotlight, Consultas IA    │      Dividir/Unir, Checksum, Borrado seguro │
│                                          │                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [Enviar a lista] ➔ Carga los resultados en una pestaña virtual para acciones en lote │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Hoja de referencia de automatización de matriz dual

| Acción | Atajo de teclado en macOS | Tecla Commander clásica | ID de comando | Descripción | 
| :--- | :--- | :--- | :--- | :--- | 
| **Cambio de nombre múltiple por lotes** | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | Abre el cuadro de diálogo de la herramienta Cambio de nombre múltiple por lotes. | 
| **Diferenciación de archivos en paralelo** | `Meta+Shift+F12` / `⌘⇧F12` | `Meta+Shift+F12` | `cm_FileDiff` / `cm_CompareFiles` | Compara dos archivos seleccionados uno al lado del otro (`Shift+F3` para `cm_CompareContents`). | 
| **Sincronización de directorio** | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | Compara y sincroniza directorios de panel dual. | 
| **Búsqueda avanzada de archivos** | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` / `cm_FileSearch` | Abre el cuadro de diálogo de búsqueda de filtros múltiples. | 
| **Búsqueda rápida destacada** | `Ctrl+Shift+F` / `⌃⇧F` | `Ctrl+Shift+F` | *(Menú de comandos)* | Inicia la búsqueda instantánea de metadatos de Spotlight. | 
| **Entrada de comando semántico**| `/` | `/` | `cm_VisSemanticCommand` | Activa la barra de comandos de lenguaje natural integrada. | 
| **Dividir archivo grande** | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | Divide un archivo grande en partes numeradas. | 
| **Combinar archivos divididos** | Menú: Archivos ➔ Combinar archivos | — | `cm_FileLinker` / `cm_Combine` | Vuelve a ensamblar los fragmentos `.001`, `.002` en una sola fila. | 
| **Calcular suma de comprobación** | `Ctrl+X` / `⌃X` | `Ctrl+X` | `cm_CheckSumCalc` / `cm_CalculateChecksum` | Calcula hashes MD5, SHA-1, SHA-256 o SHA-512. | 
| **Verificar archivo de suma de comprobación** | Menú Herramientas | — | `cm_CheckSumVerify` / `cm_VerifyChecksum` | Verifica archivos con `.md5`, `.sha256` o `.sfv`. | 
| **Borrado seguro (Wipe)** | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | Sobrescribe y elimina archivos de forma segura. | 
| **Ejecutar terminal del sistema** | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` | Genera la terminal macOS en la ruta del panel actual. | 

---

## 2. Herramienta de renombrado masivo (Multi-Rename) por lotes (`Ctrl+M` / `⌃M` / `cm_MultiRename`)

Cambiar el nombre de docenas o cientos de archivos manualmente es tedioso y propenso a errores. La **Herramienta de renombrado masivo (Multi-Rename) por lotes** (`cm_MultiRename`, asignada a `fmultirename.pas` en la arquitectura clásica) le permite definir patrones de nombres flexibles, aplicar contadores de secuencia dinámicos, realizar conversiones de casos y ejecutar poderosas reglas de búsqueda y reemplazo de expresiones regulares (RegEx) con garantías de seguridad visual en tiempo real. 

![Batch Multi-Rename Tool](images/multi_rename_dialog.png) 
*Figura 5.1: La herramienta de cambio de nombre múltiple por lotes que presenta filas de vista previa en vivo, máscaras de tokens, parámetros de contador numérico y detección de duplicados.*

### 2.1 El flujo de trabajo de cambio de nombre múltiple

1. **Seleccionar archivos**: en el panel de archivos activos, seleccione los archivos o directorios cuyo nombre desea cambiar usando `Space`, `Insert` o la selección con comodín (`+`). Si no se selecciona nada, se utiliza el elemento debajo del cursor. 
2. **Herramienta de inicio**: Presione **`Ctrl+M`** (`⌃M`) o elija **Archivos ➔ Herramienta de renombrado masivo (Multi-Rename)...** en la barra de menú. 
3. **Configurar plantillas y reglas**: ingrese máscaras de nombre de archivo/extensión, establezca opciones de contador o defina cadenas de búsqueda y reemplazo. 
4. **Inspeccionar vista previa en vivo**: la tabla de 3 columnas (`Old Name`, `New Name`, `Directory`) se actualiza instantáneamente con cada pulsación de tecla. 
5. **Ejecutar**: haga clic en **Iniciar cambio de nombre** (o presione `Enter`). ATBCmder realiza los cambios de nombre de forma atómica y actualiza los paneles de archivos. 

---

### 2.2 Fichas de plantilla y división de rango

ATBCmder utiliza tokens intuitivos entre corchetes para hacer referencia a partes de los metadatos del archivo original: 

| Ficha | Descripción | Entrada de ejemplo | Valor resultante | 
| :--- | :--- | :--- | :--- | 
| **`[N]`** | Nombre de archivo original sin extensión | `report_2026.pdf` | `report_2026` | 
| **`[E]`** | Extensión de archivo original (sin punto) | `archive.tar.gz` | `gz` | 
| **`[C]`** | Contador numérico secuencial | *(Archivo 3 en la lista)* | `003` (depende de la configuración de los dígitos) | 
| **`[Y]`** | Año de modificación del archivo de 4 dígitos | `2026-09-06` | `2026` | 
| **`[M]`** | Mes de modificación del archivo de 2 dígitos | `September` | `09` | 
| **`[D]`** | Día de modificación del archivo de 2 dígitos | `6th` | `06` | 
| **`[h]`** | Hora de 2 dígitos (reloj de 24 horas) | `14:30:15` | `14` | 
| **`[m]`** | Minuto de 2 dígitos | `14:30:15` | `30` | 
| **`[s]`** | Segundo de 2 dígitos | `14:30:15` | `15` |

#### División de rango de caracteres (`[Na-b]` / `[Ea-b]`)

Puede extraer rangos de caracteres específicos del nombre o extensión original utilizando la división de índice basada en 1: 

- **`[N1-4]`**: Extrae los primeros 4 caracteres del nombre. Para `Document_Final.txt`, esto produce `Docu`. 
- **`[N5-]`**: Extrae desde el quinto carácter hasta el final del nombre. Para `DSC_0982.jpg`, esto produce `0982`. 
- **`[N-5]`**: Extrae hasta el quinto carácter. 
- **`[E1-2]`**: Extrae los 2 primeros caracteres de la extensión. Para `archive.html`, esto produce `ht`. 

---

### 2.3 Controles de contador y secuencias numéricas

El grupo **Configuración del contador** permite un control granular sobre la indexación numérica: 

- **Iniciar en**: el número entero inicial para la secuencia del contador (predeterminado: `1`). 
- **Paso**: el valor de incremento agregado para cada archivo posterior (predeterminado: `1`). Establecer el paso en `2` genera `1, 3, 5, 7...`. 
- **Dígitos**: el ancho del relleno de ceros (rango: `1` a `10`). Al configurar los dígitos en `3`, los números se formatean como `001`, `002`, `003`. Establecer dígitos en `1` deshabilita los ceros a la izquierda (`1`, `2`, `3`). 

---

### 2.4 Buscar y reemplazar y expresiones regulares

El grupo **Buscar y reemplazar** permite reemplazar texto en todos los elementos seleccionados: 

- **Buscar**: subcadena de destino o patrón de expresión regular. 
- **Reemplazar con**: Cadena de repuesto. Cuando RegEx está habilitado, las referencias inversas (`$1`, `$2` o `\1`, `\2`) se refieren a grupos de captura. 
- **Usar expresiones regulares (Regex)**: alterna el análisis de expresiones regulares de la biblioteca estándar de Python. 
- **Distingue entre mayúsculas y minúsculas**: cuando no está marcada, la coincidencia ignora las mayúsculas y minúsculas (por ejemplo, coincidir tanto con `.JPG` como con `.jpg`).

#### Potentes ejemplos de sustitución de expresiones regulares

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

### 2.5 Modos de conversión de casos

ATBCmder proporciona normalización instantánea de carcasas sin necesidad de patrones complejos: 

- **Sin cambios**: conserva las mayúsculas originales. 
- **minúsculas**: convierte todo el nombre del archivo y la extensión a minúsculas (`PHOTO_001.JPG` ➔ `photo_001.jpg`). 
- **MAYÚSCULAS**: Convierte todos los caracteres a mayúsculas (`readme.txt` ➔ `README.TXT`). 
- **Primera letra mayúscula**: pone en mayúscula el carácter inicial de cada palabra (`war and peace.epub` ➔ `War And Peace.epub`). 

---

### 2.6 Vista previa en vivo de cuadrícula y protección contra colisiones

Cambiar el nombre de cientos de archivos sin obtener una vista previa puede provocar sobrescrituras de datos desastrosas. ATBCmder implementa una **Arquitectura de seguridad sin accidentes**: 

1. **Vista previa instantánea de rebotes**: a medida que escribe las entradas de la plantilla o ajusta los cuadros de giro, la tabla calcula inmediatamente los nombres de archivo resultantes. 
2. **Detección de objetivos duplicados**: ATBCmder escanea todos los nombres de archivos de salida calculados dentro de la carpeta de destino. Si dos o más archivos se resuelven con exactamente el mismo nombre, o si un nombre de archivo se resuelve con una cadena vacía: 
- Las filas en colisión se resaltan inmediatamente en rojo prominente (`#FFEBEB` / `#D70000` en modo claro, `#4A1515` / `#FF8080` en modo oscuro). 
- El botón **Iniciar cambio de nombre** se **deshabilita** automáticamente. 
- Una información sobre herramientas advierte: *"Se detectaron colisiones de nombres. Resuelva los duplicados antes de cambiar el nombre".* 
3. **Eliminación de colisiones**: una vez que ajusta su contador, plantilla o expresión regular para que todos los nombres de archivos de destino sean únicos, la advertencia se borra y el botón **Iniciar cambio de nombre** se vuelve a habilitar. 

---

### 2.7 Recetas prácticas paso a paso

#### Receta A: cambiar el nombre de las fotos de la cámara digital con marcas de tiempo

Transforme nombres de cámaras crípticos (`IMG_4092.JPG`, `IMG_4093.JPG`) en activos organizados cronológicamente: 

1. Seleccione los archivos de fotos y presione **`Ctrl+M`**. 
2. Establezca **Plantilla de nombre de archivo** en: `Photo_[Y][M][D]_[C]`. 
3. Establezca **Plantilla de extensión** en: `[E]`. 
4. Establezca **Dígitos** en `3`, **Inicio en** en `1`. 
5. Establezca **Conversión de caso** en `lowercase`. 
6. Obtenga una vista previa del resultado: `photo_20260906_001.jpg`, `photo_20260906_002.jpg`. 
7. Presione `Enter` para presentar la solicitud.

#### Receta B: Agregar un prefijo conservando el nombre y la extensión

Prefije un lote de documentos con un código de proyecto: 

1. Seleccione documentos y presione **`Ctrl+M`**. 
2. En **Plantilla de nombre de archivo**, ingrese: `PRJ-ALPHA_[N]`. 
3. Deje **Plantilla de extensión** como `[E]`. 
4. Haga clic en **Iniciar cambio de nombre**. 

---

## 3. Diferenciación de archivos visuales en paralelo (`Meta+Shift+F12` / `⌘⇧F12` / `cm_FileDiff`)

Detectar diferencias entre revisiones de configuración, archivos de código fuente o volcados de datos es una tarea diaria para los usuarios avanzados. ATBCmder incluye un **Visual File Diff Viewer** integrado de lado a lado (`DiffViewerDialog`) que elimina la necesidad de iniciar herramientas externas pesadas. 

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

### 3.1 Iniciar diferenciación de archivos

- **Comparar dos archivos seleccionados**: en un solo panel, seleccione exactamente dos archivos y presione **`Meta+Shift+F12`** (`⌘⇧F12`) o elija **Comandos ➔ Comparar por contenido...**. 
- **Comparar archivos opuestos**: Resalte un archivo en el Panel izquierdo, resalte el archivo correspondiente en el Panel derecho y active `cm_CompareContents`. 
- **Comandos admitidos**: `cm_CompareContents`, `cm_FileDiff` y `cm_CompareByContent` todos enrutan al motor de comparación en paralelo. 

---

### 3.2 Resaltado de diferencias visuales y códigos de color

El motor de diferencias analiza el texto línea por línea utilizando un algoritmo LCS de Hunt-Szymanski optimizado (`TextDiffer`), dividiendo las diferencias en fragmentos codificados por colores: 

| Tipo de diferencia | Resaltado del tema ligero | Resaltado del tema oscuro | Descripción | 
| :--- | :--- | :--- | :--- | 
| **Líneas agregadas** | Esmeralda suave (`#e6ffed`) | Verde bosque oscuro (`#234b2d`) | Líneas presentes solo en el archivo derecho. | 
| **Líneas eliminadas** | Carmesí suave (`#ffeef0`) | Rojo carmesí oscuro (`#552328`) | Líneas presentes en el archivo de la izquierda pero faltantes en el de la derecha. | 
| **Líneas modificadas** | Ámbar suave (`#fff5b1`) | Oro ámbar oscuro (`#50461e`) | Líneas modificadas entre las versiones izquierda y derecha. | 
| **Trozo activo** | Sombra de contraste vivo | Sombra de contraste vivo | El bloque de diferencia actualmente enfocado por el cursor. | 

Cada panel presenta un canal izquierdo dedicado (`LineNumberArea`) que muestra números de línea basados ​​en 1 sincronizados con posiciones diferenciales. 

---

### 3.3 Seguridad de reentrada y desplazamiento sincronizado

Al comparar archivos fuente largos que contienen miles de líneas, navegar a través del código requiere una coordinación estrecha: 

- Al desplazarse por la barra de desplazamiento vertical u horizontal de cualquiera de los editores, se ajusta instantáneamente el editor opuesto con el mismo desplazamiento de píxeles. 
- ATBCmder implementa un **bloqueo de reentrada** interno (`_syncing_vscroll`, `_syncing_hscroll`) que evita bucles de retroalimentación de eventos, tartamudeo o deriva del cursor. 

---

### 3.4 Navegación Hunk y fusión bidireccional

Puede navegar a través de las diferencias sin usar el mouse: 

- **Siguiente diferencia**: Presione **`Alt+Down`** / `⌥↓` (o `Ctrl+Down`). 
- **Diferencia anterior**: Presione **`Alt+Up`** / `⌥↑` (o `Ctrl+Up`). 
- **Saltar a trozo**: al hacer clic directamente en cualquier línea resaltada en cualquier panel, ese trozo se establece automáticamente como activo.

#### Fusión bidireccional (compatibilidad con Vimdiff `dp` / `do`)

Fusione diferencias entre archivos con una sola pulsación de tecla: 

- **Copiar de izquierda a derecha (`→`)**: Presione **`Alt+Right`** / `⌥→` (o `Ctrl+Alt+Right` o Vimdiff `dp` a través de **`Alt+P`**). El fragmento activo en el editor izquierdo reemplaza la sección correspondiente en el editor derecho. 
- **Copiar de derecha a izquierda (`←`)**: Presione **`Alt+Left`** / `⌥←` (o `Ctrl+Alt+Left` o Vimdiff `do` a través de **`Alt+O`**). El fragmento activo en el editor derecho reemplaza la sección correspondiente en el editor izquierdo. 

---

### 3.5 Edición in situ y guardado atómico

A diferencia de los visores de diferencias que tratan el texto como de sólo lectura, ambos paneles de ATBCmder son editores de código completamente funcionales: 

- Escriba, pegue o elimine texto directamente en cualquiera de los editores. 
- Siempre que las ediciones manuales alteren líneas, presione **`F5`** (o `Ctrl+R`) para volver a ejecutar el cálculo de diferencia en los buffers actualizados. 
- Guardar archivo izquierdo: haga clic en **💾 Guardar archivo izquierdo** (o presione `Cmd+S` / `Ctrl+S` mientras el editor izquierdo está enfocado). 
- Guardar archivo derecho: haga clic en **💾 Guardar derecho** (o presione `Cmd+S` / `Ctrl+S` mientras el editor derecho tiene el foco). 

---

### 3.6 Opciones de filtrado de comparación

La barra de herramientas del visor de diferencias le permite aislar los cambios lógicos genuinos del ruido de formato: 

- **Ignorar espacios en blanco (`_cb_ws`)**: ignora los cambios en las pestañas, los espacios finales y la sangría de espacios frente a pestañas. 
- **Ignorar mayúsculas y minúsculas (`_cb_case`)**: realiza comparaciones de caracteres que no distinguen entre mayúsculas y minúsculas. 
- **Ignorar líneas en blanco (`_cb_blank`)**: contrae las adiciones y eliminaciones de líneas vacías, centrándose estrictamente en cambios sustanciales de código. 

---

### 3.7 Detección de diferencias de archivos binarios

Si cualquiera de los archivos seleccionados para comparar contiene bytes nulos o firmas MIME binarias (por ejemplo, imágenes, ejecutables, archivos compilados), ATBCmder invoca automáticamente `BinaryDiffer`: 

- Muestra tamaños de archivos y hashes criptográficos SHA-256 uno al lado del otro. 
- Indica claramente si los archivos binarios son de bytes idénticos o divergentes. 

---

## 4. Sincronización de carpetas (Sync Dirs) (`Shift+F12` / `⇧F12` / `cm_SyncDirs`)

Mantener los árboles de directorios sincronizados en los discos locales, las unidades de respaldo y el almacenamiento en red es la piedra angular de los sistemas confiables. El **Sincronizador de directorios** de ATBCmder (`SyncDirsDialog`, asignado a `fsyncdirsdlg.pas`) compara jerarquías de carpetas completas, determina operaciones direccionales exactas y obtiene una vista previa de cada copia y eliminación de archivos antes de tocar su almacenamiento. 

![Directory Synchronization](images/folder_synchronization.png) 
*Figura 5.2: Cuadro de diálogo de sincronización de directorios que muestra el estado de comparación recursiva, flechas de sincronización direccional y controles de espejo asimétrico.*

### 4.1 Iniciar sincronización de directorios

1. Abra el **Directorio de origen** en el Panel izquierdo y el **Directorio de destino** en el Panel derecho. 
2. Presione **`Shift+F12`** (`⇧F12`) o elija **Comandos ➔ Sincronizar directorios...**. 
3. Aparece el cuadro de diálogo Sincronizar directorios con ambas rutas precargadas en las tarjetas de encabezado. 

---

### 4.2 Métodos de comparación y precisión

Antes de sincronizar, configure sus criterios de comparación en la tarjeta **Sincronizar configuración**: 

| Configuración | Predeterminado | Descripción | 
| :--- | :--- | :--- | 
| **Comparar subdirectorios** | `Enabled` | Atraviesa recursivamente todos los directorios anidados. | 
| **Comparar por contenido** | `Disabled` | Lee y verifica bytes de archivos directamente usando `filecmp.cmp`. Garantiza una precisión del 100 % para archivos con marcas de tiempo idénticas pero con datos modificados. | 
| **Ignorar fecha** | `Disabled` | Compara archivos exclusivamente por tamaño de bytes, ignorando las marcas de tiempo de modificación del sistema de archivos. | 
| **Tolerancia de marca de tiempo FAT/SMB** | `2.0 sec` | Tiene en cuenta automáticamente las resoluciones de marca de tiempo de 2 segundos FAT/FAT32/exFAT, lo que evita indicadores falsos de discrepancia al sincronizar entre macOS y unidades externas. | 

---

### 4.3 Análisis direccional e indicadores de estado

Haga clic en **Comparar** para iniciar un trabajador de comparación en segundo plano sin bloqueo (`SyncCompareWorker`). La tabla de comparación se completa con filas direccionales codificadas por colores: 

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
 

- **`->` (De izquierda a derecha)**: el archivo de la izquierda es más nuevo o existe solo en la izquierda. Acción predeterminada: copiar a la derecha. 
- **`<-` (De derecha a izquierda)**: el archivo de la derecha es más nuevo o existe solo en la derecha. Acción predeterminada: copiar a la izquierda (en modo bidireccional). 
- **`=` (Igual)**: los archivos coinciden en tamaño y marca de tiempo/contenido. Filtrado de la lista de sincronización activa para ahorrar tiempo. 
- **`!=` (Conflicto)**: colisión entre directorio y archivo incompatible o conflicto de marca de tiempo irresoluble. Se omitió durante la sincronización masiva automatizada por motivos de seguridad de los datos. 

---

### 4.4 Duplicación asimétrica versus sincronización simétrica bidireccional

ATBCmder admite dos filosofías de sincronización fundamentalmente diferentes:

#### 1. Sincronización simétrica bidireccional (predeterminada)

- **Objetivo**: alinear ambos directorios para que ambos tengan las últimas versiones de cada archivo. 
- **Acción**: Los archivos marcados `->` se copian Izquierda ➔ Derecha. Los archivos marcados `<-` se copian Derecha ➔ Izquierda. 
- **Seguridad**: No se eliminan archivos en ninguno de los lados.

#### 2. Duplicación asimétrica (`Asymmetric` casilla de verificación habilitada)

- **Objetivo**: Hacer que el directorio derecho sea una réplica exacta e idéntica del directorio izquierdo. 
- **Acción**: Los archivos marcados `->` se copian Izquierda ➔ Derecha. Los archivos de la derecha que *no* existen en la izquierda (`<- Right missing on Left`) se **eliminan permanentemente del directorio derecho**. 
- **Caso de uso**: creación de espejos de respaldo impecables en discos de respaldo externos o recursos compartidos NAS. 

---

### 4.5 Registro de auditoría y seguridad previo a la ejecución

- **Inspeccionar antes de sincronizar**: revise cuidadosamente la tabla completa. Puede ver las rutas relativas exactas y los motivos operativos de cada transferencia. 
- **Detener control**: si es necesario cancelar un trabajo de comparación o sincronización de gran tamaño, haga clic en **Detener**. El hilo en segundo plano termina de forma segura sin dejar archivos parciales dañados. 
- **Registro de auditoría automatizado**: cada copia, sobrescritura y eliminación ejecutadas durante la sincronización se registra en el **Registro de operaciones** interno de ATBCmder (`LogCategory.COPY_MOVE_LINK`, `LogCategory.DELETE`). 

---

## 5. Búsqueda avanzada de archivos y alimentación al cuadro de lista (`Alt+F7` / `⌥F7` / `cm_Search`)

La localización de archivos específicos en estructuras de carpetas anidadas es un cuello de botella administrativo común. ATBCmder proporciona un **Diálogo de búsqueda avanzada de archivos** de alto rendimiento (`SearchDialog`, asignado a `fFindDlg.pas`), que combina la indexación nativa de macOS Spotlight con un motor de escaneo profundo del sistema de archivos y la indispensable capacidad **Feed to Listbox**. 

![Advanced File Search](images/advanced_search_dialog.png) 
*Figura 5.3: Cuadro de diálogo Búsqueda avanzada de archivos con parámetros de filtro múltiple, controles de escaneo profundo y el botón Enviar al cuadro de lista.*

### 5.1 Iniciar la búsqueda

- Presione **`Alt+F7`** (`⌥F7`) en cualquier panel, o elija **Comandos ➔ Buscar archivos...**. 
- El cuadro de diálogo de búsqueda se abre con el campo **Buscar en directorio** precargado con la ruta actual del panel activo. 

---

### 5.2 Backends de búsqueda dual: Spotlight versus escaneo profundo

ATBCmder presenta dos motores de búsqueda especializados: 

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
 

1. **Motor de búsqueda Spotlight (`SpotlightSearchWorker`)**: en macOS, al hacer clic en **Iniciar búsqueda** (o presionar `Enter`) se utiliza el índice de metadatos de Spotlight del sistema (`mdfind`). Recupera miles de rutas coincidentes en gigabytes de almacenamiento en una fracción de segundo. 
2. **Motor de escaneo profundo (`DeepScanWorker`)**: Al hacer clic en **Escaneo profundo** se omite la indexación del sistema y se realiza un recorrido directo y recursivo del sistema de archivos. Esto es fundamental a la hora de buscar: 
- Unidades USB externas o tarjetas SD que tengan desactivada la indexación de Spotlight. 
- Recursos compartidos de archivos de red remota (SMB, SFTP, FTP, WebDAV). 
- Directorios de compilación de desarrolladores excluidos a través de `.metadata_never_index`. 

---

### 5.3 Criterios de búsqueda multifiltro

Ajuste las consultas de búsqueda utilizando parámetros granulares en los grupos **General** y **Filtros avanzados**: 

- **Patrón de nombres de archivos**: 
- *Comodines*: comodines de shell estándar como `*.py`, `invoice_2026_*.pdf` o `test_??.go`. 
- *Subcadenas*: Al ingresar `draft` se encuentra cualquier archivo o carpeta que contenga "borrador". 
- *Expresiones regulares*: marque **Expresión regular** para habilitar la sintaxis de expresiones regulares completa (por ejemplo, `^v\d+\.\d+\.(json|xml)$`). 
- **Buscar texto (búsqueda en archivos)**: 
- Busca contenido de cadenas UTF-8 y ASCII dentro de archivos de texto, código fuente y documentos. 
- Marque **Búsqueda de contenido que distinga entre mayúsculas y minúsculas** para ver coincidencias exactas de casos. 
- **Rango de tamaño de archivo**: 
- Establezca **Tamaño mínimo** y **Tamaño máximo** en kilobytes (`KB`). Establecer el tamaño máximo en `0` deja los límites superiores ilimitados. 
- **Rango de fechas**: 
- Especifique **Modificado en los últimos N días** (por ejemplo, `7` días para buscar trabajo de la semana pasada). 

---

### 5.4 Inspección rápida en los resultados de búsqueda

Mientras navega por los resultados de búsqueda en la lista de resultados: 

- **Ver archivo (`F3`)**: abre instantáneamente el resultado de búsqueda resaltado en Universal Lister. 
- **Editar archivo (`F4`)**: abre el archivo directamente en el editor de texto integrado. 
- **Ir a archivo (`Enter` / `Go to File`)**: cierra el cuadro de diálogo de búsqueda, navega por el panel principal hasta el directorio principal del archivo y coloca el cursor directamente en el archivo. 

---

### 5.5 El poder de "Alimentar al cuadro de lista"

La característica más transformadora de los administradores de archivos ortodoxos es **Feed to Listbox**: 

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
 

1. En el cuadro de diálogo de búsqueda, una vez que se encuentren los archivos coincidentes, haga clic en el botón **Alimentar al cuadro de lista**. 
2. ATBCmder cierra el cuadro de diálogo y abre una nueva **pestaña de resultados de búsqueda virtual** en el panel activo. 
3. En lugar de navegar a cada carpeta individualmente, todos los archivos coincidentes de diferentes profundidades de directorio aparecen en una única tabla plana. 
4. **Ejecutar cualquier acción del comandante**: 
- Seleccione todos o elementos específicos (`Space`, `+`, `Cmd+A`). 
- **Copiar (`F5`)** o **Mover (`F6`)** archivos coincidentes en diversas carpetas a una única carpeta de destino en el panel opuesto. 
- **Cambio de nombre múltiple por lotes (`Ctrl+M`)** todos los resultados de búsqueda coincidentes simultáneamente. 
- **Elimine de forma segura (`F8` o `Alt+Delete`)** archivos temporales no deseados en toda la jerarquía del proyecto de un solo golpe. 

---

## 6. Integración de Spotlight y sistema de comando semántico (`/` y `Ctrl+Shift+F`)

Los flujos de trabajo modernos requieren consultas ágiles más allá de los rígidos diálogos de filtro. ATBCmder integra la indexación de macOS Spotlight directamente con un **Sistema de comando semántico en lenguaje natural** accesible desde la barra de comandos integrada en la parte inferior de la ventana principal. 

![Semantic Command Bar](images/semantic_command.png) 
*Figura 5.4: La barra de comandos semánticos analiza una consulta en lenguaje natural con plantillas de autocompletado en vivo.* 

![Semantic Search](images/semantic_search_bar.png) 
*Figura 5.5: Resultados de la búsqueda semántica mostrados directamente dentro del panel activo.*

### 6.1 Activación de comandos semánticos

- **Presione `/`**: En el panel de archivos activos, simplemente presione la tecla de barra (`/`). ATBCmder inmediatamente enfoca la barra de edición de comandos inferior y la completa previamente con `/`. 
- **Atajo de búsqueda de Spotlight**: presione **`Ctrl+Shift+F`** (`⌃⇧F`) o `Cmd+Shift+F` para abrir la interfaz de filtro semántico. 
- **Descartar**: presione `Escape` para borrar el filtro y restaurar la lista de directorio estándar. 

---

### 6.2 Alcances: Local (`/`) vs. Global (`//`)

ATBCmder diferencia entre filtrado a nivel de carpeta y descubrimiento en todo el sistema mediante convenciones de prefijo:

#### 1. Alcance del directorio local (`/<query>`)

Las consultas que comienzan con una sola barra operan exclusivamente en el directorio abierto en el panel activo (y sus subcarpetas si se especifican opciones recursivas): 

- `/larger than 10MB`: muestra solo archivos de más de 10 Megabytes en la carpeta actual. 
- `/> 50MB`: abreviatura numérica para filtrado de tamaño. 
- `/today modified pdf`: Filtros para documentos PDF modificados en las últimas 24 horas. 
- `/images`: Muestra solo formatos de imágenes rasterizadas y vectoriales. 
- `/source code`: muestra Python, C++, Rust, Go, JavaScript y otros archivos fuente. 
- `/contains "API_KEY"`: Filtros para archivos de texto que contienen la cadena "API_KEY". 
- `/hide *.log`: Oculta los archivos de registro de la pantalla activa.

#### 2. Alcance del sistema global (`//<query>`)

Las consultas que comienzan con una doble barra consultan todo el volumen del sistema macOS a través de Spotlight: 

- `//today modified pdf`: busca todos los documentos PDF modificados hoy en todo su Mac. 
- `//larger than 1GB dmg`: Localiza todos los instaladores de imágenes de disco que superan 1 GB. 
- `//code contains "OAuth2Handler"`: busca todos los archivos fuente de todo el sistema que contienen "OAuth2Handler". 

---

### 6.3 Consultas semánticas asistidas por IA (`?` o `/?`)

Cuando se configura con un proveedor de IA (Google Gemini, OpenAI, Anthropic Claude u Ollama local) en *Preferencias ➔ Filtro semántico*: 

- Prefijar una consulta con `?` o `/?` dirige la instrucción en lenguaje natural a través de un analizador LLM. 
- Ejemplo: `/? find all final invoices sent to client Acme last quarter over $5000` 
- La IA traduce frases humanas complejas en atributos precisos de metadatos de Spotlight (`kMDItemFSSize`, `kMDItemContentModificationDate`, `kMDItemTextContent`), mostrando archivos coincidentes instantáneamente en el panel. 

---

### 6.4 Autocompletar, catálogo (`/help`) e historial (`/history`)

Mientras escribe en el cuadro de edición del comando semántico: 

- **Ventana emergente de finalización interactiva**: un menú desplegable (`SemanticCompletionPopup`) muestra sugerencias de plantillas contextuales basadas en el catálogo integrado (`semantic-command-templates.xml`). Utilice las flechas `Down` y `Up` para resaltar sugerencias y presione `Tab` o `Enter` para aceptar. 
- **Catálogo de ayuda (`/help`)**: al escribir `/help` se abre el **Diálogo de ayuda de comandos semánticos**, que enumera docenas de ejemplos de búsqueda en categorías (Tamaño, Fecha, Tipo de archivo, Contenido, Etiquetado). Al hacer doble clic en cualquier entrada, se inserta en la línea de comando. 
- **Historial de comandos (`/history`)**: Al escribir `/history` se muestra un registro cronológico de todos los comandos semánticos ejecutados previamente con marcas de tiempo de ejecución, lo que permite una recuperación instantánea. 

---

### 6.5 Modificadores de acción del panel instantáneo

La barra de comandos semántica también puede manipular las selecciones del panel y la clasificación sin tocar el mouse: 

| Comando Semántico | Acción ejecutada | 
| :--- | :--- | 
| `/select all visible` | Selecciona todos los elementos que se muestran actualmente después del filtrado. | 
| `/clear selection` | Deselecciona todos los elementos del panel. | 
| `/invert selection` | Invierte el estado de selección de archivo actual. | 
| `/select images` | Agrega todos los archivos de imagen en el panel a la selección actual. | 
| `/sort by size descending` | Ordena la tabla de archivos por tamaño de mayor a menor. | 
| `/reset sort` | Restaura la clasificación de nombres alfabética predeterminada. | 
| `/group by date` | Agrupa archivos dinámicamente por corchetes de fecha de modificación. | 
| `/clear filter` | Elimina todos los filtros semánticos activos y restaura la lista completa del directorio. | 

---

## 7. Utilidades de archivos esenciales e integridad de datos

Más allá de la búsqueda y el cambio de nombre por lotes, ATBCmder integra un conjunto de utilidades esenciales del sistema diseñadas para administrar archivos grandes, auditar la seguridad y verificar la integridad criptográfica.

### 7.1 Divisor de archivos grandes (`cm_FileSpliter` / `cm_Split` / `Alt+F6`)

Al transferir imágenes de disco masivas, archivos de video o contenedores de máquinas virtuales a través de dispositivos de almacenamiento con límites de tamaño del sistema de archivos (como el límite de 4 GB de FAT32) o límites de archivos adjuntos de correo electrónico, el **File Splitter** (`SplitWorker`) divide los archivos en segmentos secuenciales numerados: 

1. Seleccione el archivo grande en el panel activo. 
2. Elija **Archivos ➔ Dividir archivo...** (o active `cm_Split`). 
3. Elija el directorio de destino (el valor predeterminado es el panel opuesto). 
4. Seleccione un tamaño de fragmento estándar preestablecido o ingrese un tamaño de byte personalizado: 
- **1,44 MB**: disquete heredado de 3,5". 
- **700 MB**: Capacidad CD-R estándar. 
- **4,7 GB**: Capacidad de DVD-R de una sola capa. 
- **100 MB**: fragmento de carga estándar. 
- **Tamaño personalizado**: umbral de bytes, KB, MB o GB definido por el usuario. 
5. Haga clic en **Aceptar**. ATBCmder divide el archivo fuente en un hilo de trabajo en segundo plano, creando `.001`, `.002`, `.003`... archivos de secuencia. 

---

### 7.2 Vinculador y combinador de archivos (`cm_FileLinker` / `cm_Combine` / `Alt+F7`)

Reensamblar fragmentos de archivos divididos en el archivo original intacto es sencillo: 

1. En el panel de archivos, resalte la **primera parte dividida** (debe terminar con la extensión `.001`). 
2. Elija **Archivos ➔ Combinar archivos...** (o active `cm_Combine`). 
3. ATBCmder detecta automáticamente todas las piezas secuenciales (`.001`, `.002`, `.003`... hasta `.999`). 
4. Seleccione el nombre del archivo de salida y el directorio de destino. 
5. Haga clic en **Aceptar**. El trabajador en segundo plano (`CombineWorker`) concatena secuencialmente las partes nuevamente en una réplica binaria exacta byte por byte. 

---

### 7.3 Sumas de verificación criptográficas y verificación (`cm_CheckSumCalc`, `cm_CheckSumVerify`)

Verificar que los archivos descargados, las imágenes de disco o las copias de seguridad de archivos no hayan sido dañados o alterados es vital para la integridad de los datos. ATBCmder incluye una **Calculadora y verificador de suma de comprobación** integrada (`ChecksumDialog`). 

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

#### Calcular hashes (`cm_CheckSumCalc` / `Ctrl+X`)

1. Seleccione uno o más archivos en el panel. 
2. Elija **Archivos ➔ Calcular suma de comprobación...** (o presione `Ctrl+X`). 
3. Seleccione el algoritmo que desee: **MD5**, **SHA1**, **SHA256** o **SHA512**. 
4. Haga clic en **Calcular**. El trabajador transmite archivos a través de fragmentos de 64 KB en segundo plano sin bloquear la interfaz. 
5. Haga clic en **Guardar en archivo** para exportar los hash a un archivo de manifiesto estándar `.sha256` o `.md5`.

#### Verificación de manifiestos de suma de comprobación (`cm_CheckSumVerify`)

1. Elija **Archivos ➔ Verificar sumas de verificación...**. 
2. Seleccione un archivo de suma de verificación existente (`.sha256`, `.md5`, `.sha1`, `.sha512` o `.sfv`). 
3. ATBCmder analiza automáticamente el manifiesto, localiza los archivos correspondientes en el mismo directorio, recalcula los hashes en el disco y presenta un informe de estado codificado por colores: 
- **`OK`**: El archivo coincide perfectamente con la suma de comprobación. 
- **`FAILED`**: ¡Se detectó corrupción o modificación de datos! 
- **`MISSING`**: el archivo de referencia no se encuentra en el directorio. 

---

### 7.4 Destrucción/borrado seguro de archivos (`cm_Wipe` / `Alt+Delete` / `⌥⌫`)

La eliminación de archivos estándar simplemente desvincula las entradas del directorio, dejando intactos los bloques de datos sin procesar en el disco, donde las utilidades de recuperación pueden extraerlos. Cuando maneje claves, credenciales o código fuente propietario confidenciales, utilice **Eliminación/borrado seguro** (`cm_Wipe`): 

1. Seleccione los archivos o directorios confidenciales. 
2. Presione **`Alt+Delete`** (`⌥⌫`) o elija **Archivo ➔ Eliminación segura (borrar)...**. 
3. Confirme el mensaje de alerta de seguridad. 
4. **La secuencia de destrucción criptográfica de múltiples pasadas (`wipe_path`)**: 
- **Pase 1**: sobrescribe toda la longitud de bytes del archivo con bytes pseudoaleatorios criptográficamente seguros (`os.urandom`). 
- **Pase 2**: sobrescribe todo el archivo con cero bytes nulos (`\x00`). 
- **Pase 3**: sobrescribe con bytes aleatorios nuevos. 
- **Sincronización de hardware**: llama a `os.fsync()` en el descriptor de archivo subyacente para forzar que el sistema operativo y la caché del controlador de almacenamiento escriban datos en medios físicos. 
- **Truncar y desvincular**: trunca el archivo a 0 bytes antes de llamar a `os.unlink()`. 
- **Borrado de directorios**: borra recursivamente todos los archivos contenidos antes de desvincular los directorios principales. 

---

### 7.5 Terminal del sistema integrado (`Ctrl+J` / `⌃J` / `cm_RunTerm`)

Si bien ATBCmder se destaca en los flujos de trabajo gráficos de doble panel, a menudo se requiere acceso al shell para la compilación, las ramas de git o la administración del servidor: 

- Presione **`Ctrl+J`** (`⌃J`) o elija **Comandos ➔ Ejecutar terminal**. 
- ATBCmder abre inmediatamente macOS **Terminal.app** (o su emulador de terminal predeterminado configurado) con su directorio de trabajo inicializado en la ruta exacta abierta en el panel activo. 
- No es necesario escribir `cd /Users/...` ni arrastrar carpetas a las ventanas del terminal. 

---

## 8. ⚡ Consejos profesionales y flujos de trabajo de automatización de profundidad

### 8.1 Receta: Búsqueda recursiva ➔ Enviar al cuadro de lista ➔ Cambio de nombre múltiple

**Objetivo**: Eliminar los números de versión de cientos de archivos de recursos repartidos en 50 subcarpetas anidadas. 

1. Abra la raíz del proyecto en el Panel izquierdo. 
2. Presione **`Alt+F7`** para abrir la Búsqueda. 
3. En Patrón de nombres de archivos, ingrese: `*_v[0-9]*.png`. 
4. Haga clic en **Iniciar búsqueda**. Una vez que aparezcan los recursos coincidentes, haga clic en **Alimentar al cuadro de lista**. 
5. En la pestaña del panel virtual resultante, seleccione todos los archivos con **`Cmd+A`**. 
6. Presione **`Ctrl+M`** para iniciar la herramienta de cambio de nombre múltiple. 
7. En **Buscar**, ingrese: `_v\d+`. Habilite **Usar expresiones regulares (Regex)**. 
8. Deje **Reemplazar con** vacío. 
9. Verifique que la tabla de vista previa en vivo muestre nombres de archivos limpios sin sufijos de versión. 
10. Haga clic en **Iniciar cambio de nombre**. ¡ATBCmder cambia el nombre de cada archivo en las 50 subcarpetas al instante! 

---

### 8.2 Receta: Duplicación de copia de seguridad NAS y en la nube segura con sincronización asimétrica

**Objetivo**: Mantener una réplica externa idéntica de sus documentos en una unidad SSD externa o NAS SMB sin que se acumulen archivos duplicados. 

1. Abra `~/Documents` local en el Panel izquierdo. 
2. Abra `/Volumes/BackupSSD/Documents` en el Panel derecho. 
3. Presione **`Shift+F12`** (`cm_SyncDirs`). 
4. En Configuración, asegúrese de que **Comparar subdirectorios** esté marcado. 
5. Marque **Asimétrico (Eliminar destino si falta en el origen)**. 
6. Haga clic en **Comparar**. 
7. Revise la lista: 
- Las flechas azul/verde (`->`) indican los archivos que se copiarán en la copia de seguridad. 
- Las eliminaciones en rojo (`<-`) indican archivos obsoletos en el disco de respaldo que desde entonces ha eliminado localmente. 
8. Haga clic en **Sincronizar**. Su unidad de respaldo ahora es un espejo de su carpeta local. 

---

### 8.3 Receta: Manifiestos de hash forense antes del almacenamiento de archivos a largo plazo

**Objetivo**: Calcular y almacenar sumas de comprobación criptográficas para un proyecto de varios terabytes antes de trasladarlo a una cinta fría o al almacenamiento en un glaciar en la nube. 

1. Navegue hasta el directorio que contiene los entregables de su proyecto. 
2. Seleccione todos los elementos (`Cmd+A`) y presione **`Ctrl+X`** (`cm_CheckSumCalc`). 
3. Establezca el algoritmo en **SHA256**. 
4. Haga clic en **Calcular**. El trabajador de hash de transmisión procesa los archivos en segundo plano. 
5. Haga clic en **Guardar en archivo** y asígnele el nombre `MANIFEST-SHA256.txt`. 
6. Siempre que recupere los archivos años después, simplemente seleccione `MANIFEST-SHA256.txt` y ejecute **Verificar sumas de verificación** para garantizar cero bits podridos o corrupción silenciosa. 

---

### 8.4 Receta: combinación de filtrado semántico de lenguaje natural con vista de rama plana (`Cmd+B`)

**Objetivo**: buscar y organizar todos los archivos multimedia en una estructura de directorio profunda y compleja sin abrir cuadros de diálogo de búsqueda. 

1. Resalte la carpeta de su proyecto de nivel superior y presione **`Cmd+B`** (`cm_FlatView`) para aplanar todos los contenidos de las subcarpetas en una sola lista. 
2. Presione **`/`** para enfocar la barra de comandos semánticos. 
3. Escriba: `/images larger than 5MB`. 
4. La lista aplanada aísla instantáneamente imágenes de alta resolución en cada directorio anidado. 
5. Presione `/select all visible`, luego presione **`F5`** para copiarlos todos en un directorio de destino organizado en el panel opuesto. 
6. Presione `Cmd+B` nuevamente para restaurar la exploración normal del árbol jerárquico. 

---

## 9. Alertas de seguridad, rendimiento y sistema

> [!CAUTION] 
> **Irreversibilidad de sincronización de directorios asimétrica** 
> Habilitar la opción **Asimétrica** en Sincronización de carpetas (Sync Dirs) (`Shift+F12`) hace que los archivos en el directorio de destino que no existen en el origen se **eliminen permanentemente**. Realice siempre una inspección visual de la tabla de vista previa de comparación antes de hacer clic en **Sincronizar**. 

> [!WARNING] 
> **Sustituciones de expresiones regulares con múltiples cambios de nombre** 
> Al realizar sustituciones de expresiones regulares con referencias inversas (`$1`, `$2`), asegúrese de que los números de su grupo de captura coincidan con los paréntesis en su patrón. Pruebe su patrón con las filas de la tabla de vista previa en vivo antes de hacer clic en **Iniciar cambio de nombre**. Si aparecen nombres duplicados de destino, ATBCmder bloquea la ejecución para protegerlo de la pérdida de datos. 

> [!IMPORTANT] 
> **Limitaciones de destrucción de unidades de estado sólido (SSD)** 
> La utilidad Secure Wipe (`cm_Wipe` / `Alt+Delete`) sobrescribe los datos del archivo con múltiples pases de bytes aleatorios y cero, seguidos de una llamada `fsync`. Sin embargo, las unidades de estado sólido (SSD) modernas utilizan algoritmos de nivelación de desgaste y sobreaprovisionamiento a nivel de controlador que pueden redirigir las escrituras a bloques flash alternativos. Para eliminar SSD de alta seguridad, combine la destrucción de archivos con el cifrado de disco completo de macOS FileVault. 

> [!NOTE] 
> **Disponibilidad destacada en volúmenes de red y FAT** 
> Fast Spotlight Search (`Ctrl+Shift+F`) se basa en índices de metadatos de macOS, que están activos de forma predeterminada en las unidades APFS internas. Es posible que Spotlight no indexe los montajes de red remotos (SMB, SFTP) y las unidades exFAT externas. Si una consulta de Spotlight no arroja resultados en una unidad externa, utilice **Escaneo profundo** (`Alt+F7`) o habilite el escaneo de directorio recursivo. 

> [!TIP] 
> **Compatibilidad con teclas de función de Apple (`Fn`)** 
> En Apple Magic Keyboards y MacBooks, las teclas de función (`F1`-`F12`) utilizan de forma predeterminada acciones de hardware (brillo, volumen). Para presionar `Shift+F12` o `Alt+F7`, mantenga presionada la tecla **`Fn`**: `Fn+Shift+F12`, `Fn+Alt+F7`. Alternativamente, habilite **"Usar teclas F1, F2, etc. como teclas de función estándar"** en macOS *Configuración del sistema ➔ Teclado ➔ Atajos de teclado ➔ Teclas de función*. 

---

## 10. Tabla de referencia del teclado maestro de matriz dual

| Área Funcional | Descripción de la acción | Atajo de teclado en macOS | Tecla Commander clásica | ID de comando | 
| :--- | :--- | :--- | :--- | :--- | 
| **Cambio de nombre múltiple** | Inicie la herramienta de cambio de nombre múltiple por lotes | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | 
| **Cambio de nombre múltiple** | Ejecutar / Iniciar Renombrar | `Enter` / `⏎` | `Enter` | — | 
| **Cambio de nombre múltiple** | Herramienta Cancelar/Cerrar | `Esc` | `Esc` | — | 
| **Diferenciación de archivos** | Comparar archivos/paneles seleccionados | `Meta+Shift+F12` / `⌘⇧F12` | `Meta+Shift+F12` | `cm_FileDiff` / `cm_CompareFiles` | 
| **Diferenciación de archivos** | Saltar a la siguiente diferencia | `Alt+Down` / `⌥↓` | `Ctrl+Down` | — | 
| **Diferenciación de archivos** | Saltar a la diferencia anterior | `Alt+Up` / `⌥↑` | `Ctrl+Up` | — | 
| **Diferenciación de archivos** | Copiar trozo de izquierda a derecha | `Alt+Right` / `⌥→` / `Alt+P` | `Ctrl+Alt+Right` | — | 
| **Diferenciación de archivos** | Copiar trozo de derecha a izquierda | `Alt+Left` / `⌥←` / `Alt+O` | `Ctrl+Alt+Left` | — | 
| **Diferenciación de archivos** | Guardar cambios en el editor enfocado | `Cmd+S` / `⌘S` | `Ctrl+S` | — | 
| **Diferenciación de archivos** | Recalcular diferencias | `F5` / `Fn+F5` | `Ctrl+R` | — | 
| **Sincronización de directorio**| Abra Sincronizar directorios | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | 
| **Sincronización de directorio**| Iniciar comparación de directorios | `Alt+C` / `⌥C` | `Enter` | — | 
| **Sincronización de directorio**| Cancelar comparación/sincronización | Haga clic en `Stop` | `Esc` | — | 
| **Búsqueda de archivos** | Abrir cuadro de diálogo de búsqueda avanzada | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` / `cm_FileSearch` | 
| **Búsqueda de archivos** | Ver resultados en Universal Lister | `F3` / `Fn+F3` | `F3` | `cm_View` | 
| **Búsqueda de archivos** | Editar resultado en el editor de texto | `F4` / `Fn+F4` | `F4` | `cm_Edit` | 
| **Búsqueda de archivos** | Ir a Archivo en Panel Activo | `Enter` / `⏎` | `Enter` | — | 
| **Búsqueda de archivos** | Enviar resultados al panel virtual | Haga clic en `Feed to listbox` | Haga clic en `Feed to listbox` | — *(Acción de diálogo)* | 
| **Enfoque y PNL**| Búsqueda rápida destacada | `Ctrl+Shift+F` / `⌃⇧F` | `Ctrl+Shift+F` | *(Menú de comandos)* | 
| **Enfoque y PNL**| Activar barra de comandos semántica | `/` | `/` | `cm_VisSemanticCommand` | 
| **Enfoque y PNL**| Descartar filtro semántico | `Esc` | `Esc` | — | 
| **Utilidades de archivos**| Dividir archivo en trozos | `Alt+F6` / `⌥F6` | `Alt+F6` | `cm_FileSpliter` / `cm_Split` | 
| **Utilidades de archivos**| Combinar trozos divididos numerados | Menú: Archivos ➔ Combinar archivos | — | `cm_FileLinker` / `cm_Combine` | 
| **Utilidades de archivos**| Calcular suma de comprobación (Hash) | `Ctrl+X` / `⌃X` | `Ctrl+X` | `cm_CheckSumCalc` / `cm_CalculateChecksum` | 
| **Utilidades de archivos**| Verificar archivo de manifiesto de suma de comprobación | Menú Herramientas | Menú Herramientas | `cm_CheckSumVerify` / `cm_VerifyChecksum` | 
| **Utilidades de archivos**| Limpieza segura de varias pasadas (triturar)| `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | 
| **Utilidades de archivos**| Abrir terminal nativa de macOS | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` |

--- 

<div align="center"> 
<p>¿Listo para conectarse a servidores remotos y explorar archivos virtuales?</p> 
<p><strong><a href="network_and_vfs.md">Continúe con el Capítulo 6: Red y sistemas de archivos virtuales →ATB_HTML_00006__</strong></p> 
</div>