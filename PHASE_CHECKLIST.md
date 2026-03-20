# GigGuard X — Build Progress Tracker
# ======================================
# Check off items as you complete them.
# Each phase must be 100% complete before starting the next.

---

## PHASE 1: Foundation & Auth
**Status:** [ ] Not Started  [ ] In Progress  [x] Complete

### Backend
- [ ] FastAPI project scaffold with exact folder structure
- [ ] SQLAlchemy models: users, worker_profiles, policies, claims, payouts, wallet, transactions
- [ ] Alembic initial migration created and applied
- [ ] JWT auth: register, login, refresh, logout endpoints
- [ ] Role-based middleware (worker / admin / insurer)
- [ ] Worker onboarding endpoint (basic, returns mock risk score for now)
- [ ] Policy creation endpoint (basic weekly premium)
- [ ] Redis connection configured
- [ ] CORS configured for frontend
- [ ] Health check endpoint
- [ ] Pydantic schemas for all request/response bodies
- [ ] Error handling middleware (structured JSON errors)

### Frontend
- [ ] React + Vite + TypeScript scaffold
- [ ] Tailwind CSS configured with custom colors
- [ ] React Router with all routes defined
- [ ] Zustand auth store (JWT tokens, user data, persist to localStorage)
- [ ] Axios instance with JWT interceptor (attach token, auto-refresh on 401)
- [ ] LandingPage (hero + features + CTA)
- [ ] LoginPage (React Hook Form + Zod, show errors)
- [ ] RegisterPage (React Hook Form + Zod)
- [ ] OnboardingPage (5-step wizard, step 1-5 UI complete, calls API on step 5)
- [ ] Protected route wrapper
- [ ] Sidebar navigation component
- [ ] Topbar component (user chip, live badge)
- [ ] Empty DashboardPage (shows "welcome" message)
- [ ] React Query configured with proper defaults

**Phase 1 Verification:** Register new user → complete onboarding → land on dashboard ✓

---

## PHASE 2: ML Models & Risk Engine
**Status:** [ ] Not Started  [ ] In Progress  [ ] Complete

### Backend
- [ ] Synthetic dataset generation script (10,000 records each)
- [ ] XGBoost risk score model trained + saved (risk_model.pkl)
- [ ] XGBoost income prediction model trained + saved (income_model.pkl)
- [ ] Isolation Forest fraud model trained + saved (fraud_model.pkl)
- [ ] WorkabilityService with 4-factor formula
- [ ] RiskScoreService wrapping XGBoost
- [ ] IncomePredicationService with 7-day forecast
- [ ] FraudDetectionService wrapping Isolation Forest
- [ ] TrustScoreService composite formula
- [ ] ProofOfWorkService 4-signal scorer
- [ ] PricingService full premium formula
- [ ] Models load at startup (FastAPI lifespan)
- [ ] Risk score wired into onboarding endpoint
- [ ] Dynamic pricing wired into policy creation
- [ ] /api/v1/workers/me/insights endpoint complete

### Frontend
- [ ] WorkabilityScoreRing SVG component (animated)
- [ ] DashboardPage fully built (WS ring, metrics, earnings chart, insights)
- [ ] EarningsChart with Recharts (expected vs actual vs lost)
- [ ] TrustScoreComposite component (3-column)
- [ ] RiskEnginePage (WS formula, income prediction, heatmap)
- [ ] Premium breakdown shown in onboarding step 3
- [ ] AI risk scan animation in onboarding step 4

**Phase 2 Verification:** Onboard worker → see risk score 62 → see premium ₹89 → dashboard WS ring shows live ✓

---

## PHASE 3: External APIs & Trigger Engine
**Status:** [ ] Not Started  [ ] In Progress  [ ] Complete

### Backend
- [ ] WeatherClient (OpenWeatherMap) with Redis caching (10-min TTL)
- [ ] AQIClient (WAQI) with Redis caching (15-min TTL)
- [ ] GeocodingClient (Nominatim) with caching
- [ ] Mock data fallbacks for all external APIs (USE_MOCK_* flags)
- [ ] Live Workability Score endpoint (fetches real data)
- [ ] DisruptionEventService (creates events on threshold breach)
- [ ] All 6 trigger threshold checks implemented
- [ ] Celery beat scheduler: monitor task every 15 minutes
- [ ] Admin demo endpoint: POST /api/v1/admin/trigger-disruption
- [ ] WebSocket endpoint: WS /ws/triggers/{worker_id}
- [ ] 7-day disruption forecast endpoint

### Frontend
- [ ] TriggersPage (6 trigger cards, live status, 30s polling)
- [ ] Live weather widget on PolicyPage
- [ ] WebSocket hook for real-time WS updates
- [ ] 7-day forecast grid (7 cards with icons + scores)
- [ ] Predictive alert cards in InsightsPage
- [ ] "Simulate Disruption" button in admin view

**Phase 3 Verification:** Real weather data in triggers page → simulate rain → WS score drops to 18 ✓

---

## PHASE 4: Claims Automation & Payout
**Status:** [ ] Not Started  [ ] In Progress  [ ] Complete

### Backend
- [ ] AutoClaimService: find affected workers, create claim records
- [ ] Payout percentage calculation (60% rain, 40% heat, etc.)
- [ ] Full claim Celery task pipeline (fraud→pow→trust→decision→payout)
- [ ] Mock PoW signal collection (realistic simulation)
- [ ] RazorpayService (test mode): fund account creation + payout execution
- [ ] Razorpay webhook handler (payout status updates)
- [ ] Claim status WebSocket push to frontend
- [ ] WalletService (deposit 10% on policy create, use for minor events)
- [ ] Year-end cashback calculation
- [ ] AI explanation generation per claim (Gemini)
- [ ] Claim appeal endpoint
- [ ] Admin claim management endpoints

