from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

df = pd.read_csv('crimedata.csv')

app.layout = html.Div([

    #1
    html.Div([
        html.H3("1. Зависимость количества жестоких и нежестоких преступлений от уровня образования населения"),
        html.H4(
            "Легенда: мне показалось интересным посмотреть, есть ли зависимость количества преступлений от образованности людей. В частности, "
            "наблюдается ли в штатах с высоким уровнем людей без высщего образования или даже незакончишвих школу большее количество мелких нежестоких преступлений"),

        dcc.Graph(id='graph-education-grade'),
        dcc.Checklist(
            options=list(df['state'].unique()),
            value=list(df['state'].unique()),
            inline=True,
            id='state-check'
        ),
        dcc.RadioItems(
            options={'PctLess9thGrade': 'Less then 9th grade',
            'PctNotHSGrad': 'Without high school graduates',
            'PctBSorMore': 'Bachelors degree or higher education'},
            value= 'PctLess9thGrade',
            id='education-type',
            labelStyle={'display': 'inline-block', 'marginTop': '5px'}
        ),

        html.H4(
            "Результат: явной обратной зависимости 'уровень образования - уровень преступности' выявить по нашим данным не удалось, однако было замечено, что во многих"
            " штатах с высоким уровнем нежестоких преступлений процент людей со средним образованием больше процента людей с высшим образованиeм "
            "\n"),
    ]),

    #2
    html.Div([
        html.H3(
            "2. Зависимость количества жестоких и нежестоких преступлений от владения языком"),
        html.H4(
            "Легенда: продолжая разговор об образовании, хочется посмотреть на зависимость владения языками и уровнем преступности. Интуитивно кажется, что люди"
            " плохо владеющие английским в Америке - это в основном иммигранты, которым тяжело устроиться на хорошо-оплачиваемую работу из-за незнания языка,"
            "а значит в теории могут зарабатывать на жизнь незаконными способами - это нас и интересует"
            " А люди, которые владею только родным языком - опять же говорят об уровне образования (ничего против не имею, это не буллинг, лишь гипотезы)"),


        dcc.Graph(id='graph-English proficiency'),
        dcc.Checklist(
            options=list(df['state'].unique()),
            value=list(df['state'].unique()),
            inline=True,
            id='state-check-type'
        ),
        dcc.RadioItems(
            options={'PctSpeakEnglOnly': 'People who speak english only',
            'PctNotSpeakEnglWell': 'People who dont speak English well'},
            value= 'PctSpeakEnglOnly',
            id='language-type',
            labelStyle={'display': 'inline-block', 'marginTop': '5px'}
        ),

        html.H4(
            "Результат: зависимость выявить не удалось, можем считать гипотезу неподтвердившейся "),

    ]),

    #3
    html.Div([
        html.H3(
            "3. Зависимость количества различных преступлений от количества проживающих людей в комнате/количества спален"),
        html.H5("P.s. Данный график вдохновлен совместным проживанием в одной комнате c братьями/сёстрами "),
        html.H4(
            "Легенда: Разумеется, это отчасти сатирический график, но, в целом, большое количество людей в комнате и малое количество спален говорит о "
            "низких доходах, а значит может быть связано с высоким уровнем преступности"),

        dcc.Dropdown(
                ['murdPerPop', 'rapesPerPop', 'robbbPerPop', 'assaultPerPop', 'burglPerPop', 'larcPerPop',
                'autoTheftPerPop', 'arsonsPerPop'],
                'murdPerPop',
                id='crime_type'
            ),

        dcc.Graph(id='graph-living-comfort'),
        dcc.Checklist(
            options=list(df['state'].unique()),
            value=list(df['state'].unique()),
            inline=True,
            id='state'
        ),

        html.H4(
            "Результат: моей целью было посмотреть, больше ли убийств совершается в штатах, где люди чаще живут с кем-то в комнате (но, я и без всяких"
            " графиков уверена, что так оно и есть). В целом, можно заметить, что в штатах, где люди чаще делят комнату с кем-то совершается больше нетяжких"
            " престулпений вида автокража-нападение-грабеж-поджог. И, кстати, меня удивило, что во всех штатаъ примерно одинаковый уровень домов с < 3 спальянми, поэтому"
            " на этот показатель ориентироваться не пришлось, зато второй признак оказался дельным"),

    ]),

    #4
    html.Div([
        html.H3(
            "4. Зависимость количества различных преступлений от вида заработка"),
        html.H4(
            "Легенда: Мне кажется, что вид дохода семьи может влиять на уровень преступности, особенно если основным доходом являются государственные субсидии"),

        dcc.RadioItems(
            options={'pctWWage': 'Salary income',
            'pctWSocSec': 'Social security income', 'pctWPubAsst' : 'Public assistance income', 'pctWRetire': 'Retirement income'},
            value= 'pctWWage',
            id='income-type'),

        dcc.Dropdown(
            ['murdPerPop', 'rapesPerPop', 'robbbPerPop', 'assaultPerPop', 'burglPerPop', 'larcPerPop',
             'autoTheftPerPop', 'arsonsPerPop'],
            'murdPerPop',
            id='crime'
        ),

        dcc.Graph(id='graph-income-type'),
        dcc.Checklist(
            options=list(df['state'].unique()),
            value=list(df['state'].unique()),
            inline=True,
            id='stat'
        ),

        html.H4(
            "Результат: В целом, можно заметить тенденцию, что в штатах, где больше людей, у которых доход - это зарплата или пенсия, ниже уровень"
            " преступности и наоборот в штатах с высокими уровнями выплат социальной помощи"),
    ]),

    #5
    html.Div([
        html.H3(
            "5. Зависимость количества людей, живущих за чертой бедности и совершенных преступлений"),
        html.H4(
            "Легенда: на десерт посмотрим на классику жанра - связь количества бедных людей и совершенных преступлений разных категорий "),


        dcc.Dropdown(
            ['murders', 'rapes', 'robberies', 'assaults', 'burglaries', 'larcenies', 'autoTheft', 'arsons'],
            'arsons',
            id='crimes'
        ),

        dcc.Graph(id='graph-poverty-level'),
        dcc.Checklist(
            options=list(df['state'].unique()),
            value=list(df['state'].unique()),
            inline=True,
            id='states'
        ),

        html.H4(
            "Результат: Однозначно есть зависимость, причем по всем видам преступлений"),
    ]),

])
#
#
@app.callback(
    Output('graph-education-grade', 'figure'),
    Input('state-check', 'value'),
    Input('education-type', 'value'))
