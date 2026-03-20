# GigGuard X — Master Build Prompt for AI Agent
# ================================================
# Copy this ENTIRE file as your prompt to the AI agent.
# Do NOT skip any section. Every section is load-bearing.

---

## IDENTITY & MISSION

You are a senior full-stack engineer building **GigGuard X** — an AI-powered parametric income insurance platform for India's gig economy (Swiggy/Zomato delivery partners). This is a hackathon project for **Guidewire DEVTrails 2026**.

Your job is to build the complete project **phase by phase**, implementing each phase fully before moving to the next. Every phase must be **working, tested, and runnable** before proceeding.

Read this entire prompt before writing a single line of code.

---

## PROJECT OVERVIEW

GigGuard X automatically detects environmental disruptions (heavy rain, heat, floods, AQI spikes, curfews) and pays delivery workers via UPI **without them filing a claim**. The system uses:

- **Parametric insurance**: payout triggers on objective thresholds (rain >35mm/hr), not manual claims
- **Proof of Work**: verifies workers actually tried to work (unique differentiator)
- **Trust Score**: composite of Fraud + PoW + History scores
- **GenAI + RAG**: Claude/Gemini-powered chatbot grounded in policy documents
- **Weekly pricing**: ₹20–₹149/week aligned to Swiggy/Zomato payout cycles

---

## TECH STACK (MANDATORY — do not substitute)

### Frontend
```
React 18 + Vite
TypeScript
Tailwind CSS v3
React Router v6
Zustand (state management)
React Query (TanStack Query v5)
Recharts (charts/analytics)
React Hook Form + Zod (forms/validation)
Axios (HTTP client)
React Hot Toast (notifications)
Lucide React (icons)
```

### Backend
```
Python 3.11+
FastAPI (REST API framework)
SQLAlchemy 2.0 (ORM)
Alembic (database migrations)
PostgreSQL 15 (primary database)
Redis 7 (caching + real-time state)
Celery 5 (async task queue)
Pydantic v2 (data validation)
python-jose (JWT auth)
passlib + bcrypt (password hashing)
httpx (async HTTP client for external APIs)
pytest (testing)
```

### AI / ML
```
# LLM (FREE - no paid API key needed)
google-generativeai   # Gemini 2.0 Flash (free tier via Google AI Studio)
                      # Get free key at: https://aistudio.google.com/app/apikey

# Embeddings (FREE)
sentence-transformers # HuggingFace all-MiniLM-L6-v2 (runs locally, no API key)

# Vector Store (FREE, local)
faiss-cpu             # Facebook AI Similarity Search

# ML Models (runs locally)
scikit-learn          # Isolation Forest (fraud detection)
xgboost               # Risk scoring + income prediction
numpy
pandas
joblib                # model serialization
```

### Infrastructure
```
Docker + Docker Compose
nginx (reverse proxy)
GitHub Actions (CI/CD)
```

### External APIs (FREE tiers)
```
OpenWeatherMap API    # Free: 1000 calls/day — weather triggers
                      # https://openweathermap.org/api (free signup)

AQI India (WAQI)     # Free: 1000 calls/day — air quality
                      # https://aqicn.org/data-platform/token/

Nominatim (OSM)      # Free, no key needed — geocoding/reverse geocoding
                      # https://nominatim.openstreetmap.org

Razorpay Test Mode   # Free sandbox — UPI payout simulation
                      # https://razorpay.com (create test account)
```

---

## PROJECT STRUCTURE (create exactly this)

```
gigguard-x/
├── frontend/
│   ├── src/
│   │   ├── api/              # API client functions
│   │   ├── components/       # Reusable UI components
│   │   │   ├── ui/           # Base components (Button, Card, Badge...)
│   │   │   ├── charts/       # WorkabilityRing, EarningsChart...
│   │   │   └── layout/       # Sidebar, Topbar, Layout
│   │   ├── pages/            # Page components (one per route)
│   │   ├── stores/           # Zustand state stores
│   │   ├── hooks/            # Custom React hooks
│   │   ├── types/            # TypeScript type definitions
│   │   └── utils/            # Helper functions
│   ├── public/
│   ├── index.html
│   ├── vite.config.ts
│   ├── tailwind.config.ts
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── auth.py         # Auth endpoints
│   │   │   │   ├── workers.py      # Worker profile endpoints
│   │   │   │   ├── policies.py     # Policy CRUD
│   │   │   │   ├── claims.py       # Claims management
│   │   │   │   ├── triggers.py     # Disruption trigger endpoints
│   │   │   │   ├── payouts.py      # Payout processing
│   │   │   │   ├── admin.py        # Admin-only endpoints
│   │   │   │   └── chat.py         # RAG chatbot endpoint
│   │   ├── core/
│   │   │   ├── config.py           # Settings (pydantic-settings)
│   │   │   ├── security.py         # JWT + password utils
│   │   │   └── database.py         # SQLAlchemy engine + session
│   │   ├── models/                 # SQLAlchemy ORM models
│   │   │   ├── user.py
│   │   │   ├── worker.py
│   │   │   ├── policy.py
│   │   │   ├── claim.py
│   │   │   ├── payout.py
│   │   │   └── disruption_event.py
│   │   ├── schemas/                # Pydantic request/response schemas
│   │   ├── services/               # Business logic layer
│   │   │   ├── workability.py      # WS Engine
│   │   │   ├── trust_score.py      # Trust Score composite
│   │   │   ├── proof_of_work.py    # PoW signal collection
│   │   │   ├── pricing.py          # Dynamic premium calculator
│   │   │   ├── risk_score.py       # AI risk profiling
│   │   │   ├── income_prediction.py# XGBoost income model
│   │   │   ├── fraud_detection.py  # Isolation Forest
│   │   │   └── payout.py           # Razorpay integration
│   │   ├── ml/                     # ML model training + inference
│   │   │   ├── models/             # Saved .pkl model files
│   │   │   ├── train_risk.py
│   │   │   ├── train_income.py
│   │   │   └── train_fraud.py
│   │   ├── rag/                    # GenAI + RAG pipeline
│   │   │   ├── knowledge_base/     # Policy docs as .txt/.md files
│   │   │   ├── embeddings.py       # HuggingFace embedder + FAISS
│   │   │   ├── retriever.py        # Semantic search
│   │   │   └── chat.py             # Gemini generation + context injection
│   │   ├── integrations/           # External API clients
│   │   │   ├── weather.py          # OpenWeatherMap client
│   │   │   ├── aqi.py              # WAQI client
│   │   │   └── geocoding.py        # Nominatim client
│   │   ├── tasks/                  # Celery async tasks
│   │   │   ├── monitor.py          # 15-min monitoring loop
│   │   │   ├── claims.py           # Auto-claim processing
│   │   │   └── payouts.py          # Payout execution
│   │   └── main.py                 # FastAPI app entry point
│   ├── alembic/                    # Database migrations
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── docker-compose.dev.yml
├── nginx/
│   └── nginx.conf
├── .env.example
├── Makefile
└── README.md
```

