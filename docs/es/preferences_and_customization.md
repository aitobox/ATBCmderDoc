# Capítulo 7: Preferencias y personalización

Un administrador de archivos verdaderamente eficiente debe adaptarse a su flujo de trabajo, no obligarlo a adaptarse a sus valores predeterminados. Cada ingeniero, administrador de sistemas, archivero digital y profesional creativo aporta una memoria muscular, requisitos de visualización y hábitos operativos distintos: algunos dependen estrictamente de las teclas de función ortodoxas de Norton Commander/Total Commander (`F1`–`F10`), mientras que otros esperan atajos nativos de macOS (`Cmd+C`, `Cmd+V`, `Cmd+O`); algunos exigen un ajuste automático de columnas dinámico con métricas tipográficas de subpíxeles, mientras que otros necesitan límites de columna rígidos y fijos; algunos requieren un monitoreo agresivo de eventos del sistema de archivos en tiempo real, mientras que otros se ejecutan en recursos compartidos de red de alta latencia donde el sondeo pasivo es obligatorio. 

ATBCmder está diseñado desde cero para una configuración total. A través de su **Diálogo de preferencias** modular (`Cmd+,` / `⌘,` / `cm_Options`), **Editor de teclas de acceso rápido** intuitivo con detección de conflictos en tiempo real, **Motor de ajuste automático de columnas** inteligente, **Asociaciones de archivos** personalizables con macros de tokens externos y **Paquetes de configuración ZIP** portátiles. (`cm_ExportConfiguration`), ATBCmder le permite ajustar cada dimensión de su entorno de panel dual y llevar su configuración personalizada sin problemas a todos sus sistemas Mac. 

---

## 1. Inicio rápido visual: el centro de preferencias y la matriz de comandos

ATBCmder centraliza todas las configuraciones del usuario en una arquitectura de preferencias unificada compuesta por 16 páginas de configuración especializadas, un motor de mapeo de teclas de acceso rápido aislado y una capa de almacenamiento XML atómico. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          ATBCMDER PREFERENCES CENTER (Cmd+,)                           │
├──────────────────────┬─────────────────────────────────────────────────────────────────┤
│  CATEGORY NAVIGATION │  ACTIVE CONFIGURATION PAGE                                      │
├──────────────────────┼─────────────────────────────────────────────────────────────────┤
│  • General           │  Column Auto-Fit Mode:                                          │
│  • Hotkeys           │  [ Average Mode (Smart Padding)                       ▼ ]       │
│  • Language          │                                                                 │
│  • File Views        │  Average Mode Padding Factor: [ 1.25x ]                         │
│  • Auto Refresh      │                                                                 │
│  • Operations        │  Sorting Behavior:                                              │
│  • Packer            │  [X] Natural (numeric) sorting: photo1.jpg < photo10.jpg        │
│  • Plugins           │  [X] Case-sensitive sorting                                     │
│  • Directory Hotlist │  Folder Position: [ Folders First                     ▼ ]       │
│  • Favorite Tabs     │                                                                 │
│  • Editor            │  Thumbnail Generation:                                          │
│  • Viewer            │  Default Size: [ 128 px ]   Cache: [~/.cache/atbcmder]          │
│  • Toolbar           │                                                                 │
│  • Middle Toolbar    │  Date/Time Format:                                              │
│  • Log               │  Long Format: [ %Y-%m-%d %H:%M:%S                             ] │
│  • Quick Search      │                                                                 │
│  • Semantic Filter   │  [ Revert Changes ]                   [ Apply ] [ OK ] [Cancel] │
├──────────────────────┴─────────────────────────────────────────────────────────────────┤
│  CONFIG BACKEND:  atbcmder.xml  |  atbcmder_hotkeys.xml  |  favtabs.xml  |  hotlist.xml│
│  PORTABILITY:     cm_ExportConfiguration (ZIP)  ➔  cm_ImportConfiguration (ZIP)        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Hoja de trucos de personalización y preferencias de matriz dual

| Acción | Atajo de teclado en macOS | Tecla Commander clásica | ID de comando | Descripción | 
| :--- | :--- | :--- | :--- | :--- | 
| **Abrir Preferencias** | `Cmd+,` / `⌘,` | `Alt+O` / `⌥O` | `cm_Options` | Abre el cuadro de diálogo principal de Preferencias de varias páginas. | 
| **Configurar teclas de acceso rápido** | `Cmd+,` ➔ Teclas de acceso rápido | — | `cm_Options` (teclas de acceso rápido) | Acceso directo a la tabla de vinculación de atajos de teclado. | 
| **Configurar asociaciones de archivos**| Menú: Configuración | — | `cm_FileAssoc` | Asigna extensiones de archivos a visores/editores internos o externos. | 
| **Configuración de la lista activa del directorio** | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | Edita los marcadores de carpetas guardadas y las teclas de acceso rápido activas (`Ctrl+D` para abrir la lista activa). | 
| **Configurar pestañas favoritas** | Menú: Configuración | — | `cm_ConfigFavoriteTabs`| Gestiona conjuntos de pestañas de carpetas de doble panel guardados. | 
| **Configurar archivadores** | Menú: Configuración | — | `cm_ConfigArchivers` | Configura ejecutables de archivador externo y reglas de compresión. | 
| **Configuración de exportación** | Menú: Configuración | — | `cm_ExportConfiguration`| Exporta todos los archivos XML de configuración a un paquete `.zip` portátil. | 
| **Importar configuración** | Menú: Configuración | — | `cm_ImportConfiguration`| Restaura archivos XML de configuración de un paquete `.zip`. | 
| **Abrir directorio de configuración** | Menú: Configuración | — | `cm_OpenConfigDirectory`| Navega por el panel activo directamente a la carpeta de configuración de ATBCmder. | 
| **Guardar configuración inmediatamente** | Menú: Configuración | — | `cm_ConfigSaveSettings`| Vuelca todos los cambios de configuración en memoria al disco inmediatamente. | 
| **Guardar posición de ventana** | Menú: Configuración | — | `cm_ConfigSavePos` | Conserva la geometría de la ventana actual y las proporciones del divisor. | 
| **Alternar información sobre herramientas de archivos** | Preferencias: Vistas de archivos | — | *(Preferencias)* | Habilita o deshabilita información sobre herramientas detallada de metadatos flotantes. | 
| **Otorgar permisos del sistema** | Menú: Configuración | — | `cm_GrantFilesystemAccess`| Inicia la guía de incorporación de acceso completo al disco de la aplicación macOS Sandbox. | 

---

## 2. El cuadro de diálogo Preferencias Anatomía y navegación (`Cmd+,` / `cm_Options`)

La sala de control central de ATBCmder es el **Diálogo de Preferencias**. Puede invocarlo en cualquier momento presionando **`Cmd+,`** (`⌘,`) en macOS, eligiendo **ATBCmder ➔ Preferencias...** en el menú de la aplicación o ejecutando `cm_Options` a través de la barra de comandos semántica (`/`).

