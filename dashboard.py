import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("flagged_transactions.csv")
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
daily_amounts = df.groupby(df['Timestamp'].dt.date)['Amount Paid'].sum().reset_index()

def assign_severity(row):
    if row['Payment Format'] == 'Bitcoin' or row['Payment Format'] == 'Cash':
        return 'High'
    elif row['Amount Paid'] > 10000:
        return 'Medium'
    else:
        return 'Low'

df['Severity'] = df.apply(assign_severity, axis=1)

severity_counts = df['Severity'].value_counts()
top_banks = df['From Bank'].value_counts().head(10)
top_formats = df['Payment Format'].value_counts()

fig = make_subplots(
    rows=2, cols=3,
    specs=[[{"type": "pie"}, {"type": "bar"}, {"type": "bar"}],
           [{"type": "scatter", "colspan": 3}, None, None]],
    subplot_titles=("Severity Distribution", "Top 10 Banks", "Payment Methods", "Flagged Transaction Amounts Over Time"),
    vertical_spacing=0.08,
    row_heights=[0.5, 0.5]
)
fig.add_trace(go.Pie(labels=severity_counts.index, values=severity_counts.values), row=1, col=1)
fig.add_trace(go.Bar(x=top_banks.index.astype(str), y=top_banks.values), row=1, col=2)
fig.add_trace(go.Bar(x=top_formats.index, y=top_formats.values), row=1, col=3)
fig.add_trace(go.Scatter(x=daily_amounts['Timestamp'], y=daily_amounts['Amount Paid'], mode='lines', name='Amount'), row=2, col=1)
fig.update_layout(
    title=dict(
        text="AML/CFT Transaction Flagging Dashboard",
        font=dict(size=28, color="#58a6ff"),
        x=0.5,
        xanchor='center'
    ),
    paper_bgcolor="#0d1117",
    plot_bgcolor="#0d1117",
    font=dict(color="white"),
    height=830,
    width=1400,
    showlegend=True,
    margin=dict(t=120, b=40, l=40, r=40)
)
fig.update_xaxes(range=[daily_amounts['Timestamp'].min(), daily_amounts['Timestamp'].max()], row=2, col=1)

fig.write_html("dashboard.html", 
    full_html=True,
    include_plotlyjs='cdn',
    config={'displayModeBar': False}
)
