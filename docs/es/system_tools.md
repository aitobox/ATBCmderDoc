# Capítulo 7: Herramientas del sistema y mantenimiento

Un administrador de archivos profesional no opera en el vacío: es el centro neurálgico para su almacenamiento, memoria y recursos del sistema operativo. Si bien la gestión de archivos tradicional de doble panel destaca a la hora de organizar, mover y sincronizar jerarquías de directorios, los usuarios avanzados, desarrolladores y administradores de sistemas se enfrentan con frecuencia a retos a nivel de sistema: detectar con precisión qué directorio oculto ha consumido silenciosamente 50 GB de espacio en disco, identificar un proceso descontrolado en segundo plano que satura los núcleos de la CPU, limpiar gigabytes de cachés de desarrollo y artefactos de compilación abandonados, y desinstalar por completo aplicaciones heredadas de macOS sin dejar archivos de preferencias huérfanos, daemons de inicio o carpetas de soporte de aplicaciones dispersas por `~/Library/`.

ATBCmder integra cuatro herramientas especializadas de diagnóstico y mantenimiento del sistema directamente en el menú **Herramientas**. Impulsadas por un daemon de monitorización nativo y asíncrono, estas herramientas funcionan a la perfección junto a sus paneles de archivos sin bloquear la interfaz de usuario ni requerir aplicaciones de utilidades pesadas de terceros repletas de publicidad.

---

## 1. Inicio rápido visual: herramientas del sistema y HUD de estado

ATBCmder divide el mantenimiento del sistema en cuatro instrumentos operativos fundamentales, acompañados de una cápsula de monitorización siempre visible en la barra de herramientas:

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

### Matriz de atajos de herramientas del sistema de matriz dual

| Herramienta / Acción | Atajo de macOS | Tecla Commander clásica | ID de comando | Ubicación en el menú |
| :--- | :--- | :--- | :--- | :--- |
| **Panel de estado del sistema** | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` | **Herramientas ➔ Estado del sistema...** |
| **Analizador de uso de disco** | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` | **Herramientas ➔ Analizador de uso de disco...** |
| **Limpiador del sistema** | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` | **Herramientas ➔ Limpiador del sistema...** |
| **Desinstalador de aplicaciones** | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` | **Herramientas ➔ Desinstalar aplicación...** |
| **Alternar cápsula de estado** | Preferencias ➔ General | — | *(Configuración)* | **Configuración ➔ Opciones ➔ General** |

---

## 2. HUD de cápsula de estado en la barra de herramientas y ventana emergente interactiva

ATBCmder incluye una **cápsula de estado del sistema** integrada directamente en el extremo derecho de la barra de herramientas principal. Esto proporciona una supervisión periférica e inmediata del estado del sistema sin obligarle a cambiar a Monitor de Actividad ni a abrir una ventana independiente de Terminal.

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

### 2.1 Componentes de la cápsula y estilo visual

La cápsula de estado (de `320px` de ancho) muestra tres métricas de telemetría en tiempo real actualizadas una vez por segundo:

1. **Uso de CPU**: Porcentaje de uso global del procesador en tiempo real con código de colores dinámico:
   - **Normal (< 75%)**: Azul de énfasis / color frontal del tema.
   - **Elevado (75% – 90%)**: Naranja de advertencia.
   - **Crítico (> 90%)**: Rojo de alerta.
2. **Uso de memoria (RAM)**: Presión de memoria activa y conectada (wired) actual expresada como un porcentaje de la memoria RAM física.
3. **Rendimiento de red**: Velocidades de subida y bajada agregadas en tiempo real a través de todos los adaptadores de red activos, presentadas en un formato compacto (por ejemplo, `↓2.4 MB/s ↑512 KB/s`).

### 2.2 Ventana emergente interactiva (`StatusPopup`)

Al hacer clic en cualquier parte de la cápsula de estado se abre una **ventana emergente de estado** flotante y no modal:

- **Telemetría de hardware**: Permite ver los porcentajes combinados de CPU, memoria, GPU y estado de la batería (incluyendo el porcentaje de carga y el estado de conexión al cargador).
- **Puntos de montaje del sistema de archivos**: Muestra una lista de todos los contenedores APFS locales montados y unidades externas con barras de espacio libre y capacidad total.
- **Los 5 procesos principales**: Destaca los cinco procesos con mayor consumo de recursos ordenados por porcentaje de CPU y huella de memoria.
- **Botón de diagnóstico detallado**: Haga clic en **"Abrir monitor completo del sistema"** (o presione `⌘⇧M`) para abrir la ventana completa de diagnóstico.

