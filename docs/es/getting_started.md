# Capítulo 1: Fundamentos y configuración de macOS

¡Bienvenido a **ATBCmder**! Diseñado de forma nativa para macOS 12+ en Apple Silicon (M1/M2/M3/M4, arquitectura ARM64; Intel x86_64 no es compatible actualmente), ATBCmder brinda velocidad, agilidad del teclado y precisión inigualables de la administración de archivos ortodoxa de panel dual a Mac. 

Este capítulo lo guía a través de la filosofía central del panel dual, detalla cada hito importante de la interfaz, lo guía a través de la incorporación de permisos de macOS App Sandbox y proporciona las configuraciones esenciales del sistema necesarias para una experiencia perfecta. 

---

## 1. Inicio rápido visual: la filosofía del panel dual

Si ha utilizado macOS Finder, está acostumbrado a abrir múltiples ventanas superpuestas, arrastrar archivos a través de escritorios desordenados y esperar que los archivos terminen en la carpeta de destino deseada en lugar de en una subcarpeta adyacente accidental. 

ATBCmder reemplaza esta fricción con el paradigma probado **Orthodox File Manager (OFM)**: dos paneles de directorio independientes y complementarios colocados uno al lado del otro. 

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

### El modelo activo (fuente) versus inactivo (destino)

En ATBCmder, nunca tendrás que preguntarte dónde tendrá efecto una operación: 

1. **El Panel Activo (Fuente)**: 
- Este es el panel donde residen actualmente el foco del teclado y el cursor. 
- Cualquier selección, navegación o acción que realice se dirige directamente a este panel. 
- **Señal visual**: el panel activo presenta un anillo de enfoque prominente (color de acento del sistema macOS), texto de pestaña resaltado y un cursor activo distintivo resaltado en el elemento actualmente enfocado. 

2. **El panel inactivo (objetivo)**: 
- Este es el panel opuesto. Permanece completamente visible y muestra una jerarquía de carpetas independiente. 
- El panel inactivo actúa como **destino automático** para las operaciones de archivos iniciadas en el panel activo. 
- **Señal visual**: el panel inactivo muestra un borde tenue, texto ligeramente atenuado y títulos de pestañas silenciados.

### Operaciones direccionales: siempre fuente ➔ objetivo

Cuando inicia una operación en ATBCmder, la aplicación entiende automáticamente la dirección: 

- **Copiar (`F5` / `Cmd+C` ➔ `Cmd+V`)**: Copia los archivos seleccionados del panel Activo (Fuente) directamente al directorio que se muestra actualmente en el panel Inactivo (Destino). 
- **Mover (`F6` / `Cmd+C` ➔ `Opt+Cmd+V`)**: Mueve archivos seleccionados del panel Activo al panel Inactivo sin necesidad de escribir o buscar el directorio de destino. 
- **Sincronización de directorios (`Shift+F12` / `cm_SyncDirs`)**: Compara el directorio en el panel activo con el directorio en el panel inactivo. 

> [!CONSEJO] 
> **No se requieren conjeturas de arrastrar y soltar**: no es necesario arrastrar elementos a través de los límites de la pantalla. Simplemente seleccione lo que desea en el panel activo, presione `F5` (Copiar) o `F6` (Mover), presione `Enter` para confirmar el mensaje y ATBCmder transferirá los archivos inmediatamente.

### Navegación del panel y cambio de enfoque

| Acción | Acceso directo a macOS | Llave de comandante clásica | ID de comando | Descripción | 
| :--- | :--- | :--- | :--- | :--- | 
| **Cambiar enfoque** | `Tab` | `Tab` | `cm_FocusSwap` | Alterna el enfoque del teclado entre los paneles izquierdo y derecho (`cm_SwitchPanel`). | 
| **Enfoque inverso** | `Shift+Tab` | `Shift+Tab` | `cm_FocusSwap` | Invierte el orden de enfoque en paneles y controles. | 
| **Intercambiar izquierda y derecha** | `Ctrl+U` | `Ctrl+U` | `cm_Exchange` | Intercambia rutas de directorio entre los paneles izquierdo y derecho sin perder pestañas ni selecciones. | 
| **Relación de ecualización** | `Double-click splitter` | `Double-click splitter` | — | Restablece automáticamente el divisor medio a un equilibrio limpio 50/50. | 