### Frontend
- [ ] ClaimsPage (list with status badges + filters)
- [ ] ClaimDetailPage (stepper + trust breakdown + PoW signals + explanation)
- [ ] ClaimFlowStepper component (5 steps, live WebSocket updates)
- [ ] ProofOfWorkSignals component (4 signal bars)
- [ ] Payout success modal (amount + UPI ref + AI explanation)
- [ ] WalletPage (balance, transactions, projected cashback)
- [ ] Fraud transparency explanation component
- [ ] WebSocket listener for real-time claim updates

**Phase 4 Verification:** Simulate rain → claim auto-created → trust score evaluated → ₹525 payout modal appears ✓

---

## PHASE 5: RAG Chatbot
**Status:** [ ] Not Started  [ ] In Progress  [ ] Complete

### Backend
- [ ] Knowledge base .txt files created (8 files)
- [ ] EmbeddingPipeline with sentence-transformers (all-MiniLM-L6-v2)
- [ ] FAISS index built from knowledge base
- [ ] RAGChatbot with Gemini 2.0 Flash
- [ ] Conversation history in Redis (TTL 24h)
- [ ] POST /api/v1/chat/message endpoint (with SSE streaming)
- [ ] Suggested questions generation
- [ ] Multilingual detection (HI/TE → respond in same language)
- [ ] Worker context injection into prompt

### Frontend
- [ ] ChatInterface component (bubbles, typing indicator, source citations)
- [ ] AssistantPage (chat + RAG architecture explainer)
- [ ] Quick-question chips (6 preset questions)
- [ ] Streaming SSE text rendering
- [ ] Language toggle (EN/HI/TE) integrated with chatbot

**Phase 5 Verification:** Ask "Why was my payout Rs 525?" → get grounded answer with source citation ✓

---

## PHASE 6: Admin Dashboard
**Status:** [ ] Not Started  [ ] In Progress  [ ] Complete

### Backend
- [ ] Admin dashboard metrics endpoint
- [ ] Fraud alerts endpoint with network graph data
- [ ] ML-powered 7-day reserve forecast
- [ ] Admin claim approval/rejection endpoints
- [ ] Zone-wise analytics endpoint
- [ ] Financial insights (loss ratio, profitability)
- [ ] Fraud cluster data endpoint
- [ ] Worker search + filter endpoint
- [ ] CSV export endpoints

### Frontend
- [ ] AdminDashboard (4 metric cards + sparklines + reserve forecast)
- [ ] FraudCentrePage (network graph + flags table + analytics)
- [ ] AdminClaimsPage (table + filters + approve/reject modals)
- [ ] AdminWorkersPage (table + search + detail panel)
- [ ] Role-based navigation (admin-only routes hidden from workers)
- [ ] FraudNetworkGraph SVG component

**Phase 6 Verification:** Login as admin → see all 12,847 policies → approve a flagged claim ✓

---

## PHASE 7: Polish & Advanced Features
**Status:** [ ] Not Started  [ ] In Progress  [ ] Complete

### Backend
- [ ] Gamification XP/level/badge endpoints
- [ ] Weekly adaptive model retraining Celery task
- [ ] What-if simulation endpoint
- [ ] Rate limiting (100 req/min per user)
- [ ] Structured logging (JSON format)
- [ ] Global error handler
- [ ] Database indexes optimized
- [ ] 80%+ test coverage achieved

### Frontend
- [ ] SimulatorPage (6 sliders + live results + AI explanation)
- [ ] Gamification XP bar + badges in dashboard
- [ ] PWA manifest + service worker
- [ ] i18next multilingual (EN/HI/TE translations)
- [ ] Web Push notification registration
- [ ] Skeleton loading states throughout
- [ ] Error boundaries
- [ ] Dark/light mode toggle
- [ ] Mobile responsive at 375px ✓
- [ ] Accessibility (ARIA labels) ✓

**Phase 7 Verification:** Full app works on mobile, all 3 languages, notifications on disruption ✓

---

## PHASE 8: Docker & Deployment
**Status:** [ ] Not Started  [ ] In Progress  [ ] Complete

- [ ] Backend Dockerfile (multi-stage)
- [ ] Frontend Dockerfile (nginx)
- [ ] docker-compose.yml (production)
- [ ] docker-compose.dev.yml (development with hot reload)
- [ ] nginx.conf (reverse proxy)
- [ ] GitHub Actions CI/CD workflow
- [ ] Makefile with all commands
- [ ] seed_demo_data.py complete
- [ ] `make dev` starts everything in 1 command ✓
- [ ] README with 3-command setup ✓

**Phase 8 Verification:** `git clone && make dev` → app running with demo data in under 5 minutes ✓

---

## FINAL CHECKLIST (before hackathon demo)

- [ ] `make dev` works from a fresh clone
- [ ] All 3 demo users login correctly
- [ ] Onboarding flow completes in < 2 minutes
- [ ] Risk score appears on onboarding step 4
- [ ] Dashboard WS ring updates every 15 seconds
- [ ] "Simulate Disruption" creates claims visibly
- [ ] Claim processes to "Paid" within 30 seconds in demo mode
- [ ] Chatbot responds to "Why was my payout Rs 525?"
- [ ] Admin can see fraud alerts and approve/reject claims
- [ ] App works on mobile phone (375px)
- [ ] All pages load in < 2 seconds
- [ ] No uncaught console errors
- [ ] No broken API calls (all return 200/201)