---

## DATABASE SCHEMA (implement exactly)

### Table: users
```sql
id            UUID PRIMARY KEY DEFAULT gen_random_uuid()
email         VARCHAR(255) UNIQUE NOT NULL
phone         VARCHAR(20) UNIQUE NOT NULL
hashed_password VARCHAR(255) NOT NULL
role          ENUM('worker', 'admin', 'insurer') DEFAULT 'worker'
is_active     BOOLEAN DEFAULT true
is_verified   BOOLEAN DEFAULT false
created_at    TIMESTAMP DEFAULT NOW()
updated_at    TIMESTAMP DEFAULT NOW()
```

### Table: worker_profiles
```sql
id              UUID PRIMARY KEY DEFAULT gen_random_uuid()
user_id         UUID REFERENCES users(id) UNIQUE
full_name       VARCHAR(255) NOT NULL
aadhaar_last4   VARCHAR(4)
platform        ENUM('swiggy','zomato','zepto','blinkit','amazon','flipkart')
delivery_category ENUM('food','grocery','ecommerce')
partner_id      VARCHAR(100)
city            VARCHAR(100)
zone            VARCHAR(100)
latitude        DECIMAL(10,8)
longitude       DECIMAL(11,8)
vehicle_type    ENUM('bike','ev_scooter','bicycle')
daily_hours     INTEGER   -- 4, 8, or 12
avg_weekly_earnings DECIMAL(10,2)
months_active   INTEGER
risk_score      INTEGER DEFAULT 50
trust_score     INTEGER DEFAULT 70
loyalty_xp      INTEGER DEFAULT 0
loyalty_level   INTEGER DEFAULT 1
preferred_language ENUM('en','hi','te') DEFAULT 'en'
created_at      TIMESTAMP DEFAULT NOW()
updated_at      TIMESTAMP DEFAULT NOW()
```

### Table: policies
```sql
id              UUID PRIMARY KEY DEFAULT gen_random_uuid()
policy_number   VARCHAR(50) UNIQUE NOT NULL  -- GS-2026-{CITY}-{NUM}
worker_id       UUID REFERENCES worker_profiles(id)
status          ENUM('active','expired','cancelled') DEFAULT 'active'
plan_tier       ENUM('basic','standard','full') NOT NULL
weekly_premium  DECIMAL(8,2) NOT NULL
coverage_amount DECIMAL(10,2) NOT NULL
week_start      DATE NOT NULL
week_end        DATE NOT NULL
risk_score_at_creation INTEGER
auto_renew      BOOLEAN DEFAULT true
created_at      TIMESTAMP DEFAULT NOW()
```

### Table: disruption_events
```sql
id              UUID PRIMARY KEY DEFAULT gen_random_uuid()
event_type      ENUM('heavy_rain','extreme_heat','flood','severe_aqi','curfew','app_outage')
zone            VARCHAR(100) NOT NULL
city            VARCHAR(100) NOT NULL
severity        ENUM('watch','warning','critical')
value           DECIMAL(10,2)   -- actual value (mm, celsius, AQI number)
threshold       DECIMAL(10,2)   -- threshold that was breached
data_source     VARCHAR(100)    -- which API detected this
started_at      TIMESTAMP NOT NULL
ended_at        TIMESTAMP
is_active       BOOLEAN DEFAULT true
workability_score INTEGER        -- WS at time of event
created_at      TIMESTAMP DEFAULT NOW()
```

### Table: claims
```sql
id              UUID PRIMARY KEY DEFAULT gen_random_uuid()
claim_number    VARCHAR(50) UNIQUE NOT NULL  -- CLM-{YEAR}-{NUM}
policy_id       UUID REFERENCES policies(id)
worker_id       UUID REFERENCES worker_profiles(id)
disruption_id   UUID REFERENCES disruption_events(id)
status          ENUM('initiated','fraud_check','pow_check','approved','rejected','paid','flagged','appealing')
trigger_type    VARCHAR(50)
trigger_value   DECIMAL(10,2)
duration_hours  DECIMAL(5,2)
estimated_loss  DECIMAL(10,2)
payout_amount   DECIMAL(10,2)
payout_percentage INTEGER        -- 30, 40, 50, 60, or 100
fraud_score     INTEGER DEFAULT 0
pow_score       INTEGER DEFAULT 0
history_score   INTEGER DEFAULT 0
trust_score     INTEGER DEFAULT 0
fraud_flags     JSONB DEFAULT '[]'
pow_signals     JSONB DEFAULT '{}'  -- stores the PoW evidence
rejection_reason TEXT
initiated_at    TIMESTAMP DEFAULT NOW()
approved_at     TIMESTAMP
paid_at         TIMESTAMP
created_at      TIMESTAMP DEFAULT NOW()
```

### Table: payouts
```sql
id              UUID PRIMARY KEY DEFAULT gen_random_uuid()
claim_id        UUID REFERENCES claims(id)
worker_id       UUID REFERENCES worker_profiles(id)
amount          DECIMAL(10,2) NOT NULL
upi_id          VARCHAR(100)
razorpay_payout_id VARCHAR(100)
razorpay_fund_account_id VARCHAR(100)
status          ENUM('pending','processing','success','failed')
failure_reason  TEXT
processed_at    TIMESTAMP
created_at      TIMESTAMP DEFAULT NOW()
```

### Table: income_buffer_wallet
```sql
id              UUID PRIMARY KEY DEFAULT gen_random_uuid()
worker_id       UUID REFERENCES worker_profiles(id) UNIQUE
balance         DECIMAL(10,2) DEFAULT 0
total_deposited DECIMAL(10,2) DEFAULT 0
total_withdrawn DECIMAL(10,2) DEFAULT 0
created_at      TIMESTAMP DEFAULT NOW()
updated_at      TIMESTAMP DEFAULT NOW()
```

### Table: wallet_transactions
```sql
id              UUID PRIMARY KEY DEFAULT gen_random_uuid()
wallet_id       UUID REFERENCES income_buffer_wallet(id)
type            ENUM('deposit','withdrawal','cashback')
amount          DECIMAL(10,2) NOT NULL
description     TEXT
related_claim_id UUID REFERENCES claims(id)
created_at      TIMESTAMP DEFAULT NOW()
```

---

## ROLE-BASED AUTH SPECIFICATION

### Roles
- **worker**: Standard gig worker — can view own dashboard, policy, claims, chat with AI
- **admin**: Platform admin — full access to all data, can approve/reject claims, view fraud alerts
- **insurer**: Guidewire insurer view — analytics only, cannot modify data

### JWT Token Structure
```json
{
  "sub": "user_uuid",
  "role": "worker",
  "worker_id": "worker_profile_uuid",
  "exp": 1234567890,
  "iat": 1234567890,
  "jti": "unique_token_id"
}
```