---

## 2. Anatomía de la interfaz y recorrido por lugares emblemáticos

ATBCmder proporciona una interfaz macOS limpia y nativa construida con Qt6 y PySide6, diseñada de acuerdo con las pautas de interfaz humana de Apple y al mismo tiempo respeta los flujos de trabajo clásicos de Commander centrados en el teclado. 

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

### [1] Barra de menú nativa de macOS

Totalmente integrado en la barra de menú superior de macOS. Todas las operaciones, cambios de vista, herramientas eléctricas y preferencias se clasifican de forma lógica: 

- **Archivo**: Nueva pestaña, Cerrar pestaña, Propiedades del archivo, Permisos de Sandbox, Salir. 
- **Marcar**: Seleccionar grupo (`Num+`), Deseleccionar grupo (`Num-`), Invertir selección (`Num*`), Seleccionar todo (`Cmd+A`). 
- **Comandos**: Lista activa de directorios (`Ctrl+D`), Unidades izquierda/derecha (`Alt+F1/F2`), Búsqueda (`Alt+F7`), Sincronización de directorios (`Shift+F12`), Paneles de intercambio (`Ctrl+U`), Terminal (`Ctrl+J`). 
- **Mostrar**: alterna el modo de vista (breve, columnas completas, miniaturas, árbol, vista de rama plana), visibilidad de la barra de herramientas, diseño de paneles horizontales. 
- **Configuración**: Opciones/Preferencias (`Cmd+,`), Guardar Posición (`cm_ConfigSavePos`), Guardar Pestañas.

### [2] Barra de herramientas principal superior

Ubicado directamente debajo de la barra de título de la ventana. Proporciona acceso instantáneo con un solo clic a comandos globales: 

- **Acciones predeterminadas**: Actualizar (`Ctrl+R`), Vista rápida (`Ctrl+Q`), Copiar (`F5`), Mover (`F6`), Nueva carpeta (`F7`), Eliminar (`F8`), Buscar (`Alt+F7`) y Opciones (`Cmd+,`). 
- **Personalizable**: personalice los tamaños de los íconos (de 16 px a 48 px), alterne las etiquetas de texto de los botones u oculte la barra de herramientas por completo a través del menú **Mostrar** → **Mostrar barra de herramientas** para maximizar el espacio en pantalla.

### [3] Barra de navegación interactiva estilo Finder

Ubicada encima de cada panel de archivos, la barra de ruta de navegación permite saltos de jerarquía ultrarrápidos: 

- **Navegación por segmentos**: haga clic en cualquier carpeta ancestral en la cadena de ruta de navegación (por ejemplo, haciendo clic en `username` en `/Users/username/Projects/ATBCmder`) para navegar directamente a ese directorio. 
- **Menú desplegables de hermanos**: coloque el cursor o haga clic en la flecha de galón entre los segmentos para revelar un menú desplegable que enumera todas las carpetas hermanas en ese nivel. 
- **Menú contextual de segmento**: haga clic derecho en cualquier segmento de ruta de navegación para acceder a utilidades contextuales rápidas: 
- **Abrir en una pestaña nueva**: mantiene su vista actual mientras abre el directorio principal en una pestaña nueva. 
- **Revelar en Finder**: abre el directorio en macOS Finder (`open -R`). 
- **Copiar ruta**: copia la ruta UNIX absoluta del segmento al portapapeles de su sistema. 
- **Abrir en Terminal**: genera el Terminal macOS directamente dentro de esa carpeta (`open -a Terminal`). 
- **Edición de ruta directa (`BreadcrumbLineEdit`)**: haga doble clic en el espacio vacío a la derecha de la cadena de ruta de navegación. La barra se convierte instantáneamente en un campo de texto editable donde puede pegar o escribir cualquier ruta (por ejemplo, archivos `/var/log`, `~/Library` o `vfs://`). Presione `Enter` para navegar o `Esc` para cancelar.

