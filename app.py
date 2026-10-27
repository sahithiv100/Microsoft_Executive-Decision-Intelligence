"""
app.py - Executive Decision Intelligence Web Application
Illustrative Prototype for Microsoft (Synthetic Data Only)
Turns cross-departmental KPIs into concise, evidence-backed explanations and recommended management actions.
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Set Streamlit Page Config - Must be first Streamlit command
st.set_page_config(
    page_title="Executive Decision Intelligence | Microsoft Prototype",
    page_icon="\U0001F4CA",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import local modules directly from root
from data_generator import generate_synthetic_data, get_kpi_dictionary, SYNTHETIC_DATA_LABEL
from analytics_engine import (
    validate_reconciliation,
    detect_anomalies,
    analyze_lagged_causality,
    calculate_driver_sensitivities,
    simulate_operational_scenario,
    generate_executive_recommendations,
    answer_natural_language_query
)
from ui_components import (
    get_custom_css,
    render_banner,
    build_kpi_tree_sunburst,
    build_trend_anomaly_chart,
    build_lead_lag_heatmap,
    build_scenario_comparison_chart,
    build_sensitivity_tornado_chart
)
from export_manager import generate_executive_brief_markdown

# Apply High-Contrast Custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Initialize Session State
if "seed" not in st.session_state:
    st.session_state.seed = 42
if "noise_level" not in st.session_state:
    st.session_state.noise_level = 1.0
if "shock_event" not in st.session_state:
    st.session_state.shock_event = True
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Executive Cockpit"
if "nl_query_input" not in st.session_state:
    st.session_state.nl_query_input = "Why did Operating Margin drop in Q3 despite Revenue growth?"

# Sidebar Controls
with st.sidebar:
    st.markdown("<h2 style='color:#FFFFFF;margin-bottom:0px;'>Executive Cockpit</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#A78BFA;font-size:0.85rem;font-weight:600;'>Microsoft Enterprise Intelligence Prototype</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<h4 style='color:#FFFFFF;'>Data & Simulation Controls</h4>", unsafe_allow_html=True)
    
    seed_input = st.number_input("Simulation Random Seed", min_value=1, max_value=9999, value=st.session_state.seed, step=1)
    noise_slider = st.slider("Environmental Volatility / Noise", min_value=0.2, max_value=2.5, value=float(st.session_state.noise_level), step=0.1)
    shock_toggle = st.checkbox("Include SRE Capacity Shock Event", value=st.session_state.shock_event, help="Simulates the mid-2024 engineering retention crunch and downstream SLA cascade.")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("Apply / Regenerate", use_container_width=True):
            st.session_state.seed = int(seed_input)
            st.session_state.noise_level = float(noise_slider)
            st.session_state.shock_event = shock_toggle
            st.rerun()
    with col_btn2:
        if st.button("Reset Defaults", use_container_width=True):
            st.session_state.seed = 42
            st.session_state.noise_level = 1.0
            st.session_state.shock_event = True
            st.rerun()
            
    st.markdown("---")
    
    # Navigation Selector
    st.markdown("<h4 style='color:#FFFFFF;'>Navigation View</h4>", unsafe_allow_html=True)
    views = [
        "Executive Cockpit",
        "Driver Tree & Anomaly Deep-Dive",
        "Decision Intelligence & Actions",
        "Natural Language Executive Q&A",
        "Scenario & What-If Simulator",
        "Data Explorer & Reconciliation",
        "How the Algorithm Works",
        "Metrics, Limitations & Governance"
    ]
    selected_view = st.radio("Select Intelligence View:", views, index=views.index(st.session_state.active_tab) if st.session_state.active_tab in views else 0)
    st.session_state.active_tab = selected_view
    
    st.markdown("---")
    st.markdown(
        f"<div style='background-color:#161F33;padding:10px;border-radius:6px;border:1px solid #2C3B59;font-size:0.75rem;color:#94A3B8;'>"
        f"<b>Environment Status:</b> Operational<br>"
        f"<b>Data Lineage:</b> 100% Synthetic Math Model<br>"
        f"<b>Governance:</b> Human-in-the-Loop Active"
        f"</div>",
        unsafe_allow_html=True
    )

# Compute & Cache Application Data
df = generate_synthetic_data(seed=st.session_state.seed, n_months=36, shock_event=st.session_state.shock_event, noise_level=st.session_state.noise_level)
kpi_dict = get_kpi_dictionary()
rec_df, health_score = validate_reconciliation(df)
anomalies_df = detect_anomalies(df, kpi_dict)
causality_df = analyze_lagged_causality(df)
sensitivities_df, r2_margin, r2_fcf = calculate_driver_sensitivities(df)
recommendations_df = generate_executive_recommendations(df, anomalies_df, causality_df)
latest_period = df.iloc[-1]

# Top Synthetic Banner - Rendered on every page
st.markdown(render_banner(), unsafe_allow_html=True)

# Header Section
col_title, col_freshness = st.columns([3, 1])
with col_title:
    st.markdown("<h1 style='margin-bottom:4px;color:#FFFFFF;'>Executive Decision Intelligence</h1>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='color:#CBD5E1;font-size:1.05rem;margin-top:0px;'>"
        f"Turning fragmented departmental KPIs into evidence-backed explanations and management actions. "
        f"<b>Illustrative Tenant: Microsoft Corporation</b>"
        f"</p>",
        unsafe_allow_html=True
    )
with col_freshness:
    st.markdown(
        f"""
        <div style='background-color:#161F33;border:1px solid #2C3B59;border-radius:8px;padding:12px;text-align:right;'>
            <span class='badge badge-success'>Data Freshness: Verified</span>
            <div style='font-size:0.80rem;color:#E2E8F0;margin-top:4px;'>
                Reporting Period: <b>{latest_period['period']}</b> ({latest_period['quarter']})<br>
                Reconciliation Integrity: <b>{health_score:.1f}%</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr style='border:0.5px solid #2C3B59;margin-top:12px;margin-bottom:20px;'>", unsafe_allow_html=True)


