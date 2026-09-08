# Capítulo 8: Referencia maestra de atajos de teclado

ATBCmder está diseñado desde cero como un administrador de archivos basado en el teclado. Cada operación de archivo, salto de directorio, transformación de vista y utilidad por lotes se puede ejecutar sin interacción con el mouse. 

Para unir las tradiciones ortodoxas de Commander con la ergonomía nativa de Apple, ATBCmder emplea una **Arquitectura de teclado de matriz dual**: cada comando se puede invocar utilizando las teclas de función clásicas de Commander (`F1`–`F12`, `Insert`, teclado numérico) o acordes modificadores nativos de macOS (`⌘` Comando, `⌥` Opción, `⇧` Turno, `⌃` Control). 

---

## 1. La filosofía de la matriz dual y la notación clave

Ya sea que tenga veinte años de memoria muscular de Total Commander y Norton Commander o que viva completamente dentro de los accesos directos nativos de macOS Finder, ATBCmder se adapta a sus reflejos desde el primer momento sin necesidad de reasignación manual. 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      DUAL-MATRIX KEYBOARD ENGINE                            │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  CLASSIC COMMANDER PARADIGM          │  NATIVE macOS PARADIGM               │
│  • Function Key Centric (F1–F12)     │  • Modifier Chords (⌘, ⌥, ⇧, ⌃)      │
│  • Dedicated Keypad Marking (+, -, *)│  • Finder Parity (⌘C, ⌘V, ⌘⌫, ⏎)     │
│  • Zero-Modal Terminal Velocity      │  • Native Menu Bar Integration       │
│  Examples:                           │  Examples:                           │
│    F5        ➔ Copy Files            │    ⌘C ➔ ⌘V   ➔ Copy Files            │
│    F6        ➔ Move Files            │    ⌘C ➔ ⌥⌘V  ➔ Move Files            │
│    Shift+F4  ➔ Create Text File      │    ⇧⌘4       ➔ Create Text File      │
│    Alt+F7    ➔ Find Files            │    ⌥⌘F       ➔ Find Files            │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Símbolos modificadores del teclado de Apple

A lo largo de esta guía y dentro de los cuadros de diálogo de preferencias de ATBCmder, las combinaciones de teclas se representan mediante glifos tipográficos estándar de macOS: 

| Glifo | Nombre del modificador | Equivalente a Windows/PC | Descripción | 
| :---: | :--- | :--- | :--- | 
| **`⌘`** | **Comando** (`Cmd`) | `Win` / `Ctrl` | Tecla modificadora de acción principal de macOS. | 
| **`⌥`** | **Opción** (`Alt`) | `Alt` | Modificador secundario para acciones alternativas y personajes especiales. | 
| **`⇧`** | **Cambio** | `Shift` | Amplía selecciones, invierte acciones o activa modos de capital. | 
| **`⌃`** | **Control** (`Ctrl`) | `Ctrl` | Control de terminal y modificador de acordes de comandante clásico. | 
| **`⎋`** | **Escapar** (`Esc`) | `Esc` | Cancela operaciones, borra filtros o cierra cuadros de diálogo. | 
| **`⏎`** | **Devolución** (`Enter`) | `Enter` | Ejecuta acciones, abre elementos o confirma mensajes de diálogo. | 
| **`⌫`** | **Eliminar/Retroceder** | `Backspace` | Eliminación de caracteres hacia atrás o navegación por el directorio principal. | 
| **`⌦`** | **Reenviar eliminar** | `Del` | Reenviar eliminar carácter o eliminar archivo seleccionado. | 
| **`⇥`** | **Pestaña** | `Tab` | Alterna el enfoque entre los paneles de origen y de destino. | 
| **`⇞`** | **Arriba página** | `PgUp` | Desplaza el panel listado hacia arriba por una ventana gráfica. | 
| **`⇟`** | **Abajo de página** | `PgDn` | Desplaza la lista del panel hacia abajo en una ventana gráfica. | 

---

## 2. Guía clave de función macOS (`Fn`)

> [!IMPORTANT] 
> ### Cómo utilizar las teclas de función en teclados Mac 
> 
> De forma predeterminada, los teclados Apple (incluidos los teclados MacBook integrados, los Magic Keyboard y los Touch Bar Mac) asignan la fila física superior (`F1` a `F12`) a controles de hardware como el brillo de la pantalla, Mission Control, Spotlight, Dictado, reproducción multimedia y volumen del altavoz. 
> 
> Debido a que los flujos de trabajo clásicos de Commander dependen en gran medida de `F1`–`F12`, tienes dos opciones: 
> 
> #### Método A: Mantenga presionado el acorde de clave `Fn` (predeterminado listo para usar) 
> Mantenga presionada la tecla física **`Fn`** (o la tecla Globo 🌐) ubicada en la esquina inferior izquierda del teclado de su Mac mientras presiona cualquier tecla de función: 
> 
> * **`Fn + F3`**: Ver archivo en Lister 
> * **`Fn + F4`**: Editar archivo 
> * **`Fn + F5`**: Copiar archivos al panel de destino 
> * **`Fn + F6`**: Mover archivos al panel de destino 
> * **`Fn + F7`**: Crear nuevo directorio 
> * **`Fn + F8`**: Eliminar archivos 
> * **`Fn + Shift + F4`**: Crear y editar un nuevo archivo de texto 
> * **`Fn + Alt + F7`**: Abrir búsqueda de archivos 
> 
> #### Método B: Habilite las "Teclas de función estándar" en la configuración de macOS (recomendado) 
> Si usa ATBCmder regularmente, cambie su fila de funciones para que presionar `F1`–`F12` active los comandos de función directamente, mientras mantiene presionado `Fn` active los ajustes de brillo y volumen: 
> 
> 1. **macOS 13 Ventura, macOS 14 Sonoma, macOS 15 Sequoia**: 
> - Abrir ** Menú Apple ➔ Configuración del sistema...** 
> - En la barra lateral izquierda, seleccione **Teclado**. 
> - Haga clic en el botón **Atajos de teclado...**. 
> - En la barra lateral del cuadro de diálogo, seleccione **Teclas de función**. 
> - Alternar **"Usar teclas F1, F2, etc. como teclas de función estándar"** a **ON**. 
> - Haga clic en **Listo**. 
> 
> 2. **macOS 12 Monterey y macOS 11 Big Sur**: 
> - Abra ** Menú Apple ➔ Preferencias del Sistema... ➔ Teclado**. 
> - En la pestaña **Teclado**, marque la casilla denominada **"Usar teclas F1, F2, etc. como teclas de función estándar"**. 
> 
> #### Modelos de MacBook Pro con Touch Bar 
> 
> * Mantenga presionada la tecla física **`Fn`** en la parte inferior izquierda para mostrar instantáneamente la fila virtual `F1`–`F12` en la Touch Bar. 
> * Alternativamente, configure **Configuración del sistema ➔ Teclado ➔ Configuración de la barra táctil...** y establezca **"La barra táctil muestra"** en **"Teclas F1, F2, etc."** cuando ATBCmder sea la aplicación frontal activa. 
> 
> #### Teclados compactos sin una fila de funciones dedicada 
> 
> * Si está utilizando un teclado mecánico 60% o 65% sin teclas `F` dedicadas, no necesita contorsionar los dedos. Utilice los acordes modificadores nativos de macOS de ATBCmder (`⌘C`, `⌥⌘V`, `⇧⌘N`, `⌘⌫`, `⌥⏎`) que proporcionan una paridad operativa del 100 %.

