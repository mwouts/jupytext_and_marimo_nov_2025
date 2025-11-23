import marimo

__generated_with = "0.18.0"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # World Population Evolution

    This notebook visualizes the evolution of world population by continent using World Bank data.
    """)
    return


@app.cell
def _():
    import plotly.express as px
    import plotly.graph_objects as go
    return (px,)


@app.cell
def _(pd):
    # Load World Bank population data
    # Using the World Bank API or pre-downloaded data
    url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
    df = pd.read_csv(url)
    return (df,)


@app.cell
def _(df):
    # Display the first few rows
    df.head()
    return


@app.cell
def _():
    # Map countries to continents
    continent_mapping = {
        'Asia': ['China', 'India', 'Indonesia', 'Pakistan', 'Bangladesh', 'Japan', 'Philippines', 
                 'Vietnam', 'Turkey', 'Iran', 'Thailand', 'Myanmar', 'South Korea', 'Iraq', 'Afghanistan',
                 'Saudi Arabia', 'Malaysia', 'Nepal', 'Yemen', 'North Korea'],
        'Africa': ['Nigeria', 'Ethiopia', 'Egypt', 'Congo', 'Tanzania', 'South Africa', 'Kenya', 
                   'Uganda', 'Algeria', 'Sudan', 'Morocco', 'Angola', 'Ghana', 'Mozambique', 'Madagascar'],
        'Europe': ['Russia', 'Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Ukraine', 
                   'Poland', 'Romania', 'Netherlands', 'Belgium', 'Greece', 'Portugal', 'Sweden'],
        'North America': ['United States', 'Mexico', 'Canada', 'Guatemala', 'Cuba', 'Haiti', 
                          'Dominican Republic', 'Honduras', 'Nicaragua', 'El Salvador'],
        'South America': ['Brazil', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Chile', 
                          'Ecuador', 'Bolivia', 'Paraguay', 'Uruguay'],
        'Oceania': ['Australia', 'Papua New Guinea', 'New Zealand', 'Fiji']
    }

    # Create reverse mapping
    country_to_continent = {}
    for continent, countries in continent_mapping.items():
        for country in countries:
            country_to_continent[country] = continent
    return (country_to_continent,)


@app.cell
def _(country_to_continent, df):
    # Add continent column
    df['Continent'] = df['Country Name'].map(country_to_continent)

    # Filter out rows without continent mapping
    df_continents = df[df['Continent'].notna()].copy()
    return (df_continents,)


@app.cell
def _(df_continents):
    # Group by year and continent
    population_by_continent = df_continents.groupby(['Year', 'Continent'])['Value'].sum().reset_index()
    return (population_by_continent,)


@app.cell
def _(population_by_continent, px):
    # Create stacked area chart
    fig = px.area(
        population_by_continent,
        x='Year',
        y='Value',
        color='Continent',
        title='World Population Evolution by Continent',
        labels={'Value': 'Population', 'Year': 'Year'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_layout(
        hovermode='x unified',
        yaxis_title='Population',
        xaxis_title='Year',
        legend_title='Continent'
    )

    fig.show()
    return


@app.cell
def _(population_by_continent):
    # Summary statistics
    print("\nTotal Population by Continent (Most Recent Year):")
    latest_year = population_by_continent['Year'].max()
    latest_data = population_by_continent[population_by_continent['Year'] == latest_year]
    print(latest_data.sort_values('Value', ascending=False).to_string(index=False))
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()