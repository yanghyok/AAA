# Do Better Things — Joint Camp Design System

> 5/16-17 합동 AX Bootcamp 데모용 브랜드 디자인 가이드. PDF·HTML·슬라이드 어떤 산출물이든 이 파일을 `@`로 호출하면 동일한 브랜드 톤이 적용된다.

---

## Overview

Do Better Things(DBT)의 디지털 표면은 **크림 배경 (`{colors.canvas}` — #F3F2ED)** 위에 **딥 포레스트 그린 (`{colors.forest}` — #1B3B36)** 타입을 얹는 에디토리얼 구조다. 페이지 전체에 강한 색을 칠하지 않고 — 큰 여백, 가는 헤어라인, 그리고 한 곳에만 등장하는 **머티드 레드 액센트 (`{colors.accent}` — #D45D5D)** 가 브랜드 시그니처다. AX 캠프 진행이 다업종이라는 점을 그대로 반영해, 어느 도메인의 보고서를 만들어도 톤이 흐트러지지 않도록 **타이포 + 여백 + 한 점의 액센트**만으로 권위를 만든다.

브랜드 voltage는 색이 아니라 **활자의 무게 대비**에서 나온다. 본문은 light(300), 헤드라인은 semibold(600). 큰 헤드라인은 sentence case 유지 — 한글 가독성을 우선한다. 영문 라벨(CATEGORY·VIEW·SECTION)만 UPPERCASE + 1.2px 트래킹이 들어가 "에디토리얼 매거진" 톤을 만든다.

Voice는 "Sense × AI = Better Work". 데이터를 통해 의사결정을 더 빠르게 — 화려한 차트보다 **한 줄 헤드라인 + 비교 가능한 표**가 우선. 페이지에 박힌 단 하나의 #D45D5D 점이 "이게 가장 우려되는 한 곳이다"를 말한다.

## Key Characteristics

- **크림 캔버스** (`{colors.canvas}` — #F3F2ED) 위에 포레스트 타입. 흰색은 사용하지 않는다 — 종이 같은 따뜻한 톤이 브랜드의 기본.
- **딥 포레스트** (`{colors.forest}` — #1B3B36) 가 활자의 기본 잉크 컬러. 너무 푸르지도, 너무 검지도 않은 깊은 녹색.
- **머티드 레드** (`{colors.accent}` — #D45D5D) 는 한 페이지에 1~2회만 사용. 헤드라인의 강조 토큰·표의 위험 알림·CTA 버튼 라벨에만. 면으로 칠하지 않는다.
- 헤드라인은 sentence case + semibold(600). 영문 라벨만 UPPERCASE + letter-spacing 1.2px.
- 본문은 light(300) — 300 본문 vs 600 헤드라인의 무게 대비가 브랜드 톤의 핵심.
- 표는 헤어라인 (`{colors.hairline}` — #D9D6CB) 1px 만으로 구획. 박스·그림자 사용 금지. 표가 종이처럼 보여야 한다.
- 면 그림자·둥근 모서리 거의 사용하지 않는다. `{rounded.none}` (0px) 기본, 알림·태그 칩에만 `{rounded.full}`.
- 여백이 voltage. 섹션 사이 `{spacing.section}` 56px / 카드 안쪽 `{spacing.xl}` 32px / 행 간 `{spacing.md}` 16px.
- 차트는 단색 (`{colors.forest}` + `{colors.accent}` 두 톤). 다색 팔레트 사용 금지.
- "오늘 가장 우려되는 한 곳" 1줄이 페이지 최상단. 페이지를 펴면 가장 먼저 읽힌다.

## Colors

### Brand & Accent
- **Forest** (`{colors.forest}` — #1B3B36): 모든 텍스트의 기본 잉크. 본문·헤드라인·표 셀 라벨.
- **Accent** (`{colors.accent}` — #D45D5D): 페이지당 1~2회만. 헤드라인의 강조 단어, 위험 표시 (🔴), 버튼 라벨. 면 채우기 금지.
- **Dark Forest** (`{colors.forest-dark}` — #0A1F1C): 다크 모드 캔버스 또는 푸터 띠. 본 가이드 출력물(PDF)에서는 거의 사용 X.

### Surface
- **Canvas** (`{colors.canvas}` — #F3F2ED): 종이 같은 크림 톤. 모든 페이지의 기본 배경.
- **Surface Soft** (`{colors.surface-soft}` — #EFEEE6): 카드·강조 영역. 캔버스와 차이가 거의 없어서 "면이 살짝 떠 있는" 느낌.
- **Surface Card** (`{colors.surface-card}` — #E9E6DA): 표 헤더 띠, 박스형 카드 한정.

### Hairlines & Borders
- **Hairline** (`{colors.hairline}` — #D9D6CB): 1px 디바이더. 표 셀 구획, 섹션 사이 라인.
- **Hairline Strong** (`{colors.hairline-strong}` — #B7B3A3): 표의 헤더 아래 굵은 라인 (1.5px).

### Text
- **Ink** (`{colors.ink}` — #1B3B36): 기본 텍스트 — Forest와 동일.
- **Body** (`{colors.body}` — #2D4944): 본문 강조하지 않는 라인. 약간 옅은 포레스트.
- **Muted** (`{colors.muted}` — #6B7E78): 캡션·메타데이터.

### Semantic
- **Risk** (`{colors.risk}` — #D45D5D): 위험·지연·이상 신호. Accent와 같은 hex (브랜드 일관).
- **Caution** (`{colors.caution}` — #C7A24A): 임박·주의. 머스타드 톤.
- **OK** (`{colors.ok}` — #3F7A56): 정상·완료. 포레스트 계열의 살짝 밝은 변형.

## Typography

### Font Family
**Pretendard** 를 본 가이드의 기본으로 한다. 한글·영문·숫자 모두 한 글꼴에서 처리. 영문 헤드라인 대안으로 **Inter** 도 호환.

Fallback stack: `Pretendard, "Apple SD Gothic Neo", Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`.

가중치 두 축만 사용 — **600 (Semibold) for headlines** + **300 (Light) for body**. 400/500 사용 금지. 무게 대비가 브랜드 시그니처.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 48px | 600 | 1.15 | -0.5px | 표지 헤드라인 (1페이지) |
| `{typography.display-lg}` | 36px | 600 | 1.2 | -0.3px | 섹션 진입 헤드라인 |
| `{typography.display-md}` | 28px | 600 | 1.25 | -0.2px | 서브섹션 |
| `{typography.title-lg}` | 20px | 600 | 1.35 | 0 | 카드 제목, 표 캡션 |
| `{typography.title-md}` | 17px | 600 | 1.4 | 0 | 표 헤더, 강조 본문 |
| `{typography.body-md}` | 14px | 300 | 1.55 | 0 | 기본 본문 |
| `{typography.body-sm}` | 12px | 300 | 1.5 | 0 | 표 셀, 캡션 |
| `{typography.label-uppercase}` | 11px | 600 | 1.3 | 1.2px | 영문 카테고리·섹션 라벨 (UPPERCASE) |
| `{typography.number-display}` | 32px | 600 | 1.0 | -1.0px | 헤드라인 수치 (한 자리수 KPI) |
| `{typography.button}` | 13px | 600 | 1.0 | 0.8px | 버튼 라벨 |
| `{typography.caption}` | 11px | 300 | 1.4 | 0.3px | 출처·각주 |

### Principles
- **헤드라인은 sentence case**. UPPERCASE는 영문 라벨에만.
- 무게 두 축(600/300) 만 사용. 400 사용 금지 — 무게 대비가 흐려진다.
- 숫자 헤드라인(`{typography.number-display}`)은 -1px 트래킹으로 살짝 압축. "기억에 남는 한 자리수" 톤.

### Note on Font Substitutes
Pretendard 미설치 환경에서는 시스템 글꼴 fallback이 자동 적용된다. PDF 출력 시 Pretendard webfont(또는 로컬 설치본)을 인라인 또는 link로 포함하면 톤이 유지된다.

## Layout

### Spacing System

| Token | Value | Use |
|---|---|---|
| `{spacing.xs}` | 4px | 칩·태그 내부 |
| `{spacing.sm}` | 8px | 표 셀 내부, 인라인 아이콘 간격 |
| `{spacing.md}` | 16px | 본문 줄 간격, 카드 내부 행 간격 |
| `{spacing.lg}` | 24px | 카드 사이, 표 위아래 |
| `{spacing.xl}` | 32px | 카드 안쪽 padding, 헤드라인 아래 |
| `{spacing.xxl}` | 48px | 섹션 헤드라인 위 |
| `{spacing.section}` | 56px | 섹션 사이 |
| `{spacing.page}` | 72px | 페이지 좌우·상하 마진 (A4 기준) |

### Grid & Container
- A4 세로 기준 본문 폭 약 540pt (좌우 마진 36pt 적용 시).
- 3컬럼 카드 그리드: 카드 간격 `{spacing.lg}` (24px), 카드 내부 `{spacing.xl}` (32px).
- 표는 폭 100%, 셀 padding 좌우 12px / 상하 10px.

### Whitespace Philosophy
- 흰 공간 = 메시지의 일부. 차지 않는 부분이 권위를 만든다.
- 카드를 박스로 감싸지 않고 헤어라인 한 줄로 끊는다.
- 표 위아래는 `{spacing.lg}` 보장 — 표가 본문에 붙어 보이지 않도록.

## Elevation & Depth

| Level | Use | Spec |
|---|---|---|
| 0 | 기본 표면 | 그림자 없음, hairline 1px |
| 1 | 강조 카드 | `box-shadow: 0 1px 0 {colors.hairline}` (라인 한 줄만, 그림자 X) |
| 2 | 핵심 KPI 박스 | 1.5px hairline-strong + 좌측 4px accent 띠 |

### Decorative Depth
- 면 그림자는 없다. "떠 있는 느낌"은 hairline의 굵기와 좌측 액센트 띠로만 표현.
- 카드 좌측 4px accent 띠는 페이지당 1개만 — "이게 핵심이다" 신호.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0 | 기본. 표·카드·헤드라인 모두. |
| `{rounded.sm}` | 4px | 인라인 코드, 작은 칩 한정 |
| `{rounded.full}` | 9999px | 상태 칩 (🔴/🟡/🟢), 버튼 |

### Photography Geometry
- 사진을 쓰는 경우 직사각형 풀블리드. 둥근 모서리 X.
- 사진 캡션은 사진 바로 아래 muted 톤으로 한 줄.

## Components

### Top Header (PDF/HTML 출력물 상단)
- 좌측: "Do Better Things" 워드마크 — Forest 컬러, `{typography.label-uppercase}`.
- 우측: 발행일 — Muted 컬러, `{typography.caption}`.
- 두 요소 사이 hairline 1px (페이지 상단 라인).

### Headline Bar
- `{typography.display-xl}` 1줄 + 한 줄 부제 (`{typography.title-md}` Body 컬러).
- 강조 단어 1개만 Accent 컬러로.
- 헤드라인 위쪽에 영문 카테고리 라벨 (`{typography.label-uppercase}`, Accent 컬러).

### KPI Numbers
- `{typography.number-display}` 숫자 + `{typography.body-sm}` 라벨.
- 라벨은 숫자 아래 4px 간격, Muted 컬러.
- 위험 KPI는 숫자만 Accent 컬러.

### Tables
- 헤더 행: 배경 `{colors.surface-card}`, 폰트 `{typography.title-md}`, 아래 `{colors.hairline-strong}` 1.5px.
- 셀 행: 캔버스, 셀 사이 `{colors.hairline}` 1px.
- 위험 행: 좌측 4px Accent 띠 (한 행만 강조).
- 숫자 셀: 우측 정렬, 단위는 셀 우측에 작게 (12px, Muted).

### Status Chips
- 🔴 위험·지연: 배경 #FCEAE9 / 텍스트 `{colors.accent}` / `{rounded.full}` / padding 4px 10px.
- 🟡 임박·주의: 배경 #FBF1DC / 텍스트 `{colors.caution}`.
- 🟢 정상·완료: 배경 #E6EFE6 / 텍스트 `{colors.ok}`.

### Buttons (HTML 출력 한정)
- Primary: Forest 배경 + Canvas 텍스트, `{rounded.full}`, padding 10px 24px, `{typography.button}`.
- Secondary: Canvas + Forest 1px 외곽선 + Forest 텍스트.
- Risk action: Accent 배경 + Canvas 텍스트.

### Footer
- 좌측: "Sense × AI = Better Work" — `{typography.caption}` Muted.
- 우측: 페이지 번호 — `{typography.caption}` Muted.
- 위쪽 hairline 1px.

## Do's and Don'ts

### Do
- 헤드라인 한 단어만 Accent로.
- 무게 두 축(600/300)만.
- 표는 hairline만, 박스·그림자 없음.
- 페이지 최상단에 "오늘 한 줄" 헤드라인.
- 영문 라벨만 UPPERCASE + 1.2px 트래킹.
- 위험·지연은 좌측 4px 액센트 띠 + 칩 한 개.
- 여백을 두려워하지 않는다.

### Don't
- 흰색(#FFFFFF) 배경 사용 금지. 항상 크림.
- Accent를 면으로 칠하지 않는다 (스트라이프·외곽선 한정).
- 다색 차트 사용 금지 (Forest + Accent 두 톤).
- 폰트 가중치 400·500 사용 금지.
- 한글 헤드라인 UPPERCASE 시도 금지 (안 됨).
- 표 셀에 둥근 모서리 적용 금지.
- 페이지에 액센트 컬러를 두 곳 이상 분산 금지 ("어디를 봐야 하지?" 가 된다).

## Responsive Behavior

### Breakpoints

| Breakpoint | Width | Behavior |
|---|---|---|
| Print A4 | 595pt × 842pt | 본 가이드의 기준 출력 |
| Desktop | ≥ 1024px | 3컬럼 카드, 표 전체 가로 |
| Tablet | 640–1023px | 2컬럼 카드, 표 가로 스크롤 |
| Mobile | < 640px | 1컬럼, KPI 가로 정렬, 표는 카드형으로 변환 |

### Touch Targets
- 모바일 버튼·칩은 최소 44pt 높이.
- 인라인 링크는 24pt 이상 hit-area.

### Collapsing Strategy
- 모바일에서 표는 헤더-셀 페어로 카드 변환. 각 행이 카드 한 장.
- KPI는 가로 그리드 유지 (스크롤 X) — 가로 폭 줄어들면 폰트 크기 자동 -2pt.

### Image Behavior
- 사진은 모바일에서 풀블리드 유지. 캡션은 사진 아래 한 줄.

## Iteration Guide

1. **새 출력물 만들 때**: 페이지 최상단 "오늘 한 줄"부터 잡는다. 헤드라인이 정해지면 나머지는 부수적.
2. **차트 추가할 때**: 단색(Forest) 기본, 위험 표시만 Accent. 다색 팔레트 금지.
3. **표가 길어질 때**: 8행 넘으면 카드 변환 또는 분리. 가독성 우선.
4. **위험·지연 표시**: 좌측 4px 띠 + 칩 1개 + 헤드라인 강조 단어 — 페이지당 1회.
5. **외부 공유용 변형**: 헤더의 워드마크를 발행 채널 톤에 맞게 교체. Accent 컬러는 유지.
6. **다크 변형이 필요할 때**: 캔버스를 `{colors.forest-dark}` (#0A1F1C), 텍스트를 Canvas로. Accent는 동일.
7. **다국어**: 영문 헤드라인은 sentence case + semibold 유지. 영문 카테고리 라벨만 UPPERCASE.
8. **첨부 자료**: 표 분리·세부 데이터는 별지 또는 별첨 시트로. 본문은 1페이지를 넘기지 않는다.

## Known Gaps

- 차트 라이브러리 토큰화는 본 가이드 범위 밖. Forest + Accent 두 톤 규칙만 따른다.
- 다크 모드 표면 토큰은 PDF 출력물에서 거의 사용되지 않아 1개(forest-dark)만 정의.
- 모션·인터랙션 가이드는 본 워크스페이스가 정적 출력물 위주이므로 본 가이드에선 다루지 않음.
- 일러스트레이션·아이콘 시스템은 아직 미정. 표·헤어라인·타이포만으로 톤을 만든다.