### 2.1 Diseño de diálogo y modelo de interacción

El cuadro de diálogo Preferencias utiliza un diseño dividido maestro-detalle diseñado para brindar claridad y accesibilidad al teclado: 

1. **Lista de navegación por categorías (izquierda)**: un selector vertical que presenta una fuente de interfaz legible de 14 puntos y una barra lateral fija de 195 píxeles. Navegue entre categorías usando las teclas de flecha `Up` y `Down`, o haga clic con el mouse. 
2. **Área de desplazamiento de páginas apiladas (derecha)**: un panel de configuración expansivo encerrado en un `QScrollArea` sin marco. A medida que cambia de categoría, la página de configuración correspondiente aparece suavemente sin provocar cambios de tamaño del diálogo ni parpadeo de la ventana. 
3. **Matriz de botones de acción (abajo)**: 
- **OK**: valida todos los campos de entrada en todas las páginas, escribe la configuración modificada en el disco (`atbcmder.xml`), activa la retraducción y las actualizaciones del tema, y cierra el cuadro de diálogo. 
- **Aplicar**: confirma todos los parámetros modificados inmediatamente sin cerrar el cuadro de diálogo. Esto es ideal para probar fuentes de interfaz de usuario, variaciones de temas, relleno de columnas e intervalos de actualización automática en tiempo real. 
- **Cancelar**: descarta cualquier cambio no guardado realizado en la sesión actual. Si obtuvo una vista previa de un tema sin aplicarlo, ATBCmder revierte automáticamente la interfaz a su tema anterior. 

```
┌────────────────────────────────────────────────────────────────────────────┐
│ Preferences Dialog Sidebar Navigation                                      │
├────────────────────────────────────────────────────────────────────────────┤
│  [ General ]         Basic UI, file lists, confirmation prompts, theme     │
│  [ Hotkeys ]         Keyboard shortcuts, context scoping, conflict manager │
│  [ Language ]        30+ real-time GUI translations without restart        │
│  [ File Views ]      Sorting rules, column auto-fitting, datetime formats  │
│  [ Auto Refresh ]    File monitoring events, polling, background sleep     │
│  [ Operations ]      Collision defaults (overwrite/rename), permissions    │
│  [ Packer ]          Archive formats (ZIP, 7Z, TAR), external binaries     │
│  [ Directory Hotlist]Bookmarks management, target panels, drag-and-drop    │
│  [ Favorite Tabs ]   Dual-panel workspace sets, layout persistence         │
│  [ Editor ]          Internal code editor typography, external editor CLI  │
│  [ Viewer ]          Universal Lister fonts, image rendering, external CLI │
│  [ Toolbar ]         Main button bar layout, custom commands, icon picker  │
│  [ Middle Toolbar ]  Middle splitter button bar, quick actions             │
│  [ Log ]             Operation audit trails, file logging, rotation        │
│  [ Quick Search ]    In-panel letter search, matching algorithms           │
│  [ Semantic Filter ] Natural language command input, spotlight integration │
│  [ Tabs ]            Folder tab bar styling, close buttons, locking rules  │
└────────────────────────────────────────────────────────────────────────────┘
```
 

---

### 2.2 Directorio de páginas de configuración completa

Cada página del cuadro de diálogo Preferencias aborda un dominio funcional específico:

| Página | Módulo de Implementación | Controles de configuración primaria | 
| :--- | :--- | :--- | 
| **Generalidades** | `page_general.py` | Visibilidad de archivos ocultos, íconos de archivos, cuadros de diálogo de confirmación de eliminación/sobrescritura, integración de la Papelera del sistema, tamaño de búfer para copiar/mover (4 KB–10 MB), selección de tema, tamaño de fuente global, alternancia de minimizar a bandeja y tecla de acceso rápido global para mostrar/ocultar ventana (`Cmd+Opt+H`). | 
| **Teclas de acceso rápido** | `page_hotkeys.py` | Búsqueda de comandos multicontexto, vinculación de acordes de atajos primarios y secundarios, advertencias de colisión de atajos automatizadas y restablecimiento de valores predeterminados de fábrica. | 
| **Idioma** | `page_language.py` | Selector de localización dinámico que admite más de 30 idiomas (inglés, alemán, francés, chino simplificado, japonés, ruso, español, etc.) con traducción instantánea de la interfaz de usuario en vivo. | 
| **Vistas de archivos** | `page_fileview.py` | Clasificación numérica natural y que distingue entre mayúsculas y minúsculas, posicionamiento de clasificación de carpetas (carpetas primero, archivos primero, mixtos), ubicación de archivos nuevos/actualizados, modos de ajuste automático de columnas (fijo, promedio, máximo), control deslizante de factor de relleno y formatos de fecha y hora personalizados. | 
| **Actualización automática** | `page_auto_refresh.py` | Monitoreo de creación/eliminación/cambio de nombre del sistema de archivos, monitoreo de cambios de atributos de archivos, intervalo de respaldo de sondeo del temporizador, alternancia de deshabilitación cuando está en segundo plano y lista de filtros de exclusión de directorios. | 
| **Operaciones** | `page_operations.py` | Políticas de colisión de archivos predeterminadas (Preguntar, Sobrescribir, Omitir, Sobrescribir lo antiguo, Cambiar nombre automáticamente al destino), políticas de colisión de directorios (Preguntar, Fusionar, Sobrescribir, Omitir), preasignación de espacio libre, manejo de enlaces simbólicos, preservación de permisos/marcas de tiempo y verificación. | 
| **Empaquetador** | `page_packer.py` | Formato de archivo de compresión predeterminado (`zip`, `7z`, `tar.gz`, `tar.bz2`, `tar.xz`, `tar`), rutas ejecutables externas para 7-Zip, GNU Tar, Gzip, Utilidades Bzip2 y XZ. | 
| **Lista destacada del directorio**| `page_hotlist.py` | Administrador de marcadores interactivo: agregue, elimine y reordene (`Drag & Drop`) directorios favoritos, especifique rutas de destino de panel dual y asigne claves de acceso rápido. | 
| **Pestañas favoritas** | `page_favorite_tabs.py` | Administrador de instantáneas del espacio de trabajo: guarde, cambie el nombre, reordene y restaure diseños de directorios de panel dual con múltiples pestañas. | 
| **Editor** | `page_editor.py` | Familia de fuentes del editor de código interno, tamaño de fuente, ancho de tabulación, ajuste de palabras y alternancia de números de línea; Ruta ejecutable del editor externo y argumentos de la línea de comandos. | 
| **Visor** | `page_viewer.py` | Tipografía de texto de Universal Lister, tabulaciones, márgenes, ajuste de línea, visibilidad del cursor, opciones de representación de imágenes (rotación automática EXIF, modos de zoom, cuadrícula de transparencia) y herramienta CLI de visor externo. | 
| **Barra de herramientas** | `page_toolbar.py` | Personalización de la barra de botones superior: control deslizante del tamaño del icono (16–64 px), control deslizante del tamaño de la barra, estilo de botón plano, alternancia de subtítulos, árbol de jerarquía de comandos y cuadro de diálogo de selección de iconos personalizado. | 
| **Barra de herramientas central** | `page_toolbar.py` | Configuración de la barra de herramientas del divisor vertical central: tamaños de iconos, botones de acción y reordenamiento del diseño. | 
| **Registro** | `page_log.py` | Registro de auditoría operativa: destino del archivo de registro, sustitución de ruta de token, tamaño máximo del archivo de registro, comportamiento de rotación de registros y filtros de eventos de operación específicos (copiar, mover, eliminar, descomprimir). | 
| **Búsqueda rápida** | `page_quicksearch.py` | Modo de búsqueda rápida del teclado (coincidencia exacta, inicio, final, comodines), distinción entre mayúsculas y minúsculas y tiempo de espera de cierre automático. | 
| **Filtro semántico** | `page_semantic_filter.py` | Comportamiento integrado de la barra de comandos de lenguaje natural (`/`), backends del proveedor de búsqueda y eliminación de sugerencias. | 
| **Pestañas** | `page_tabs.py` | Apariencia de las pestañas de la carpeta: visibilidad del botón de cierre, diseño de pestañas de varias filas frente a pestañas que se desplazan, comportamiento de navegación de pestañas bloqueadas y confirmaciones de cierre de pestañas. |

