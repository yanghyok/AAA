# Skills

이 폴더는 이 워크스페이스 전용 스킬을 담습니다.

## Skills란?

Skills는 Claude Code가 **키워드 기반으로 자동 트리거**하는 기능 모음입니다.
구 슬래시 커맨드 방식(`/daily-note`)을 대체합니다.

- 자연어 호출: "오늘 daily note 만들어줘"
- Claude가 description에 있는 키워드를 감지하여 자동 실행
- 각 스킬은 `SKILL.md`를 루트에 두고, 필요시 `scripts/`, `resources/` 같은 하위 폴더 사용

## 파일 구조

```
.claude/skills/
├── README.md             # 이 파일
└── [skill-name]/
    ├── SKILL.md          # 스킬 정의 (YAML frontmatter + 설명 + 실행 절차)
    ├── scripts/          # (선택) 실행 스크립트
    └── resources/        # (선택) 참고 자료, 템플릿
```

## SKILL.md 구조

```yaml
---
name: skill-name
description: 이 스킬이 언제 트리거되는지 명확히. "X를 언급하면 자동 실행" 형식 권장.
---

# 스킬 제목

본문 — 실행 절차, 예시, 주의사항
```

## 전역 vs 프로젝트 스킬

- **전역**: `~/.claude/skills/` — 모든 프로젝트에서 적용
- **프로젝트**: 이 폴더 — 이 워크스페이스에서만 적용

프로젝트 스킬이 전역 스킬과 이름이 같으면 프로젝트 것이 우선.

## 포함된 스킬

*(아직 없음 — v2 업데이트 중. 포팅 예정 목록은 작업 로그 참조)*
