# 제9장: 실전 문제 해결 및 레시피

정통 듀얼 패널 파일 관리자는 원시 속도와 키보드 효율성으로 유명하지만, 실제 작업을 마스터하려면 디렉터리 동기화, 배치 패턴 이름 바꾸기, 원격 가상 파일 시스템, 아카이브 재압축, 재귀 검색과 같은 고유한 하위 시스템이 일상적인 시나리오에서 어떻게 함께 작동하는지 이해해야 하는 경우가 많습니다. 또한 최신 macOS에서 작동하면 모든 사용자가 결국 접하게 되는 보안 경계, 샌드박스 제약 조건 및 시스템 바로 가기 교차점이 발생합니다. 

이 장은 두 개의 포괄적인 섹션으로 구분됩니다. 

1. **실용적인 실제 레시피**: 단계별 절차, UI 시각적 표현, 키보드 단축키 및 고급 사용자 팁을 통해 높은 가치의 파일 관리 워크플로를 다루는 5가지 완전한 엔드투엔드 연습입니다. 
2. **문제 해결 가이드 및 FAQ**: 일반적인 작동 질문, 권한 오류, 자동 새로 고침 동작, 구성 재설정, Apple 키보드 기능 키 및 볼륨 간 파일 전송 메커니즘에 대한 심층적인 설명 및 진단 해결 방법입니다. 

---

## 1. 시각적 빠른 시작: 일상적인 문제 해결 매트릭스

다음 결정 매트릭스는 일반적인 파일 관리 목표와 기술적 과제를 ATBCmder의 내장 도구 및 명령 식별자에 직접 매핑합니다. 

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              EVERYDAY TASK & DIAGNOSTIC ROUTER                         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  TASK / GOAL                               TOOL / METHOD            KEYSTROKE          │
│  ──────────────────────────────────────    ───────────────────────  ─────────────────  │
│  [1] Mirror local projects to backup       Directory Synchronizer   Shift+F12 (⇧F12)   │
│  [2] Reorganize photo libraries by date    Batch Multi-Rename Tool  Ctrl+M (⌃M)        │
│  [3] Mount home/office NAS or server       Network VFS Manager     cm_ManageConnections│
│  [4] Update config file in .zip archive    Archive VFS + Lister    Enter ➔ F4 ➔ Save   │
│  [5] Reclaim disk space from nested clutter Flat Branch View        Cmd+B (⌘B) / Alt+F7│
│                                                                                        │
│  ISSUE / SYMPTOM                           ROOT CAUSE              RESOLUTION          │
│  ──────────────────────────────────────    ──────────────────────  ──────────────────  │
│  "Operation not permitted" error           macOS Sandbox / TCC     cm_GrantAccess      │
│  Panels don't update external drives       FSEvents missing on FAT  attr_poll_interval │
│  Want to experiment without risk           Production XML safety    ATBCmder_test.sh   │
│  F-keys change brightness or volume        macOS hardware F-keys    Fn key or Settings │
│  Move takes long time across drives        Cross-volume Copy+Delete Verify free space  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 듀얼 매트릭스 빠른 참조 테이블

| 조치/진단 | macOS 바로가기 | 클래식 커맨더 키 | 명령 ID | 주요 목적 | 
| :--- | :--- | :--- | :--- | :--- | 
| **디렉터리 동기화** | `Shift+F12` / `⇧F12` | `Shift+F12` | `cm_SyncDirs` | 이중 패널 디렉터리 트리를 비교하고 동기화합니다. | 
| **일괄 다중 이름 바꾸기** | `Ctrl+M` / `⌃M` | `Ctrl+M` | `cm_MultiRename` | 토큰, 카운터 및 RegEx를 사용하여 여러 파일의 이름을 바꿉니다. | 
| **네트워크 연결** | 메뉴: 네트워크 | `cm_ManageConnections`| `cm_ManageConnections`| 저장된 SMB, SFTP, WebDAV 및 FTP 서버 프로필을 관리합니다. | 
| **빠른 네트워크 연결** | 메뉴: 네트워크 | `cm_NetworkConnect` | `cm_NetworkConnect` | 원격 서버에 대한 임시 연결 대화 상자입니다. | 
| **내부 편집 보관** | `F4` / `Fn+F4` | `F4` | `cm_Edit` | 아카이브 회원을 편집합니다. 저장 시 `RepackWorker`을 트리거합니다. | 
| **플랫 브랜치 뷰** | `Cmd+B` / `⌘B` | `Ctrl+B` | `cm_FlatView` | 단일 단순 목록에 중첩된 모든 파일을 반복적으로 표시합니다. | 
| **고급 검색** | `Alt+F7` / `⌥F7` | `Alt+F7` | `cm_Search` | "Feed to Listbox" 출력을 사용한 다중 필터 파일 검색. | 
| **파일 시스템 액세스 권한 부여**| 메뉴: 파일/도움말 | — | `cm_GrantFilesystemAccess`| macOS App Sandbox 권한 도우미를 시작합니다. | 
| **수동 패널 새로 고침** | `Ctrl+R` / `⌃R` 또는 `Cmd+R` / `⌘R` | `Ctrl+R` | `cm_Refresh` | 디스크에서 즉시 디렉터리를 다시 읽도록 합니다. | 
| **실행 시스템 터미널** | `Ctrl+J` / `⌃J` | `Ctrl+J` | `cm_RunTerm` | 현재 패널 경로에서 macOS 터미널을 생성합니다. | 
| **폴더 공간 계산** | `Alt+Shift+Enter` (`Space`) | `Alt+Shift+Enter` (`Space`) | `cm_CountDirContent` / `cm_CalculateSpace` | 총 재귀 바이트 크기를 계산합니다(단일의 경우 `Space`, 선택한 전체의 경우 `Ctrl+L`). | 
| **보안 삭제(세단)** | `Alt+Delete` / `⌥⌫` | `Alt+Delete` | `cm_Wipe` | 다중 패스 덮어쓰기 및 영구 파일 삭제. | 

---

## 2. 실용적인 실제 요리법

### 2.1 레시피 1: 두 개의 백업 폴더 비교 및 ​​동기화

**목표**: 외부 백업 드라이브 또는 네트워크 폴더에 활성 프로젝트 디렉터리의 정확한 최신 복제본이 포함되어 있는지 확인하고 변경하기 전에 추가, 수정 또는 삭제된 파일을 완벽하게 볼 수 있습니다. 

![Directory Synchronization](images/folder_synchronization.png) 
*그림 9.1: 병렬 디렉터리 비교, 방향 복사 화살표 및 비대칭 미러 옵션을 표시하는 디렉터리 동기화 대화 상자.*

#### 단계별 절차

