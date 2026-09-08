# Capítulo 9: Soluciones prácticas y resolución de problemas

Si bien los administradores de archivos ortodoxos de panel dual son reconocidos por su velocidad bruta y la eficiencia del teclado, dominar las tareas del mundo real a menudo requiere comprender cómo los distintos subsistemas (como la sincronización de directorios, el cambio de nombre de patrones por lotes, los sistemas de archivos virtuales remotos, el reempaquetado de archivos y la búsqueda recursiva) funcionan juntos en escenarios cotidianos. Además, operar dentro de macOS moderno introduce límites de seguridad, restricciones de espacio aislado e intersecciones de accesos directos al sistema que todo usuario eventualmente encuentra. 

Este capítulo se divide en dos secciones completas: 

1. **Recetas prácticas y flujos de trabajo**: cinco tutoriales completos de principio a fin que cubren flujos de trabajo de administración de archivos de alto valor con procedimientos paso a paso, representaciones visuales de la interfaz de usuario, atajos de teclado y consejos para usuarios avanzados. 
2. **Guía de solución de problemas y preguntas frecuentes**: explicaciones detalladas y resoluciones de diagnóstico para preguntas operativas comunes, errores de permisos, comportamientos de actualización automática, restablecimientos de configuración, teclas de función del teclado Apple y mecanismos de transferencia de archivos entre volúmenes. 

---

## 1. Inicio rápido visual: Matriz de resolución de problemas cotidianos

La siguiente matriz de decisiones asigna objetivos comunes de administración de archivos y desafíos técnicos directamente a las herramientas integradas y los identificadores de comandos de ATBCmder: 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                 ENRUTADOR DE TAREAS DIARIAS Y RESOLUCIÓN DE PROBLEMAS                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  TAREA / OBJETIVO                          HERRAMIENTA / MÉTODO     ATAJO              │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Sincronizar proyectos a NAS o disco ext. Sincronizador carpetas Shift+F12 (⇧F12)  │
│  [2] Renombrar fotos por fecha y lote      Renombrado múltiple     Ctrl+M (⌃M)         │
│  [3] Montar NAS, servidor o nube           Gestor VFS de red       cm_ManageConnections│
│  [4] Editar archivos dentro de .zip        VFS archivos + Editor   Enter ➔ F4 ➔ Guardar│
│  [5] Hallar archivos grandes anidados      Vista plana             Cmd+B (⌘B) / Alt+F7 │
│                                                                                        │
│  PROBLEMA / SÍNTOMA                        CAUSA RAÍZ              RESOLUCIÓN          │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  Error "Operation not permitted"           Sandbox de macOS / TCC cm_GrantAccess       │
│  Discos externos no se actualizan solos    Sin FSEvents en FAT/exFAT attr_poll_interval│
│  Probar ajustes sin riesgo alguno          Protección XML producción ATBCmder_test.sh  │
│  Teclas F cambian brillo o volumen         Teclas multimedia macOS Tecla Fn o Ajustes  │
│  Mover entre volúmenes tarda bastante      Copia física + Borrado Verificar espacio    │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Tabla de referencia rápida de matriz dual

| Acción / Diagnóstico | Atajo de teclado en macOS | Tecla Commander clásica | ID de comando | Propósito principal | 
| :--- | :--- | :--- | :--- | :--- | 
| **Sincronización de directorio** | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | Compara y sincroniza árboles de directorios de doble panel. | 
| **Cambio de nombre múltiple por lotes** | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | Cambia el nombre de varios archivos utilizando tokens, contadores y RegEx. | 
| **Conexiones de red** | Menú: Red | `cm_ManageConnections`| `cm_ManageConnections`| Gestiona perfiles de servidor SMB, SFTP, WebDAV y FTP guardados. | 
| **Conexión de red rápida** | Menú: Red | `cm_NetworkConnect` | `cm_NetworkConnect` | Cuadro de diálogo de conexión ad-hoc para servidores remotos. | 
| **Edición directa en archivo comprimido** | `F4` / `Fn+F4` | `F4` | `cm_Edit` | Edita elemento del archivo; activa `RepackWorker` al guardar. | 
| **Vista de árbol plano (Flat Branch View)** | `Cmd+B` / `⌘B` | `Ctrl+B` | `cm_FlatView` | Muestra recursivamente todos los archivos anidados en una única lista plana. | 
| **Búsqueda avanzada** | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` | Búsqueda de archivos con múltiples filtros con salida "Feed to Listbox". | 
| **Conceder acceso al sistema de archivos**| Menú: Archivo / Ayuda | — | `cm_GrantFilesystemAccess`| Inicia el asistente de permisos de la aplicación Sandbox de macOS. | 
| **Actualización manual del panel** | `Ctrl+R` / `⌃R` o `Cmd+R` / `⌘R` | `Ctrl+R` | `cm_Refresh` | Fuerza una relectura inmediata del directorio desde el disco. | 
| **Terminal del sistema de lanzamiento** | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` | Genera la terminal macOS en la ruta del panel actual. | 
| **Calcular espacio en carpeta** | `Alt+Shift+Enter` (`Space`) | `Alt+Shift+Enter` (`Space`) | `cm_CountDirContent` / `cm_CalculateSpace` | Calcula el tamaño de byte recursivo agregado (`Space` para un solo, `Ctrl+L` para el total seleccionado). | 
| **Borrado seguro (Wipe)** | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | Sobrescritura de múltiples pasadas y eliminación permanente de archivos. | 

---

## 2. Recetas prácticas y flujos de trabajo

### 2.1 Receta 1: Comparar y sincronizar dos carpetas de respaldo

**Objetivo**: Asegúrese de que una unidad de respaldo externa o una carpeta de red contenga una réplica exacta y actualizada de su directorio de proyecto activo, con visibilidad completa de los archivos agregados, modificados o eliminados antes de realizar cambios. 

![Directory Synchronization](images/folder_synchronization.png) 
*Figura 9.1: El cuadro de diálogo Sincronización de carpetas (Sync Dirs) que muestra comparaciones de directorios en paralelo, flechas de copia direccionales y opciones de espejo asimétrico.*

#### Procedimiento paso a paso