---

### 2.3 Tema en tiempo real y cambio dinámico de idioma

A diferencia de las utilidades heredadas que requieren cerrar y reiniciar la aplicación después de alterar la configuración de apariencia, ATBCmder presenta **Temática y localización intercambiables en caliente**: 

1. **Vistas previas del tema**: abra **General**, elija entre `Classic`, `Light`, `Dark` o `macOS Native (Stylish)` y observe cómo el estilo de la ventana cambia instantáneamente mediante la inyección de hojas de estilo Qt. Si presiona **Cancelar**, el tema anterior se restaura sin problemas. 
2. **Traducción instantánea**: abra **Idioma**, seleccione su dialecto preferido de la lista de más de 30 idiomas traducidos y haga clic en **Aplicar**. El título de la ventana, la barra lateral de categorías, los menús, los botones, las barras de estado y los mensajes de diálogo se vuelven a representar inmediatamente en el idioma de destino a través del canal de traducción dinámico `tr()` de ATBCmder. 

![Language Settings](images/language_settings.png) 
*Figura 7.1: La página de Preferencias de idioma que permite la localización instantánea y sin reinicio en más de 30 idiomas admitidos.* 

---

## 3. Personalización de atajos de teclado y gestión de conflictos

La eficiencia del teclado es la filosofía central de la gestión de archivos de panel dual. El **Editor de teclas de acceso rápido** de ATBCmder (`page_hotkeys.py`) proporciona control total sobre los acordes de acceso directo al mismo tiempo que aplica un estricto aislamiento del contexto y prevención de colisiones. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              HOTKEY CONFIGURATION PAGE                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Hotkey Context: [ FilePanel                                                 ▼ ]       │
│  Filter Commands: [ copy                                                     ] ⌧       │
├──────────────────────┬────────────────────────┬───────────────────┬────────────────────┤
│ Command ID           │ Description            │ Primary Shortcut  │ Secondary Shortcut │
├──────────────────────┼────────────────────────┼───────────────────┼────────────────────┤
│ cm_Copy              │ Copy Files or Folders  │ F5                │ Cmd+C              │
│ cm_CopySamePanel     │ Duplicate File in Pane │ Shift+F5          │ Cmd+D              │
│ cm_CopyRightPanel     │ Copy to Right Panel    │ Alt+F5            │                   │
│ cm_CopyFullNamesToClip│ Copy Full Path Names   │ Ctrl+Shift+C      │ Cmd+Opt+C         │
├──────────────────────┴────────────────────────┴───────────────────┴────────────────────┤
│  [ Edit Shortcut... ]           [ Clear Shortcuts ]            [ Reset to Defaults ]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Aislamiento y alcance del contexto

Para evitar el agotamiento de los atajos, ATBCmder separa las combinaciones de teclas en **Ámbitos de contexto**. Un atajo definido en un contexto no interfiere con teclas idénticas en ventanas no relacionadas: 

- **Principal**: accesos directos a aplicaciones globales disponibles en todas las ventanas (por ejemplo, `Cmd+,` para Preferencias, `Cmd+Q` para Salir). 
- **FilePanel**: activo siempre que la lista de archivos izquierda o derecha tiene el foco del teclado (por ejemplo, `F5` copia, `Space` calcula el tamaño del directorio, `Backspace` navega al padre). 
- **Visor**: activo dentro de Universal Lister (`F3`): controla codificaciones de texto, alternancia de vista hexadecimal (`2`/modo hexadecimal), zoom de imagen y reproducción multimedia. 
- **Editor**: Activo dentro del editor de texto integrado (`F4`): controla el resaltado de sintaxis, sangría, buscar/reemplazar (`Cmd+F`) y guardar archivos (`Cmd+S`). 
- **Diferir**: activo dentro de la diferenciación de archivos en paralelo: navegación de fragmentos (`F7`/`F8`), sincronización de líneas y operaciones de fusión. 
- **FindFiles**: activo en el cuadro de diálogo Búsqueda multifiltro: activa nuevas búsquedas, navega por los resultados y alimenta el cuadro de lista. 
- **MultiRename**: Activo en la herramienta Batch Multi-Rename: manipulación de contadores, inserción de tokens y ejecución. 

---

### 3.2 Arquitectura de enlace dual (atajos primarios y secundarios)

ATBCmder le permite asignar **dos combinaciones de atajos distintas** a cada comando: 

- **Atajo principal**: su acorde de memoria muscular principal (por ejemplo, `F5` para usuarios de Commander clásico). 
- **Atajo secundario**: un acorde alternativo (por ejemplo, `Cmd+C` para la ergonomía nativa de macOS). 

Ambos atajos permanecen activos simultáneamente en el contexto especificado. Al navegar por los menús, ATBCmder muestra automáticamente el acceso directo principal junto al texto del elemento del menú para una referencia visual clara. 

---

### 3.3 Receta paso a paso: personalizar un método abreviado de teclado

Siga este tutorial práctico para volver a vincular un comando existente o asignar un acceso directo secundario: 