1. **이중 패널에서 소스와 대상 정렬**: 
- **왼쪽 패널**에서 기본 로컬 작업 디렉터리(예: `~/Documents/Projects/AppAlpha`)로 이동합니다. 
- **`Tab`**을 눌러 **오른쪽 패널**로 전환하고 대상 백업 대상(예: `/Volumes/BackupDrive/Backups/AppAlpha`)으로 이동합니다. 
2. **디렉터리 동기화 실행**: 
- **`Shift+F12`**(`⇧F12`)을 누르거나 메뉴 표시줄에서 **Commands ➔ Dirs 동기화...**를 선택합니다. 
- 왼쪽 경로와 오른쪽 경로가 자동으로 채워진 상태로 디렉터리 동기화 대화 상자가 열립니다. 
3. **비교 매개변수 구성**: 
- **Compare Subdirectories**를 선택하면 중첩된 모든 폴더를 반복적으로 탐색할 수 있습니다. 
- 파일 크기와 수정 타임스탬프에만 의존하기보다는 암호화 확실성(`filecmp`을 통해 파일 바이트 확인)이 필요한 경우 **콘텐츠별 비교**를 선택하세요. 
- 백업 대상이 FAT32, exFAT 또는 SMB 네트워크 공유를 사용하는 경우 **FAT/SMB 타임스탬프 허용 범위(2.0초)**가 활성화되어 있는지 확인하여 2초 파일 시스템 타임스탬프 반올림으로 인해 발생하는 잘못된 불일치 플래그를 방지합니다. 
4. **비교 시작**: 
- **비교**를 클릭합니다(또는 `Alt+C` / `⌥C` 누르기). 
- ATBCmder는 백그라운드 비교 작업자(`SyncCompareWorker`)를 실행하고 방향 작업 표시기로 비교 테이블을 채웁니다. 
* **`->` (왼쪽에서 오른쪽으로)**: 로컬 파일이 최신 파일이거나 왼쪽에만 존재합니다. 조치: 왼쪽에서 오른쪽으로 복사하세요. 
* **`<-` (Right to Left)**: The backup file is newer, or only exists on the right. Action: copy right to left.
     * **`=` (Equal)**: Both files are identical in size and timestamp/content. These are hidden from the pending action list by default.
     * **`!=` (Conflict)**: Incompatible directory-versus-file collision or timestamp mismatch requiring manual inspection.
5. **Select Your Synchronization Strategy**:
   - **Two-Way Symmetric Sync (Default)**: Copies newer files in both directions (`->` 및 `<-`). No files are deleted on either side. Ideal for syncing collaborative folders between machines.
   - **Asymmetric Mirroring (`Asymmetric` Checkbox Enabled)**: Makes the Right directory an exact binary replica of the Left directory. Any file on the Right that does not exist on the Left is **permanently deleted from the backup target**.
6. **Review and Execute**:
   - Inspect the summary count at the bottom: *e.g., "Left to Right: 42 files (128.4 MB) | Right to Left: 0 files | Deletes: 3 files"*.
   - Click **Synchronize** to launch the non-blocking background transfer queue. Progress bars reflect active transfer volume and remaining item counts.

> [!CAUTION] 
> **비대칭 미러링 데이터 손실 위험**: 
> **비대칭** 모드를 선택하면 소스에서 삭제되거나 이름이 변경된 대상 드라이브에 있는 파일이 macOS 휴지통으로 이동하지 않고 **영구적으로 제거**됩니다. 동기화를 클릭하기 전에 항상 방향 비교표를 검토하세요! 

> [!TIP] 
> **⚡ 전문가 팁: 미디어 및 코드에 대한 콘텐츠 수준 검증**: 
> 비디오 영상이나 Git 리포지토리를 백업할 때 파일 크기가 일치할 수 있지만 미묘한 내부 바이트 손상이 있을 수 있습니다. 미션 크리티컬 아카이브에 대해서는 항상 **컨텐츠별 비교**를 확인하세요. USB 또는 Wi-Fi를 통해 바이트별 비교는 시간이 더 오래 걸리지만 100% 데이터 무결성을 보장합니다. 

---

### 2.2 레시피 2: 날짜와 일련번호를 사용하여 카메라 사진의 이름을 일괄적으로 변경

**목표**: 정리되지 않은 수백 개의 카메라 파일(예: `DSC_0012.JPG`, `DSC_0013.JPG`, `IMG_4901.CR3`)을 제로 패딩된 시퀀스 카운터 및 실시간 안전 미리보기를 사용하여 `2026-09-06_Vacation_001.jpg`과 같은 깔끔하고 정렬 가능한 파일 이름으로 변환합니다. 

![Batch Multi-Rename Tool](images/multi_rename_dialog.png) 
*그림 9.2: 실시간 미리보기 행, 메타데이터 토큰, 숫자 카운터 제어 및 충돌 감지 기능을 갖춘 일괄 다중 이름 바꾸기 도구.*

#### 단계별 절차

1. **사진 선택**: 
- 활성 패널에서 카메라 가져오기 디렉터리로 이동합니다. 
- **`Cmd+A`**(`⌘A`)을 사용하여 모든 사진을 선택하거나 키보드에서 **`+`**을 눌러 `*.jpg;*.jpeg;*.cr3;*.arw`과 같은 와일드카드 마스크를 입력합니다. 
2. **일괄 다중 이름 바꾸기 도구 실행**: 
- **`Ctrl+M`** (`⌃M`) 또는 **`Cmd+M`** (`⌘M`)을 누르거나 메뉴 표시줄에서 **파일 ➔ 다중 이름 바꾸기 도구...**를 선택합니다. 
3. **파일 이름 마스크 정의**: 
- **파일 이름 마스크** 필드에 메타데이터 토큰을 사용하여 원하는 구조를 입력합니다. 
     ```
     [Y]-[M]-[D]_Vacation_[C]
     ```


- **토큰 설명**: 
* `[Y]`: 파일 수정 연도 4자리(예: `2026`). 
* `[M]`: 2자리 월(예: `09`). 
* `[D]`: 2자리 일(예: `06`). 
* `Vacation`: 정적 설명 텍스트. 
* `[C]`: 순차 숫자 카운터. 
4. **카운터 시퀀스 구성**: 
- **카운터 설정** 카드에서: 
* **시작 위치**: `1` 
* **단계**: `1` 
* **숫자**: `3`(0 채우기 적용: `001`, `002`, `003`... 최대 `999`). 
5. **찾기 및 바꾸기를 사용하여 카메라 접두사 제거(선택 사항)**: 
- 카메라 접두사 없이 원본 파일 이름의 일부를 유지하려는 경우(예: `DSC_8941.JPG`의 카메라 시퀀스 번호 유지): 
* **파일 이름 마스크**를 다음으로 설정: `[YMD]_[N5-]` 
* `[N5-]`은 인덱스 5부터 이름 끝까지의 문자를 추출하여 `DSC_`을 완전히 제거합니다. 
- 또는 **검색 및 바꾸기** 필드를 사용하세요. 
* **찾기**: `DSC_` 
* **교체**: `Photo_` 
* `^IMG_(\d+)`과 같은 복잡한 표현식 패턴을 사용하는 경우 **RegEx**를 확인하세요. 
6. **실시간 미리보기 테이블 검사**: 
- 3열 테이블(`Old Name`, `New Name`, `Directory`)은 키를 누를 때마다 즉시 업데이트됩니다. 
- **상태** 열을 확인하세요. ATBCmder는 중복된 대상 이름을 충돌 표시기로 굵은 빨간색으로 강조 표시하여 실수로 덮어쓰는 것을 방지합니다. 
7. **이름 바꾸기 실행**: 
- **`Enter`**를 누르거나 **이름 바꾸기 시작**을 클릭하세요. ATBCmder는 디스크에서 원자적으로 이름 바꾸기를 수행하고 패널 보기를 새로 고칩니다. 