### 2.3 Configuración de la visibilidad de la cápsula

Si prefiere una barra de herramientas despejada con controles exclusivos para la navegación de archivos:

1. Abra **Preferencias** (`⌘,` / **Configuración ➔ Opciones...**).
2. Seleccione **General** en la barra lateral izquierda.
3. En la sección **Visualización y diseño**, marque o desmarque la casilla:
   `[X] Show system status capsule on toolbar`
4. Haga clic en **Aplicar** u **Aceptar**. La cápsula aparecerá o desaparecerá de inmediato de la barra de herramientas principal.

---

## 3. Estado del sistema y diagnósticos (`cm_SystemStatus` / `⌘⇧M`)

Al presionar **`⌘⇧M`** (o **`Ctrl+Shift+M`**) se abre el **panel de estado del sistema** completo. Esta utilidad funciona como una consola de diagnóstico integrada diseñada a medida para administradores de sistemas, desarrolladores y resolución de problemas de rendimiento.

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

### 3.1 Funciones de diagnóstico y secciones de métricas

1. **Monitor de procesador multinúcleo**:
   - Visualiza la carga general del sistema y el desglose individual entre núcleos de rendimiento (Performance) y de eficiencia (Efficiency).
   - Los indicadores de progreso por núcleo permiten advertir la saturación de los procesadores durante compilaciones o renderizados multiproceso.
2. **Desglose de memoria y presión de intercambio (Swap)**:
   - Clasifica la asignación de memoria física en memoria de aplicaciones (App Memory), memoria fija (Wired Memory), memoria comprimida y archivos en caché.
   - Supervisa el uso del espacio de intercambio virtual (swap) para ayudar a identificar fugas de memoria que provocan paginación excesiva en el disco.
3. **Resumen de almacenamiento y puntos de montaje**:
   - Métricas de rendimiento de lectura y escritura de disco en tiempo real junto con datos de capacidad de los puntos de montaje.
4. **Administrador interactivo de procesos**:
   - Tabla ordenable en tiempo real que enumera todas las tareas del sistema y del usuario en ejecución.
   - **Búsqueda y filtrado**: Escriba cualquier nombre de proceso o PID en el cuadro de búsqueda para filtrar los resultados de forma instantánea.
   - **Terminación de procesos**:
     - Haga clic en **Kill** o seleccione un proceso y presione `Delete` (o `Supr`).
     - Muestra un cuadro de diálogo de confirmación que ofrece **Terminar (`SIGTERM`)** para un cierre ordenado o **Forzar salida (`SIGKILL`)** para tareas que no responden.

---

## 4. Analizador de uso de disco (`cm_DiskUsageAnalyzer` / `⌘⇧D`)

Cuando una unidad de estado sólido (SSD) empieza a quedarse sin espacio libre, averiguar dónde se esconden los gigabytes de datos puede resultar una tarea dolorosamente lenta. Las listas de archivos estándar de Finder no calculan automáticamente el tamaño de las carpetas, y la inspección manual requiere descender laboriosamente a través de niveles jerárquicos anidados.

El **Analizador de uso de disco** (`cm_DiskUsageAnalyzer`, atajo de teclado **`⌘⇧D`** / **`Ctrl+Shift+D`**) examina árboles de directorios completos de forma asíncrona mediante un motor de escaneo multiproceso y visualiza su almacenamiento tanto en una lista de árbol jerárquica clásica como en un mapa de árbol interactivo rectangular (**Squarified Treemap**).

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

### 4.1 Arquitectura clave y capacidades

- **Escaneo asíncrono multiproceso**: Examina cientos de miles de archivos en contenedores APFS sin bloquear la interfaz principal de ATBCmder. Una barra de progreso muestra la tasa de directorios escaneados por segundo.
- **Visualización mediante mapa de árbol rectangular (Squarified Treemap)**:
  - Las carpetas y archivos se representan como bloques rectangulares anidados cuya superficie bidimensional es estrictamente proporcional a su tamaño en disco.
  - Los colores reflejan de manera automática la profundidad del directorio, lo que permite identificar a simple vista qué elementos están consumiendo más espacio de almacenamiento.
- **Sincronización bidireccional**:
  - Al seleccionar un elemento en el árbol de directorios, se resalta su bloque correspondiente en el mapa de árbol.
  - Al hacer clic en cualquier rectángulo del mapa de árbol, se resalta la fila en la vista de árbol y se muestra la ruta de archivo completa junto con el tamaño exacto en bytes.

### 4.2 Navegación interactiva y flujos de trabajo