### Route Protection Rules
```
PUBLIC (no auth):
  POST /api/v1/auth/register
  POST /api/v1/auth/login
  POST /api/v1/auth/refresh
  GET  /api/v1/health

WORKER ONLY:
  GET  /api/v1/workers/me
  PUT  /api/v1/workers/me
  GET  /api/v1/policies/my
  POST /api/v1/policies/create
  GET  /api/v1/claims/my
  GET  /api/v1/claims/{id}
  POST /api/v1/chat/message
  GET  /api/v1/wallet/my
  GET  /api/v1/triggers/current
  GET  /api/v1/workers/me/insights

ADMIN + INSURER:
  GET  /api/v1/admin/dashboard
  GET  /api/v1/admin/workers
  GET  /api/v1/admin/claims
  GET  /api/v1/admin/fraud-alerts
  GET  /api/v1/admin/analytics

ADMIN ONLY:
  PUT  /api/v1/admin/claims/{id}/approve
  PUT  /api/v1/admin/claims/{id}/reject
  POST /api/v1/admin/trigger-disruption   (test/demo endpoint)
  GET  /api/v1/admin/users
```

---

## API SPECIFICATION (implement all endpoints)

### Auth Endpoints

#### POST /api/v1/auth/register
```json
// Request
{
  "email": "ravi@example.com",
  "phone": "+919876543210",
  "password": "SecurePass123!",
  "full_name": "Ravi Kumar",
  "role": "worker"
}
// Response 201
{
  "user_id": "uuid",
  "email": "ravi@example.com",
  "role": "worker",
  "access_token": "jwt_token",
  "refresh_token": "jwt_refresh",
  "token_type": "bearer"
}
```

#### POST /api/v1/auth/login
```json
// Request
{ "email": "ravi@example.com", "password": "SecurePass123!" }
// Response 200
{
  "access_token": "jwt",
  "refresh_token": "jwt",
  "token_type": "bearer",
  "user": { "id": "uuid", "email": "...", "role": "worker" },
  "worker_profile": { "id": "uuid", "full_name": "...", ... } | null
}
```

### Worker Endpoints

#### POST /api/v1/workers/onboard
```json
// Request (multipart or JSON, auth required)
{
  "platform": "swiggy",
  "delivery_category": "food",
  "partner_id": "SW-HYD-284921",
  "city": "Hyderabad",
  "zone": "Central",
  "latitude": 17.3850,
  "longitude": 78.4867,
  "vehicle_type": "bike",
  "daily_hours": 8,
  "avg_weekly_earnings": 3500,
  "months_active": 14,
  "aadhaar_last4": "4821"
}
// Response 201
{
  "worker_profile": { ...all fields... },
  "risk_score": 62,
  "risk_category": "medium_high",
  "recommended_plan": "standard",
  "weekly_premium": 89,
  "coverage_amount": 1250
}
```

#### GET /api/v1/workers/me/insights
```json
// Response — AI-generated personalized insights
{
  "workability_score": 70,
  "score_breakdown": {
    "weather": 65, "aqi": 72, "traffic": 80, "demand": 68
  },
  "income_forecast": {
    "today": { "low": 480, "high": 560, "disruption_risk": 0.68 },
    "week": { "low": 3200, "high": 3500 }
  },
  "alerts": [
    { "type": "rain", "message": "Heavy rain forecast tomorrow 2pm–6pm", "probability": 0.68 }
  ],
  "recommendations": [
    { "icon": "clock", "title": "Best working window", "text": "11am–2pm, 6pm–9pm" },
    { "icon": "map", "title": "Safer zone nearby", "text": "Secunderabad — 40% lower flood risk" }
  ],
  "best_working_hours": ["11:00", "14:00", "18:00", "21:00"]
}
```

### Policy Endpoints

#### POST /api/v1/policies/create
```json
// Request
{ "plan_tier": "standard", "auto_renew": true }
// Response 201
{
  "policy_number": "GS-2026-HYD-04821",
  "weekly_premium": 89,
  "coverage_amount": 1250,
  "week_start": "2026-03-17",
  "week_end": "2026-03-23",
  "premium_breakdown": {
    "base": 60, "zone_loading": 18, "hours_factor": 8,
    "seasonal": 3, "ai_discount": 0, "total": 89
  },
  "triggers_active": ["heavy_rain","extreme_heat","flood","severe_aqi","curfew","app_outage"],
  "wallet_contribution": 8.90
}
```

### Trigger Endpoints

#### GET /api/v1/triggers/current
```json
// Response — live environmental data
{
  "workability_score": 70,
  "timestamp": "2026-03-20T14:15:00Z",
  "triggers": [
    {
      "type": "heavy_rain",
      "current_value": 12.5,
      "threshold": 35,
      "unit": "mm/hr",
      "status": "monitoring",
      "data_source": "openweathermap"
    }
  ],
  "active_disruptions": [],
  "environment": {
    "temperature": 28,
    "rainfall_mm_hr": 12.5,
    "aqi": 156,
    "wind_kmh": 18,
    "visibility_km": 4.2
  }
}
```

#### POST /api/v1/admin/trigger-disruption (Admin only — for demo)
```json
// Request
{
  "event_type": "heavy_rain",
  "city": "Hyderabad",
  "zone": "Central",
  "value": 38.0,
  "duration_hours": 3.5
}
// Response — triggers auto-claim for all active policies in zone
{
  "disruption_id": "uuid",
  "claims_initiated": 147,
  "workers_affected": 147
}
```

### Claims Endpoints

#### GET /api/v1/claims/my
```json
// Response
{
  "claims": [
    {
      "claim_number": "CLM-2026-0093",
      "status": "fraud_check",
      "trigger_type": "heavy_rain",
      "trigger_value": 38.0,
      "duration_hours": 3.5,
      "payout_amount": 525,
      "trust_score": 88,
      "fraud_score": 12,
      "pow_score": 91,
      "initiated_at": "2026-03-18T14:00:00Z",
      "explanation": "Heavy rainfall 38mm/hr exceeded 35mm threshold..."
    }
  ],
  "total": 5,
  "total_paid": 2775
}
```

### Chat Endpoint

#### POST /api/v1/chat/message
```json
// Request
{
  "message": "Why was my payout only Rs 525?",
  "conversation_id": "optional_uuid_for_history"
}
// Response (streaming SSE supported)
{
  "response": "Your Rs 525 payout = 60% of Rs 875 estimated lost income...",
  "sources": ["Policy T&C §3.1", "Claim Calculation §5.4"],
  "conversation_id": "uuid",
  "suggested_questions": [
    "How is my premium calculated?",
    "When will I get my next payout?"
  ]
}
```

### Wallet Endpoints

#### GET /api/v1/wallet/my
```json
{
  "balance": 340,
  "total_deposited": 468,
  "total_withdrawn": 128,
  "projected_cashback": 204,
  "transactions": [
    { "type": "deposit", "amount": 8.90, "description": "Weekly premium 10%", "date": "..." }
  ]
}
```

### Admin Dashboard