> [!NOTE] 
> **확장 안전**: 
> 기본적으로 **확장 마스크**는 `[E]`로 설정되어 원본 파일 확장자를 수정되지 않은 상태로 유지합니다. 파일에서 확장명을 명시적으로 제거하려는 경우가 아니면 `[E]`을 삭제하지 마십시오.

> [!TIP] 
> **⚡ 전문가 팁: 외부 편집기 작업 흐름(`⌘I`)**: 
> 클라이언트 이름 또는 트랙 제목 목록이 불규칙한 경우 다중 이름 바꾸기 도구 내에서 **`Cmd+I`** (`⌘I` / 외부 편집기에서 편집)을 누르세요. ATBCmder는 대상 이름을 기본 텍스트 편집기로 내보냅니다. Vim, VS Code 또는 TextEdit에서 목록을 편집하고 문서를 저장하면 ATBCmder가 수정된 이름을 미리 보기 그리드로 즉시 가져옵니다. 

---

### 2.3 레시피 3: SMB, SFTP 또는 WebDAV를 통해 가정/사무실 NAS에 연결

**목표**: 별도의 터미널 명령이나 Finder 연결 시트를 조작하지 않고도 온프레미스 TrueNAS 또는 Synology 저장소 풀, AWS EC2 Linux 서버 또는 Nextcloud WebDAV 클라우드 저장소를 듀얼 패널 탭에 탑재합니다. 

![Remote VFS Connection](images/smb_sftp_ftp_remote_access.png) 
*그림 9.3: SMB, SFTP 및 WebDAV 프로토콜 전반에 걸쳐 보안 원격 네트워크 공유 구성.*

#### 단계별 절차

1. **네트워크 연결 관리자를 엽니다**: 
- 기본 메뉴 표시줄에서 **네트워크 ➔ 네트워크 연결 관리...**를 선택하거나 **`cm_ManageConnections`** 명령을 실행합니다. 
2. **새 연결 프로필 만들기**: 
- 왼쪽 하단의 **`➕ New`** 버튼을 클릭하세요. 
- **레이블** 필드에 인식 가능한 식별자(예: `Synology Office NAS` 또는 `AWS Production Web`)를 입력합니다. 
3. **프로토콜 및 호스트 세부 정보 구성**: 
- **프로토콜**: 드롭다운에서 대상 프로토콜을 선택합니다. 
* **SMB/CIFS**: 포트 `445`(Synology, QNAP, Windows Server, TrueNAS의 표준). 
* **SFTP(SSH 파일 전송)**: 포트 `22`(Linux/UNIX 클라우드 인스턴스 표준). 
* **WebDAV / WebDAVS**: 포트 `80` 또는 `443`(Nextcloud, ownCloud의 표준). 
* **FTP / FTPS**: 포트 `21` 또는 `990`(레거시 파일 호스트). 
- **호스트**: IP 주소 또는 도메인 이름(예: `192.168.1.100` 또는 `sftp.mycompany.com`)을 입력합니다. 
- **포트**: 프로토콜을 선택하면 자동으로 설정됩니다. 서버가 비표준 포트를 사용하는 경우 조정하십시오. 
- **사용자 이름**: 원격 시스템 계정 사용자 이름을 입력합니다. 
- **원격 경로**: 기본 랜딩 디렉터리를 설정합니다(예: `/volume1/Media` 또는 `/var/www/html`). 
4. **보안 자격 증명 저장소**: 
- 비밀번호나 패스키를 입력하세요. 
- **macOS 키체인에 비밀번호 기억**을 선택하세요. 
- **보안 보장**: ATBCmder는 XML 구성 파일에 일반 텍스트 자격 증명을 저장하지 않습니다. 모든 비밀은 기본 Apple 키체인(`com.aitobox.atbcmder.vfs`) 내에 암호화되어 봉인됩니다. 
5. **연결 테스트**: 
- **`🔍 Test Connection`**을 클릭하세요. 
- ATBCmder는 네트워크 연결 가능성을 확인하고, SSH 호스트 키 또는 TLS 인증서를 확인하고, 자격 증명을 확인하고, 대화 상자를 닫지 않고 성공 경고를 표시하는 백그라운드 작업자(`ConnectionTestWorker`)를 파견합니다. 
6. **연결 및 찾아보기**: 
- **`🔗 Connect`**을 클릭합니다(또는 `Enter`을 누릅니다). 
- 활성 패널에 새 폴더 탭이 열리고 통합 VFS URI로 형식화된 원격 경로가 표시됩니다. 
     ```
     vfs://smb://admin@192.168.1.100/volume1/Media/
     vfs://sftp://ubuntu@aws.prod.internal:22/var/www/html/
     ```


- 이제 동일한 이중 패널 민첩성을 사용하여 로컬 디스크와 원격 서버에서 파일을 탐색, 검색, 복사(`F5`), 이동(`F6`) 및 삭제(`F8`)할 수 있습니다. 
7. **메뉴 표시줄에서 빠른 재연결**: 
- 저장된 모든 프로필은 자동으로 **네트워크 ➔ 저장된 연결**에 나타납니다. 저장된 서버를 클릭하면 즉시 마운트됩니다. 

> [!TIP] 
> **⚡ 전문가 팁: SFTP를 위한 SSH 키 기반 인증**: 
> 자동화된 클라우드 서버 액세스를 위해 공개 키 인증을 구성합니다. SFTP 연결 프로필에서 비밀번호 필드를 비워두고 로컬 개인 키(예: `~/.ssh/id_ed25519`)를 가리킵니다. 키가 암호로 보호되는 경우 ATBCmder는 해당 키를 묻는 메시지를 한 번 표시하고 macOS 키체인에 안전하게 저장합니다. 

---

### 2.4 레시피 4: 압축을 풀지 않고 아카이브 내에서 직접 파일 편집

