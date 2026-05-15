"""
Joint Camp 2026-05 sample data generator.

Two storylines share this folder:
  (A) Marketing weekly review — competitor SNS monitoring + own SNS posts.
  (B) Project tracker — 3D animation studio works, contracts, meeting action items.

All CSVs use utf-8-sig (Excel-friendly BOM).
random.seed fixed for reproducibility.
"""

from __future__ import annotations

import csv
import random
from datetime import date, datetime, timedelta
from pathlib import Path

OUT = Path(__file__).parent
random.seed(20260516)


# ---------------------------------------------------------------------------
# Storyline A — Marketing weekly review (Kim Banya, De:maf 입사 첫주)
# ---------------------------------------------------------------------------

# 1) competitors_master.csv  — 모니터링 대상 브랜드 마스터
competitors_master_rows = [
    # brand_id, brand_name, country, category, ig_handle, ig_followers, founded_year, monitoring_priority, note
    ("BR001", "Glow Recipe",    "US", "스킨케어",    "@glowrecipe",      1850000, 2014, "★★★", "K-beauty 코어, US 메인스트림 진입"),
    ("BR002", "Tower 28",       "US", "스킨/메이크업", "@tower28beauty",    580000, 2019, "★★★", "민감성 피부 친화, Sephora 핵심"),
    ("BR003", "Fenty Skin",     "US", "스킨케어",    "@fentyskin",       2300000, 2020, "★★",  "Rihanna, 인플루언서 모델"),
    ("BR004", "Drunk Elephant", "US", "스킨케어",    "@drunkelephant",   1200000, 2012, "★★",  "성분 중심 마케팅"),
    ("BR005", "Rare Beauty",    "US", "메이크업",   "@rarebeauty",      4100000, 2020, "★★★", "Selena Gomez, 정서·웰니스 결합"),
    ("BR006", "Topicals",       "US", "기능성",     "@topicals",         610000, 2020, "★★★", "민감/문제성 피부, TikTok 강세"),
    ("BR007", "Beauty of Joseon","KR", "스킨케어",   "@beautyofjoseon",   980000, 2019, "★★★", "글로벌 K-beauty 1위 라인"),
    ("BR008", "TIRTIR",         "KR", "베이스/스킨", "@tirtir.korea",     720000, 2018, "★★",  "쿠션·앰플 TikTok 바이럴"),
    ("BR009", "AMUSE",          "KR", "메이크업",   "@amuse.official",   430000, 2018, "★★",  "비건 라인"),
    ("BR010", "ROUND LAB",      "KR", "스킨케어",   "@roundlab_official",520000, 2017, "★★",  "성분 narrative, 약산성"),
    ("BR011", "Mediheal",       "KR", "마스크팩",   "@mediheal_official",890000, 2009, "★",   "마스크팩 카테고리 강자"),
    ("BR012", "ANUA",           "KR", "스킨케어",   "@anua_official",    410000, 2018, "★★★", "어성초 토너 글로벌 히트"),
    ("BR013", "Tirtir Japan",   "JP", "베이스",     "@tirtir_japan",     150000, 2022, "★",   "JP 진출 사례"),
    ("BR014", "Cosrx",          "KR", "스킨케어",   "@cosrx",           1700000, 2014, "★★",  "Amazon US 1위 K-beauty"),
    ("BR015", "Naturium",       "US", "스킨케어",   "@naturium",         680000, 2019, "★★",  "Susan Yara 인플루언서 창업"),
    ("BR016", "U Beauty",       "US", "기능성",     "@ubeauty",          230000, 2019, "★",   "고가 라인 비교군"),
    ("BR017", "Saie",           "US", "메이크업",   "@saiehello",        510000, 2019, "★★",  "클린 메이크업"),
    ("BR018", "Innisfree",      "KR", "스킨/메이크업","@innisfreeofficial",1200000, 2000, "★",   "1세대 K-beauty 비교군"),
    ("BR019", "Laneige",        "KR", "스킨케어",   "@laneige_kr",       820000, 1994, "★★",  "Sephora 강세 (슬리핑 마스크)"),
    ("BR020", "Then I Met You", "US", "스킨케어",   "@thenimetyou",       95000, 2018, "★",   "Soko Glam 창업자 라인"),
]

with (OUT / "competitors_master.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow([
        "brand_id", "brand_name", "country", "category",
        "ig_handle", "ig_followers", "founded_year",
        "monitoring_priority", "note",
    ])
    w.writerows(competitors_master_rows)