1. Presione **`Cmd+,`** (`⌘,`) para abrir Preferencias y seleccione **Teclas de acceso rápido** en la barra lateral izquierda. 
2. Seleccione el **Contexto de tecla de acceso rápido** apropiado en el menú desplegable (por ejemplo, `FilePanel`). 
3. Escriba el nombre del comando o una palabra clave en el cuadro **Filtrar comandos** (por ejemplo, `Wipe` o `Terminal`). La tabla filtra las entradas coincidentes en tiempo real. 
4. Haga doble clic en la fila de comando o seleccione la fila y haga clic en **Editar...**. 
5. En el cuadro de diálogo **Editar tecla de acceso rápido**: 
- Haga clic dentro del cuadro **Atajo principal** y presione la combinación de teclas que desee (por ejemplo, `Ctrl+Alt+T`). ATBCmder captura el acorde limpiamente, restringiendo las secuencias a un solo acorde simultáneo. 
- (Opcional) Haga clic dentro del cuadro **Atajo secundario** y presione una combinación alternativa (por ejemplo, `Cmd+Shift+T`). 
6. Haga clic en **Guardar**. 

```
┌────────────────────────────────────────────────────┐
│ Edit Hotkey Dialog                                 │
├────────────────────────────────────────────────────┤
│ Command:             cm_RunTerm - Run Terminal     │
│ Primary Shortcut:    [ Ctrl+J                    ] │
│ Secondary Shortcut:  [ Cmd+Opt+T                 ] │
│                                                    │
│                           [ Cancel ]    [ Save ]   │
└────────────────────────────────────────────────────┘
```
 

---

### 3.4 Detección automatizada de colisiones y advertencias de conflictos

Si intenta asignar un acorde clave que ya ha sido reclamado por otro comando dentro del mismo contexto, el motor de detección de colisiones de ATBCmder interviene inmediatamente. Un cuadro de diálogo de alerta muestra la asignación en conflicto: 

> [!WARNING] 
> **Conflicto de acceso directo detectado** 
> El acceso directo `Ctrl+M` ya está asignado a `cm_MultiRename` en el contexto `FilePanel`. 
> ¿Quieres sobrescribirlo y reasignar `Ctrl+M` a `cm_MarkCurrentExtension`? 

- Al hacer clic en **Sí**, se desvincula automáticamente `Ctrl+M` del comando anterior y se aplica al comando recién seleccionado. 
- Al hacer clic en **No**, se cancela la edición y se conservan los enlaces existentes sin modificaciones. 

---

### 3.5 Tecla de acceso rápido global para mostrar/ocultar ventana (`Cmd+Opt+H` / `Ctrl+Alt+H`)

Para usuarios avanzados que prefieren mantener ATBCmder ejecutándose discretamente en segundo plano: 

1. Abra **Preferencias ➔ General**. 
2. Marque **Minimizar en la bandeja del sistema**. 
3. Localice **Mostrar/Ocultar tecla de acceso rápido de ventana** (predeterminado: `Ctrl+Alt+H` / `⌘⌥H`). 
4. Haga clic en el cuadro de secuencia para registrar cualquier acorde de tecla de acceso rápido global personalizado. 
5. Haga clic en **Aplicar**. 

Ahora puede llamar instantáneamente a ATBCmder al frente o descartarlo en segundo plano desde cualquier lugar dentro de macOS, incluso cuando trabaja dentro de otras aplicaciones de pantalla completa. 

---

## 4. Vistas de archivos, modos de columnas y gestión de miniaturas

La página **Vistas de archivos** (`page_fileview.py`) rige cómo se representan, miden, clasifican y presentan los directorios en los paneles duales. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              FILE VIEWS CONFIGURATION                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Sorting Rules:                                                                        │
│  [X] Case-sensitive sorting             [X] Natural (numeric) sorting                  │
│  [ ] Special sorting rules                                                             │
│  Folder sort mode:        [ Folders first                                    ▼ ]       │
│  New files position:      [ Sorted                                           ▼ ]       │
│  Updated files position:  [ Top                                              ▼ ]       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Column Widths & Auto-Fit Engine:                                                      │
│  Column auto-fit mode:    [ Average mode                                     ▼ ]       │
│  Average mode padding:    [ 1.20x ]  (Range: 1.00x - 5.00x)                            │
│  Hint: In Fixed mode, drag column dividers to save exact pixel widths per side.        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Date/Time Formatting:                                                                 │
│  Long datetime format:    [ %Y-%m-%d %H:%M:%S                                ]         │
│  Sync dirs format:        [ %Y.%m.%d %H:%M:%S                                ]         │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Motor de ajuste automático de columnas: los tres modos

Los administradores de archivos de doble panel a menudo tienen problemas con las diferentes longitudes de los nombres de archivos: las columnas demasiado anchas provocan desplazamiento horizontal, mientras que las columnas demasiado estrechas truncan las extensiones de archivos críticas. ATBCmder resuelve esto con tres comportamientos distintos de ajuste automático: 

1. **Modo fijo (`fixed`)**: 
- Desactiva el recálculo automático. 
- Los anchos de las columnas permanecen exactamente donde los colocas. 
- **Arrastrar manualmente**: cuando arrastra el borde vertical entre los encabezados de las columnas (por ejemplo, entre `Name` y `Ext`), ATBCmder captura el ancho de píxel exacto y lo conserva por separado para cada lado del panel (`column_widths_left` y `column_widths_right` en `atbcmder.xml`). 
2. **Modo promedio (`average` — Valor predeterminado recomendado)**: 
- Evalúa el ancho tipográfico medio (`QFontMetrics`) de todos los nombres de archivos visibles en el directorio. 
- Multiplica el ancho promedio por el **Factor de relleno** configurado (control deslizante ajustable de `1.0x` a `5.0x`, predeterminado `1.0x`–`1.25x`), agregando 40 píxeles para íconos de tipo de archivo y espacio para respirar visual. 
- Evita que los nombres de archivos con valores atípicos extremos (como un único nombre de archivo de registro de 120 caracteres) empujen todas las demás columnas fuera de la pantalla. 
3. **Modo de ancho máximo (`max`)**: 
- Escanea las entradas del directorio y expande la columna para que coincida con el nombre de archivo más amplio más el relleno de seguridad (+50 px). 
- Garantiza que cero nombres de archivos se trunquen con puntos suspensivos (`...`), ideal para archivos multimedia y conjuntos de datos científicos. 

> [!TIP] 
> **Optimización de directorios grandes**: 
> En directorios que contienen decenas de miles de elementos, medir cada cadena individual congelaría la interfaz. ATBCmder aplica automáticamente el muestreo por pasos inteligente (`_MAX_SAMPLE = 200`), evaluando un subconjunto de filas distribuidas uniformemente para calcular métricas de tipografía en menos de 2 milisegundos mientras ignora los marcadores del directorio principal (`..`). 

---

### 4.2 Opciones de clasificación de archivos

Ajuste cómo se ordenan los elementos dentro de las vistas de tabla: 

