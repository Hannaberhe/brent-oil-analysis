# Brent Oil Price Analysis Plan

## Analysis Steps
1. Load and clean Brent oil price data (1987-2022)
2. Research and compile major geopolitical and economic events
3. Perform EDA: trends, volatility, log returns
4. Build Bayesian change point model using PyMC
5. Identify structural breaks in price series
6. Associate detected change points with documented events
7. Quantify impact of each major event on prices
8. Build Flask API and React dashboard for visualization

## Assumptions
- Events have a causal impact on oil prices
- Change points in the time series correspond to real world events
- The model can detect significant structural breaks

## Limitations
- Correlation does not equal causation
- Multiple events may occur simultaneously making attribution difficult
- Market reactions may be delayed or anticipatory
- The model assumes a simple before/after mean change

## Communication Channels
- Final report as Medium blog post
- Interactive dashboard for stakeholders
- GitHub repository for technical audience