---

## 3. Arquitectura de acceso directo contextualizada

Para evitar colisiones de teclas de acceso rápido entre diferentes áreas de aplicación (por ejemplo, buscar dentro de la lista de archivos principal versus buscar dentro de un visor de archivos de texto), ATBCmder segmenta todos los accesos directos en distintos contextos jerárquicos: 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          APPLICATION SCOPE: Main                            │
│  Global commands, panel navigation, window management, toolbar, power tools │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  PANEL SCOPE: FilePanel       │  MODAL TOOLS SCOPES                         │
│  Active during directory      │  • Viewer      (Lister preview window)      │
│  table and thumbnail browsing │  • Editor      (Built-in code editor)       │
│  (marking, range selection,   │  • Differ      (Side-by-side diff viewer)   │
│  inline editing, space count) │  • FindFiles   (Multi-threaded file search) │
│                               │  • MultiRename (Batch rename engine)        │
└───────────────────────────────┴─────────────────────────────────────────────┘
```
 

Cuando presionas un acorde clave, el motor **`HotkeyManager`**: 

1. Evalúa el contexto enfocado activo (por ejemplo, `Viewer` o `FilePanel`). 
2. Si un enlace exacto coincide, el comando `cm_*` asociado se ejecuta inmediatamente. 
3. Si no existe ningún enlace en el contexto local, la pulsación de tecla vuelve correctamente al contexto `Main`. 
4. Si aún no está vinculado, se hace cargo de la edición de texto estándar o del manejo de pulsaciones de teclas del sistema. 

---

## 4. Tablas maestras de matriz dual categorizadas

Las siguientes tablas de referencia documentan todos los comandos admitidos por ATBCmder, categorizados por flujo de trabajo funcional.

### 4.1 Operaciones de archivos

Las operaciones con archivos constituyen la columna vertebral del trabajo diario. Cada operación tiene como valor predeterminado el paradigma **Fuente ➔ Destino**: los elementos seleccionados en el panel activo se procesan en el directorio abierto en el panel opuesto inactivo.

| ID de comando | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_View` | Ver archivo usando Universal Lister (vista previa de solo lectura) | `⌘3` / `Space` *(Vista rápida)* | `F3` / `Shift+F3` | Principal | 
| `cm_Edit` | Abrir archivo en el editor de texto integrado | `⌘4` | `F4` | Principal | 
| `cm_EditNew` | Cree y edite inmediatamente un nuevo archivo de texto | `⇧⌘4` / `⇧F4` | `Shift+F4` | Principal | 
| `cm_Copy` | Copie los archivos seleccionados del panel activo al de destino | `⌘C` *(al portapapeles)* / `F5` | `F5` | Principal | 
| `cm_CopySamePanel` | Duplicar/clonar archivo seleccionado dentro del mismo directorio | `⇧F5` | `Shift+F5` | Principal | 
| `cm_Move` | Mover archivos seleccionados del panel activo al de destino | `⌥⌘V` *(pegar mover)* / `F6` | `F6` | Principal | 
| `cm_RenameOnly` | Cambio rápido de nombre en línea del archivo bajo el cursor | `⏎` *(Devolución)* / `F2` | `F2` / `Shift+F6` | Principal | 
| `cm_Rename` | Cambiar el nombre del archivo seleccionado mediante el cuadro de diálogo | `⇧F6` | `Shift+F6` | Principal | 
| `cm_MkDir` | Crear un nuevo directorio/carpeta | `⇧⌘N` / `F7` | `F7` | Principal | 
| `cm_Delete` | Eliminar elementos seleccionados a la Papelera de macOS | `⌘⌫` *(Cmd+Suprimir)* / `⌦` | `F8` / `Delete` | Principal | 
| `cm_Wipe` | Eliminar archivos de forma segura (evitar la Papelera de forma permanente) | `⌥⇧⌫` / `⌥⌦` | `Alt+Delete` / `Shift+Delete` | Panel de archivos | 
| `cm_Open` | Abra el archivo con la aplicación predeterminada o ingrese al directorio | `⌘↓` / `⏎` *(Devolución)* | `Enter` | Principal | 
| `cm_SetFileProperties` | Inspeccionar y editar metadatos de archivos, fechas y permisos UNIX | `⌥⏎` *(Opción+Retorno)* / `⌘I` | `Alt+Enter` | Principal | 
| `cm_CountDirContent` | Calcular el tamaño en bytes del directorio bajo el cursor | `⌥⇧⏎` *(Opción+Mayús+Retorno)* | `Alt+Shift+Enter` | Panel de archivos | 
| `cm_CalculateSpace` | Calcular el tamaño total de todos los directorios seleccionados | `⌃L` / `⌘L` | `Ctrl+L` | Principal | 
| `cm_SymLink` | Crear enlace simbólico en el panel de destino | `⌥⌘S` | *(Menú: Archivos ➔ Enlace simbólico)* | Principal | 
| `cm_HardLink` | Crear un enlace físico del sistema de archivos en el panel de destino | `⌥⌘H` | *(Menú: Archivos ➔ Enlace físico)* | Principal | 
| `cm_PackFiles` | Empaquetar/comprimir archivos seleccionados en un archivo (`.zip`, `.tar`, `.7z`) | `⌥F5` / `⌥⌘P` | `Alt+F5` | Principal | 
| `cm_ExtractFiles` | Extraiga el contenido del archivo directamente al panel de destino | `⌥F9` / `⌥⌘E` | `Alt+F9` | Principal | 
| `cm_ArchiveView` | Ingrese el archivo como directorio del sistema de archivos virtual (`vfs://`) | `⌃⇟` *(Ctrl+AvPág)* / `⌘↓` | `Ctrl+PgDn` | Principal | 
| `cm_CompareContents` | Comparar el contenido de dos archivos seleccionados | `⇧F3` | `Shift+F3` | Principal |