### [4] Barra de pestañas de carpetas

Cada panel mantiene un conjunto independiente de pestañas: 

- Abra nuevas pestañas con `Cmd+T` (`cm_NewTab`), cierre pestañas con `Cmd+W` (`cm_CloseTab`). 
- Arrastrar y soltar para reordenar pestañas dentro de un panel. 
- Haga clic derecho en las pestañas para bloquear rutas, cambiar el nombre de los títulos, cerrar duplicados o duplicar pestañas en el panel opuesto.

### [5] Paneles de archivos duales

Listas de archivos virtualizados de alto rendimiento capaces de representar carpetas con cientos de miles de entradas sin problemas y sin tartamudeos en la interfaz de usuario: 

- Ordenación de columnas: haga clic en cualquier encabezado (Nombre, Extensión, Tamaño, Fecha, Atributos) para ordenar de forma ascendente o descendente. 
- Múltiples modos de visualización: vista de detalles completos, vista de cuadrícula breve, vista de galería de miniaturas, vista de árbol y vista de rama plana recursiva (`Cmd+B`).

### [6] Barra de herramientas central y divisor arrastrable

Ubicada directamente entre los paneles de archivos izquierdo y derecho, la barra de herramientas central es una característica única de ATBCmder que combina la administración de archivos con un solo clic con un divisor de panel ajustable: 

![Middle Toolbar](images/middle_toolbar.png) 

- **Tira de acción rápida**: alberga botones verticales para operaciones comunes: 
- `cm_Copy` (Copia) 
- `cm_Move` (Mover/Cortar) 
- `cm_Delete` (Eliminar a la Papelera) 
- `cm_MkDir` (Nuevo directorio) 
- `cm_Rename` (cambio de nombre rápido en línea) 
- `cm_View` (Listador universal) 
- `cm_Edit` (Editor de texto/código interno) 
- `cm_Exchange` (Intercambiar paneles izquierdo y derecho) 
- `cm_SyncDirs` (Sincronizador de carpetas) 
- `cm_FileSearch` (Búsqueda avanzada) 
- **Arrastre continuo del divisor**: al mover el cursor del mouse sobre la barra central, el puntero cambia a un cursor dividido horizontal (`SplitHCursor`). Haga clic y arrastre horizontalmente para ajustar suavemente la proporción de ancho entre los dos paneles. 
- **Preajustes de proporción de tema con estilo**: cuando se utiliza el tema moderno "Elegante", la barra central muestra controles segmentados que permiten ajustar instantáneamente a la distribución del ancho del panel **50/50**, **70/30** o **30/70**. 
- **Preferencias de la barra de herramientas intermedia**: habilite o deshabilite la barra de herramientas intermedia, ajuste el tamaño de los iconos o alterne entre botones planos modernos y divisores hundidos clásicos en **Preferencias** (`Cmd+,`) → **Barras de herramientas** → **Barra de herramientas intermedia**.

### [7] Barra de estado y medidor de almacenamiento en unidad

Anclado en la parte inferior de la ventana: 

- **Estadísticas de selección**: Muestra métricas en tiempo real para el panel activo: 
- Recuento total de elementos y tamaño total de carpeta. 
- Número de elementos seleccionados y tamaño de bytes seleccionado combinado. 
- **Medidor de almacenamiento en unidad**: indicador visual de uso del disco que muestra el nombre del volumen actualmente montado (por ejemplo, `Macintosh HD`), la capacidad total, el almacenamiento utilizado y el porcentaje de espacio libre restante. 

---

## 3. Receta paso a paso: Permisos del sistema de archivos y zona de pruebas de la aplicación macOS