def update_figure(selected_state, ed_type):
    fig = go.Figure()

    df0 = df[df.state.isin(selected_state)]
    df1 = df0.groupby('state')[ed_type].mean().reset_index()
    df1[ed_type] = df1[ed_type] #Приведем данные к единому масштабу на 100К человек
    df2 = df0.groupby('state')['ViolentCrimesPerPop'].mean().reset_index()
    df3 = df0.groupby('state')['nonViolPerPop'].mean().reset_index()

    df1 = df1.merge(df2, on="state")
    df1 = df1.merge(df3, on="state")

    fig.add_trace(go.Bar(x=df1['state'], y=df1[ed_type], name='education_type'))
    fig.add_trace(go.Bar(x=df1['state'], y=df1['ViolentCrimesPerPop'], name='violent_crimes'))
    fig.add_trace(go.Bar(x=df1['state'], y=df1['nonViolPerPop'], name='not_violent_crimes'))
    fig.update_xaxes(title="states")

    fig.update_layout(height=400, margin={'l': 50, 'b': 50, 'r': 100, 't': 30})
    return fig

#2
@app.callback(
    Output('graph-English proficiency', 'figure'),
    Input('state-check-type', 'value'),
    Input('language-type', 'value'))
def update_figure(selected_state, lang_level):
    fig = go.Figure()


    df0 = df[df.state.isin(selected_state)]
    df1 = df0.groupby('state')[lang_level].mean().reset_index()
    df1[lang_level] = df1[lang_level] * 100  #Приведем данные к единому масштабу на 100К человек
    df2 = df0.groupby('state')['ViolentCrimesPerPop'].mean().reset_index()
    df3 = df0.groupby('state')['nonViolPerPop'].mean().reset_index()


    df1 = df1.merge(df2, on="state")
    df1 = df1.merge(df3, on="state")


    fig.add_trace(go.Bar(x=df1['state'], y=df1[lang_level], name='language_profiency'))
    fig.add_trace(go.Bar(x=df1['state'], y=df1['ViolentCrimesPerPop'], name='violent_crimes'))
    fig.add_trace(go.Bar(x=df1['state'], y=df1['nonViolPerPop'], name='not_violent_crimes'))
    fig.update_xaxes(title="states")


    fig.update_layout(height=400, margin={'l': 50, 'b': 50, 'r': 100, 't': 30})
    return fig