#### GET /api/v1/admin/dashboard
```json
{
  "metrics": {
    "total_active_policies": 12847,
    "weekly_premiums_collected": 1143383,
    "total_payouts_this_week": 840000,
    "loss_ratio": 0.736,
    "fraud_flags_this_week": 3,
    "avg_trust_score": 82.4
  },
  "zone_distribution": [
    { "city": "Hyderabad", "policies": 3850 }
  ],
  "fraud_alerts": [
    {
      "worker_id": "...",
      "fraud_score": 82,
      "reason": "GPS spoofing detected",
      "claim_id": "...",
      "action_required": true
    }
  ],
  "reserve_forecast": {
    "predicted_payouts_next_7_days": 840000,
    "recommended_reserve": 1200000
  }
}
```

---

## AI / ML IMPLEMENTATION SPECIFICATION

### 1. Risk Score Model (XGBoost)

Train on synthetic data. Generate 10,000 synthetic worker records.

**Features (17):**
```python
features = [
  'zone_disruption_frequency',  # historical events/month for zone
  'platform_risk_index',        # 0-1 (zepto=high, amazon=low)
  'daily_hours',                # 4, 8, 12
  'delivery_category_risk',     # food=0.7, grocery=0.8, ecommerce=0.4
  'months_active',              # experience reduces risk
  'season_monsoon',             # 1 if Jun-Sep
  'season_summer',              # 1 if Apr-May
  'city_risk_index',            # Mumbai=0.9, Bangalore=0.5
  'vehicle_ev',                 # EV=slightly higher risk in rain
  'avg_weekly_earnings',        # higher = higher coverage need
  'historical_claims_6m',       # past claims in 6 months
  'zone_flood_prone',           # binary
  'zone_heat_prone',            # binary
  'zone_aqi_prone',             # binary
  'partner_tenure_months',      # longer = lower risk
  'peak_hours_overlap',         # overlap with high-risk hours
  'day_of_week_risk'            # weekday vs weekend
]
```

**Output:** risk_score 0-100, where:
- 0-30: Low risk (Basic tier: ₹20-40/week)
- 31-60: Medium risk (Standard tier: ₹41-89/week)
- 61-80: Medium-High (Standard/Full: ₹71-99/week)
- 81-100: High risk (Full tier: ₹100-149/week)

### 2. Income Prediction Model (XGBoost Regressor)

**Features (15):**
```python
features = [
  'day_of_week',          # 0-6
  'hour_of_day',          # 0-23
  'weather_score',        # 0-100
  'aqi_score',            # 0-100
  'traffic_score',        # 0-100
  'platform_demand',      # 0-100
  'is_weekend',           # binary
  'is_peak_lunch',        # 11am-2pm binary
  'is_peak_dinner',       # 6pm-10pm binary
  'rainfall_mm_hr',       # actual rainfall
  'temperature',          # celsius
  'historical_avg_same_hour',
  'historical_avg_same_day',
  'zone_demand_index',
  'disruption_active'     # binary
]
```

**Output:** predicted_hourly_earnings in ₹

### 3. Fraud Detection Model (Isolation Forest)

```python
# Feature vector per claim:
fraud_features = [
  'gps_zone_match',          # 1 if GPS in disruption polygon, else 0
  'gps_movement_km',         # distance moved during event
  'gps_velocity_kmh',        # max velocity (>60 = suspicious)
  'order_attempts_count',    # number of order acceptances tried
  'app_interactions_count',  # number of app taps during event
  'app_session_duration',    # time app was active
  'nearby_workers_same_status', # ratio of nearby workers also inactive
  'claim_frequency_30d',     # claims in last 30 days
  'duplicate_event_flag',    # binary: same event claimed twice
  'weather_data_match',      # cross-source validation score
  'time_since_last_claim_days',
  'worker_tenure_days',
  'historical_fraud_score_avg'
]
```

**Threshold:** contamination=0.05 (5% expected fraud rate).
Isolation Forest score → normalize to 0-100 fraud score.
fraud_score > 70 → auto-reject
fraud_score 40-70 → manual review
fraud_score < 40 → auto-approve

### 4. Workability Score Engine

```python
def calculate_workability_score(weather: float, aqi: float, traffic: float, demand: float) -> int:
    """
    All inputs are normalized 0-100 (100 = best conditions)
    """
    ws = (weather * 0.35) + (aqi * 0.20) + (traffic * 0.20) + (demand * 0.25)
    
    # Flood zone override
    if weather < 15 and rainfall_mm_hr > 35:
        ws = min(ws, 20)  # force critical
    
    return round(ws)

# Trigger threshold: WS < 20 → auto-claim fires
# Sub-threshold categories:
# 80-100: Excellent
# 60-79: Good
# 40-59: Caution (send alert)
# 20-39: High Risk (pre-trigger warning)
# 0-19: TRIGGER (auto-claim fires)
```

### 5. Trust Score Engine

```python
def calculate_trust_score(fraud_score: int, pow_score: int, history_score: int) -> int:
    """
    fraud_score: 0-100 (higher = MORE fraudulent → invert for trust)
    pow_score: 0-100 (higher = more legitimate)
    history_score: 0-100 (higher = better history)
    """
    fraud_trust = 100 - fraud_score  # invert
    trust = (fraud_trust * 0.40) + (pow_score * 0.35) + (history_score * 0.25)
    return round(trust)

# Decision thresholds:
# trust >= 85: instant auto-approve (< 2 min)
# trust 70-84: fast-track approve (< 5 min)
# trust 40-69: manual review queue (2-4 hours)
# trust < 40: auto-reject
```

### 6. Proof of Work Score

```python
def calculate_pow_score(
    order_attempts: int,       # 0-10 attempts
    movement_km: float,        # GPS movement distance
    app_interactions: int,     # number of app taps
    nearby_workers_ratio: float # 0-1, ratio of nearby workers also inactive
) -> int:
    # Normalize each signal to 0-100
    order_score = min(100, order_attempts * 20)
    movement_score = min(100, movement_km * 50)  # 2km = 100
    interaction_score = min(100, app_interactions * 6)  # 17 taps = 100
    density_score = nearby_workers_ratio * 100
    
    pow = (order_score * 0.30) + (movement_score * 0.25) + \
          (interaction_score * 0.25) + (density_score * 0.20)
    return round(pow)
```

### 7. Dynamic Premium Calculator