1. **Alinear origen y destino en paneles duales**: 
- En el **Panel izquierdo**, navegue hasta su directorio de trabajo local principal (por ejemplo, `~/Documents/Projects/AppAlpha`). 
- Presione **`Tab`** para cambiar al **Panel derecho** y navegue hasta el destino de la copia de seguridad de destino (por ejemplo, `/Volumes/BackupDrive/Backups/AppAlpha`). 
2. **Iniciar sincronización de directorio**: 
- Presione **`Shift+F12`** (`⇧F12`) o seleccione **Comandos ➔ Sincronizar directorios...** en la barra de menú. 
- El cuadro de diálogo Sincronizar directorios se abre con la ruta izquierda y la ruta derecha completadas automáticamente. 
3. **Configurar parámetros de comparación**: 
- Marque **Comparar subdirectorios** para recorrer todas las carpetas anidadas de forma recursiva. 
- Marque **Comparar por contenido** si necesita certeza criptográfica (verificar los bytes del archivo mediante `filecmp`) en lugar de depender únicamente del tamaño de los archivos y las marcas de tiempo de modificación. 
- Asegúrese de que **Tolerancia de marca de tiempo FAT/SMB (2,0 segundos)** esté habilitada si el destino de su copia de seguridad utiliza FAT32, exFAT o un recurso compartido de red SMB, evitando indicadores falsos de discrepancia causados ​​por el redondeo de marca de tiempo del sistema de archivos de 2 segundos. 
4. **Iniciar la comparación**: 
- Haga clic en **Comparar** (o presione `Alt+C` / `⌥C`). 
- ATBCmder ejecuta un trabajador de comparación en segundo plano (`SyncCompareWorker`) y completa la tabla de comparación con indicadores de acción direccional: 
* **`->` (De izquierda a derecha)**: el archivo local es más nuevo o solo existe en el lado izquierdo. Acción: copiar de izquierda a derecha. 
* **`<-` (Right to Left)**: The backup file is newer, or only exists on the right. Action: copy right to left.
     * **`=` (Equal)**: Both files are identical in size and timestamp/content. These are hidden from the pending action list by default.
     * **`!=` (Conflict)**: Incompatible directory-versus-file collision or timestamp mismatch requiring manual inspection.
5. **Select Your Synchronization Strategy**:
   - **Two-Way Symmetric Sync (Default)**: Copies newer files in both directions (`->` y `<-`). No files are deleted on either side. Ideal for syncing collaborative folders between machines.
   - **Asymmetric Mirroring (`Asymmetric` Checkbox Enabled)**: Makes the Right directory an exact binary replica of the Left directory. Any file on the Right that does not exist on the Left is **permanently deleted from the backup target**.
6. **Review and Execute**:
   - Inspect the summary count at the bottom: *e.g., "Left to Right: 42 files (128.4 MB) | Right to Left: 0 files | Deletes: 3 files"*.
   - Click **Synchronize** to launch the non-blocking background transfer queue. Progress bars reflect active transfer volume and remaining item counts.

> [!CAUTION] 
> **Peligro de pérdida de datos de duplicación asimétrica**: 
> Cuando se marca el modo **Asimétrico**, los archivos presentes en la unidad de destino que se eliminaron o cambiaron de nombre en la fuente se **eliminarán permanentemente** sin pasar a la Papelera de macOS. ¡Revise siempre la tabla de comparación direccional antes de hacer clic en Sincronizar! 

> [!TIP] 
> **⚡ Consejo profesional: verificación a nivel de contenido para medios y código**: 
> Al realizar copias de seguridad de secuencias de vídeo o repositorios Git, los tamaños de los archivos pueden coincidir mientras existen sutiles daños en los bytes internos. Consulte siempre **Comparar por contenido** para archivos de misión crítica. Aunque la comparación byte a byte lleva más tiempo a través de USB o Wi-Fi, garantiza el 100% de integridad de los datos. 

---

### 2.2 Receta 2: Cambiar el nombre de las fotos de la cámara por lotes con fechas y números de secuencia

**Objetivo**: transformar cientos de archivos de cámara no organizados (por ejemplo, `DSC_0012.JPG`, `DSC_0013.JPG`, `IMG_4901.CR3`) en nombres de archivos limpios y ordenables, como `2026-09-06_Vacation_001.jpg`, con contadores de secuencia con relleno de ceros y vistas previas de seguridad en vivo. 

![Batch Multi-Rename Tool](images/multi_rename_dialog.png) 
*Figura 9.2: La herramienta de cambio de nombre múltiple por lotes que presenta filas de vista previa en tiempo real, tokens de metadatos, controles de contador numérico y detección de colisiones.*

#### Procedimiento paso a paso

1. **Seleccione las fotos**: 
- Navegue hasta el directorio de importación de su cámara en el panel activo. 
- Seleccione todas las fotos usando **`Cmd+A`** (`⌘A`), o presione **`+`** en su teclado para ingresar una máscara comodín como `*.jpg;*.jpeg;*.cr3;*.arw`. 
2. **Inicie la herramienta de cambio de nombre múltiple por lotes**: 
- Presione **`Ctrl+M`** (`⌃M`) o **`Cmd+M`** (`⌘M`), o elija **Archivos ➔ Herramienta de renombrado masivo (Multi-Rename)...** en la barra de menú. 
3. **Defina la máscara del nombre de archivo**: 
- En el campo **Máscara de nombre de archivo**, ingrese la estructura deseada usando tokens de metadatos: 
     ```
     [Y]-[M]-[D]_Vacation_[C]
     ```


- **Explicación del token**: 
* `[Y]`: Año de modificación del archivo de 4 dígitos (por ejemplo, `2026`). 
* `[M]`: Mes de 2 dígitos (por ejemplo, `09`). 
* `[D]`: Día de 2 dígitos (p. ej., `06`). 
* `Vacation`: Texto descriptivo estático. 
* `[C]`: Contador numérico secuencial. 
4. **Configurar la secuencia del contador**: 
- En la tarjeta **Configuración del contador**: 
* **Comienza en**: `1` 
* **Paso**: `1` 
* **Dígitos**: `3` (esto aplica el relleno de ceros: `001`, `002`, `003`... hasta `999`). 
5. **Elimine los prefijos de la cámara con Buscar y reemplazar (opcional)**: 
- Si desea conservar parte del nombre de archivo original sin el prefijo de la cámara (por ejemplo, manteniendo el número de secuencia de la cámara de `DSC_8941.JPG`): 
* Establezca **Máscara de nombre de archivo** en: `[YMD]_[N5-]` 
* `[N5-]` extrae caracteres desde el índice 5 hasta el final del nombre, eliminando `DSC_` por completo. 
- Como alternativa, utilice los campos **Buscar y reemplazar**: 
* **Buscar**: `DSC_` 
* **Reemplazar**: `Photo_` 
* Marque **RegEx** si usa patrones de expresión complejos como `^IMG_(\d+)`. 
6. **Inspeccione la tabla de vista previa en vivo**: 
- La tabla de 3 columnas (`Old Name`, `New Name`, `Directory`) se actualiza instantáneamente con cada pulsación de tecla. 
- Verifique la columna **Estado**: ATBCmder resalta los nombres de objetivos duplicados en negrita y rojo con un indicador de colisión, lo que evita sobrescrituras accidentales. 
7. **Ejecutar el cambio de nombre**: 
- Presione **`Enter`** o haga clic en **Iniciar cambio de nombre**. ATBCmder realiza los cambios de nombre de forma atómica en el disco y actualiza la vista del panel. 