macOS moderno emplea una estricta zona de pruebas de seguridad de aplicaciones para proteger los datos del usuario del acceso no autorizado. Cuando se ejecuta ATBCmder (particularmente cuando se instala a través de Mac App Store o se distribuye con el sandboxing habilitado), la aplicación se aísla en su propio directorio contenedor seguro: 
`~/Library/Containers/com.aitobox.atbcmder/Data` 

De forma predeterminada, las aplicaciones de espacio aislado no pueden inspeccionar ni modificar arbitrariamente archivos fuera de su contenedor a menos que el usuario otorgue permiso explícitamente a través de los paneles abiertos nativos de Apple. 

ATBCmder agiliza este proceso de incorporación con **Marcadores con ámbito de seguridad**, lo que le permite otorgar permiso una vez y disfrutar de un acceso persistente y sin restricciones en todas las sesiones futuras.

### Comprensión de los marcadores con ámbito de seguridad

Cuando autoriza una ruta de carpeta usando macOS `NSOpenPanel`: 

1. macOS emite un **Marcador con ámbito de seguridad** criptográfico (`NSURLBookmarkCreationWithSecurityScope`). 
2. ATBCmder serializa y guarda este marcador en su directorio de configuración: 
`~/Library/Application Support/ATBCmder/sandbox_bookmarks.plist` 

3. En cada inicio de la aplicación, ATBCmder resuelve y activa automáticamente estos marcadores a través de `startAccessingSecurityScopedResource()`. 
4. Una vez otorgado, nunca más tendrá que volver a autorizar estos directorios.

### Tutorial de configuración guiada: uso de `cm_GrantFilesystemAccess`

Para configurar sus permisos en el primer inicio, o en cualquier momento posterior, siga estos pasos:

#### Paso 1: abra el Asistente de incorporación de permisos

Desde la barra de menú nativa, seleccione **Archivo** (o **Ayuda**) → **Conceder acceso al sistema de archivos…**, o active el comando interno `cm_GrantFilesystemAccess`. Aparece el cuadro de diálogo de incorporación: 

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

#### Paso 2: Conceder acceso al directorio raíz (`/`)

1. Haga clic en **"Conceder acceso al directorio raíz (/)"**. 
2. ATBCmder invoca la hoja `NSOpenPanel` nativa de macOS, apuntando al disco raíz `Macintosh HD` (`/`). 
3. Haga clic en **"Otorgar acceso"** (o **Abrir**). 
4. El botón se actualiza inmediatamente a **"Acceso al directorio raíz concedido ✓"** y se desactiva. 
5. **Qué permite esto**: La autorización de la ruta raíz `/` cubre automáticamente todos los directorios de usuarios (`~/Documents`, `~/Downloads`, `~/Desktop`, `~/Projects`, `/Applications`, etc.) porque Los marcadores con ámbito de seguridad heredan automáticamente permisos descendentes para todas las subrutas secundarias.

#### Paso 3: Conceder acceso a discos externos (`/Volumes`)

1. Haga clic en **"Conceder acceso a discos externos (/volúmenes)"**. 
2. Cuando el panel nativo muestre `/Volumes`, haga clic en **"Conceder acceso"**. 
3. El botón se actualiza a **"Acceso a discos externos concedido ✓"**. 
4. **Qué permite esto**: acceso de lectura/escritura sin restricciones a unidades USB externas, unidades Thunderbolt, tarjetas SD, montajes de imágenes de disco DMG y volúmenes SMB/NFS/AFP montados en red.

#### Paso 4: Acceso selectivo carpeta por carpeta (alternativa)

Si prefiere no otorgar acceso raíz amplio a ATBCmder, no tiene que hacer clic en acceso raíz: 

- Cuando navega a una carpeta no autorizada (como una carpeta externa o un repositorio de proyectos), ATBCmder detecta el límite del permiso y muestra un mensaje bajo demanda: 
`ATBCmder requires your permission to access: /Users/username/SecretProject` 

