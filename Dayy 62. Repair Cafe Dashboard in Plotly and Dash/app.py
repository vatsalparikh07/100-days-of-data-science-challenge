import dash
from dash import Dash, html, dcc, Input, Output, callback, Patch, State, ctx
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd
from help_functions import *

# Read CSV file from Google Drive 
url = 'https://drive.google.com/uc?id=1cT7JSWDQw9cb3u2H4RgcLO9xj79HYYWM'
try:    
    df = pd.read_csv(url, low_memory=False)
except Exception as e:
    print(f"An error occurred: {e}")

# only one records = 'Unknown'
df = df[df['repair_status']!='Unknown']
# Create a new column with the product name
df['product'] = df['partner_product_category'].apply(lambda x : x.split('~')[-1].strip())

# Create combined dataframe with counts and percentage
comb_df_category = combine_data_cnt_percent(df, col_base='product_category', col_add='repair_status', col_prod='product')
comb_df_product = combine_data_cnt_percent(df, col_base='product', col_add='repair_status', col_prod='product'
                                           ).sort_values(by='total', ascending=False)

# Calculate metrics
total_repairs = df.shape[0]
num_categories = df['product_category'].nunique()
num_products = df['product'].nunique()
max_fixed = df['repair_status'].value_counts(normalize=True).max()


# Create app object=============================================================================
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, "/assets/styles.css"])

server = app.server

# ===================Create components==========================================================
# Create header with link to Figure Friday challenge
header = html.Div([
    html.Img(src='assets/repairing-tools.png', style={'width': '48px', 'margin-left': '10px'}),
    html.H2('Repair Cafe International Dashboard', 
             style={'textAlign': 'center', 'color': 'white',  'padding': 15, 'margin-bottom': 0}),
    html.A(
        html.Img(src='assets/plotly_logo_dark.png', 
                 id='image-link',
                 style={'cursor': 'pointer', 'height': '48px'}),
        href='https://community.plotly.com/t/figure-friday-2024-week-43/88243', 
        target='_blank' ,
        style={'display': 'flex', 'justify-content': 'end'}), 

    dbc.Tooltip("Click to view Challenge Figure Friday 2024 - week 43",
                 target="image-link", 
                 placement="top" , 
                 className="custom-tooltip" )                
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'backgroundColor': '#456F9C',})


# Define helper function to create metric cards 
def make_metric_card(name, value):    
    if name == 'Status Fixed':
        child_p = f'{value:.0%}'
        f_color ='forestgreen'
    else:        
        child_p = f'{value:,.0f}' 
        f_color ='rgb(53 86 120)'  

    return dbc.Col(dbc.Card(
        dbc.CardBody(
            html.H4([
                html.Span(name),
                html.P(child_p, style={'fontWeight': 'bold', 'color': f_color, 'margin-bottom': 0, 'margin-top': '3px'})
                ], style={'textAlign': 'center', 'fontWeight': 'normal', 'margin-bottom': 0}),
            ), style={'border-left': '7px solid #3E638D'}),
        width=3)

# Create cards with metrics
metrics_value = [total_repairs, max_fixed, num_categories, num_products] 
metrics_name = ['Number of Repairs', 'Status Fixed', 'Categories', 'Products']
cards = [make_metric_card(name, value) for name, value in zip(metrics_name, metrics_value)]  


# Create bar polar chart for top 10 categories
comb_df_category_all = combine_data_cnt_percent(
    df, col_base='product_category',
    col_add='repair_status',
    col_prod='product', norm='index').sort_values(by='total', ascending=True)
polar =create_barpolar_top_10(comb_df_category_all, base_col='product_category')


# Create bar chart for 20 most presented products
polar_prod =create_barpolar_top_20(
    comb_df_product.head(20), 
    base_col='product',
    title='Top 20 Most Presented Products')


# Create radio buttons
radio_btns_polar =html.Div([
    dbc.Label('Sort by :', style={'margin-bottom': '0',  'align-text': 'center'}),
    dbc.RadioItems(
                id='radio-buttons',
                options=['Total', 'Fixed', 'Repairable', 'End of life'],
                value='Total',                  
                style={'display': 'flex', 'justify-content': 'space-around', 'width': '70%' })
    ], style={'display': 'flex', 'justify-content': 'space-around', 'margin-top': '20px', 'padding': '5px',
              'align-items': 'center', 'border': '1px solid lightgrey', 'borderRadius': '5px'})

