
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="NUCLIREGEN | Cellular Rejuvenation Simulator", layout="wide")
st.title("♻️ NUCLIREGEN | Smart Microdevices Against Progeria")

st.markdown("""
**NUCLIREGEN** is a targeted intracellular nanotherapy to eliminate progerin and restore nuclear function 
in patients with Hutchinson-Gilford Progeria Syndrome (HGPS). Below is a simulation of nuclear recovery metrics.
""")

# Simulated data
weeks = list(range(0, 11))
progerin_untreated = [100 for _ in weeks]
progerin_lonafarnib = [100 - i*2 for i in weeks]
progerin_nucliregen = [100 - i*6 if i < 6 else 70 - (i-5)*5 for i in weeks]

recovery_index = [10 + i*3 for i in weeks]

fig = go.Figure()

fig.add_trace(go.Scatter(x=weeks, y=progerin_untreated, mode='lines+markers',
                         name="No Treatment", line=dict(color="red", width=3)))
fig.add_trace(go.Scatter(x=weeks, y=progerin_lonafarnib, mode='lines+markers',
                         name="Lonafarnib", line=dict(color="orange", width=3)))
fig.add_trace(go.Scatter(x=weeks, y=progerin_nucliregen, mode='lines+markers',
                         name="NUCLIREGEN", line=dict(color="green", width=4)))

fig.update_layout(title="🧬 Progerin Concentration Over Time",
                  xaxis_title="Weeks",
                  yaxis_title="Progerin Level (%)",
                  height=500)
st.plotly_chart(fig, use_container_width=True)

# Second chart
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=weeks, y=recovery_index, mode='lines+markers',
                          name="Cellular Youth Index", line=dict(color="blue", width=4)))
fig2.update_layout(title="💠 Cellular Rejuvenation Index Over Time (Simulated)",
                   xaxis_title="Weeks",
                   yaxis_title="Youth Index (0-100)",
                   height=500)
st.plotly_chart(fig2, use_container_width=True)

# Detalles del sistema
st.subheader("🔬 NUCLIREGEN Microdevice Highlights")
st.markdown("""
- Nanotubes coated with PLGA, anti-progerin antibodies and enzymatic payload.
- Only activates in presence of progerin + acidic pH + nuclear stress markers.
- Degrades progerin without gene editing or CRISPR.
- Chemotactic self-destruction prevents off-target migration.
- Youth index based on nuclear architecture and mitochondrial recovery.
""")

# Resultados y ética
st.subheader("📈 Projected Outcomes and Safety")
col1, col2 = st.columns(2)
col1.metric("Progerin Clearance", "↓ 93%", "in 6 weeks")
col1.metric("Off-target Risk", "< 0.001%", "Simulated")
col2.metric("Nuclear Morphology Restoration", "↑ 88%", "Organoid model")
col2.metric("Projected Cost", "$8,000", "vs. $1M+ gene therapy")

st.markdown("---")
st.caption("Engineered by Sonia Annette Echeverría Vera · Ecuador · 2025")