> [!NOTE] 
> **Seguridad de la extensión**: 
> De forma predeterminada, la **Máscara de extensión** está configurada en `[E]`, preservando la extensión del archivo original sin modificar. Nunca elimine `[E]` a menos que tenga la intención explícita de eliminar las extensiones de sus archivos.

> [!TIP] 
> **⚡ Consejo profesional: flujo de trabajo del editor externo (`⌘I`)**: 
> Si tiene una lista irregular de nombres de clientes o títulos de pistas, presione **`Cmd+I`** (`⌘I` / Editar en editor externo) dentro de la herramienta Multi-Rename. ATBCmder exporta los nombres de los objetivos a su editor de texto predeterminado. Edite la lista en Vim, VS Code o TextEdit, guarde el documento y ATBCmder importará inmediatamente los nombres revisados ​​en la cuadrícula de vista previa. 

---

### 2.3 Receta 3: Conexión a un NAS doméstico/de oficina a través de SMB, SFTP o WebDAV

**Objetivo**: montar un grupo de almacenamiento TrueNAS o Synology local, un servidor AWS EC2 Linux o un repositorio en la nube Nextcloud WebDAV en una pestaña de panel dual sin tener que hacer malabarismos con comandos de terminal separados u hojas de conexión del Finder. 

![Remote VFS Connection](images/smb_sftp_ftp_remote_access.png) 
*Figura 9.3: Configuración de recursos compartidos de red remotos seguros en protocolos SMB, SFTP y WebDAV.*

#### Procedimiento paso a paso

1. **Abra el Administrador de conexión de red**: 
- Elija **Red ➔ Administrar conexiones de red...** en la barra de menú nativa o ejecute el comando **`cm_ManageConnections`**. 
2. **Crea un nuevo perfil de conexión**: 
- Haga clic en el botón **`➕ New`** en la parte inferior izquierda. 
- En el campo **Etiqueta**, ingrese un identificador reconocible (por ejemplo, `Synology Office NAS` o `AWS Production Web`). 
3. **Configurar protocolo y detalles del host**: 
- **Protocolo**: seleccione su protocolo de destino en el menú desplegable: 
* **SMB/CIFS**: Puerto `445` (Estándar para Synology, QNAP, Windows Server, TrueNAS). 
* **SFTP (Transferencia de archivos SSH)**: Puerto `22` (Estándar para instancias en la nube de Linux/UNIX). 
* **WebDAV / WebDAVS**: Puerto `80` o `443` (Estándar para Nextcloud, ownCloud). 
* **FTP/FTPS**: Puerto `21` o `990` (hosts de archivos antiguos). 
- **Host**: ingrese la dirección IP o el nombre de dominio (por ejemplo, `192.168.1.100` o `sftp.mycompany.com`). 
- **Puerto**: se configura automáticamente cuando se elige el protocolo; ajústelo si su servidor utiliza un puerto no estándar. 
- **Nombre de usuario**: ingrese el nombre de usuario de su cuenta del sistema remoto. 
- **Ruta remota**: establezca el directorio de aterrizaje predeterminado (por ejemplo, `/volume1/Media` o `/var/www/html`). 
4. **Almacenamiento seguro de credenciales**: 
- Ingrese su contraseña o clave de acceso. 
- Marque **Recordar contraseña en el llavero de macOS**. 
- **Garantía de seguridad**: ATBCmder nunca almacena credenciales de texto sin formato en archivos de configuración XML. Todos los secretos están sellados criptográficamente dentro del llavero nativo de Apple (`com.aitobox.atbcmder.vfs`). 
5. **Pruebe la conexión**: 
- Haga clic en **`🔍 Test Connection`**. 
- ATBCmder envía un trabajador en segundo plano (`ConnectionTestWorker`) que valida la accesibilidad de la red, verifica las claves de host SSH o los certificados TLS, verifica las credenciales y muestra una alerta de éxito sin cerrar el cuadro de diálogo. 
6. **Conectar y navegar**: 
- Haga clic en **`🔗 Connect`** (o presione `Enter`). 
- Se abre una nueva pestaña de carpeta en el panel activo, que muestra la ruta remota formateada como un URI VFS unificado: 
     ```
     vfs://smb://admin@192.168.1.100/volume1/Media/
     vfs://sftp://ubuntu@aws.prod.internal:22/var/www/html/
     ```


- Ahora puede explorar, buscar, copiar (`F5`), mover (`F6`) y eliminar (`F8`) archivos en discos locales y servidores remotos con idéntica agilidad del panel dual. 
7. **Reconexión rápida desde la barra de menú**: 
- Todos los perfiles guardados aparecen automáticamente en **Red ➔ Conexiones guardadas**. Simplemente haga clic en cualquier servidor guardado para montarlo al instante. 

> [!TIP] 
> **⚡ Consejo profesional: autenticación basada en claves SSH para SFTP**: 
> Para el acceso automatizado al servidor en la nube, configure la autenticación de clave pública. En su perfil de conexión SFTP, deje el campo de contraseña en blanco y apunte a su clave privada local (por ejemplo, `~/.ssh/id_ed25519`). Si la clave está protegida por una frase de contraseña, ATBCmder la solicita una vez y la guarda de forma segura en su llavero macOS. 

---

### 2.4 Receta 4: Editar un archivo directamente dentro de un archivo sin extraerlo

**Objetivo**: Modificar un archivo de configuración anidado (`settings.json` o `config.yaml`) dentro de un archivo de varios gigabytes `.zip`, `.tar.gz` o `.7z` en el almacenamiento local o en un servidor remoto sin descomprimir todo el archivo en su disco duro. 