# 2) competitor_posts.csv  — 경쟁사 SNS 모니터링 기록 (최근 1주)
post_formats = ["릴스", "이미지", "카드뉴스", "스토리하이라이트", "콜라보영상"]
themes = [
    "성분 narrative (vitamin C / niacinamide / mugwort)",
    "Before-After 사용 후기",
    "인플루언서 GRWM",
    "신제품 런칭 티저",
    "리뷰 모음 (UGC 큐레이션)",
    "성분 설명 (실험실/연구원 출연)",
    "K-beauty 루틴 소개",
    "비건/클린뷰티 메시지",
    "민감성 피부 사례",
    "병행 사용 루틴 데모",
    "팬덤 콘텐츠 (해시태그 챌린지)",
    "한정판 패키지 unbox",
    "Sephora/Amazon 입점 announcement",
    "TikTok Shop 라이브 클립",
    "글로벌 매거진 픽업",
]
hooks = [
    "성분", "텍스처", "결과 후기", "패키지", "가격", "한정판",
    "콜라보", "지속력", "민감성 안전", "비건",
]

competitor_post_rows = []
base = date(2026, 5, 8)
post_id = 1
for brand in competitors_master_rows:
    brand_id, brand_name, country, category, handle, followers, *_ = brand
    n_posts = random.randint(3, 6)
    for _ in range(n_posts):
        day = base + timedelta(days=random.randint(0, 6))
        fmt = random.choices(post_formats, weights=[5, 3, 2, 1, 1])[0]
        theme = random.choice(themes)
        hook = random.choice(hooks)
        # engagement scales with followers + post format + random
        base_rate = {"릴스": 0.045, "이미지": 0.018, "카드뉴스": 0.022, "스토리하이라이트": 0.008, "콜라보영상": 0.062}[fmt]
        likes = int(followers * base_rate * random.uniform(0.4, 2.4))
        comments = int(likes * random.uniform(0.012, 0.06))
        saves = int(likes * random.uniform(0.04, 0.18))
        shares = int(likes * random.uniform(0.02, 0.12))
        # surge flag — extraordinary post
        engagement_rate = (likes + comments + saves + shares) / followers if followers else 0
        surge = "Y" if engagement_rate > base_rate * 2.2 else "N"
        competitor_post_rows.append((
            f"P{post_id:04d}",
            day.isoformat(),
            brand_id,
            brand_name,
            country,
            handle,
            fmt,
            theme,
            hook,
            likes,
            comments,
            saves,
            shares,
            f"{engagement_rate*100:.2f}%",
            surge,
        ))
        post_id += 1

# inject a few standout posts for narrative
competitor_post_rows.append((
    f"P{post_id:04d}", "2026-05-12", "BR007", "Beauty of Joseon", "KR", "@beautyofjoseon",
    "릴스", "성분 narrative (vitamin C / niacinamide / mugwort)", "성분",
    412000, 18800, 96000, 41000, "57.93%", "Y",
)); post_id += 1
competitor_post_rows.append((
    f"P{post_id:04d}", "2026-05-13", "BR006", "Topicals", "US", "@topicals",
    "콜라보영상", "팬덤 콘텐츠 (해시태그 챌린지)", "민감성 안전",
    298000, 14200, 88000, 36500, "71.40%", "Y",
)); post_id += 1
competitor_post_rows.append((
    f"P{post_id:04d}", "2026-05-11", "BR012", "ANUA", "KR", "@anua_official",
    "릴스", "Before-After 사용 후기", "결과 후기",
    187000, 9200, 41000, 18800, "62.92%", "Y",
)); post_id += 1

random.shuffle(competitor_post_rows)
with (OUT / "competitor_posts.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow([
        "post_id", "post_date", "brand_id", "brand_name", "country", "ig_handle",
        "format", "theme", "main_hook",
        "likes", "comments", "saves", "shares",
        "engagement_rate", "surge_flag",
    ])
    w.writerows(competitor_post_rows)


