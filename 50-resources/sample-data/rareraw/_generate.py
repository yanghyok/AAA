"""
레어로우 합동 AX Bootcamp 데모용 더미데이터 생성기

생성 파일:
- products_master.csv     상품 마스터 (시스템000 / 랙 / 워크 시리즈)
- online_sales.csv        온라인 매출 (자사몰 + 입점몰 다채널, 최근 8주)
- offline_sales.csv       오프라인 매출 (청담 쇼룸 + 강남 쇼룸)
- ad_performance.csv      퍼포먼스 마케팅 성과 (채널별 일별)

데이터 기준일: 2026-05-17 (캠프 직전)
범위: 2026-03-23 ~ 2026-05-17 (8주)
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(20260518)
OUT = Path(__file__).parent
END_DATE = date(2026, 5, 17)
DAYS = 56  # 8 weeks
START_DATE = END_DATE - timedelta(days=DAYS - 1)


# -------------------------------------------------------------
# 1. 상품 마스터 (rareraw.com 실제 라인업 기반)
# -------------------------------------------------------------
# 정가 / 자사몰가(15% off 진행중) / 입점몰가는 채널별 가공
products = [
    # SKU, 상품명, 시리즈, 카테고리, 정가, 자사몰가, 무게(kg), 발주처
    ("RR-RAK-101", "레어로우 랙 소파 테이블", "랙", "테이블", 189000, 160650, 12, "심플라인"),
    ("RR-RAK-102", "레어로우 랙 사이드 테이블", "랙", "테이블", 157000, 133450, 8, "심플라인"),
    ("RR-RAK-103", "레어로우 랙 유틸리티 랙", "랙", "수납", 475000, 403750, 24, "심플라인"),
    ("RR-RAK-104", "레어로우 랙 행거 랙", "랙", "수납", 383000, 325550, 18, "심플라인"),
    ("RR-RAK-105", "레어로우 랙 미니 랙", "랙", "수납", 219000, 186150, 9, "심플라인"),
    ("RR-RAK-106", "레어로우 랙 와이드 셸프", "랙", "수납", 565000, 480250, 32, "심플라인"),
    ("RR-SYS-201", "시스템000 1단 모듈", "시스템000", "수납", 298000, 253300, 14, "심플라인"),
    ("RR-SYS-202", "시스템000 2단 모듈", "시스템000", "수납", 498000, 423300, 27, "심플라인"),
    ("RR-SYS-203", "시스템000 3단 모듈", "시스템000", "수납", 698000, 593300, 41, "심플라인"),
    ("RR-SYS-204", "시스템000 코너 모듈", "시스템000", "수납", 348000, 295800, 17, "심플라인"),
    ("RR-SYS-205", "시스템000 도어 패널", "시스템000", "부속", 89000, 75650, 4, "심플라인"),
    ("RR-WRK-301", "레어로우 워크 데스크 1200", "워크", "데스크", 458000, 389300, 28, "심플라인"),
    ("RR-WRK-302", "레어로우 워크 데스크 1500", "워크", "데스크", 528000, 448800, 34, "심플라인"),
    ("RR-WRK-303", "레어로우 워크 체어", "워크", "체어", 348000, 295800, 12, "외주처A"),
    ("RR-WRK-304", "레어로우 워크 모니터암", "워크", "액세서리", 168000, 142800, 3, "외주처B"),
    ("RR-WRK-305", "레어로우 워크 케이블 트레이", "워크", "액세서리", 78000, 66300, 2, "외주처B"),
    ("RR-HOM-401", "홈 시리즈 TV 보드", "홈", "리빙", 698000, 593300, 38, "심플라인"),
    ("RR-HOM-402", "홈 시리즈 화분 스탠드", "홈", "리빙", 128000, 108800, 5, "외주처A"),
    ("RR-HOM-403", "홈 시리즈 행거", "홈", "리빙", 218000, 185300, 8, "심플라인"),
    ("RR-LIF-501", "10 COLORS 미니 사이드", "라이프스타일", "테이블", 138000, 117300, 6, "심플라인"),
    ("RR-LIF-502", "10 COLORS 스툴", "라이프스타일", "체어", 168000, 142800, 5, "심플라인"),
    ("RR-LIF-503", "10 COLORS 매거진 랙", "라이프스타일", "수납", 98000, 83300, 3, "외주처A"),
]

# 채널별 판매가 (자사몰 = own, 입점몰별 가격 차이 반영)
# 채널: 자사몰, 29CM, 오늘의집, 네이버스마트스토어, 쿠팡
def channel_price(own_price):
    return {
        "자사몰": own_price,
        "29CM": int(own_price * 1.05),  # 29CM 5% 비쌈
        "오늘의집": int(own_price * 1.02),
        "네이버": int(own_price * 0.97),
        "쿠팡": int(own_price * 0.95),  # 쿠팡 최저
    }

# 채널별 수수료율
CHANNEL_FEE = {
    "자사몰": 0.035,    # PG 수수료
    "29CM": 0.27,
    "오늘의집": 0.18,
    "네이버": 0.07,
    "쿠팡": 0.108,
}

with open(OUT / "products_master.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow([
        "sku", "product_name", "series", "category",
        "list_price", "own_price",
        "price_29cm", "price_ohouse", "price_naver", "price_coupang",
        "weight_kg", "supplier",
    ])
    for sku, name, series, cat, list_p, own_p, weight, supplier in products:
        cp = channel_price(own_p)
        w.writerow([
            sku, name, series, cat,
            list_p, own_p,
            cp["29CM"], cp["오늘의집"], cp["네이버"], cp["쿠팡"],
            weight, supplier,
        ])

print(f"products_master.csv: {len(products)} rows")


# -------------------------------------------------------------
# 2. 온라인 매출 (다채널, 8주)
# -------------------------------------------------------------
# 채널별 가중치 (자사몰 비중 최대)
CHANNEL_WEIGHT = {
    "자사몰": 0.40,
    "29CM": 0.15,
    "오늘의집": 0.20,
    "네이버": 0.15,
    "쿠팡": 0.10,
}

# 시리즈별 인기도 (랙 > 시스템000 > 워크 > 홈 > 라이프스타일)
SERIES_WEIGHT = {
    "랙": 0.42,
    "시스템000": 0.22,
    "워크": 0.18,
    "홈": 0.10,
    "라이프스타일": 0.08,
}

# 주차별 트렌드 (8주, 봄 이사철 + 5월 가정의달 부스트)
# week 0 = 가장 오래된, week 7 = 최근
WEEK_BOOST = [0.85, 0.90, 0.95, 1.00, 1.05, 1.15, 1.25, 1.30]

# 요일별 가중 (주말 약함, 평일 강함 — 가구 특성)
DOW_WEIGHT = [1.0, 1.05, 1.1, 1.15, 1.2, 0.85, 0.75]  # 월~일

# 5/1~5/10 가정의 달 프로모션 (15% 추가 할인, 트래픽 증가)
PROMO_START = date(2026, 5, 1)
PROMO_END = date(2026, 5, 10)

# 4/20 ~ 4/26: 자사몰만 신규 컬러 런칭 (자사몰 매출 스파이크)
LAUNCH_START = date(2026, 4, 20)
LAUNCH_END = date(2026, 4, 26)

# 5/5~5/8: 오늘의집 정기 큐레이션 노출 (오늘의집 채널 부스트)
OHOUSE_BOOST_START = date(2026, 5, 5)
OHOUSE_BOOST_END = date(2026, 5, 8)


def pick_product():
    series = random.choices(
        list(SERIES_WEIGHT.keys()),
        weights=list(SERIES_WEIGHT.values()),
    )[0]
    candidates = [p for p in products if p[2] == series]
    return random.choice(candidates)


def order_no(channel, d, seq):
    code_map = {
        "자사몰": "OWN", "29CM": "29C", "오늘의집": "OHS",
        "네이버": "NAV", "쿠팡": "CPG",
    }
    return f"{code_map[channel]}-{d.strftime('%y%m%d')}-{seq:04d}"


online_rows = []
for day_idx in range(DAYS):
    d = START_DATE + timedelta(days=day_idx)
    week = day_idx // 7
    boost = WEEK_BOOST[week] * DOW_WEIGHT[d.weekday()]

    # 일별 베이스 주문 건수 (35 ~ 55 base)
    base_orders = int(random.uniform(35, 55) * boost)

    # 프로모션 기간 부스트
    if PROMO_START <= d <= PROMO_END:
        base_orders = int(base_orders * 1.4)
    # 자사몰 컬러 런칭
    own_extra = 0
    if LAUNCH_START <= d <= LAUNCH_END:
        own_extra = int(random.uniform(8, 15))
    # 오늘의집 큐레이션
    ohouse_extra = 0
    if OHOUSE_BOOST_START <= d <= OHOUSE_BOOST_END:
        ohouse_extra = int(random.uniform(6, 12))

    seq = 1
    for _ in range(base_orders):
        channel = random.choices(
            list(CHANNEL_WEIGHT.keys()),
            weights=list(CHANNEL_WEIGHT.values()),
        )[0]
        sku_row = pick_product()
        sku, name, series, cat, list_p, own_p, weight, supplier = sku_row
        cp = channel_price(own_p)
        unit_price = cp[channel] if channel != "자사몰" else own_p
        # 프로모 기간 자사몰만 추가 5% 할인
        if channel == "자사몰" and PROMO_START <= d <= PROMO_END:
            unit_price = int(unit_price * 0.95)
        qty = random.choices([1, 1, 1, 2, 2, 3], weights=[5, 5, 5, 2, 2, 1])[0]
        revenue = unit_price * qty
        fee = int(revenue * CHANNEL_FEE[channel])
        online_rows.append({
            "order_date": d.isoformat(),
            "order_no": order_no(channel, d, seq),
            "channel": channel,
            "sku": sku,
            "product_name": name,
            "series": series,
            "category": cat,
            "qty": qty,
            "unit_price": unit_price,
            "revenue": revenue,
            "channel_fee": fee,
        })
        seq += 1

    # 자사몰 런칭 보너스 주문
    for _ in range(own_extra):
        sku_row = pick_product()
        # 런칭 컬러는 라이프스타일 시리즈 위주
        if random.random() < 0.5:
            life_products = [p for p in products if p[2] == "라이프스타일"]
            sku_row = random.choice(life_products)
        sku, name, series, cat, list_p, own_p, weight, supplier = sku_row
        unit_price = own_p
        qty = random.choices([1, 1, 2], weights=[6, 2, 2])[0]
        revenue = unit_price * qty
        online_rows.append({
            "order_date": d.isoformat(),
            "order_no": order_no("자사몰", d, seq),
            "channel": "자사몰",
            "sku": sku,
            "product_name": name,
            "series": series,
            "category": cat,
            "qty": qty,
            "unit_price": unit_price,
            "revenue": revenue,
            "channel_fee": int(revenue * CHANNEL_FEE["자사몰"]),
        })
        seq += 1

    # 오늘의집 큐레이션 부스트
    for _ in range(ohouse_extra):
        sku_row = pick_product()
        sku, name, series, cat, list_p, own_p, weight, supplier = sku_row
        unit_price = channel_price(own_p)["오늘의집"]
        qty = random.choices([1, 1, 2], weights=[7, 2, 1])[0]
        revenue = unit_price * qty
        online_rows.append({
            "order_date": d.isoformat(),
            "order_no": order_no("오늘의집", d, seq),
            "channel": "오늘의집",
            "sku": sku,
            "product_name": name,
            "series": series,
            "category": cat,
            "qty": qty,
            "unit_price": unit_price,
            "revenue": revenue,
            "channel_fee": int(revenue * CHANNEL_FEE["오늘의집"]),
        })
        seq += 1

with open(OUT / "online_sales.csv", "w", encoding="utf-8-sig", newline="") as f:
    fieldnames = [
        "order_date", "order_no", "channel", "sku", "product_name",
        "series", "category", "qty", "unit_price", "revenue", "channel_fee",
    ]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(online_rows)

print(f"online_sales.csv: {len(online_rows)} rows")


# -------------------------------------------------------------
# 3. 오프라인 매출 (청담 쇼룸 + 강남 쇼룸, 일별 합계)
# -------------------------------------------------------------
# 오프라인은 채널별 분산이 적고, 주말 부스트 (반대)
SHOWROOMS = ["청담 쇼룸", "강남 쇼룸"]
OFFLINE_DOW_WEIGHT = [0.5, 0.5, 0.6, 0.7, 0.9, 1.6, 1.5]  # 주말 강세

offline_rows = []
for day_idx in range(DAYS):
    d = START_DATE + timedelta(days=day_idx)
    week = day_idx // 7
    boost = WEEK_BOOST[week] * OFFLINE_DOW_WEIGHT[d.weekday()]
    # 가정의달 + 봄 이사철 부스트
    if PROMO_START <= d <= PROMO_END:
        boost *= 1.3
    for sr in SHOWROOMS:
        sr_factor = 1.0 if sr == "청담 쇼룸" else 0.6  # 청담이 매출 큼
        # 일 평균 방문 6~14, 구매 전환 2~5건
        visitors = max(0, int(random.uniform(6, 14) * boost * sr_factor))
        orders = max(0, int(visitors * random.uniform(0.25, 0.45)))
        # 오프라인 객단가는 온라인보다 큼 (시스템000 모듈 패키지 판매)
        avg_ticket = random.uniform(380000, 820000)
        revenue = int(orders * avg_ticket)
        offline_rows.append({
            "date": d.isoformat(),
            "showroom": sr,
            "visitors": visitors,
            "orders": orders,
            "revenue": revenue,
            "avg_ticket": int(avg_ticket) if orders > 0 else 0,
        })

with open(OUT / "offline_sales.csv", "w", encoding="utf-8-sig", newline="") as f:
    fieldnames = ["date", "showroom", "visitors", "orders", "revenue", "avg_ticket"]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(offline_rows)

print(f"offline_sales.csv: {len(offline_rows)} rows")


# -------------------------------------------------------------
# 4. 광고 성과 (퍼포먼스 마케팅, 채널별 일별)
# -------------------------------------------------------------
# 광고 캠페인: Meta/Google/네이버/카카오
AD_CAMPAIGNS = [
    # (캠페인명, 매체, 일일 평균 광고비, 평균 ROAS)
    ("랙_브랜드인지_Meta", "Meta", 180000, 2.8),
    ("랙_DPA리타겟_Meta", "Meta", 220000, 4.2),
    ("시스템000_관심사_Meta", "Meta", 150000, 3.1),
    ("워크_검색_Google", "Google", 130000, 5.6),
    ("브랜드명_검색_Google", "Google", 80000, 9.2),
    ("쇼핑_PMax_Google", "Google", 200000, 3.7),
    ("브랜드검색_네이버", "네이버", 90000, 7.4),
    ("쇼핑검색_네이버", "네이버", 160000, 4.1),
    ("모먼트_카카오", "카카오", 70000, 2.2),
]

ad_rows = []
for day_idx in range(DAYS):
    d = START_DATE + timedelta(days=day_idx)
    for camp_name, media, base_spend, base_roas in AD_CAMPAIGNS:
        spend = int(base_spend * random.uniform(0.85, 1.15))
        # 프로모션 기간 광고비 증가 + ROAS 상승
        if PROMO_START <= d <= PROMO_END:
            spend = int(spend * 1.5)
            roas = base_roas * random.uniform(1.1, 1.4)
        elif LAUNCH_START <= d <= LAUNCH_END and "Meta" in media:
            spend = int(spend * 1.3)
            roas = base_roas * random.uniform(0.9, 1.2)
        else:
            roas = base_roas * random.uniform(0.7, 1.3)
        revenue = int(spend * roas)
        impressions = int(spend / random.uniform(8, 14))
        clicks = int(impressions * random.uniform(0.008, 0.025))
        conversions = int(clicks * random.uniform(0.015, 0.045))
        ad_rows.append({
            "date": d.isoformat(),
            "campaign": camp_name,
            "media": media,
            "spend": spend,
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "attributed_revenue": revenue,
            "roas": round(roas, 2),
        })

with open(OUT / "ad_performance.csv", "w", encoding="utf-8-sig", newline="") as f:
    fieldnames = [
        "date", "campaign", "media", "spend",
        "impressions", "clicks", "conversions",
        "attributed_revenue", "roas",
    ]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(ad_rows)

print(f"ad_performance.csv: {len(ad_rows)} rows")


# -------------------------------------------------------------
# 5. 일일 매출 보고 메시지 (참고용 — 박소연이 사내 메신저에 보내는 형식)
# 사용하지는 않지만 본인 일과 매핑되는지 시연 후 참고 자료로 둠
# -------------------------------------------------------------
print()
print("=== Generated ===")
print(f"START: {START_DATE}  END: {END_DATE}  ({DAYS} days)")
print(f"Total online orders: {len(online_rows)}")
print(f"Total offline rows: {len(offline_rows)}")
print(f"Total ad rows: {len(ad_rows)}")