**목표**: 전체 아카이브를 하드 드라이브에 압축 해제하지 않고 로컬 저장소 또는 원격 서버에 있는 멀티 기가바이트 `.zip`, `.tar.gz` 또는 `.7z` 아카이브 내의 중첩된 구성 파일(`settings.json` 또는 `config.yaml`)을 수정합니다. 

![Archive VFS](images/archive_vfs.png) 
*그림 9.4: 통합 `vfs://` 가상 파일 시스템을 통해 압축된 아카이브 내부 탐색 및 편집.*

#### 단계별 절차

1. **아카이브를 가상 디렉터리로 입력**: 
- 활성 패널에서 아카이브 파일(예: `production_backup.zip`)을 강조 표시합니다. 
- **`Enter`**를 누르거나 더블클릭하세요. 
- ATBCmder는 탐색을 가로채고 아카이브를 가상 파일 시스템으로 마운트합니다. 
     ```
     vfs:///Users/brain/Downloads/production_backup.zip/
     ```
 

2. **대상 파일로 이동**: 
- 물리적 볼륨에서와 마찬가지로 중첩된 가상 디렉터리(`etc`, `nginx`, `conf.d`)를 찾아보세요. 
- 업데이트해야 하는 파일을 찾습니다(예: `nginx.conf` 또는 `app_settings.json`). 
3. **내장된 텍스트 편집기에서 열기**: 
- **`F4`**(`Fn+F4` / `cm_Edit`)을 누릅니다. 
- ATBCmder는 압축된 멤버를 임시 격리된 버퍼로 스트리밍하고 구문 강조 텍스트 편집기에서 직접 엽니다. 
4. **수정하고 저장**: 
- 필요한 구성을 수정합니다. 
- 버퍼를 저장하려면 **`Cmd+S`**(`⌘S`)을 누르세요. 
5. **자동 재포장 수명 주기(`RepackWorker`)**: 
- 편집기를 저장하거나 닫으면 ATBCmder의 백그라운드 재압축 엔진(`RepackWorker`)이 자동으로 활성화됩니다. 
1. 원래 압축된 멤버와 수정된 버퍼 사이의 델타를 계산합니다. 
2. 구성된 경고 임계값(`ArchiveRepackWarningMB`)을 기준으로 전체 아카이브 크기를 확인합니다. 
3. 수정된 파일을 다시 압축하고 임시 파일에 아카이브 구조를 다시 작성합니다. 
4. 디스크의 원본 아카이브 파일을 원자적으로 대체하여 쓰기 도중에 시스템 전원이 꺼지더라도 손상이 발생하지 않도록 보장합니다. 
5. 활성 패널 보기가 자동으로 새로 고쳐져 업데이트된 구성원 바이트 크기 및 타임스탬프가 표시됩니다.

> [!IMPORTANT] 
> **대형 아카이브 재포장 가드(`ArchiveRepackWarningMB`)**: 
> 15GB 아카이브 내의 단일 2KB 텍스트 파일을 업데이트하려면 디스크의 전체 아카이브 파일을 다시 작성해야 합니다. 예상치 못한 CPU 급증 및 SSD 마모를 방지하기 위해 ATBCmder는 아카이브 크기를 확인합니다. 아카이브가 `ArchiveRepackWarningMB`(기본값: 500MB)을 초과하면 경고 대화 상자가 표시됩니다. *"이 아카이브는 1.4GB입니다. 다시 압축하면 전체 파일이 다시 작성됩니다. 계속하시겠습니까?"* **구성 ➔ 옵션 ➔ 아카이브**에서 이 임계값을 사용자 정의할 수 있습니다. 

---

### 2.5 레시피 5: 중첩된 디렉터리에서 대용량 파일 찾기 및 삭제

**목표**: 버려진 4K 비디오 렌더, 부풀어 오른 `node_modules` 폴더, Docker 가상 디스크 이미지 또는 다중 레벨 디렉토리 구조 내에 깊숙이 흩어져 있는 오래된 DMG 설치 프로그램을 신속하게 찾아 안전하게 제거하여 귀중한 SSD 용량을 확보합니다. 

![Flat Branch View](images/branch_view.png) 
*그림 9.5: 즉각적인 크기 정렬을 위해 단일 평면 테이블에 깊이 중첩된 내용을 표시하는 평면 분기 보기(`Cmd+B`).*

#### 방법 A: Flat Branch View를 통한 즉각적인 평면화(`Cmd+B`)

1. **상위 루트 폴더로 이동**: 
- 감사할 최상위 상위 폴더(예: `~/Projects` 또는 `~/Downloads`)를 강조 표시합니다. 
2. **플랫 분기 보기 활성화**: 
- **`Cmd+B`**(`⌘B`) 또는 **`Ctrl+B`**(`cm_FlatView`)을 누르거나 **표시 ➔ 분기 보기(플랫 보기)**를 선택합니다. 
- ATBCmder는 모든 하위 디렉터리를 반복적으로 검색하고 디렉터리 폴더 경계를 제거하여 **단일 단순 목록**에 중첩된 모든 파일을 표시합니다. 
3. **크기 내림차순으로 정렬**: 
- **크기** 열 헤더를 클릭하거나 **`Ctrl+F6`**(`cm_SortBySize`)을 눌러 가장 큰 파일을 맨 위로 정렬합니다. 
- 거대한 ISO 파일, 데이터베이스 덤프 및 가상 머신 이미지가 즉시 패널 상단에 떠 있습니다. 
4. **디렉터리 공간 계산**: 
- 표준 보기에 표시되는 하위 폴더의 경우 폴더에 커서를 놓고 **`Space`**(`␣` / `cm_CalculateSpace`)을 누릅니다. ATBCmder는 총 재귀 바이트 공간을 계산하고 이를 기본 `<DIR>` 레이블 위치에 표시합니다. 
5. **분기 보기 종료**: 
- **`Cmd+B`**을 다시 누르거나 `..`에서 `Esc` / `Backspace`을 눌러 일반 계층적 디렉터리 탐색으로 돌아갑니다. 

---

#### 방법 B: 고급 검색(`Alt+F7`) 및 "목록 상자에 피드"를 통한 타겟 필터링

![Advanced Search](images/advanced_search_dialog.png) 
*그림 9.6: 크기 필터 기준과 "목록 상자에 피드" 버튼이 있는 고급 검색 대화 상자.* 

