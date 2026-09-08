# Capítulo 10: Descarga e instalación

¡Gracias por su interés en ATBCmder! Ofrecemos dos métodos diferentes de descarga e instalación para satisfacer sus necesidades. 

> [!IMPORTANT] 
> **Requisitos de sistema y arquitectura** 
> 
> - **Sistema operativo**: macOS 12.0 (Monterey) o posterior (incluidos macOS 13 Ventura, macOS 14 Sonoma y macOS 15 Sequoia). 
> - **Arquitectura de hardware compatible**: **Apple Silicon (M1/M2/M3/M4, ARM64)**. 
> - **Compatibilidad Intel (x86_64)**: Las Mac basadas en Intel **no son compatibles** en este momento.

## 1. Tienda de aplicaciones de Mac (recomendada)

Esta es la forma recomendada de instalar ATBCmder. **¡ATBCmder ya está disponible oficialmente en Mac App Store!** La descarga a través de la Mac App Store oficial le garantiza obtener actualizaciones automáticas sin interrupciones, protección nativa de entorno aislado de macOS y la mejor integración del sistema. 

- **Mac App Store**: [Descargar ATBCmder en Mac App Store](https://apps.apple.com/app/atbcmder/id6792398333)

## 2. Descarga del instalador DMG

Si no puede acceder a Mac App Store o prefiere las descargas directas, le proporcionamos un paquete de instalación de DMG independiente creado de forma nativa para Apple Silicon (ARM64). 

- **Enlace de descarga de DMG**: [Haga clic aquí para descargar ATBCmder DMG](https://storage.aitobox.com/@s/bNAshV6G/ATBCmder) *(solo Apple Silicon / ARM64)* 

*Nota: Al instalar a través de DMG, las funciones de seguridad de macOS pueden requerir que permita explícitamente la aplicación en "Configuración del sistema > Privacidad y seguridad" la primera vez que la abra. No se admiten Mac Intel (x86_64).*

### ⚠️ Otorgar acceso completo al disco

ATBCmder es una herramienta de administración de archivos y requiere permisos explícitos de administración de disco por parte del usuario. Siga estos pasos: 

1. Haga clic en el ícono de Apple en la esquina superior izquierda de su pantalla y seleccione **Configuración del sistema** (o "Preferencias del sistema" en versiones anteriores de macOS). 
2. Navegue hasta **Privacidad y seguridad** en el menú izquierdo o derecho. 
3. Desplácese hacia abajo y seleccione **Acceso total al disco**. 
4. Busque la aplicación (**ATBCmder**) en la lista y mueva el interruptor para encenderla. Si la aplicación no está en la lista, haga clic en el botón **+** en la parte inferior para agregarla manualmente. 
5. El sistema le pedirá que ingrese su contraseña de inicio de sesión de Mac o use Touch ID para confirmar los cambios.

## Notas de la versión

### 1.7.0 (2026-09-06)

- Universal File Viewer y Office Preview Suite: se agregaron motores de vista previa nativos para hojas de cálculo de Excel (con carga virtual diferida), documentos de Word (con paginación y representación de imágenes incrustadas) y presentaciones de PowerPoint (vista de tarjeta de diapositivas); se agregaron vistas previas para bases de datos SQLite, Markdown (con TOC), Jupyter Notebooks, fuentes, archivos, audio y EML; Implementado desplazamiento infinito de transmisión instantánea para archivos de texto grandes. 
- Visor de diferencias de archivos lado a lado: herramienta de comparación bidireccional integrada estilo vimdiff con resaltado de diferencias a nivel de caracteres, copia de fragmentos, edición en vivo, deshacer/rehacer y preservación de codificación. 
- Motor de búsqueda de archivos avanzado: subsistema de búsqueda reescrito con coincidencia de subcadenas difusa predeterminada, compatibilidad con expresiones regulares y un modo de pestaña "Alimentar al cuadro de lista"; La limitación de la interfaz de usuario por lotes elimina las congelaciones de la interfaz de usuario en resultados de búsqueda masivos 
- Operaciones de archivos y refuerzo de la interfaz de usuario: se corrigieron mensajes de sobrescritura duplicados durante movimientos entre dispositivos y bloqueos en la cola de transferencia; se agregaron marcas de tiempo de creación de archivos en el cuadro de diálogo de propiedades; barra de herramientas central vertical habilitada de forma predeterminada e indicadores visuales del panel activo refinados

### 1.6.2 (2026-09-03)

- Selección e interacción de arrastre con banda elástica: se agregó selección de arrastre con banda elástica del mouse tanto en la vista de tabla de archivos como en la vista de miniaturas, además de hacer clic en el espacio vacío para anular la selección de todos. 
- Tecla de acceso directo de ventana global y entrada de acceso directo: se agregó una tecla de acceso rápido global configurable para mostrar/ocultar la ventana de la aplicación; Entrada fija de combinaciones de modificadores de 4 teclas en la configuración de teclas de acceso rápido. 
- Solución de restauración de bandeja y base de macOS: se resolvió un problema por el cual hacer clic en el icono de base mientras estaba minimizado en la bandeja podía no restaurar la ventana principal o mostrar un marco en blanco. 
- Mejoras en el endurecimiento y la estabilidad del núcleo: se corrigieron posibles fallas de segmento del ciclo de vida, se fortalecieron los backends de VFS y se estabilizaron los conjuntos de prueba y desmontaje de subprocesos.

### 1.6.1 (2026-08-27)

- Revisión integral de UI/UX de macOS: basada en Apple HIG con paletas claras/oscuras refinadas, contraste de resaltado del panel estilo Finder, información sobre herramientas de tarjetas nativas y animaciones de control segmentadas suaves 
- Motor de íconos vectoriales y widgets modernos: se agregó un generador de íconos vectoriales independiente de la resolución inspirado en SF Symbols y barras de unidad, rutas de navegación y cuadros combinados modernizados 
- Interacción y diseño pulido: cambio de nombre múltiple rediseñado con un diseño de 2 columnas y detección de colisiones de nombres en tiempo real; La vista en miniatura admite `Cmd + Wheel` zoom dinámico; Se agregaron vistas unificadas de estado vacío.

### 1.6.0 (27/08/2026)

- Canal de distribución dual: se establecieron flujos de trabajo de compilación automatizados separados diseñados para la distribución independiente de DMG y el lanzamiento de Mac App Store (MAS). 
- Cumplimiento de la política de la App Store: ajusta dinámicamente los menús de la interfaz de usuario en las compilaciones MAS eliminando elementos de verificación de actualizaciones externas para cumplir estrictamente con las pautas de revisión de Apple, al tiempo que conserva las comprobaciones de actualización manuales en las compilaciones DMG. 
- `itms-services` Binary Patcher: se agregó un escáner binario automatizado y un parche seguro para eliminar cadenas de protocolo privadas en artefactos compilados de PySide6/Qt, lo que garantiza una validación automatizada impecable de App Store Connect.

### 1.5.6 (22/08/2026)

- Modos de vista independientes por pestaña: cada pestaña ahora conserva su propio diseño de vista independiente (vista plana/modo de árbol), sincroniza automáticamente el estado del menú y persiste sin problemas durante las restauraciones de la sesión. 
- Apertura inteligente de archivos y respaldo del sistema: se agregó un detector de tipo de archivo multicapa (bytes mágicos/MIME/extensión) para abrir medios y documentos compatibles en el visor/editor integrado mientras recurre limpiamente a las aplicaciones predeterminadas del sistema operativo para archivos no compatibles.

### 1.5.5 (2026-08-21)

- Optimización de la política de verificación de actualizaciones: comprobaciones de actualización automáticas deshabilitadas al iniciar la aplicación de forma predeterminada; Las actualizaciones ahora se pueden verificar manualmente a través de `Help` -> `Check for Updates...`, lo que mejora la velocidad de inicio y la privacidad fuera de línea.

### 1.5.4 (2026-08-21)

- Enfoque del panel y pulido de selección: se corrigieron los contornos de enfoque persistentes en los paneles divididos inactivos al cambiar de panel; lógica de reinicio de selección mejorada después de mover archivos entre paneles para evitar operaciones accidentales

### 1.5.3 (2026-08-19)

- Pulido de submenús en cascada con ruta de navegación: alineó con precisión la posición vertical de los menús de subcarpetas en cascada con la fila resaltada, eliminando los saltos de diseño y suavizando el recorrido profundo de las carpetas.

### 1.5.2 (2026-08-19)

- Solución de notas de lanzamiento y de inicio: se solucionó un problema por el cual el cuadro de diálogo de Notas de lanzamiento aparecía repetidamente en cada inicio de la aplicación; manejo de respaldo predeterminado mejorado `Config.get` para garantizar que las notas de la versión solo aparezcan en el lanzamiento inicial o en las actualizaciones de versión

### 1.5.1 (2026-08-19)

- Notas de la versión multilingüe: se agregaron 7 nuevas notas de la versión en idiomas principales (zh_TW, ja, ko, de, fr, ru, es) con descubrimiento dinámico y respaldo jerárquico de 5 niveles. 
- Polaco de firma y compilación de código de macOS: secuencias de comandos de empaquetado refactorizadas con orientación binaria Mach-O y envoltorios de reintento de marca de tiempo, lo que elimina fallas de firma y limitaciones

### 1.5.0 (2026-08-17)

- Administrador de sesión global: persistencia de sesión implementada a nivel de aplicación que restaura sin problemas todas las pestañas del panel izquierdo/derecho, rutas, modos de visualización (plano/árbol), proporciones de paneles y límites de ventanas de varios monitores al reiniciar 
- Importación/exportación de configuraciones: se agregó exportación e importación ZIP con 1 clic para todas las configuraciones y datos de la aplicación, lo que agiliza la migración entre dispositivos. 
- Mejoras en el editor de imágenes: se agregó un cambio de tamaño de imagen personalizado con bloqueo de relación de aspecto y resoluciones preestablecidas rápidas

### 1.4.9 (2026-08-17)

- Editor de imágenes avanzado: se agregó recorte de imágenes, rotación fina, ajustes de filtro y un módulo de eliminación y pintura de marcas de agua con IA basado en OpenCV. 
- Visor de imágenes mejorado: soporte completo para GIF animados, zoom, panorámica, rotación, extracción de metadatos EXIF y modo de presentación de diapositivas. 
- Integración de búsqueda de Spotlight: Spotlight nativo de macOS profundamente integrado para búsqueda instantánea de archivos y navegación mejorada con enfoque en los resultados de búsqueda

### 1.4.8 (2026-08-16)

- Localización integral (i18n): auditoría completa y finalización de la traducción en la interfaz de usuario, el visor F3 y el editor F4, lo que mejora significativamente la localización de los reproductores multimedia y los componentes de vista previa. 
- Optimizaciones del visor F3: manejo mejorado de enlaces externos y lógica envolvente de búsqueda en el lector EPUB alternativo (SimpleEpubPanel); Simplificó la barra de herramientas del visor de PDF eliminando botones de rotación redundantes.

### 1.4.7 (2026-08-16)

- Mejoras en el reproductor multimedia: UI, UX y estabilidad significativamente mejoradas de los reproductores de audio y vídeo integrados 
- Refactorización del sistema de compilación: se cambió el nombre de `BUILD_EPUB` env flag a `BUILD_WEBENGINE` para reflejar con precisión el comportamiento del empaquetado. 
- Corrección de dependencias de empaquetado: se garantiza que `ebooklib` siempre esté incluido en compilaciones DMG livianas para el lector EPUB alternativo.

### 1.4.6 (2026-08-16)

- Lector de EPUB ligero (SimpleEpubPanel): se agregó un lector de EPUB alternativo sin WebEngine con navegación y búsqueda de capítulos, además de un argumento CLI `--epub-reader` para anular el motor predeterminado 
- Menús de ruta de navegación en cascada: se refactorizó el menú desplegable de ruta de navegación en un diseño desplazable de una sola columna con infinitos submenús en cascada, solucionando problemas de superposición y bloqueo del mouse.

### 1.4.5 (2026-08-15)

- Visor de código avanzado (F3): resaltado de sintaxis agregado (Pygments), seguimiento de archivos en vivo, búsqueda de expresiones regulares y números de línea 
- Editor de código avanzado (F4): Se agregó codificación dinámica/conversión EOL, guardado atómico seguro, sangría inteligente y buscar/reemplazar 
- Arrastrar y soltar externo global: arrastre archivos sin problemas, incluidos contenidos de archivos profundamente anidados, directamente al escritorio macOS o a editores de terceros (por ejemplo, VSCode)

### 1.4.4 (2026-08-15)

- Mejoras en la tipografía: aumento del tamaño de fuente en menús, botones, información sobre herramientas y diálogo de configuración para una mejor legibilidad 
- Correcciones de cambio de tamaño del cursor: se restauraron los cursores de cambio de tamaño del mouse que faltaban en los bordes de las ventanas, los divisores y los encabezados de las columnas de las tablas. 
- Correcciones en la interfaz de usuario de macOS: se resolvieron los fondos de selección negros en los menús desplegables y se corrigieron los desbordamientos de títulos en los cuadros de grupo

### 1.4.3 (2026-08-14)

- Nueva interfaz de usuario nativa de macOS (Aqua Blue Theme): presentada como el nuevo tema predeterminado, que incluye navegación interactiva con ruta de navegación (con desglose de subcarpetas en cascada), medidor de almacenamiento estilo Mac (desbordamiento de TB fijo) y selección de cápsulas redondeadas 
- Pulido profundo de la interfaz de usuario: diseño refinado del botón de cierre de pestañas, superposición fija del símbolo del sistema y fondos, divisores y bordes de paneles de la barra de herramientas unificados en todos los temas. 
- i18n y actualización de la aplicación: auditoría completa de cobertura del proyecto i18n; Se agregó compatibilidad con API compartida AList/OpenList en el módulo de actualización automática.

### 1.4.2 (2026-08-13)

- Filtro semántico de IA mejorado: admite el análisis de extensiones más comunes, formas plurales y está totalmente integrado con i18n 
- Semantic Search UX: se reemplazó el cursor de espera con QProgressBar y se mejoró el comportamiento de la tecla Intro para las finalizaciones. 
- Análisis semántico central: detección mejorada del tipo de destino y eliminación de palabras clave para una búsqueda en lenguaje natural más precisa

### 1.4.1 (2026-08-13)

- Revisión y refactorización integral del código base (Batches A-D) 
- Mejoras de seguridad: se corrigieron posibles vulnerabilidades de acceso y recorrido de ruta 
- Simultaneidad y rendimiento: seguridad mejorada de subprocesos en segundo plano y eficiencia de ejecución 
- Arquitectura: estabilidad mejorada y gestión de recursos en componentes centrales

### 1.4.0 (2026-08-12)

- Correcciones profundas de red VFS: compatibilidad con codificación múltiple, controladores de protocolo, montaje de archivos encadenados y resolución de conflictos 
- Módulo de actualización de aplicaciones mejorado: correcciones de verificación SSL, validación de descarga de DMG e integración de UI 
- UI de la nota de la versión: muestra el historial completo de versiones durante las actualizaciones automáticas

### 1.3.9 (2026-08-12)

- Se agregó un lector de EPUB incorporado (vista rápida F3) 
- Mecanismo de detección de actualización de aplicaciones implementado 
- Se corrigió la congelación del trabajador de VFS durante la resolución de conflictos de archivos.

### 1.3.8 (2026-08-08)

- Refinamiento de la interfaz de usuario de vista de árbol 
- Integración de red fsspec refactorizada 
- Manejo mejorado de caracteres de archivos no válidos.

### 1.3.7 (2026-08-06)

- Arquitectura VFS de red: revisión de los sistemas de archivos de red (FTP/WebDAV/SMB) usando `fsspec`, implementación de async `VfsTableModel`, streaming `StreamCopyWorker`, operaciones remotas de archivos (mkdir/rename/delete/overwrites) y visualización/edición remota F3/F4 
- Bandeja del sistema y teclas de acceso rápido: admite minimizar en la bandeja del sistema, acceso directo global (`Option+Cmd+H`), alternar ícono de Dock de macOS e integración de ícono de plantilla nativa
 - Configuración de LLM: introduzca el recurso `default_llm.xml` y el singleton para el filtrado semántico de IA y la interfaz de usuario de opciones 
- Mejoras en la navegación: admite accesos directos de navegación Re Pág / Av Pág / Inicio / Fin / Fn en paneles de archivos y ventanas emergentes de listas activas 
- Internacionalización: empaquete todos los mensajes de error de VFS, las etiquetas del panel de Vista rápida y las cadenas del menú de la bandeja con catálogos de traducción i18n.

### 1.3.6 (2026-08-04)

- Mejoras de Network VFS: agregue detección automática UTF-8/GBK, actualización dinámica de codificación de archivos MAKE, manejo de respaldo y restablecimiento de socket para FTP; resolver el tiempo de espera y responder desincronización 
- Correcciones de WebDAV y SMB: corrige la eliminación de la ruta raíz de WebDAV/SMB, la propagación del último error, la confiabilidad de la conexión, los íconos VFS y la visualización de títulos de pestañas 
- Navegación en miniatura: implemente una navegación fluida con flechas de cuadrícula 2D para la vista en miniatura 
- i18n y calidad de código: corrige traducciones corruptas de Cerrar pestaña en catálogos zh_CN/zh_TW y completa auditoría de optimización de la base de código

### 1.3.5 (2026-08-03)

- Panel de vista rápida: implemente la función Vista rápida (`cm_QuickView`, `Cmd+Q`/`Ctrl+Q`) que admite vistas previas multiformato, propiedades de archivos de respaldo, giro simétrico, integración de menú Mostrar e i18n completo 
- Widgets de vista rápida: agregue `QuickViewContainer` y `QuickViewPropertiesWidget` integrados en FilePanel 
- UI Polish: corrige la alineación del encabezado de la pestaña y los problemas de aplastamiento de la página del diálogo de opciones en el tema claro

### 1.3.4 (2026-08-02)

- Interfaz de usuario del panel de archivos: agregue selección por lotes Mayús+RePág/Mayús+AvPág en las vistas del panel de archivos 
- Operaciones de archivos: corrige defectos de copia F5 y movimiento de archivos/directorios F6 
- Cree scripts: establezca nombres de identidad de certificados exactos, agregue marcas de tiempo al diseño del código y maneje con elegancia el estado no válido de la certificación notarial

### 1.3.3 (2026-08-01)

- Transfer Engine: calcule la velocidad de transferencia precisa en tiempo real y ETA en ProcessTransferWorker 
- Permisos y zona de pruebas: verificaciones separadas de la zona de pruebas de macOS del flujo de detección de acceso total al disco 
- Scripts de compilación: actualice la configuración del script de compilación para las compilaciones firmadas 1.3.3 DMG

### 1.3.2 (2026-08-01)

- Subprocess Transfer Worker: soluciona el error de congelamiento/inicio en el modo de paquete independiente de la App Store de Nuitka 
- Habilidades del agente: agregue la verificación de auditoría de integridad de i18n a la habilidad de revisión de código, optimización y auditoría

### 1.3.1 (2026-08-01)

- macOS Sandbox: corrige el estado falso de 'Acceso total al disco concedido' causado por la verificación `os.access` 
- Tareas simultáneas: resuelve la conversación cruzada de estado para operaciones simultáneas en segundo plano. 
- i18n: agregue traducción al chino para la casilla de verificación por lotes en el cuadro de diálogo de eliminación permanente 
- Habilidades del agente: agregue y actualice la habilidad de auditoría de optimización de revisión de código

### 1.3.0 (2026-08-01)

- Motor de transferencia aislado de procesos: implemente ProcessTransferWorker y ProcessIOEngine para descargar archivos, copiar/mover E/S desde el subproceso de la interfaz de usuario. 
- Rendimiento de transferencia y capacidad de respuesta: limitación de velocidad IPC de 10 Hz, almacenamiento en búfer adaptativo y optimización de macOS `F_NOCACHE` para evitar la tartamudez de la GUI 
- Auditoría y refuerzo de código: refactorización de 4 fases que incluye bloqueos mutex de simultaneidad, refuerzo de seguridad y limpiezas de arquitectura. 
- Correcciones de interfaz de usuario: corrige el error de eliminación de Shiboken C++, el diseño del modo de panel horizontal y las señales indicadoras de progreso de tareas en segundo plano.

### 1.2.0 (2026-07-30)

- Implementar un grupo de procesos de E/S global (IoWorkerPool) para aislar las operaciones de E/S de archivos de bloqueo y evitar que la GUI se congele. 
- Control de versiones de configuración: lea/escriba app_version en el nodo raíz XML y agregue el registro del ejecutor de migración automatizado 
- Arrastrar y soltar/Portapapeles: integre el puente Finder nativo de macOS, las carpetas con resorte y la máquina de estado del portapapeles 
- Expansión de ruta: agregue la utilidad compartida `expand_path` que admita `~`, `$VAR`, `%VAR%` y `%COMMANDER_PATH%` 
- Lista activa: implementar HotlistConfig singleton independiente y configuración de lista activa predeterminada

### 1.1.0 (2026-07-29)

- Se corrigió el orden de entrada de las notas de la versión para garantizar una clasificación cronológica inversa debajo del encabezado de la Nota de la versión. 
- Se corrigió el script del administrador de versiones para admitir el nodo XML System/LastVersion en default_config.xml 
- Teclas de acceso rápido: agregue accesos directos predeterminados Meta+Tab y Meta+Shift+Tab para la navegación por pestañas 
- Pestañas favoritas: agregue migración automática y limpieza para pestañas favoritas heredadas desde la configuración principal 
- Visor de archivos: optimice el rendimiento de carga de archivos grandes y el uso de memoria

### 1.0.1 (22/07/2026)

> Solucionar el error de vista previa de texto F3 en entornos sandbox de App Store

### 1.0.0 (2026-07-18)

> Implementación inicial del puerto Python de TotalCommander.