- **Clasificación natural (numérica): cuando está habilitado, los números dentro de las cadenas se comparan matemáticamente: `file1.txt`, `file2.txt`, `file10.txt` (en lugar de alfabético `file1.txt`, `file10.txt`, `file2.txt`). 
- **Clasificación que distingue entre mayúsculas y minúsculas**: cuando está marcada, los caracteres en mayúscula preceden a los caracteres en minúscula según los valores ordinales ASCII/Unicode (`File.txt` ordena antes de `apple.txt`). Cuando no está marcada, la clasificación no distingue entre mayúsculas y minúsculas. 
- **Modo de clasificación de carpetas**: 
- `Folders first`: Los directorios se agrupan en la parte superior del panel, encima de todos los archivos. 
- `Files first`: los archivos se enumeran primero, con los directorios ubicados en la parte inferior. 
- `Mixed`: los archivos y carpetas se ordenan alfabéticamente en una secuencia unificada. 
- **Posición de archivos nuevos y actualizados**: controla dónde aparecen los archivos recién creados o modificados recientemente durante las actualizaciones del sistema de archivos en vivo (`Sorted`, `Top` o `Bottom`). 

---

### 4.3 Vista de cuadrícula en miniatura y mecánica de caché

Para fotógrafos, diseñadores y editores de vídeo, ATBCmder proporciona una **Vista de cuadrícula de miniaturas** integrada (`cm_ThumbnailsView`), que reemplaza las filas tabulares con vistas previas de imágenes visuales. 

![Thumbnail Grid View](images/thumbnails_grid_view.png) 
*Figura 7.2: Vista en miniatura de alto rendimiento que muestra vistas previas de imágenes con espaciado de cuadrícula personalizado.*

#### Tamaño y zoom dinámico

- **Tamaño de miniatura predeterminado**: Configurable desde 48 px hasta 512 px (predeterminado: 128 px). 
- **Pellizcar para hacer zoom interactivo**: en los trackpads de Apple, use gestos estándar de pellizcar con dos dedos o mantenga presionado **`Ctrl`** mientras desplaza la rueda del mouse para escalar las miniaturas dinámicamente en tiempo real.

#### Arquitectura de almacenamiento en caché de varios niveles

Generar miniaturas para fotografías RAW de 48 megapíxeles de alta resolución o SVG vectoriales complejos requiere un uso intensivo de la CPU. ATBCmder emplea una sólida arquitectura de almacenamiento en caché de dos niveles: 

1. **Caché LRU en memoria**: retiene 500 objetos `QPixmap` descomprimidos en la RAM para un desplazamiento instantáneo y suave a 60 fps. 
2. **Caché de disco persistente**: almacenado localmente en el directorio de caché de su usuario: 
- Ruta macOS/Linux: `~/.cache/atbcmder/thumbnails/` 
- Las claves de caché se generan mediante hashes criptográficos SHA-256 que combinan la ruta del archivo, la marca de tiempo de modificación del archivo (`mtime`), el tamaño de píxel solicitado y la versión del esquema de caché: 
$$\text{Clave de caché} = \text{SHA256}(\text{filepath} + \text{mtime} + \text{size} + \text{version})$$ 

- Si un archivo de imagen se edita o actualiza en el disco, su marca de tiempo cambia, lo que invalida inmediatamente las entradas de caché obsoletas y activa la reproducción automática en segundo plano. 
3. **Subprocesos de trabajo en segundo plano**: el procesamiento de imágenes se descarga a un grupo de trabajadores `QThread` dedicado que utiliza Pillow (PIL) o canalizaciones `QImage` aceleradas por hardware, lo que garantiza que la interfaz de panel dual nunca tartamudee durante las importaciones de lotes pesados. 

---

### 4.4 Formato personalizado de fecha y hora

ATBCmder le permite definir cadenas de formato de marca de tiempo personalizadas utilizando la sintaxis estándar de Python `strftime`: 

- **Formato de fecha y hora larga** (predeterminado: `%Y-%m-%d %H:%M:%S`): controla la visualización de la fecha en la vista de columna completa (`2026-09-06 14:30:00`). 
- **Formato de directorios de sincronización** (predeterminado: `%Y.%m.%d %H:%M:%S`): controla la presentación de la marca de tiempo en el cuadro de diálogo Sincronizador de directorios. 

| Ficha | Descripción | Salida de ejemplo | 
| :--- | :--- | :--- | 
| `%Y` | Año de 4 dígitos | `2026` | 
| `%m` | Mes de 2 dígitos (`01`–`12`) | `09` | 
| `%d` | Día del mes de 2 dígitos (`01`–`31`) | `06` | 
| `%H` | Hora de 2 dígitos en formato de 24 horas (`00`–`23`) | `14` | 
| `%I` | Hora de 2 dígitos en formato de 12 horas (`01`–`12`) | `02` | 
| `%p` | Designación AM / PM | `PM` | 
| `%M` | Minuto de 2 dígitos (`00`–`59`) | `30` | 
| `%S` | Segundo de 2 dígitos (`00`–`59`) | `15` | 

---

## 5. Sensibilidad de monitoreo y actualización automática del sistema de archivos

Al colaborar en bases de código compartidas, descargar recursos del navegador o ejecutar tareas de compilación en segundo plano, el contenido del directorio cambia constantemente. La página **Actualización automática** (`page_auto_refresh.py`) equilibra la precisión de la interfaz de usuario en tiempo real con el consumo de CPU y batería. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              AUTO-REFRESH CONFIGURATION                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [X] Refresh file list:                                                                │
│      [X] When files are created, deleted or renamed                                    │
│      [X] When size, date or attributes change                                          │
│      Polling interval (seconds): [ 5 ]                                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Disable auto-refresh:                                                                 │
│      [X] When application is in the background                                         │
│      [X] For the following paths and their subdirectories:                             │
│          ┌──────────────────────────────────────────────────────────────────────────┐  │
│          │ /Volumes/NetworkShare/LargeMediaArchive                                  │  │
│          │ /Users/username/Developer/linux-kernel/                                  │  │
│          │ /Users/username/work/heavy_project/node_modules/                         │  │
│          └──────────────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Activadores de eventos frente a respaldo de sondeo

ATBCmder combina el monitoreo de eventos del sistema operativo nativo con un respaldo de sondeo inteligente: 

- **Monitoreo de eventos (`watch_file_name_change`)**: aprovecha las notificaciones nativas del kernel del sistema operativo (macOS `FSEvents` / `kqueue`) para detectar creaciones, eliminaciones y cambios de nombre de archivos sin sobrecarga de CPU. 
- **Monitoreo de atributos (`watch_attributes_change`)**: realiza un seguimiento de las expansiones del tamaño de los archivos, las actualizaciones de las marcas de tiempo y los ajustes del modo de permisos. 
- **Intervalo de respaldo de sondeo (`attr_poll_interval`)**: Configurable de 1 a 60 segundos (predeterminado: 5 segundos). 
*¿Por qué es necesario el sondeo?* Los montajes de almacenamiento de red remoto (SMB, CIFS, NFS, SFTP VFS) con frecuencia no emiten eventos del sistema de archivos del sistema operativo nativo cuando los clientes remotos realizan cambios. El temporizador de sondeo en segundo plano garantiza que los listados de sus paneles remotos nunca queden desactualizados. 

