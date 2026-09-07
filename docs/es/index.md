# Bienvenido a ATBCmder

[![macOS](https://img.shields.io/badge/platform-macOS%2012%2B-blue.svg)](download.md) 
[![Architecture](https://img.shields.io/badge/arch-Apple%20Silicon%20(ARM64)-orange.svg)](download.md) 
[![Release](https://img.shields.io/badge/release-latest-green.svg)](download.md) 
[![Privacy](https://img.shields.io/badge/telemetry-zero%20tracking-brightgreen.svg)](privacy_policy.md) 

Bienvenido al portal de documentación oficial de **ATBCmder**: el administrador de archivos rápido, de panel dual y con teclado, diseñado específicamente para macOS. ATBCmder une la herencia de velocidad y comando de los administradores de archivos ortodoxos (Total Commander, Double Commander, Norton Commander) con un diseño moderno de macOS, integración nativa del sistema y herramientas eléctricas avanzadas. 

---

## La filosofía del panel dual

Los administradores de archivos de escritorio tradicionales de ventana única, como macOS Finder, obligan a los usuarios a un ciclo interminable de abrir ventanas superpuestas, perder la pista de las carpetas de origen y destino y correr el riesgo de caídas accidentales en subcarpetas equivocadas. 

```
Traditional File Browsing (Finder):
┌────────────────────────┐      ┌────────────────────────┐
│ Folder A (Where was I?)│ ──?  │ Folder B (Which one?)  │  → Clutter, lost focus,
└────────────────────────┘      └────────────────────────┘    and accidental drops

The ATBCmder Way (Orthodox Dual-Panel):
┌───────────────────────────────┬───────────────────────────────┐
│     ACTIVE PANEL (Source)     │    INACTIVE PANEL (Target)    │
│  Files waiting for action     │  Predictable destination      │
│  [ Copy / Move / Diff / Sync  ═════════════════════════════► ]│
└───────────────────────────────┴───────────────────────────────┘
```
 

ATBCmder resuelve esto a través del **paradigma de panel dual fuente-destino**: 

- **Orientación constante**: dos vistas de directorio independientes están visibles una al lado de la otra en todo momento. 
- **Operaciones direccionales predecibles**: cuando activa Copiar (`F5`) o Mover (`F6`), ATBCmder transfiere automáticamente elementos del **Panel activo** (donde está el cursor) al **Panel inactivo** (la vista opuesta). Sin arrastrar, sin adivinar, sin buscar ventanas de destinos ocultos. 
- **Velocidad del teclado**: mantén las manos en el teclado. Vaya a directorios, seleccione archivos con comodines, inspeccione archivos y ejecute transformaciones por lotes en milisegundos. 
- **Zero Finder Window Clutter**: una ventana maneja todo: volúmenes locales, servidores de red (FTP, SFTP, SMB, WebDAV), contenidos de archivos (`.zip`, `.7z`, `.tar`) y colas de transferencia en segundo plano. 

---

## Visita a la interfaz visual y lugares emblemáticos

ATBCmder organiza la energía en un diseño limpio e intuitivo diseñado para brindarle conocimiento instantáneo de la situación de ambos directorios. 

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ [1] Menu Bar: File   Mark   Commands   Show   Configuration   Help                       │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ [2] Main Toolbar:  [🔍 Search]  [⚡ Queue]  [⚙️ Preferences]  [📁 Drive Bar]             │
├─────────────────────────────────────────────┬────────────────────────────────────────────┤
│ [3] Breadcrumbs: 🏠 > Users > brain > work  │ [3] Breadcrumbs: 💾 > Volumes > Backup     │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│ [4] Tab Bar: [Project Alpha ✕] [Docs] [+]   │ [4] Tab Bar: [2026 Archive ✕] [+]          │
├──────────────────────────────────────┬──────┼────────────────────────────────────────────┤
│ [5] Left Panel (Active / Source)     │ [6]  │ [5] Right Panel (Inactive / Target)        │
│ 📁 .. [Parent Directory]             │  M   │ 📁 .. [Parent Directory]                   │
│ 📁 assets                            │  I   │ 📁 archive_2025                            │
│ 📁 src                               │  D   │ 📁 release_builds                          │
│ 📄 Cargo.toml             1.2 KB     │  D   │ 📄 CHANGELOG.md                 14.8 KB    │
│ 📄 main.rs                8.4 KB     │  L   │ 📄 README.md                     4.1 KB    │
│ 📄 config.json            2.1 KB     │  E   │ 📦 backup_bundle.zip           128.4 MB    │
│                                      │      │                                            │
├──────────────────────────────────────┴──────┴────────────────────────────────────────────┤
│ [7] Status Bar: 6 items | 2 selected (10.5 KB)   │ Drive: 142.6 GB free / 494.3 GB total │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

### Referencia de puntos de referencia de la interfaz de usuario

1. **Barra de menú e integración nativa de macOS (`[1]`)**: compatibilidad completa con el menú de la aplicación macOS, accesos directos estándar (`⌘,`, `⌘Q`, `⌘W`) y acceso completo al menú para cada comando interno de Commander (`cm_*`). 
2. **Barra de herramientas principal y lanzadores rápidos (`[2]`)**: acceso inmediato con un clic a Búsqueda (`Alt+F7`), Cola de transferencia en segundo plano (`cm_OperationsPanel`), Preferencias (`Cmd+,`) y selectores de unidades. 
3. **Barra de ruta de navegación interactiva (`[3]`)**: haga clic en cualquier segmento del directorio en la ruta para saltar directamente hacia arriba en la jerarquía. Haga clic en la flecha desplegable del segmento para buscar subdirectorios. 
4. **Pestañas de carpetas y espacios de trabajo (`[4]`)**: abra pestañas ilimitadas en cada panel (`Cmd+T`), cierre pestañas (`Cmd+W`), bloquee ubicaciones favoritas y guarde espacios de trabajo completos con pestañas de panel dual (`cm_SaveFavoriteTabs`). 
5. **Paneles de archivos duales (`[5]`)**: Tablas de archivos independientes. El panel activo muestra un borde de acento distintivo y un cursor enfocado. Cambie el enfoque instantáneamente con `Tab`. 
6. **Barra de herramientas intermedia y divisor arrastrable (`[6]`)**: una tira vertical de acción rápida colocada directamente en el divisor del panel. Proporciona activadores con un solo clic para Ver (`F3`), Editar (`F4`), Copiar (`F5`), Mover (`F6`), Nueva carpeta (`F7`), Eliminar (`F8`), Borrar e intercambiar paneles. (`cm_Exchange`). Arrastre el divisor hacia la izquierda o hacia la derecha para cambiar el tamaño de los paneles. 
7. **Barra de estado y medidor de almacenamiento en unidad (`[7]`)**: muestra recuentos de archivos en vivo, estadísticas de elementos seleccionados, tamaños de bytes agregados y un indicador de capacidad de almacenamiento de volumen activo con cálculo de espacio libre. 

---

## Muestra de interfaz

Explore las capacidades de ATBCmder a través de características clave destacadas: 

| Paneles dobles y vista de árbol | Barra de herramientas de acción rápida central | 
| :---: | :---: | 
| ![Tree View and Thumbnail Display](images/treeview+thumbview.png) | ![Middle Toolbar](images/middle_toolbar.png) | 
| *Diseño de panel dual con árbol de directorios y vista previa en miniatura.* | *Banda de acciones rápidas: Ver, Editar, Copiar, Mover, MkDir, Eliminar, Limpiar.* | 

| Comandos de lenguaje natural | Vista de rama plana recursiva | 
| :---: | :---: | 
| ![Natural Language File Search](images/semantic_command.png) | ![Flat View of Nested Directories](images/branch_view.png) | 
| *Búsqueda instantánea impulsada por macOS Spotlight y análisis de consultas semánticas.* | *Vista de sucursal (`Cmd+B`) que muestra contenidos anidados en una única lista plana.* | 

| Red y VFS remoto | Archivo VFS (no se necesita extracción) | 
| :---: | :---: | 
| ![Network VFS](images/network_vfs.png) | ![Archive VFS](images/archive_vfs.png) | 
| *Conéctese a redes compartidas FTP, SFTP, WebDAV y SMB/Samba.* | *Explore y edite dentro de archivos ZIP, TAR y 7z como carpetas estándar.* | 

---

## Elige tu camino

Ya sea que nunca antes haya tocado una herramienta de panel dual o haya pasado dos décadas usando Total Commander, ATBCmder proporciona un camino optimizado a seguir:

### 🟢 Pista A: ¿Nuevo en los administradores de archivos de panel dual?

*Bienvenido a una forma más rápida y limpia de administrar archivos en macOS.* 

Si viene de Finder o de sistemas operativos de escritorio estándar, los administradores de archivos ortodoxos pueden parecerle desconocidos al principio. Una vez que aprenda los patrones principales, no querrá volver a arrastrar archivos por ventanas dispersas: 

1. **Comience con los conceptos básicos**: lea el [Capítulo 1: Fundamentos y configuración de macOS](getting_started.md) para comprender los paneles activos e inactivos, la barra de herramientas intermedia y cómo otorgar permisos de disco a macOS. 
2. **Domine las operaciones diarias**: aprenda a copiar, mover, cambiar el nombre y eliminar sin tocar el mouse en el [Capítulo 3: Cola y operaciones diarias de archivos](file_operations.md). 
3. **Vista previa de todo al instante**: descubra cómo obtener una vista previa de imágenes, escuchar archivos de audio, leer códigos e inspeccionar archivos PDF con una sola pulsación de tecla en el [Capítulo 4: Listadores y editores universales](viewers_and_editors.md). 
4. **Siga las guías prácticas**: consulte los flujos de trabajo prácticos cotidianos y las preguntas comunes en el [Capítulo 9: Recetas y solución de problemas del mundo real](faq_howtos.md). 

---

### ⚡ Pista B: ¿Migrar desde Total Commander / Double Commander?

*Toda la potencia y los reflejos del teclado que conoces, diseñados de forma nativa para macOS.* 

ATBCmder fue creado para llevar la experiencia auténtica de Commander a macOS moderno sin ejecutar X11 torpe, envoltorios de vino o puertos heredados sin mantenimiento: 

1. **Domine las combinaciones de teclas de matriz dual**: revise nuestra matriz completa de atajos de teclado en paralelo (`macOS Cmd` frente a `Commander Fn`) en el [Capítulo 8: Atajos de teclado maestros](keyboard_shortcuts.md). 
2. **Aproveche las herramientas eléctricas avanzadas**: utilice la herramienta de cambio de nombre múltiple por lotes (`Ctrl+M`), la diferenciación de archivos en paralelo (`Meta+Shift+F12`), la sincronización de carpetas (`Shift+F12`) y la búsqueda avanzada en el [Capítulo 5: Herramientas eléctricas y automatización] (power_tools.md). 
3. **Conéctese a sistemas virtuales y remotos**: explore y edite directamente dentro de los archivos `.zip` y `.tar` con reempaquetado en vivo, o administre servidores remotos a través de SFTP, SMB y WebDAV en el [Capítulo 6: Red y sistemas de archivos virtuales] (network_and_vfs.md). 
4. **Personalice y transfiera su configuración**: vuelva a vincular comandos, configure el comportamiento de actualización automática y exporte su configuración XML en el [Capítulo 7: Preferencias y personalización](preferences_and_customization.md). 

---

## Tabla maestra de contenidos

Explore el conjunto completo de documentación de ATBCmder:

### 🚀 [Capítulo 1: Fundamentos y configuración de macOS](getting_started.md)

Comprenda la filosofía del panel dual, explore la anatomía de la interfaz, configure los permisos de la zona de pruebas de la aplicación macOS a través del asistente de incorporación (`cm_GrantFilesystemAccess`), establezca anulaciones de idioma del sistema en más de 30 configuraciones regionales y adapte temas claros/oscuros.

### 🧭 [Capítulo 2: Navegación y pestañas de carpetas](navigation_and_tabs.md)

Muévase sin esfuerzo a través de árboles de directorios usando rutas de navegación interactivas, saltos de teclado (`Ctrl+\`, `Backspace`), organización de múltiples pestañas (`Cmd+T`, `Cmd+W`), conjuntos de espacios de trabajo favoritos de doble panel (`cm_SaveFavoriteTabs`), marcadores de lista activa de directorios (`Ctrl+D`) y modos de vista flexibles (Breve, Columnas completas, Miniaturas, Vista de árbol y Vista de rama plana `Cmd+B`).

### 📁 [Capítulo 3: Cola y operaciones diarias de archivos](file_operations.md)

Realice operaciones de archivos rápidas y sólidas: copiar (`F5`), mover (`F6`), nueva carpeta (`F7`), eliminar a la papelera (`F8`) y cambio rápido de nombre en línea (`F2`). Selecciones de atributos y comodines maestros, interoperabilidad de arrastrar y soltar, resolución de conflictos de colisiones, permisos octales de UNIX (`Alt+Enter`) y monitoreo de transferencias asincrónicas a través de la cola de operaciones en segundo plano (`cm_OperationsPanel`).

### 👁️ [Capítulo 4: Lister universal y editores integrados](viewers_and_editors.md)

Inspeccione archivos sin iniciar software pesado de terceros. Utilice Vista rápida (`Ctrl+Q` / `Cmd+Q`) para obtener vistas previas en vivo del panel lateral y Universal Lister (`F3`) para documentos de Word, hojas de cálculo, bases de datos SQLite, cuadernos Jupyter, EPUB, código resaltado de sintaxis, inspección de bytes hexadecimales sin formato (`2`), imagen. anotaciones y marcas de agua (`F4`), lector de documentos PDF y reproductores multimedia de audio/vídeo integrados con reproducción de audio de fondo. Edite archivos directamente con el editor de texto integrado (`F4`).

### ⚡ [Capítulo 5: Herramientas eléctricas y automatización](power_tools.md)

Automatice desafíos complejos de administración de archivos: cambio de nombre múltiple por lotes (`Ctrl+M`) con tokens y sustitución de expresiones regulares, diferenciación visual de archivos en paralelo (`Meta+Shift+F12`), sincronización de directorios bidireccional (`Shift+F12`), búsqueda avanzada de múltiples filtros (`Alt+F7`) con "Feed to Listbox", Spotlight & comandos semánticos de lenguaje natural (`/`), divisor y vinculador de archivos, verificación de suma de comprobación (MD5, SHA-256, CRC32), borrado seguro de múltiples pasadas (`cm_Wipe`) y terminal integrado (`Ctrl+J`).

### 🌐 [Capítulo 6: Red y sistemas de archivos virtuales](network_and_vfs.md)

Trate los servidores remotos y los archivos comprimidos como carpetas locales normales utilizando URI `vfs://` unificados. Navegue dentro de archivos `.zip`, `.tar` y `.7z` sin descomprimirlos, edite archivos en el lugar con reempaquetado en vivo automatizado, cree archivos cifrados (`Alt+F5`) y administre conexiones persistentes a través de FTP, SFTP (claves SSH), WebDAV y recursos compartidos de red SMB/Samba.

### ⚙️ [Capítulo 7: Preferencias y personalización](preferences_and_customization.md)

Configure ATBCmder para que coincida con su estilo de trabajo exacto. Busque y vincule teclas de acceso rápido primarias/secundarias con advertencias de conflictos en tiempo real, personalice las columnas de la tabla de archivos y las reglas de ajuste automático, ajuste la sensibilidad de actualización automática del observador de archivos, defina asociaciones de extensiones de archivos personalizadas y exporte/importe perfiles de configuración portátiles (`cm_ExportConfiguration`).

### ⌨️ [Capítulo 8: Atajos de teclado maestros](keyboard_shortcuts.md)

Guía de referencia completa de atajos de matriz dual que compara los atajos nativos de macOS (modificadores `Cmd`) con las teclas de función clásicas de Commander (`F1`-`F12`). Incluye instrucciones dedicadas para el comportamiento del modificador `Fn` del teclado Apple y la configuración de las "teclas de función estándar" de macOS.

### ❓ [Capítulo 9: Recetas del mundo real y solución de problemas](faq_howtos.md)

Tutoriales prácticos paso a paso para tareas comunes del mundo real: sincronización de copias de seguridad de directorios, cambio de nombre por lotes de bibliotecas de fotografías de cámaras con marcas de tiempo, montaje de unidades NAS de red, actualización de archivos de configuración dentro de archivos remotos y diagnóstico de errores de permisos de entorno aislado de macOS o problemas de actualización automática.

### 📥 [Capítulo 10: Descarga e instalación](download.md)

Opciones de instalación para macOS 12.0+ Monterey a través de Sequoia. Descárguelo directamente desde Mac App Store o obtenga paquetes de instalación de DMG independientes creados de forma nativa para Apple Silicon (arquitectura M1/M2/M3/M4, ARM64). *Nota: Las Mac Intel (x86_64) no son compatibles actualmente.* 

---

### 🔒 [Apéndice: Política de privacidad y seguridad de datos](privacy_policy.md)

Nuestro compromiso fundamental con la privacidad del usuario: ATBCmder incluye cero seguimiento, cero registros telemétricos y cero análisis en segundo plano. Todas las operaciones con archivos, credenciales de red e índices de búsqueda permanecen estrictamente locales en su Mac. 

--- 

<div align="center"> 
<p>¿Listo para comenzar?</p> 
<p><strong><a href="getting_started.md">Continúe con el Capítulo 1: Fundamentos y configuración de macOS →ATB_HTML_00006__</strong></p> 
</div>