- Haga clic en **"Conceder acceso a la carpeta"**, apruebe el cuadro de diálogo nativo y ese directorio específico se marcará permanentemente.

#### Paso 5: Acceso completo al disco (FDA) para datos protegidos del sistema

> [!IMPORTANTE] 
> **Marcadores de Sandbox frente a acceso completo al disco (FDA)**: 
> 
> - **Marcadores de Sandbox** otorgan acceso general al sistema de archivos a carpetas de usuario estándar, archivos y unidades externas. 
> - **Acceso completo al disco (FDA)** es un permiso de privacidad adicional de Transparencia, Consentimiento y Control (TCC) de macOS necesario para inspeccionar datos personales confidenciales de macOS (como el historial de Safari, archivos adjuntos de correo, mensajes, copias de seguridad de Time Machine y cachés del sistema). 
> 
> Si necesita administrar estas carpetas protegidas: 
> 
> 1. Haga clic en **"Abrir configuración de acceso completo al disco..."** en el cuadro de diálogo de incorporación. 
> 2. macOS abre **Configuración del sistema** → **Privacidad y seguridad** → **Acceso total al disco**. 
> 3. Haga clic en el candado o autentíquese con Touch ID/contraseña. 
> 4. Asegúrese de que el interruptor de palanca junto a **ATBCmder** esté en **ON**.

### Revocar y restablecer permisos

Si alguna vez necesita restablecer o revocar sus marcadores de sandbox: 

1. Abra el directorio de configuración de ATBCmder a través del menú **Configuración** → **Abrir directorio de configuración** (`cm_OpenConfigDirectory`). 
2. Elimine el archivo `sandbox_bookmarks.plist`. 
3. Reinicie ATBCmder. 
4. Para restablecer los permisos TCC a nivel del sistema macOS, ejecute el siguiente comando en la Terminal macOS: 
   ```bash
   tccutil reset SystemPolicyAllFiles com.aitobox.atbcmder
   ```
 

---

## 4. Configuración de idioma y personalización de apariencia

ATBCmder está localizado para flujos de trabajo globales y se integra perfectamente con las preferencias de apariencia de macOS.

### Internacionalización y anulaciones de idiomas

ATBCmder admite **más de 30 idiomas**, incluidos inglés, chino simplificado (简体中文), chino tradicional (繁體中文), alemán (Deutsch), francés (Français), español (Español), ruso (Русский), japonés (日本語), italiano, polaco, coreano y más. 

![Language Settings](images/language_settings.png) 

- **Seguimiento automático del idioma del sistema**: de forma predeterminada, ATBCmder detecta la configuración regional de su sistema macOS (`AppleLanguages`) al iniciar y aplica la traducción coincidente automáticamente. 
- **Selección manual de idioma**: 
1. Abra Preferencias presionando `Cmd+,` o ejecutando `cm_Options`. 
2. En el panel de navegación izquierdo, seleccione **Idioma**. 
3. Elija su idioma preferido de la lista desplegable. 
- **Recarga en vivo (no es necesario reiniciar)**: a diferencia de la mayoría de las utilidades tradicionales de Mac que requieren salir y reiniciar la aplicación, ATBCmder retraduce dinámicamente toda la interfaz (menús, barras de herramientas, cuadros de diálogo, información sobre herramientas de botones y mensajes de estado) en tiempo real en el momento en que selecciona un nuevo idioma.

### Apariencia y temas

ATBCmder es totalmente compatible con los modos de apariencia Claro y Oscuro de macOS: 

