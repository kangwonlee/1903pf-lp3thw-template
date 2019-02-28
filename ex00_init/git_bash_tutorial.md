# 실습 안내

* 해당 **저장소**에는 교재 실습을 위한 파일이 준비되어 있음
* `git` 프로그램을 이용, 웹사이트의 **원격저장소**로부터 실습용 PC에 **지역저장소**를 만들어서 작업 후 다시 **원격저장소**에 반영

## 명령행 `git` 설치 파일 링크

* [전체 OS](https://git-scm.com/download/)
* [Windows](https://git-scm.com/download/win)

## 자주 사용하는 `git bash` 명령 일람

`git bash` 는 Windows 에서 `git` 명령을 키보드 입력으로 실행할 수 있는 창이라고 생각할 수 있음

| 작업 | 명령 |
|:----------:|:----------------------------------------------:|
| `git bash` 시작 | 특정 폴더를 선택<br>오른쪽 마우스 버튼을 누름<br>메뉴에서 `Git Bash Here` 선택 |
| 현재 작업 폴더 확인 | `pwd` 입력 후 <kbd>Enter</kbd> |
| `pwd`에 대한 도움말 | `pwd --help` |
| 현재 작업 폴더 내용 확인  (LS 의 소문자) | `ls` |
| 현재 작업 폴더에 새 폴더 만들기 | `mkdir temp` |
| 특정 폴더로 작업 폴더 변경 | <code>cd tem<kbd>Tab</kbd></code> |
| 상위 폴더로 이동 | `cd ..` |
| 비어 있는 특정 폴더 삭제 | `rmdir temp` |
| `git` 실행 파일의 정확한 위치 | `which git` |
| `python` 실행 파일의 정확한 위치 | `which python` |
| 문서 파일의 내용 확인 | `cat ~/.bashrc` |
| 여러 명령을 이어서 실행 | `ls ; cd ..`<br>`mkdir test && cd temp` |

## 실습 준비 : 저장소 받아오기

|                 작업                 |                      명령                   |
|:------------------------------------:|:-------------------------------------------:|
| 현재 작업 폴더 확인                    | `pwd`                                      |
| 현재 작업 폴더 내용 확인 (LS 의 소문자) | `ls`                                       |
| (Windows) D: drive 로 이동            | `cd /d/`                                   |
| 현재 작업 폴더 내용 확인                | `ls`                                      |
| 현재 작업 폴더에 새 폴더 만들기         | `mkdir <폴더 이름>`                         |
| 특정 폴더로 이동                       | `cd <폴더 이름>`                            |
| 현재 폴더 아래에 원격 저장소를 복제하여 지역저장소 생성 | `git clone <원격 저장소 url>` |
| 현재 작업 폴더 내용 확인                | `ls`                                    |
| 지역 저장소 폴더로 이동                 | `cd <지역 저장소 폴더이름>`               |
| 현재 작업 폴더 내용 확인                | `ls`                                    |
| 지역 저장소 변경 이력 확인              | `git log`                               |
| 사용자 이름 설정 (commit 이전)          | `git config user.name "<사용자 이름>"`    |
| 사용자 email 설정 (commit 이전)        | `git config user.email "<사용자 email>"` |

[![git bash clone video](https://i.ytimg.com/vi/fR0jyqhsU6w/hqdefault.jpg)](https://youtu.be/fR0jyqhsU6w)

## 수정사항 등록

![Git Data Transport Commands](https://images.osteele.com/2008/git-transport.png)

* (`notepad` 등) 적당한 편집기로 지역 저장소 안의 파일을 임의로 변경한 후 계속

|                 작업                 |                      명령                      |
|:----------:|:----------------------------------------------:|
| 현재 지역 저장소 상태 확인 | `git status` |
| 지정되지 않은 변경 사항 중 확인 | `git diff` |
| 지역 저장소의 현재 작업 폴더에 있는 어떤 file 을<br>다음 등록 `commit` 대상으로 지정 `stage` | `git add <file>` |
| 변경 사항을 관찰하며 지정 `stage` | `git add -p` |
| 지정 상태를 해제하고 싶은 경우 (변경 사항은 유지) | `git reset <file>` |
| 등록 대기중인 지정 사항 확인 | `git diff --staged` |
| 지정된 변경사항을 지역 저장소에 등록 | `git commit -m "<변경 내용 설명>"` |
| 지정 사항을 지역 저장소에 등록<br>설명은 (`vi`) 편집기로 입력 |  `git commit`<kbd>Enter</kbd><br><kbd>i</kbd><변경 내용 설명><kbd>Enter</kbd><br><kbd>ESC</kbd>`:wq`<kbd>Enter</kbd> |
| 지역 저장소 변경 이력 확인 | `git log` |
| 새로운 지역 저장소 변경 이력을 원격 저장소로 송신<br>해당 원격 저장소에 쓰기 권한 필요 | `git push` |

* 웹 브라우저로 자신의 원격 저장소에 변경 사항 적용을 확인
* commit 할 때 변경 내용 설명에는 되도록 특수문자(` \ % 등)는 사용하지 않는 것을 추천

[![git bash add commit push](https://i.ytimg.com/vi/TcULRXQHtzo/hqdefault.jpg)](https://youtu.be/TcULRXQHtzo?t=17)