# 3) own_posts.csv  — 자사 De:maf 콘텐츠 성과 (최근 4주)
demaf_accounts = [
    ("@demaf.official",  "KR",  85000),
    ("@demaf.us",        "US",  31000),
    ("@demaf.global",    "GLB", 22000),
]
demaf_themes = [
    "성분 narrative", "Before-After", "사용자 후기 큐레이션",
    "임상 결과 발표", "라이프스타일 (모닝 루틴)", "신제품 티저",
    "팀 소개 (창업자 출연)", "한정판 unbox",
]
own_rows = []
post_id = 1
for handle, country, followers in demaf_accounts:
    for day_offset in range(28):
        if random.random() > 0.55:  # 약 절반의 날만 발행
            continue
        day = date(2026, 4, 15) + timedelta(days=day_offset)
        fmt = random.choice(post_formats)
        theme = random.choice(demaf_themes)
        base_rate = {"릴스": 0.040, "이미지": 0.014, "카드뉴스": 0.019, "스토리하이라이트": 0.006, "콜라보영상": 0.055}[fmt]
        likes = int(followers * base_rate * random.uniform(0.3, 2.0))
        comments = int(likes * random.uniform(0.01, 0.05))
        saves = int(likes * random.uniform(0.05, 0.20))
        shares = int(likes * random.uniform(0.02, 0.10))
        reach = int(followers * random.uniform(0.45, 1.9))
        ctr = round(random.uniform(0.6, 4.5), 2)
        purchase_conv = round(random.uniform(0.05, 1.2), 2)
        own_rows.append((
            f"O{post_id:04d}",
            day.isoformat(),
            handle,
            country,
            fmt,
            theme,
            reach,
            likes,
            comments,
            saves,
            shares,
            f"{ctr}%",
            f"{purchase_conv}%",
            "https://instagram.com/demaf-mock/p/" + f"{post_id:04d}",
        ))
        post_id += 1

# inject high/low performers
own_rows.append((
    f"O{post_id:04d}", "2026-05-05", "@demaf.us", "US", "릴스", "Before-After",
    78000, 4200, 320, 1800, 540, "3.8%", "1.4%",
    "https://instagram.com/demaf-mock/p/hit1",
)); post_id += 1
own_rows.append((
    f"O{post_id:04d}", "2026-05-09", "@demaf.official", "KR", "콜라보영상", "신제품 티저",
    92000, 6800, 510, 3100, 980, "4.2%", "1.8%",
    "https://instagram.com/demaf-mock/p/hit2",
)); post_id += 1
own_rows.append((
    f"O{post_id:04d}", "2026-04-22", "@demaf.global", "GLB", "스토리하이라이트", "팀 소개 (창업자 출연)",
    8200, 110, 4, 28, 5, "0.4%", "0.05%",
    "https://instagram.com/demaf-mock/p/low1",
)); post_id += 1

random.shuffle(own_rows)
with (OUT / "own_posts.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow([
        "post_id", "post_date", "account_handle", "country",
        "format", "theme",
        "reach", "likes", "comments", "saves", "shares",
        "ctr", "purchase_conversion", "post_url",
    ])
    w.writerows(own_rows)


# 4) ad_campaigns.csv  — Meta/TikTok 광고 캠페인 최근 14일
campaigns = [
    ("CAM01", "Meta",   "US",  "Hero-Serum-Spring", "Reels Boost",  "신제품 세럼",       2200),
    ("CAM02", "Meta",   "US",  "BoF-Cluster-A",    "Conversion",    "Before-After 묶음",  3100),
    ("CAM03", "Meta",   "KR",  "Naver-Tie-In",     "Awareness",     "네이버 기획 연동",   1500),
    ("CAM04", "TikTok", "US",  "UGC-Topical",      "UGC Spark",     "민감성 케어 UGC",   2700),
    ("CAM05", "TikTok", "US",  "TT-Shop-Live",     "Live Promo",    "TT Shop 라이브",   1800),
    ("CAM06", "Meta",   "GLB", "Founder-Story",    "Brand Lift",    "창업자 스토리",     1200),
    ("CAM07", "TikTok", "JP",  "JP-Soft-Launch",   "Awareness",     "JP 초기 도달",      900),
]
camp_rows = []
for cam_id, ch, country, name, objective, theme, daily_budget in campaigns:
    for d in range(14):
        day = date(2026, 5, 2) + timedelta(days=d)
        spend = daily_budget * random.uniform(0.85, 1.12)
        impressions = int(spend * random.uniform(80, 220))
        clicks = int(impressions * random.uniform(0.012, 0.045))
        ctr = clicks / impressions * 100 if impressions else 0
        purchases = int(clicks * random.uniform(0.005, 0.04))
        revenue = purchases * random.uniform(48, 95)  # USD
        roas = revenue / spend if spend else 0
        camp_rows.append((
            cam_id, day.isoformat(), ch, country, name, objective, theme,
            round(spend, 2), impressions, clicks, f"{ctr:.2f}%",
            purchases, round(revenue, 2), f"{roas:.2f}",
        ))