- **Sincronización de apariencia del sistema**: cambia automáticamente entre el modo claro y oscuro cada vez que cambia la apariencia del sistema macOS (por ejemplo, al atardecer o a través del Centro de control). 
- **Opciones de tema**: 
- **Fusion / Native macOS**: estética de escritorio limpia y clásica que respeta los colores destacados de macOS y la vitalidad de las ventanas. 
- **Tema con estilo**: estética moderna con controles segmentados redondeados, separadores de degradado sutiles y barras de pestañas en forma de píldora. 
- **Paleta de modo oscuro**: utiliza superficies de carbón oscuro (`#2C2C2E` / `#242426`) con texto de alto contraste e íconos de carpetas personalizados, lo que reduce la fatiga visual en entornos con poca luz. 
- **Paleta de modo claro**: fondo blanco nítido con divisores grises suaves (`#FAFBFD` / `#EEF2F7`) y bordes de contraste claros. 

---

## 5. ⚡ Consejos profesionales y configuraciones de diseño avanzadas

Aproveche al máximo el motor de diseño flexible de ATBCmder para adaptar su espacio de trabajo a configuraciones de gestión de datos especializadas, ultraanchas o de múltiples monitores.

### Consejo 1: guardar la posición de la ventana y las proporciones de diseño (`cm_ConfigSavePos`)

Cuando organiza su espacio de trabajo (personalizando las dimensiones de la ventana, maximizándola en una pantalla externa o estableciendo una proporción de divisor central específica), puede bloquear esta configuración para que se restaure de manera idéntica cada vez: 

1. Organice la ventana principal de ATBCmder y ajuste el divisor central a su proporción preferida. 
2. Seleccione el menú **Configuración** → **Guardar posición y diseño**, o ejecute el comando interno: 
   ```
   cm_ConfigSavePos
   ```
 

3. El tamaño de su ventana, las coordenadas de la pantalla, el estado maximizado y las proporciones del panel se escriben directamente en `atbcmder.xml`. 
4. En **Preferencias** → **Diseño**, asegúrese de que **"Guardar posición de la ventana al salir"** esté marcado para actualizaciones automáticas continuas.

### Consejo 2: alternar el diseño de panel dual horizontal (`cm_HorizontalFilePanels`)

Si bien los paneles verticales uno al lado del otro son estándar para operaciones con archivos, los paneles horizontales apilados (panel superior y panel inferior) son excepcionalmente útiles cuando: 

- Trabajar con nombres de archivos ultralargos que requieren un ancho de pantalla completo. 
- Comparación de columnas amplias de metadatos de archivos (permisos, propietarios, sumas de verificación, dimensiones). 
- Trabajar en monitores verticales rotados o tabletas. 

Para cambiar diseños: 

1. Seleccione el menú **Mostrar** → **Paneles horizontales** o active el comando interno: 
   ```
   cm_HorizontalFilePanels
   ```
 

2. Cuando el modo horizontal está activo: 
- Los paneles se apilan verticalmente (Panel superior y Panel inferior). 
- La barra de herramientas central gira automáticamente formando una franja horizontal entre los paneles superior e inferior. 
- El cursor de arrastre se adapta a un puntero de división vertical (`SplitVCursor`), lo que le permite cambiar el tamaño de la relación de altura entre los paneles superior e inferior sin esfuerzo.

### Consejo 3: Ajuste del divisor medio con un clic

- **Saldo instantáneo 50/50**: haga doble clic en cualquier lugar de la barra divisoria central o de la línea separadora. Los paneles vuelven inmediatamente a una división exacta del 50%/50%. 
- **Preajustes de relación**: en el tema "Elegante", al hacer clic en los botones segmentados del medio, el diseño se ajusta a `50:50`, `70:30` (enfatizando el panel de origen) o `30:70` (enfatizando el panel de destino).

### Consejo 4: restauración automática de sesiones y persistencia del espacio de trabajo

ATBCmder cuenta con un subsistema de gestión de sesiones inteligente (`SessionManager`) que garantiza que su entorno de trabajo esté siempre preservado: 