![Archive VFS](images/archive_vfs.png) 
*Figura 9.4: Navegación y edición dentro de archivos comprimidos a través del sistema de archivos virtual unificado `vfs://`.*

#### Procedimiento paso a paso

1. **Ingrese al Archivo como Directorio Virtual**: 
- Resalte el archivo comprimido (por ejemplo, `production_backup.zip`) en el panel activo. 
- Presione **`Enter`** (o haga doble clic). 
- ATBCmder intercepta la navegación y monta el archivo como un sistema de archivos virtual: 
     ```
     vfs:///Users/brain/Downloads/production_backup.zip/
     ```
 

2. **Navegue hasta el archivo de destino**: 
- Explore directorios virtuales anidados (`etc`, `nginx`, `conf.d`) tal como lo haría en un volumen físico. 
- Localice el archivo que necesita actualizar (por ejemplo, `nginx.conf` o `app_settings.json`). 
3. **Abrir en el editor de texto integrado**: 
- Presione **`F4`** (`Fn+F4` / `cm_Edit`). 
- ATBCmder transmite el miembro comprimido a un búfer aislado temporal y lo abre directamente en el editor de texto resaltado por sintaxis. 
4. **Realizar ediciones y guardar**: 
- Realice las modificaciones de configuración necesarias. 
- Presione **`Cmd+S`** (`⌘S`) para guardar el búfer. 
5. **Ciclo de vida de reempaquetado automático (`RepackWorker`)**: 
- Cuando guarda o cierra el editor, el motor de reempaquetado en segundo plano de ATBCmder (`RepackWorker`) se activa automáticamente: 
1. Calcula el delta entre el miembro comprimido original y su búfer modificado. 
2. Comprueba el tamaño total del archivo con respecto al umbral de advertencia configurado (`ArchiveRepackWarningMB`). 
3. Recomprime el archivo modificado y reconstruye la estructura del archivo en un archivo temporal. 
4. Reemplaza atómicamente el archivo original en el disco, garantizando que no se produzcan daños si el sistema pierde energía a mitad de escritura. 
5. La vista del panel activo se actualiza automáticamente para mostrar los tamaños de bytes de los miembros y las marcas de tiempo actualizados.

> [!IMPORTANT] 
> **Guardia de reempaquetado de archivos grandes (`ArchiveRepackWarningMB`)**: 
> Actualizar un único archivo de texto de 2 KB dentro de un archivo de 15 GB requiere reescribir todo el archivo en el disco. Para evitar picos inesperados de CPU y desgaste de SSD, ATBCmder verifica el tamaño del archivo. Si el archivo supera `ArchiveRepackWarningMB` (predeterminado: 500 MB), aparecerá un cuadro de diálogo de advertencia: *"Este archivo tiene 1,4 GB. Al volver a empaquetarlo se reescribirá todo el archivo. ¿Desea continuar?"* Puede personalizar este umbral en **Configuración ➔ Opciones ➔ Archivos**. 

---

### 2.5 Receta 5: Buscar y eliminar archivos grandes e inflados en directorios anidados

**Objetivo**: recuperar la valiosa capacidad de SSD localizando rápidamente y eliminando de forma segura renderizaciones de video 4K abandonadas, carpetas `node_modules` infladas, imágenes de discos virtuales Docker o instaladores DMG obsoletos dispersos en estructuras de directorios de varios niveles. 

![Flat Branch View](images/branch_view.png) 
*Figura 9.5: Vista de rama plana (`Cmd+B`) que muestra contenidos profundamente anidados en una única tabla aplanada para una clasificación instantánea por tamaño.*

#### Método A: Aplanamiento instantáneo mediante vista de rama plana (`Cmd+B`)

1. **Navegue a la carpeta raíz principal**: 
- Resalte la carpeta principal de nivel superior que desea auditar (por ejemplo, `~/Projects` o `~/Downloads`). 
2. **Activar vista de sucursal plana**: 
- Presione **`Cmd+B`** (`⌘B`) o **`Ctrl+B`** (`cm_FlatView`), o seleccione **Mostrar ➔ Vista de sucursal (Vista plana)**. 
- ATBCmder escanea recursivamente todos los subdirectorios y muestra cada archivo anidado en una **lista única y plana**, eliminando los límites de las carpetas del directorio. 
3. **Ordenar por tamaño descendente**: 
- Haga clic en el encabezado de la columna **Tamaño** o presione **`Ctrl+F6`** (`cm_SortBySize`) para ordenar los archivos más grandes en la parte superior. 
- Archivos ISO gigantes, volcados de bases de datos e imágenes de máquinas virtuales flotan inmediatamente en la parte superior de su panel. 
4. **Calcular espacio en el directorio**: 
- Para subcarpetas visibles en vistas estándar, coloque el cursor en cualquier carpeta y presione **`Space`** (`␣` / `cm_CalculateSpace`). ATBCmder calcula la huella total de bytes recursivos y la muestra en lugar de la etiqueta predeterminada `<DIR>`. 
5. **Salir de la vista de sucursal**: 
- Presione **`Cmd+B`** nuevamente, o presione `Esc` / `Backspace` en `..` para volver a la navegación jerárquica normal del directorio. 

---

#### Método B: Filtrado dirigido mediante búsqueda avanzada (`Alt+F7`) y "Alimentar al cuadro de lista"

![Advanced Search](images/advanced_search_dialog.png) 
*Figura 9.6: Cuadro de diálogo Búsqueda avanzada con criterios de filtro de tamaño y el botón "Alimentar al cuadro de lista".* 

