# 第 8 章：終極快速鍵全書

ATBCmder 是一款為**純鍵盤高效操作**而生的雙面板檔案管理器。無論是日常檔案複製移動、跨目錄跳轉、檢視切換，還是批次重新命名與內容對比，完全無需觸碰滑鼠即可瞬間完成。

為了兼顧擁有數十年經驗的老牌 Commander 使用者習慣與蘋果 macOS 觸控原生人機工學，ATBCmder 獨創了**雙矩陣快速鍵架構**：幾乎每一項功能都同時繫結了**經典 Commander 功能鍵**（`F1`–`F12`、`Insert`、小鍵盤等）與 **macOS 原生組合修飾鍵**（`⌘` Command、`⌥` Option、`⇧` Shift、`⌃` Control）。

---

## 1. 雙矩陣設計哲學與按鍵符號速查

無論你習慣了 Norton Commander / Total Commander 傳承數十年的肌肉記憶，還是早已習慣原生 macOS Finder 的按鍵風格，ATBCmder 都能即開即用、完美契合，無需痛苦地重設鍵位。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          雙矩陣快捷鍵引擎架構                               │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  經典 COMMANDER 體系 (PC/經典習慣)     │  macOS 原生體系 (Mac 標準人機工學) │
│  • 以功能鍵為核心 (F1–F12)            │  • 以修飾組合鍵為核心 (⌘, ⌥, ⇧, ⌃)  │
│  • 專用小鍵盤標記快捷鍵 (+, -, *)    │  • 與 Finder 深度一致 (⌘C, ⌘V, ⌘⌫, ⏎)│
│  • 盲操盲打、極速響應                │  • 深度整合原生選單欄加速鍵          │
│  典型示例：                          │  典型示例：                          │
│    F5        ➔ 複製檔案到對側        │    ⌘C ➔ ⌘V   ➔ 複製檔案              │
│    F6        ➔ 移動檔案到對側        │    ⌘C ➔ ⌥⌘V  ➔ 剪下移動檔案          │
│    Shift+F4  ➔ 快速新建文字檔案      │    ⇧⌘4       ➔ 快速新建文字檔案      │
│    Alt+F7    ➔ 高階檔案搜尋          │    ⌥⌘F       ➔ 高階檔案搜尋          │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Apple 修飾鍵符號對照表

在本文件及 ATBCmder 的首選項配置視窗中，按鍵組合均採用 macOS 標準印刷體圖示表示：

| 符號 | 修飾鍵名稱 | PC / Windows 對應 | 說明 |
| :---: | :--- | :--- | :--- |
| **`⌘`** | **Command** (`Cmd`) | `Win` / `Ctrl` | macOS 最主要的操作主鍵 |
| **`⌥`** | **Option** (`Alt`) | `Alt` | 次級修飾鍵，用於備用動作、特殊字元或增強指令 |
| **`⇧`** | **Shift** | `Shift` | 擴充套件多選、反轉動作或觸發大寫功能 |
| **`⌃`** | **Control** (`Ctrl`) | `Ctrl` | 終端控制鍵及經典 Commander 組合修飾鍵 |
| **`⎋`** | **Escape** (`Esc`) | `Esc` | 取消當前操作、清空篩選輸入或關閉模態彈窗 |
| **`⏎`** | **Return** (`Enter`) | `Enter` | 執行動作、開啟專案或確認對話方塊 |
| **`⌫`** | **Delete / 退格鍵** | `Backspace` | 向後刪除字元，或在面板中返回上一級父目錄 |
| **`⌦`** | **Forward Delete (前向刪除)** | `Del` | 向前刪除字元，或直接刪除選中的檔案專案 |
| **`⇥`** | **Tab (製表鍵)** | `Tab` | 在左右雙面板之間迴圈切換鍵盤焦點 |
| **`⇞`** | **Page Up (上翻頁)** | `PgUp` | 向上翻動一整屏檔案列表 |
| **`⇟`** | **Page Down (下翻頁)** | `PgDn` | 向下翻動一整屏檔案列表 |

---

## 2. Mac 鍵盤 Fn 功能鍵使用指引