# Define ag grid table for categories and products
cat_grid = dag.AgGrid(
    id="category-grid",
    style={'height': '530px'},   
    rowData=comb_df_category.to_dict("records"),
    columnDefs=create_column_defs(comb_df_category, max_fixed),
    columnSize="sizeToFit", 
    defaultColDef={"filter": "agTextColumnFilter", "tooltipComponent": "CustomTooltipSimple"},     
    dashGridOptions={"animateRows": False, 
                     'pagination':True, 
                     'paginationPageSize': 20, 
                     'tooltipShowDelay': 0,
                     'tooltipHideDelay': 2000},)


# Create scatter plot for all categories by status fixed
df_category_for_scatter = comb_df_category.copy()
df_category_for_scatter['size'] = df_category_for_scatter['total'].map(set_marker_size)*1.2
scatter_cat_status = create_scatter_plot_for_status(
            df_category_for_scatter, col_x='product_category', col_y='Fixed', size='size', 
            cust_data=['total', 'Repairable', 'End of life'], max_fixed=max_fixed)


# Create scatter plot for all products by status fixed
df_product_for_scatter = comb_df_product.copy().reset_index(drop=True)
df_product_for_scatter['size'] = df_product_for_scatter['total'].map(set_marker_size)*1.2
scatter_prod_status = create_scatter_plot_for_status(
            df_product_for_scatter, col_x='product', col_y='Fixed', size='size', 
            cust_data=['total', 'Repairable', 'End of life'], max_fixed=max_fixed)


# Create dropdown for categories
drdw_category = dcc.Dropdown(
    id='categories-dropdown', 
    options= df['product_category'].unique(),    
    placeholder='Select a category',
    style={'width': '100%', 'font-weight': '400', 'font-size': '18px'})

# Create dropdown for products
drdw_product = dcc.Dropdown(
    id='products-dropdown', 
    options= df['product'].unique(),    
    placeholder='Select a product',
    style={'width': '100%', 'font-weight': '400', 'font-size': '18px'})

       
# Define helper function to create modal windows
def create_modal_window(title_name, dropdown, fig, suffix):
    return html.Div([
        dbc.Modal([
                dbc.ModalHeader(
                    dbc.ModalTitle([
                        f"{title_name} by Status Fixed (%)", 
                        html.Div(dropdown, style={'flex': '0.6'})], 
                        style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'width': '100%'}
                    ), close_button=False
                ),
                dbc.ModalBody(dcc.Graph(id=f'scatter-{suffix}', figure=fig, config=config_mode)),
                dbc.ModalFooter(dbc.Button("Close", id=f'btn-close-scatter-{suffix}')),
            ],
            id=f"modal-scatter-{suffix}",
            size="xl",
            keyboard=False,
            backdrop="static")
    ])

#Create modal window for all categories by status fixed
modal_scatter_cat = create_modal_window("Categories", drdw_category, scatter_cat_status, "cat")  

# Create modal window for all products
modal_scatter_prod = create_modal_window("Products", drdw_product, scatter_prod_status, "prod")


