# Agents

이 폴더는 이 워크스페이스 전용 서브에이전트를 담습니다.

## Agents란?

Agents는 **독립된 컨텍스트에서 복잡한 작업을 수행**하는 Claude의 하위 인스턴스입니다.

- 메인 세션의 컨텍스트 오염 방지 (큰 리서치, 병렬 작업 등)
- 명시적 위임: `research-worker로 조사해줘`
- 암묵적 위임: description에 맞는 작업을 Claude가 자동으로 위임

## 파일 구조

```
.claude/agents/
├── README.md             # 이 파일
└── [agent-name].md       # 각 에이전트 1파일 (YAML frontmatter + 시스템 프롬프트)
```

## 에이전트 파일 구조

```yaml
---
name: agent-name
description: 이 에이전트를 언제 쓰는지. 메인이 위임 판단할 때 이 설명을 봄.
tools: Read, Write, Bash, ...  # 허용 도구
---

# 에이전트 시스템 프롬프트

역할, 절차, 출력 형식 등
```

## 포함된 에이전트

*(아직 없음 — v2 업데이트 중. 포팅 예정: research-worker, analysis-worker, content-worker 등)*