> [!IMPORTANT]
> ### 如何在蘋果 Mac 鍵盤上順暢使用 F1–F12 功能鍵
>
> 蘋果 Mac 鍵盤（包括 MacBook 筆記本內建鍵盤、Magic Keyboard 外接鍵盤以及帶 Touch Bar 的機型）在出廠預設狀態下，頂部的物理 `F1`–`F12` 鍵會被系統優先分配給**硬體多媒體控制**（如調節螢幕亮度、排程中心、聚焦搜尋、聽寫、播放暫停、音量控制等）。
>
> 鑑於經典 Commander 工作流重度依賴 `F1`–`F12`，建議根據自身習慣從以下兩種方案中任選其一：
>
> #### 方案 A：配合物理 `Fn` 鍵同按（預設即開即用）
> 按住 Mac 鍵盤左下角的 **`Fn`** 鍵（或帶地球儀圖示 🌐 的按鍵），同時按下相應的功能鍵：
>
> * **`Fn + F3`**：全能檢視器 Lister 快速只讀預覽
> * **`Fn + F4`**：內建編輯器編輯文字
> * **`Fn + F5`**：複製選中檔案到對側目標面板
> * **`Fn + F6`**：移動選中檔案到對側目標面板
> * **`Fn + F7`**：新建資料夾目錄
> * **`Fn + F8`**：刪除檔案到廢紙簍
> * **`Fn + Shift + F4`**：新建並立即編輯文字檔案
> * **`Fn + Alt + F7`**：撥出高階檔案搜尋對話方塊
>
> #### 方案 B：在 macOS 系統中開啟“標準功能鍵”（強烈推薦）
> 如果你將 ATBCmder 作為主力檔案管理工具，建議在系統設定中將頂排按鍵切換為“標準功能鍵”。切換後直接單按 `F1`–`F12` 即可觸發對應命令，需要調節音量亮度時再組合 `Fn` 鍵：
>
> 1. **macOS 13 Ventura、macOS 14 Sonoma、macOS 15 Sequoia**：
>    - 開啟 ** 蘋果選單 ➔ 系統設定...**
>    - 在左側側邊欄選擇 **鍵盤**。
>    - 點選右側的 **鍵盤快速鍵...** 按鈕。
>    - 在彈出對話方塊的左欄選擇 **功能鍵**。
>    - 將 **“將 F1、F2 等鍵用作標準功能鍵”** 開關開啟（ON）。
>    - 點選 **完成** 儲存生效。
>
> 2. **macOS 12 Monterey 及更早系統**：
>    - 開啟 ** 蘋果選單 ➔ 系統偏好設定... ➔ 鍵盤**。
>    - 在“鍵盤”標籤頁中，勾選 **“將 F1、F2 等鍵用作標準功能鍵”**。
>
> #### 配備 Touch Bar 的 MacBook Pro 機型
>
> * 按住左下角的物理 **`Fn`** 鍵，Touch Bar 會瞬間展開虛擬的 `F1`–`F12` 功能鍵欄。
> * 也可以前往 **系統設定 ➔ 鍵盤 ➔ 觸控欄設定...**，將當前在前臺執行 ATBCmder 時的顯示模式設定為**“顯示 F1、F2 等鍵”**。
>
> #### 沒有獨立 F 鍵的 60%/65% 緊湊型機械鍵盤
>
> * 無需使用彆扭的層級按鍵切換，直接使用 ATBCmder 原生支援的 macOS 修飾組合鍵（如 `⌘C`、`⌥⌘V`、`⇧⌘N`、`⌘⌫`、`⌥⏎` 等），功能 100% 齊備對等。

---

## 3. 按鍵作用域分層架構

為了徹底避免全域性熱鍵與區域性工具環境發生衝突（例如：在檔案列表中搜尋檔名，與在文字檢視器中搜尋段落文字），ATBCmder 將快速鍵劃分至明確的層級作用域中：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          全域性主作用域 (Main Scope)                          │
│  通用命令、雙面板跳轉、標籤頁切換、工具欄、系統級自動化工具                 │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  檔案面板作用域 (FilePanel)   │  專用模態工具作用域 (Modal Tools)           │
│  在目錄列表與縮圖瀏覽時生效  │  • Viewer      (全能檢視器 Lister 視窗)    │
│  (檔案多選、萬用字元標記、行內  │  • Editor      (內建程式碼/文字編輯器)        │
│  快速重新命名、目錄容量統計)    │  • Differ      (雙欄檔案差異對比視窗)       │
│                               │  • FindFiles   (多執行緒高階檔案搜尋對話方塊)   │
│                               │  • MultiRename (多重批次重新命名工具)         │
└───────────────────────────────┴─────────────────────────────────────────────┘
```

當你在軟體中按下任意按鍵時，**`HotkeyManager`** 核心按鍵引擎會按如下順序智慧分發：

1. 檢測當前處於焦點狀態的區域性上下文（如 `Viewer` 或 `FilePanel`）。
2. 若該上下文中已繫結該快速鍵，則立即觸發專屬命令。
3. 若區域性上下文中未配置該按鍵，則優雅向上回退至全域性 `Main` 作用域匹配。
4. 若全域性作用域也未攔截，則直接交付給基礎文字輸入控制元件或系統底層預設處理。

---

## 4. 全分類雙矩陣快速鍵一覽表

以下收錄了 ATBCmder 全部常用操作命令與對應的雙矩陣鍵位繫結，按工作場景詳細歸類。

### 4.1 基礎檔案操作

檔案操作是雙面板管理的核心。除特殊標明外，所有操作均嚴格遵循經典的**“源面板 ➔ 目標面板”**原則：在當前啟用面板中選中的檔案，將被處理到對側閒置面板所開啟的目標路徑中。

| 命令標識 (Command ID) | 功能描述 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_View` | 使用全能檢視器 Lister 開啟（只讀預覽） | `⌘3` / `Space` *(快速檢視)* | `F3` / `Shift+F3` | Main |
| `cm_Edit` | 在內建文字/程式碼編輯器中開啟 | `⌘4` | `F4` | Main |
| `cm_EditNew` | 新建空檔案並立即在編輯器中開啟 | `⇧⌘4` / `⇧F4` | `Shift+F4` | Main |
| `cm_Copy` | 複製選中專案至對側目標面板 | `⌘C` *(至剪貼簿)* / `F5` | `F5` | Main |
| `cm_CopySamePanel` | 在同目錄下快速克隆/副本當前選中的檔案 | `⇧F5` | `Shift+F5` | Main |
| `cm_Move` | 移動選中專案至對側目標面板 | `⌥⌘V` *(貼上移動)* / `F6` | `F6` | Main |
| `cm_RenameOnly` | 行內快速重新命名游標所在的專案 | `⏎` *(Return)* / `F2` | `F2` / `Shift+F6` | Main |
| `cm_Rename` | 彈出對話方塊重新命名選中專案 | `⇧F6` | `Shift+F6` | Main |
| `cm_MkDir` | 在當前面板中新建資料夾目錄 | `⇧⌘N` / `F7` | `F7` | Main |
| `cm_Delete` | 將選中專案移動至 macOS 廢紙簍 | `⌘⌫` *(Cmd+Delete)* / `⌦` | `F8` / `Delete` | Main |
| `cm_Wipe` | 永久粉碎/強制抹除檔案（繞過廢紙簍） | `⌥⇧⌫` / `⌥⌦` | `Alt+Delete` / `Shift+Delete` | FilePanel |
| `cm_Open` | 呼叫系統預設程式開啟，或進入所選目錄 | `⌘↓` / `⏎` *(Return)* | `Enter` | Main |
| `cm_SetFileProperties` | 檢視並編輯檔案屬性、時間戳與 UNIX 許可權 | `⌥⏎` *(Option+Return)* / `⌘I` | `Alt+Enter` | Main |
| `cm_CountDirContent` | 統計游標所在資料夾的真實位元組佔用大小 | `⌥⇧⏎` *(Option+Shift+Return)* | `Alt+Shift+Enter` | FilePanel |
| `cm_CalculateSpace` | 統計所有選中資料夾的累計容量大小 | `⌃L` / `⌘L` | `Ctrl+L` | Main |
| `cm_SymLink` | 在對側目標面板建立符號連結 (Symlink) | `⌥⌘S` | *(選單: 檔案 ➔ 建立符號連結)* | Main |
| `cm_HardLink` | 在對側目標面板建立檔案系統硬連結 (Hardlink) | `⌥⌘H` | *(選單: 檔案 ➔ 建立硬連結)* | Main |
| `cm_PackFiles` | 打包壓縮選中專案 (`.zip`, `.tar`, `.7z`) | `⌥F5` / `⌥⌘P` | `Alt+F5` | Main |
| `cm_ExtractFiles` | 將壓縮包解壓提取到對側目標面板 | `⌥F9` / `⌥⌘E` | `Alt+F9` | Main |
| `cm_ArchiveView` | 以虛擬檔案系統進入壓縮包原地瀏覽 (`vfs://`) | `⌃⇟` *(Ctrl+PgDn)* / `⌘↓` | `Ctrl+PgDn` | Main |
| `cm_CompareContents` | 快速比對兩個選中檔案的內容差異 | `⇧F3` | `Shift+F3` | Main |

