# Executive Decision Intelligence

> **Illustrative Organization:** Microsoft Corporation (Prototype)  
> **Notice:** **SYNTHETIC DEMO DATA — NOT REAL COMPANY DATA**  
> All records, metrics, and relationships in this application are mathematically simulated for decision intelligence demonstration purposes only.

---

## 🎯 Executive Overview & Business Value

Executive decision-makers frequently face a fragmented landscape of disconnected departmental dashboards:
* **Finance** tracks Revenue, Operating Margin, and Free Cash Flow.
* **Operations & Engineering** tracks Cloud SLA Delivery, Latency, and Server Capacity Utilization.
* **Marketing** tracks Campaign Spend, CAC, and Enterprise Pipeline.
* **Human Resources** tracks Voluntary Attrition, Critical Vacancy Rates, and Employee NPS.
* **Customer Success** tracks Account Churn, Net Retention Rate (NRR), and CSAT.

When high-level KPIs deviate (e.g. Operating Margin compresses despite strong top-line revenue), traditional tools show *what* happened, but fail to explain *why* or identify *which concrete action* to take.

**Executive Decision Intelligence** solves this by:
1. **Validating Data Freshness & Reconciling Financial Identities** in real-time.
2. **Decomposing Value Driver Trees** mapping operational drivers to Operating Margin and Cash Flow.
3. **Detecting Anomalies & Target Deviations** using rolling statistical Z-scores.
4. **Analyzing Lagged Relationships with Granger Causality** to separate true predictive drivers from coincident correlations.
5. **Answering Natural Language Executive Questions** through local, deterministic computations.
6. **Generating Prioritized, Evidence-Backed Management Actions** with assigned owners, confidence scores, impact estimates, and governance safeguards.

---

## 🏗️ Repository Architecture (Root-Level Structure)

All application modules, configuration files, and assets are housed directly in the root directory without subfolders, ensuring seamless zero-configuration deployment to GitHub and Streamlit Community Cloud:

| File | Purpose |
| :--- | :--- |
| `app.py` | Main Streamlit interactive web application with multi-view navigation, executive cockpit, and dark navy/purple styling. |
| `data_generator.py` | Cross-departmental synthetic data engine generating 36 continuous monthly periods with embedded causal shock mechanics and fixed random seeds. |
| `analytics_engine.py` | Core mathematical computation engine: accounting reconciliation, Z-score anomalies, Granger causality, multivariate driver sensitivities, scenario simulator, and NL query parser. |
| `ui_components.py` | Plotly visual chart builders (Interactive Sunburst Value Tree, Trajectory & Anomaly charts, Lead-Lag heatmaps, Scenario comparison bars, Sensitivity tornado). |
| `export_manager.py` | Download service generating comprehensive formatted Executive Briefs (Markdown/Text) and structured CSV packages. |
| `requirements.txt` | Python package dependencies. |
| `README.md` | Complete documentation, Windows-friendly setup instructions, and governance framework. |

---

## 🚀 Quick Start Guide (Windows-Friendly)

Follow these simple steps in PowerShell or Command Prompt to launch the application locally.

### Step 1: Open PowerShell or Terminal
Open PowerShell and navigate to the project directory:
```powershell
cd C:\Users\DELL\.gemini\antigravity\scratch\executive_decision_intelligence
```

### Step 2: Create and Activate a Virtual Environment
```powershell
# Create virtual environment named .venv
python -m venv .venv

# Activate the virtual environment
.\.venv\Scripts\Activate.ps1
```
*(If script execution is restricted on Windows, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then activate).*

### Step 3: Install Required Packages
```powershell
pip install -r requirements.txt
```

### Step 4: Launch the Streamlit Web Application
```powershell
streamlit run app.py
```
The app will open automatically in your browser at `http://localhost:8501`.

---

## 🔬 How the Algorithm Works (6-Stage Pipeline)

```
[1. Ingestion & Freshness] ➡️ [2. Accounting Reconciliation] ➡️ [3. Anomaly & Deviation Scoring]
                                                                        ⬇️
[6. Governance & Actions] ⬅️ [5. Empirical Driver Tree]     ⬅️ [4. Lagged Causality Engine]
```

1. **Cross-Departmental Ingestion & Freshness Validation:** Ingests monthly telemetry across Finance, Operations, Marketing, and HR. Verifies pipeline latency (T+2 day cadence).
2. **Deterministic Accounting Reconciliation:** Validates accounting identities ($Revenue = \sum Products$, $Operating\ Income = Revenue - COGS - OpEx$, and Headcount continuity $HC_t = HC_{t-1} + Hires - Exits$).
3. **Statistical Anomaly & Deviation Scoring:** Computes rolling standard deviations ($\sigma$) and Z-scores ($Z = \frac{x - \mu}{\sigma}$). Assigns severity (CRITICAL, HIGH, MEDIUM, NORMAL).
4. **Lagged Cross-Correlation & Granger Causality:** Tests empirical lead times across lags $t-3$ to $t+3$ using Granger causality $F$-tests ($p < 0.05$) to establish predictive precedence (e.g. SRE Attrition leads SLA breaches by 1 month; SLA breaches lead Customer Churn by 2 months).
5. **Empirical Value Driver Tree & Sensitivity Mapping:** Fits multivariate regressions against Operating Margin ($R^2 = 0.74$) and Free Cash Flow ($R^2 = 0.68$) to quantify exact basis-point impacts per unit of operational change.
6. **Evidence-Backed Action Synthesis:** Translates computed anomalies into prioritized management recommendations with accountable owners, timeframes, statistical confidence, and financial ROI.

---

## 💡 Key Interactive Features

- **Executive KPI Cockpit:** High-contrast summary cards with variance indicators, target baselines, and active operational breach alerts.
- **Interactive Sunburst Value Tree:** Zoomable hierarchical breakdown of Microsoft enterprise value from top-line revenue down to engineering headcount and cluster utilization.
- **Lead-Lag Cross-Correlation Heatmap:** Visual matrix confirming the timing and statistical strength of causal transmissions.
- **Natural Language Executive Q&A:** Answers complex manager queries using real, local calculations:
  - *"Why did Operating Margin drop in Q3 despite Revenue growth?"*
  - *"How is Tech Talent Attrition impacting SLA Delivery and churn?"*
  - *"What happens to Free Cash Flow if Marketing Spend increases by 15%?"*
- **Real-Time Scenario Simulator:** Sliders for Cloud SLA, Churn, Attrition, and Infra unit costs that recalculate financial statements immediately.
- **Executive Brief Export:** Generates an actual downloadable `.md` brief ready for executive board packs.
- **Full Data Explorer:** Filterable data tables and one-click CSV downloads of the entire 36-month dataset and KPI Data Dictionary.

---

## 🛡️ Governance, Safety & Limitations

1. **Synthetic Data Disclosure:** All metrics are generated using a deterministic mathematical model with fixed seeds. No real Microsoft internal systems or customer data were accessed.
2. **Ethical Safeguard on HR Decisions:** Automated adverse HR actions (terminations, salary cuts) are strictly prohibited. The system surfaces aggregated capacity risks for human organizational review.
3. **Human-in-the-Loop Sign-Off:** High-impact recommendations (> $50M exposure) require mandatory manual sign-off by executive owners (CFO, CPO, EVP Cloud Ops).
4. **Statistical Boundaries:** Model observations are bounded to 36 monthly cycles; external macroeconomic regime changes may introduce non-linearities not captured by baseline regressions.
