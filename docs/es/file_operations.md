# Capítulo 3: Operaciones de archivos y cola en segundo plano

Todos los días, los administradores de archivos son juzgados por una métrica: la rapidez, precisión y seguridad con la que se pueden manipular los datos. En ATBCmder, nunca tendrá que hacer malabares con múltiples ventanas superpuestas, soportar errores de caída accidental o esperar sin hacer nada mientras las transferencias de archivos grandes congelan su pantalla. 

Este capítulo cubre el espectro completo de operaciones de archivos: flujos de trabajo de copia y movimiento direccionales, cambio de nombre en línea en el lugar, marcado de energía con comodines, interoperabilidad del sistema de arrastrar y soltar, manejo granular de colisiones, permisos y enlaces simbólicos de UNIX y la cola de operaciones en segundo plano de subprocesos múltiples. 

---

## 1. Inicio rápido visual: el modelo de operación direccional

Los administradores de archivos ortodoxos utilizan un modelo direccional **Fuente ➔ Destino**. Cuando inicia una transferencia de archivos o la creación de un enlace, ATBCmder toma los elementos seleccionados en el **Panel activo** (Fuente) y ejecuta la operación directamente en el directorio abierto en el **Panel inactivo** (Destino). 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PANEL ACTIVO (Origen)                              PANEL INACTIVO (Destino)           │
│  /Users/brain/Downloads                             /Volumes/ExternalSSD/Projects      │
├──────────────────────────────────────────────┬───┬─────────────────────────────────────┤
│  Nombre                       Tamaño Fecha   │   │  Nombre                       Tamaño│
│  ▸ [..]                              --:--   │ C │  ▸ [..]                             │
│  ✔ database_dump.sql        1.8 GB   14:10   │ O │  ▸ client_portal                    │
│  ✔ schema_migration.sql      42 KB   14:12   │ P │  ▸ microservices                    │
│  ● notes.txt                  4 KB   09:30   │ ➔ │  ● .env.production                  │
│                                              │   │                                     │
│  [2 archivos seleccionados: 1.8 GB]          │   │  [Carpeta destino lista para recibir]│
├──────────────────────────────────────────────┴───┴─────────────────────────────────────┤
│  [F5] Copiar   [F6] Mover   [Shift+F5] Duplicar   [F8 / ⌘⌫] Mover a la papelera        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Hoja de referencia de operaciones centrales de matriz dual

| Acción | Acceso directo a macOS | Llave de comandante clásica | ID de comando | Descripción | 
| :--- | :--- | :--- | :--- | :--- | 
| **Copiar al destino** | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Copia los elementos seleccionados al panel opuesto. | 
| **Copiar en el mismo panel** | `Shift+F5` / `⇧F5` | `Shift+F5` | `cm_CopySamePanel` | Duplica elementos en el panel activo con mensaje de cambio de nombre. | 
| **Mover al destino** | `F6` / `Fn+F6` | `F6` | `cm_Move` | Mueve los elementos seleccionados al panel opuesto. | 
| **Nueva carpeta (MkDir)** | `F7` / `Fn+F7` | `F7` | `cm_MkDir` | Crea un nuevo directorio en el panel activo. | 
| **Eliminar a la Papelera** | `F8` / `⌘⌫` | `F8` / `Delete` | `cm_Delete` | Mueve los elementos seleccionados a la Papelera de macOS. | 
| **Eliminación permanente** | `Shift+Delete` / `⇧⌦` | `Shift+F8` | `cm_Delete` | Omite la Papelera y desvincula archivos permanentemente. | 
| **Cambio de nombre rápido en línea**| `F2` / `Shift+F6` | `Shift+F6` | `cm_RenameOnly` | Cambia el nombre del elemento activo directamente dentro de la fila de la tabla. | 
| **Propiedades del archivo** | `Alt+Enter` / `⌥⏎` | `Alt+Enter` | `cm_SetFileProperties` | Abre el cuadro de diálogo de permisos, marcas de tiempo y metadatos de UNIX. | 
| **Calcular espacio en carpeta**| `Alt+Shift+Enter` / `⌥⇧⏎` | `Alt+Shift+Enter` | `cm_CountDirContent` | Calcula bytes recursivos para directorios (`Ctrl+L` / `cm_CalculateSpace` para el total seleccionado). | 
| **Cola en segundo plano** | `Toolbar ⚡` | — | `cm_OperationsPanel` | Abre el monitor de transferencia en segundo plano de 3 colas. |

### Punto de referencia visual: la barra de herramientas del medio

ATBCmder cuenta con una barra de herramientas vertical dedicada de acción rápida integrada directamente en el divisor central que separa los dos paneles: 

![Middle Toolbar](images/middle_toolbar.png) 
*La barra de herramientas central proporciona acceso instantáneo con el mouse a Ver (F3), Editar (F4), Copiar (F5), Mover (F6), Nueva carpeta (F7), Eliminar (F8) e Intercambiar panel.* 

---

## 2. Operaciones principales: copiar, mover, MkDir y eliminar

La gestión diaria de archivos gira en torno a cuatro acciones principales: copiar, mover, crear directorios y eliminar archivos no deseados.

### 2.1 Copiar archivos (`F5` / `cm_Copy`)

Para copiar archivos o directorios: 

