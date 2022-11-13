# A Game Theoretic Approach to Stock Market Modelling 
This Project contains coevolutionary and genetic algorithms to predict profitable strategies for better payoff amongst players (agents/stockbrokers) in a stock market game. The players are the stockbroker agents (investing on behalf of a population of agents, while charging an amount for each profit). Either of the two strategies -> Buy/Sell stocks based on a stock of a single company are generated. Genetic and Coevolutionary algorithms are used to formulate the optimal strategy (rule-base matrix M, read report), from previous market data.

# Description of the Project
A stock market is a diversified hub of agents trying to make profits, while contributing to several companies based on the utility of their projects and stocks. A stock/equity/share is essentially a piece of ownership/security of a company's inventory. When a company is private, only a few stakeholders are present and the inventory is low. So, the shares of the company based on the inventory required is made public at IPO (Initial Public Offering). The company enters the stock-market, in any registered national stock exchange (in India, NSE/BSE). 

E.g. The image below depicts the HDFC Bank NSE Shares Price Dated 6:40 pm, 13th November, 2022

![HDFC Bank NSE Shares Price](https://drive.google.com/uc?export=view&id=1i2jfkNY_apzGx2z045vVG3hkIkT9ZvNn#center) 

An agent is a player in a stock market who has either of the strategies - buy, hold or sell stocks of any company. A stockbroker agent acts as a _"middleman"_ in the investment process. Having charged a small percentage from the profits made by an agent, he acts as an investment/financial adviser for strategising investments for optimal profit. Thus, the entire process can be viewed as a complex game.

Our project aims at modelling the behaviour of players (agents) in a stock market using an Evolutionary Game Theoretic Approach. The Players are the stockbroker agents (playing on behalf of the actual agents). The strategies are buying or selling of stocks. For simplicity, stocks of only one company at a time are transacted upon.

# Building and Execution

Both the FuzzyLogic and CoevolutionaryAlgo files are python scripts (.py extension). Python3 is used for the scripts, hence, it has to be installed.

## Installation of Python

- Navigate to [Python Official Website](https://www.python.org/downloads/).
- Select the OS installed on your system.
- Download the Python Installer Package.
- Follow the steps to install python and set its environment up on your system.

## Installation of required packages

We have used the following external packages for building our scripts - 
1. Pandas : For parsing stock data smoothly from csv files
2. Matplotlib : For visualising the wealth of each player on plots
3. Numpy : For using numpy standard arrays as against Python heterogenous lists

In order to install these packages, follow these steps -

1. Open the terminal on your system.
2. Execute the following command/script in a .bat file - `pip install pandas & pip install numpy & pip install maplotlib`

## Stock Data Download

For downloading the stock data (of the past year, or 5 years, etc.), follow the steps - 
1. Navigate to [Nasdaq Official Website](https://www.nasdaq.com/). Create an account on Nasdaq.
2. Go to [Nasdaq Composite Index](https://www.nasdaq.com/market-activity/index/comp). Select _Historical_.
3. Click on Download Data. It will download the data as a .csv file.
4. Move the file to the same folder where the python scripts are present.
5. Open the .csv file and change the header of 'Close/Last' to just 'Close'.
6. Change the file name in line 12 of the _CoevolutionaryAlgo.py_ script to the csv file name.

## Running the Script

For executing the python scripts, follow these steps -
1. Make sure both scripts - _FuzzyLogic.py_ and _CoevolutionaryAlgo.py_ are present in the same directory and the .csv Data files too. 
2. An IDE can be used with required Python extensions to build and run the code at the same time. In that case, just run the CoevolutionaryAlgo.py script. 
3. If an IDE is not present, run the following command on your terminal after navigating to the directory - `python .\CoevolutionaryAlgo.py `.
4. A plot will  be displayed on Matplotlib api window.

The plot will be of an alpha population (red), an omega population (green) and an ordinary population (blue). Along with this, a black plot (of stock price data) will be present.

The alpha population and omega population follow the coevolutionary as well as genetic algorithm strategy, which evolve with market data and experience. The ordinary population doesn't evolve and so has on average a lower pay-off after playing for around 10-20 generations, each generation involving consecutive trading for 70 days.