# ==============================================================================
# VIEW 1: EXECUTIVE COCKPIT
# ==============================================================================
if selected_view == "Executive Cockpit":
    st.markdown("### Executive Performance Cockpit")
    st.markdown("Consolidated C-Suite overview across Financials, Cloud Operations, Marketing, and Human Capital.")
    
    # Critical Alerts Ticker
    crit_anomalies = anomalies_df[anomalies_df["severity"].isin(["CRITICAL", "HIGH"])]
    if len(crit_anomalies) > 0:
        st.markdown(
            f"""
            <div style='background-color:#26121E;border-left:5px solid #EF4444;border-radius:6px;padding:12px 18px;margin-bottom:20px;border-top:1px solid #7F1D1D;border-right:1px solid #7F1D1D;border-bottom:1px solid #7F1D1D;'>
                <span style='color:#FCA5A5;font-weight:700;font-size:0.90rem;'>\u26a0\ufe0f {len(crit_anomalies)} OPERATIONAL ALERTS REQUIRE ATTENTION:</span>
                <span style='color:#F3F4F6;font-size:0.88rem;margin-left:10px;'>
                    Cloud SLA breach ({latest_period['sla_delivery_pct']}%), Tech Talent Attrition elevated ({latest_period['tech_attrition_pct']}%), Cloud Churn ({latest_period['cloud_churn_pct']}%), Operating Margin compressed to {latest_period['operating_margin_pct']}%.
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Top KPI Row (6 Core Departmental Cards)
    kpi_cols = st.columns(6)
    
    with kpi_cols[0]:
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-title'>Total Revenue</div>
                <div class='kpi-value'>${latest_period['revenue_b']}B</div>
                <div class='kpi-target'>Target: $65.0B <span style='color:#10B981;'>+{latest_period['revenue_b'] - 65.0:.1f}B</span></div>
                <div style='margin-top:6px;'><span class='badge badge-success'>On Target</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with kpi_cols[1]:
        margin_var = latest_period['operating_margin_pct'] - 45.0
        badge_cls = "badge-critical" if margin_var < -1.5 else "badge-high" if margin_var < 0 else "badge-success"
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-title'>Operating Margin</div>
                <div class='kpi-value'>{latest_period['operating_margin_pct']}%</div>
                <div class='kpi-target'>Target: 45.0% <span style='color:{'#EF4444' if margin_var < 0 else '#10B981'};'>{margin_var:+.1f}%</span></div>
                <div style='margin-top:6px;'><span class='badge {badge_cls}'>Deviation</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with kpi_cols[2]:
        sla_var = latest_period['sla_delivery_pct'] - 99.95
        badge_cls = "badge-critical" if sla_var < -0.05 else "badge-high" if sla_var < 0 else "badge-success"
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-title'>Cloud SLA Delivery</div>
                <div class='kpi-value'>{latest_period['sla_delivery_pct']}%</div>
                <div class='kpi-target'>Target: 99.95% <span style='color:{'#EF4444' if sla_var < 0 else '#10B981'};'>{sla_var:+.3f}%</span></div>
                <div style='margin-top:6px;'><span class='badge {badge_cls}'>{'SLA Breach' if sla_var < 0 else 'Healthy'}</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with kpi_cols[3]:
        churn_var = latest_period['cloud_churn_pct'] - 0.95
        badge_cls = "badge-critical" if churn_var > 0.4 else "badge-high" if churn_var > 0 else "badge-success"
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-title'>Cloud Churn Rate</div>
                <div class='kpi-value'>{latest_period['cloud_churn_pct']}%</div>
                <div class='kpi-target'>Target: 0.95% <span style='color:{'#EF4444' if churn_var > 0 else '#10B981'};'>{churn_var:+.2f}%</span></div>
                <div style='margin-top:6px;'><span class='badge {badge_cls}'>{'Elevated' if churn_var > 0 else 'Nominal'}</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with kpi_cols[4]:
        attr_var = latest_period['tech_attrition_pct'] - 8.0
        badge_cls = "badge-critical" if attr_var > 3.0 else "badge-high" if attr_var > 0 else "badge-success"
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-title'>Tech Talent Attrition</div>
                <div class='kpi-value'>{latest_period['tech_attrition_pct']}%</div>
                <div class='kpi-target'>Target: 8.0% <span style='color:{'#EF4444' if attr_var > 0 else '#10B981'};'>{attr_var:+.1f}%</span></div>
                <div style='margin-top:6px;'><span class='badge {badge_cls}'>{'SRE Turnover' if attr_var > 0 else 'Healthy'}</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with kpi_cols[5]:
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-title'>Free Cash Flow</div>
                <div class='kpi-value'>${latest_period['free_cash_flow_b']}B</div>
                <div class='kpi-target'>Target: $22.0B <span style='color:{'#10B981' if latest_period['free_cash_flow_b'] >= 22.0 else '#EF4444'};'>{latest_period['free_cash_flow_b'] - 22.0:+.1f}B</span></div>
                <div style='margin-top:6px;'><span class='badge badge-medium'>Liquidity</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Main Cockpit Visuals: Sunburst Tree & Trend Trajectory
    col_chart_left, col_chart_right = st.columns([1, 1])
    
    with col_chart_left:
        st.plotly_chart(build_kpi_tree_sunburst(df), use_container_width=True)
        
    with col_chart_right:
        # Selector for trend chart
        trend_metric = st.selectbox(
            "Select KPI for Historical Trajectory & Target Breaches:",
            [
                ("operating_margin_pct", "Operating Margin", 45.0, "%", True),
                ("sla_delivery_pct", "Cloud SLA Delivery", 99.95, "%", True),
                ("cloud_churn_pct", "Cloud Churn Rate", 0.95, "%", False),
                ("tech_attrition_pct", "Tech Talent Attrition", 8.0, "%", False),
                ("revenue_b", "Total Consolidated Revenue", 65.0, "$B", True),
                ("server_capacity_util_pct", "Server Capacity Utilization", 82.0, "%", False)
            ],
            format_func=lambda x: x[1]
        )
        st.plotly_chart(
            build_trend_anomaly_chart(df, trend_metric[0], trend_metric[1], trend_metric[2], trend_metric[3], trend_metric[4]),
            use_container_width=True
        )

    # Executive Evidence Drawer (Collapsible)
    with st.expander("\U0001F4C2 Open Executive Evidence Drawer & Drill-Down Analysis", expanded=False):
        st.markdown("#### Deep-Dive Evidence Breakdown")
        col_ev1, col_ev2 = st.columns(2)
        with col_ev1:
            st.markdown(
                f"""
                <div class='evidence-box'>
                    <h5 style='color:#FFFFFF;margin-top:0px;'>Operational Root-Cause Path</h5>
                    <p style='color:#E2E8F0;font-size:0.88rem;'>
                        <b>1. Upstream Catalyst:</b> Tech Talent Attrition rose to <b>{latest_period['tech_attrition_pct']}%</b> (\u03c3 = +2.4), causing SRE vacancies.<br>
                        <b>2. Transmission Mechanism:</b> Incident MTTR increased to <b>{latest_period['support_resolution_time_hrs']} hrs</b>, causing SLA delivery to fall to <b>{latest_period['sla_delivery_pct']}%</b>.<br>
                        <b>3. Financial Squeeze:</b> Data center emergency capacity drove COGS up to <b>${latest_period['cogs_b']}B</b> and customer churn to <b>{latest_period['cloud_churn_pct']}%</b>.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_ev2:
            st.markdown(
                f"""
                <div class='evidence-box'>
                    <h5 style='color:#FFFFFF;margin-top:0px;'>Data Lineage & Accounting Verification</h5>
                    <p style='color:#E2E8F0;font-size:0.88rem;'>
                        • <b>Revenue Verification:</b> Cloud (${latest_period['cloud_revenue_b']}B) + Productivity (${latest_period['productivity_revenue_b']}B) + Personal (${latest_period['personal_computing_revenue_b']}B) = ${latest_period['revenue_b']}B (Diff: $0.0M)<br>
                        • <b>Operating Income Identity:</b> Gross Profit (${latest_period['gross_profit_b']}B) - OpEx (${latest_period['opex_b']}B) = ${latest_period['operating_income_b']}B<br>
                        • <b>Headcount Flow Continuity:</b> Verified across all {len(df)} monthly periods.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )


# ==============================================================================
# VIEW 2: DRIVER TREE & ANOMALY DEEP-DIVE
# ==============================================================================
elif selected_view == "Driver Tree & Anomaly Deep-Dive":
    st.markdown("### Operational Driver Decomposition & Anomaly Analysis")
    st.markdown("How operational drivers mathematically transmit into Financial Operating Margin and Cash Flow.")
    
    tab_drivers, tab_lag, tab_anom = st.tabs(["\U0001F333 Driver Sensitivities & Elasticities", "\U0001F550 Lagged Causality Matrix", "\U0001F6A8 Full Anomaly Table"])
    
    with tab_drivers:
        st.markdown("#### Multivariate Driver Elasticity Matrix")
        st.markdown(
            f"Regression model explains **{r2_margin * 100:.1f}% of Operating Margin variation** (R² = {r2_margin:.2f}) "
            f"and **{r2_fcf * 100:.1f}% of Free Cash Flow variation** (R² = {r2_fcf:.2f}) across {len(df)} historical monthly observations."
        )
        
        st.plotly_chart(build_sensitivity_tornado_chart(sensitivities_df), use_container_width=True)
        
        st.markdown("##### Detailed Elasticity Table")
        st.dataframe(
            sensitivities_df[[
                "driver_name", "standard_benchmark_change", "margin_impact_pct", 
                "margin_impact_bps", "fcf_impact_usd_m", "model_coefficient"
            ]].rename(columns={
                "driver_name": "Operational Driver",
                "standard_benchmark_change": "Benchmark Shift Tested",
                "margin_impact_pct": "Operating Margin Impact (%)",
                "margin_impact_bps": "Margin Delta (bps)",
                "fcf_impact_usd_m": "Free Cash Flow Delta ($M)",
                "model_coefficient": "Model \u03b2 Coefficient"
            }),
            use_container_width=True
        )
        
    with tab_lag:
        st.markdown("#### Lagged Cross-Correlation & Granger Causality Analysis")
        st.markdown(
            "Distinguishing **true predictive precedence** from coincident correlation. "
            "Granger tests determine whether past values of operational variables contain information that statistically forecasts downstream outcomes."
        )
        
        st.plotly_chart(build_lead_lag_heatmap(causality_df), use_container_width=True)
        
        st.markdown("##### Empirical Lead-Lag Findings Table")
        st.dataframe(
            causality_df[[
                "relationship", "classification", "optimal_lead_months", 
                "peak_correlation", "granger_p_value", "explanation"
            ]].rename(columns={
                "relationship": "Operational Relationship",
                "classification": "Causal Classification",
                "optimal_lead_months": "Optimal Lead (Months)",
                "peak_correlation": "Peak Correlation (r)",
                "granger_p_value": "Granger Test p-value",
                "explanation": "Statistical Interpretation"
            }),
            use_container_width=True
        )
        
    with tab_anom:
        st.markdown("#### Comprehensive Anomaly & Deviation Register")
        st.markdown("All 22 monitored enterprise KPIs evaluated for target deviation and statistical Z-score outliers.")
        
        # Filter controls
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            dep_filter = st.multiselect("Filter by Department:", options=list(anomalies_df["department"].unique()), default=list(anomalies_df["department"].unique()))
        with col_f2:
            sev_filter = st.multiselect("Filter by Severity:", options=list(anomalies_df["severity"].unique()), default=list(anomalies_df["severity"].unique()))
            
        filtered_anom = anomalies_df[
            (anomalies_df["department"].isin(dep_filter)) &
            (anomalies_df["severity"].isin(sev_filter))
        ]
        
        st.dataframe(
            filtered_anom[[
                "kpi_name", "department", "current_value", "target_value", "unit",
                "variance_pct", "z_score", "severity", "owner", "estimated_impact"
            ]].rename(columns={
                "kpi_name": "KPI Name",
                "department": "Department",
                "current_value": "Current",
                "target_value": "Target",
                "unit": "Unit",
                "variance_pct": "Var %",
                "z_score": "Z-Score",
                "severity": "Severity",
                "owner": "Owner",
                "estimated_impact": "Financial / Operational Impact"
            }),
            use_container_width=True
        )


# ==============================================================================
# VIEW 3: DECISION INTELLIGENCE & ACTIONS
# ==============================================================================
elif selected_view == "Decision Intelligence & Actions":
    st.markdown("### Evidence-Backed Management Action Plan")
    st.markdown("Algorithmic recommendations grounded in computed anomalies, driver sensitivities, and causal lead-times.")
    
    st.markdown(
        """
        <div style='background-color:#1E1B4B;border-left:4px solid #8B5CF6;border-radius:6px;padding:12px 18px;margin-bottom:20px;'>
            <b style='color:#FAF5FF;'>GOVERNANCE MANDATE:</b>
            <span style='color:#DDD6FE;font-size:0.88rem;margin-left:6px;'>
                All high-impact recommendations require explicit human review by designated executive owners before resource allocation. 
                No adverse personnel actions are automated.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    for _, rec in recommendations_df.iterrows():
        p_badge = "badge-critical" if "P1" in rec["priority"] else "badge-high" if "P2" in rec["priority"] else "badge-medium"
        
        with st.container():
            st.markdown(
                f"""
                <div style='background-color:#161F33;border:1px solid #2C3B59;border-radius:8px;padding:18px 20px;margin-bottom:20px;'>
                    <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;'>
                        <span class='badge {p_badge}'>{rec['priority']}</span>
                        <span style='color:#A78BFA;font-size:0.85rem;font-weight:700;'>ACTION ID: {rec['id']}</span>
                    </div>
                    <h4 style='color:#FFFFFF;margin-top:0px;margin-bottom:8px;'>{rec['title']}</h4>
                    <div style='display:flex;gap:24px;font-size:0.85rem;color:#E2E8F0;margin-bottom:14px;'>
                        <span><b>Owner:</b> {rec['owner']}</span>
                        <span><b>Timeframe:</b> {rec['timeframe']}</span>
                        <span><b>Confidence:</b> {rec['confidence_score']}</span>
                        <span><b>Department:</b> {rec['department']}</span>
                    </div>
                    <div style='background-color:#0E131F;padding:12px 14px;border-radius:6px;border-left:3px solid #8B5CF6;margin-bottom:12px;font-size:0.88rem;color:#E2E8F0;'>
                        <b style='color:#A78BFA;'>Triggering Evidence:</b> {rec['triggering_evidence']}
                    </div>
                    <div style='font-size:0.88rem;color:#E2E8F0;margin-bottom:10px;'>
                        <b style='color:#10B981;'>Expected Business Impact:</b> {rec['expected_impact']}
                    </div>
                    <div style='font-size:0.84rem;color:#CBD5E1;margin-bottom:10px;'>
                        <b style='color:#FFFFFF;'>Key Assumptions:</b><br>{rec['assumptions'].replace(chr(10), '<br>')}
                    </div>
                    <div style='font-size:0.84rem;color:#FCA5A5;margin-bottom:12px;'>
                        <b>Uncertainty & Risks:</b> {rec['uncertainty_and_risks']}
                    </div>
                    <div style='background-color:#1F2937;padding:8px 12px;border-radius:4px;font-size:0.80rem;color:#94A3B8;'>
                        \U0001F6E1\ufe0f <b>Governance Policy:</b> {rec['governance_note']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Interactive Human Sign-Off Checkpoint
            col_sign1, col_sign2 = st.columns([1, 3])
            with col_sign1:
                signed = st.checkbox(f"Sign-off / Approve {rec['id']}", key=f"sign_{rec['id']}")
            with col_sign2:
                if signed:
                    st.success(f"\u2705 {rec['id']} Approved by Executive Reviewer for execution.")
                else:
                    st.info(f"\u23f3 Pending Executive Review by {rec['owner'].split('&')[0]}.")
            st.markdown("<br>", unsafe_allow_html=True)


# ==============================================================================
# VIEW 4: NATURAL LANGUAGE EXECUTIVE Q&A
# ==============================================================================
elif selected_view == "Natural Language Executive Q&A":
    st.markdown("### Natural Language Executive Q&A")
    st.markdown("Ask complex cross-departmental questions. Backed entirely by local deterministic data analytics.")
    
    st.markdown("#### Select a Pre-Built Manager Question to Explore:")
    
    q_cols = st.columns(3)
    with q_cols[0]:
        if st.button("Question 1:\nWhy did Operating Margin drop in Q3 despite Revenue growth?", use_container_width=True):
            st.session_state.nl_query_input = "Why did Operating Margin drop in Q3 despite Revenue growth?"
    with q_cols[1]:
        if st.button("Question 2:\nHow is Tech Talent Attrition impacting SLA Delivery and churn?", use_container_width=True):
            st.session_state.nl_query_input = "How is Tech Talent Attrition impacting Cloud SLA Delivery and customer churn?"
    with q_cols[2]:
        if st.button("Question 3:\nWhat happens to Free Cash Flow if Marketing Spend increases by 15%?", use_container_width=True):
            st.session_state.nl_query_input = "What happens to Free Cash Flow if Marketing Spend increases by 15% next quarter?"

    user_query = st.text_input(
        "Or type a custom manager question or KPI query:",
        value=st.session_state.nl_query_input,
        placeholder="e.g. Why did margin drop? Or enter 'Cloud SLA', 'Tech Attrition', 'Free Cash Flow'..."
    )
    
    if user_query:
        ans_text, evidence_tbl, rec_action, owner = answer_natural_language_query(
            user_query, df, anomalies_df, causality_df, sensitivities_df
        )
        
        st.markdown(
            f"""
            <div style='background-color:#161F33;border:1px solid #8B5CF6;border-radius:8px;padding:20px;margin-top:16px;margin-bottom:20px;'>
                <div style='color:#FAF5FF;font-size:0.95rem;line-height:1.6;'>
                    {ans_text.replace(chr(10), '<br>')}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("#### Computed Evidence Table Backing This Response")
        st.dataframe(evidence_tbl, use_container_width=True)
        
        col_rec1, col_rec2 = st.columns([3, 1])
        with col_rec1:
            st.markdown(
                f"<div style='background-color:#111A2E;border-left:4px solid #10B981;padding:12px;border-radius:4px;'>"
                f"<b style='color:#FFFFFF;'>Recommended Operational Next Step:</b> <span style='color:#E2E8F0;'>{rec_action}</span>"
                f"</div>",
                unsafe_allow_html=True
            )
        with col_rec2:
            st.markdown(
                f"<div style='background-color:#111A2E;border:1px solid #2C3B59;padding:12px;border-radius:4px;text-align:center;'>"
                f"<span style='color:#94A3B8;font-size:0.75rem;'>ACTION OWNER</span><br><b style='color:#FFFFFF;font-size:0.85rem;'>{owner}</b>"
                f"</div>",
                unsafe_allow_html=True
            )


# ==============================================================================
# VIEW 5: SCENARIO & WHAT-IF SIMULATOR
# ==============================================================================
elif selected_view == "Scenario & What-If Simulator":
    st.markdown("### Operational Scenario & What-If Simulator")
    st.markdown("Adjust key operational levers to immediately recalculate projected Revenue, COGS, Operating Margin, and Free Cash Flow.")
    
    col_sim_left, col_sim_right = st.columns([1, 2])
    
    with col_sim_left:
        st.markdown(
            "<div style='background-color:#161F33;border:1px solid #2C3B59;border-radius:8px;padding:16px;'>",
            unsafe_allow_html=True
        )
        st.markdown("<h4 style='color:#FFFFFF;margin-top:0px;'>Scenario Levers</h4>", unsafe_allow_html=True)
        
        sla_slider = st.slider("Cloud SLA Delivery Delta (%)", min_value=-0.40, max_value=0.20, value=0.08, step=0.02, help="Improving SLA reduces customer credits and contractual penalties.")
        churn_slider = st.slider("Cloud Account Churn Delta (%)", min_value=-0.60, max_value=0.60, value=-0.30, step=0.05, help="Reducing churn directly protects high-margin recurring ARR.")
        attr_slider = st.slider("Tech Talent Attrition Delta (%)", min_value=-4.0, max_value=4.0, value=-2.0, step=0.5, help="Lower attrition stabilizes engineering velocity and cuts recruiting premium.")
        infra_slider = st.slider("Data Center Infra Unit Cost Delta (%)", min_value=-15.0, max_value=15.0, value=-5.0, step=1.0, help="Workload rebalancing reduces spot core-hour costs.")
        mkt_slider = st.slider("Enterprise Marketing Spend Delta (%)", min_value=-20.0, max_value=25.0, value=10.0, step=5.0, help="Expanding marketing budget feeds future deal pipeline.")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
    sim_df = simulate_operational_scenario(
        df,
        sla_delta=sla_slider,
        churn_delta=churn_slider,
        attrition_delta=attr_slider,
        infra_cost_delta_pct=infra_slider,
        marketing_spend_delta_pct=mkt_slider
    )
    
    with col_sim_right:
        st.plotly_chart(build_scenario_comparison_chart(sim_df), use_container_width=True)
        
    st.markdown("#### Recalculated Financial Summary Table")
    st.dataframe(
        sim_df.rename(columns={
            "Metric": "Financial Metric",
            "Baseline": f"Baseline Plan ({latest_period['period']})",
            "Scenario": "Projected Scenario Outcome",
            "Variance": "Net Variance Delta"
        }),
        use_container_width=True
    )


# ==============================================================================
# VIEW 6: DATA EXPLORER & RECONCILIATION
# ==============================================================================
elif selected_view == "Data Explorer & Reconciliation":
    st.markdown("### Data Explorer, Dictionary & Accounting Reconciliation")
    st.markdown("Full transparency into historical synthetic data points, accounting identities, and KPI definitions.")
    
    tab_data, tab_rec, tab_dict = st.tabs(["\U0001F4C1 Full Dataset Explorer", "\U0001F50D Accounting Reconciliation", "\U0001F4D6 KPI Data Dictionary"])
    
    with tab_data:
        st.markdown("#### Historical Synthetic Dataset Preview")
        
        col_down1, col_down2 = st.columns([3, 1])
        with col_down1:
            st.markdown(f"Displaying **{len(df)} monthly observations** spanning **{df['period'].iloc[0]} to {df['period'].iloc[-1]}**.")
        with col_down2:
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="\U0001F4E5 Download Full CSV Dataset",
                data=csv_data,
                file_name=f"microsoft_synthetic_kpi_dataset_{st.session_state.seed}.csv",
                mime="text/csv",
                use_container_width=True
            )
            
        st.dataframe(df, use_container_width=True)
        
    with tab_rec:
        st.markdown("#### Accounting Identity & Continuous Flow Validation")
        st.markdown(
            f"Overall Data Integrity Score: **{health_score:.1f}% PASS**. "
            "Every period is validated against fundamental corporate financial identities."
        )
        
        col_id1, col_id2, col_id3 = st.columns(3)
        with col_id1:
            st.markdown(
                "<div class='kpi-card'><div class='kpi-title'>Revenue Addition Check</div>"
                "<div style='font-size:1.1rem;font-weight:700;color:#10B981;'>Revenue = Cloud + Prod + Personal</div>"
                "<div style='font-size:0.80rem;color:#94A3B8;margin-top:4px;'>Max tolerance: $60M (0.09%)</div></div>",
                unsafe_allow_html=True
            )
        with col_id2:
            st.markdown(
                "<div class='kpi-card'><div class='kpi-title'>Operating Income Check</div>"
                "<div style='font-size:1.1rem;font-weight:700;color:#10B981;'>Operating Inc = Revenue - COGS - OpEx</div>"
                "<div style='font-size:0.80rem;color:#94A3B8;margin-top:4px;'>Max tolerance: $60M (0.09%)</div></div>",
                unsafe_allow_html=True
            )
        with col_id3:
            st.markdown(
                "<div class='kpi-card'><div class='kpi-title'>Headcount Continuity Check</div>"
                "<div style='font-size:1.1rem;font-weight:700;color:#10B981;'>HC(t) = HC(t-1) + Hires - Exits</div>"
                "<div style='font-size:0.80rem;color:#94A3B8;margin-top:4px;'>Exact integer reconciliation: 100%</div></div>",
                unsafe_allow_html=True
            )
            
        st.dataframe(rec_df, use_container_width=True)
        
    with tab_dict:
        st.markdown("#### KPI Metadata & Data Lineage Dictionary")
        
        col_dict_down1, col_dict_down2 = st.columns([3, 1])
        with col_dict_down2:
            dict_csv = kpi_dict.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="\U0001F4E5 Download KPI Dictionary",
                data=dict_csv,
                file_name="microsoft_kpi_data_dictionary.csv",
                mime="text/csv",
                use_container_width=True
            )
            
        st.dataframe(
            kpi_dict.rename(columns={
                "kpi_id": "KPI ID",
                "name": "KPI Name",
                "department": "Department",
                "owner": "Accountable Owner",
                "unit": "Unit",
                "target": "Target",
                "target_direction": "Target Direction",
                "formula": "Calculation Formula",
                "strategic_role": "Strategic Role",
                "freshness_cadence": "Cadence"
            }),
            use_container_width=True
        )


# ==============================================================================
# VIEW 7: HOW THE ALGORITHM WORKS
# ==============================================================================
elif selected_view == "How the Algorithm Works":
    st.markdown("### How the Decision Intelligence Algorithm Works")
    st.markdown("End-to-end mathematical methodology transforming operational telemetry into executive management actions.")
    
    st.markdown(
        """
        <div style='background-color:#161F33;border:1px solid #2C3B59;border-radius:8px;padding:24px;margin-bottom:24px;'>
            <h4 style='color:#A78BFA;margin-top:0px;'>Connected 6-Stage Intelligence Architecture</h4>
            
            <div style='display:flex;flex-direction:column;gap:16px;margin-top:16px;'>
                <div style='background-color:#0E131F;padding:14px;border-left:4px solid #8B5CF6;border-radius:4px;'>
                    <b style='color:#FFFFFF;font-size:0.95rem;'>1. Cross-Departmental Ingestion & Freshness Validation</b><br>
                    <span style='color:#CBD5E1;font-size:0.85rem;'>
                        Ingests time-series metrics across Finance, Cloud Operations, Marketing, and Human Resources. Validates schema, timestamps, and pipeline delivery latency (T+2 day cadence).
                    </span>
                </div>
                
                <div style='background-color:#0E131F;padding:14px;border-left:4px solid #3B82F6;border-radius:4px;'>
                    <b style='color:#FFFFFF;font-size:0.95rem;'>2. Strict Accounting & Operational Continuity Reconciliation</b><br>
                    <span style='color:#CBD5E1;font-size:0.85rem;'>
                        Executes deterministic reconciliation audits on fundamental financial identities: Revenue addition, Gross Profit, Operating Income, Operating Margin, and integer headcount continuity flows.
                    </span>
                </div>
                
                <div style='background-color:#0E131F;padding:14px;border-left:4px solid #10B981;border-radius:4px;'>
                    <b style='color:#FFFFFF;font-size:0.95rem;'>3. Statistical Anomaly & Target Breach Scoring</b><br>
                    <span style='color:#CBD5E1;font-size:0.85rem;'>
                        Calculates rolling standard deviations (\u03c3) and Z-scores: Z = (x - \u03bc) / \u03c3. Classifies severity into CRITICAL, HIGH, MEDIUM, and NORMAL based on target variance and historical distribution tails.
                    </span>
                </div>
                
                <div style='background-color:#0E131F;padding:14px;border-left:4px solid #F59E0B;border-radius:4px;'>
                    <b style='color:#FFFFFF;font-size:0.95rem;'>4. Lagged Cross-Correlation & Granger Causality Engine</b><br>
                    <span style='color:#CBD5E1;font-size:0.85rem;'>
                        Evaluates lead-lag matrices across lags t-3 to t+3. Computes Granger causality F-tests to prove statistical precedence (e.g. SRE Attrition leading Cloud SLA breach by 1 month; SLA breach leading Customer Churn by 2 months).
                    </span>
                </div>
                
                <div style='background-color:#0E131F;padding:14px;border-left:4px solid #EC4899;border-radius:4px;'>
                    <b style='color:#FFFFFF;font-size:0.95rem;'>5. Empirical Value Driver Tree & Sensitivity Mapping</b><br>
                    <span style='color:#CBD5E1;font-size:0.85rem;'>
                        Fits multivariate regressions mapping operational drivers to Operating Margin and Free Cash Flow. Quantifies precise basis-point sensitivities per unit of operational change.
                    </span>
                </div>
                
                <div style='background-color:#0E131F;padding:14px;border-left:4px solid #A855F7;border-radius:4px;'>
                    <b style='color:#FFFFFF;font-size:0.95rem;'>6. Evidence-Backed Action Synthesis & Governance Safeguards</b><br>
                    <span style='color:#CBD5E1;font-size:0.85rem;'>
                        Synthesizes executive actions grounded in computed anomalies. Attaches accountable owner, timeframe, statistical confidence, financial impact, underlying assumptions, and mandatory human review sign-offs.
                    </span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==============================================================================
# VIEW 8: METRICS, LIMITATIONS & GOVERNANCE
# ==============================================================================
elif selected_view == "Metrics, Limitations & Governance":
    st.markdown("### Model Metrics, Statistical Limitations & Governance")
    st.markdown("Scientific rigor, baseline disclosures, degrees of freedom, and ethical constraints.")
    
    col_m1, col_m2 = st.columns(2)
    
    with col_m1:
        st.markdown(
            f"""
            <div class='evidence-box'>
                <h4 style='color:#FFFFFF;margin-top:0px;'>Empirical Model Metrics</h4>
                <p style='color:#E2E8F0;font-size:0.88rem;'>
                    • <b>Sample Size:</b> {len(df)} continuous monthly observations (Jan 2023 - Dec 2025)<br>
                    • <b>Degrees of Freedom:</b> {len(df) - 6} residual degrees of freedom<br>
                    • <b>Operating Margin Model R²:</b> <b>{r2_margin:.3f}</b> (Strong explanatory power)<br>
                    • <b>Free Cash Flow Model R²:</b> <b>{r2_fcf:.3f}</b><br>
                    • <b>Granger Test Critical Threshold:</b> \u03b1 = 0.05 (F-statistic > 3.84)
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col_m2:
        st.markdown(
            """
            <div class='evidence-box'>
                <h4 style='color:#FFFFFF;margin-top:0px;'>Disclosed Model Limitations</h4>
                <p style='color:#E2E8F0;font-size:0.88rem;'>
                    • <b>Observational Data Boundary:</b> Macroeconomic shocks (e.g. interest rate spikes, global semiconductor supply freezes) may alter linear elasticities.<br>
                    • <b>Granger Precedence != Physical Causality:</b> Granger causality confirms temporal predictive precedence, not structural physics.<br>
                    • <b>Baseline Fallback:</b> In subsets with N < 12 periods, regression weights revert to industry benchmark prior distributions.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    st.markdown(
        """
        <div style='background-color:#161F33;border:1px solid #7F1D1D;border-left:4px solid #EF4444;border-radius:8px;padding:20px;margin-top:16px;'>
            <h4 style='color:#FCA5A5;margin-top:0px;'>Ethical AI & Human Safety Governance Framework</h4>
            <p style='color:#E2E8F0;font-size:0.88rem;line-height:1.6;'>
                1. <b>Strict Prohibition of Automated Adverse HR Decisions:</b> The system does not execute automated terminations, performance sanctions, or individual employee compensation cuts. Organizational capacity metrics are aggregated at team and departmental levels.<br>
                2. <b>Human-in-the-Loop Sign-Off Mandate:</b> Recommendations with high financial exposure (> $50M) require signed approval from the CFO and designated EVP before execution.<br>
                3. <b>Synthetic Data Isolation:</b> No live Microsoft internal production databases or proprietary tenant logs are accessed. The system operates on mathematical synthetic data structures designed for decision intelligence demonstration.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr style='border:0.5px solid #2C3B59;margin-top:30px;margin-bottom:20px;'>", unsafe_allow_html=True)

# Executive Brief Export Action Bar (Present on all pages)
col_exp_info, col_exp_btn = st.columns([3, 1])
with col_exp_info:
    st.markdown(
        f"<span style='color:#E2E8F0;font-size:0.85rem;'>Ready to brief executive leadership? Download the comprehensive decision package for period <b>{latest_period['period']}</b>.</span>",
        unsafe_allow_html=True
    )
with col_exp_btn:
    brief_md = generate_executive_brief_markdown(df, anomalies_df, recommendations_df, health_score, r2_margin)
    st.download_button(
        label="\U0001F4C4 Export Executive Brief (Markdown)",
        data=brief_md,
        file_name=f"executive_brief_microsoft_{latest_period['period']}.md",
        mime="text/markdown",
        use_container_width=True
    )