---

### 4.2 Selección y marcado

Los administradores de archivos ortodoxos destacan por la selección rápida de varios archivos. ATBCmder permite seleccionar elementos individuales, patrones comodín, grupos de extensiones o bloques continuos sin usar el mouse.

| ID de comando | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_MarkMarkAll` | Seleccionar todos los archivos y carpetas en el panel activo | `⌘A` | `Ctrl+A` / `Ctrl+Num+` | Principal | 
| `cm_MarkUnmarkAll` | Deseleccionar todos los archivos y carpetas en el panel activo | `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+Num-` | Principal | 
| `cm_MarkInvert` | Invertir el estado de selección actual en el panel activo | `⌘I` / `⌃I` | `Num*` *(Teclado `*`)* | Panel de archivos | 
| `cm_MarkPlus` | Seleccionar grupo comodín coincidente (por ejemplo, `*.ts`) | `⌘+` / `⌃+` | `Num+` *(Teclado `+`)* | Panel de archivos | 
| `cm_MarkMinus` | Anular la selección del grupo que coincida con el patrón comodín (por ejemplo, `*.log`) | `⌘-` / `⌃-` | `Num-` *(Teclado `-`)* | Panel de archivos | 
| `cm_MarkCurrentExtension` | Seleccionar todos los archivos que comparten la extensión del archivo del cursor | `⇧⌘E` / `⌥F8` | `Shift+Num+` / `Alt+Num+` | Principal | 
| `cm_UnmarkCurrentExt` | Deseleccionar todos los archivos que comparten la extensión del archivo del cursor | `⌥⇧Num-` | `Shift+Num-` / `Alt+Num-` | Principal | 
| `cm_MarkCurrentName` | Seleccionar todos los archivos que comparten el nombre de archivo base del cursor | `⌥⌘N` | *(Menú: Marcar ➔ Mismo nombre)* | Principal | 
| `cm_SelectOrDeselectFile` | Alternar selección de elementos y hacer avanzar el cursor hacia abajo | `Space` | `Insert` / `Space` | Panel de archivos | 
| `Shift+Up / Shift+Down` | Ampliar o contraer gama de selección continua | `⇧↑` / `⇧↓` | `Shift+↑` / `Shift+↓` | Panel de archivos | 
| `Shift+PageUp / Shift+PageDown` | Ampliar la selección continua mediante la página de vista completa | `⇧⇞` / `⇧⇟` | `Shift+PgUp` / `Shift+PgDn` | Panel de archivos | 
| `cm_ClearAll` | Borrar todas las marcas de selección y aspectos destacados de búsqueda | `⌃L` | `Ctrl+L` | Principal | 
| `cm_CopyToClipboard` | Copie los archivos seleccionados al portapapeles del sistema macOS | `⌘C` | `Ctrl+C` | Principal | 
| `cm_CutToClipboard` | Cortar archivos seleccionados al portapapeles del sistema macOS | `⌘X` | `Ctrl+X` | Principal | 
| `cm_PasteFromClipboard` | Pegue archivos del portapapeles al directorio activo | `⌘V` | `Ctrl+V` | Principal | 
| `cm_PasteAsMove` | Pegar archivos desde el portapapeles como una operación Mover | `⌥⌘V` | `Ctrl+Alt+V` | Principal | 
| `cm_CopyNamesToClip` | Copie los nombres de archivo solo al portapapeles | `⇧⌘X` | `Ctrl+Shift+X` | Principal | 
| `cm_CopyFullNamesToClip` | Copie las rutas absolutas completas al portapapeles | `⇧⌘C` | `Ctrl+Shift+C` | Principal | 
| `cm_CompareDirectories` | Marcar archivos que existen en un panel pero no en el otro | `⌥⇧C` | *(Menú: Marcar ➔ Comparar Directorios)* | Principal |

---

### 4.3 Navegación del panel y marcadores

Muévase sin esfuerzo entre carpetas, volúmenes locales, montajes de red e historial de navegación.

| ID de comando | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_FocusSwap` / `cm_SwitchPanel` | Enfoque alternativo del teclado entre los paneles izquierdo y derecho | `⇥` *(Tab)* | `Tab` | Principal | 
| `cm_Refresh` | Actualizar/volver a leer el contenido del directorio activo | `⌘R` / `⌃R` | `Ctrl+R` | Principal | 
| `cm_ChangeDirToParent` | Navegue hasta el directorio principal (`..`) | `⌘↑` / `⌫` *(Retroceso)* | `Backspace` / `Ctrl+PgUp` | Principal | 
| `cm_ChangeDirToRoot` | Saltar directamente a la raíz del sistema de archivos (`/`) | `⌘\` | `Ctrl+\` | Principal | 
| `cm_ChangeDirToHome` | Saltar directamente a la carpeta de inicio del usuario (`~`) | `⇧⌘H` | `Ctrl+Shift+Home` / `Alt+Home` | Panel de archivos | 
| `cm_ViewHistoryPrev` | Navegar hacia atrás en el historial de navegación del directorio | `⌘[` / `⌥←` | `Alt+Left` / `Ctrl+[` | Principal | 
| `cm_ViewHistoryNext` | Navegar hacia adelante en el historial de navegación del directorio | `⌘]` / `⌥→` | `Alt+Right` / `Ctrl+]` | Principal | 
| `cm_DirHistory` | Abrir el menú desplegable del historial del directorio interactivo | `⌥↓` / `⌃↓` | `Alt+Down` / `Alt+F8` | Principal | 
| `cm_Drives` | Ventana emergente de selección de volumen abierta y montada | `⌥D` | `Alt+D` | Principal | 
| `cm_LeftOpenDrives` | Abra el menú de selección de unidad para el panel izquierdo | `⌥F1` | `Alt+F1` | Principal | 
| `cm_RightOpenDrives` | Abra el menú de selección de unidad para el panel derecho | `⌥F2` | `Alt+F2` | Principal | 
| `cm_Exchange` | Intercambiar paneles izquierdo y derecho (directorios, pestañas, estados) | `⌘U` | `Ctrl+U` | Principal | 
| `cm_TargetEqualSource` | Establecer el directorio del panel inactivo para que coincida con el directorio activo | `⌥Z` / `⌃←` / `⌃→` | `Alt+Z` / `Ctrl+Left` / `Ctrl+Right` | Principal | 
| `cm_SyncSlaveDir` | Bloquear la navegación del panel de destino para reflejar el panel de origen | `⌥S` | *(Menú: Comandos ➔ Sincronizar navegación)* | Principal | 
| `cm_DirHotList` | Abrir lista activa del directorio/menú Marcadores | `⌘D` | `Ctrl+D` | Principal | 
| `cm_ConfigDirHotList` | Abrir el cuadro de diálogo de configuración de la lista activa del directorio | `⇧⌘D` | `Ctrl+Shift+D` | Principal | 
| `cm_GoToFirst` | Saltar el cursor al primer elemento del panel activo | `⌘↑` / `Fn+←` *(Casa)* | `Home` | Principal | 
| `cm_GoToLast` | Saltar el cursor al último elemento del panel activo | `⌘↓` / `Fn+→` *(Fin)* | `End` | Principal | 
| `PageUp / PageDown` | Desplazar el panel activo hacia arriba o hacia abajo una ventana gráfica completa | `⇞` *(Fn+ ↑)* / `⇟` *(Fn+↓)* | `PageUp` / `PageDown` | Panel de archivos |

---

### 4.4 Modos de visualización y clasificación

Cambie sin problemas entre listas compactas, columnas de metadatos detalladas, cuadrículas de miniaturas visuales, aplanamiento recursivo de directorios y vistas de árbol sincronizadas.

| ID de comando | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_BriefView` | Cambiar a vista breve (nombres compactos de varias columnas) | `⌃F1` | `Ctrl+F1` | Principal | 
| `cm_ColumnsView` | Cambiar a Vista de columnas/detalles (nombre, tamaño, fecha, permisos) | `⌃F2` | `Ctrl+F2` | Principal | 
| `cm_ThumbnailsView` | Cambiar a vista de cuadrícula de miniaturas (imágenes, medios, archivos PDF) | `⌃⇧F1` | `Ctrl+Shift+F1` | Principal | 
| `cm_FlatView` | Alternar vista plana/sucursal (listado de directorio recursivo) | `⌘B` | `Ctrl+B` | Principal | 
| `cm_FlatViewSel` | Vista plana/sucursal solo de directorios seleccionados | `⇧⌘B` | `Ctrl+Shift+B` | Principal | 
| `cm_TreeView` | Vista de árbol (Reemplace el panel activo con un árbol de directorios) | `⌃⇧F8` | `Ctrl+Shift+F8` | Principal | 
| `cm_TreeViewSplit` | Vista de árbol (panel dividido: árbol arriba/izquierda, archivos abajo/derecha) | `cm_TreeViewSplit` | *(Menú: Mostrar ➔ Vista de árbol dividida)* | Principal | 
| `cm_TreeViewBoth` | Vista de árbol (Ambos paneles muestran árboles de directorios) | `cm_TreeViewBoth` | *(Menú: Mostrar ➔ Vista de árbol ambos)* | Principal | 
| `cm_QuickView` | Alternar panel Vista rápida (vista previa en vivo en el panel opuesto) | `⌘Q` / `⌃Q` | `Ctrl+Q` | Principal | 
| `cm_SortByName` | Ordenar elementos por nombre (alternar ascendente/descendente) | `⌃F3` | `Ctrl+F3` | Principal | 
| `cm_SortByExt` | Ordenar elementos por extensión | `⌃F4` | `Ctrl+F4` | Principal | 
| `cm_SortByDate` | Ordenar elementos por fecha/hora de modificación | `⌃F5` | `Ctrl+F5` | Principal | 
| `cm_SortBySize` | Ordenar elementos por tamaño de archivo | `⌃F6` | `Ctrl+F6` | Principal | 
| `cm_SortByAttr` | Ordenar elementos por atributos/permisos UNIX | `cm_SortByAttr` | *(Menú: Ordenar ➔ Atributos)* | Principal | 
| `cm_ShowHiddenFiles` | Alternar visibilidad de archivos ocultos (`.` dotfiles) | `⌘H` / `⇧⌘.` | `Ctrl+H` | Principal | 
| `cm_ShowSysFiles` | Alternar visibilidad del sistema macOS y archivos protegidos | `⇧⌘.` | `Ctrl+.` | Principal | 
| `cm_QuickSearch` | Abrir la barra de búsqueda rápida en el panel (escriba letras para filtrar) | `⌥S` / `⌃S` *(o escribiendo)* | `Ctrl+S` / *(Mecanografía de letras)* | Principal | 
| `cm_SemanticFilter` | Abrir barra de filtro inteligente semántico de lenguaje natural | `⌘F` | `Ctrl+F` | Principal | 
| `cm_HorizontalFilePanels` | Alternar diseño de panel dual horizontal (apilado verticalmente) | `⇧⌘H` | `Ctrl+Shift+H` | Principal |