```python
def calculate_premium(
    risk_score: int,
    zone: str,
    daily_hours: int,
    platform: str,
    season: str,
    trust_score: int
) -> dict:
    base = 60  # ₹60 base for food delivery
    
    zone_multipliers = {
        'Mumbai': 1.50, 'Delhi': 1.40, 'Hyderabad_Central': 1.30,
        'Chennai': 1.30, 'Bengaluru': 1.15, 'Hyderabad_Suburbs': 1.10
    }
    
    season_multipliers = {
        'monsoon': 1.30,    # Jun-Sep
        'pre_monsoon': 1.05, # Apr-May
        'summer': 1.10,     # Mar-May
        'winter': 0.95      # Nov-Feb
    }
    
    hours_factors = { 4: 1.0, 8: 1.13, 12: 1.27 }
    
    # Behavior discount (high trust = discount)
    behavior_discount = max(0, (trust_score - 70) * 0.05)  # up to ₹5 discount
    
    zone_load = base * (zone_multipliers.get(zone, 1.2) - 1.0)
    seasonal_load = base * (season_multipliers.get(season, 1.0) - 1.0)
    hours_load = base * (hours_factors.get(daily_hours, 1.13) - 1.0)
    
    total = base + zone_load + seasonal_load + hours_load - behavior_discount
    total = max(20, min(149, round(total)))  # clamp ₹20-₹149
    
    return {
        "base": base,
        "zone_loading": round(zone_load),
        "seasonal": round(seasonal_load),
        "hours_factor": round(hours_load),
        "ai_discount": round(behavior_discount),
        "total": total,
        "coverage_amount": round(total * 14.04),  # ~35.7% of ₹3500 weekly earnings
        "wallet_contribution": round(total * 0.10, 2)
    }
```

---

## RAG CHATBOT IMPLEMENTATION

### Knowledge Base Files (create these in backend/app/rag/knowledge_base/)

Create the following text files with relevant content:

**policy_terms.txt** — Full policy terms and conditions
**claim_faq.txt** — Frequently asked questions about claims
**trigger_thresholds.txt** — Exact thresholds for all 6 triggers
**premium_explainer.txt** — How premium is calculated
**pow_explainer.txt** — What Proof of Work is and how it works
**trust_score_explainer.txt** — Trust Score formula and thresholds
**wallet_explainer.txt** — Income Buffer Wallet mechanics
**govt_schemes.txt** — Relevant government schemes for gig workers

### Embedding Pipeline

```python
# backend/app/rag/embeddings.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
import pickle

MODEL_NAME = "all-MiniLM-L6-v2"  # ~80MB, runs locally, no API key

class EmbeddingPipeline:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.index = None
        self.chunks = []
        self.chunk_metadata = []
    
    def chunk_document(self, text: str, source: str, chunk_size: int = 256) -> list:
        """Split document into overlapping chunks"""
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size - 50):  # 50 word overlap
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append({"text": chunk, "source": source, "chunk_id": i})
        return chunks
    
    def build_index(self, knowledge_base_dir: str):
        """Build FAISS index from all .txt files in knowledge_base_dir"""
        all_chunks = []
        for file in Path(knowledge_base_dir).glob("*.txt"):
            text = file.read_text(encoding="utf-8")
            chunks = self.chunk_document(text, source=file.stem)
            all_chunks.extend(chunks)
        
        self.chunks = [c["text"] for c in all_chunks]
        self.chunk_metadata = all_chunks
        
        embeddings = self.model.encode(self.chunks, show_progress_bar=True)
        embeddings = np.array(embeddings).astype("float32")
        
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)  # Inner product (cosine sim after normalize)
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings)
        
        # Save index
        faiss.write_index(self.index, "rag_index.faiss")
        with open("rag_chunks.pkl", "wb") as f:
            pickle.dump({"chunks": self.chunks, "metadata": self.chunk_metadata}, f)
    
    def retrieve(self, query: str, top_k: int = 5) -> list:
        """Retrieve top-k relevant chunks for a query"""
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")
        faiss.normalize_L2(query_embedding)
        
        scores, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for score, idx in zip(scores[0], indices[0]):
            results.append({
                "text": self.chunks[idx],
                "source": self.chunk_metadata[idx]["source"],
                "score": float(score)
            })
        return results
```

### Gemini Chat Pipeline (FREE)

```python
# backend/app/rag/chat.py
import google.generativeai as genai
from app.rag.embeddings import EmbeddingPipeline
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
# Use gemini-2.0-flash-exp (completely free as of 2026)

class RAGChatbot:
    def __init__(self, embedding_pipeline: EmbeddingPipeline):
        self.embedder = embedding_pipeline
        self.model = genai.GenerativeModel("gemini-2.0-flash-exp")
    
    def build_system_prompt(self, worker_context: dict) -> str:
        return f"""You are GigGuard X AI assistant for gig workers in India.
        
Worker context:
- Name: {worker_context.get('full_name', 'Worker')}
- Platform: {worker_context.get('platform', 'Swiggy')}
- Zone: {worker_context.get('zone', 'Hyderabad')}
- Weekly Premium: ₹{worker_context.get('weekly_premium', 89)}
- Coverage: ₹{worker_context.get('coverage_amount', 1250)}
- Trust Score: {worker_context.get('trust_score', 80)}/100
- Active Policy: {worker_context.get('policy_number', 'N/A')}

Rules:
1. Answer ONLY questions about GigGuard X insurance, claims, payouts, premiums
2. Always explain WHY things happen (explainable AI)
3. Use simple language — the worker may not be highly educated
4. Keep responses under 150 words
5. Ground answers in the provided context documents
6. If asked in Hindi or Telugu, respond in that language
7. NEVER make up policy details not in the context"""
    
    async def chat(self, message: str, worker_context: dict, conversation_history: list = []) -> dict:
        # Retrieve relevant chunks
        retrieved_chunks = self.embedder.retrieve(message, top_k=5)
        context_text = "\n\n".join([f"[{c['source']}]: {c['text']}" for c in retrieved_chunks])
        
        # Build prompt
        full_prompt = f"""Context from GigGuard X knowledge base:
{context_text}

Worker question: {message}

Answer based on the context above. Be specific, use the worker's actual data where relevant."""
        
        # Build conversation history for Gemini
        history = []
        for msg in conversation_history[-6:]:  # last 3 turns
            history.append({"role": msg["role"], "parts": [msg["content"]]})
        
        # Start chat with system context
        chat = self.model.start_chat(history=history)
        
        response = await chat.send_message_async(full_prompt)
        
        sources = list(set([c["source"] for c in retrieved_chunks]))
        
        return {
            "response": response.text,
            "sources": sources,
            "retrieved_chunks": len(retrieved_chunks)
        }
```

---

## CELERY MONITORING TASK (runs every 15 minutes)