---

### 5.2 Conservación de batería y CPU: deshabilitar cuando esté en segundo plano

En las computadoras portátiles macOS que funcionan con batería, los observadores activos del sistema de archivos pueden consumir energía innecesaria. 

- Al marcar **Cuando la aplicación está en segundo plano** (`watch_only_foreground`) se suspenden automáticamente todos los temporizadores de sondeo activos y observadores de eventos en el momento en que ATBCmder pierde el foco de la ventana. 
- Cuando regresa a ATBCmder, los paneles ejecutan inmediatamente una única actualización coordinada, actualizando todos los listados de directorios instantáneamente. 

---

### 5.3 Filtros de exclusión de rutas

Los directorios de alta rotación, como `node_modules`, repositorios de metadatos de Git (`.git`), cachés de artefactos de compilación (`target/`, `build/`) y archivos de bases de datos locales, generan miles de eventos de disco por minuto. 

1. Marque **Las siguientes rutas y sus subdirectorios** (`watch_exclude_dirs`). 
2. Ingrese una ruta de directorio absoluta por línea en el área de texto de exclusión: 
   ```text
   /Users/username/Developer/project/node_modules
   /Users/username/Developer/linux/.git
   /Volumes/ProductionNAS/RenderingQueue
   ```
 

3. Haga clic en **Aplicar**. ATBCmder ignora los eventos del sistema de archivos que ocurren dentro de estos árboles de rutas, eliminando actualizaciones no deseadas de la interfaz de usuario y picos de CPU. 

---

## 6. Asociaciones de archivos personalizados e integración de herramientas externas

Al hacer doble clic en un archivo o presionar **`Enter`** normalmente se abre usando la aplicación predeterminada del sistema. El **Sistema de asociaciones de archivos** de ATBCmder (`cm_FileAssoc` / `file_associations.py`) le permite definir acciones personalizadas para patrones de archivos específicos, asignándolos a comandos internos o aplicaciones de terminal/GUI externas.

### 6.1 Arquitectura y especificidad del patrón

Las asociaciones de archivos se evalúan en orden de especificidad del patrón: el patrón global más largo y específico coincide primero: 

