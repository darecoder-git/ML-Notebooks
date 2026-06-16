import plotly.express as px


def render_chart(df):

    if len(df.columns) < 2:
        return None

    x_col = df.columns[0]
    y_col = df.columns[1]

    if "date" in x_col.lower() or "month" in x_col.lower():
        fig = px.line(df, x=x_col, y=y_col)
    else:
        fig = px.bar(df, x=x_col, y=y_col)

    return fig