1. **Profundizar (Drill Down)**: Haga doble clic en cualquier fila de carpeta o bloque del mapa de árbol para hacer zoom en ese subdirectorio y recalcular la vista en relación con la nueva raíz.
2. **Alejar (Zoom Out)**: Haga clic en el botón **Zoom Out** en la barra de herramientas o haga clic en cualquier segmento de la barra de ruta (breadcrumbs) en la parte superior para regresar a los directorios superiores.
3. **Inspeccionar en los paneles dobles**: Haga clic en **Mostrar en el panel doble** para navegar de inmediato en su panel activo de ATBCmder hasta el directorio seleccionado.
4. **Limpieza instantánea**: Seleccione cualquier carpeta o archivo grande obsoleto y presione **`⌘⌫`** (o haga clic en **Mover a la Papelera**). El elemento se envía de forma segura a la Papelera de macOS y el árbol del escaneo se actualiza automáticamente.
5. **Exportar informes de almacenamiento**: Haga clic en **Exportar** para generar auditorías integrales de uso del disco formateadas como CSV estructurado o resúmenes de texto sin formato para su planificación de almacenamiento.

---

## 5. Limpiador del sistema (`cm_CleanSystem` / `⌘⇧C`)

A lo largo de meses de uso diario, macOS acumula gigabytes de datos temporales: cachés obsoletas de aplicaciones, artefactos de compilación de Xcode, descargas de gestores de paquetes, registros de diagnóstico huérfanos y cachés del navegador web. Aunque algunas cachés aceleran los flujos de trabajo, los elementos obsoletos desperdician un valioso espacio en unidades SSD de alta velocidad.

El **Limpiador del sistema** (`cm_CleanSystem`, atajo de teclado **`⌘⇧C`** / **`Ctrl+Shift+C`**) ofrece un sistema de limpieza determinista en dos etapas, diseñado con garantías de seguridad de nivel empresarial.

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

### 5.1 La arquitectura de seguridad en dos fases

A diferencia de los limpiadores imprudentes de "un solo clic" que eliminan archivos silenciosamente en segundo plano, ATBCmder aplica un estricto **protocolo de seguridad en dos fases**:

1. **Fase 1: Escaneo preliminar y evaluación (Dry-Run)**:
   - El limpiador realiza una inspección de solo lectura en las ubicaciones estandarizadas del sistema.
   - Calcula la cantidad exacta de archivos y los tamaños en bytes sin modificar ni eliminar un solo byte.
   - Agrupa los resultados en categorías transparentes con clasificaciones explícitas de riesgo.
2. **Fase 2: Eliminación selectiva revisada por el usuario**:
   - Usted revisa la lista categorizada y marca o desmarca elementos individuales o categorías completas.
   - Al hacer clic en **"Limpiar elementos seleccionados"**, la eliminación solo se ejecuta sobre los destinos seleccionados explícitamente.
   - Cada evento de eliminación se registra en un archivo de registro de auditoría atómico en `~/Library/Preferences/atbcmder/operations.log`.

### 5.2 Seis dominios principales de limpieza

| Categoría | Ubicación típica | Nivel de riesgo | Descripción |
| :--- | :--- | :---: | :--- |
| **Cachés de aplicaciones** | `~/Library/Caches/` | **Seguro** | Cachés obsoletas generadas por aplicaciones de escritorio que se vuelven a crear automáticamente cuando es necesario. |
| **Registros del sistema y de usuarios** | `~/Library/Logs/`, `/var/log/` | **Seguro** | Registros antiguos de fallos (crash logs), volcados de diagnóstico y registros de actualización de software que ya no son necesarios para la resolución de problemas. |
| **Cachés de navegadores** | Safari, Chrome, Edge, Firefox | **Seguro** | Páginas web en caché, búferes multimedia y artefactos de scripts en todos los navegadores web de escritorio instalados. |
| **DerivedData de Xcode** | `~/Library/Developer/Xcode/DerivedData` | **Advertencia** | Archivos de objetos intermedios, cachés de módulos y datos de indexación procedentes de compilaciones anteriores de desarrolladores de Apple. |
| **Cachés de gestores de paquetes** | Homebrew, CocoaPods, NPM, Yarn | **Advertencia** | Archivos tarball descargados, archivos de fórmulas y directorios de caché de paquetes. |
| **Papelera** | `~/.Trash`, `.Trashes` | **Peligro** | Elementos trasladados previamente a la Papelera de macOS que aún no se han vaciado de forma permanente. |

### 5.3 Niveles de riesgo y lista blanca de seguridad