1. **고급 검색 실행**: 
- **`Alt+F7`**(`⌥F7`)을 누르거나 **명령 ➔ 검색...**을 선택합니다. 
2. **크기 및 유형 필터 정의**: 
- **검색 위치** 필드에서 루트 디렉터리를 확인합니다. 
- **크기** 필터를 확인합니다. **`>`**을 선택하고 단위 **`MB`**(또는 `1` **`GB`**)와 함께 `100`을 입력합니다. 
- **파일 마스크** 필드에서 대상 확장명(예: `*.dmg;*.iso;*.mp4;*.mov;*.zip`)을 지정하거나 `*`로 두어 부풀린 항목을 찾습니다. 
- **날짜** 탭에서 선택적으로 지난 180일 동안 수정되지 않은 파일로 결과를 제한합니다. 
3. **검색 실행**: 
- **검색 시작**을 클릭합니다. 
4. **가상 패널 탭에 결과 피드("목록 상자에 피드")**: 
- 결과가 채워지면 **목록 상자에 피드** 버튼을 클릭하세요. 
- 전체 검색 결과 세트는 활성 패널의 **전용 가상 탭**으로 전송됩니다. 
- 정적 모달 대화 상자와 달리 이 탭의 파일은 일반 파일 패널 항목처럼 작동합니다. 훑어보기(`Ctrl+Q` / `⌘Q`)로 미리 보거나, Universal Lister(`F3`)에서 검사하거나, `Insert` / `Space`로 여러 파일을 표시할 수 있습니다. 
5. **검토 및 삭제**: 
- 원하지 않는 파일을 선택하고 **`F8`**(`Fn+F8` / `cm_Delete`)을 눌러 macOS 휴지통으로 안전하게 이동하세요. 
- 영구적이고 복구 불가능한 데이터 삭제(예: 기밀 클라이언트 데이터 삭제)가 필요한 경우 **`Alt+Delete`**(`⌥⌫` / `cm_Wipe`)을 눌러 보안 다중 패스 파일 파쇄를 시작하세요. 

> [!TIP] 
> **⚡ 전문가 팁: 체크섬을 통해 동일한 중복 파일 식별**: 
> 여러 개의 대용량 파일이 완전히 중복된 것으로 의심되면 해당 파일을 선택하고 **`Ctrl+X`**(`⌃X` / `cm_CheckSumCalc`)을 누르세요. **SHA-256**을 선택하고 계산을 클릭합니다. 일치하는 해시 다이제스트는 100% 바이너리 중복을 확인하므로 완전한 확신을 가지고 불필요한 복사본을 삭제할 수 있습니다. 

---

## 3. 문제 해결 가이드 및 자주 묻는 질문(FAQ)

### 3.1 "작업이 허용되지 않음" / macOS 권한 거부 오류

#### 근본 원인

최신 macOS(macOS 12 Monterey~macOS 15 Sequoia)에서 Apple은 엄격한 **앱 샌드박스** 및 **TCC(투명성, 동의 및 제어)** 개인 정보 보호 경계를 시행합니다. 샌드박스 애플리케이션은 **보안 범위 책갈피**라고 알려진 명시적인 사용자 부여 암호화 권한 토큰 없이는 외부 드라이브, 시스템 폴더 또는 표준 사용자 디렉터리(`~/Documents`, `~/Downloads`, `~/Desktop`)에 액세스할 수 없습니다. 

ATBCmder에 파일 시스템 액세스 권한이 부여되지 않은 경우 다음이 발생할 수 있습니다. 

- 표시되는 파일 작업 대화상자: `"Error: Operation not permitted"`. 
- Finder에 파일이 있는데도 디렉토리가 비어 있는 것으로 나타납니다. 
- `/Volumes` 아래의 외부 USB 또는 Thunderbolt 드라이브에 액세스 거부 오류가 표시됩니다.

#### 해결 방법 1: App Sandbox 온보딩 도우미 사용(`cm_GrantFilesystemAccess`)

ATBCMder에는 macOS에 영구 보안 북마크를 등록하도록 설계된 내장 온보딩 도우미가 포함되어 있습니다. 

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
 

1. 메뉴 모음에서 **파일**(또는 **도움말**) ➔ **파일 시스템 액세스 권한 부여...**를 선택하거나 **`cm_GrantFilesystemAccess`** 명령을 실행합니다. 
2. **"루트 디렉터리(/)에 대한 액세스 권한 부여"**를 클릭합니다. 
* `Macintosh HD`(`/`)을 가리키는 기본 Apple `NSOpenPanel` 시트가 나타나면 **액세스 권한 부여**(또는 **열기**)를 클릭합니다. 
* **작동 이유**: `/`을 승인하면 `sandbox_bookmarks.plist`에 저장된 루트 보안 범위 책갈피가 생성됩니다. 하위 경로는 보안 토큰을 하향 상속하므로 `/`에 대한 액세스 권한을 부여하면 모든 표준 사용자 폴더(`~/Documents`, `~/Downloads`, `/Applications`, `~/Projects`)가 영구적으로 잠금 해제됩니다. 
3. **"외부 디스크(/볼륨)에 대한 액세스 권한 부여"**를 클릭합니다. 
* 열려 있는 시트에서 `/Volumes`에 대한 **액세스 권한 부여**를 클릭합니다. 
* 연결된 모든 USB 플래시 드라이브, 외부 SSD, SD 카드, 디스크 이미지(DMG) 및 네트워크 SMB 마운트를 인증합니다. 
4. **완료**를 클릭합니다. 귀하의 권한은 애플리케이션을 다시 시작해도 영구적으로 저장됩니다.

#### 해결 방법 2: macOS 시스템 설정에서 전체 디스크 액세스(FDA) 부여

`~/Library/Mail`, `~/Library/Messages`, Safari 탐색 캐시 또는 Time Machine 백업 트리와 같은 보호된 시스템 위치를 관리해야 하는 경우 macOS TCC에는 추가 시스템 수준 권한이 필요합니다. 

1. **시스템 설정**(Apple 메뉴  ➔ 시스템 설정)을 엽니다. 
2. **개인 정보 보호 및 보안 ➔ 전체 디스크 액세스**로 이동합니다. 
3. 애플리케이션 목록에서 **ATBCmder**를 찾아 스위치를 **켜기**로 전환합니다. 
4. ATBCmder가 목록에 없는 경우: 
* 하단의 **`+`** 버튼을 클릭하세요. 
* Mac 비밀번호 또는 Touch ID로 인증하세요. 
* `/Applications/ATBCmder.app`을 선택하고 **열기**를 클릭합니다. 
5. 애플리케이션을 다시 시작하라는 메시지가 표시되면 **종료 후 다시 열기**를 클릭합니다.

#### 해결 방법 3: 터미널을 통해 손상된 TCC 개인 정보 보호 권한 재설정

macOS 운영 체제 업그레이드 또는 애플리케이션 재서명 이벤트 후에 권한이 손상된 경우 macOS `tccutil` 명령줄 도구를 사용하여 TCC 데이터베이스를 재설정하세요. 

