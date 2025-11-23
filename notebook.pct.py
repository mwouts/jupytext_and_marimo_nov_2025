# %%
import pandas as pd

# %% [markdown]
# # World Population Evolution
#
# This notebook visualizes the evolution of world population by continent using World Bank data.

# %%
import plotly.express as px
import plotly.graph_objects as go

# %%
# Load World Bank population data
# Using the World Bank API or pre-downloaded data
url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
df = pd.read_csv(url)

# %%
# Display the first few rows
df.head()

# %%
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

# %%
# Add continent column
df['Continent'] = df['Country Name'].map(country_to_continent)

# Filter out rows without continent mapping
df_continents = df[df['Continent'].notna()].copy()

# %%
# Group by year and continent
population_by_continent = df_continents.groupby(['Year', 'Continent'])['Value'].sum().reset_index()

# %%
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

# %%
# Summary statistics
print("\nTotal Population by Continent (Most Recent Year):")
latest_year = population_by_continent['Year'].max()
latest_data = population_by_continent[population_by_continent['Year'] == latest_year]
print(latest_data.sort_values('Value', ascending=False).to_string(index=False))

# %%