# Create app layout=============================================================================
app.layout = dbc.Container([
    dbc.Row(id='title', children=header, style={"padding": 0}),
    html.Br(),

    dbc.Row([*cards]),
    html.Br(),  

    dbc.Row([
        dbc.Col([
            dbc.Card(dcc.Graph(id='polar-category', figure=polar, config={'displayModeBar': False}), body=True), 
            radio_btns_polar,          
            ], width=6),                    
      
        dbc.Col([
            dbc.Card(dbc.CardBody(dcc.Graph(id='polar-product', figure=polar_prod, config={'displayModeBar': False}) ) ), 

            html.Div([
                html.H6(f'Open Table: ', className="text-nowrap mb-0"),
                dbc.Button("Categories", id="open-cat-table", color="primary",  n_clicks=0),
                dbc.Button('Products', id='open-prod-table', color="primary",  n_clicks=0),
                html.H6(f'View Graph: ', className="text-nowrap mb-0"),
                dbc.Button('Categories', id='btn-view-all-cat', color="info",  n_clicks=0),                
                dbc.Button('Products', id='btn-view-all-prod', color="info",  n_clicks=0)
                ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'margin-top': '20px'}),                                  
            ], width=6, style={'justify-content': 'space-between', 'align-items': 'center'}),       
         ]),
               
    dbc.Row([modal_scatter_cat, modal_scatter_prod]),

    dbc.Row([
        dbc.Col([
            dbc.Modal([
                dbc.ModalHeader(id="modal-title", style={'width': '100%'}),
                dbc.ModalBody(id="modal-body")
                ], id="notification-modal", is_open=False, centered=True ),           

            dbc.Collapse(
                id='cat-collapse',
                children=[
                    html.Br(),
                    cat_grid,
                    html.Div([
                        dbc.Button("Reset All Filters", id="reset-button", color="primary",  n_clicks=0),
                        dbc.Button("Close Table", id="close-table-button", color="primary",  n_clicks=0),
                        dbc.Input(id='input-file-name', type='text', placeholder="Enter a file name", style={'flex': '0.5'}),
                        dbc.Button("Save as CSV", id="save-button", color="primary")
                        ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'margin-top': '20px'}),
                    ],
                is_open=False),           
            ], width=12),    
    ]),
    html.Br(),

    dbc.Row([
        dbc.Col([
            html.H6("Created with 🤍 by Natalia", style={'margin':'10px'}),
            html.A(html.Img(src='assets/github_blue.png', style={'height': '32px'}), 
                href="https://github.com/natatsypora/figure-friday-week43-dash-app",
                target="_blank")                      
            ], width=12, style={'background-color': 'white', 'padding': '20px',  'display': 'flex', 'justify-content': 'center',}),  
        ])
],     
 style={'background-color': '#F8F9FA', }
)

# =======================Callbacks===============================

# Callback to toggle collapse window with ag-grid table
@app.callback(
    Output("cat-collapse", "is_open"),
    Output("category-grid", "rowData"),
    Output("category-grid", "columnDefs"),
    Input("open-cat-table", "n_clicks"),
    Input("open-prod-table", "n_clicks"), 
    Input("close-table-button", "n_clicks"),
    State("cat-collapse", "is_open"),
    prevent_initial_call=True
)

def toggle_collapse(open_cat_clicks, open_prod_clicks, close_table_clicks, is_open):
    if ctx.triggered_id in ["open-cat-table", "open-prod-table"]:
        df = comb_df_category if ctx.triggered_id == "open-cat-table" else comb_df_product
        return (            
            True if is_open else not is_open,       # Keep the collapse state open or toggle it to open
            df.to_dict("records"),                  # Update rowData
            create_column_defs(df, max_fixed)       # Update columnDefs
        )
    elif ctx.triggered_id == "close-table-button":
        return (
            not is_open,        # Toggle the collapse state to close
            dash.no_update,     # No update to rowData
            dash.no_update      # No update to columnDefs
        )


# Callback to reset filters in the ag-grid table
@app.callback(
    Output("category-grid", "filterModel"),
    Input("reset-button", "n_clicks")       
)
def reset_filters(n_clicks):
    if n_clicks:
        return {}
    return dash.no_update   


# Define helper functions for modal windows with alert
def alert_response(): 
    return ( False,                                     # exportDataAsCsv 
            {},                                         # csvExportParams 
            True,                                       # is_open 
            "Alert",                                    # modal-title
            {'background-color': '#FFF3CD'},            # modal-header style 
            "File name cannot be empty!" )              # modal-body 
           

def success_response(file_name): 
    return ( True,                                                       # exportDataAsCsv
            {"fileName": f"{file_name}.csv"},                            # csvExportParams 
            True,                                                        # is_open 
            "Success",                                                   # modal-title 
            {'background-color': '#D8F0D3'},                             # modal-header style 
            f"File has been successfully saved as '{file_name}.csv' !")  # modal-body


# Callback to handle the CSV Export and Modal Notification
@app.callback( Output("category-grid", "exportDataAsCsv"),
               Output("category-grid", "csvExportParams"),
               Output("notification-modal", "is_open"),
               Output("modal-title", "children"),
               Output("modal-title", "style"),
               Output("modal-body", "children"),                     
               Input("save-button", "n_clicks"),                      
               State("input-file-name", "value"), 
               prevent_initial_call=True 
) 
def save_table(n_clicks, file_name):   
    if ctx.triggered_id  == "save-button":
        if not file_name or file_name.isspace(): 
            # Show alert modal 
            return alert_response()
        else:
            # Show success modal 
            return success_response(file_name)    