---

### 4.2 選擇與標記

Commander 類軟體的一大精髓是閃電般的多檔案批次標記。你可以無需滑鼠，透過萬用字元、同副檔名、反轉或者鍵盤連續按鍵完成各種複雜選擇。

| 命令標識 (Command ID) | 功能描述 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_MarkMarkAll` | 全選當前面板內的所有檔案與資料夾 | `⌘A` | `Ctrl+A` / `Ctrl+Num+` | Main |
| `cm_MarkUnmarkAll` | 取消全選（清空面板內所有已勾選項） | `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+Num-` | Main |
| `cm_MarkInvert` | 反選（反轉當前面板內各專案的勾選狀態） | `⌘I` / `⌃I` | `Num*` *(小鍵盤 `*`)* | FilePanel |
| `cm_MarkPlus` | 按萬用字元規則批次選定（如 `*.ts;*.tsx`） | `⌘+` / `⌃+` | `Num+` *(小鍵盤 `+`)* | FilePanel |
| `cm_MarkMinus` | 按萬用字元規則反向剔除（如 `*.log`） | `⌘-` / `⌃-` | `Num-` *(小鍵盤 `-`)* | FilePanel |
| `cm_MarkCurrentExtension` | 自動選中與當前游標檔案相同字尾的所有檔案 | `⇧⌘E` / `⌥F8` | `Shift+Num+` / `Alt+Num+` | Main |
| `cm_UnmarkCurrentExt` | 剔除與當前游標檔案相同字尾的所有選中項 | `⌥⇧Num-` | `Shift+Num-` / `Alt+Num-` | Main |
| `cm_MarkCurrentName` | 自動選中與當前游標同名（不計副檔名）的檔案 | `⌥⌘N` | *(選單: 選擇 ➔ 同名檔案)* | Main |
| `cm_SelectOrDeselectFile` | 切換選中狀態並將游標向下移動一行 | `Space` | `Insert` / `Space` | FilePanel |
| `Shift+Up / Shift+Down` | 向上/向下展開或收縮連續區域選擇 | `⇧↑` / `⇧↓` | `Shift+↑` / `Shift+↓` | FilePanel |
| `Shift+PageUp / Shift+PageDown` | 向上/向下快速擴充套件整整一屏的選區 | `⇧⇞` / `⇧⇟` | `Shift+PgUp` / `Shift+PgDn` | FilePanel |
| `cm_ClearAll` | 清空所有選區標記與快速搜尋高亮 | `⌃L` | `Ctrl+L` | Main |
| `cm_CopyToClipboard` | 將選中檔案複製到系統剪貼簿 | `⌘C` | `Ctrl+C` | Main |
| `cm_CutToClipboard` | 將選中檔案剪下到系統剪貼簿 | `⌘X` | `Ctrl+X` | Main |
| `cm_PasteFromClipboard` | 將剪貼簿中的檔案貼上到當前面板目錄中 | `⌘V` | `Ctrl+V` | Main |
| `cm_PasteAsMove` | 將剪貼簿中的檔案以“移動”形式貼上過來 | `⌥⌘V` | `Ctrl+Alt+V` | Main |
| `cm_CopyNamesToClip` | 僅複製選中檔案的檔名到剪貼簿 | `⇧⌘X` | `Ctrl+Shift+X` | Main |
| `cm_CopyFullNamesToClip` | 複製選中檔案的絕對完整路徑到剪貼簿 | `⇧⌘C` | `Ctrl+Shift+C` | Main |
| `cm_CompareDirectories` | 對比左右面板，自動標記出單側獨有的檔案 | `⌥⇧C` | *(選單: 選擇 ➔ 比較目錄)* | Main |

---

### 4.3 面板導航與書籤

在多層目錄、本地驅動器、外接磁碟、網路掛載點與歷史記錄之間瞬間穿梭。

| 命令標識 (Command ID) | 功能描述 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_FocusSwap` / `cm_SwitchPanel` | 在左面板與右面板之間輪換鍵盤焦點 | `⇥` *(Tab)* | `Tab` | Main |
| `cm_Refresh` | 強制重新讀取並重新整理當前面板目錄 | `⌘R` / `⌃R` | `Ctrl+R` | Main |
| `cm_ChangeDirToParent` | 跳轉到上一級父目錄 (`..`) | `⌘↑` / `⌫` *(退格鍵)* | `Backspace` / `Ctrl+PgUp` | Main |
| `cm_ChangeDirToRoot` | 瞬間直達磁碟根目錄 (`/`) | `⌘\` | `Ctrl+\` | Main |
| `cm_ChangeDirToHome` | 瞬間直達使用者個人主目錄 (`~`) | `⇧⌘H` | `Ctrl+Shift+Home` / `Alt+Home` | FilePanel |
| `cm_ViewHistoryPrev` | 沿瀏覽歷史後退至上一個訪問過的路徑 | `⌘[` / `⌥←` | `Alt+Left` / `Ctrl+[` | Main |
| `cm_ViewHistoryNext` | 沿瀏覽歷史前進至下一個訪問過的路徑 | `⌘]` / `⌥→` | `Alt+Right` / `Ctrl+]` | Main |
| `cm_DirHistory` | 彈出近期訪問過的歷史目錄互動下拉選單 | `⌥↓` / `⌃↓` | `Alt+Down` / `Alt+F8` | Main |
| `cm_Drives` | 撥出已掛載卷宗與驅動器列表快速切換彈窗 | `⌥D` | `Alt+D` | Main |
| `cm_LeftOpenDrives` | 為**左面板**撥出驅動器/磁碟切換選單 | `⌥F1` | `Alt+F1` | Main |
| `cm_RightOpenDrives` | 為**右面板**撥出驅動器/磁碟切換選單 | `⌥F2` | `Alt+F2` | Main |
| `cm_Exchange` | 互換左右面板的當前目錄、標籤頁與瀏覽狀態 | `⌘U` | `Ctrl+U` | Main |
| `cm_TargetEqualSource` | 將對側面板同步跳轉到與當前面板完全一致的目錄 | `⌥Z` / `⌃←` / `⌃→` | `Alt+Z` / `Ctrl+Left` / `Ctrl+Right` | Main |
| `cm_SyncSlaveDir` | 開啟雙面板協同映象導航（同進同退） | `⌥S` | *(選單: 命令 ➔ 聯動導航)* | Main |
| `cm_DirHotList` | 開啟常用目錄書籤 (Hotlist) 快捷列表 | `⌘D` | `Ctrl+D` | Main |
| `cm_ConfigDirHotList` | 開啟常用目錄書籤的管理與編輯視窗 | `⇧⌘D` | `Ctrl+Shift+D` | Main |
| `cm_GoToFirst` | 將游標定位至面板內第一個檔案條目 | `⌘↑` / `Fn+←` *(Home)* | `Home` | Main |
| `cm_GoToLast` | 將游標定位至面板內最後一個檔案條目 | `⌘↓` / `Fn+→` *(End)* | `End` | Main |
| `PageUp / PageDown` | 向上/向下滾動整整一屏檢視 | `⇞` *(Fn+↑)* / `⇟` *(Fn+↓)* | `PageUp` / `PageDown` | FilePanel |

---

### 4.4 檢視模式與排序

在緊湊列表、詳細資訊列、高保真縮圖、多層級遞迴展平模式與雙欄目錄樹之間無縫切換。

| 命令標識 (Command ID) | 功能描述 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_BriefView` | 切換為簡要列表模式（多列緊湊排列檔名） | `⌃F1` | `Ctrl+F1` | Main |
| `cm_ColumnsView` | 切換為詳細列表模式（名稱、大小、日期、許可權等完整列） | `⌃F2` | `Ctrl+F2` | Main |
| `cm_ThumbnailsView` | 切換為縮圖網格模式（圖片、音影片與 PDF 大圖預覽） | `⌃⇧F1` | `Ctrl+Shift+F1` | Main |
| `cm_FlatView` | 切換為扁平檢視（平鋪穿透顯示所有子目錄檔案） | `⌘B` | `Ctrl+B` | Main |
| `cm_FlatViewSel` | 僅將選中的子目錄在扁平檢視中展開平鋪 | `⇧⌘B` | `Ctrl+Shift+B` | Main |
| `cm_TreeView` | 目錄樹檢視（將當前面板替換為多級目錄樹） | `⌃⇧F8` | `Ctrl+Shift+F8` | Main |
| `cm_TreeViewSplit` | 目錄樹檢視（單側面板內部分割：上/左為樹，下/右為檔案） | `cm_TreeViewSplit` | *(選單: 顯示 ➔ 目錄樹分割)* | Main |
| `cm_TreeViewBoth` | 目錄樹檢視（左右兩個面板同時顯示目錄樹） | `cm_TreeViewBoth` | *(選單: 顯示 ➔ 雙面板目錄樹)* | Main |
| `cm_QuickView` | 開啟/關閉對側快速預覽（在閒置面板即時預覽當前檔案） | `⌘Q` / `⌃Q` | `Ctrl+Q` | Main |
| `cm_SortByName` | 按檔名排序（再次按下可在升序/降序間切換） | `⌃F3` | `Ctrl+F3` | Main |
| `cm_SortByExt` | 按副檔名字尾排序 | `⌃F4` | `Ctrl+F4` | Main |
| `cm_SortByDate` | 按修改日期與時間排序 | `⌃F5` | `Ctrl+F5` | Main |
| `cm_SortBySize` | 按檔案體積大小排序 | `⌃F6` | `Ctrl+F6` | Main |
| `cm_SortByAttr` | 按 UNIX 屬性與許可權排序 | `cm_SortByAttr` | *(選單: 排序 ➔ 檔案屬性)* | Main |
| `cm_ShowHiddenFiles` | 切換是否顯示以點 `.` 開頭的隱藏檔案 | `⌘H` / `⇧⌘.` | `Ctrl+H` | Main |
| `cm_ShowSysFiles` | 切換是否顯示 macOS 系統關鍵受保護檔案 | `⇧⌘.` | `Ctrl+.` | Main |
| `cm_QuickSearch` | 撥出面板內快速搜尋欄（直接鍵入字元過濾列表） | `⌥S` / `⌃S` *(或直接鍵盤打字)* | `Ctrl+S` / *(直接打字)* | Main |
| `cm_SemanticFilter` | 撥出自然語言語義智慧過濾欄 | `⌘F` | `Ctrl+F` | Main |
| `cm_HorizontalFilePanels` | 切換水平上下堆疊顯示雙面板（預設左右並排） | `⇧⌘H` | `Ctrl+Shift+H` | Main |

