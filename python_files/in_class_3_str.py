import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb # optional to set plot theme
sb.set_theme() # optional to set plot theme
import yfinance as yf

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()


    def get_data(self):
        
        if end_date is None:
            end_date = datetime.today().strftime('%Y-%m-%d')
        if start_date is None:
            start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
    
        data = yf.download(symbol, start=start_date, end=end_date)
        data.index = pd.to_datetime(data.index)
        self.calc_returns(data)
        return data
        pass

    
    def calc_returns(self, df):
        
        df['change'] = df['Close'].diff().round(4)
        df['instant_return'] = np.log(df['Close'] / df['Close'].shift(1)).round(4)
        
        pass

    
    def plot_return_dist(self):
        
        valid_returns = df['instant_return'].dropna()
        plt.figure(figsize=(10, 6))  
        plt.hist(valid_returns, bins=50, alpha=0.7, color='blue')  
        plt.title('Histogram of Instantaneous Returns')  
        plt.xlabel('Instantaneous Return')  
        plt.ylabel('Frequency')  
        plt.grid(axis='y', alpha=0.75)  
        plt.axvline(valid_returns.mean(), color='red', linestyle='dashed', linewidth=1)  
        plt.text(valid_returns.mean() * 1.1, max(plt.hist(valid_returns, bins=50)[0]) * 0.9, f'Mean: {valid_returns.mean():.4f}', color='red')  
        plt.show()
        pass


    def plot_performance(self):
        
        initial_close = df['Close'].iloc[0]
        df['percent_change'] = ((df['Close'] - initial_close) / initial_close) * 100
    
        plt.figure(figsize=(10, 6))  
        plt.plot(df.index, df['percent_change'], label='Percent Change', color='green')  
        plt.title('Stock Performance: Percent Gain/Loss')  
        plt.xlabel('Date')  
        plt.ylabel('Percent Change') 
        plt.axhline(0, color='black', linewidth=0.5)  
        plt.grid(axis='both', alpha=0.3)  
        plt.legend() 
        plt.show()
        pass
                  



def main():
    # uncomment (remove pass) code below to test
    test = Stock(symbol=[stock_symbol]) # optionally test custom data range
    print(test.data)
    test.plot_performance()
    test.plot_return_dist()
    pass

if __name__ == '__main__':
    main() 