- 🟢 **Seguro (Verde)**: Cachés temporales y metadatos descartados que se pueden eliminar sin pérdida de configuración ni interrupción del flujo de trabajo.
- 🟡 **Advertencia (Naranja)**: Artefactos de desarrollo o cachés de gestores de paquetes. Eliminarlos es seguro, pero la compilación posterior del proyecto o la descarga de paquetes tardará más mientras se vuelven a obtener los archivos.
- 🔴 **Peligro (Rojo)**: Contiene archivos que requieren confirmación explícita (por ejemplo, vaciar permanentemente la Papelera).
- **Reglas personalizadas de la lista blanca**:
  - Agregue rutas específicas, extensiones o nombres de carpetas que ATBCmder **nunca** deba tocar en `~/.config/atbsys/whitelist`.
  - Las reglas de protección integradas evitan automáticamente el escaneo de archivos críticos del sistema operativo macOS, directorios del llavero del usuario y carpetas de sincronización local de almacenamiento en la nube.

---

## 6. Desinstalador de aplicaciones (`cm_UninstallApp` / `⌘⇧U`)

En macOS, arrastrar una aplicación desde `/Applications` a la Papelera solo elimina el paquete `.app` en sí. Las aplicaciones modernas con frecuencia dispersan cientos de archivos auxiliares por su disco: archivos plist de preferencias, bases de datos en Application Support, agentes de inicio en segundo plano, contenedores aislados (sandboxes) y elementos multimedia en caché. Con el tiempo, estos residuos huérfanos consumen gigabytes de almacenamiento y pueden dejar procesos innecesarios ejecutándose en segundo plano al iniciar sesión.

El **Desinstalador de aplicaciones** (`cm_UninstallApp`, atajo de teclado **`⌘⇧U`** / **`Ctrl+Shift+U`**) proporciona un análisis profundo de dependencias para erradicar por completo las aplicaciones y todos sus residuos asociados.

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

### 6.1 Ubicaciones de detección de residuos

Al buscar componentes de aplicaciones, ATBCmder examina las siguientes ubicaciones estándar de los subsistemas de macOS mediante la coincidencia exacta del identificador de paquete (bundle identifier):

1. **Paquete de la aplicación**: `/Applications/<Nombre>.app` y `~/Applications/<Nombre>.app`.
2. **Soporte de aplicaciones (Application Support)**: `~/Library/Application Support/<Nombre>` y `<BundleID>`.
3. **Cachés de aplicaciones**: `~/Library/Caches/<BundleID>`.
4. **Preferencias y valores predeterminados**: `~/Library/Preferences/<BundleID>.plist`.
5. **Estado guardado (Saved State)**: `~/Library/Saved Application State/<BundleID>.savedState`.
6. **Daemons y agentes de inicio**: `~/Library/LaunchAgents/<BundleID>.plist`.
7. **Contenedores aislados (Sandbox)**: `~/Library/Containers/<BundleID>/` y `~/Library/Group Containers/`.
8. **Registros de aplicaciones**: `~/Library/Logs/<Nombre>/`.

### 6.2 Modos operativos duales

- **Desinstalación completa (predeterminado)**:
  - Diseñado para eliminar una aplicación instalada presente actualmente en su Mac.
  - Elimina tanto el paquete ejecutable `.app` de `/Applications` como todos los archivos de soporte auxiliares asociados en una única acción atómica.
- **Solo residuos**:
  - Diseñado para realizar limpieza tras aplicaciones que fueron eliminadas manualmente con anterioridad mediante Finder o herramientas de terceros.
  - Examina `~/Library/` en busca de carpetas de soporte huérfanas cuyo paquete `.app` principal ya no esté presente en el sistema.

### 6.3 Integridad del sistema de Apple y barreras de seguridad

Para evitar la desestabilización accidental del sistema:

- **Protección de aplicaciones del sistema**: Las aplicaciones integradas del sistema macOS (Safari, Finder, Vista Previa, Música, Ajustes del Sistema, etc.) están protegidas con un icono de candado de solo lectura y no se pueden desinstalar.
- **Detección de procesos en ejecución**: Si una aplicación o su daemon auxiliar está activo en ese momento, ATBCmder le solicitará que cierre la aplicación de forma ordenada antes de proceder con la desinstalación.
- **Protocolo de envío a la Papelera**: Todos los elementos desinstalados se envían a la Papelera de macOS de forma predeterminada en lugar de eliminarse de inmediato del disco, lo que permite una recuperación completa en caso de ser necesario.

---

## 7. Avisos sobre el sistema y mantenimiento

> [!NOTE]
> **Consumo mínimo de recursos del sistema**  
> El daemon del monitor de estado en segundo plano está desarrollado en código compilado nativo y se ejecuta con un intervalo de sondeo de 1,0 segundo. Consume menos del 0,1% de CPU durante la exploración activa de archivos y suspende automáticamente el sondeo cuando ATBCmder se minimiza o se oculta.