with (OUT / "ad_campaigns.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow([
        "campaign_id", "date", "channel", "country", "campaign_name",
        "objective", "theme",
        "spend_usd", "impressions", "clicks", "ctr",
        "purchases", "revenue_usd", "roas",
    ])
    w.writerows(camp_rows)


# ---------------------------------------------------------------------------
# Storyline B — Project/Contract tracker (Cha Ji-hyun, 3D animation IP team)
# ---------------------------------------------------------------------------

# 5) projects_master.csv  — 작품/프로젝트 마스터 (디자인 회사·법률·HR 컨설팅 모두 호환되는 추상 단위)
projects = [
    # project_id, title, kind, partner_org, lead, kickoff_date, premiere_or_deliv, status, priority
    ("PRJ001", "별바라기 (애니메이션 시리즈)", "애니메이션", "ABC프로덕션",   "차지현", "2026-01-15", "2026-08-30", "제작중",    "★★★"),
    ("PRJ002", "달뜬밤 굿즈 펀딩",            "굿즈 펀딩", "텀블벅",        "차지현", "2026-03-02", "2026-06-15", "사전기획",  "★★★"),
    ("PRJ003", "노을여행 (단편)",            "애니메이션", "글로벌배급사X", "차지현", "2025-11-20", "2026-05-25", "개봉임박",  "★★★"),
    ("PRJ004", "포포의숲 시즌2",             "애니메이션", "스튜디오Y",     "차지현", "2026-02-10", "2026-12-20", "제작중",    "★★"),
    ("PRJ005", "리틀스타 IP 라이선싱",       "라이선싱",  "완구사Z",       "차지현", "2026-04-05", "2026-09-30", "협상중",    "★★"),
    ("PRJ006", "별바라기 OST 콜라보",        "음원 콜라보","음반사W",       "차지현", "2026-04-20", "2026-07-10", "협상중",    "★★"),
    ("PRJ007", "포포의숲 영문판 더빙",       "현지화",    "더빙스튜디오V", "차지현", "2026-03-12", "2026-08-01", "제작중",    "★"),
    ("PRJ008", "노을여행 일본 배급",         "배급",      "일본배급사U",   "차지현", "2026-04-28", "2026-10-15", "계약검토",  "★★"),
]

with (OUT / "projects_master.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow([
        "project_id", "title", "kind", "partner_org", "lead",
        "kickoff_date", "premiere_or_deliv", "status", "priority",
    ])
    w.writerows(projects)


# 6) contract_terms.csv  — 작품별 계약 조건 (다양한 컬럼이 다 달라서 표준화 어려운 지점 재현)
contracts = [
    # contract_id, project_id, rights_scope, settle_ratio, holdback, settle_cycle, approval_required, copyright_text, signed_date, status
    ("CT001", "PRJ001", "전 세계, OTT 포함",         "60:40", "3개월", "분기 정산",  "Y", "© ABC프로덕션 / 자사", "2026-01-22", "체결완료"),
    ("CT002", "PRJ002", "국내, 펀딩 한정",            "70:30", "없음", "1회 정산",   "N", "© 자사",               "2026-03-08", "체결완료"),
    ("CT003", "PRJ003", "글로벌, 극장 우선",          "55:45", "6개월", "반기 정산", "Y", "© 글로벌배급사X / 자사","2025-12-04", "체결완료"),
    ("CT004", "PRJ004", "전 세계, 스트리밍 우선",     "50:50", "3개월", "분기 정산",  "Y", "© 스튜디오Y",          "2026-02-18", "체결완료"),
    ("CT005", "PRJ005", "국내 + 동남아",              "8% 로열티", "없음", "월 정산", "Y", "© 자사",               "",          "조건검토"),
    ("CT006", "PRJ006", "음원 사용권",                 "12% 로열티", "없음", "분기 정산","Y","© 음반사W / 자사",    "",          "협상중"),
    ("CT007", "PRJ007", "영문 더빙판 권리",            "Work for hire", "없음", "1회 정산", "N", "© 자사",         "2026-03-22", "체결완료"),
    ("CT008", "PRJ008", "일본 극장 + 스트리밍",        "50:50", "9개월", "반기 정산",  "Y", "© 일본배급사U / 자사", "",          "검토중"),
]
with (OUT / "contract_terms.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow([
        "contract_id", "project_id",
        "rights_scope", "settle_ratio", "holdback",
        "settle_cycle", "approval_required", "copyright_text",
        "signed_date", "status",
    ])
    w.writerows(contracts)