```bash
# Reset all Full Disk Access permissions for ATBCmder
tccutil reset SystemPolicyAllFiles com.aitobox.atbcmder

# Reset Desktop, Documents, and Downloads folder permissions
tccutil reset SystemPolicyDocumentsFolder com.aitobox.atbcmder
tccutil reset SystemPolicyDownloadsFolder com.aitobox.atbcmder
tccutil reset SystemPolicyDesktopFolder com.aitobox.atbcmder
```
 

이 명령을 실행한 후 ATBCmder를 다시 시작하고 **`cm_GrantFilesystemAccess`**를 다시 실행하세요. 

---

### 3.2 자동 새로 고침이 디스크의 파일 변경 사항을 감지하지 못함

#### 근본 원인

ATBCmder는 다계층 파일 모니터링 엔진을 사용합니다. 

1. **커널 `FSEvents`**: 기본 Apple APFS 및 HFS+ 볼륨에서 macOS 커널은 외부 도구에 의해 파일이 추가, 수정 또는 삭제될 때 즉각적인 디렉터리 변형 이벤트를 발생시킵니다. 
2. **파일 시스템 제한**: Apple이 아닌 파일 시스템(예: **FAT32** 또는 **exFAT**으로 포맷된 외부 USB 스틱) 및 원격 네트워크 마운트(**SMB**, **NFS**, **SFTP**, **WebDAV**) **커널 `FSEvents` 알림을 지원하지 않습니다**. 타사 앱이 SMB 공유에서 파일을 생성하거나 삭제하면 macOS 커널은 알림 이벤트를 전혀 받지 않습니다.

#### 해결 단계

1. **폴링 폴백 간격 조정(`attr_poll_interval`)**: 
- **`Cmd+,`**(`⌘,`) 또는 **구성 ➔ 옵션...**을 통해 기본 설정을 엽니다. 
- **자동 새로고침** 페이지로 이동합니다. 
- **파일 이름 변경 감시** 및 **속성 변경 감시**가 활성화되어 있는지 확인하세요. 
- **폴링 간격(`attr_poll_interval`)**을 조정합니다. 
* 기본값: `5 seconds`. 
* 빠른 로컬 테스트 또는 활성 네트워크 개발의 경우: `1` 또는 `2 seconds`로 줄이세요. 
* 대기 시간이 긴 Wi-Fi 공유의 경우: 네트워크 오버헤드를 최소화하려면 `10` 또는 `15 seconds`로 늘립니다. 
2. **제외된 디렉터리 목록을 확인하세요**: 
- 동일한 **자동 새로 고침** 기본 설정 페이지에서 **제외된 디렉터리** 테이블을 검토합니다. 
- 활성 경로(또는 상위 폴더)가 제외 목록에 추가된 경우 ATBCmder는 CPU 주기를 보존하기 위해 의도적으로 파일 모니터링을 억제합니다. 모니터링을 다시 활성화하려면 경로를 제거하십시오. 
3. **백그라운드 새로 고침 설정 확인**: 
- ATBCmder가 최소화되거나 다른 창 뒤에 있을 때만 파일 패널이 업데이트되지 않는 경우 다음 옵션을 확인하십시오. 
`[ ] Disable auto-refresh when ATBCmder is in the background` 

- ATBCmder가 백그라운드 빌드 출력 및 외부 다운로드를 지속적으로 반영하도록 하려면 이 옵션을 선택 취소합니다. 
4. **즉시 수동 새로 고침을 강제 실행**: 
- 언제든지 **`Ctrl+R`**(`⌃R`) 또는 **`Cmd+R`**(`⌘R`)(`cm_Refresh`)을 누르세요. 
- 이는 모든 캐싱 계층을 우회하고 내부 디렉터리 모델을 플러시하며 스토리지 컨트롤러에서 디렉터리 내용을 즉시 다시 읽습니다. 

---

### 3.3 격리된 테스트 모드에서 구성 또는 테스트를 안전하게 재설정

#### `scripts/ATBCmder_test.sh`을 사용하여 새로운 구성을 안전하게 테스트

실험적인 키보드 단축키 레이아웃, 새로운 색상 테마 또는 자동화된 스크립팅 명령을 테스트할 때 프로덕션 구성 XML을 수정하지 않아야 합니다. 

ATBCmder는 샌드박스 테스트 실행 프로그램 스크립트를 제공합니다. 
```bash
# Run ATBCmder in an isolated test environment
./scripts/ATBCmder_test.sh
```
 

**작동 방식**: 

1. 스크립트는 전용 임시 디렉터리 `tests/.test_config/`을 생성합니다. 
2. 깨끗한 기준 테스트 구성(`src/atbcmder/resources/test_config.xml`)을 `tests/.test_config/atbcmder.xml`에 복사합니다. 
3. 환경 변수를 내보냅니다. 
   ```bash
   export ATBCMDER_CONFIG_PATH="$(pwd)/tests/.test_config"
   ```
 

4. ATBCmder가 시작되면 이 테스트 폴더에서만 모든 설정을 읽습니다. 모든 변경 사항, 탭 수정 또는 단축키 실험은 `tests/.test_config/` 내에 완전히 포함되며 개인 기본 설정은 전혀 변경되지 않습니다.

#### 공장 기본 구성 복원

프로덕션 구성이 손상되었거나 완전히 새로 시작하려는 경우: 

1. **ATBCmder**를 완전히 종료합니다(**`Cmd+Q`** / `⌘Q`). 
2. macOS 터미널을 열고 구성 디렉터리를 찾습니다. 
* 표준 설치: `~/Library/환경설정/atbcmder/` 
* Linux/XDG 대체: `~/.config/atbcmder/` 
3. 활성 구성 파일을 백업하거나 제거합니다. 
   ```bash
   # Move configuration files to a backup location
   mv ~/Library/Preferences/atbcmder/atbcmder.xml ~/Library/Preferences/atbcmder/atbcmder.xml.bak
   mv ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml ~/Library/Preferences/atbcmder/atbcmder_hotkeys.xml.bak
   ```
 

4. ATBCmder를 다시 시작합니다. 
5. 시작 시 ATBCmder는 누락된 구성 파일을 감지하고 공식 공장 기본값으로 채워진 깨끗하고 검증된 XML 구성을 자동으로 재생성합니다.

#### 휴대용 구성 내보내기 및 가져오기

여러 Mac에 걸쳐 구성을 마이그레이션하거나 외부 백업을 생성하려면: 

- **내보내기**: **구성 ➔ 구성 내보내기...**(**`cm_ExportConfiguration`** 명령)를 선택하여 단축키, 열, 즐겨찾는 탭 및 색상 팔레트가 포함된 통합 `.zip` 또는 `.xml` 스냅샷을 저장합니다. 
- **가져오기**: 대상 컴퓨터에서 **구성 ➔ 구성 가져오기...**(명령 **`cm_ImportConfiguration`**)를 선택하여 설정을 즉시 복원합니다. 

---

### 3.4 명령 대신 macOS 밝기/볼륨을 트리거하는 기능 키

