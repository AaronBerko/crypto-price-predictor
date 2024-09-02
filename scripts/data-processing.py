#Imports 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Clean the data: I would od this but my dataset has no missing values

#Display the clean data
def display_clean_data(dataframe):
    plt.figure(figsize=(10,6))
    plt.title("Historical Close of Bitcoin from Sept 14, 2014 to Sept 2 2024")
    plt.xlabel("Date")
    plt.ylabel("Bitcoin Close Price (USD)") 
    plt.plot(dataframe['Close'], label = 'Close Price')
    plt.plot(dataframe['Open'], label = 'Open Price')
    plt.plot(dataframe['High'], label = 'High Price')
    plt.plot(dataframe['7_Day_MA'], label = '7 Day Moving Avg')
    plt.plot(dataframe['1_Month_MA'], label = '1 Month Moving Avg')
    plt.grid()
    plt.legend()
    plt.show()

#Save the data

def main():
    #Load in the financial data from the data folder
    raw_data_path = "../data/BTC-USD.csv"
    fin_data = pd.read_csv(raw_data_path, index_col='Date', parse_dates=True)
    
    #Create Moving Avg frame to help level the price data over a specified time
    fin_data['7_Day_MA'] = fin_data['Close'].rolling(window=7).mean()
    fin_data['1_Month_MA'] = fin_data['Close'].rolling(window=30).mean()

    #Display the clean data 
    display_clean_data(fin_data)
    
if __name__=="__main__":
    main()