---

### 4.5 標籤頁與視窗管理

支援在任意一側面板開啟無限數量的資料夾標籤頁，支援工作區儲存與跨面板克隆。

| 命令標識 (Command ID) | 功能描述 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_NewTab` | 在當前面板新建一個資料夾標籤頁 | `⌘T` | `Ctrl+T` | Main |
| `cm_CloseTab` | 關閉當前正在瀏覽的標籤頁 | `⌘W` | `Ctrl+W` | Main |
| `cm_NextTab` / `cm_NextTabCtrl` | 切換至右側下一個標籤頁 | `⌃⇥` *(Ctrl+Tab)* / `⌘⇧]` | `Ctrl+Tab` | Main |
| `cm_PrevTab` / `cm_PrevTabCtrl` | 切換至左側上一個標籤頁 | `⌃⇧⇥` *(Ctrl+Shift+Tab)* / `⌘⇧[` | `Ctrl+Shift+Tab` | Main |
| `cm_ShowTabsList` | 彈出當前面板已開啟的全部標籤頁彙總選單 | `⇧⌘L` | `Ctrl+Shift+L` | Main |
| `cm_CloseAllTabs` | 關閉當前面板的所有標籤頁（保留最後一張） | `⌥⌘W` | *(標籤右鍵選單: 關閉全部)* | Main |
| `cm_CloseOtherTabs` | 關閉當前面板除活動標籤之外的其他全部標籤頁 | `⇧⌘W` | *(標籤右鍵選單: 關閉其他)* | Main |
| `cm_Duplicatetab` | 快速克隆副本當前標籤頁 | `⌘D` / `cm_Duplicatetab` | *(標籤右鍵選單: 複製標籤)* | Main |
| `cm_MoveTabLeft` | 將當前活動標籤向左移動一個位置 | `⌃⇧←` | *(標籤右鍵選單: 向左移動)* | Main |
| `cm_MoveTabRight` | 將當前活動標籤向右移動一個位置 | `⌃⇧→` | *(標籤右鍵選單: 向右移動)* | Main |
| `cm_CopyTabToOtherPanel` | 將當前標籤頁直接複製克隆到對側面板中 | `⌥⌘T` | *(標籤右鍵選單: 複製到對側)* | Main |
| `cm_SaveTab` / `cm_SaveTabs` | 將當前的雙面板標籤頁佈局儲存到配置檔案 | `cm_SaveTab` | *(選單: 標籤 ➔ 儲存標籤)* | Main |
| `cm_LoadTab` / `cm_LoadTabs` | 從配置檔案重新恢復載入已儲存的標籤頁佈局 | `cm_LoadTab` | *(選單: 標籤 ➔ 載入標籤)* | Main |
| `cm_OptionsFavorites` | 開啟“常用標籤組 (Favorite Tabs)”多會話管理面板 | `cm_OptionsFavorites` | *(選單: 標籤 ➔ 常用標籤組)* | Main |
| `cm_FullScreen` | 切換軟體全屏模式 | `⌃⌘F` / `F11` | `F11` | Main |

---

### 4.6 效率工具與系統輔助

透過快速鍵直接喚起多重批次重新命名、差異對比、雙向同步、檔案粉碎與內建終端等工具。

| 命令標識 (Command ID) | 功能描述 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_FileSearch` / `cm_Search` | 撥出高階多維度檔案搜尋對話方塊 | `⌥F7` / `⌥⌘F` | `Alt+F7` | Main |
| `cm_FileDiff` / `cm_CompareFiles` | 啟動雙欄檔案差異對比工具 (Diff) | `⌘⇧F12` | `Meta+Shift+F12` | Main |
| `cm_SyncDirs` | 啟動資料夾雙向同步工具 (Sync Dirs) | `⇧F12` | `Shift+F12` | Main |
| `cm_MultiRename` | 啟動多重批次重新命名工具（支援正則與動態佔位符） | `⌘M` | `Ctrl+M` | Main |
| `cm_Split` | 將超大檔案分割為指定大小的均勻資料切片 | `⌥F6` | `Alt+F6` | Main |
| `cm_Combine` | 將有序的切片檔案合併復原為原始檔案 | `⌥F7` | `Alt+F7` | Main |
| `cm_CalculateChecksum` | 計算檔案的安全校驗雜湊值 (MD5, SHA-1, SHA-256) | `⌃X` / `⌘K` | `Ctrl+X` | Main |
| `cm_VerifyChecksum` | 讀取校驗檔案 (`.md5`, `.sha256`) 批次核驗檔案完整性 | `cm_VerifyChecksum` | *(選單: 檔案 ➔ 驗證校驗值)* | Main |
| `cm_RunTerm` | 在當前面板目錄路徑下喚起 macOS 系統終端 | `⌃J` / `F9` | `Ctrl+J` / `F9` | Main |
| `cm_FocusCmdLine` | 將鍵盤焦點直接轉移至底部嵌入式命令列輸入框 | `⇧F2` | `Shift+F2` | Main |
| `cm_ShowCmdLineHistory` | 彈出近期在底部命令列中執行過的歷史指令下拉選單 | `⌥↓` / `⌃↓` | `Alt+F8` / `Ctrl+Down` | Main |
| `cm_AddPathToCmdLine` | 將當前目錄絕對路徑追加填入到底部命令列中 | `⌘P` | `Ctrl+P` | Main |
| `cm_ShowCommandLine` | 顯示/隱藏底部命令列與控制檯輸入欄 | `⌘O` | `Ctrl+O` | Main |
| `cm_DiskBenchmark` | 啟動磁碟讀寫效能基準測速工具 | `cm_DiskBenchmark` | *(選單: 命令 ➔ 磁碟測速)* | Main |
| `cm_VisSemanticCommand` | 啟用自然語言語義命令與智慧檢索條 | `/` / `⇧⌘P` | `/` | Main |

---

### 4.7 系統偏好、配置與幫助

快速訪問軟體偏好設定、配置匯入匯出以及線上文件。

| 命令標識 (Command ID) | 功能描述 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_Options` | 開啟偏好設定 / 選項配置中心 | `⌘,` | `Ctrl+,` | Main |
| `cm_HelpContents` / `cm_HelpIndex` | 開啟互動式幫助文件與使用者指南手冊 | `⌘?` / `F1` | `F1` | Main |
| `cm_HelpKeyboard` | 彈出快速鍵快速速查卡片 | `cm_HelpKeyboard` | *(選單: 幫助 ➔ 快速鍵)* | Main |
| `cm_Exit` | 完全退出關閉 ATBCmder | `⌘Q` | `F10` / `Alt+F4` / `Alt+X` | Main |
| `cm_About` | 顯示關於 ATBCmder 版本與版權資訊 | `cm_About` | *(選單: ATBCmder ➔ 關於)* | Main |
| `cm_OpenConfigDirectory` | 在面板中直接開啟軟體配置儲存資料夾 | `cm_OpenConfigDirectory` | *(選單: 配置 ➔ 開啟配置目錄)* | Main |
| `cm_ExportConfiguration` | 將軟體所有個性化配置匯出打包為可遷移 ZIP 檔案 | `cm_ExportConfiguration` | *(選單: 配置 ➔ 匯出配置)* | Main |
| `cm_ImportConfiguration` | 從匯出的 ZIP 配置包中匯入恢復軟體設定 | `cm_ImportConfiguration` | *(選單: 配置 ➔ 匯入配置)* | Main |
| `cm_CheckForUpdate` | 線上檢查軟體最新發布版本 | `cm_CheckForUpdate` | *(選單: 幫助 ➔ 檢查更新)* | Main |

---

## 5. 專屬模態工具環境快速鍵

當你開啟全能檢視器、內建程式碼編輯器、雙欄差異比對或多重批次重新命名等獨立視窗時，ATBCmder 會自動切換為各工具特有的鍵位表。這些按鍵在該工具視窗內部直接生效，不佔用全域性 `cm_*` 名稱空間。

### 5.1 全能檢視器 (`Viewer` 作用域)

在瀏覽各種純文字、原始碼、二進位制 Hex 資料、圖片、音影片與 PDF 文件時生效：

| 操作 / 功能 | 詳細說明 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| 全選 | 選定檢視器內的全部文字或資料內容 | `⌘A` | `Ctrl+A` | Viewer |
| 純文字模式 | 強制以純文字形式顯示內容 | `1` | `1` | Viewer |
| 二進位制模式 | 強制以原始二進位制字元流顯示 | `2` | `2` | Viewer |
| 十六進位制模式 | 切換為 Hex 雙列十六進位制位元組檢查模式 | `3` | `3` | Viewer |
| 十進位制模式 | 切換為十進位制位元組資料解析模式 | `4` | `4` | Viewer |
| 翻頁圖書模式 | 切換為分頁自適應排版閱讀模式 | `5` | `5` | Viewer |
| 影象模式 | 切換為高保真圖片檢視器引擎 | `6` | `6` | Viewer |
| 外掛模式 | 切換為第三方擴充套件外掛解析檢視 | `7` | `7` | Viewer |
| PDF/文件模式 | 切換為 PDF 與辦公文件專用閱讀引擎 | `8` | `8` | Viewer |
| 程式碼高亮模式 | 切換為帶語法高亮的程式碼著色模式 | `9` | `9` | Viewer |
| 影象居中 | 將圖片精準居中在視窗正中間 | `C` | `C` | Viewer |
| 自適應視窗 | 縮放圖片使其完整適應當前視窗長寬 | `F` | `F` | Viewer |
| 僅縮小超大圖 | 圖片小於視窗時保持 100%，超出時自適應縮小 | `L` | `L` | Viewer |
| 自動換行切換 | 開啟或關閉長文字按視窗寬度自動折行 | `W` | `W` | Viewer |
| 顯示游標插入符 | 在只讀檢視器中開啟可見的文字游標 | `F6` | `F6` | Viewer |
| 查詢文字 | 在當前開啟的檔案中搜尋關鍵字 | `⌘F` / `F7` | `F7` | Viewer |
| 查詢下一個 | 跳轉到下一個搜尋匹配命中項 | `⌘G` / `F3` | `F3` | Viewer |
| 查詢上一個 | 跳轉到上一個搜尋匹配命中項 | `⇧⌘G` / `⇧F3` | `Shift+F3` | Viewer |
| 放大檢視 | 放大圖片或 PDF 顯示比例 | `⌘+` / `Num+` | `Num+` | Viewer |
| 縮小檢視 | 縮小圖片或 PDF 顯示比例 | `⌘-` / `Num-` | `Num-` | Viewer |
| 全屏沉浸檢視 | 切換檢視器全屏沉浸顯示 | `⌃⌘F` / `⌥⏎` | `Alt+Enter` | Viewer |
| 關閉檢視器 | 退出關閉 Lister 檢視器視窗 | `⎋` *(Esc)* / `Q` | `Escape` / `Q` | Viewer |

---

### 5.2 內建程式碼編輯器 (`Editor` 作用域)

在新建或編輯原始檔、配置檔案與文字檔案時生效：

| 操作 / 功能 | 詳細說明 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| 儲存檔案 | 將已修改的內容安全寫入磁碟 | `⌘S` / `F2` | `F2` | Editor |
| 查詢內容 | 在編輯器中撥出文字搜尋欄 | `⌘F` / `F7` | `F7` | Editor |
| 查詢下一個 | 跳轉到下一個搜尋匹配項 | `⌘G` / `F3` | `F3` | Editor |
| 查詢上一個 | 跳轉到上一個搜尋匹配項 | `⇧⌘G` / `⇧F3` | `Shift+F3` | Editor |
| 剪下 | 剪下選中文字到系統剪貼簿 | `⌘X` | `Ctrl+X` | Editor |
| 複製 | 複製選中文字到系統剪貼簿 | `⌘C` | `Ctrl+C` | Editor |
| 貼上 | 從系統剪貼簿貼上文字內容 | `⌘V` | `Ctrl+V` | Editor |
| 撤銷 (Undo) | 撤銷上一步編輯或輸入操作 | `⌘Z` | `Ctrl+Z` | Editor |
| 重做 (Redo) | 重新執行剛剛被撤銷的操作 | `⇧⌘Z` | `Ctrl+Shift+Z` | Editor |
| 全選 | 選中文件中的全部文字內容 | `⌘A` | `Ctrl+A` | Editor |
| 關閉編輯器 | 關閉當前編輯視窗（若有未儲存修改會自動提示） | `⎋` *(Esc)* / `⌘W` | `Esc` / `Alt+X` | Editor |

---

### 5.3 雙欄檔案差異比對 (`Differ` 作用域)

在視覺化比對兩個檔案或程式碼版本的視窗中生效：

| 操作 / 功能 | 詳細說明 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| 查詢文字 | 在差異分欄中搜尋文字內容 | `⌘F` / `F7` | `F7` | Differ |
| 查詢下一個 | 跳轉到下一個文字匹配項 | `⌘G` / `F3` | `F3` | Differ |
| 查詢上一個 | 跳轉到上一個文字匹配項 | `⇧⌘G` / `⇧F3` | `Shift+F3` | Differ |
| 下一處差異 | 將游標定位並滾動至下一處不同程式碼塊 | `⌥↓` *(Option+Down)* | `Alt+Down` | Differ |
| 上一處差異 | 將游標定位並滾動至上一處不同程式碼塊 | `⌥↑` *(Option+Up)* | `Alt+Up` | Differ |
| 第一處差異 | 直達兩個檔案之間最初的第一處差異點 | `⌥Fn+←` *(Opt+Home)* | `Alt+Home` | Differ |
| 最後一處差異 | 直達兩個檔案之間最後的一處差異點 | `⌥Fn+→` *(Opt+End)* | `Alt+End` | Differ |
| 向左合併程式碼塊 | 將右側視窗中的差異塊複製覆蓋到左側對應行 | `⌥←` *(Option+Left)* | `Alt+Left` | Differ |
| 向右合併程式碼塊 | 將左側視窗中的差異塊複製覆蓋到右側對應行 | `⌥→` *(Option+Right)* | `Alt+Right` | Differ |
| 重新掃描重新整理 | 重新自磁碟載入兩個檔案並重新計算差異 | `⌘R` | `Ctrl+R` | Differ |
| 關閉比對工具 | 退出關閉差異比對視窗 | `⎋` *(Esc)* / `⌘W` | `Alt+X` / `Esc` | Differ |

---

### 5.4 高階檔案搜尋視窗 (`FindFiles` 作用域)

在後臺多執行緒檔案搜尋對話方塊中生效：

| 操作 / 功能 | 詳細說明 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| 開始搜尋 | 立即啟動多執行緒磁碟掃描 | `⏎` *(Return)* / `F9` | `F9` | FindFiles |
| 取消 / 關閉 | 停止正在執行的搜尋任務，或直接關閉對話方塊 | `⎋` *(Esc)* | `Esc` | FindFiles |
| 檢視選中檔案 | 在全能檢視器中預覽當前高亮的搜尋結果條目 | `⌘3` / `F3` | `F3` | FindFiles |
| 編輯選中檔案 | 在內建編輯器中開啟當前高亮的搜尋結果條目 | `⌘4` / `F4` | `F4` | FindFiles |
| 新建搜尋 | 清空當前關鍵詞並重置搜尋表單 | `⌘N` | `Ctrl+N` | FindFiles |
| 重置全部過濾器 | 快速清除日期、體積與屬性等全部附加限制條件 | `⇧⌘N` | `Ctrl+Shift+N` | FindFiles |
| 讀取上次搜尋條件 | 恢復上一次成功執行過的搜尋引數配置 | `⌘L` | `Ctrl+L` | FindFiles |

---

### 5.5 多重批次重新命名工具 (`MultiRename` 作用域)

在多檔案批次重新命名規則配置工作區中生效：

| 操作 / 功能 | 詳細說明 | macOS 原生快速鍵 | 經典 Commander 鍵位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| 重置規則 | 將命名模板與正則替換規則恢復至預設初值 | `⌘R` | `Ctrl+R` | MultiRename |
| 在編輯器中手動改名 | 將目標更名列表匯出至外接文字編輯器進行批次手動微調 | `⌘I` | `Ctrl+I` | MultiRename |
| 匯入外部名稱檔案 | 從外部純文字檔案中逐行讀取新名稱以替換當前檔案 | `F3` | `F3` | MultiRename |

---

## 6. 進階技巧與系統熱鍵避讓最佳化

### 6.1 解決 macOS 全域性系統熱鍵攔截衝突

部分 macOS 預設全域性熱鍵會在系統層攔截按鍵，導致應用程式無法正常捕獲。若想釋放 ATBCmder 的極致鍵盤潛能，建議按需微調以下 macOS 系統設定：

1. **聚焦搜尋 (`⌘Space` 與快速搜尋衝突)**：
   - 預設情況下 `⌘Space` 會喚起系統 Spotlight 搜尋。如果你習慣用 `⌘Space` 選定檔案或搜尋面板條目，可前往 **系統設定 ➔ 鍵盤 ➔ 鍵盤快速鍵... ➔ 聚焦 (Spotlight)**，將系統 Spotlight 快速鍵微調為 `⌥Space`。
2. **排程中心 (`⌃↑`) 與應用程式視窗 (`⌃↓`)**：
   - macOS 預設佔用 `⌃↑` 和 `⌃↓`。而在 ATBCmder 中，`⌃↓` 是開啟目錄訪問歷史選單的經典鍵位。你可以在 **系統設定 ➔ 鍵盤 ➔ 鍵盤快速鍵... ➔ 排程中心** 中更改系統熱鍵。
3. **隱藏應用程式 (`⌘H`)**：
   - macOS 預設將 `⌘H` 繫結為隱藏當前前臺應用視窗。ATBCmder 中使用 `⌘H` 或 `⇧⌘.` 快速切換顯示隱藏的點檔案 (`.`)。若希望更順暢，可以直接使用完全符合 Finder 習慣的 `⇧⌘.`（`Cmd+Shift+點`）。
4. **視窗最小化 (`⌘M`)**：
   - macOS 預設使用 `⌘M` 最小化視窗到 Dock。ATBCmder 將其賦予了生產力極高的批次重新命名工具 (`cm_MultiRename`)。在 ATBCmder 視窗啟用時它會被優先捕獲；你也可以隨時使用備用的經典按鍵 `Ctrl+M` 或工具欄按鈕喚起。

---

### 6.2 觸控板手勢與滑鼠配合

對於使用 MacBook 筆記本觸控板的使用者，ATBCmder 深度融合了直覺式的多指觸控手勢：

* **雙指捏合縮放縮圖**：在縮圖網格檢視 (`cm_ThumbnailsView`) 中，在觸控板上雙指輕捏放大或縮小，縮圖即可在 `48 px` 到 `512 px` 之間無級平滑縮放。
* **雙指左右輕掃前後導航**：在檔案列表區域雙指左右輕掃，可快速後退（`cm_ViewHistoryPrev`）與前進（`cm_ViewHistoryNext）訪問過的目錄路徑。
* **雙擊中縫重置 50/50 分屏**：雙擊左右雙面板中間的垂直分割線，即可瞬間將兩欄面板恢復為精確對半平分。
* **標籤頁中鍵直接關閉**：對準任意資料夾標籤頁按滑鼠中鍵（或在觸控板上三指輕擊），即可瞬間關閉該標籤，省去按 `⌘W` 的步驟。

---

### 6.3 在首選項中自定義修改熱鍵

以上列出的所有快速鍵均可在軟體設定中自由更改或補充：

1. 按下 **`⌘,`**（或點選選單欄 **配置 ➔ 選項...**）開啟偏好設定視窗。
2. 在左側分類中選擇 **快速鍵 (Hotkeys)**。
3. 在頂部的 **作用域 (Context)** 下拉選單中選擇要修改的環境（如 `Main` 全域性、`FilePanel` 面板、`Viewer` 檢視器等）。
4. 在搜尋框中輸入功能名稱或 `cm_*` 識別符號快速定位。
5. 點選快速鍵輸入框，直接在物理鍵盤上按下你心儀的鍵位組合。內建的**按鍵衝突檢測引擎**會實時判斷是否有重疊，若有衝突將明確預警。
6. 點選 **應用** 按鈕，修改立即生效，無需重啟軟體。

你自定義的按鍵資料將安全儲存在 `~/.config/atbcmder/atbcmder_hotkeys.xml`（macOS 位於 `~/Library/Preferences/atbcmder/`）。日後使用 **`cm_ExportConfiguration`** 即可一鍵打包匯出並遷移至新裝置。

---

<div align="center">
  <p>想了解如何使用雙向同步做日常備份？或是快速連線區域網 NAS？</p>
  <p><strong><a href="faq_howtos.md">前往第 9 章：實戰指南與疑難解答 &rarr;</a></strong></p>
</div>