1. **Iniciar búsqueda avanzada**: 
- Presione **`Alt+F7`** (`⌥F7`) o seleccione **Comandos ➔ Buscar...**. 
2. **Definir filtros de tamaño y tipo**: 
- En el campo **Buscar en**, confirme su directorio raíz. 
- Verifique el filtro **Tamaño**: seleccione **`>`** e ingrese `100` con unidad **`MB`** (o `1` **`GB`**). 
- En el campo **Máscara de archivo**, especifique las extensiones de destino (por ejemplo, `*.dmg;*.iso;*.mp4;*.mov;*.zip`) o déjelas como `*` para encontrar cualquier elemento inflado. 
- En la pestaña **Fecha**, opcionalmente restrinja los resultados a archivos no modificados en los últimos 180 días. 
3. **Ejecutar la búsqueda**: 
- Haga clic en **Iniciar búsqueda**. 
4. **Alimentar resultados en una pestaña del panel virtual ("Alimentar al cuadro de lista")**: 
- Una vez que se completen los resultados, haga clic en el botón **Alimentar al cuadro de lista**. 
- Todo el conjunto de resultados de búsqueda se transfiere a una **pestaña virtual dedicada** en su panel activo. 
- A diferencia de un cuadro de diálogo modal estático, los archivos en esta pestaña se comportan como elementos normales del panel de archivos: puede obtener una vista previa de ellos con Vista rápida (`Ctrl+Q` / `⌘Q`), inspeccionarlos en Universal Lister (`F3`) o marcar varios archivos con `Insert` / `Space`. 
5. **Revisar y eliminar**: 
- Seleccione archivos no deseados y presione **`F8`** (`Fn+F8` / `cm_Delete`) para moverlos de forma segura a la Papelera de macOS. 
- Si necesita un borrado permanente e irrecuperable de datos (por ejemplo, borrar datos confidenciales del cliente), presione **`Alt+Delete`** (`⌥⌫` / `cm_Wipe`) para activar la destrucción segura de archivos en múltiples pasadas. 

> [!TIP] 
> **⚡ Consejo profesional: identificación de archivos duplicados idénticos mediante sumas de verificación**: 
> Si sospecha que varios archivos grandes son duplicados exactos, selecciónelos y presione **`Ctrl+X`** (`⌃X` / `cm_CheckSumCalc`). Elija **SHA-256** y haga clic en Calcular. Los resúmenes de hash coincidentes confirman duplicados binarios al 100%, lo que le permite eliminar copias superfluas con total confianza. 

---

## 3. Guía de solución de problemas y preguntas frecuentes (FAQ)

### 3.1 Errores de "Operación no permitida"/Permiso denegado de macOS

#### Causa principal

En macOS moderno (macOS 12 Monterey a macOS 15 Sequoia), Apple aplica estrictos límites de privacidad **App Sandbox** y **TCC (Transparencia, Consentimiento y Control)**. Las aplicaciones en espacio aislado no pueden acceder a unidades externas, carpetas del sistema o incluso directorios de usuarios estándar (`~/Documents`, `~/Downloads`, `~/Desktop`) sin un token de permiso criptográfico explícito otorgado por el usuario conocido como **Marcador con ámbito de seguridad**. 

Si a ATBCmder no se le ha otorgado acceso al sistema de archivos, puede experimentar: 

- Cuadros de diálogo de operación de archivos que muestran: `"Error: Operation not permitted"`. 
- Los directorios aparecen vacíos aunque existan archivos en Finder. 
- Unidades USB o Thunderbolt externas bajo `/Volumes` que muestran errores de acceso denegado.

#### Solución 1: utilice el asistente de incorporación de la aplicación Sandbox (`cm_GrantFilesystemAccess`)

ATBCmder incluye un asistente de incorporación integrado diseñado para registrar marcadores de seguridad persistentes con macOS: 

```
┌─────────────────────────────────────────────────────────────┐
│  Conceder acceso al sistema (Filesystem Access)         [x] │
├─────────────────────────────────────────────────────────────┤
│  Dado que ATBCmder opera en una Sandbox segura de macOS,    │
│  requiere su autorización expresa para acceder a carpetas   │
│  críticas y discos externos.                                │
│                                                             │
│  [  Conceder acceso al directorio raíz (/)  ]               │
│                                                             │
│  [  Conceder acceso a discos externos (/Volumes)  ]         │
│                                                             │
│  [  Abrir ajustes de Acceso total al disco…  ]              │
│                                                             │
│  El acceso a la raíz es requerido por la Sandbox.           │
│  Acceso total al disco protege los datos privados.          │
│                                                  [ Listo ]  │
└─────────────────────────────────────────────────────────────┘
```
 

1. En la barra de menú, elija **Archivo** (o **Ayuda**) ➔ **Conceder acceso al sistema de archivos…**, o active el comando **`cm_GrantFilesystemAccess`**. 
2. Haga clic en **"Conceder acceso al directorio raíz (/)"**. 
* Cuando la hoja nativa de Apple `NSOpenPanel` aparezca apuntando a `Macintosh HD` (`/`), haga clic en **Conceder acceso** (o **Abrir**). 
* **Por qué funciona esto**: Al autorizar `/` se genera un marcador raíz con ámbito de seguridad almacenado en `sandbox_bookmarks.plist`. Debido a que las rutas secundarias heredan tokens de seguridad hacia abajo, otorgar acceso a `/` desbloquea permanentemente todas las carpetas de usuario estándar (`~/Documents`, `~/Downloads`, `/Applications`, `~/Projects`). 
3. Haga clic en **"Conceder acceso a discos externos (/volúmenes)"**. 
* En la hoja abierta, haga clic en **Otorgar acceso** para `/Volumes`. 
* Esto autoriza todas las unidades flash USB, SSD externas, tarjetas SD, imágenes de disco (DMG) y soportes SMB de red conectados. 
4. Haga clic en **Listo**. Sus permisos se guardan permanentemente cuando se reinicia la aplicación.

#### Solución 2: conceder acceso completo al disco (FDA) en la configuración del sistema macOS

Si necesita administrar ubicaciones protegidas del sistema, como `~/Library/Mail`, `~/Library/Messages`, cachés de navegación de Safari o árboles de respaldo de Time Machine, macOS TCC requiere un derecho adicional a nivel de sistema: 

1. Abra **Configuración del sistema** (menú Apple  ➔ Configuración del sistema). 
2. Navegue hasta **Privacidad y seguridad ➔ Acceso total al disco**. 
3. Ubique **ATBCmder** en la lista de aplicaciones y cambie el interruptor a **Activado**. 
4. Si ATBCmder no aparece en la lista: 
* Haga clic en el botón **`+`** en la parte inferior. 
* Autentícate con tu contraseña de Mac o Touch ID. 
* Seleccione `/Applications/ATBCmder.app` y haga clic en **Abrir**. 
5. Cuando se le solicite reiniciar la aplicación, haga clic en **Salir y volver a abrir**.

#### Solución 3: Restablecer los permisos de privacidad de TCC corruptos a través de la terminal