$$\text{Orden de especificidad: } \texttt{*.min.js} \longrightarrow \texttt{*.js} \longrightarrow \texttt{text/*} \longrightarrow \texttt{*}$$ 

Cada asociación puede contener múltiples acciones (por ejemplo, "Abrir en código VS", "Ver hexadecimal", "Ejecutar en Python"), con una designada como la acción predeterminada principal activada en `Enter`. 

---

### 6.2 Sustituciones de macros de tokens para comandos externos

Al iniciar herramientas externas o scripts de línea de comandos, ATBCmder reemplaza automáticamente las macros de token con los metadatos del archivo activo: 

| Ficha macro | Significado | Valor de ejemplo | 
| :--- | :--- | :--- | 
| **`%f`** | Ruta absoluta completa del archivo seleccionado | `/Users/username/Documents/report.pdf` | 
| **`%d`** | Ruta del directorio que contiene el archivo | `/Users/username/Documents` | 
| **`%n`** | Nombre de archivo base sin extensión | `report` | 
| **`%e`** | Extensión de archivo sin punto inicial | `pdf` | 

---

### 6.3 Recetas prácticas de asociación

#### Receta 1: abrir scripts de Python en Visual Studio Code

- **Patrón**: `*.py` 
- **Etiqueta**: `Edit in VS Code` 
- **Comando**: `code %f` 
- **Tipo de acción**: Comando de Shell externo

#### Receta 2: ejecutar el script Python en la terminal

- **Patrón**: `*.py` 
- **Etiqueta**: `Execute Script` 
- **Comando**: `python3 %f` 
- **Tipo de acción**: Comando de Shell externo

#### Receta 3: ver Markdown en la vista previa dedicada

- **Patrón**: `*.md` 
- **Etiqueta**: `Preview in Typora` 
- **Comando**: `open -a Typora %f` 
- **Tipo de acción**: Comando de Shell externo

#### Receta 4: comparar archivos con el panel opuesto en Beyond Compare

- **Patrón**: `*` 
- **Etiqueta**: `Compare with Target` 
- **Comando**: `bcomp %f %d` 
- **Tipo de acción**: Comando de Shell externo 

---

## 7. Personalización de la barra de herramientas y de la barra de herramientas intermedia

ATBCmder proporciona dos barras de herramientas personalizables: la **Barra de herramientas principal** situada debajo de la barra de menú y la **Barra de herramientas intermedia** incrustada verticalmente dentro del divisor que separa los dos paneles de archivos. 

![Middle Toolbar](images/middle_toolbar.png) 
*Figura 7.3: La página de opciones de la barra de herramientas central configurando botones divisores y activadores de acciones rápidas.*

### 7.1 Personalización de la apariencia de la barra de herramientas

Abra **Preferencias ➔ Barra de herramientas** o **Preferencias ➔ Barra de herramientas central**: 

- **Control deslizante de tamaño de barra**: ajusta la altura/ancho de la barra de herramientas de 16 px a 64 px. 
- **Control deslizante de tamaño de icono**: escala los iconos de los botones de 16 px a 64 px (predeterminado: 24 px). 
- **Botones planos**: alterna los modernos botones planos sin bordes frente a los clásicos botones en relieve. 
- **Mostrar subtítulos**: muestra etiquetas de texto debajo o al lado de los iconos de la barra de herramientas. 

---

### 7.2 Agregar elementos y el selector de íconos incorporado

Los elementos de la barra de herramientas están organizados en un árbol jerárquico que admite tres tipos de elementos: 

1. **Separador**: Inserta una línea divisoria visual o un espaciador entre grupos de botones. 
2. **Comando interno**: seleccione cualquiera de los más de 230 comandos `cm_*` de ATBCmder utilizando el campo de comando de autocompletar. 
3. **Comando externo**: especifique un comando de shell externo, un directorio de trabajo y tokens de parámetros (`%f`, `%d`).

#### El selector de iconos incorporado (`IconPickerDialog`)

Al configurar botones personalizados, haga clic en el botón de vista previa del ícono para abrir el **Selector de íconos** integrado: 

- Cuenta con un filtro de búsqueda instantánea en cientos de íconos SVG y PNG incluidos. 
- Muestra íconos en una cuadrícula uniforme con vista previa de alta resolución y nombres de raíces de activos. 

```
┌────────────────────────────────────────────────────────────────────────┐
│ Icon Picker Dialog                                                     │
├────────────────────────────────────────────────────────────────────────┤
│ Search: [ terminal                                                   ] │
├──────────────────────────────────────────────────────┬─────────────────┤
│  ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐ │ PREVIEW:        │
│  │ 💻 │   │ 🖥️ │   │ ⌨️ │   │ ⚙️ │   │ 📁 │   │ 🔍 │ │                  │
│  └────┘   └────┘   └────┘   └────┘   └────┘   └────┘ │      💻         │
│  cm_RunTerm  console  terminal  bash   sh      zsh   │                 │
│  ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐ │ Name: cm_RunTerm│
│  │ 📄 │   │ ✏️ │   │ ✂️ │   │ 📋 │   │ 🗑️ │   │ 🔒 │ │ Size: 48x48     │
│  └────┘   └────┘   └────┘   └────┘   └────┘   └────┘ │ Format: SVG/PNG │
├──────────────────────────────────────────────────────┴─────────────────┤
│                                                [ Cancel ]  [ Select ]  │
└────────────────────────────────────────────────────────────────────────┘
```
 

---

### 7.3 Personalización de la lista activa del directorio y de las pestañas favoritas

- **Lista activa del directorio (`page_hotlist.py`)**: administre sus `Ctrl+D` favoritos. Agregue rutas actuales, reordene los marcadores usando arrastrar y soltar, configure la sincronización del panel de destino y asigne claves de acceso. 
- **Pestañas favoritas (`page_favorite_tabs.py`)**: guarde diseños completos de espacio de trabajo de múltiples pestañas de panel dual. Restaure sus conjuntos exactos de directorios de revelado o edición de fotografías con un solo clic. 

![Directory Hotlist](images/quick_access_paths.png) 
*Figura 7.4: Gestión de rutas y marcadores de la lista activa de directorios.* 

---

## 8. Portabilidad de configuración y modo de prueba aislado

Ya sea migrando a una nueva Mac, aprovisionando una flota de máquinas de desarrollo o compartiendo combinaciones de teclas personalizadas con colegas, ATBCmder hace que la implementación y el respaldo de la configuración sean triviales.

### 8.1 Arquitectura de almacenamiento de configuración

ATBCmder almacena todas las configuraciones del usuario en archivos XML claramente estructurados y legibles por humanos ubicados en el directorio de configuración estándar de su sistema operativo: 

- **Ruta estándar de macOS**: 
`~/Library/Preferencias/atbcmder/` 

- **Ruta de la zona de pruebas de la aplicación macOS**: 
`~/Library/Containers/com.aitobox.atbcmder/Data/Library/Preferencias/atbcmder/` 

- **Ruta Linux/UNIX**: 
`~/.config/atbcmder/` 

- **Comando de acceso directo**: 
Ejecute **`cm_OpenConfigDirectory`** (o elija **Configuración ➔ Abrir directorio de configuración** en el menú) para navegar instantáneamente por el panel activo directamente a esta carpeta. 

```
~/Library/Preferences/atbcmder/
├── atbcmder.xml          # Core application configuration, geometry, themes, view rules
├── atbcmder_hotkeys.xml  # User keyboard shortcut overrides and custom bindings
├── favtabs.xml           # Saved favorite folder tab layouts and paths
├── hotlist.xml           # Directory Hotlist (Ctrl+D) bookmarks hierarchy
└── history.xml           # Recent directory jumps, command line history, search history
```
 

---

### 8.2 Exportación de paquetes de configuración (`cm_ExportConfiguration`)

Para crear una copia de seguridad portátil todo en uno de su entorno ATBCmder: 

1. Elija **Configuración ➔ Exportar configuración...** en la barra de menú (o ejecute `cm_ExportConfiguration`). 
2. Seleccione su directorio de destino y elija un nombre de archivo (predeterminado: `atbcmder-config.zip`). 
3. Haga clic en **Guardar**. 

ATBCmder vacía todos los cambios de memoria pendientes en el disco, reúne todos los archivos XML de configuración (`atbcmder.xml`, `atbcmder_hotkeys.xml`, `favtabs.xml`, `hotlist.xml`) y los empaqueta en un archivo ZIP comprimido y atómico. 

---

### 8.3 Importación de paquetes de configuración (`cm_ImportConfiguration`)

Para restaurar una copia de seguridad de la configuración en una nueva máquina o revertirla a un buen estado conocido: 

1. Elija **Configuración ➔ Importar configuración...** en la barra de menú (o ejecute `cm_ImportConfiguration`). 
2. Seleccione su archivo `atbcmder-config.zip` exportado previamente. 
3. Confirme el mensaje de advertencia: 
> La importación reemplazará todas las configuraciones actuales con el contenido del archivo seleccionado. ¿Continuar? 
4. Haga clic en **Sí**. 

ATBCmder descomprime de forma segura el archivo, verifica que todos los archivos extraídos sean configuraciones XML válidas, reemplaza los archivos de disco activos, recarga el singleton interno `Config()` y actualiza inmediatamente los paneles de archivos y los diseños de columnas, todo sin necesidad de reiniciar la aplicación. 

> [!IMPORTANT] 
> **Seguridad empresarial: protección anti-traversal** 
> ATBCmder aplica una estricta validación transversal de ruta durante la importación de configuración (`zipfile` desinfección). Cualquier elemento del archivo que contenga separadores de ruta (`/`, `\`), recorridos de directorio (`..`) o extensiones de archivo que no sean XML se rechaza inmediatamente, protegiendo su sistema operativo contra manipulaciones maliciosas de archivos. 

---

### 8.4 Modo de prueba aislado (`ATBCmder_test.sh`)

Al desarrollar complementos personalizados, experimentar con vinculaciones agresivas de teclas de acceso rápido o probar configuraciones beta, debe evitar modificar la configuración diaria de su controlador. 

ATBCmder admite la redirección de configuración completa a través de la variable de entorno `ATBCMDER_CONFIG_PATH`. Se incluye un script de prueba dedicado en el repositorio del proyecto: 

```bash
# Launch ATBCmder in completely isolated test mode:
./scripts/ATBCmder_test.sh
```

#### Cómo funciona el modo de prueba aislado:

1. Proporciona un directorio de prueba temporal limpio en `tests/.test_config/`. 
2. Copia la configuración inicial de fábrica de `src/atbcmder/resources/test_config.xml` a `tests/.test_config/atbcmder.xml`. 
3. Establece `export ATBCMDER_CONFIG_PATH="$(pwd)/tests/.test_config"`. 
4. Genera ATBCmder en Python. Cualquier configuración modificada o eliminada durante la sesión afecta solo al directorio de prueba temporal, dejando sus archivos personales `~/Library/Preferencias/atbcmder/` 100% intactos. 

---

## 9. ⚡ Consejos profesionales y análisis profundo: personalización avanzada

### Consejo profesional 1: aprovisionamiento automatizado de archivos Dot a través de Chezmoi/Ansible

Debido a que ATBCmder serializa todo el estado en archivos XML UTF-8 estándar, puede verificar su configuración en un repositorio de Git dotfiles y administrarla mediante herramientas como Chezmoi, GNU Stow o Ansible: 

```bash
# Example: Adding ATBCmder configuration to Chezmoi dotfiles manager
chezmoi add ~/Library/Preferences/atbcmder/atbcmder.xml
chezmoi add ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml
```

### Consejo profesional 2: Ajuste de Network Watcher de alto rendimiento

Cuando se trabaja en servidores de archivos SMB/NFS empresariales que contienen millones de archivos, la supervisión activa de eventos recursivos puede causar congestión en la red. 

1. Abra **Preferencias ➔ Actualización automática**. 
2. Desmarque **Cuando el tamaño, la fecha o los atributos cambian**. 
3. Establezca **Intervalo de sondeo** en `15` o `30` segundos. 
4. Agregue la raíz de montaje de red (`/Volumes/EnterpriseShare`) a la **Lista de exclusión de rutas**. 
5. Utilice la actualización manual del panel (**`Ctrl+R`** / `⌘R`) cuando se requiera sincronización inmediata.

### Consejo profesional 3: variables de entorno de comandos externos

Al configurar botones personalizados de la barra de herramientas externa o asociaciones de archivos, ATBCmder hereda automáticamente su entorno de shell de usuario (`PATH`, `HOME`, `USER`). Puede invocar utilidades de línea de comandos instaladas a través de Homebrew (`/opt/homebrew/bin/`) directamente sin proporcionar rutas ejecutables absolutas completas.

### Consejo profesional 4: configuración de información sobre herramientas de archivos flotantes

ATBCmder incluye información sobre herramientas de metadatos flotantes enriquecidas que muestran las dimensiones del archivo, los datos EXIF, la tasa de bits de audio y el recuento de miembros del archivo al pasar el cursor sobre los elementos. Puede activar o desactivar la información sobre herramientas en **Preferencias ➔ Vistas de archivos**. 

![Helpful Tooltips](images/helpful_tooltips.png) 
*Figura 7.5: Información sobre herramientas de metadatos enriquecidos que muestran propiedades detalladas del archivo al pasar el mouse.* 

---

## 10. Alertas de seguridad y sistema

> [!CAUTION] 
> **Verificación de sobrescritura de acceso directo** 
> Sobrescribir un acceso directo principal en el contexto `Main` o `FilePanel` lo desvincula del comando original inmediatamente. Si accidentalmente desvincula comandos esenciales como `F5` (Copiar) o `Enter` (Abrir), use el botón **Restablecer valores predeterminados** en el Editor de teclas de acceso rápido para restaurar las combinaciones de teclas de fábrica. 

> [!WARNING] 
> **La importación de configuración reemplaza todas las configuraciones** 
> Restaurar un paquete de configuración a través de `cm_ImportConfiguration` sobrescribe completamente sus archivos actuales `atbcmder.xml`, `favtabs.xml` y `hotlist.xml`. Exporte siempre una copia de seguridad de su configuración existente antes de importar un archivo externo. 

> [!IMPORTANT] 
> **Sandbox de aplicaciones macOS y acceso total al disco** 
> Si ATBCmder se ejecuta en macOS App Sandbox, no puede leer archivos o directorios de configuración fuera de su contenedor sin el permiso explícito del usuario. Si encuentra errores de permiso al acceder a unidades externas, ejecute **`cm_GrantFilesystemAccess`** para completar el flujo de incorporación de Acceso total al disco de macOS. 

---

## 11. Referencia de comandos de preferencias y personalización de matriz dual maestra

| Categoría | Descripción de la acción | Atajo de teclado en macOS | Tecla Commander clásica | ID de comando | 
| :--- | :--- | :--- | :--- | :--- | 
| **Preferencias** | Abrir el cuadro de diálogo de Preferencias principales | `Cmd+,` / `⌘,` | `Alt+O` / `⌥O` | `cm_Options` | 
| **Preferencias** | Guarde la configuración en XML ahora | Menú: Configuración | — | `cm_ConfigSaveSettings` | 
| **Preferencias** | Guardar posición y tamaño de ventana | Menú: Configuración | — | `cm_ConfigSavePos` | 
| **Preferencias** | Alternar información sobre herramientas de archivos | Preferencias ➔ Vistas de archivos | — | *(Preferencias)* | 
| **Preferencias** | Conceder permisos completos de disco | Menú: Configuración | — | `cm_GrantFilesystemAccess` | 
| **Teclas de acceso rápido** | Abrir la página del editor de teclas de acceso rápido | `Cmd+,` ➔ Teclas de acceso rápido | — | `cm_Options` | 
| **Teclas de acceso rápido** | Tecla de acceso rápido global para mostrar/ocultar ventana | `Ctrl+Alt+H` / `⌘⌥H` | `Ctrl+Alt+H` | *(Tecla de acceso rápido del sistema global)* | 
| **Asociaciones** | Abrir Administrador de asociaciones de archivos | Menú: Configuración | — | `cm_FileAssoc` | 
| **Marcadores** | Administrador de lista activa de directorio | `Ctrl+Shift+D` / `⌃⇧D` | `Ctrl+Shift+D` | `cm_ConfigDirHotList` | 
| **Marcadores** | Agregar directorio actual a la lista activa | Menú: Marcadores | — | `cm_AddDirToHotlist` | 
| **Pestañas de carpeta** | Administrador de pestañas de carpetas favoritas | Menú: Configuración | — | `cm_ConfigFavoriteTabs` | 
| **Pestañas de carpeta** | Guardar pestañas actuales como conjunto favorito| Menú: Pestañas | — | `cm_SaveFavoriteTabs` | 
| **Archivadores** | Configurar archivos binarios de Archiver | Menú: Configuración | — | `cm_ConfigArchivers` | 
| **Portabilidad** | Exportar configuración a ZIP | Menú: Configuración | — | `cm_ExportConfiguration` | 
| **Portabilidad** | Importar configuración desde ZIP | Menú: Configuración | — | `cm_ImportConfiguration` | 
| **Portabilidad** | Abrir carpeta de configuración | Menú: Configuración | — | `cm_OpenConfigDirectory` | 
| **Modos de visualización** | Alternar vista de cuadrícula de miniaturas | `Ctrl+Shift+F1` / `⌃⇧F1` | `Ctrl+Shift+F1` | `cm_ThumbnailsView` | 
| **Modos de visualización** | Actualizar listado de paneles activos | `Ctrl+R` / `⌃R` | `Ctrl+R` | `cm_Refresh` |

--- 

<div align="center"> 
<p>¿Listo para dominar todos los atajos de teclado y matrices de comandos en toda la aplicación?</p> 
<p><strong><a href="keyboard_shortcuts.md">Continúe con el Capítulo 8: Atajos de teclado maestros →ATB_HTML_00006__</strong></p> 
</div>