# 7) meeting_actions.csv  — 위클리 미팅 액션 아이템 (지난 4주)
meetings = [
    # meeting_id, meeting_date, project_id, attendee_count, action, owner, due_date, severity, status, note
    ("MT001", "2026-04-22", "PRJ001", 6, "캐릭터 디자인 시안 3개 추가 작업", "디자인팀",       "2026-05-06", "중", "완료",  "1차 시안 5/6 컨펌"),
    ("MT002", "2026-04-22", "PRJ001", 6, "분기 정산 자료 준비",            "회계",          "2026-05-15", "중", "진행중","ABC 정산 데이터 대조 중"),
    ("MT003", "2026-04-23", "PRJ002", 4, "굿즈 가격 적정성 시장 조사",     "차지현",        "2026-04-30", "상", "완료",  "팬덤 반응 기반 22% 조정"),
    ("MT004", "2026-04-29", "PRJ003", 8, "개봉 마케팅 KPI 확정",          "마케팅",        "2026-05-08", "상", "지연",  "글로벌배급사 회신 대기"),
    ("MT005", "2026-04-29", "PRJ003", 8, "OST 콜라보 음반사 계약 검토",   "법무",          "2026-05-13", "상", "진행중","CT006 조건 협상"),
    ("MT006", "2026-04-30", "PRJ004", 5, "시즌2 5화 시나리오 확정",       "스토리팀",      "2026-05-20", "중", "진행중","2차 회의 5/14 예정"),
    ("MT007", "2026-05-06", "PRJ005", 4, "완구사Z 라이선스 조건 1차 회신","차지현",        "2026-05-13", "상", "완료",  "8% 로열티로 응답"),
    ("MT008", "2026-05-06", "PRJ002", 4, "텀블벅 페이지 카피 최종 검수",  "차지현",        "2026-05-16", "중", "진행중","마감 임박"),
    ("MT009", "2026-05-07", "PRJ006", 3, "음반사W 홀드백 조항 재협의",    "법무",          "2026-05-21", "상", "지연",  "음반사 측 외부 변호사 검토"),
    ("MT010", "2026-05-08", "PRJ003", 7, "노을여행 시사회 게스트 리스트", "마케팅",        "2026-05-18", "중", "진행중","외부 평론가 5명 컨펌"),
    ("MT011", "2026-05-08", "PRJ001", 6, "캐릭터 시안 컬러 가이드",       "디자인팀",      "2026-05-22", "하", "예정",  ""),
    ("MT012", "2026-05-13", "PRJ008", 5, "일본 배급사 카피라이트 문구",   "법무",          "2026-05-20", "상", "진행중","공동 표기 합의 필요"),
    ("MT013", "2026-05-13", "PRJ007", 3, "영문 더빙 1차 검수",            "현지화팀",      "2026-05-23", "중", "진행중","3 에피소드 완료"),
    ("MT014", "2026-05-14", "PRJ001", 6, "ABC프로덕션 분기 정산 보고 초안","회계",         "2026-05-22", "상", "예정",  "지연되면 다음 분기로 이월"),
    ("MT015", "2026-05-14", "PRJ002", 4, "굿즈 펀딩 D-30 SNS 캠페인 기획","마케팅",       "2026-05-21", "중", "예정",  ""),
    ("MT016", "2026-05-14", "PRJ003", 8, "글로벌배급사 마케팅 KPI 재요청","차지현",        "2026-05-16", "상", "지연",  "MT004 후속, 부사장님께 보고 필요"),
    ("MT017", "2026-05-15", "PRJ005", 4, "라이선스 카피라이트 표기 협의", "법무",          "2026-05-23", "중", "예정",  ""),
    ("MT018", "2026-05-15", "PRJ004", 5, "시즌2 5화 시나리오 2차 검토",   "스토리팀",      "2026-05-22", "중", "예정",  "MT006 후속"),
]

with (OUT / "meeting_actions.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow([
        "meeting_id", "meeting_date", "project_id", "attendee_count",
        "action", "owner", "due_date", "severity", "status", "note",
    ])
    w.writerows(meetings)


# Summary
print("Generated:")
for p in sorted(OUT.glob("*.csv")):
    size = p.stat().st_size
    with p.open(encoding="utf-8-sig") as f:
        n = sum(1 for _ in f) - 1
    print(f"  {p.name}  ({n} rows, {size:,} bytes)")