```python
# backend/app/tasks/monitor.py
from celery import shared_task
from app.services.workability import WorkabilityService
from app.integrations.weather import WeatherClient
from app.integrations.aqi import AQIClient
from app.services.trust_score import TrustScoreService
from app.services.proof_of_work import ProofOfWorkService

@shared_task(name="monitor.check_disruptions")
async def check_all_zones():
    """
    Runs every 15 minutes.
    1. Fetch weather + AQI for all active zones
    2. Calculate Workability Score per zone
    3. If WS < 20: create DisruptionEvent, trigger claims for all active policies in zone
    4. For each triggered claim: run fraud check → PoW check → Trust Score → auto-approve/reject
    5. For approved claims: initiate payout via Razorpay
    """
    
    active_zones = await get_all_active_zones()
    
    for zone in active_zones:
        weather_data = await WeatherClient.get_current(zone.lat, zone.lon)
        aqi_data = await AQIClient.get_current(zone.lat, zone.lon)
        
        ws_score = WorkabilityService.calculate(
            weather=weather_data.workability_component,
            aqi=aqi_data.workability_component,
            traffic=await get_traffic_score(zone),
            demand=await get_platform_demand(zone)
        )
        
        if ws_score < 20:
            disruption = await create_disruption_event(zone, weather_data, ws_score)
            await trigger_claims_for_zone(zone, disruption)

@shared_task(name="claims.process")
async def process_claim(claim_id: str):
    """Full claim processing pipeline"""
    claim = await get_claim(claim_id)
    worker = await get_worker(claim.worker_id)
    
    # Step 1: Fraud Check
    fraud_features = await collect_fraud_features(claim, worker)
    fraud_score = FraudDetectionService.score(fraud_features)
    
    # Step 2: Proof of Work
    pow_signals = await collect_pow_signals(claim, worker)
    pow_score = ProofOfWorkService.score(pow_signals)
    
    # Step 3: History Score
    history_score = await HistoryScoreService.calculate(worker.id)
    
    # Step 4: Trust Score
    trust_score = TrustScoreService.calculate(fraud_score, pow_score, history_score)
    
    # Update claim with scores
    await update_claim_scores(claim_id, fraud_score, pow_score, history_score, trust_score)
    
    # Step 5: Decision
    if trust_score >= 70:
        await approve_and_payout(claim, trust_score)
    elif trust_score >= 40:
        await flag_for_manual_review(claim)
    else:
        await reject_claim(claim, reason=f"Trust score {trust_score} below threshold")

@shared_task(name="payouts.execute")
async def execute_payout(claim_id: str):
    """Execute UPI payout via Razorpay"""
    # Uses Razorpay Test Mode - no real money
    # https://razorpay.com/docs/payments/test-mode
    pass
```

---

## FRONTEND PAGES (implement all)

### Routes Structure
```
/                           → LandingPage (public)
/login                      → LoginPage (public)
/register                   → RegisterPage (public)
/onboard                    → OnboardingPage (worker, first-time only)
/dashboard                  → DashboardPage (worker)
/policy                     → PolicyPage (worker)
/claims                     → ClaimsPage (worker)
/claims/:id                 → ClaimDetailPage (worker)
/trust-score                → TrustScorePage (worker)
/proof-of-work              → ProofOfWorkPage (worker)
/risk-engine                → RiskEnginePage (worker)
/wallet                     → WalletPage (worker)
/assistant                  → AssistantPage (worker)
/simulator                  → SimulatorPage (worker)
/insights                   → InsightsPage (worker)
/triggers                   → TriggersPage (worker)
/admin                      → AdminDashboard (admin/insurer only)
/admin/claims               → AdminClaimsPage (admin only)
/admin/fraud                → FraudCentrePage (admin only)
/admin/workers              → AdminWorkersPage (admin only)
```

### Key Components to Build

**WorkabilityScoreRing** — animated SVG ring showing 0-100 score
**TrustScoreComposite** — 3-column breakdown (Fraud/PoW/History)
**ProofOfWorkSignals** — 4 signal cards with progress bars
**EarningsChart** — weekly earnings vs expected vs lost (Recharts)
**ClaimFlowStepper** — 5-step horizontal progress (Detected→Verified→TrustCheck→Approved→Paid)
**TriggerMonitor** — live 6-trigger status list
**FraudNetworkGraph** — SVG cluster visualization
**ChatInterface** — RAG chatbot UI with typing indicators, source citations
**PremiumBreakdown** — itemized premium card with AI discount
**WalletCard** — buffer wallet with fill animation
**ZoneHeatmap** — grid-based risk visualization
**InsightCard** — AI-generated insight cards
**WeekForecast** — 7-day disruption forecast grid
**WhatIfSimulator** — 6-slider interactive tool
**AdminMetricCard** — metric with sparkline chart
**GamificationBadges** — XP bar + badge collection
**LanguageToggle** — EN/HI/TE switcher

---

## BUILD PHASES (implement in order, fully complete each before next)

---

### PHASE 1: Foundation & Auth
**Goal:** Working skeleton with auth, DB, and basic worker flow.

**Backend tasks:**
1. Set up FastAPI project structure exactly as defined above
2. Configure PostgreSQL + SQLAlchemy + Alembic
3. Create all database models (users, worker_profiles, policies, claims, payouts, wallet tables)
4. Run initial migration: `alembic revision --autogenerate -m "initial" && alembic upgrade head`
5. Implement JWT auth (register, login, refresh, logout)
6. Implement role-based route protection middleware
7. Implement worker onboarding endpoint with basic risk score calculation
8. Implement policy creation endpoint
9. Set up Redis connection
10. Basic FastAPI health check endpoint
11. Configure CORS for frontend

**Frontend tasks:**
1. Scaffold React + Vite + TypeScript + Tailwind project
2. Set up React Router with all routes defined above
3. Build auth store (Zustand) with JWT token management
4. Build LandingPage with hero section and feature highlights
5. Build LoginPage + RegisterPage with React Hook Form + Zod validation
6. Build OnboardingPage — 5-step wizard matching backend spec
7. Build protected route wrapper component
8. Build basic Layout with Sidebar + Topbar
9. Set up Axios instance with JWT interceptors (auto-attach token, handle 401 refresh)

**Deliverable:** User can register, login, complete onboarding, see empty dashboard.

---

### PHASE 2: ML Models & Risk Engine
**Goal:** All ML models trained, risk scoring live, dynamic premium working.

**Backend tasks:**
1. Generate synthetic training datasets (10,000 records each) using numpy/pandas
2. Train XGBoost risk score model → save to `backend/app/ml/models/risk_model.pkl`
3. Train XGBoost income prediction model → save to `backend/app/ml/models/income_model.pkl`
4. Train Isolation Forest fraud model → save to `backend/app/ml/models/fraud_model.pkl`
5. Implement `WorkabilityService` with formula as specified
6. Implement `RiskScoreService` wrapping XGBoost model
7. Implement `IncomePredicationService` wrapping XGBoost regressor
8. Implement `FraudDetectionService` wrapping Isolation Forest
9. Implement `TrustScoreService` with composite formula
10. Implement `ProofOfWorkService` with 4-signal scoring
11. Implement `PricingService` with full premium formula
12. Wire risk score into onboarding endpoint
13. Wire pricing into policy creation endpoint
14. Add `/api/v1/workers/me/insights` endpoint with income forecast

**Frontend tasks:**
1. Build DashboardPage with WorkabilityScoreRing (live from API)
2. Build TrustScoreComposite component
3. Build EarningsChart with Recharts
4. Build RiskEnginePage showing WS formula breakdown
5. Build premium breakdown in OnboardingPage step 3
6. Show AI risk scan animation in onboarding step 4

**Deliverable:** Risk scoring live, premium calculated by ML model, dashboard shows WS ring.