Si los permisos se dañan después de una actualización del sistema operativo macOS o un evento de nueva firma de una aplicación, restablezca la base de datos TCC usando la herramienta de línea de comandos macOS `tccutil`: 

```bash
# Reset all Full Disk Access permissions for ATBCmder
tccutil reset SystemPolicyAllFiles com.aitobox.atbcmder

# Reset Desktop, Documents, and Downloads folder permissions
tccutil reset SystemPolicyDocumentsFolder com.aitobox.atbcmder
tccutil reset SystemPolicyDownloadsFolder com.aitobox.atbcmder
tccutil reset SystemPolicyDesktopFolder com.aitobox.atbcmder
```
 

Después de ejecutar estos comandos, reinicie ATBCmder y vuelva a ejecutar **`cm_GrantFilesystemAccess`**. 

---

### 3.2 La actualización automática no detecta cambios en los archivos en el disco

#### Causa principal

ATBCmder utiliza un motor de monitoreo de archivos de varios niveles: 

1. **Kernel `FSEvents`**: en volúmenes nativos Apple APFS y HFS+, el kernel de macOS emite eventos de mutación de directorio instantáneos cuando herramientas externas agregan, modifican o eliminan archivos. 
2. **Limitaciones del sistema de archivos**: Los sistemas de archivos que no son de Apple (por ejemplo, memorias USB externas formateadas como **FAT32** o **exFAT**) y los montajes de red remotos (**SMB**, **NFS**, **SFTP**, **WebDAV**) **no admiten notificaciones del kernel `FSEvents`**. Cuando una aplicación de terceros crea o elimina un archivo en un recurso compartido SMB, el kernel de macOS no recibe eventos de notificación.

#### Pasos de resolución

1. **Ajuste el intervalo de respaldo de sondeo (`attr_poll_interval`)**: 
- Abra Preferencias a través de **`Cmd+,`** (`⌘,`) o **Configuración ➔ Opciones...**. 
- Vaya a la página **Actualización automática**. 
- Verifique que **Ver cambio de nombre de archivo** y **Ver cambio de atributos** estén habilitados. 
- Ajuste el **Intervalo de sondeo (`attr_poll_interval`)**: 
* Predeterminado: `5 seconds`. 
* Para pruebas locales rápidas o desarrollo de red activo: reduzca a `1` o `2 seconds`. 
* Para recursos compartidos de Wi-Fi de alta latencia: aumente a `10` o `15 seconds` para minimizar la sobrecarga de la red. 
2. **Consulte la lista de directorios excluidos**: 
- En la misma página de preferencias de **Actualización automática**, revise la tabla **Directorios excluidos**. 
- Si su ruta activa (o una carpeta principal) se agregó a la lista de exclusión, ATBCmder suprimirá deliberadamente la supervisión de archivos para conservar los ciclos de la CPU. Elimine la ruta si desea volver a habilitar la supervisión. 
3. **Verifique la configuración de actualización en segundo plano**: 
- Si los paneles de archivos solo no se actualizan cuando ATBCmder está minimizado o detrás de otras ventanas, marque la opción: 
`[ ] Disable auto-refresh when ATBCmder is in the background` 

- Desmarque esta opción si desea que ATBCmder refleje continuamente los resultados de la compilación en segundo plano y las descargas externas. 
4. **Forzar una actualización manual inmediata**: 
- En cualquier momento, presione **`Ctrl+R`** (`⌃R`) o **`Cmd+R`** (`⌘R`) (`cm_Refresh`). 
- Esto omite todas las capas de almacenamiento en caché, vacía los modelos de directorio internos y vuelve a leer inmediatamente el contenido del directorio desde el controlador de almacenamiento. 

---

### 3.3 Restablecimiento seguro de la configuración o prueba en modo de prueba aislado

#### Probar nuevas configuraciones de forma segura con `scripts/ATBCmder_test.sh`

Al probar diseños experimentales de atajos de teclado, nuevos temas de color o comandos de secuencias de comandos automatizados, debe evitar modificar el XML de configuración de producción. 

ATBCmder proporciona un script de inicio de pruebas en un espacio aislado: 
```bash
# Run ATBCmder in an isolated test environment
./scripts/ATBCmder_test.sh
```
 

**Cómo funciona**: 

1. El script crea un directorio temporal dedicado: `tests/.test_config/`. 
2. Copia la configuración de prueba de referencia limpia (`src/atbcmder/resources/test_config.xml`) a `tests/.test_config/atbcmder.xml`. 
3. Exporta la variable de entorno: 
   ```bash
   export ATBCMDER_CONFIG_PATH="$(pwd)/tests/.test_config"
   ```
 

4. Cuando se inicia, ATBCmder lee todas las configuraciones exclusivamente desde esta carpeta de prueba. Cualquier cambio, modificación de pestañas o experimento de teclas de acceso rápido está contenido en su totalidad en `tests/.test_config/`, dejando sus preferencias personales completamente intactas.

#### Restauración de la configuración predeterminada de fábrica

Si su configuración de producción se daña o desea comenzar completamente de nuevo: 

1. **Salga de ATBCmder** por completo (**`Cmd+Q`** / `⌘Q`). 
2. Abra la Terminal macOS y busque su directorio de configuración: 
* Instalación estándar: `~/Library/Preferencias/atbcmder/` 
* Respaldo de Linux/XDG: `~/.config/atbcmder/` 
3. Haga una copia de seguridad o elimine los archivos de configuración activos: 
   ```bash
   # Move configuration files to a backup location
   mv ~/Library/Preferences/atbcmder/atbcmder.xml ~/Library/Preferences/atbcmder/atbcmder.xml.bak
   mv ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml.bak
   ```
 

4. Reinicie ATBCmder. 
5. Al iniciar, ATBCmder detecta los archivos de configuración que faltan y regenera automáticamente configuraciones XML limpias y validadas con los valores predeterminados oficiales de fábrica.

#### Exportación e importación de configuraciones portátiles

Para migrar su configuración en varias Mac o crear una copia de seguridad externa: 

- **Exportar**: elija **Configuración ➔ Exportar configuración...** (comando **`cm_ExportConfiguration`**) para guardar una instantánea consolidada `.zip` o `.xml` que contenga sus teclas de acceso rápido, columnas, pestañas favoritas y paletas de colores. 
- **Importar**: elija **Configuración ➔ Importar configuración...** (comando **`cm_ImportConfiguration`**) en su máquina de destino para restaurar la configuración al instante. 

---