> [!TIP]
> **Combinación del analizador de uso de disco con la vista plana de ramas (Branch View) en doble panel**  
> Si el analizador de uso de disco detecta un directorio con miles de archivos temporales dispersos, seleccione ese directorio y presione **Mostrar en el panel doble**. Luego presione **`Cmd+B`** (`cm_DirBranch`) para aplanar todo el árbol anidado en una lista única donde podrá ordenar, seleccionar y eliminar elementos por lotes con total precisión de teclado.

> [!IMPORTANT]
> **Revise siempre las selecciones del limpiador antes de confirmar**  
> Aunque el limpiador del sistema califique las cachés como **Seguro (Verde)**, algunas herramientas de desarrollo (como DerivedData de Xcode o volúmenes locales de Docker) pueden requerir tiempo para recompilar o descargar paquetes en el siguiente inicio de proyecto. Revise las categorías marcadas para asegurarse de no vaciar cachés necesarias para su sprint actual de trabajo.

> [!CAUTION]
> **Forzar la detención de procesos del sistema (`SIGKILL`)**  
> En el administrador de procesos de estado del sistema, enviar `SIGKILL` (Forzar detención) detiene de inmediato el proceso de destino sin permitirle vaciar los búferes de archivos abiertos ni guardar el estado de los documentos. Intente siempre realizar primero una terminación ordenada con `SIGTERM`.

> [!WARNING]
> **Eliminación de contenedores aislados de aplicaciones (App Sandbox)**  
> Al desinstalar aplicaciones descargadas de Mac App Store, los archivos auxiliares almacenados en `~/Library/Containers/<BundleID>` suelen incluir bases de datos de documentos aislados en sandbox. Asegúrese de haber exportado cualquier archivo local de proyecto imprescindible antes de confirmar la eliminación del contenedor.

---

## 8. Tabla de referencia maestra de herramientas del sistema de matriz dual

| Categoría | Descripción de la acción | Atajo de macOS | Tecla Commander clásica | ID de comando |
| :--- | :--- | :--- | :--- | :--- |
| **Monitor del sistema** | Abrir el panel completo de diagnóstico del sistema | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` |
| **Monitor del sistema** | Abrir la ventana emergente de estado ligera | Clic en la cápsula de la barra de herramientas | — | *(Acción de UI)* |
| **Monitor del sistema** | Filtrar la lista del administrador de procesos | `Cmd+F` (en el panel) | `F7` | — |
| **Monitor del sistema** | Terminar proceso (`SIGTERM`) | `Delete` / `⌫` | `Delete` | — |
| **Monitor del sistema** | Forzar la detención del proceso (`SIGKILL`) | `Shift+Delete` / `⇧⌫` | `Shift+Delete` | — |
| **Analizador de disco** | Abrir el cuadro de diálogo del analizador de uso de disco | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` |
| **Analizador de disco** | Profundizar en la carpeta seleccionada | `Enter` / `Return` | `Enter` | — |
| **Analizador de disco** | Regresar al directorio superior | `Backspace` / `⌫` | `Backspace` | — |
| **Analizador de disco** | Mover el elemento resaltado a la Papelera | `Cmd+Delete` / `⌘⌫` | `F8` / `Delete` | — |
| **Analizador de disco** | Mostrar el elemento seleccionado en el panel doble | `Cmd+Return` / `⌘⏎` | `Ctrl+Enter` | — |
| **Limpiador del sistema** | Abrir el cuadro de diálogo del limpiador seguro del sistema | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` |
| **Limpiador del sistema** | Ejecutar escaneo de prueba de solo lectura (Dry Run) | `Cmd+R` / `⌘R` | `Ctrl+R` | — |
| **Limpiador del sistema** | Alternar selección de categoría | `Space` | `Space` | — |
| **Desinstalador de apps** | Abrir el desinstalador de aplicaciones | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` |
| **Desinstalador de apps** | Cambiar al modo de solo residuos | `Cmd+2` / `⌘2` | `Alt+2` | — |
| **Preferencias** | Alternar HUD de cápsula de estado en la barra de herramientas | Preferencias ➔ General | — | *(Configuración)* |

---

<div align="center">
  <p>¿Listo para personalizar atajos de teclado, vistas de panel y el comportamiento de la aplicación?</p>
  <p><strong><a href="preferences_and_customization.md">Continuar al Capítulo 8: Preferencias y personalización &rarr;</a></strong></p>
</div>
