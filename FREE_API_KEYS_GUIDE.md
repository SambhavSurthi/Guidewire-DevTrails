# GigGuard X — Free API Keys Setup Guide
# =========================================
# All APIs used are FREE. No credit card required.
# This guide explains how to get each key in under 5 minutes.

---

## 1. Google Gemini API (AI Chatbot) — FREE

**What it does:** Powers the RAG chatbot. 
**Cost:** Free. 15 requests/min, 1 million tokens/day — more than enough.
**Model:** gemini-2.0-flash-exp

**How to get it:**
1. Go to: https://aistudio.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key (starts with "AIza...")
5. Add to .env: `GEMINI_API_KEY=AIzaSy...`

**That's it. No billing setup needed.**

---

## 2. OpenWeatherMap API (Weather Data) — FREE

**What it does:** Real-time rainfall, temperature, heat index for trigger detection.
**Cost:** Free. 1,000 calls/day, 60 calls/min — perfect with 15-min polling.

**How to get it:**
1. Go to: https://openweathermap.org/api
2. Click "Sign Up" (top right)
3. Fill out the form (email + password)
4. Verify your email
5. Go to: https://home.openweathermap.org/api_keys
6. Your default key is already there (or click "Generate" for a new one)
7. Copy the key
8. Add to .env: `OPENWEATHERMAP_API_KEY=abc123...`

**Note:** Key activates within ~2 hours of signup. Use mock data in the meantime.

**APIs we use (both free):**
- Current Weather: `GET /data/2.5/weather?lat={lat}&lon={lon}&appid={key}`
- One Call 3.0: `GET /data/3.0/onecall?lat={lat}&lon={lon}&appid={key}`

---

## 3. WAQI Air Quality API (AQI Data) — FREE

**What it does:** Real-time AQI for severe pollution trigger.
**Cost:** Free. 1,000 calls/day.

**How to get it:**
1. Go to: https://aqicn.org/data-platform/token/
2. Enter your email address
3. Click "Submit"
4. Check your email for the token
5. Copy the token
6. Add to .env: `WAQI_API_KEY=your_token_here`

**API we use:**
- `GET https://api.waqi.info/feed/geo:{lat};{lon}/?token={key}`

---

## 4. Razorpay (Payment Gateway) — FREE TEST MODE

**What it does:** Simulates UPI payouts to workers. No real money moves.
**Cost:** Free. Test mode has no transaction limits.

**How to get it:**
1. Go to: https://dashboard.razorpay.com/signup
2. Create a free account (business name: "GigGuard X Demo")
3. After signup, make sure you're in **Test Mode** (toggle in the sidebar)
4. Go to Settings → API Keys → Generate Test Key
5. You'll get two keys:
   - Key ID (starts with `rzp_test_`)
   - Key Secret (shown once — copy immediately)
6. Add to .env:
   ```
   RAZORPAY_KEY_ID=rzp_test_xxxxxxxxxxxx
   RAZORPAY_KEY_SECRET=your_secret_here
   ```
7. For Account Number: Go to "Fund Accounts" in test mode, create one.

**Test mode payout API:**
```
POST https://api.razorpay.com/v1/payouts
```

---

## 5. Nominatim Geocoding — NO KEY NEEDED

**What it does:** Converts GPS coordinates to zone/city names.
**Cost:** Completely free. No signup.

**Usage restriction:** Must include a User-Agent header with your app name and email.
```
User-Agent: gigguardx/1.0 (your-email@example.com)
```

**API:**
```
GET https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json
```

**Already configured in .env.example — just update the email in User-Agent.**

---

## 6. HuggingFace Sentence Transformers — NO API KEY NEEDED

**What it does:** Generates text embeddings for RAG retrieval.
**Cost:** Runs 100% locally on your machine. No internet needed after first download.
**Model:** `all-MiniLM-L6-v2` (~80MB)

**Setup:**
```bash
pip install sentence-transformers
```

The model downloads automatically on first run:
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
# Downloads ~80MB on first run, then cached locally
```

**No API key, no rate limits, no cost.**

---

## Summary Checklist

| API | Key Required | Cost | Time to Setup |
|-----|-------------|------|---------------|
| Google Gemini | Yes | Free | 2 minutes |
| OpenWeatherMap | Yes | Free | 3 minutes (key activates in ~2hr) |
| WAQI AQI | Yes (email) | Free | 2 minutes |
| Razorpay | Yes (test mode) | Free | 5 minutes |
| Nominatim | No | Free | Instant |
| Sentence Transformers | No | Free | Instant (model downloads on first run) |

**Total setup time: ~15 minutes**
**Total cost: ₹0**

---

## If APIs Aren't Working Yet (Fallback)

The backend has mock data fallbacks for all APIs.
Set in .env to use mocks during development:
```
USE_MOCK_WEATHER=true
USE_MOCK_AQI=true
USE_MOCK_PAYMENTS=true
```

Mock data simulates realistic values for Hyderabad, Mumbai, Bengaluru, Chennai, Delhi.