### 3.4 Teclas de función que activan el brillo/volumen de macOS en lugar de comandos

#### Causa principal

De forma predeterminada, los teclados Apple (teclados integrados de MacBook, teclados Magic) asignan funciones de hardware especiales a la fila superior de teclas: 

- `F1` / `F2`: Brillo de pantalla hacia abajo / hacia arriba 
- `F3`: Control de misión 
- `F4`: Destacado/Plataforma de lanzamiento 
- `F7` / `F8` / `F9`: controles de reproducción multimedia (rebobinar, reproducir/pausar, avance rápido) 
- `F10` / `F11` / `F12`: Silenciar audio, bajar volumen, subir volumen 

Cuando presiona `F5` con la esperanza de copiar un archivo, macOS intercepta la pulsación de tecla y no hace nada (o ajusta la iluminación del teclado).

#### Solución 1: utilice el acorde modificador `Fn`

Mantenga presionada la tecla **`Fn`** (Función) o **Globo (`🌐`)** en la esquina inferior izquierda de su teclado mientras presiona la tecla de función: 

- **`Fn+F3`**: Listador universal (`cm_View`) 
- **`Fn+F4`**: Editor de texto (`cm_Edit`) 
- **`Fn+F5`**: Copiar archivos (`cm_Copy`) 
- **`Fn+F6`**: Mover/Renombrar archivos (`cm_Rename`) 
- **`Fn+F7`**: Crear nueva carpeta (`cm_MakeDir`) 
- **`Fn+F8`**: Eliminar a la Papelera (`cm_Delete`) 
- **`Fn+Shift+F12`**: Sincronizar directorios (`cm_SyncDirs`)

#### Solución 2: habilite las teclas de función estándar en todo el sistema en la configuración de macOS

Si usa ATBCmder con regularidad, la configuración recomendada es configurar macOS para que trate las teclas de función como teclas estándar `F1`-`F12`: 

1. Abra **Configuración del sistema** (menú Apple  ➔ Configuración del sistema). 
2. Seleccione **Teclado** en la barra lateral izquierda. 
3. Haga clic en el botón **Atajos de teclado...**. 
4. Seleccione **Teclas de función** en la lista izquierda de la hoja modal. 
5. Encienda el interruptor de palanca: 
**"Utilice las teclas F1, F2, etc. como teclas de función estándar"** 

6. Haga clic en **Listo**. 

```
┌─────────────────────────────────────────────────────────────┐
│  Atajos de teclado                                          │
├──────────────────────────────┬──────────────────────────────┤
│  Navegación por teclado      │  Usar teclas F1, F2 como     │
│  Teclas de modificación      │  función estándar        [SÍ]│
│  Teclas de función      ◄─── │                              │
│  Spotlight                   │  Con esta opción activa,     │
│  Mission Control             │  pulse Fn para usar las      │
│  Atajos de la app            │  funciones especiales        │
│                              │  impresas en cada tecla.     │
│                              │                    [ Listo ] │
└──────────────────────────────┴──────────────────────────────┘
```
 

*Resultado*: Al presionar `F5` ahora se activa directamente Copiar en ATBCmder. Para ajustar el brillo o el volumen, mantenga presionada `Fn` mientras presiona la tecla.

#### Solución 3: utilice equivalentes de claves nativas de macOS `Cmd`

Si prefiere no cambiar la configuración del teclado del sistema, ATBCmder proporciona atajos de teclado nativos de macOS para cada operación principal: 

- **Copia**: `Cmd+C` / `Cmd+V` (o estándar `F5`) 
- **Mover**: `Cmd+C` ➔ `Cmd+Option+V` (`⌥⌘V` mover y pegar) 
- **Eliminar**: `Cmd+Delete` (`⌘⌫`) 
- **Nueva carpeta**: `Shift+Cmd+N` (`⇧⌘N`) 
- **Cambiar nombre**: `F2` o `Return` 
- **Cambio de nombre múltiple por lotes**: `Ctrl+M` (`⌃M`) o `Cmd+M` (`⌘M`) 
- **Preferencias**: `Cmd+,` (`⌘,`) 
- **Cerrar pestaña**: `Cmd+W` (`⌘W`) 

---

### 3.5 Mover archivos entre diferentes unidades frente a la misma unidad

Una pregunta frecuente de los usuarios es por qué mover un archivo de 20 GB dentro de la misma carpeta toma una fracción de segundo, mientras que mover el mismo archivo a una unidad externa o a un recurso compartido de red demora varios minutos.

#### Mover dentro del volumen (misma unidad/partición APFS)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      MOVER EN EL MISMO VOLUMEN (EN MILISEGUNDOS)                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Origen: /Users/brain/Downloads/BigFile.iso ➔ Destino: /Users/brain/Movies/           │
│                                                                                        │
│   1. La llamada POSIX rename() solo actualiza la tabla de inodos del directorio.       │
│   2. Los bloques de datos físicos en el SSD NUNCA se leen ni se copian.                │
│   3. Tiempo de ejecución: < 5 milisegundos. Espacio libre requerido: 0 bytes.          │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

Cuando las rutas de origen y destino residen en el **mismo volumen físico del sistema de archivos**, ATBCmder emite una llamada al sistema POSIX atómica `rename()`. El sistema operativo simplemente actualiza las entradas del puntero en el catálogo de directorios del sistema de archivos. Los grupos de datos físicos de su SSD no se mueven.

#### Movimiento entre volúmenes (diferentes unidades/particiones/montajes de red)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   MOVER ENTRE VOLÚMENES DIFERENTES (FLUJO DE DATOS)                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Origen: /Users/brain/Downloads/BigFile.iso ➔ Destino: /Volumes/ExternalSSD/Movie/    │
│                                                                                        │
│   Fase 1: Copia de flujo binario (Lectura del SSD interno ➔ Escritura en SSD externo)  │
│   Fase 2: Verificación y volcado (fsync garantiza la escritura física en el medio)     │
│   Fase 3: Eliminación segura del origen (el archivo origen se borra solo tras el éxito)│
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

Al realizar transferencias a través de diferentes límites de sistemas de archivos (por ejemplo, desde su SSD interno de Mac a una unidad USB externa, un recurso compartido SMB de red o una imagen de disco), una actualización del puntero atómico es físicamente imposible. ATBCmder ejecuta una canalización **Copiar-Verificar-Eliminar** de varias etapas: 