#3
@app.callback(
    Output('graph-living-comfort', 'figure'),
    Input('state', 'value'),
    Input('crime_type', 'value'))
def update_figure(selected_state, crime):
    fig = go.Figure()

    df0 = df[df.state.isin(selected_state)]
    df1 = df0.groupby('state')[crime].mean().reset_index()
    df2 = df0.groupby('state')['PctPersDenseHous'].mean().reset_index()
    df2['PctPersDenseHous'] = df2['PctPersDenseHous'] * 100  #Приведем данные к единому масштабу на 100К человек
    df3 = df0.groupby('state')['PctHousLess3BR'].mean().reset_index()
    df3['PctHousLess3BR'] = df3['PctHousLess3BR'] * 10

    df1 = df1.merge(df2, on="state")
    df1 = df1.merge(df3, on="state")

    fig.add_trace(go.Bar(x=df1['state'], y=df1[crime], name=crime))
    fig.add_trace(go.Bar(x=df1['state'], y=df1['PctHousLess3BR'], name='decades houses with < 3 bedrooms'))
    fig.add_trace(go.Bar(x=df1['state'], y=df1['PctPersDenseHous'], name='people who dont living alone in room'))

    fig.update_layout(height=400, margin={'l': 50, 'b': 50, 'r': 100, 't': 30})
    return fig

#4
@app.callback(
    Output('graph-income-type', 'figure'),
    Input('stat', 'value'),
    Input('income-type', 'value'),
    Input('crime', 'value'))
def update_figure(selected_state, crime, income):
    fig = go.Figure()

    df0 = df[df.state.isin(selected_state)]
    df1 = df0.groupby('state')[crime].mean().reset_index()
    df2 = df0.groupby('state')[income].mean().reset_index()
    df2[income] = df2[income] / 10

    df1 = df1.merge(df2, on="state")

    fig.add_trace(go.Bar(x=df1['state'], y=df1[crime], name='crime'))

    fig.add_trace(go.Bar(x=df1['state'], y=df1[income], name='thousands households with this income type'))

    fig.update_layout(height=400, margin={'l': 50, 'b': 50, 'r': 100, 't': 30})
    return fig

#5
@app.callback(
    Output('graph-poverty-level', 'figure'),
    Input('states', 'value'),
    Input('crimes', 'value'))
def update_figure(selected_state, crime):
    fig = go.Figure()

    df0 = df[df.state.isin(selected_state)]
    df1 = df0.groupby('state')[crime].mean().reset_index()
    df2 = df0.groupby('state')['NumUnderPov'].mean().reset_index()
    df2['NumUnderPov'] = df2['NumUnderPov'] / 100

    df1 = df1.merge(df2, on="state")

    fig.add_trace(go.Bar(x=df1['state'], y=df1[crime], name=crime))
    fig.add_trace(go.Bar(x=df1['state'], y=df1['NumUnderPov'], name='hundreds of people under the poverty level'))

    fig.update_layout(height=400, margin={'l': 50, 'b': 50, 'r': 100, 't': 30})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
