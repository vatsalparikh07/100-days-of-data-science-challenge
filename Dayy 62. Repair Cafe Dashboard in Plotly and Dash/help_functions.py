import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

#https://www.color-hex.com/color/7fbf7b
mar_colors=['#7fbf7b', '#c2cfda', '#2b83ba']
marker_color_map={'Fixed':'#7fbf7b', 'Repairable':'#2b83ba', 'End of life':'#c2cfda'}

# Define config mode for plotly graph
config_mode = {'displaylogo': False,
               'modeBarButtonsToRemove': ['zoom', 'pan', 'select', 'zoomIn', 'zoomOut', 'lasso', 'autoScale', 'toImage']}

# Define function to combine data with count and percent---------  
def combine_data_cnt_percent(df, col_base, col_add, col_prod, norm='index'):
    # Calculate counts and normalized counts
    count = df[col_base].value_counts()
    count_norm = df[col_base].value_counts(normalize=True)
    
    # Combine counts and normalized data into a single DataFrame
    comb_df = pd.concat([count, count_norm], axis=1)
    comb_df.columns = ['total', 'percentage']
    
    # Add column with number of products if col_base is different from col_prod
    if col_base != col_prod:
        comb_df['n_products'] = df.groupby(col_base)[col_prod].nunique()
    
    # Calculate crosstabs for counts and normalized counts
    ct_cnt = pd.crosstab(df[col_base], df[col_add])
    ct_norm = pd.crosstab(df[col_base], df[col_add], normalize=norm)
    
    # Ensure the order of columns in crosstabs
    order = ['Fixed', 'Repairable', 'End of life']
    ct_cnt = ct_cnt[order]    
    ct_norm = ct_norm[order]
    
    # Combine all DataFrames
    comb_df = comb_df.join(ct_norm).join(ct_cnt, rsuffix=' cnt').reset_index()
    
    return comb_df

# Define function to create a column definitions----------------
def create_column_defs(df, max_fixed):
    column_defs = []
    for col in df.columns:
        col_def = {
            'field': col,
            'minWidth': 100, 'width': 135,
            'type': 'rightAligned',
            'filter': 'agNumberColumnFilter',
            'filterParams': {
                'buttons': ['apply', 'reset', 'clear'],
                'closeOnApply': True}
        }
        if df[col].dtype == 'int64':
            col_def.update({
                'valueFormatter': {'function': 'd3.format(",.0f")(params.value)'}
            })
        elif col == 'Fixed':
            col_def.update({"cellStyle": {
            "styleConditions": [
                {
                    "condition": f"params.value >= {max_fixed}",
                    "style": {"color": "forestgreen", 'fontWeight': 'bold'}}
           ]
                }, 'valueFormatter': {'function': 'd3.format(".1%")(params.value)'}})
            
        elif df[col].dtype == 'float64':
            col_def.update({
                'valueFormatter': {'function': 'd3.format(".1%")(params.value)'}
            })
        elif df[col].dtype == 'object':
            col_def.update({'type': 'leftAligned', 'tooltipField': col, 
                            'filter': 'agTextColumnFilter', 'width': 210})
        
        column_defs.append(col_def)

    return column_defs

# Define function to set marker size-----------------------------
def set_marker_size(x):
    if x <= 10:
        return 5
    if x <= 100:
        return 8
    if x <= 500:
        return 11  
    if x <= 1000:
        return 14
    if x <= 2000:
        return 17
    if x <= 5000:
        return 20
    else:
        return 25

# Create scatter plot for all categories by status fixed=========
def create_scatter_plot_for_status(dff, col_x, col_y, size, cust_data, max_fixed):
    fig = go.Figure()
    fig.add_scatter(
        x=dff[col_x], y=dff[col_y],
        mode='markers', name='', 
        marker_size=dff[size], marker_color='#456F9C',        
        customdata=dff[cust_data])
   
    # Update hovertemplate for more detailed customization
    fig.update_traces(
        hovertemplate='<br>'.join(['<b>%{x}</b><br>',
                                   'Total Repairs: %{customdata[0]:,.0f}',
                                   'Fixed: <b>%{y:.0%}</b>',
                                   'Repairable: %{customdata[1]:.0%}',
                                   'End of life: %{customdata[2]:.0%}']))        
    
    fig.update_yaxes(
        visible=True, showticklabels=True, 
        tickformat='.0%', title=None, 
        range=[-0.02, 1.03], nticks=10)
    
    fig.update_layout(
         margin=dict(l=0, r=0, t=10, b=0), 
         height=400,
         template='plotly_white',
         #title='Products by Status Fixed', title_font_size=20,
         xaxis_visible=False)
     
    fig.add_hline(y=max_fixed, line_width=1, line_dash='dot')

    fig.add_hrect(y0=max_fixed, y1=1.01,
                  label_text=f'Average <b>{max_fixed:.0%}</b>',
                  label_textposition='bottom right',
                  fillcolor="forestgreen", opacity=0.2,
                  layer="below", line_width=0,)
    
    return fig

# Create barpolar top 10 Product Categories======================
def create_barpolar_top_10(dff_comb, base_col):    
    fig = go.Figure()
    for col, mc in marker_color_map.items():
        fig.add_barpolar(
            r=dff_comb[col],
            customdata = list(zip(dff_comb[['percentage', base_col, 'n_products']].values, [col] * len(dff_comb))),
            hovertemplate='<b>%{customdata[0][1]}</b><br>Repair rate %{customdata[0][0]:.1%}'+
                          '<br>Products in Category %{customdata[0][2]:,.0f}<br>%{customdata[1]} %{r:.1%}<extra></extra>',
            theta=[f'{n}<br> {v:,.0f}' for n, v in dff_comb[[base_col, 'total']].values],
            name=col, opacity=0.8, marker_color=mc)        

    fig.update_layout(
        title=f'Top 10 Product Categories',
        title_font_size=20, title_x=0.1, title_y=0.97,
        height=550, margin=dict(l=0, r=120), 
        template=None, font_size=14,
        legend=dict(orientation='h', x=0.1, title='Repair Status' ),
        polar = dict(
            sector=[0, 90],
            radialaxis = dict(showticklabels=True, ticks='',
                              nticks=7, tickformat='.1%',),
            angularaxis = dict(showticklabels=True, ticks='', rotation=95)))
    
    return fig

# Create barpolar top 20 Most Presented Products=================
def create_barpolar_top_20(dff_comb, base_col, title):
    fig = go.Figure()
    for col, mc in marker_color_map.items():
        fig.add_barpolar(
            r=dff_comb[col],
            customdata = list(zip(dff_comb[['percentage', col+' cnt', base_col]].values, [col] * len(dff_comb))),
            hovertemplate='<b>%{customdata[0][2]}</b><br>Repair rate %{customdata[0][0]:.1%}'+
                          '<br>%{customdata[1]} %{r:.1%} (%{customdata[0][1]:,.0f})<extra></extra>',
            theta=[f'{n}<br> {v:,.0f}' for n, v in dff_comb[[base_col, 'total']].values],
            name=col, opacity=0.8, marker_color=mc)

    fig.update_layout(#paper_bgcolor='#e1e9e9',
        title=title,
        title_font_size=20, title_x=0.2, title_y=0.97,
        height=550,  margin=dict(l=120, r=100), 
        template=None, font_size=14,
        legend=dict(orientation='h', x=0, title='Repair Status : ' ),
        polar = dict(
            radialaxis = dict(showticklabels=True, ticks='',
                              nticks=6, tickformat='.0%',),
            angularaxis = dict(showticklabels=True, ticks='',
                               direction='clockwise',
                               rotation=90)))

    return fig