1. **Lectura/escritura de flujo binario**: los datos se transmiten en fragmentos desde el controlador de almacenamiento de origen a través de la memoria del sistema y se escriben en el controlador de almacenamiento de destino. La duración de la transferencia depende completamente de la velocidad del bus físico (por ejemplo, USB 3.0 a ~100 MB/s frente a Thunderbolt 4 a ~2800 MB/s). 
2. **Vaciado y verificación del búfer**: ATBCmder llama a `fsync()` en el identificador del archivo de destino para garantizar que todos los datos almacenados en caché se hayan escrito en medios físicos y verifica la equivalencia del recuento de bytes. 
3. **Eliminación segura del origen**: solo después de que el archivo de destino se haya escrito y verificado por completo, ATBCmder elimina el archivo de origen del disco original.

#### Implicaciones críticas y garantías de seguridad

* **Requisito de espacio libre**: la unidad de destino **debe tener suficiente capacidad libre** para almacenar la carga útil completa del archivo *antes* de que comience la operación. Si intenta mover un archivo de 30 GB a una unidad externa con solo 10 GB libres, la transferencia fallará. 
* **Garantía de pérdida cero de datos**: si una unidad externa se desconecta accidentalmente, o si el almacenamiento de destino se queda sin espacio durante la transferencia, ATBCmder cancela inmediatamente la operación, deja el archivo de origen **completamente intacto e ileso**, elimina cualquier archivo de destino parcial e informa un cuadro de diálogo de error claro. 
* **Monitoreo de cola en segundo plano (`cm_OperationsPanel`)**: los movimientos de volúmenes cruzados de larga duración se ejecutan en subprocesos de trabajo en segundo plano asíncronos (`FileOpWorker`). Puede monitorear las velocidades de transferencia en tiempo real, los tiempos restantes, pausar/reanudar transferencias o poner en cola operaciones posteriores sin bloquear la interfaz de usuario. 

---

### 3.6 Preguntas frecuentes adicionales

#### P1: ¿Cómo cambio el enfoque entre los paneles izquierdo y derecho?

Presione la tecla **`Tab`** (`⇥`). Focus alterna instantáneamente entre las tablas de archivos activos e inactivos. El panel activo muestra un borde resaltado y un texto de barra de estado enfocado.

#### P2: ¿Cómo cambio el contenido de los paneles izquierdo y derecho?

Presione **`Ctrl+U`** (`⌃U`) o ejecute el comando **`cm_Exchange`**. Los directorios, pestañas de carpetas y posiciones del cursor de los paneles izquierdo y derecho se intercambian instantáneamente. Para igualar los anchos de los paneles a una división exacta de 50/50, haga doble clic en cualquier lugar de la barra divisoria vertical central.

#### P3: ¿Cómo selecciono archivos usando patrones comodín?

Presione la tecla **`+`** en su teclado (o elija **Marcar ➔ Seleccionar grupo...** / `cm_MarkPlus`). Introduzca un patrón comodín como `*.pdf` o `photo_2026_*.jpg`. Para anular la selección de archivos que coincidan con un patrón, presione la tecla **`-`** (`cm_MarkMinus`). Para invertir su selección actual, presione **`*`** (`cm_MarkInvert`).

#### P4: ¿Cómo puedo alternar la visibilidad de los archivos de puntos ocultos?

Presione **`Cmd+H`** (`⌘H`) o **`Cmd+Shift+Period`** (`⇧⌘.`), o ejecute el comando **`cm_ShowSysFiles`**. Los archivos ocultos de Unix (archivos que comienzan con un punto, como `.zshrc`, `.gitignore`, `.env`) alternan inmediatamente entre los estados visible y oculto.

#### P5: ¿Cómo abro una ventana de Terminal de macOS en el directorio actual?

Presione **`Ctrl+J`** (`⌃J`) o ejecute el comando **`cm_RunTerm`**. ATBCmder genera una nueva sesión de macOS Terminal (o iTerm2) con su directorio de trabajo actual configurado en la ruta exacta de su panel de archivos activo.

#### P6: ¿ATBCmder es compatible con Mac Intel (x86_64)?

Actualmente, ATBCmder está compilado de forma nativa y exclusiva para Mac **Apple Silicon (M1/M2/M3/M4, arquitectura ARM64)** para aprovechar al máximo la memoria unificada de Apple, la aceleración de hardware Metal y los subsistemas Neural Engine. **Las Mac Intel (x86_64) no son compatibles en este momento.** 

---

## 4. Consejos profesionales y lista de verificación de mantenimiento del sistema

Para que ATBCmder siga funcionando a su máxima velocidad en todos los flujos de trabajo empresariales: 

- **Mantenimiento de caché semanal**: si navega con frecuencia por tarjetas de cámara de alta resolución, borre periódicamente los cachés de miniaturas temporales a través de **Configuración ➔ Opciones ➔ Miniaturas ➔ Borrar caché de miniaturas** para recuperar espacio en el disco. 
- **Auditoría de llavero**: si rota contraseñas en servidores SFTP o SMB remotos, actualice sus credenciales en ATBCmder a través de **Red ➔ Administrar conexiones de red...**. Editar y guardar actualiza el elemento de credencial correspondiente en su llavero macOS sin problemas. 
- **Optimización de la cola en segundo plano**: para transferencias de varios gigabytes en redes de 1 Gbps o 10 Gbps, ajuste los tamaños del búfer de fragmentos en **Configuración ➔ Opciones ➔ Operaciones de archivos** para maximizar la saturación del bus. 
- **Conservar permisos UNIX**: al copiar scripts o archivos binarios compilados entre unidades APFS de macOS, asegúrese de que **Conservar atributos y permisos de archivos** esté marcado en el cuadro de diálogo Copiar (`F5`), manteniendo los indicadores de ejecución (`chmod +x`) automáticamente. 

--- 

<div align="center"> 
<p><strong>ATBCmder Guía del usuario y portal de documentación</strong></p> 
<p> 
<a href="index.md">&larr; Volver al Portal de Documentación</a> &nbsp;&bull;&nbsp; 
<a href="getting_started.md">Capítulo 1: Fundamentos</a> &nbsp;&bull;&nbsp; 
<a href="keyboard_shortcuts.md">Capítulo 8: Atajos</a> &nbsp;&bull;&nbsp; 
<a href="download.md">Capítulo 10: Descarga e instalación →ATB_HTML_00013__ 
</p> 
</div>