#### 근본 원인

기본적으로 Apple 키보드(MacBook 내장 키보드, Magic Keyboard)는 키의 맨 윗줄에 특별한 하드웨어 기능을 할당합니다. 

- `F1` / `F2`: 디스플레이 밝기 감소/증가 
- `F3`: 임무 제어 
- `F4`: 스포트라이트/런치패드 
- `F7` / `F8` / `F9`: 미디어 재생 컨트롤(되감기, 재생/일시 정지, 빨리 감기) 
- `F10` / `F11` / `F12`: 오디오 음소거, 볼륨 낮추기, 볼륨 높이기 

파일을 복사하려고 `F5`을 누르면 macOS는 키 입력을 가로채고 아무 작업도 수행하지 않습니다(또는 키보드 조명을 조정합니다).

#### 해결 방법 1: `Fn` 수정자 코드 사용

키보드 왼쪽 하단에 있는 **`Fn`**(기능) 또는 **구형(`🌐`)** 키를 누른 상태에서 기능 키를 누르세요. 

- **`Fn+F3`**: 범용 리스터(`cm_View`) 
- **`Fn+F4`**: 텍스트 편집기(`cm_Edit`) 
- **`Fn+F5`**: 파일 복사(`cm_Copy`) 
- **`Fn+F6`**: 파일 이동/이름 바꾸기(`cm_Rename`) 
- **`Fn+F7`**: 새 폴더 생성(`cm_MakeDir`) 
- **`Fn+F8`**: 휴지통으로 삭제(`cm_Delete`) 
- **`Fn+Shift+F12`**: 디렉터리 동기화(`cm_SyncDirs`)

#### 해결 방법 2: macOS 설정에서 시스템 전체에 표준 기능 키를 활성화합니다.

ATBCmder를 정기적으로 사용하는 경우 기능 키를 표준 `F1`-`F12` 키로 처리하도록 macOS를 구성하는 것이 권장되는 설정입니다. 

1. **시스템 설정**(Apple 메뉴  ➔ 시스템 설정)을 엽니다. 
2. 왼쪽 사이드바에서 **키보드**를 선택합니다. 
3. **키보드 단축키...** 버튼을 클릭합니다. 
4. 모달 시트 왼쪽 목록에서 **Function Keys**를 선택합니다. 
5. 토글 스위치를 켭니다. 
**"F1, F2 등의 키를 표준 기능 키로 사용합니다"** 

6. **완료**를 클릭합니다. 

```
┌─────────────────────────────────────────────────────────────┐
│  Keyboard Shortcuts                                         │
├──────────────────────────────┬──────────────────────────────┤
│  Keyboard Navigation         │  Use F1, F2, etc. keys as    │
│  Modifier Keys               │  standard function keys  [ON]│
│  Function Keys          ◄─── │                              │
│  Spotlight                   │  When this option is on,     │
│  Mission Control             │  press the Fn key to use the │
│  App Shortcuts               │  special features printed    │
│                              │  on each key.                │
│                              │                     [ Done ] │
└──────────────────────────────┴──────────────────────────────┘
```
 

*결과*: 이제 `F5`을 누르면 ATBCmder에서 복사가 직접 실행됩니다. 밝기나 볼륨을 조정하려면 키를 누른 상태에서 `Fn`을 누르세요.

#### 해결 방법 3: 기본 macOS `Cmd` 해당 키 사용

시스템 키보드 설정을 변경하지 않으려는 경우 ATBCmder는 모든 핵심 작업에 대해 기본 macOS 키보드 단축키를 제공합니다. 

- **복사본**: `Cmd+C` / `Cmd+V`(또는 표준 `F5`) 
- **이동**: `Cmd+C` ➔ `Cmd+Option+V` (`⌥⌘V` 이동 붙여넣기) 
- **삭제**: `Cmd+Delete` (`⌘⌫`) 
- **새 폴더**: `Shift+Cmd+N` (`⇧⌘N`) 
- **이름 바꾸기**: `F2` 또는 `Return` 
- **일괄 다중 이름 바꾸기**: `Ctrl+M` (`⌃M`) 또는 `Cmd+M` (`⌘M`) 
- **기본 설정**: `Cmd+,` (`⌘,`) 
- **탭 닫기**: `Cmd+W` (`⌘W`) 

---

### 3.5 다른 드라이브와 동일한 드라이브 간 파일 이동

사용자들이 자주 묻는 질문은 동일한 폴더 내에서 20GB 파일을 이동하는 데 몇 초도 걸리지 않는 반면, 동일한 파일을 외부 드라이브나 네트워크 공유로 이동하는 데 몇 분이 걸리는 이유입니다.

#### 볼륨 내 이동(동일 드라이브/APFS 파티션)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              INTRA-VOLUME MOVE (SAME PARTITION)                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Source: /Users/brain/Downloads/BigFile.iso   ➔ Target: /Users/brain/Movies/          │
│                                                                                        │
│   1. POSIX rename() system call updates filesystem inode directory table.              │
│   2. Physical data blocks on the SSD are NEVER touched or copied.                      │
│   3. Execution time: < 5 milliseconds. Free disk space required: 0 bytes.              │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

소스 및 대상 경로가 **동일한 물리적 파일 시스템 볼륨**에 있는 경우 ATBCmder는 원자적 POSIX `rename()` 시스템 호출을 실행합니다. 운영 체제는 단순히 파일 시스템의 디렉토리 카탈로그에 있는 포인터 항목을 업데이트합니다. SSD의 물리적 데이터 클러스터는 이동되지 않습니다.

#### 볼륨 간 이동(다른 드라이브/파티션/네트워크 마운트)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              CROSS-VOLUME MOVE (ACROSS DRIVES)                         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   Source: /Users/brain/Downloads/BigFile.iso   ➔ Target: /Volumes/ExternalSSD/Movie/   │
│                                                                                        │
│   Stage 1: Binary Stream Copy (Read from Source SSD ➔ Write to Target External SSD)    │
│   Stage 2: Verification and Flush (fsync ensures complete write to external media)     │
│   Stage 3: Source Deletion (Source file is unlinked only after Stage 2 succeeds)       │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
 

다양한 파일 시스템 경계를 넘어 전송할 때(예: 내부 Mac SSD에서 외부 USB 드라이브, 네트워크 SMB 공유 또는 디스크 이미지로) 원자 포인터 업데이트는 물리적으로 불가능합니다. ATBCmder는 다단계 **복사-검증-삭제 파이프라인**을 실행합니다. 