- **Almacenamiento XML de sesión**: el estado de la sesión persiste automáticamente en `atbcmder_session.xml` dentro de su directorio de configuración (`~/Library/Application Support/ATBCmder/`). 
- **Memoria de geometría de ventana**: Restaura las coordenadas exactas de la ventana (`x`, `y`), las dimensiones (`width`, `height`), el estado maximizado y la proporción del divisor medio (`splitter_ratio`). 
- **Restauración de pestaña de panel dual**: 
- Restaura todas las pestañas abiertas en los paneles izquierdo y derecho al iniciar. 
- Recuerda el índice de la pestaña activa en cada panel. 
- Carga automáticamente el directorio de trabajo exacto para cada pestaña, eliminando la fricción de volver a navegar manualmente a carpetas profundas del proyecto. 
- **Bloqueo de posición predeterminada**: También puede bloquear permanentemente la geometría de la ventana actual y la proporción del divisor como configuración de inicio predeterminada usando **Configuración ➔ Guardar posición** (`cm_ConfigSavePos`). 

---

## 6. Alertas de seguridad y sistema: configuración de la tecla de función (Fn) de macOS

Si ha utilizado Total Commander, Double Commander o Norton Commander en el teclado de una PC, sus dedos están entrenados para usar las teclas de función de la fila superior (`F3` Ver, `F4` Editar, `F5` Copiar, `F6` Mover, `F7` MkDir, `F8` Eliminar). 

Sin embargo, los teclados Apple manejan la fila de funciones de manera diferente desde el primer momento. 

> [!ADVERTENCIA] 
> ### 🍎 Conflicto de hardware de teclas de función de macOS 
> En los teclados Apple (teclados integrados de MacBook, Apple Magic Keyboard), las teclas de la fila superior tienen de forma predeterminada **Funciones especiales de hardware de macOS** (Brillo de pantalla, Control de misión, Spotlight, Dictado, No molestar, Controles multimedia y Volumen de audio). 
> 
> Si presiona `F5` en una MacBook sin configuración, macOS intentará ajustar la iluminación del teclado o activar el dictado en lugar de copiar sus archivos.

### Opción A: mantenga presionada la tecla `Fn` (Globo 🌐) (configuración predeterminada de macOS)

Si prefieres mantener intactas las claves multimedia predeterminadas de Apple: 

- Mantenga presionada la tecla **`Fn`** (o Globo 🌐) mientras presiona cualquier tecla de función: 
- `Fn+F3`: Listador universal 
- `Fn+F4`: Editor interno 
- `Fn+F5`: Copiar archivos 
- `Fn+F6`: Mover archivos 
- `Fn+F7`: Crear carpeta 
- `Fn+F8`: Eliminar a la Papelera

### Opción B: habilitar las teclas de función estándar en todo el sistema (recomendado)

Si desea reflejos Commander auténticos y de alta velocidad con una sola tecla sin mantener presionado el modificador `Fn`: 

1. Abra **Configuración del sistema** desde el menú Apple (). 
2. Haga clic en **Teclado** en la barra lateral. 
3. Haga clic en el botón **Atajos de teclado…**. 
4. En la lista de navegación de la izquierda, seleccione **Teclas de función**. 
5. Habilite la opción: **"Usar las teclas F1, F2, etc. como teclas de función estándar"**. 

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
 

Una vez habilitado: 

- Al presionar `F1`–`F12` se activan directamente los comandos ATBCmder inmediatamente. 
- Para usar los controles de brillo o volumen, simplemente mantenga presionada la tecla `Fn` mientras presiona la tecla. 

---

## 7. Referencia rápida de atajos esenciales de matriz dual

ATBCmder proporciona compatibilidad total con el teclado de matriz dual: use atajos nativos de macOS (`Cmd ⌘`), teclas clásicas de Commander (`Fn`) o ambas indistintamente.