---

### PHASE 3: External API Integrations & Trigger Engine
**Goal:** Live weather/AQI data flowing, Workability Score updating in real-time.

**Backend tasks:**
1. Implement `WeatherClient` (OpenWeatherMap free API)
   - `get_current_conditions(lat, lon)` → temperature, rainfall_mm_hr, heat_index, wind
   - `get_forecast_7day(lat, lon)` → daily disruption probability
   - Cache in Redis with 10-minute TTL
2. Implement `AQIClient` (WAQI free API)
   - `get_current_aqi(lat, lon)` → AQI value, PM2.5, PM10
   - Cache in Redis with 15-minute TTL
3. Implement `GeocodingClient` (Nominatim, no API key)
   - `reverse_geocode(lat, lon)` → zone/city/district
4. Create live Workability Score endpoint that fetches real data
5. Implement `DisruptionEventService` — creates events when thresholds breached
6. Implement 6 trigger threshold checks:
   - heavy_rain: rainfall_mm_hr > 35
   - extreme_heat: heat_index > 40
   - flood: IMD alert (mock for demo)
   - severe_aqi: aqi > 300
   - curfew: government alert (mock for demo)
   - app_outage: platform_uptime < 98% (mock for demo)
7. Set up Celery beat scheduler: monitor task every 15 minutes
8. Implement admin demo endpoint `POST /api/v1/admin/trigger-disruption`
9. WebSocket endpoint for real-time WS updates: `WS /ws/triggers/{worker_id}`

**Frontend tasks:**
1. Build TriggersPage with live trigger status (polls API every 30s)
2. Build live weather widget in PolicyPage
3. Add WebSocket hook for real-time WS score updates in dashboard
4. Build 7-day forecast grid in InsightsPage
5. Build predictive alert cards in InsightsPage
6. Add "Simulate Disruption" button for demo (admin view)

**Deliverable:** Real weather data, live WS score updating, trigger simulation working.

---

### PHASE 4: Claims Automation & Payout
**Goal:** Full zero-touch claim pipeline from trigger to UPI payout.

**Backend tasks:**
1. Implement `AutoClaimService`:
   - On disruption event → find all active policies in affected zone
   - Create claim records for each affected worker
   - Calculate estimated_loss: duration × hourly_avg × payout_percentage
   - Payout percentages: rain=60%, heat=40%, flood=100%, aqi=50%, curfew=100%, outage=30%
2. Implement full claim processing pipeline as Celery task:
   - fraud_check → pow_check → trust_score → decision → payout
3. Implement mock PoW signal collection (simulate signals, explained in code)
4. Implement `RazorpayService` (test mode):
   - Create fund account for worker UPI
   - Create payout to fund account
   - Webhook handler for payout status
   - Uses Razorpay test mode keys — no real money
5. Implement claim status webhook — push updates to frontend via WebSocket
6. Implement `WalletService`:
   - Deposit 10% of premium on policy creation
   - Use wallet for minor disruptions (WS 20-40)
   - Year-end cashback calculation
7. Implement claim appeal endpoint
8. Implement GenAI claim explanation generation per claim
9. Full admin claims management endpoints (approve/reject/flag)

**Frontend tasks:**
1. Build ClaimsPage with claim list + status badges
2. Build ClaimDetailPage with:
   - ClaimFlowStepper (5 steps with live status)
   - TrustScoreComposite breakdown
   - ProofOfWorkSignals
   - AI Explanation box
   - Payout details
3. Build WalletPage with transaction history + projected cashback
4. Show payout success modal with UPI transfer details
5. Build fraud transparency explanation component
6. WebSocket listener for real-time claim status updates

**Deliverable:** Full auto-claim lifecycle working end-to-end. Simulate rain → see claim created → trust score evaluated → payout sent.

---

### PHASE 5: RAG Chatbot & AI Assistant
**Goal:** Fully working GenAI chatbot grounded in policy knowledge base.

**Backend tasks:**
1. Create all knowledge base .txt files (8 files as listed above)
2. Implement `EmbeddingPipeline` using sentence-transformers (exact code above)
3. Build FAISS index: `python -m app.rag.embeddings build`
4. Implement `RAGChatbot` using Gemini 2.0 Flash (exact code above)
5. Implement conversation history storage in Redis (per worker, TTL 24h)
6. Implement `POST /api/v1/chat/message` with streaming SSE support
7. Implement suggested questions generation
8. Implement multilingual response detection (Hindi/Telugu input → respond in same language)
9. Add worker context injection (policy number, premium, last claim status into prompt)

**Frontend tasks:**
1. Build full ChatInterface component:
   - Message bubbles (bot/user differentiation)
   - Typing indicator (animated dots)
   - Source citation badges
   - Suggested question chips
   - Streaming text rendering (SSE)
2. Build AssistantPage housing the chat interface + RAG architecture explainer
3. Quick-question chips: "What's covered?", "My premium?", "Payout status?", "PoW score?"
4. Language toggle integration (EN/HI/TE)
5. Explainable AI boxes on ClaimDetailPage powered by chatbot

**Deliverable:** Working chatbot that answers policy questions with source citations in EN/HI/TE.

---

### PHASE 6: Admin Dashboard & Analytics
**Goal:** Full admin and insurer views with analytics.

**Backend tasks:**
1. Implement full admin dashboard metrics endpoint
2. Implement fraud alerts endpoint with network graph data
3. Implement reserve forecast endpoint (ML-powered 7-day payout prediction)
4. Implement admin claim management (approve/reject with reason)
5. Implement zone-wise analytics (policies, claims, fraud by zone)
6. Implement financial insights (premium vs payout ratio, loss ratio, profitability)
7. Fraud cluster data endpoint (for network graph viz)
8. Worker search + filter endpoint
9. Export endpoints (CSV export of claims/workers for admin)

**Frontend tasks:**
1. Build AdminDashboard with:
   - 4 metric cards with Recharts sparklines
   - Zone distribution bar chart
   - Loss ratio trend chart
   - Reserve forecast card
2. Build FraudCentrePage:
   - FraudNetworkGraph (SVG — fraud rings visualization)
   - Fraud flags table with action buttons
   - Detection analytics
3. Build AdminClaimsPage:
   - Claims table with filters (status, zone, date range)
   - Approve/Reject modals with reason input
   - Bulk action support
4. Build AdminWorkersPage:
   - Worker table with search
   - Risk score distribution chart
   - Worker detail slide-out panel
