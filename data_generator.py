"""
data_generator.py - Synthetic Enterprise KPI Data Generator for Microsoft (Illustrative Prototype)
Generates cross-departmental, internally consistent monthly operational and financial data.
All data is synthetic and generated for decision intelligence demonstration purposes only.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Metadata banner constant
SYNTHETIC_DATA_LABEL = "SYNTHETIC DEMO DATA — NOT REAL COMPANY DATA"

def get_kpi_dictionary():
    """
    Returns the comprehensive dictionary of all departmental KPIs,
    their mathematical definitions, owners, units, targets, and strategic roles.
    """
    kpis = [
        # Finance KPIs
        {
            "kpi_id": "FIN_REV",
            "name": "Total Consolidated Revenue",
            "department": "Finance",
            "owner": "Chief Financial Officer (CFO)",
            "unit": "$B",
            "target": 65.0,
            "target_direction": "higher",
            "formula": "Cloud Revenue + Productivity Revenue + Personal Computing Revenue",
            "strategic_role": "Top-line commercial scale and enterprise growth indicator",
            "freshness_cadence": "Monthly close (T+2 days)"
        },
        {
            "kpi_id": "FIN_CLOUD_REV",
            "name": "Intelligent Cloud Revenue",
            "department": "Finance",
            "owner": "EVP Cloud + AI",
            "unit": "$B",
            "target": 28.5,
            "target_direction": "higher",
            "formula": "Azure Consumption + Server Products + Enterprise Cloud Services",
            "strategic_role": "High-growth strategic engine driving platform scalability",
            "freshness_cadence": "Daily telemetry reconciled monthly"
        },
        {
            "kpi_id": "FIN_COGS",
            "name": "Cost of Goods Sold (COGS)",
            "department": "Finance",
            "owner": "VP Financial Planning & Analysis",
            "unit": "$B",
            "target": 20.0,
            "target_direction": "lower",
            "formula": "Data Center Operations + Cloud Infrastructure Compute Costs + Hardware Royalty",
            "strategic_role": "Direct variable cost of delivering cloud compute and digital products",
            "freshness_cadence": "Monthly close (T+3 days)"
        },
        {
            "kpi_id": "FIN_OP_MARGIN",
            "name": "Operating Margin",
            "department": "Finance",
            "owner": "Chief Financial Officer (CFO)",
            "unit": "%",
            "target": 45.0,
            "target_direction": "higher",
            "formula": "(Revenue - COGS - OpEx) / Revenue * 100",
            "strategic_role": "Core measure of operational efficiency and pricing power",
            "freshness_cadence": "Monthly close (T+2 days)"
        },
        {
            "kpi_id": "FIN_FCF",
            "name": "Free Cash Flow",
            "department": "Finance",
            "owner": "VP Treasury & Corporate Finance",
            "unit": "$B",
            "target": 22.0,
            "target_direction": "higher",
            "formula": "Operating Cash Flow - Capital Expenditures (CapEx)",
            "strategic_role": "Liquidity for strategic reinvestment, R&D, and shareholder return",
            "freshness_cadence": "Monthly close (T+4 days)"
        },
        {
            "kpi_id": "FIN_CAPEX",
            "name": "Cloud & AI Infrastructure CapEx",
            "department": "Finance",
            "owner": "VP Cloud Infrastructure & Procurement",
            "unit": "$B",
            "target": 12.0,
            "target_direction": "lower",
            "formula": "Data center land, servers, GPUs, network silicon buildout investments",
            "strategic_role": "Future capacity expansion determining operational throughput",
            "freshness_cadence": "Monthly close (T+3 days)"
        },

        # Operations & Engineering KPIs
        {
            "kpi_id": "OPS_SLA",
            "name": "Cloud Service Level Agreement (SLA) Delivery",
            "department": "Operations",
            "owner": "EVP Cloud Operations",
            "unit": "%",
            "target": 99.95,
            "target_direction": "higher",
            "formula": "(Available Cloud Cluster Minutes / Total Contracted Minutes) * 100",
            "strategic_role": "Primary driver of customer contract retention and contractual penalty avoidance",
            "freshness_cadence": "Continuous telemetry, aggregated monthly"
        },
        {
            "kpi_id": "OPS_CAPACITY_UTIL",
            "name": "Server Cluster Capacity Utilization",
            "department": "Operations",
            "owner": "VP Site Reliability Engineering (SRE)",
            "unit": "%",
            "target": 82.0,
            "target_direction": "range", # 78% - 85% is optimal
            "formula": "(Active Compute & Memory Load / Provisioned Data Center Capacity) * 100",
            "strategic_role": "Efficiency balance: >88% causes latency spikes, <75% wastes capital",
            "freshness_cadence": "Continuous telemetry"
        },
        {
            "kpi_id": "OPS_P99_LATENCY",
            "name": "P99 Cloud API Latency",
            "department": "Operations",
            "owner": "Director of Network Reliability",
            "unit": "ms",
            "target": 45.0,
            "target_direction": "lower",
            "formula": "99th percentile end-to-end response time across tier-1 API gateways",
            "strategic_role": "User experience benchmark for mission-critical enterprise workloads",
            "freshness_cadence": "Hourly aggregated"
        },
        {
            "kpi_id": "OPS_SUPPORT_MTTR",
            "name": "P1 Incident Mean Time to Resolution (MTTR)",
            "department": "Operations",
            "owner": "VP Global Customer Support & SRE",
            "unit": "hrs",
            "target": 2.0,
            "target_direction": "lower",
            "formula": "Sum(Resolved P1 Outage Duration) / Count(P1 Incidents)",
            "strategic_role": "Operational resiliency and crisis containment metric",
            "freshness_cadence": "Real-time incident ticketing"
        },
        {
            "kpi_id": "OPS_INFRA_UNIT_COST",
            "name": "Compute Unit Cost per Core-Hour",
            "department": "Operations",
            "owner": "VP Cloud Supply Chain",
            "unit": "$",
            "target": 0.042,
            "target_direction": "lower",
            "formula": "Total Data Center Energy + Depreciation / Delivered Core Hours",
            "strategic_role": "Underlying cost-to-serve foundation for cloud gross margins",
            "freshness_cadence": "Monthly"
        },

        # Marketing & Commercial KPIs
        {
            "kpi_id": "MKT_SPEND",
            "name": "Commercial Marketing & Campaign Spend",
            "department": "Marketing",
            "owner": "Chief Marketing Officer (CMO)",
            "unit": "$M",
            "target": 850.0,
            "target_direction": "range",
            "formula": "Enterprise Digital Campaigns + Global Partner Co-op + Industry Events",
            "strategic_role": "Demand generation engine feeding enterprise sales pipeline",
            "freshness_cadence": "Monthly"
        },
        {
            "kpi_id": "MKT_CAC",
            "name": "Blended Customer Acquisition Cost (CAC)",
            "department": "Marketing",
            "owner": "VP Commercial Go-to-Market",
            "unit": "$k",
            "target": 28.0,
            "target_direction": "lower",
            "formula": "Total Commercial S&M Spend / New Enterprise Logos Acquired",
            "strategic_role": "Capital efficiency of the enterprise customer acquisition pipeline",
            "freshness_cadence": "Monthly close"
        },
        {
            "kpi_id": "MKT_PIPELINE",
            "name": "Enterprise Deal Pipeline (Weighted)",
            "department": "Marketing",
            "owner": "Chief Commercial Officer (CCO)",
            "unit": "$B",
            "target": 38.0,
            "target_direction": "higher",
            "formula": "Sum(Opportunity Deal Value * Probability Stage Weight)",
            "strategic_role": "Leading forward indicator of enterprise contract bookings",
            "freshness_cadence": "Weekly CRM refresh"
        },
        {
            "kpi_id": "MKT_MQL",
            "name": "Enterprise Qualified Leads (MQL)",
            "department": "Marketing",
            "owner": "VP Global Growth Marketing",
            "unit": "k leads",
            "target": 45.0,
            "target_direction": "higher",
            "formula": "Count of scored high-propensity enterprise decision-maker leads",
            "strategic_role": "Direct output volume of marketing awareness and intent targeting",
            "freshness_cadence": "Weekly"
        },

        # Human Resources & Engineering Talent KPIs
        {
            "kpi_id": "HR_TECH_ATTRITION",
            "name": "Critical Tech Talent Attrition (Annualized)",
            "department": "Human Resources",
            "owner": "Chief People Officer (CPO)",
            "unit": "%",
            "target": 8.0,
            "target_direction": "lower",
            "formula": "(Annualized Voluntary Exits in Cloud/AI/SRE / Average Tech Headcount) * 100",
            "strategic_role": "Retention of mission-critical engineering and operational talent",
            "freshness_cadence": "Monthly close"
        },
        {
            "kpi_id": "HR_VACANCY_RATE",
            "name": "Critical Architecture Vacancy Rate",
            "department": "Human Resources",
            "owner": "VP Talent Acquisition",
            "unit": "%",
            "target": 4.5,
            "target_direction": "lower",
            "formula": "(Open Requisitions in Cloud Core Architecture / Total Allocated Roles) * 100",
            "strategic_role": "Capacity constraint indicator for engineering throughput and SRE coverage",
            "freshness_cadence": "Bi-weekly HRIS sync"
        },
        {
            "kpi_id": "HR_ENG_VELOCITY",
            "name": "Engineering Velocity Index",
            "department": "Human Resources",
            "owner": "VP Engineering Productivity",
            "unit": "score",
            "target": 85.0,
            "target_direction": "higher",
            "formula": "Normalized index of production deployments, commit frequency, and code review cycle",
            "strategic_role": "R&D innovation speed and bug remediation throughput",
            "freshness_cadence": "Monthly git telemetry"
        },
        {
            "kpi_id": "HR_ENPS",
            "name": "Employee Net Promoter Score (eNPS)",
            "department": "Human Resources",
            "owner": "Chief People Officer (CPO)",
            "unit": "pts",
            "target": 55.0,
            "target_direction": "higher",
            "formula": "% Promoters - % Detractors from internal organizational sentiment pulse",
            "strategic_role": "Workforce morale, culture health, and predictor of voluntary turnover",
            "freshness_cadence": "Quarterly pulse survey"
        },

        # Customer Success & Retention KPIs
        {
            "kpi_id": "CUST_CHURN",
            "name": "Enterprise Cloud Logo & Consumption Churn",
            "department": "Customer Success",
            "owner": "VP Customer Success",
            "unit": "%",
            "target": 0.95,
            "target_direction": "lower",
            "formula": "(Lost Monthly Recurring Revenue + Workload Downgrades / Starting ARR) * 100",
            "strategic_role": "Direct leakage from recurring revenue base",
            "freshness_cadence": "Monthly billing close"
        },
        {
            "kpi_id": "CUST_NRR",
            "name": "Net Retention Rate (NRR)",
            "department": "Customer Success",
            "owner": "Chief Commercial Officer (CCO)",
            "unit": "%",
            "target": 116.0,
            "target_direction": "higher",
            "formula": "(Starting ARR + Expansion - Contraction - Churn) / Starting ARR * 100",
            "strategic_role": "Compounds enterprise lifetime value and organic expansion velocity",
            "freshness_cadence": "Monthly"
        },
        {
            "kpi_id": "CUST_CSAT",
            "name": "Enterprise CSAT Score",
            "department": "Customer Success",
            "owner": "VP Enterprise Support",
            "unit": "/5.0",
            "target": 4.5,
            "target_direction": "higher",
            "formula": "Average rating from post-incident and post-deployment customer surveys",
            "strategic_role": "Leading indicator of contract renewal friction and account vulnerability",
            "freshness_cadence": "Weekly aggregation"
        }
    ]
    return pd.DataFrame(kpis)


def generate_synthetic_data(seed=42, n_months=36, shock_event=True, noise_level=1.0):
    """
    Generates internally consistent synthetic monthly data across 36 periods (Jan 2023 to Dec 2025).
    Incorporates real causal mechanics:
      - Months 18-22 contain an illustrative operational shock:
        A talent retention crunch (Tech Attrition spikes) leads to high vacancy in SRE.
        This degrades Cloud SLA delivery and support MTTR 1 month later.
        Customer churn spikes 2 months later, depressing NRR.
        Operating Margin drops due to SLA penalties and churn, despite top-line marketing spend.
    """
    np.random.seed(seed)
    
    # Dates: 36 months starting Jan 2023
    start_date = pd.Timestamp("2023-01-01")
    dates = [start_date + pd.DateOffset(months=i) for i in range(n_months)]
    periods = [d.strftime("%Y-%m") for d in dates]
    quarters = [f"{d.year}-Q{((d.month - 1) // 3) + 1}" for d in dates]
    
    # Base trend (linear mild enterprise growth)
    t = np.linspace(0, 1, n_months)
    
    # Department Headcount & HR drivers
    base_headcount = 215000 + (t * 12000)
    tech_headcount_base = 82000 + (t * 6000)
    
    # Baseline HR metrics
    tech_attrition = 7.8 + 1.2 * np.sin(t * 6) + np.random.normal(0, 0.4 * noise_level, n_months)
    vacancy_rate = 4.2 + 0.6 * np.cos(t * 5) + np.random.normal(0, 0.3 * noise_level, n_months)
    enps = 58.0 - (tech_attrition - 7.5) * 2.5 + np.random.normal(0, 1.5 * noise_level, n_months)
    eng_velocity = 86.0 - (vacancy_rate - 4.0) * 2.0 + np.random.normal(0, 1.0 * noise_level, n_months)
    
    # Introduce synthetic historical shock around months 18 to 23 (mid-2024)
    # Scenario: SRE talent attrition spike creates capacity shortage
    if shock_event:
        shock_window = (np.arange(n_months) >= 17) & (np.arange(n_months) <= 22)
        tech_attrition[shock_window] += np.array([2.5, 4.8, 5.5, 4.2, 3.0, 1.5])[:sum(shock_window)]
        vacancy_rate[shock_window] += np.array([1.8, 3.6, 4.2, 3.5, 2.2, 1.0])[:sum(shock_window)]
        enps[shock_window] -= np.array([8.0, 16.0, 19.0, 14.0, 9.0, 4.0])[:sum(shock_window)]
        eng_velocity[shock_window] -= np.array([5.0, 11.0, 14.0, 10.0, 6.0, 2.0])[:sum(shock_window)]

    # Clip HR bounds
    tech_attrition = np.clip(tech_attrition, 5.0, 16.0)
    vacancy_rate = np.clip(vacancy_rate, 2.5, 12.0)
    enps = np.clip(enps, 20.0, 75.0)
    eng_velocity = np.clip(eng_velocity, 60.0, 98.0)
    
    # Operations KPIs (lagged response to HR vacancy & velocity)
    # SLA depends on previous month vacancy and velocity
    sla_delivery = np.zeros(n_months)
    support_mttr = np.zeros(n_months)
    capacity_util = 81.0 + 3.0 * np.sin(t * 4) + np.random.normal(0, 1.0 * noise_level, n_months)
    p99_latency = np.zeros(n_months)
    infra_unit_cost = 0.040 + (t * 0.003) + np.random.normal(0, 0.0008 * noise_level, n_months)
    
    for i in range(n_months):
        lag_vac = vacancy_rate[max(0, i - 1)]
        lag_attr = tech_attrition[max(0, i - 1)]
        
        # When vacancy is high, MTTR increases and SLA degrades
        base_sla = 99.96 - (lag_vac - 4.2) * 0.06 - (lag_attr - 8.0) * 0.03
        sla_delivery[i] = base_sla + np.random.normal(0, 0.015 * noise_level)
        
        base_mttr = 1.9 + (lag_vac - 4.2) * 0.45 + np.random.normal(0, 0.15 * noise_level)
        support_mttr[i] = max(1.2, base_mttr)
        
        # Latency depends on capacity util and SLA state
        util_penalty = max(0, capacity_util[i] - 84.0) * 4.5
        p99_latency[i] = 43.0 + util_penalty + (2.0 - min(2.0, sla_delivery[i] - 98.0)) * 12.0 + np.random.normal(0, 2.0 * noise_level)
        
        # If capacity util gets too high, infra unit cost increases due to spot compute leasing
        if capacity_util[i] > 84.0:
            infra_unit_cost[i] += (capacity_util[i] - 84.0) * 0.0012

    sla_delivery = np.clip(sla_delivery, 99.40, 99.99)
    p99_latency = np.clip(p99_latency, 35.0, 120.0)
    
    # Marketing & Commercial KPIs
    mkt_spend_m = 780.0 + (t * 180.0) + 40.0 * np.cos(t * 8) + np.random.normal(0, 15.0 * noise_level, n_months)
    mql_count_k = (mkt_spend_m / 19.0) + np.random.normal(0, 1.5 * noise_level, n_months)
    cac_usd_k = (mkt_spend_m / (mql_count_k * 0.65)) + np.random.normal(0, 0.8 * noise_level, n_months)
    
    # Pipeline lags marketing spend by 1 month
    pipeline_b = np.zeros(n_months)
    for i in range(n_months):
        lag_spend = mkt_spend_m[max(0, i - 1)]
        pipeline_b[i] = 32.0 + (lag_spend - 780.0) * 0.035 + (t[i] * 8.0) + np.random.normal(0, 0.6 * noise_level)

    # Customer Success & Retention (Lags SLA by 1-2 months!)
    cloud_churn_pct = np.zeros(n_months)
    nrr_pct = np.zeros(n_months)
    csat_score = np.zeros(n_months)
    
    for i in range(n_months):
        lag_sla_1 = sla_delivery[max(0, i - 1)]
        lag_sla_2 = sla_delivery[max(0, i - 2)]
        avg_lag_sla = (lag_sla_1 + lag_sla_2) / 2.0
        
        # When SLA drops below 99.95%, churn escalates non-linearly
        sla_gap = max(0, 99.95 - avg_lag_sla)
        base_churn = 0.92 + (sla_gap * 3.8) + np.random.normal(0, 0.05 * noise_level)
        cloud_churn_pct[i] = np.clip(base_churn, 0.70, 3.20)
        
        # NRR is compressed by churn
        nrr_pct[i] = 117.5 - (cloud_churn_pct[i] - 0.92) * 4.2 + np.random.normal(0, 0.5 * noise_level)
        
        # CSAT is directly impacted by latency and MTTR
        csat_score[i] = 4.65 - (support_mttr[i] - 1.9) * 0.18 - (p99_latency[i] - 45.0) * 0.004 + np.random.normal(0, 0.05 * noise_level)
        csat_score[i] = np.clip(csat_score[i], 3.2, 4.95)

    # Finance KPIs (Mechanically calculated from drivers)
    # Intelligent Cloud Revenue driven by base + pipeline conversion (lag 2) - churn leakage
    cloud_rev_b = np.zeros(n_months)
    prod_rev_b = 18.0 + (t * 4.0) + np.random.normal(0, 0.3 * noise_level, n_months)
    personal_rev_b = 14.5 + (t * 1.5) + 0.8 * np.sin(t * 8) + np.random.normal(0, 0.4 * noise_level, n_months)
    
    for i in range(n_months):
        lag_pipe = pipeline_b[max(0, i - 2)]
        churn_drag = (cloud_churn_pct[i] - 0.95) * 1.4
        cloud_rev_b[i] = 23.5 + (lag_pipe - 32.0) * 0.38 + (t[i] * 9.5) - churn_drag + np.random.normal(0, 0.25 * noise_level)
    
    # Total Revenue Reconciliation
    total_rev_b = cloud_rev_b + prod_rev_b + personal_rev_b
    
    # COGS driven by Cloud Infra cost, capacity utilization, and SLA penalty rebates
    cogs_b = np.zeros(n_months)
    for i in range(n_months):
        sla_penalty = max(0, 99.95 - sla_delivery[i]) * 4.0 # contractual credits to enterprise tenants
        infra_component = cloud_rev_b[i] * (0.28 + (infra_unit_cost[i] - 0.040) * 3.0)
        base_cogs = 17.5 + (t[i] * 3.8) + infra_component + sla_penalty + np.random.normal(0, 0.2 * noise_level)
        cogs_b[i] = base_cogs

    gross_profit_b = total_rev_b - cogs_b
    gross_margin_pct = (gross_profit_b / total_rev_b) * 100.0
    
    # OpEx (R&D + SG&A)
    # Marketing spend contributes directly to SG&A ($M to $B)
    opex_b = 14.0 + (t * 2.5) + (mkt_spend_m / 1000.0) * 0.85 + (tech_attrition - 7.5) * 0.08 + np.random.normal(0, 0.15 * noise_level, n_months)
    
    # Operating Income & Margin
    operating_income_b = gross_profit_b - opex_b
    operating_margin_pct = (operating_income_b / total_rev_b) * 100.0
    
    # CapEx & Free Cash Flow
    capex_b = 9.5 + (t * 4.5) + (capacity_util - 80.0) * 0.12 + np.random.normal(0, 0.3 * noise_level, n_months)
    fcf_b = (operating_income_b * 0.82) + (capex_b * 0.35) - capex_b + np.random.normal(0, 0.4 * noise_level, n_months)

    # Human Headcount flow reconciliation
    # Headcount_t = Headcount_{t-1} + Hires - Voluntary departures
    headcount = np.zeros(n_months, dtype=int)
    hires = np.zeros(n_months, dtype=int)
    departures = np.zeros(n_months, dtype=int)
    headcount[0] = int(base_headcount[0])
    
    for i in range(n_months):
        dep_rate = (tech_attrition[i] / 12.0) / 100.0
        departures[i] = int(headcount[max(0, i-1)] * dep_rate)
        target_hc = int(base_headcount[i])
        needed_hires = max(100, target_hc - headcount[max(0, i-1)] + departures[i])
        hires[i] = needed_hires + int(np.random.normal(0, 50))
        if i > 0:
            headcount[i] = headcount[i-1] + hires[i] - departures[i]

    # Build DataFrame
    df = pd.DataFrame({
        "period": periods,
        "date": dates,
        "quarter": quarters,
        
        # Finance
        "revenue_b": np.round(total_rev_b, 2),
        "cloud_revenue_b": np.round(cloud_rev_b, 2),
        "productivity_revenue_b": np.round(prod_rev_b, 2),
        "personal_computing_revenue_b": np.round(personal_rev_b, 2),
        "cogs_b": np.round(cogs_b, 2),
        "gross_profit_b": np.round(gross_profit_b, 2),
        "gross_margin_pct": np.round(gross_margin_pct, 2),
        "opex_b": np.round(opex_b, 2),
        "operating_income_b": np.round(operating_income_b, 2),
        "operating_margin_pct": np.round(operating_margin_pct, 2),
        "free_cash_flow_b": np.round(fcf_b, 2),
        "capex_b": np.round(capex_b, 2),
        
        # Operations
        "sla_delivery_pct": np.round(sla_delivery, 3),
        "server_capacity_util_pct": np.round(capacity_util, 1),
        "p99_latency_ms": np.round(p99_latency, 1),
        "support_resolution_time_hrs": np.round(support_mttr, 2),
        "infra_cost_per_compute_hr_usd": np.round(infra_unit_cost, 4),
        
        # Marketing
        "marketing_spend_m": np.round(mkt_spend_m, 1),
        "cac_usd_k": np.round(cac_usd_k, 2),
        "enterprise_pipeline_b": np.round(pipeline_b, 2),
        "mql_count_k": np.round(mql_count_k, 1),
        
        # HR
        "total_headcount": headcount,
        "hires_count": hires,
        "departures_count": departures,
        "tech_attrition_pct": np.round(tech_attrition, 2),
        "critical_role_vacancy_pct": np.round(vacancy_rate, 2),
        "engineer_productivity_score": np.round(eng_velocity, 1),
        "enps_score": np.round(enps, 1),
        
        # Customer Success
        "cloud_churn_pct": np.round(cloud_churn_pct, 2),
        "nrr_pct": np.round(nrr_pct, 1),
        "csat_score": np.round(csat_score, 2),
        
        # Metadata / Lineage
        "is_synthetic": True,
        "data_freshness_status": ["Fresh" if i >= n_months - 2 else "Archived" for i in range(n_months)],
        "pipeline_latency_hours": [4.2 + (i % 3) * 1.1 for i in range(n_months)]
    })
    
    return df