1. **바이너리 스트림 읽기/쓰기**: 데이터는 소스 스토리지 컨트롤러에서 시스템 메모리를 통해 청크로 스트리밍되고 대상 스토리지 컨트롤러에 기록됩니다. 전송 시간은 전적으로 물리적 버스 속도에 따라 달라집니다(예: ~100MB/s의 USB 3.0과 ~2,800MB/s의 Thunderbolt 4). 
2. **버퍼 플러시 및 확인**: ATBCmder는 대상 파일 핸들에서 `fsync()`을 호출하여 캐시된 모든 데이터가 물리적 미디어에 기록되었는지 확인하고 바이트 수가 동등한지 확인합니다. 
3. **안전한 소스 삭제**: 대상 파일이 완전히 작성되고 검증된 후에만 ATBCmder는 원본 디스크에서 소스 파일을 삭제합니다.

#### 중요한 의미 및 안전 보장

* **여유 공간 요구 사항**: 작업이 시작되기 *전에* 전체 파일 페이로드를 저장할 수 있도록 대상 드라이브에 **충분한 여유 용량이 있어야** 합니다. 30GB 파일을 10GB만 남은 외장 드라이브로 이동하려고 하면 전송이 실패합니다. 
* **데이터 손실 제로 보장**: 실수로 외부 드라이브의 플러그를 뽑거나 전송 중에 대상 저장소의 공간이 부족한 경우 ATBCmder는 즉시 작업을 중단하고 소스 파일을 **완전히 손상되지 않은 상태로** 남겨두고 일부 대상 파일을 제거한 다음 명확한 오류 대화 상자를 보고합니다. 
* **백그라운드 큐 모니터링(`cm_OperationsPanel`)**: 장기 실행 볼륨 간 이동은 비동기 백그라운드 작업자 스레드(`FileOpWorker`)에서 실행됩니다. 사용자 인터페이스를 잠그지 않고도 실시간 전송 속도, 남은 시간, 전송 일시 중지/재개 또는 후속 작업 대기열을 모니터링할 수 있습니다. 

---

### 3.6 추가 자주 묻는 질문

#### Q1: 왼쪽 패널과 오른쪽 패널 간에 초점을 어떻게 전환합니까?

**`Tab`** (`⇥`) 키를 누릅니다. 포커스는 활성 파일 테이블과 비활성 파일 테이블 사이를 즉시 전환합니다. 활성 패널에는 강조 표시된 테두리 강조 표시와 초점이 맞춰진 상태 표시줄 텍스트가 표시됩니다.

#### Q2: 왼쪽 패널과 오른쪽 패널의 내용을 어떻게 바꾸나요?

**`Ctrl+U`**(`⌃U`)을 누르거나 **`cm_Exchange`** 명령을 실행합니다. 왼쪽 및 오른쪽 패널의 디렉터리, 폴더 탭, 커서 위치가 즉시 교체됩니다. 패널 너비를 정확히 50/50 분할로 동일하게 하려면 수직 중간 분할 막대의 아무 곳이나 두 번 클릭합니다.

#### Q3: 와일드카드 패턴을 사용하여 파일을 어떻게 선택합니까?

키보드에서 **`+`** 키를 누르세요(또는 **표시 ➔ 그룹 선택...** / `cm_MarkPlus` 선택). `*.pdf` 또는 `photo_2026_*.jpg`과 같은 와일드카드 패턴을 입력합니다. 패턴과 일치하는 파일을 선택 취소하려면 **`-`** 키(`cm_MarkMinus`)를 누르세요. 현재 선택을 반전하려면 **`*`**(`cm_MarkInvert`)을 누르세요.

#### Q4: 숨겨진 도트 파일의 가시성을 어떻게 전환합니까?

**`Cmd+H`**(`⌘H`) 또는 **`Cmd+Shift+Period`**(`⇧⌘.`)을 누르거나 **`cm_ShowSysFiles`** 명령을 실행합니다. 숨겨진 Unix 파일(`.zshrc`, `.gitignore`, `.env`과 같이 점으로 시작하는 파일)은 표시 상태와 숨김 상태 사이를 즉시 전환합니다.

#### Q5: 현재 디렉터리에서 macOS 터미널 창을 어떻게 열 수 있나요?

**`Ctrl+J`**(`⌃J`)을 누르거나 **`cm_RunTerm`** 명령을 실행합니다. ATBCmder는 현재 작업 디렉터리가 활성 파일 패널의 정확한 경로로 설정된 새로운 macOS 터미널(또는 iTerm2) 세션을 생성합니다.

#### Q6: ATBCMder는 Intel(x86_64) Mac을 지원합니까?

현재 ATBCmder는 Apple의 통합 메모리, Metal 하드웨어 가속 및 Neural Engine 하위 시스템을 완벽하게 활용하기 위해 **Apple Silicon(M1/M2/M3/M4, ARM64 아키텍처)** Mac용으로 기본적으로 독점적으로 컴파일되었습니다. **Intel(x86_64) Mac은 현재 지원되지 않습니다.** 

---

## 4. 전문가 팁 및 시스템 유지 관리 체크리스트

ATBCMder가 기업 워크플로우 전체에서 최고 속도로 성능을 유지하려면 다음을 수행하십시오. 

- **주간 캐시 유지 관리**: 고해상도 카메라 카드를 자주 탐색하는 경우 **구성 ➔ 옵션 ➔ 썸네일 ➔ 썸네일 캐시 지우기**를 통해 주기적으로 임시 썸네일 캐시를 지워 디스크 공간을 확보하세요. 
- **키체인 감사**: 원격 SFTP 또는 SMB 서버에서 비밀번호를 교체하는 경우 **네트워크 ➔ 네트워크 연결 관리...**를 통해 ATBCmder에서 자격 증명을 업데이트하세요. 편집하고 저장하면 macOS 키체인의 해당 자격 증명 항목이 원활하게 업데이트됩니다. 
- **백그라운드 큐 최적화**: 1Gbps 또는 10Gbps 네트워크를 통한 수 기가바이트 전송의 경우 **구성 ➔ 옵션 ➔ 파일 작업**에서 청크 버퍼 크기를 조정하여 버스 포화도를 최대화합니다. 
- **UNIX 권한 유지**: macOS APFS 드라이브 간에 스크립트 또는 컴파일된 바이너리를 복사할 때 복사 대화 상자(`F5`)에서 **파일 특성 및 권한 유지**가 선택되어 있는지 확인하고 실행(`chmod +x`) 플래그를 자동으로 유지합니다. 

--- 

<div align="center"> 
<p><strong>ATBCmder 사용자 가이드 및 문서 포털</strong></p> 
<p> 
<a href="index.md">&larr; 문서 포털로 돌아가기</a> &nbsp;&bull;&nbsp; 
<a href="getting_started.md">1장: 기본 사항</a> &nbsp;&bull;&nbsp; 
<a href="keyboard_shortcuts.md">8장: 바로가기</a> &nbsp;&bull;&nbsp; 
<a href="download.md">10장: 다운로드 및 설치 &rarr;</a> 
</p> 
</div>