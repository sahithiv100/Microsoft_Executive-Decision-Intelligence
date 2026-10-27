"""
ui_components.py - Visual Presentation & Plotly Chart Builders
Provides dark navy/charcoal styling with purple accents, high contrast readable typography,
interactive Plotly visualizations, custom metric cards, and evidence badges.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Theme Color Palette - High Contrast Dark Navy & Restrained Purple
BG_DARK = "#0E131F"
CARD_BG = "#161F33"
CARD_BORDER = "#2C3B59"
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#E2E8F0"
TEXT_MUTED = "#94A3B8"
ACCENT_PURPLE = "#8B5CF6"
ACCENT_PURPLE_LIGHT = "#A78BFA"
ACCENT_PURPLE_DARK = "#6D28D9"
COLOR_SUCCESS = "#10B981"
COLOR_WARNING = "#F59E0B"
COLOR_DANGER = "#EF4444"
COLOR_CYAN = "#06B6D4"


def get_custom_css():
    """
    Returns custom CSS for Streamlit with dark navy/charcoal styling,
    restrained purple accents, and high-contrast, fully visible typography.
    """
    return f"""
    <style>
        /* Base page styling */
        .stApp {{
            background-color: {BG_DARK};
            color: {TEXT_PRIMARY};
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }}
        
        /* High contrast headers */
        h1, h2, h3, h4, h5, h6 {{
            color: {TEXT_PRIMARY} !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em;
        }}
        
        p, span, label, div {{
            color: {TEXT_SECONDARY};
        }}
        
        /* Synthetic Data Top Banner */
        .synthetic-banner {{
            background: linear-gradient(90deg, #3B0764 0%, #1E1B4B 50%, #1E293B 100%);
            border-left: 5px solid {ACCENT_PURPLE};
            border-right: 1px solid #4C1D95;
            border-top: 1px solid #4C1D95;
            border-bottom: 1px solid #4C1D95;
            border-radius: 8px;
            padding: 12px 20px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
        }}
        .synthetic-banner-text {{
            color: #FAF5FF !important;
            font-weight: 800;
            font-size: 0.95rem;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }}
        .synthetic-banner-sub {{
            color: #DDD6FE !important;
            font-size: 0.85rem;
            margin-top: 2px;
        }}
        
        /* Metric Cards */
        .kpi-card {{
            background-color: {CARD_BG};
            border: 1px solid {CARD_BORDER};
            border-radius: 10px;
            padding: 18px 20px;
            margin-bottom: 16px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}
        .kpi-card:hover {{
            border-color: {ACCENT_PURPLE};
            transform: translateY(-2px);
        }}
        .kpi-title {{
            color: {TEXT_MUTED} !important;
            font-size: 0.82rem;
            text-transform: uppercase;
            font-weight: 600;
            letter-spacing: 0.05em;
            margin-bottom: 6px;
        }}
        .kpi-value {{
            color: {TEXT_PRIMARY} !important;
            font-size: 1.85rem;
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 6px;
        }}
        .kpi-target {{
            color: {TEXT_SECONDARY} !important;
            font-size: 0.80rem;
        }}
        
        /* Badges */
        .badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.03em;
            text-transform: uppercase;
        }}
        .badge-critical {{
            background-color: rgba(239, 68, 68, 0.2);
            color: #FCA5A5 !important;
            border: 1px solid {COLOR_DANGER};
        }}
        .badge-high {{
            background-color: rgba(245, 158, 11, 0.2);
            color: #FCD34D !important;
            border: 1px solid {COLOR_WARNING};
        }}
        .badge-medium {{
            background-color: rgba(139, 92, 246, 0.2);
            color: #DDD6FE !important;
            border: 1px solid {ACCENT_PURPLE};
        }}
        .badge-success {{
            background-color: rgba(16, 185, 129, 0.2);
            color: #6EE7B7 !important;
            border: 1px solid {COLOR_SUCCESS};
        }}
        
        /* Evidence Drawer Card */
        .evidence-box {{
            background-color: #111A2E;
            border: 1px solid #233352;
            border-left: 4px solid {ACCENT_PURPLE};
            border-radius: 8px;
            padding: 16px;
            margin-top: 12px;
            margin-bottom: 12px;
        }}
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
            background-color: transparent;
            border-bottom: 1px solid {CARD_BORDER};
            padding-bottom: 4px;
        }}
        .stTabs [data-baseweb="tab"] {{
            height: 44px;
            white-space: pre-wrap;
            background-color: #131A2B;
            border-radius: 6px 6px 0px 0px;
            color: {TEXT_SECONDARY} !important;
            font-weight: 600;
            border: 1px solid transparent;
            padding: 0 16px;
        }}
        .stTabs [aria-selected="true"] {{
            background-color: #1F2A44 !important;
            color: #FAF5FF !important;
            border-top: 2px solid {ACCENT_PURPLE} !important;
            border-left: 1px solid {CARD_BORDER} !important;
            border-right: 1px solid {CARD_BORDER} !important;
        }}
        
        /* Dataframes & tables */
        .dataframe {{
            color: {TEXT_PRIMARY} !important;
            background-color: {CARD_BG} !important;
        }}
        
        /* Streamlit Button Styling */
        .stButton>button {{
            background-color: #1E293B;
            color: #FFFFFF !important;
            border: 1px solid #475569;
            border-radius: 6px;
            font-weight: 600;
            padding: 0.4rem 1rem;
            transition: all 0.2s ease;
        }}
        .stButton>button:hover {{
            background-color: {ACCENT_PURPLE};
            border-color: {ACCENT_PURPLE_LIGHT};
            color: #FFFFFF !important;
            box-shadow: 0 0 12px rgba(139, 92, 246, 0.4);
        }}
        
        /* Radio, selectbox, sliders labels */
        .stSelectbox label, .stSlider label, .stRadio label, .stTextInput label {{
            color: {TEXT_PRIMARY} !important;
            font-weight: 600 !important;
        }}
        
        /* Streamlit expander */
        .streamlit-expanderHeader {{
            background-color: #161F33 !important;
            color: {TEXT_PRIMARY} !important;
            font-weight: 600;
            border-radius: 6px;
            border: 1px solid {CARD_BORDER};
        }}
    </style>
    """


def render_banner():
    """Renders the top synthetic demo data banner."""
    html = f"""
    <div class="synthetic-banner">
        <div>
            <div class="synthetic-banner-text">
                \u26a0\ufe0f SYNTHETIC DEMO DATA \u2014 NOT REAL COMPANY DATA
            </div>
            <div class="synthetic-banner-sub">
                Illustrative Microsoft Enterprise Decision Prototype. All metrics, correlations, and anomalies are mathematically simulated.
            </div>
        </div>
        <div>
            <span class="badge badge-medium">Simulation Mode: Active</span>
        </div>
    </div>
    """
    return html


def build_kpi_tree_sunburst(df):
    """
    Builds an interactive Plotly hierarchical driver tree (Sunburst)
    showing Enterprise Value -> Departments -> Drivers -> Root Factors.
    """
    latest = df.iloc[-1]
    
    # Hierarchical tree structure
    labels = [
        # Root
        "Microsoft Enterprise Value",
        # Pillars
        "Intelligent Cloud (Finance)", "Productivity & Business (Finance)", "Data Center COGS (Cost)", "OpEx (R&D & SG&A)",
        # Cloud Drivers
        "Azure Consumption ARR", "Enterprise Renewal Pipeline",
        # Cost Drivers
        "Cloud Compute Infra Cost", "SLA Penalty Credits",
        # Operational Drivers
        "Cloud SLA Delivery (99.95% Target)", "Server Capacity Utilization",
        # People & Delivery Drivers
        "Tech Talent Retention (8.0% Target)", "Critical Architecture Vacancy",
        # Customer Retention
        "Enterprise Cloud Churn", "Net Retention Rate (NRR)"
    ]
    
    parents = [
        "",
        "Microsoft Enterprise Value", "Microsoft Enterprise Value", "Microsoft Enterprise Value", "Microsoft Enterprise Value",
        "Intelligent Cloud (Finance)", "Intelligent Cloud (Finance)",
        "Data Center COGS (Cost)", "Data Center COGS (Cost)",
        "Cloud Compute Infra Cost", "Cloud Compute Infra Cost",
        "Cloud SLA Delivery (99.95% Target)", "Cloud SLA Delivery (99.95% Target)",
        "SLA Penalty Credits", "Azure Consumption ARR"
    ]
    
    values = [
        round(latest["revenue_b"], 1),
        round(latest["cloud_revenue_b"], 1), round(latest["productivity_revenue_b"], 1), 
        round(latest["cogs_b"], 1), round(latest["opex_b"], 1),
        round(latest["cloud_revenue_b"] * 0.72, 1), round(latest["enterprise_pipeline_b"] * 0.35, 1),
        round(latest["cogs_b"] * 0.65, 1), round(max(0.2, (99.95 - latest["sla_delivery_pct"]) * 4.0), 1),
        round(latest["sla_delivery_pct"], 1), round(latest["server_capacity_util_pct"], 1),
        round(latest["tech_attrition_pct"] * 3.5, 1), round(latest["critical_role_vacancy_pct"] * 2.8, 1),
        round(latest["cloud_churn_pct"] * 8.0, 1), round(latest["nrr_pct"] * 0.45, 1)
    ]
    
    colors = [
        "#8B5CF6", # Root
        "#3B82F6", "#6366F1", "#EC4899", "#F59E0B", # Pillars
        "#60A5FA", "#93C5FD",
        "#F43F5E", "#E11D48",
        "#10B981" if latest["sla_delivery_pct"] >= 99.94 else "#EF4444",
        "#F59E0B" if latest["server_capacity_util_pct"] > 84 else "#10B981",
        "#EF4444" if latest["tech_attrition_pct"] > 9.5 else "#10B981",
        "#EF4444" if latest["critical_role_vacancy_pct"] > 5.5 else "#10B981",
        "#EF4444" if latest["cloud_churn_pct"] > 1.1 else "#10B981",
        "#10B981" if latest["nrr_pct"] >= 115 else "#F59E0B"
    ]
    
    fig = go.Figure(go.Sunburst(
        labels=labels,
        parents=parents,
        values=values,
        branchvalues="total",
        marker=dict(colors=colors, line=dict(color="#0E131F", width=2)),
        hoverinfo="label+value+percent parent",
        insidetextorientation="radial"
    ))
    
    fig.update_layout(
        title=dict(
            text="Interactive Executive Value Driver Tree (Click segments to zoom)",
            font=dict(color=TEXT_PRIMARY, size=16, family="sans-serif")
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=50, l=10, r=10, b=10),
        height=520
    )
    
    return fig


def build_trend_anomaly_chart(df, kpi_col, kpi_name, target_val, unit, is_higher_better=True):
    """
    Builds a high-contrast time-series chart with actual historical trajectory,
    target reference line, rolling mean band, and distinct anomaly breach markers.
    """
    fig = go.Figure()
    
    # Target Line
    fig.add_trace(go.Scatter(
        x=df["period"],
        y=[target_val] * len(df),
        mode="lines",
        name=f"Target ({target_val} {unit})",
        line=dict(color="#F59E0B", dash="dash", width=2),
        hoverinfo="y+name"
    ))
    
    # Historical Actual Line
    fig.add_trace(go.Scatter(
        x=df["period"],
        y=df[kpi_col],
        mode="lines+markers",
        name=f"Actual {kpi_name}",
        line=dict(color=ACCENT_PURPLE, width=3),
        marker=dict(size=5, color=ACCENT_PURPLE_LIGHT),
        hovertemplate="Period: %{x}<br>Actual: %{y} " + unit + "<extra></extra>"
    ))
    
    # Identify Breaches
    if is_higher_better:
        breach_mask = df[kpi_col] < target_val * 0.985
    else:
        breach_mask = df[kpi_col] > target_val * 1.015
        
    breach_df = df[breach_mask]
    
    if len(breach_df) > 0:
        fig.add_trace(go.Scatter(
            x=breach_df["period"],
            y=breach_df[kpi_col],
            mode="markers",
            name="Target Deviation Breach",
            marker=dict(size=11, color=COLOR_DANGER, symbol="x", line=dict(width=2, color="#FFFFFF")),
            hovertemplate="<b>BREACH FLAGGED</b><br>Period: %{x}<br>Value: %{y} " + unit + "<extra></extra>"
        ))
        
    fig.update_layout(
        title=dict(
            text=f"Historical Trajectory & Target Breaches: {kpi_name}",
            font=dict(color=TEXT_PRIMARY, size=15)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(22, 31, 51, 0.6)",
        font=dict(color=TEXT_SECONDARY),
        xaxis=dict(
            showgrid=True,
            gridcolor="#233352",
            tickangle=-45,
            color=TEXT_SECONDARY
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="#233352",
            color=TEXT_SECONDARY,
            title=f"{unit}"
        ),
        legend=dict(
            bgcolor="rgba(14, 19, 31, 0.8)",
            bordercolor=CARD_BORDER,
            borderwidth=1,
            font=dict(color=TEXT_PRIMARY)
        ),
        margin=dict(t=50, l=40, r=20, b=50),
        height=380
    )
    
    return fig


def build_lead_lag_heatmap(causality_df):
    """
    Builds a cross-correlation heatmap across lags (-3 to +3 periods)
    with visible numerical annotations and clear interpretation.
    """
    y_labels = causality_df["relationship"].tolist()
    x_labels = ["Lag 0 (Simultaneous)", "Lag 1 (+1 Mo Preceding)", "Lag 2 (+2 Mo Preceding)", "Lag 3 (+3 Mo Preceding)"]
    
    z_matrix = [
        [row["corr_lag_0"], row["corr_lag_1"], row["corr_lag_2"], row["corr_lag_3"]]
        for _, row in causality_df.iterrows()
    ]
    
    fig = go.Figure(data=go.Heatmap(
        z=z_matrix,
        x=x_labels,
        y=y_labels,
        colorscale=[
            [0.0, "#EF4444"],
            [0.35, "#334155"],
            [0.65, "#6D28D9"],
            [1.0, "#06B6D4"]
        ],
        text=[[f"{val:+.2f}" for val in row] for row in z_matrix],
        texttemplate="%{text}",
        textfont=dict(size=12, color="#FFFFFF", family="Arial Black"),
        colorbar=dict(
            title=dict(text="Correlation (r)", font=dict(color=TEXT_PRIMARY)),
            tickfont=dict(color=TEXT_SECONDARY)
        )
    ))
    
    fig.update_layout(
        title=dict(
            text="Lagged Cross-Correlation Matrix: Predictive Precedence vs Coincidence",
            font=dict(color=TEXT_PRIMARY, size=15)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=TEXT_SECONDARY),
        xaxis=dict(color=TEXT_SECONDARY, side="bottom"),
        yaxis=dict(color=TEXT_SECONDARY, autorange="reversed"),
        margin=dict(t=50, l=150, r=20, b=50),
        height=420
    )
    
    return fig


def build_scenario_comparison_chart(sim_df):
    """
    Builds a grouped bar chart comparing Baseline vs Simulated Scenario outputs.
    """
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=sim_df["Metric"],
        y=sim_df["Baseline"],
        name="Baseline Plan",
        marker_color="#4B5563",
        text=sim_df["Baseline"],
        textposition="outside",
        textfont=dict(color=TEXT_SECONDARY)
    ))
    
    fig.add_trace(go.Bar(
        x=sim_df["Metric"],
        y=sim_df["Scenario"],
        name="Simulated Scenario",
        marker_color=ACCENT_PURPLE,
        text=sim_df["Scenario"],
        textposition="outside",
        textfont=dict(color="#FAF5FF")
    ))
    
    fig.update_layout(
        title=dict(
            text="Financial Model Recalculation: Baseline vs. Scenario",
            font=dict(color=TEXT_PRIMARY, size=15)
        ),
        barmode="group",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(22, 31, 51, 0.6)",
        font=dict(color=TEXT_SECONDARY),
        xaxis=dict(showgrid=False, color=TEXT_SECONDARY),
        yaxis=dict(showgrid=True, gridcolor="#233352", color=TEXT_SECONDARY),
        legend=dict(
            bgcolor="rgba(14, 19, 31, 0.8)",
            bordercolor=CARD_BORDER,
            font=dict(color=TEXT_PRIMARY)
        ),
        margin=dict(t=50, l=40, r=20, b=40),
        height=380
    )
    
    return fig


def build_sensitivity_tornado_chart(sensitivities_df):
    """
    Builds a horizontal sensitivity tornado chart showing impact on Operating Margin.
    """
    df_sorted = sensitivities_df.sort_values(by="margin_impact_pct", ascending=True)
    
    bar_colors = [COLOR_DANGER if val < 0 else COLOR_SUCCESS for val in df_sorted["margin_impact_pct"]]
    
    fig = go.Figure(go.Bar(
        y=df_sorted["driver_name"],
        x=df_sorted["margin_impact_pct"],
        orientation="h",
        marker=dict(color=bar_colors),
        text=[f"{v:+.2f}% ({v*100:+.0f} bps)" for v in df_sorted["margin_impact_pct"]],
        textposition="outside",
        textfont=dict(color=TEXT_PRIMARY, size=11)
    ))
    
    fig.update_layout(
        title=dict(
            text="Operational Driver Sensitivity: Operating Margin Impact per Benchmark Shock",
            font=dict(color=TEXT_PRIMARY, size=15)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(22, 31, 51, 0.6)",
        font=dict(color=TEXT_SECONDARY),
        xaxis=dict(
            title="Operating Margin Delta (%)",
            showgrid=True,
            gridcolor="#233352",
            color=TEXT_SECONDARY,
            zeroline=True,
            zerolinecolor="#94A3B8",
            zerolinewidth=2
        ),
        yaxis=dict(color=TEXT_PRIMARY),
        margin=dict(t=50, l=180, r=60, b=40),
        height=340
    )
    
    return fig