| Acción central | ID de comando | MacOS nativo (`Cmd ⌘`) | Comandante clásico (`Fn`) | Descripción | 
| :--- | :--- | :--- | :--- | :--- | 
| **Lista destacada del directorio** | `cm_DirHotList` | `Cmd+D` / `⌘D` | `Ctrl+D` / `⌃D` | Abre una ventana emergente de marcadores de directorio con búsqueda difusa instantánea. | 
| **Lista de unidades (izquierda/derecha)** | `cm_LeftOpenDrives` / `cm_RightOpenDrives` | `⌥F1` / `⌥F2` (`⌥D`) | `Alt+F1` / `Alt+F2` (`Alt+D`) | Abre el menú de unidad y volumen para el panel izquierdo o derecho (`Alt+D` para el panel activo). | 
| **Copiar archivos** | `cm_Copy` | `Cmd+C` ➔ `Cmd+V` | `F5` (o `Fn+F5`) | Copia los elementos seleccionados del panel activo al panel inactivo. | 
| **Mover archivos** | `cm_Move` | `Cmd+C` ➔ `Opt+Cmd+V` | `F6` (o `Fn+F6`) | Mueve los elementos seleccionados del panel activo al panel inactivo. | 
| **Ver en Lister** | `cm_View` | `Space` / `Cmd+Y` | `F3` (o `Fn+F3`) | Abre un archivo en Universal Lister (código, hexadecimal, imagen, pdf, audio). | 
| **Vista rápida** | `cm_QuickView` | `Cmd+Q` / `Ctrl+Q` | `Ctrl+Q` | Muestra una vista previa instantánea en vivo en el panel opuesto. | 
| **Editar archivo** | `cm_Edit` | `Cmd+E` | `F4` (o `Fn+F4`) | Abre el archivo en el editor de código/texto integrado. | 
| **Nuevo directorio** | `cm_MkDir` | `Shift+Cmd+N` | `F7` (o `Fn+F7`) | Crea una nueva carpeta en el panel activo. | 
| **Eliminar a la Papelera** | `cm_Delete` | `Cmd+Backspace` | `F8` (o `Fn+F8`) | Mueve de forma segura los archivos seleccionados a la Papelera de macOS. | 
| **Cambio de nombre en línea** | `cm_Rename` | `Return` | `F2` / `Shift+F6` | Cambia el nombre del archivo resaltado en el lugar. | 
| **Panel de interruptores** | `cm_FocusSwap` | `Tab` | `Tab` | Cambia el foco del teclado al panel opuesto (`cm_SwitchPanel`). | 
| **Intercambiar izquierda/derecha** | `cm_Exchange` | `Ctrl+U` | `Ctrl+U` | Intercambia rutas de directorio entre los paneles izquierdo y derecho. | 
| **Nueva pestaña** | `cm_NewTab` | `Cmd+T` | `Ctrl+T` | Abre una nueva pestaña de carpeta en el panel actual. | 
| **Cerrar pestaña** | `cm_CloseTab` | `Cmd+W` | `Ctrl+W` | Cierra la pestaña activa. | 
| **Modo horizontal** | `cm_HorizontalFilePanels` | Menú: Mostrar ➔ Horizontal | Menú: Mostrar ➔ Horizontal | Alterna el diseño apilado de lado a lado versus el de arriba y abajo. | 
| **Guardar diseño** | `cm_ConfigSavePos` | Menú: Configuración ➔ Guardar Pos | Menú: Configuración ➔ Guardar Pos | Guarda las dimensiones actuales de la ventana y las proporciones del panel. | 
| **Acceso a la zona de pruebas** | `cm_GrantFilesystemAccess` | Menú: Archivo ➔ Permisos | Menú: Archivo ➔ Permisos | Inicia el asistente de incorporación de macOS App Sandbox. | 
| **Preferencias** | `cm_Options` | `Cmd+,` | `Alt+O` | Abre el cuadro de diálogo de configuración de ATBCmder. |

---

## Próximos pasos

Ahora que domina la base del panel dual y configuró su entorno macOS, continúe con **[Capítulo 2: Navegación y pestañas de carpetas](navigation_and_tabs.md)** para aprender cómo navegar rápidamente por los árboles de directorios, dominar los espacios de trabajo de múltiples pestañas, guardar conjuntos de directorios favoritos, usar listas activas instantáneas y aprovechar las vistas recursivas de ramas planas.