---

### 4.5 Pestañas y gestión de ventanas

ATBCmder permite abrir pestañas ilimitadas en cualquiera de los paneles, bloquear ubicaciones de trabajo favoritas y administrar sesiones de múltiples pestañas en paneles duales.

| ID de comando | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_NewTab` | Abrir nueva pestaña de carpeta en el panel activo | `⌘T` | `Ctrl+T` | Principal | 
| `cm_CloseTab` | Cerrar la pestaña de la carpeta actualmente activa | `⌘W` | `Ctrl+W` | Principal | 
| `cm_NextTab` / `cm_NextTabCtrl` | Cambiar a la siguiente pestaña a la derecha | `⌃⇥` *(Ctrl+Tab)* / `⌘⇧]` | `Ctrl+Tab` | Principal | 
| `cm_PrevTab` / `cm_PrevTabCtrl` | Cambiar a la pestaña anterior a la izquierda | `⌃⇧⇥` *(Ctrl+Mayús+Tab)* / `⌘⇧[` | `Ctrl+Shift+Tab` | Principal | 
| `cm_ShowTabsList` | Mostrar menú emergente de todas las pestañas abiertas en el panel activo | `⇧⌘L` | `Ctrl+Shift+L` | Principal | 
| `cm_CloseAllTabs` | Cerrar todas las pestañas del panel activo excepto la última | `⌥⌘W` | *(Menú contextual de la pestaña: Cerrar todo)* | Principal | 
| `cm_CloseOtherTabs` | Cerrar todas las pestañas excepto la pestaña actualmente activa | `⇧⌘W` | *(Menú contextual de la pestaña: Cerrar otros)* | Principal | 
| `cm_Duplicatetab` | Duplicar pestaña de carpeta activa | `⌘D` / `cm_Duplicatetab` | *(Menú contextual de la pestaña: Duplicar)* | Principal | 
| `cm_MoveTabLeft` | Mover la pestaña activa una posición hacia la izquierda | `⌃⇧←` | *(Menú contextual de la pestaña: Mover a la izquierda)* | Principal | 
| `cm_MoveTabRight` | Mover la pestaña activa una posición a la derecha | `⌃⇧→` | *(Menú contextual de la pestaña: Mover a la derecha)* | Principal | 
| `cm_CopyTabToOtherPanel` | Clonar pestaña activa directamente en el panel opuesto | `⌥⌘T` | *(Menú contextual de la pestaña: Copiar a otro)* | Principal | 
| `cm_SaveTab` / `cm_SaveTabs` | Guardar el diseño de la pestaña actual en la configuración | `cm_SaveTab` | *(Menú: Pestañas ➔ Guardar pestañas)* | Principal | 
| `cm_LoadTab` / `cm_LoadTabs` | Restaurar el diseño de pestañas guardado desde la configuración | `cm_LoadTab` | *(Menú: Pestañas ➔ Cargar pestañas)* | Principal | 
| `cm_OptionsFavorites` | Configurar conjuntos de pestañas favoritas y espacios de trabajo persistentes | `cm_OptionsFavorites` | *(Menú: Pestañas ➔ Pestañas favoritas)* | Principal | 
| `cm_FullScreen` | Alternar ventana de aplicación de pantalla completa | `⌃⌘F` / `F11` | `F11` | Principal |

---

### 4.6 Herramientas y servicios públicos

Inicie herramientas de automatización avanzadas, utilidades por lotes y herramientas de sistemas integrados directamente desde los acordes del teclado.

| ID de comando | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_FileSearch` / `cm_Search` | Abrir el cuadro de diálogo de búsqueda avanzada con múltiples filtros | `⌥F7` / `⌥⌘F` | `Alt+F7` | Principal | 
| `cm_FileDiff` / `cm_CompareFiles` | Abrir visor de diferencias de archivos visuales uno al lado del otro | `⌘⇧F12` | `Meta+Shift+F12` | Principal | 
| `cm_SyncDirs` | Abra la herramienta de sincronización de directorios bidireccional | `⇧F12` | `Shift+F12` | Principal | 
| `cm_MultiRename` | Abrir herramienta de cambio de nombre múltiple por lotes (RegEx y tokens) | `⌘M` | `Ctrl+M` | Principal | 
| `cm_Split` | Divida un archivo grande en segmentos uniformes | `⌥F6` | `Alt+F6` | Principal | 
| `cm_Combine` | Combine segmentos numerados divididos nuevamente en el archivo original | `⌥F7` | `Alt+F7` | Principal | 
| `cm_CalculateChecksum` | Calcular hash criptográfico (MD5, SHA-1, SHA-256) | `⌃X` / `⌘K` | `Ctrl+X` | Principal | 
| `cm_VerifyChecksum` | Verificar archivos con el archivo de suma de comprobación (`.md5`, `.sha256`) | `cm_VerifyChecksum` | *(Menú: Archivos ➔ Verificar suma de comprobación)* | Principal | 
| `cm_RunTerm` | Iniciar Terminal del sistema en el directorio del panel activo | `⌃J` / `F9` | `Ctrl+J` / `F9` | Principal | 
| `cm_FocusCmdLine` | Cambie el foco del teclado directamente a la línea de comando inferior | `⇧F2` | `Shift+F2` | Principal | 
| `cm_ShowCmdLineHistory` | Abrir menú desplegable del historial de comandos de shell anteriores | `⌥↓` / `⌃↓` | `Alt+F8` / `Ctrl+Down` | Principal | 
| `cm_AddPathToCmdLine` | Agregue la ruta del directorio activo a la línea de comando | `⌘P` | `Ctrl+P` | Principal | 
| `cm_ShowCommandLine` | Alternar línea de comando inferior/barra de entrada de consola | `⌘O` | `Ctrl+O` | Principal | 
| `cm_DiskBenchmark` | Ejecute una prueba comparativa de rendimiento de lectura/escritura de la unidad de almacenamiento | `cm_DiskBenchmark` | *(Menú: Comandos ➔ Punto de referencia)* | Principal | 
| `cm_VisSemanticCommand` | Abrir barra de comandos de lenguaje natural y búsqueda semántica | `/` / `⇧⌘P` | `/` | Principal |

---

### 4.7 Sistema, configuración y ayuda

Acceda a las preferencias de la aplicación, gestión de configuración, actualizaciones de software y documentación del usuario. 

| ID de comando | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| `cm_Options` | Abra el cuadro de diálogo Preferencias/Configuración de la aplicación | `⌘,` | `Ctrl+,` | Principal | 
| `cm_HelpContents` / `cm_HelpIndex` | Abrir guía y documentación interactiva para el usuario | `⌘?` / `F1` | `F1` | Principal | 
| `cm_HelpKeyboard` | Abrir tarjeta de referencia de atajos de teclado rápidos | `cm_HelpKeyboard` | *(Menú: Ayuda ➔ Teclado)* | Principal | 
| `cm_Exit` | Salir/Salir de ATBCmder | `⌘Q` | `F10` / `Alt+F4` / `Alt+X` | Principal | 
| `cm_About` | Mostrar versión, licencia y créditos de ATBCmder | `cm_About` | *(Menú: ATBCmder ➔ Acerca de)* | Principal | 
| `cm_OpenConfigDirectory` | Mostrar carpeta de configuración (`atbcmder.xml`) en el panel | `cm_OpenConfigDirectory` | *(Menú: Configuración ➔ Abrir Configuración)* | Principal | 
| `cm_ExportConfiguration` | Exportar todas las preferencias a un paquete ZIP portátil | `cm_ExportConfiguration` | *(Menú: Configuración ➔ Exportar)* | Principal | 
| `cm_ImportConfiguration` | Importar preferencias desde un paquete ZIP portátil | `cm_ImportConfiguration` | *(Menú: Configuración ➔ Importar)* | Principal | 
| `cm_CheckForUpdate` | Buscar actualizaciones del software de la aplicación | `cm_CheckForUpdate` | *(Menú: Ayuda ➔ Buscar actualizaciones)* | Principal | 

---

## 5. Atajos de contexto de herramientas modales

Al abrir herramientas especializadas como Universal Lister, el editor de texto integrado, las diferencias en paralelo o los diálogos por lotes, ATBCmder activa mapas de teclas específicos del contexto. Estos accesos directos funcionan directamente dentro de cada ventana de herramientas en lugar de a través de comandos de registro globales `cm_*` de toda la aplicación.

### 5.1 Listador universal (`Viewer` contexto)

Activo al obtener una vista previa de documentos, texto, código, imágenes, audio, vídeo o bytes hexadecimales sin formato.

| Acción / Característica | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| Seleccionar todo | Seleccionar todo el texto/contenido en el visor | `⌘A` | `Ctrl+A` | Visor | 
| Modo de texto sin formato | Cambiar al modo Texto sin formato | `1` | `1` | Visor | 
| Modo binario | Cambiar al modo binario | `2` | `2` | Visor | 
| Modo hexagonal sin formato | Cambiar al modo de inspección de bytes hexadecimales sin formato | `3` | `3` | Visor | 
| Modo decimal | Cambiar al modo decimal | `4` | `4` | Visor | 
| Ver libro | Cambiar al modo Libro paginado | `5` | `5` | Visor | 
| Ver imagen | Cambiar al modo Visor de imágenes | `6` | `6` | Visor | 
| Complementos personalizados | Cambiar al visor de complementos personalizado | `7` | `7` | Visor | 
| Vista PDF/Oficina | Cambiar al modo lector de documentos PDF/Office | `8` | `8` | Visor | 
| Modo de código | Cambiar al modo de código resaltado por sintaxis | `9` | `9` | Visor | 
| Imagen central | Centrar la imagen dentro de la ventana del visor | `C` | `C` | Visor | 
| Ajustar a la ventana | Ajustar imagen a las dimensiones de la ventana | `F` | `F` | Visor | 
| Solo ajuste grande | Reducir la escala solo si la imagen excede las dimensiones de la ventana | `L` | `L` | Visor | 
| Alternar envoltura | Activar o desactivar el ajuste de línea | `W` | `W` | Visor | 
| Alternar cursor | Alternar cursor de texto visible cursor | `F6` | `F6` | Visor | 
| Buscar texto | Buscar texto dentro del documento | `⌘F` / `F7` | `F7` | Visor | 
| Buscar siguiente | Saltar a la siguiente búsqueda | `⌘G` / `F3` | `F3` | Visor | 
| Buscar anterior | Saltar a la búsqueda anterior | `⇧⌘G` / `⇧F3` | `Shift+F3` | Visor | 
| Acercar | Ampliar imagen o PDF | `⌘+` / `Num+` | `Num+` | Visor | 
| Alejar | Alejar imagen o PDF | `⌘-` / `Num-` | `Num-` | Visor | 
| Pantalla completa | Alternar modo de visualización de pantalla completa | `⌃⌘F` / `⌥⏎` | `Alt+Enter` | Visor | 
| Cerrar Visor | Cerrar la ventana del visor Lister | `⎋` *(Esc)* / `Q` | `Escape` / `Q` | Visor |

---

### 5.2 Editor de texto integrado (`Editor` contexto)

Activo al crear o modificar archivos de texto y código fuente. 

| Acción / Característica | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| Guardar archivo | Guardar el archivo modificado en el disco | `⌘S` / `F2` | `F2` | Redactor | 
| Buscar texto | Buscar texto en el documento del editor | `⌘F` / `F7` | `F7` | Redactor | 
| Buscar siguiente | Saltar a la siguiente búsqueda | `⌘G` / `F3` | `F3` | Redactor | 
| Buscar anterior | Saltar a la búsqueda anterior | `⇧⌘G` / `⇧F3` | `Shift+F3` | Redactor | 
| Cortar | Cortar el texto seleccionado al portapapeles | `⌘X` | `Ctrl+X` | Redactor | 
| Copiar | Copiar el texto seleccionado al portapapeles | `⌘C` | `Ctrl+C` | Redactor | 
| Pegar | Pegar texto desde el portapapeles | `⌘V` | `Ctrl+V` | Redactor | 
| Deshacer | Deshacer la última acción escrita | `⌘Z` | `Ctrl+Z` | Redactor | 
| Rehacer | Rehacer la última acción deshecha | `⇧⌘Z` | `Ctrl+Shift+Z` | Redactor | 
| Seleccionar todo | Seleccionar el texto completo del documento | `⌘A` | `Ctrl+A` | Redactor | 
| Cerrar editor | Cerrar la ventana del editor de texto | `⎋` *(Esc)* / `⌘W` | `Esc` / `Alt+X` | Redactor | 

---

### 5.3 Diferencia visual en paralelo (`Differ` contexto)

Activo dentro de la herramienta de comparación de diferencias visuales. 

| Acción / Característica | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| Buscar texto | Buscar texto dentro de los paneles de diferencia | `⌘F` / `F7` | `F7` | difieren | 
| Buscar siguiente | Saltar a la siguiente aparición de búsqueda | `⌘G` / `F3` | `F3` | difieren | 
| Buscar anterior | Saltar a la aparición de búsqueda anterior | `⇧⌘G` / `⇧F3` | `Shift+F3` | difieren | 
| Siguiente diferencia | Saltar el cursor al siguiente bloque de diferencias | `⌥↓` *(Opción+Abajo)* | `Alt+Down` | difieren | 
| Diferencia anterior | Saltar cursor al bloque de diferencias anterior | `⌥↑` *(Opción+Arriba)* | `Alt+Up` | difieren | 
| Primera diferencia | Saltar directamente a la primera diferencia en archivos | `⌥Fn+←` *(Opc+Inicio)* | `Alt+Home` | difieren | 
| Última diferencia | Saltar directamente a la última diferencia en archivos | `⌥Fn+→` *(Opc+Fin)* | `Alt+End` | difieren | 
| Copiar de derecha a izquierda | Copie el bloque de diferencia del panel derecho al panel izquierdo | `⌥←` *(Opción+Izquierda)* | `Alt+Left` | difieren | 
| Copiar de izquierda a derecha | Copie el bloque de diferencia del panel izquierdo al panel derecho | `⌥→` *(Opción+Derecha)* | `Alt+Right` | difieren | 
| Actualizar / Volver a escanear | Vuelva a leer los archivos del disco y vuelva a ejecutar la comparación de diferencias | `⌘R` | `Ctrl+R` | difieren | 
| Cerrar Diferir | Cerrar ventana de comparación de diferencias | `⎋` *(Esc)* / `⌘W` | `Alt+X` / `Esc` | difieren | 

---

### 5.4 Cuadro de diálogo Búsqueda avanzada de archivos (`FindFiles` Contexto)

Activo dentro del cuadro de diálogo de búsqueda multiproceso en segundo plano. 

| Acción / Característica | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| Iniciar búsqueda | Iniciar ejecución de búsqueda | `⏎` *(Retorno)* / `F9` | `F9` | Buscar archivos | 
| Cancelar / Cerrar | Cancelar la búsqueda en ejecución o cerrar el diálogo | `⎋` *(Esc)* | `Esc` | Buscar archivos | 
| Ver seleccionados | Ver el resultado de búsqueda seleccionado en Lister | `⌘3` / `F3` | `F3` | Buscar archivos | 
| Editar seleccionados | Abrir el resultado de búsqueda seleccionado en Editor | `⌘4` / `F4` | `F4` | Buscar archivos | 
| Nueva búsqueda | Restablecer consulta de búsqueda y preparar nueva búsqueda | `⌘N` | `Ctrl+N` | Buscar archivos | 
| Borrar filtros | Nueva búsqueda con todos los filtros de fecha/tamaño/atributo borrados | `⇧⌘N` | `Ctrl+Shift+N` | Buscar archivos | 
| Recordar Anterior | Recuperar parámetros de la búsqueda anterior | `⌘L` | `Ctrl+L` | Buscar archivos | 

---

### 5.5 Herramienta de cambio de nombre múltiple por lotes (`MultiRename` contexto)

Activo dentro del espacio de trabajo de cambio de nombre por lotes. 

| Acción / Característica | Descripción | Acceso directo principal de macOS (con glifos ⌘/⌥/⇧/⌃) | Atajo de Classic Commander (con teclas Fn) | Contexto | 
| :--- | :--- | :---: | :---: | :---: | 
| Restablecer reglas | Restablecer el cambio de nombre de las reglas de máscara y patrón a los valores predeterminados | `⌘R` | `Ctrl+R` | Cambio de nombre múltiple | 
| Editar nombres en el editor | Abra la lista de nombres de archivos de destino en un editor externo para editarlos manualmente | `⌘I` | `Ctrl+I` | Cambio de nombre múltiple | 
| Cargar archivo de nombres | Cargar nombres de reemplazo desde un archivo de texto externo | `F3` | `F3` | Cambio de nombre múltiple | 

---

## 6. Consejos profesionales y optimización de teclas de acceso rápido del sistema

### 6.1 Resolución de colisiones de accesos directos globales de macOS

Ciertas teclas de acceso rápido predeterminadas del sistema macOS interceptan las pulsaciones de teclas antes de que lleguen a las aplicaciones de escritorio. Para desbloquear la agilidad total de Commander, puedes personalizar o desactivar los atajos conflictivos de macOS: 

1. **Búsqueda destacada (`⌘Space` frente a Búsqueda rápida)**: 
- De forma predeterminada, `⌘Space` activa Spotlight. Si prefiere utilizar `⌘Space` para marcar archivos o buscar en el panel, reasigne Spotlight a `⌥Space` en **Configuración del sistema ➔ Teclado ➔ Atajos de teclado... ➔ Spotlight**. 
2. **Control de misión (`⌃↑`) y exposición de aplicaciones (`⌃↓`)**: 
- macOS usa `⌃↑` y `⌃↓` para Mission Control. En ATBCmder, `⌃↓` abre el menú desplegable Historial del directorio. Puedes reasignar Mission Control en **Configuración del sistema ➔ Teclado ➔ Atajos de teclado... ➔ Mission Control**. 
3. **Ocultación de aplicaciones (`⌘H`)**: 
- En macOS, `⌘H` oculta la aplicación principal. ATBCmder usa `⌘H` o `⇧⌘.` para alternar archivos de puntos ocultos. Si desea que `⌘H` alterne estrictamente los archivos ocultos, desactive "Ocultar aplicación" en macOS o utilice el estándar Finder `⇧⌘.` (`Cmd+Shift+Period`). 
4. **Minimización de ventana (`⌘M`)**: 
- macOS asigna `⌘M` para minimizar la ventana al Dock. ATBCmder asigna `⌘M` a la herramienta de cambio de nombre múltiple por lotes (`cm_MultiRename`). ATBCmder captura `⌘M` dentro de su ventana principal, pero también puede activar el cambio de nombre múltiple a través de `Ctrl+M` o la barra de herramientas. 

---

### 6.2 Ergonomía del trackpad y el mouse

Para usuarios de portátiles sin un teclado externo, ATBCmder combina atajos de teclado con gestos intuitivos del trackpad: 

* **Pellizca para ampliar las miniaturas**: en la vista de miniaturas (`cm_ThumbnailsView`), pellizca hacia adentro o hacia afuera en el trackpad de tu MacBook (o mantén presionado `⌃` y desplázate) para cambiar el tamaño de las vistas previas en miniatura continuamente desde `48 px` hasta `512 px`. 
* **Deslizar con dos dedos hacia atrás o hacia adelante**: deslice dos dedos hacia la izquierda o hacia la derecha en la tabla de archivos para navegar hacia atrás (`cm_ViewHistoryPrev`) y hacia adelante (`cm_ViewHistoryNext`) a través del historial de carpetas. 
* **Divisor de doble clic**: Haga doble clic en cualquier lugar de la barra divisoria central vertical para restablecer los paneles a una división horizontal exacta de 50/50. 
* **Haga clic con el medio en las pestañas**: haga clic con el botón central (o toque con tres dedos) en cualquier pestaña de la carpeta para cerrarla inmediatamente sin presionar `⌘W`. 

---

### 6.3 Personalización de combinaciones de teclas en Preferencias

Cada atajo documentado anteriormente se puede personalizar o recuperar: 

1. Presione **`⌘,`** (o seleccione **Configuración ➔ Opciones...**) para abrir el cuadro de diálogo Preferencias. 
2. Seleccione **Teclas de acceso rápido** en la barra lateral. 
3. Utilice el menú desplegable **Context** para elegir qué área desea configurar (`Main`, `FilePanel`, `Viewer`, etc.). 
4. Utilice el cuadro de filtro de búsqueda para localizar cualquier comando por nombre o `cm_*` ID. 
5. Haga clic en el cuadro de acceso directo y presione la combinación de teclas que desee. El detector de colisiones incorporado le avisará inmediatamente si ese acorde ya está asignado a otro lugar. 
6. Haga clic en **Aplicar** para activar los cambios instantáneamente sin reiniciar la aplicación. 

Las combinaciones de teclas del usuario se guardan en `~/.config/atbcmder/atbcmder_hotkeys.xml` (o `~/Library/Preferencias/atbcmder/` en macOS). Puede exportar y transferir este archivo entre máquinas usando **`cm_ExportConfiguration`**. 

--- 

<div align="center"> 
<p>¿Busca recetas prácticas para el día a día, flujos de trabajo de montaje de NAS o consejos para la resolución de problemas?</p> 
<p><strong><a href="faq_howtos.md">Continúe con el Capítulo 9: Recetas del mundo real y solución de problemas &rarr;</a></strong></p> 
</div>