# Callback to toggle the modal window with scatter plot for all categories
@app.callback(
    Output("modal-scatter-cat", "is_open"),
    Input("btn-view-all-cat", "n_clicks"),
    Input("btn-close-scatter-cat", "n_clicks"),
    State("modal-scatter-cat", "is_open"),
)
def modal_scatter_cat(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open  

# Callback to update scatter plot for categories
@app.callback(
    Output("scatter-cat", "figure"),
    Input("categories-dropdown", "value"),    
    prevent_initial_call=True       
)  
def update_scatter_cat(selected_category):
    if selected_category is None:
        return scatter_cat_status
    else:
        # Create patch
        patch2 = Patch()
        # Get the index of the selected product
        selected_index = df_category_for_scatter.index[df_category_for_scatter['product_category'] == selected_category].tolist()[0] 
        # Highlight the selected marker and increase its size
        patch2['data'][0]['marker']['color'] = ['yellow' if i == selected_index else '#486C94' for i in range(len(df_category_for_scatter))] 
        patch2['data'][0]['marker']['line']['color'] = ['red' if i == selected_index else 'white' for i in range(len(df_category_for_scatter))] 
        patch2['data'][0]['marker']['size'] = [25 if i == selected_index 
                                              else set_marker_size(df_category_for_scatter['total'][i])*1.2 for i in range(len(df_category_for_scatter))]
       
        return patch2

# Callback to toggle the modal window with scatter plot for all products
@app.callback(
    Output("modal-scatter-prod", "is_open"),
    Input("btn-view-all-prod", "n_clicks"),
    Input("btn-close-scatter-prod", "n_clicks"),
    State("modal-scatter-prod", "is_open"),
)
def modal_scatter_prod(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open  

# Callback to update scatter plot for products
@app.callback(
    Output("scatter-prod", "figure"),
    Input("products-dropdown", "value"),    
    prevent_initial_call=True       
)  
def update_scatter_prod(selected_product):
    if selected_product is None:
        return scatter_prod_status
    else:
        # Create patch
        patch = Patch()
        # Get the index of the selected product
        selected_index = df_product_for_scatter.index[df_product_for_scatter['product'] == selected_product].tolist()[0] 
        # Highlight the selected marker and increase its size
        patch['data'][0]['marker']['color'] = ['yellow' if i == selected_index else '#486C94' for i in range(len(df_product_for_scatter))] 
        patch['data'][0]['marker']['line']['color'] = ['red' if i == selected_index else 'white' for i in range(len(df_product_for_scatter))] 
        patch['data'][0]['marker']['size'] = [25 if i == selected_index 
                                              else set_marker_size(df_product_for_scatter['total'][i])*1.2 for i in range(len(df_product_for_scatter))]   
             
        return patch

    
# Callback to manage selection changes for radio buttons
@app.callback( Output('polar-category', 'figure'),
               Input('radio-buttons', 'value'), 
               State('polar-category', 'figure'), 
               )
def update_barpolar(selected_value, fig):      
    if selected_value == 'Total':
        return polar
    else:
        sorted_df = comb_df_category.sort_values(by=selected_value, ascending=True)
        base_col = 'product_category'        
       
        for trace in fig['data']:               
            if trace['name'] == selected_value:                
                trace['r'] = sorted_df[selected_value].tolist()                
                trace['theta'] = [f'{n}<br> {v:,.0%}' for n, v in sorted_df[[base_col, selected_value]].values]
                trace['customdata'] = list(zip(sorted_df[['total', selected_value+' cnt', base_col]].values,
                                                         [selected_value]*len(sorted_df)))
                trace['hovertemplate'] = '<b>%{customdata[0][2]}</b><br>Total Repairs %{customdata[0][0]:,.0f}'+\
                                         '<br>%{customdata[1]}  %{r:.1%} (%{customdata[0][1]:,.0f})<extra></extra>'
                trace['visible'] = True
                trace['showlegend'] = True
                
            else:                
                trace['visible'] = False
                trace['showlegend'] = False               

        fig['layout']['title']['text'] = f'Top 10 Product Categories by Status {selected_value}'            
            
        return fig          
        

if __name__ == "__main__":
    app.run_server(debug=False) # debug=True --> auto-reload