1. **Seleccione** uno o más elementos en el panel activo usando el teclado o el mouse. 
2. **Presione `F5`** (o `Fn+F5` en teclados Apple, o haga clic en **Copiar** en la barra de herramientas central). 
3. Aparece el **Copiar cuadro de diálogo**: 
- **Línea de destino**: se completa automáticamente con la ruta del directorio actual del panel opuesto. Puede editar esta ruta manualmente, agregar un nuevo nombre de subcarpeta para copiar y crear simultáneamente o hacer clic en `...` para explorar. 
- **Iniciar (`Enter`)**: comienza la copia inmediata en primer plano con un cuadro de diálogo de progreso en tiempo real. 
- **Agregar a la cola (`F2`)**: pone en cola la transferencia para que se ejecute en segundo plano (consulte la [Sección 7.4](#74-cola-de-operaciones-en-segundo-plano-cm_operationspanel)). 
- **Opciones**: amplía las reglas avanzadas de conflicto, la preservación de atributos y las verificaciones de suma de verificación. 

```
┌────────────────────────────────────────────────────────┐
│ Copy file(s)                                           │
│ Copy selected 3 files?                                 │
│ To: [/Volumes/Backup/Assets                          ] │
│ [Options ▼]   [Add To Queue #1 ▾]   [Cancel]   [Start] │
└────────────────────────────────────────────────────────┘
```

#### Duplicación en el panel (`Shift+F5` / `cm_CopySamePanel`)

Para clonar rápidamente un archivo dentro del directorio actual (por ejemplo, crear una copia de seguridad antes de editar `nginx.conf`): 

- Resalte el elemento y presione `Shift+F5` (o `⇧F5`). 
- ATBCmder solicita una ruta de destino en el *mismo* directorio, lo que le permite ingresar un nuevo nombre (por ejemplo, `nginx.conf.bak`).

#### Portapapeles estándar de macOS (`Cmd+C` ➔ `Cmd+V`)

ATBCmder se integra completamente con los atajos del portapapeles del sistema macOS: 

- **`Cmd+C` (`⌘C`)**: Copia las rutas de archivos seleccionadas al portapapeles (`cm_CopyToClipboard`). 
- **`Cmd+V` (`⌘V`)**: Pega archivos del portapapeles en el panel activo (`cm_PasteFromClipboard`). 
- **`Cmd+Option+V` (`⌥⌘V`)**: Mueve los archivos del portapapeles al panel activo (`cm_PasteAsMove`). 

---

### 2.2 Mover archivos (`F6` / `cm_Move`)

Mover transfiere archivos desde el directorio de origen al directorio de destino: 

1. Seleccione elementos y presione **`F6`** (o `Fn+F6` / haga clic en **Mover** en la barra de herramientas central). 
2. Se abre el **Diálogo Mover**, que muestra la ruta del panel de destino. 
3. Presione **`Enter`** para ejecutar: 
- **Mover el mismo sistema de archivos**: instantáneo y atómico en volúmenes APFS/HFS+ mediante la actualización de las referencias del catálogo del sistema de archivos sin mover bloques de disco sin formato. 
- **Mover entre sistemas de archivos**: transmite datos a través de volúmenes hasta el destino, verifica la finalización de bytes y elimina de forma segura el origen al llegar verificado. 
4. Si un archivo existente con el mismo nombre reside en el destino, ATBCmder hace una pausa y convoca el **Diálogo de sobrescritura** (consulte la [Sección 6](#6-manejo-de-colisiones-y-resolucion-de-conflictos)). 

---

### 2.3 Creación de nuevos directorios (`F7` / `cm_MkDir`)

¿Necesita crear una estructura de carpetas sobre la marcha? 

1. Presione **`F7`** (o `Fn+F7` / `Shift+Cmd+N` / `cm_MkDir`). 
2. Aparece un mensaje ligero: `Enter folder name:`. 
3. Escriba el nombre de la carpeta y presione `Enter`. 

```
┌──────────────────────────────────────────────┐
│ Create Directory                             │
│ Enter folder name:                           │
│ [2026-09-Q3_Reports                        ] │
│                      [Cancel]      [OK (⏎)]  │
└──────────────────────────────────────────────┘
```

#### Encadenamiento de subdirectorios

Puede crear jerarquías de carpetas anidadas en un solo paso. Al escribir `deep/nested/project/assets` se crean los cuatro niveles de jerarquía al instante (equivalente a `mkdir -p`).

#### Ubicación del enfoque automático

Tras la creación, ATBCmder coloca automáticamente el cursor del panel directamente en la nueva carpeta, lista para la entrada inmediata (`Enter`) o la transferencia de archivos. 

---

### 2.4 Eliminación de archivos: Papelera de macOS frente a purga permanente

La seguridad y la recuperabilidad son primordiales. ATBCmder admite flujos de trabajo de eliminación dual: 

```
                  ┌────────────────────────────────────────┐
                  │          File Deletion Trigger         │
                  └───────────────────┬────────────────────┘
                                      │
                 ┌────────────────────┴───────────────────┐
                 ▼                                        ▼
    [ F8 / Delete / Cmd+Backspace ]             [ Shift+Delete / Shift+F8 ]
                 │                                        │
                 ▼                                        ▼
    macOS System Trash (.Trash)                  Permanent Unlink
      • Fully recoverable                         • Bypasses Trash
      • Put Back support in Finder                • Zero disk footprint
      • Volume .Trashes directory                 • Unrecoverable without deep carve
```

#### Eliminación a la Papelera de macOS (`F8` / `Delete` / `Cmd+Backspace`)

- Los archivos seleccionados se enrutan a través de las API `send2trash` de macOS a la Papelera de su sistema. 
- Los archivos se pueden inspeccionar o restaurar en cualquier momento a través de macOS Finder ("Devolver"). 
- Los cuadros de diálogo de confirmación se pueden habilitar o suprimir en **Preferencias** (`operations.confirm_delete`).

#### Eliminación inmediata permanente (`Shift+Delete` / `Shift+F8`)

- Omite la Papelera por completo, desvinculando archivos inmediatamente y liberando espacio de almacenamiento. 
- Ideal para borrar máquinas virtuales de varios gigabytes o imágenes de disco donde los límites del búfer de la Papelera o el agotamiento del disco impedirían la preparación.

#### Volúmenes sin soporte de papelera (detección `trash_unavailable`)

Al eliminar de ciertos recursos compartidos de red (SMB, NFS), sistemas de archivos virtuales (`vfs://`) o unidades externas formateadas con sistemas de archivos FAT/exFAT heredados que carecen de un directorio `.Papeleraes`, macOS no puede enviar elementos a la Papelera. 

En tales casos, ATBCmder activa una alerta de seguridad inteligente: 
```
┌────────────────────────────────────────────────────────┐
│ Trash Unavailable                                      │
│ The volume containing '/Volumes/NAS/backup.iso' does   │
│ not support Trash.                                     │
│ Would you like to permanently delete this file?        │
│                                                        │
│ [✔] Apply to all remaining items                       │
│              [Skip]               [Delete Permanently] │
└────────────────────────────────────────────────────────┘
```
 
Puede elegir **Eliminar permanentemente**, **Omitir** o marcar **Aplicar a todos los elementos restantes** para manejar eliminaciones por lotes grandes sin supervisión.

#### Trituración segura de varias pasadas (`Alt+Delete` / `cm_Wipe`)

Para documentos confidenciales, credenciales o claves privadas que no deben permanecer recuperables mediante herramientas de recuperación flash sin formato: 

- Resalte el elemento y seleccione **Menú Archivo** → **Limpiar** (`Alt+Delete` / `cm_Wipe`). 
- ATBCmder realiza una sobrescritura de múltiples pasadas con patrones de bits aleatorios y ceros antes de desvincular el inodo. 

---

## 3. Cambio rápido de nombre y edición de nombre en línea

Cambiar el nombre de un solo archivo no debería requerir menús complejos ni cuadros de diálogo emergentes. ATBCmder proporciona una edición rápida de filas de tablas en el lugar. 

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Name                                  Ext      Size      Date Modified         │
│  ▸ [..]                                         --:--     drwxr-xr-x            │
│  ● Annual_Financial_Report_2025        .pdf     4.2 MB    Today, 11:20          │
│    ▲                                                                            │
│    └── [Editable Text Box: Stem highlighted, .pdf extension preserved]          │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Activar el cambio de nombre en línea

1. Resalte cualquier archivo o directorio en el panel. 
2. Presione **`F2`** o **`Shift+F6`** (`cm_RenameOnly`), o haga clic una vez en el nombre de archivo ya resaltado. 
3. La celda de la tabla se transforma en un editor en línea (`QLineEdit`).

### Preservación de extensión inteligente

Al cambiar el nombre de un archivo como `invoice_september.pdf`: 

- ATBCmder preselecciona automáticamente solo el nombre de archivo base (`invoice_september`). 
- La extensión del archivo (`.pdf`) permanece intacta y sin seleccionar, lo que evita la eliminación accidental de la extensión que rompería las asociaciones de archivos de macOS. 
- Si desea modificar la extensión, simplemente use las teclas de flecha o presione `Cmd+A` dentro del cuadro de edición.

### Atajos de teclado dentro del cambio de nombre en línea

- **`Enter` (`Return`)**: Confirma el nuevo nombre y vuelve a indexar el panel. 
- **`Esc`**: Cancela la edición y restaura el nombre original sin cambios. 
- **`Tab`**: confirma el nombre actual e inmediatamente comienza a cambiar el nombre del archivo *siguiente* en la lista, lo que permite un cambio de nombre secuencial rápido sin salir del teclado. 

---

## 4. Técnicas de selección: limas de marcado energético

En los administradores de archivos tradicionales, la posición del cursor y su selección están estrechamente relacionadas: al mover el cursor se anula la selección de los archivos anteriores a menos que mantenga presionado `Cmd`. En ATBCmder, el **enfoque del cursor** y las **selecciones marcadas** están desacoplados, lo que permite una preparación por lotes precisa. 

```
  Status Column:
  [ ]  Unselected (cursor may or may not be on row)
  [✔]  Marked / Selected (accumulated into operation payload)
```

### 4.1 Acciones de Selección Global

| Acción | Acceso directo a macOS | Clave clásica | ID de comando | Descripción | 
| :--- | :--- | :--- | :--- | :--- | 
| **Seleccionar todo** | `Cmd+A` / `⌘A` | `Ctrl+A` / `Ctrl+Num+` | `cm_MarkMarkAll` | Marca cada archivo y carpeta en el panel activo. | 
| **Deseleccionar todo** | `Cmd+Shift+A` / `⇧⌘A`| `Ctrl+Shift+A` / `Ctrl+L` | `cm_MarkUnmarkAll` | Borra todas las marcas en el panel activo. | 
| **Invertir selección**| `Num*` / `⌥⌘I` | `Num*` | `cm_MarkInvert` | Estado de selección de volteos: marcado se desmarca y viceversa. | 

---

### 4.2 Selección de patrones y comodines

La selección de comodines le permite seleccionar cientos de archivos específicos en un directorio de miles con unas pocas teclas. 

```
┌────────────────────────────────────────────────────────┐
│ Mark Files by Pattern                                  │
│ Pattern: [*.jpg;*.png;*.webp                        ]  │
│                                                        │
│ [✔] Case sensitive       [ ] Regular expression        │
│                      [Cancel]                 [OK (⏎)] │
└────────────────────────────────────────────────────────┘
```

#### Grupo de marcas (`Num+` / `cm_MarkPlus`)

- Presione **`Num+`** (Keypad Plus, o active desde Menú **Marcar** → **Seleccionar grupo**). 
- Introduzca comodines de shell estándar: 
- `*.log`: Marca todos los archivos que terminan en `.log`. 
- `*.jpg;*.png;*.webp`: lista separada por punto y coma para hacer coincidir varias extensiones a la vez. 
- `data_2026_??.csv`: Coincide con archivos mensuales de dos dígitos (`01` a `12`). 
- `*draft*`: Coincide con cualquier archivo que contenga la palabra "borrador". 
- Presione `Enter` para seleccionar todas las entradas coincidentes al instante.

#### Desmarcar grupo (`Num-` / `cm_MarkMinus`)

- Presione **`Num-`** (Teclado menos). 
- Ingrese un patrón para eliminar elementos coincidentes de una selección existente (por ejemplo, `*test*`).

#### Marcar todo con la misma extensión (`Shift+Num+` / `cm_MarkCurrentExtension`)

- Coloque el cursor en cualquier archivo (por ejemplo, `app.tsx`). 
- Presione **`Shift+Num+`**. 
- Cada archivo `.tsx` en el directorio actual se selecciona instantáneamente. 

---

### 4.3 Selección de rango y punto

- **Selección de bloque continuo (`Shift+Up` / `Shift+Down`)**: Mantener presionado `Shift` mientras navega con las teclas de flecha expande un bloque de selección contiguo hacia arriba o hacia abajo. 
- **Alternancia de elemento único (`Space` / `Insert` / `cm_SelectOrDeselectFile`)**: 
- Al presionar `Space` se marca o desmarca el elemento debajo del cursor e inmediatamente se calcula el tamaño del directorio si se encuentra en una carpeta. 
- Al presionar `Insert` (o `Fn+Return` en ciertos teclados Mac) se marca el elemento y automáticamente el cursor baja a la siguiente fila, lo que permite realizar pases rápidos de selección con un solo dedo. 
- **Ratón y panel táctil**: 
- `Cmd+Click`: alterna la selección en filas individuales sin alterar otras selecciones. 
- `Shift+Click`: extiende la selección desde la fila de anclaje actual a la fila en la que se hizo clic.

### Telemetría de selección en vivo en la barra de estado

Cada vez que se marcan archivos, la barra de estado inferior se actualiza inmediatamente: 
```
[ 48 items | 12 selected (284.6 MB) ]   [ Volume Free: 184.2 GB / 494.3 GB ]
```
 
Obtiene conocimiento de la situación en tiempo real de las cargas útiles de bytes exactos antes de realizar copias o eliminaciones grandes. 

---

## 5. Interoperabilidad de arrastrar y soltar

ATBCmder trata la función de arrastrar y soltar como un ciudadano de primera clase y, al mismo tiempo, mantiene una compatibilidad total con los flujos de trabajo ortodoxos y el ecosistema de escritorio macOS. 

```
       Dual-Panel Transfer                       External macOS Desktop
 ┌──────────────┐   ┌──────────────┐       ┌──────────────┐   ┌──────────────┐
 │ Left Panel   │══►│ Right Panel  │       │ ATBCmder     │══►│ Finder / App │
 │ (Source)     │   │ (Target)     │       │ Panel        │   │ (Desktop)    │
 └──────────────┘   └──────────────┘       └──────────────┘   └──────────────┘
```

### Arrastrando entre paneles

- Haga clic y arrastre los elementos marcados desde el panel activo a través del divisor central hasta el panel inactivo. 
- Suéltelo en cualquier lugar de la tabla de archivos para iniciar la transferencia a la carpeta de destino. 
- **Caer en una subcarpeta**: si coloca directamente en una fila de subdirectorio específica, ATBCmder enruta la carga útil a esa subcarpeta en lugar de a la raíz del panel.

### Interactuar con macOS Finder, escritorio y aplicaciones externas

- **Arrastrar a ATBCmder**: arrastre archivos desde Finder, su escritorio o descargas de AirDrop directamente a cualquiera de los paneles de ATBCmder para copiarlos o moverlos. 
- **Arrastrar fuera de ATBCmder**: arrastre archivos fuera de ATBCmder directamente a VS Code, Terminal (que pega la ruta del archivo), Slack, Apple Mail o cuadros de carga del navegador web.

### Teclas modificadoras durante el arrastre

| Tecla modificadora | Acción de arrastre | Icono del cursor del ratón | Descripción | 
| :--- | :--- | :--- | :--- | 
| **Sin modificador** | Acción predeterminada | Flecha estándar | Copias entre volúmenes; se mueve dentro del mismo volumen. | 
| **Opción (`⌥`)** | **Forzar copia** | Insignia verde `+` | Siempre copia elementos, dejando intactos los archivos fuente. | 
| **Comando (`⌘`)** | **Forzar movimiento** | Insignia de flecha curva | Siempre mueve elementos y desvincula los archivos fuente al llegar. |

### Carpetas con resorte

Al arrastrar archivos sobre un directorio anidado en ATBCmder: 

- Pase el cursor del mouse sobre la carpeta de destino durante **750 milisegundos**. 
- La carpeta parpadea automáticamente y se abre, navegando hacia el interior. 
- Puede navegar por múltiples niveles en subdirectorios anidados sin soltar el botón del mouse y luego colocar su carga útil exactamente donde desee. 

---

## 6. Manejo de colisiones y resolución de conflictos

Las colisiones de nombres son el momento más peligroso en la gestión de archivos. Sobrescribir el archivo incorrecto puede destruir horas de trabajo. ATBCmder implementa un motor de resolución de conflictos de nivel empresarial que inspecciona archivos antes de sobrescribirlos y proporciona controles de seguridad granulares. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Confirm File Overwrite                                                                 │
│                                                                                        │
│ File already exists at the destination.                                                │
│                                                                                        │
│ Source:      /Users/brain/Downloads/build_artifacts.zip                                │
│ Source info: 124,518,400 bytes, 2026-09-06 14:15                                       │
│                                                                                        │
│ Destination: /Volumes/Backup/build_artifacts.zip                                       │
│ Dest info:   118,204,112 bytes, 2026-09-01 09:30                                       │
│                                                                                        │
│ Would you like to overwrite it?                                                        │
│                                                                                        │
│ [Skip All]   [Overwrite All]   [Rename]   [Auto-rename]                                │
│                                                                                        │
│ [Cancel]                                        [Skip]               [Overwrite (⏎)]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Desglose del cuadro de diálogo Sobrescribir

Cuando se produce una colisión de objetivo, ATBCmder muestra el cuadro de diálogo **Confirmar sobrescritura de archivo**: 

1. **Inspección de metadatos en paralelo**: 
- Compara tamaños de archivos exactos hasta un solo byte. 
- Compara fechas de modificación y marcas de tiempo. Destaca notablemente si el archivo fuente es más nuevo, más antiguo o de tamaño idéntico. 
2. **Botones de decisión de elementos actuales**: 
- **Sobrescribir (`Enter`)**: reemplaza el archivo de destino en conflicto con el archivo de origen. 
- **Omitir**: deja intacto el archivo de destino existente y continúa con el siguiente elemento del lote de transferencia. 
- **Cancelar (`Esc`)**: Anula la operación restante inmediatamente, conservando los archivos que ya se hayan transferido. 
3. **Acciones de seguridad y lotes**: 
- **Sobrescribir todo**: sobrescribe silenciosamente todos los archivos conflictivos posteriores en este trabajo de transferencia. 
- **Omitir todo**: omite silenciosamente todos los archivos conflictivos restantes sin volver a preguntar. 
- **Cambiar nombre**: le solicita que ingrese un nuevo nombre personalizado para el archivo copiado antes de escribirlo. 
- **Renombrar automáticamente**: agrega automáticamente un contador incremental (por ejemplo, `build_artifacts_1.zip`, `build_artifacts_2.zip`), asegurando que ambas versiones se conserven una al lado de la otra sin intervención manual. 

---

### Políticas de colisión preconfiguradas en el cuadro de diálogo Copiar

Para grandes trabajos por lotes automatizados o copias de seguridad desatendidas, puede preconfigurar el comportamiento de conflicto por adelantado dentro del panel expandible **Opciones** del cuadro de diálogo Copiar/Mover: 

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Copy Options Panel                                                           │
│ ┌─ Conflict Resolution ─────────────────┐ ┌─ Attributes & Behaviors ──────┐  │
│ │ When file exists:      [Ask          ▾]│ │ [✔] Check free space          │ │
│ │ When directory exists: [Merge        ▾]│ │ [✔] Copy date/time            │ │
│ │ When cannot set attr:  [Skip         ▾]│ │ [✔] Copy attributes           │ │
│ └───────────────────────────────────────┘ │ [ ] Drop readonly flag        │  │
│ ┌─ Filters ─────────────────────────────┐ │ [✔] Copy ownership (POSIX)     │ │
│ │ [ ] Exclude empty directories         │ │ [✔] Verify after copy: [SHA256]│ │
│ └───────────────────────────────────────┘ └───────────────────────────────┘  │
│ [Save these options as default]                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```
 

- **Cuando el archivo existe**: 
- `Ask`: solicita el cuadro de diálogo Sobrescribir en cada colisión (predeterminado). 
- `Overwrite`: sobrescribe archivos existentes automáticamente. 
- `Skip`: omite archivos conflictivos automáticamente. 
- `Overwrite older`: sobrescribe el destino solo si la hora de modificación del origen es más reciente. 
- `Rename copied`: agrega el sufijo del contador (`_1`, `_2`) a los archivos copiados. 
- `Auto-rename target`: cambia el nombre del archivo de destino existente y escribe el nuevo archivo con el nombre original. 
- **Cuando el directorio existe**: 
- `Merge`: Une contenidos de carpetas de forma recursiva. Los subarchivos que no entran en conflicto se copian en carpetas existentes. 
- `Ask` / `Overwrite` / `Skip`. 
- **Verificación avanzada y atributos**: 
- **Verificar espacio libre / Reservar espacio**: calcula previamente los bytes de origen y garantiza que el volumen de destino tenga la capacidad adecuada antes de comenzar. 
- **Verificar después de la copia**: calcula sumas de verificación criptográficas (`SHA-256`, `MD5`, `SHA-1`, `CRC32`) en los archivos de origen y de destino escritos para garantizar el 100 % de la integridad de los datos contra la corrupción del almacenamiento silencioso. 
- **Seguir enlaces**: controla si los enlaces simbólicos se copian como referencias de puntero o se eliminan las referencias en copias físicas completas. 
- **Copiar fecha/hora y propiedad**: conserva las fechas de creación de POSIX, las marcas de tiempo de modificación y los ID de propiedad de usuarios/grupos. 

---

## 7. ⚡ Consejos profesionales y análisis profundo: potencia avanzada del sistema de archivos

Dominar la administración de panel dual significa comprender el sustrato UNIX subyacente de macOS. A continuación se presentan potentes funciones diseñadas para desarrolladores, administradores de sistemas y profesionales del almacenamiento.

### 7.1 Enlaces simbólicos y enlaces físicos (`cm_SymLink`, `cm_HardLink`)

macOS se basa en Darwin UNIX y proporciona dos tipos de enlaces distintos: 

```
  Symbolic Link (Symlink):
  [ Symlink File ] ──(Path Pointer)──► [ Target File / Directory ]
  • Can cross volume boundaries
  • Can point to directories
  • Breaks if target is moved

  Hard Link:
  [ Hard Link Entry ] ──┐
                        ├──(Direct Inode Reference)──► [ Raw Disk Blocks ]
  [ Original Entry  ] ──┘
  • Cannot cross filesystem boundaries (same APFS container)
  • Files only (no directory hard links on macOS)
  • Data persists until all hard links are deleted
```

#### Creación de enlaces simbólicos (`cm_SymLink`)

1. Resalte uno o más archivos/carpetas en el panel activo. 
2. Seleccione **Archivo de menú** → **Crear enlace simbólico...** (`cm_SymLink`). 
3. ATBCmder genera automáticamente un enlace simbólico en el panel opuesto que apunta a la ruta absoluta del elemento de origen. 
4. Los enlaces simbólicos muestran un indicador de atributo `l` distinto (por ejemplo, `lrwxr-xr-x`) en el panel.

#### Creación de vínculos físicos (`cm_HardLink`)

1. Resalte los archivos en un volumen APFS/HFS+ local. 
2. Seleccione **Archivo de menú** → **Crear vínculo físico...** (`cm_HardLink`). 
3. ATBCmder crea una entrada de directorio adicional en el panel de destino que comparte exactamente el mismo inodo. 
4. Los cambios escritos en cualquiera de los archivos se reflejan instantáneamente en ambos. Eliminar un archivo no elimina datos hasta que el recuento de enlaces llegue a cero. 

> [!NOTE] 
> **Restricciones de límites de enlaces**: los enlaces físicos no pueden cruzar los límites de los volúmenes ni crearse en recursos compartidos de red (`vfs://`). Los enlaces simbólicos se deben utilizar siempre que se establezcan enlaces entre diferentes unidades o puntos de montaje remotos. 

---

### 7.2 Permisos y atributos de archivos (`Alt+Enter` / `cm_SetFileProperties`)

Inspeccione y modifique los atributos del archivo POSIX utilizando el completo **Diálogo de propiedades**: 

```
┌────────────────────────────────────────────────────────┐
│ Properties - production_api.py                         │
│ ┌─ Metadata ─────────────────────────────────────────┐ │
│ │ Full Path:     /Users/brain/work/production_api.py │ │
│ │ Size:          84,210 bytes                        │ │
│ │ Created:       2026-03-12 10:14:22                 │ │
│ │ Last Modified: 2026-09-06 13:45:01                 │ │
│ │ Last Accessed: 2026-09-06 15:30:10                 │ │
│ └────────────────────────────────────────────────────┘ │
│ ┌─ Permissions (UNIX) ───────────────────────────────┐ │
│ │ Octal Mode: [ 755 ]                                │ │
│ │ ┌─ Owner ──┐   ┌─ Group ──┐   ┌─ Others ─┐         │ │
│ │ │ [✔] Read │   │ [✔] Read │   │ [✔] Read │         │ │
│ │ │ [✔] Write│   │ [ ] Write│   │ [ ] Write│         │ │
│ │ │ [✔] Exec │   │ [✔] Exec │   │ [✔] Exec │         │ │
│ │ └──────────┘   └──────────┘   └──────────┘         │ │
│ └────────────────────────────────────────────────────┘ │
│                             [Cancel]         [OK (⏎)]  │
└────────────────────────────────────────────────────────┘
```
 

1. **Activador**: resalte cualquier archivo o directorio y presione **`Alt+Enter`** (`⌥⏎` / `cm_SetFileProperties`). 
2. **Revisión de metadatos**: vea la ruta completa del archivo, los bytes exactos, la hora de creación (`btime`), la hora de modificación (`mtime`) y la hora del último acceso (`atime`). 
3. **Matriz de permisos UNIX**: 
- **Casillas de verificación interactivas**: alterna los permisos de lectura (`r`), escritura (`w`) y ejecución (`x`) de forma independiente para **Propietario**, **Grupo** y **Otros**. 
- **Entrada octal bidireccional**: escriba números octales directamente en el campo **Modo octal** (por ejemplo, `755` para ejecutables, `644` para documentos estándar, `600` para claves SSH privadas). Las casillas de verificación se actualizan en tiempo real y viceversa. 
4. Presione `OK` (`Enter`) para aplicar los cambios a través de POSIX `chmod`. 

---

### 7.3 Cálculo del espacio ocupado (`cm_CountDirContent` / `cm_CalculateSpace` / `Space`)

De forma predeterminada, los administradores de archivos muestran tamaños de directorio como `<DIR>` o `--` porque calcular tamaños de carpetas recursivas en millones de archivos degradaría el rendimiento del sistema de archivos. ATBCmder le ofrece cálculos instantáneos bajo demanda: 

- **Tamaño de carpeta única (`Space` / `Insert` / `cm_SelectOrDeselectFile`)**: Presione `Space` mientras descansa sobre cualquier carpeta. ATBCmder calcula el total de bytes recursivos de la carpeta en segundo plano y reemplaza `<DIR>` con el tamaño exacto (por ejemplo, `14.2 GB`). 
- **Todas las carpetas del Panel Activo (`Alt+Shift+Enter` / `⌥⇧⏎` / `cm_CountDirContent`)**: 
- Escanea todos los directorios visibles en el panel actual. 
- Actualiza las filas de la tabla con totales de bytes precisos. 
- **Tamaño de directorio seleccionado acumulado (`Ctrl+L` / `⌃L` / `cm_CalculateSpace`)**: 
- Acumula el total de bytes recursivos para las carpetas seleccionadas y resume el recuento de archivos, el recuento de carpetas y el tamaño de almacenamiento en la barra de estado. 

---

### 7.4 Cola de operaciones en segundo plano (`cm_OperationsPanel`)

Copiar grandes grabaciones de vídeo de 50 GB o transferir cientos de miles de pequeños archivos de código fuente nunca debería congelar su administrador de archivos. ATBCmder incorpora un **Motor de transferencia asíncrono de 3 colas**. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Background Operations                                                                  │
│ ┌─ [Queue #1 (Active)] ───────────┬─ [Queue #2 (Idle)] ───┬─ [Queue #3 (Idle)] ──────┐ │
│ │                                                                                    │ │
│ │ [RUNNING] Copy: 14 items -> /Volumes/BackupDrive/Media                             │ │
│ │   Current: RED_4K_Clip_0042.r3d (2.4 GB / 8.6 GB)                                  │ │
│ │   Speed: 428.5 MB/s | ETA: 00:01:14                                                │ │
│ │   [████████████████████████████████░░░░░░░░░░░░░░░░░░] 64%                         │ │
│ │                                                                                    │ │
│ │ [QUEUED] Move: 4 items -> /Volumes/BackupDrive/RAW_Audio                           │ │
│ │ [COMPLETED] Copy: 28 items -> /Users/brain/Projects/Website                        │ │
│ │                                                                                    │ │
│ └────────────────────────────────────────────────────────────────────────────────────┘ │
│                                         [Cancel Task]   [Clear Completed]   [Close]    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### ¿Por qué tres colas independientes?

- **Serializado dentro de cada cola**: las tareas dentro de la **Cola n.º 1** se ejecutan una tras otra en estricto orden FIFO. Esto evita que el cabezal del disco se golpee en los discos duros mecánicos y evita cuellos de botella por contención. 
- **Paralelo entre colas**: **Cola n.° 1**, **Cola n.° 2** y **Cola n.° 3** funcionan simultáneamente en subprocesos en segundo plano separados (`QThread`). Puede asignar transferencias dirigidas a **NVMe SSD A** a la cola n.° 1, transferencias dirigidas a **Unidad USB externa B** a la cola n.° 2 y cargas de NAS de red a la cola n.° 3, logrando el máximo rendimiento de bus agregado.

#### Envío de trabajos a la cola

1. En el panel activo, seleccione sus archivos y presione `F5` (Copiar) o `F6` (Mover). 
2. En lugar de hacer clic en Inicio, haga clic en **Agregar a la cola n.° 1** (o haga clic en el galón desplegable para seleccionar **Cola n.° 2** o **Cola n.° 3**). 
3. El cuadro de diálogo se cierra inmediatamente, liberando la ventana principal para continuar navegando.

#### Administrar la ventana de cola (`cm_OperationsPanel`)

- Haga clic en el botón **⚡ Cola** en la barra de herramientas principal, o seleccione **Comandos de menú** → **Operaciones en segundo plano** (`cm_OperationsPanel`). 
- **Telemetría en tiempo real**: inspecciona las tareas activas, los archivos en transferencia actuales, las velocidades de transferencia de streaming (por ejemplo, `428.5 MB/s`) y las cuentas regresivas de ETA calculadas. 
- **Estados codificados por colores**: 
- `[QUEUED]`: Esperando en la fila. 
- `[RUNNING]`: Transfiriendo datos activamente. 
- `[COMPLETED]`: Finalizado exitosamente con recuentos de bytes verificados. 
- `[FAILED]`: Se encontró un error de E/S (el mensaje de error se muestra en línea). 
- `[CANCELLED]`: Cancelado por el usuario. 
- **Acciones de control**: 
- **Cancelar tarea**: finaliza de forma segura la transferencia seleccionada en cola o en ejecución. 
- **Borrar completado**: elimina los trabajos terminados, fallidos y cancelados de la lista. 
- **Resolución de conflictos en segundo plano**: si una tarea en segundo plano encuentra un conflicto de sobrescritura, ATBCmder genera una notificación que le permite resolverla sin cancelar otras tareas simultáneas. 

---

## 8. Recetas prácticas paso a paso

### Receta 1: Copia de seguridad segura de varios volúmenes con verificación de suma de comprobación

**Objetivo**: realizar una copia de seguridad de un archivo fotográfico de alto valor desde su Mac en una unidad APFS externa, lo que garantiza cero daños silenciosos y resuelve posibles duplicados de forma segura. 

```
Step 1: Open source in Left Panel (~/Pictures/2026_Photos).
Step 2: Open backup destination in Right Panel (/Volumes/SanDiskPro/Photo_Backup).
Step 3: Press Cmd+A (Select All) in Left Panel.
Step 4: Press F5 (Copy).
Step 5: Click [Options ▼] to expand advanced parameters:
        • Set 'When file exists' to: [Auto-rename target]
        • Check [✔] Verify after copy: [SHA-256]
        • Check [✔] Copy date/time
        • Check [✔] Check free space
Step 6: Click [Start].
```
 
*Resultado: ATBCmder calcula hashes SHA-256 durante el flujo de copia, confirma la integridad exacta del bloque en el disco externo y numera automáticamente cualquier instantánea en conflicto sin intervención humana.* 

---

### Receta 2: Puesta en escena de precisión: selección de comodines, inversión e implementación de enlaces simbólicos

**Objetivo**: en un repositorio mixto que contiene código y artefactos compilados, seleccione todos los archivos JavaScript, TypeScript y JSON mientras ignora las salidas compiladas `.map` y `.log`, luego vincúlelas simbólicamente en una carpeta de banco de pruebas. 

```
Step 1: Navigate Left Panel to /Users/brain/dev/app/src.
Step 2: Navigate Right Panel to /Users/brain/dev/testbed/lib.
Step 3: Press Num+ (Select Group).
Step 4: Enter pattern: *.ts;*.tsx;*.js;*.json and press Enter.
Step 5: Notice you also matched *.test.ts files. Press Num- (Unmark Group).
Step 6: Enter pattern: *.test.ts and press Enter.
Step 7: Check your status bar: 84 files selected.
Step 8: Select Menu File → Create Symbolic Link... (cm_SymLink).
```
 
*Resultado: se crean instantáneamente ochenta y cuatro enlaces simbólicos en la carpeta del banco de pruebas, que apuntan claramente a sus archivos fuente activos.* 

---

### Receta 3: ingesta paralela de alto rendimiento utilizando colas en segundo plano

**Objetivo**: descargar dos tarjetas de cámara multimedia grandes simultáneamente en el RAID de su estación de trabajo sin bloquear la interfaz de usuario ni ralentizar ninguno de los lectores de tarjetas. 

```
Step 1: Mount Card A (/Volumes/CFexpress_A) in Left Panel.
Step 2: Select all raw footage (Cmd+A), press F5 (Copy).
Step 3: Click [Add To Queue #1]. Transfer begins streaming in background.
Step 4: Open Card B (/Volumes/SD_Card_B) in Left Panel (Cmd+T for a new tab).
Step 5: Select all audio tracks (Cmd+A), press F5 (Copy).
Step 6: Click the queue dropdown chevron and choose [Queue #2].
Step 7: Press Toolbar ⚡ (cm_OperationsPanel) to watch both queues stream concurrently.
```
 
*Resultado: Ambas tarjetas ingestan simultáneamente con la saturación total del bus de hardware mientras usted continúa explorando archivos, editando notas o cambiando el nombre de los recursos.* 

---

## 9. Alertas de seguridad y sistema

> [!WARNING] 
> **Eliminación permanente en unidades externas y de red**: 
> Las unidades externas formateadas con FAT32, exFAT o NTFS (a través de controladores de terceros) y los recursos compartidos de red remotos (SMB/SFTP) a menudo carecen de un directorio `.Papeleraes` del sistema macOS. Al eliminar elementos de estos volúmenes, ATBCmder le avisará que la Papelera no está disponible. Confirmar esta acción **elimina permanentemente** los archivos. Siempre verifique los encabezados de las rutas antes de confirmar. 

> [!CAUTION] 
> **Sobrescribir archivos en operaciones por lotes**: 
> Cuando se utiliza **Sobrescribir todo** en el cuadro de diálogo de colisión, ATBCmder suprime más alertas de colisión para todo ese trabajo. Si su directorio de origen contiene nombres de archivos duplicados accidentalmente, los archivos de destino existentes se reemplazarán irreversiblemente. Considere usar **Renombrar automáticamente** o **Sobrescribir versiones anteriores** para copias por lotes desatendidas. 

> [!IMPORTANT] 
> **Limitaciones del enlace duro APFS**: 
> Los enlaces físicos no pueden abarcar diferentes volúmenes APFS, particiones de disco o imágenes de disco. Si intenta crear un vínculo físico entre dos puntos de montaje diferentes (como `/Users/...` a `/Volumes/ExternalDrive/...`), la operación fallará. Utilice **Enlaces simbólicos** (`cm_SymLink`) siempre que establezca enlaces entre diferentes volúmenes de almacenamiento. 

> [!TIP] 
> **Optimización de las velocidades de transferencia NVMe**: 
> ATBCmder está optimizado para la memoria unificada Apple Silicon moderna y SSD NVMe PCIe 4.0/5.0. De forma predeterminada, las operaciones de archivos utilizan un **búfer de copia de 1 MB** de alto rendimiento (`operations.copy_buffer_size`). Puede ajustar este búfer en **Preferencias** → **Operaciones de archivos** para que coincida con interfaces de red de 10 GbE de alta gama o matrices de almacenamiento especializadas. 

---

## 10. Tabla de referencia del teclado de matriz dual

| Categoría | Acción | Acceso directo a macOS | Clave clásica | ID de comando | Descripción | 
| :--- | :--- | :--- | :--- | :--- | :--- | 
| **Operaciones de archivos principales** | Copiar al destino | `F5` / `Fn+F5` | `F5` | `cm_Copy` | Copia los elementos seleccionados al panel inactivo. | 
| | Copiar en el mismo panel | `Shift+F5` / `⇧F5` | `Shift+F5` | `cm_CopySamePanel` | Clona el archivo en el panel activo con mensaje de cambio de nombre. | 
| | Mover al destino | `F6` / `Fn+F6` | `F6` | `cm_Move` | Mueve los elementos seleccionados al panel inactivo. | 
| | Nuevo directorio | `F7` / `Fn+F7` | `F7` | `cm_MkDir` | Crea un nuevo directorio o árbol anidado. | 
| | Eliminar a la Papelera | `F8` / `⌘⌫` | `F8` / `Delete` | `cm_Delete` | Envía elementos seleccionados a la Papelera de macOS. | 
| | Eliminación permanente | `Shift+Delete` / `⇧⌦` | `Shift+F8` | `cm_Delete` | Desvincula archivos inmediatamente sin Papelera. | 
| | Limpieza segura | `Alt+Delete` / `⌥⌦` | `Alt+Delete` | `cm_Wipe` | Sobrescribe archivos con datos aleatorios antes de desvincularlos. | 
| **Renombrar** | Cambio de nombre rápido en línea| `F2` / `Shift+F6` | `Shift+F6` | `cm_RenameOnly` | Cambia el nombre del elemento activo directamente en la fila de la tabla. | 
| | Cambiar nombre del cuadro de diálogo | *Menú Archivo* | — | `cm_Rename` | Abre un cuadro de diálogo de texto modal para cambiar el nombre. | 
| **Selección** | Seleccionar todo | `Cmd+A` / `⌘A` | `Ctrl+A` / `Ctrl+Num+` | `cm_MarkMarkAll` | Selecciona todos los archivos y carpetas. | 
| | Deseleccionar todo | `Cmd+Shift+A` / `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+L` | `cm_MarkUnmarkAll` | Borra todas las selecciones. | 
| | Invertir selección | `Num*` / `⌥⌘I` | `Num*` | `cm_MarkInvert` | Invierte el estado de selección de todos los elementos. | 
| | Grupo de marcas | `Num+` | `Num+` | `cm_MarkPlus` | Selecciona elementos mediante comodín o patrón RegEx. | 
| | Desmarcar grupo | `Num-` | `Num-` | `cm_MarkMinus` | Deselecciona elementos mediante un patrón comodín. | 
| | Misma extensión | `Shift+Num+` | `Shift+Num+` | `cm_MarkCurrentExtension`| Selecciona todos los elementos con la misma extensión de archivo. | 
| | Alternar selección | `Space` / `Insert` | `Insert` / `Space` | `cm_SelectOrDeselectFile` | Alterna la selección de elementos y baja. | 
| **Portapapeles** | Copiar al portapapeles | `Cmd+C` / `⌘C` | `Ctrl+C` | `cm_CopyToClipboard` | Copia las rutas de los archivos al portapapeles del sistema. | 
| | Cortar al portapapeles | `Cmd+X` / `⌘X` | `Ctrl+X` | `cm_CutToClipboard` | Corta las rutas de los archivos al portapapeles del sistema. | 
| | Pegar portapapeles | `Cmd+V` / `⌘V` | `Ctrl+V` | `cm_PasteFromClipboard` | Pega los archivos del portapapeles en el panel activo. | 
| | Pegar como Mover | `Cmd+Option+V` / `⌥⌘V`| `Ctrl+Alt+V` | `cm_PasteAsMove` | Mueve los archivos del portapapeles al panel activo. | 
| | Copiar ruta completa | *Editar menú* | — | `cm_CopyFullPath` | Copia la ruta absoluta de UNIX al portapapeles. | 
| | Copiar nombre de archivo | *Editar menú* | — | `cm_CopyFileNameToClip` | Copia el nombre del archivo al portapapeles. | 
| **Enlaces y espacio** | Crear enlace simbólico | *Menú Archivo* | — | `cm_SymLink` | Crea un enlace simbólico en el panel de destino. | 
| | Crear vínculo físico | *Menú Archivo* | — | `cm_HardLink` | Crea un enlace físico en el panel de destino. | 
| | Propiedades / Chmod | `Alt+Enter` / `⌥⏎` | `Alt+Enter` | `cm_SetFileProperties` | Abre permisos, chmod octal y marcas de tiempo. | 
| | Calcular espacio | `Alt+Shift+Enter` / `⌥⇧⏎` | `Alt+Shift+Enter` | `cm_CountDirContent` | Calcula los tamaños de directorio recursivos (`Ctrl+L` / `cm_CalculateSpace` para el total seleccionado). | 
| **Cola de transferencia**| Cola en segundo plano | `Toolbar ⚡` | — | `cm_OperationsPanel` | Abre el monitor de transferencia en segundo plano de 3 colas. |

--- 

<div align="center"> 
<p>Ahora que domina las operaciones diarias de archivos, las técnicas de selección y las transferencias en segundo plano:</p> 
<p><strong><a href="viewers_and_editors.md">Continúe con el Capítulo 4: Listado universal y editores integrados →ATB_HTML_00006__</strong></p> 
</div>