5. Role-based navigation (admin sees admin routes, worker doesn't)

**Deliverable:** Full admin/insurer dashboard with analytics, fraud management, claim approval.

---

### PHASE 7: Polish, PWA & Advanced Features
**Goal:** Production-ready quality, all advanced features implemented.

**Backend tasks:**
1. Implement gamification endpoints:
   - XP award on: policy renewal (+50), clean claim week (+30), fraud-free month (+100)
   - Level thresholds: 1=0, 2=200, 3=500, 4=1000, 5=2000 XP
   - Badge award logic
2. Implement adaptive learning: weekly model retraining job (Celery beat)
3. Implement What-if simulation endpoint: POST /api/v1/workers/simulate
4. Implement multilingual insight generation via Gemini
5. Rate limiting (Redis-based): 100 req/min per user
6. Request logging middleware
7. Error handling: global exception handler, structured error responses
8. API documentation polish (OpenAPI/Swagger auto-generated by FastAPI)
9. Database query optimization (add indexes on frequently queried columns)
10. Comprehensive test suite (pytest): aim for 80% coverage

**Frontend tasks:**
1. Build SimulatorPage with 6 sliders + live results + AI explanation
2. Build InsightsPage with full predictive alerts + personalized insights
3. Build GamificationSection in dashboard (XP bar + badges)
4. Implement PWA: add manifest.json + service worker for offline caching
5. Implement multilingual toggle (EN/HI/TE) with i18next
6. Add Web Push notification registration for disruption alerts
7. Add skeleton loading states everywhere
8. Add proper error boundaries
9. Implement dark/light mode toggle
10. Responsive design audit — test on mobile 375px width
11. Accessibility audit (ARIA labels, keyboard navigation)

**Deliverable:** Production-quality app. Everything works offline (cached), multilingual, gamified, accessible.

---

### PHASE 8: Docker, Deployment & CI/CD
**Goal:** Fully containerized, deployable, with CI/CD pipeline.

**Tasks:**
1. Write `Dockerfile` for backend (multi-stage: builder + runtime)
2. Write `Dockerfile` for frontend (nginx serving built assets)
3. Write `docker-compose.yml` for production (backend + frontend + postgres + redis + celery)
4. Write `docker-compose.dev.yml` for development (with hot reload)
5. Write `nginx/nginx.conf` (reverse proxy: /api → backend, / → frontend)
6. Write `.github/workflows/ci.yml`:
   - On push: run pytest, eslint
   - On merge to main: build Docker images, push to registry
7. Write `Makefile` with commands:
   - `make dev` — start dev environment
   - `make build` — build production images
   - `make test` — run all tests
   - `make migrate` — run Alembic migrations
   - `make seed` — seed database with demo data
8. Write `scripts/seed_demo_data.py` — creates demo workers, policies, claims for hackathon demo
9. Write full `.env.example` documenting every required env variable
10. Document local setup in README (3 commands to get running)

**Deliverable:** `git clone && make dev` → app running on localhost.

---

## ENVIRONMENT VARIABLES (all required)

```env
# Database
DATABASE_URL=postgresql+asyncpg://gigguard:gigguard123@localhost:5432/gigguard_db
REDIS_URL=redis://localhost:6379/0

# Auth
SECRET_KEY=your-256-bit-random-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Free AI APIs
GEMINI_API_KEY=your_free_key_from_aistudio.google.com
# HuggingFace runs locally — no API key needed for sentence-transformers

# Free Weather APIs
OPENWEATHERMAP_API_KEY=your_free_key_from_openweathermap.org
WAQI_API_KEY=your_free_key_from_aqicn.org
# Nominatim — no key needed

# Razorpay (test mode — free)
RAZORPAY_KEY_ID=rzp_test_xxxxxxxxxxxx
RAZORPAY_KEY_SECRET=your_test_secret
RAZORPAY_ACCOUNT_NUMBER=your_test_account

# App
APP_ENV=development
FRONTEND_URL=http://localhost:5173
BACKEND_URL=http://localhost:8000
CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]

# Celery
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2
```

---

## CRITICAL IMPLEMENTATION RULES

1. **Never block the event loop** — All I/O in FastAPI must be `async/await`. Use `httpx.AsyncClient` not `requests`.

2. **Always validate with Pydantic** — Every request body, response, and config value must go through Pydantic schemas.

3. **Dependency injection for auth** — Use FastAPI `Depends()` for auth and DB session injection everywhere.

4. **Errors must be informative** — Never return bare 500. Every error must include `code`, `message`, and optionally `details`.

5. **ML models load once** — Load ML models at startup using FastAPI `lifespan` context manager. Never reload per request.

6. **RAG index builds once** — Build FAISS index on first startup, cache to disk. Reload from disk on subsequent starts.

7. **Gemini rate limiting** — Gemini free tier has rate limits. Add exponential backoff retry logic. Cache responses for identical queries (Redis, TTL 1 hour).

8. **Sentence Transformers downloads model on first run** — This takes ~2 minutes. Show progress. Works fully offline after first download.

9. **All monetary values in paise** — Store amounts as `DECIMAL(10,2)` representing rupees, not paise. Add validation to prevent negative amounts.

10. **Worker can only see their own data** — Every `/workers/me/*` endpoint must verify JWT sub matches the worker_profile.user_id.

11. **React Query for all server state** — Never use useState + useEffect for data fetching. Use React Query hooks.

12. **Tailwind only** — No CSS files, no styled-components. Pure Tailwind utility classes.

13. **TypeScript strict mode** — No `any` types. Define all API response types in `/src/types/`.

14. **Handle API failures gracefully** — Every API call in frontend must have error state UI. Never show blank screens on failure.

---

## DEMO DATA (seed for hackathon)

Create a seeder that generates:
- 3 demo workers:
  - Ravi Kumar (worker/worker123) — Hyderabad Central, Swiggy, medium-high risk
  - Priya Sharma (priya/worker123) — Mumbai, Zomato, high risk
  - Arjun Reddy (arjun/worker123) — Bengaluru, Zepto, low risk
- 1 admin user: admin@gigguard.in / admin123
- 1 insurer user: insurer@guidewire.com / insurer123
- Each worker has: active policy, 3-5 historical claims (mix of paid/flagged), wallet balance
- 2 active disruption events (rain in Hyderabad, heat in Mumbai)
- 1 claim in "fraud_check" status (for demo)
- 1 claim that just got auto-approved and paid out (for demo)

---

## GETTING STARTED (3 commands)

```bash
git clone https://github.com/[username]/gigguard-x.git
cd gigguard-x
make dev  # starts everything: postgres, redis, backend, frontend, celery
```

Then open: http://localhost:5173
Login with: ravi@gigguard.in / worker123

---

## NOTES FOR THE AI AGENT

- Start with Phase 1. Do not write Phase 2 code until Phase 1 fully works.
- Write tests as you go — not after.
- Use `make test` to verify each phase before proceeding.
- The hackathon judges will run `make dev` and click through the demo. It MUST work first try.
- The "Simulate Disruption" button in the admin panel is the most important demo feature — make it bulletproof.
- Gemini 2.0 Flash free tier provides 15 RPM and 1M tokens/day — more than enough.
- sentence-transformers/all-MiniLM-L6-v2 is ~80MB and requires no API key — it just works.
- OpenWeatherMap free tier gives 1000 calls/day — more than enough with 15-minute polling.
- If any external API is down during the hackathon, have mock fallback data ready.

---
END OF PROMPT
