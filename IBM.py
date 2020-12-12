'''
Ερώτημα 1
'''
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

#%%
# reading csv file 
df = pd.read_csv("C:/Users/Στέφανος/Desktop/IBM/IBM.csv",sep=",")
df.head()
#%%
'''
Ερώτημα 2
'''

df["Day_Var"] = ((df["Close"] - df["Open"]) / df["Open"])* 100

writer = pd.ExcelWriter('New Data.xlsx')
df.to_excel(writer, sheet_name = 'Day Var' , index = False)
writer.save()

pd.read_excel('New Data.xlsx', index_col=0)
df.head()
#%%
'''
Ερώτημα 3
'''

Date = df['Date']
Date

Day_Var = df['Day_Var']
Day_Var

df1 = pd.DataFrame({'Date':Date , 'Day_Var': Day_Var})
df1

count = df1.groupby('Day_Var').count()
count

print(count.max())
#%%
Date = df1['Date']  
Day_Var = df1['Day_Var']    
    
df1 = pd.DataFrame({'Date':Date , 'Day_Var': Day_Var})
print(df1)
    
count = df1.groupby('Day_Var').count()
print(count)
print("\n---------------------------------------\n\n Day Counter / var : ",count.max())

plt.figure(figsize=(17,5))
plot = df1.groupby('Day_Var').count().plot()
plot
bins = (df1['Day_Var'].max() - df1['Day_Var'].min()) * 10
bins = int(bins)
        
xmin,xmax = plt.xlim()
xmax = df1["Day_Var"].max()
xmin = df1["Day_Var"].min()
max_day = list(df1.iloc[df1['Day_Var'].argmax()])
min_day = list(df1.iloc[df1['Day_Var'].argmin()])

print(f'\n H τελευταία μέρα που πουρουσιάστηκε η μεγαλύτερη διακύμαση είχε ημ/νία και τιμή :{max_day}')
print(f'\n H τελευταία μέρα που πουρουσιάστηκε η μικρότερη διακύμαση είχε ημ/νία και τιμή :{min_day}')

plt.annotate(f'Xmax={round(xmax,3)}', xy=(xmax,0), xytext=(5, 150), fontsize=10,\
             arrowprops={'width':0.3,'headwidth':5,'color':'#333333'})

plt.annotate(f'Xmin={round(xmin,3)}', xy=(xmin,0), xytext=(-20, 150), fontsize=10,\
             arrowprops={'width':0.3,'headwidth':5,'color':'#333333'})

max_day = list(df1.iloc[df1['Day_Var'].argmax()])
min_day = list(df1.iloc[df1['Day_Var'].argmin()])
plt.text(20,200,"Last Day MaxVar:" + max_day[0] +"\n" + "\nLast Day MinVar:"+ min_day[0],fontsize=15)
#%%
'''
Ερώτημα 4
'''

mean, std= norm.fit(Day_Var)
print(f'\n mean = {mean} & std = {std}')
    
mean, std= norm.fit(df1["Day_Var"])
plt.figure(figsize=(17,5))
plt.hist(df['Day_Var'], bins=bins, density=True, alpha=0.3, color='r',linewidth=4)
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)
plt.plot(x, p, 'k', linewidth=2)
title = " IBM Rates - Year : {1962 - 2020} \nIBM Fit results: mean = %.4f, std= %.4f" % (mean, std)
#plt.savefig(' histogram - 2.png', dpi=300)
plt.title(title)

xmin,xmax = plt.xlim()
xmax = df["Day_Var"].max()
xmin = df["Day_Var"].min()
max_day = list(df.iloc[df['Day_Var'].argmax()])
min_day = list(df.iloc[df['Day_Var'].argmin()])

print(f'\n H τελευταία μέρα που πουρουσιάστηκε η μεγαλύτερη διακύμαση είχε ημ/νία και τιμή :{max_day}')
print(f'\n H τελευταία μέρα που πουρουσιάστηκε η μικρότερη διακύμαση είχε ημ/νία και τιμή :{min_day}')

plt.annotate(f'Xmax={round(xmax,3)}', xy=(xmax,0), xytext=(5, 0.2), fontsize=15, arrowprops={'width':0.3,'headwidth':5,'color':'#333333'})
plt.annotate(f'Xmin={round(xmin,3)}', xy=(xmin,0), xytext=(-20, 0.2), fontsize=15, arrowprops={'width':0.3,'headwidth':5,'color':'#333333'})


max_day = list(df.iloc[df['Day_Var'].argmax()])
min_day = list(df.iloc[df['Day_Var'].argmin()])
plt.text(-20,0.4,"Last Date MaxVar:" + max_day[0] +"\n" + "\nLast Date of MinVar:"+ min_day[0],fontsize=15)
plt.show()

#%%
'''
Ερώτημα 5
'''
import pandas as pd
import pandas_datareader.data as web
import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

start = datetime.datetime(1980,1,1)
stop = datetime.datetime(2020,1,1)

print("\n---------------------------------------------\n\
*** Please fill find below IBM or S&P500 Stock Rates {1980 - 2020}\
\n---------------------------------------------\n ")

print("\n For IBM Rates please write : IBM\n For S&P500 Rates please write : SPY")

Stock_name = input("Insert a Stock - Name :")

print("\n---------------------------------------------\n\
*** Please wait few sec for the downloading of the data\
\n---------------------------------------------\n ")

while Stock_name != 'IBM'and Stock_name != 'SPY' :
    Stock_name = input("Insert a stock :")

if  Stock_name == 'IBM':
   
    df1 = web.DataReader("IBM",'yahoo',start,stop)
    df1.to_csv('IBM - Rates.csv')
    print("\n------- IBM - Rates.csv has been downloaded correctly ! -------")
    
     
        
    df1 = pd.read_csv('IBM - Rates.csv',sep=",")
    df1.head() 
    
    
        
    df1["Day_Var"] = ((df1["Close"] - df1["Open"]) / df1["Open"])* 100
    # df1["Day_Var"] = ((df1["Open"] - df1["Close"]) / df1["Open"])* 100

    writer = pd.ExcelWriter('New Data IBM.xlsx')
    df1.to_excel(writer, sheet_name = 'Day Var' , index = False)
    writer.save()    
     
    pd.read_excel('New Data IBM.xlsx', index_col=0)
    df1.head()

elif  Stock_name == 'SPY':
   
    df1 = web.DataReader("SPY",'yahoo',start,stop)
    df1.to_csv('SPY - Rates.csv')
    print("\n SPY - Rates.csv has been downloaded correctly !!!")
    
     
        
    df1 = pd.read_csv('SPY - Rates.csv',sep=",")
    df1.head() 
    
    
        
    df1["Day_Var"] = ((df1["Close"] - df1["Open"]) / df1["Open"])* 100
    # df1["Day_Var"] = ((df1["Open"] - df1["Close"]) / df1["Open"])* 100

    writer = pd.ExcelWriter('New Data SPY.xlsx')
    df1.to_excel(writer, sheet_name = 'Day Var' , index = False)
    writer.save()    
     
    pd.read_excel('New Data SPY.xlsx', index_col=0)
    df1.head()        

#%%

    Date = df1['Date']  
    Day_Var = df1['Day_Var']    
    
    df = pd.DataFrame({'Date':Date , 'Day_Var': Day_Var})
    print(df)
    
    count = df.groupby('Day_Var').count()
    print(count)
    print("\n---------------------------------------\n\n Day Counter / var : ",count.max())
    
      
    plot = df.groupby('Day_Var').count().plot()
    plot
    bins = (df['Day_Var'].max() - df['Day_Var'].min()) * 10
    
    bins = int(bins)
        
    xmin,xmax = plt.xlim()
    xmax = df["Day_Var"].max()
    xmin = df["Day_Var"].min()
    max_day = list(df.iloc[df['Day_Var'].argmax()])
    min_day = list(df.iloc[df['Day_Var'].argmin()])

    print(f'\n H τελευταία μέρα που πουρουσιάστηκε η μεγαλύτερη διακύμαση είχε ημ/νία και τιμή :{max_day}')
    print(f'\n H τελευταία μέρα που πουρουσιάστηκε η μικρότερη διακύμαση είχε ημ/νία και τιμή :{min_day}')
     
#     plt.annotate(f'Xmax={round(xmax,3)}', xy=(xmax,0), xytext=(5, 150), fontsize=15, arrowprops={'width':0.3,'headwidth':5,'color':'#333333'})
#     plt.annotate(f'Xmin={round(xmin,3)}', xy=(xmin,0), xytext=(-20, 150), fontsize=15, arrowprops={'width':0.3,'headwidth':5,'color':'#333333'})
    
    

    
    max_day = list(df.iloc[df['Day_Var'].argmax()])
    min_day = list(df.iloc[df['Day_Var'].argmin()])
#     plt.text(-13,230,"Last Date MaxVar:" + max_day[0] +"\n" + "\nLast Date of MinVar:"+ min_day[0],fontsize=15)
    plt.ylabel('Number of Days')
    plt.xlabel('The Day_Var %')
    plt.title(Stock_name + "-" + 'Histogram')
#%%

    # Normal Distribution Plot    

    mean, std= norm.fit(Day_Var)
    print(f'\n mean = {mean} & std = {std}')
    
    mean, std= norm.fit(df1["Day_Var"])
    plt.figure(figsize=(17,5))
    plt.hist(df['Day_Var'], bins=bins, density=True, alpha=0.3, color='r',linewidth=4)
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = Stock_name + " Fit results: mean = %.4f, std= %.4f" % (mean, std)
    #plt.savefig(' histogram - 2.png', dpi=300)
    plt.title(title)

    xmin,xmax = plt.xlim()
    xmax = df["Day_Var"].max()
    xmin = df["Day_Var"].min()
    max_day = list(df.iloc[df['Day_Var'].argmax()])
    min_day = list(df.iloc[df['Day_Var'].argmin()])

    print(f'\n H τελευταία μέρα που πουρουσιάστηκε η μεγαλύτερη διακύμαση είχε ημ/νία και τιμή :{max_day}')
    print(f'\n H τελευταία μέρα που πουρουσιάστηκε η μικρότερη διακύμαση είχε ημ/νία και τιμή :{min_day}')

    plt.annotate(f'Xmax={round(xmax,3)}', xy=(xmax,0), xytext=(7, 0.2), fontsize=15, arrowprops={'width':0.3,'headwidth':5,'color':'#333333'})
    plt.annotate(f'Xmin={round(xmin,3)}', xy=(xmin,0), xytext=(-7, 0.2), fontsize=15, arrowprops={'width':0.3,'headwidth':5,'color':'#333333'})


    max_day = list(df.iloc[df['Day_Var'].argmax()])
    min_day = list(df.iloc[df['Day_Var'].argmin()])
    plt.text(5,0.4,"Last Day MaxVar:" + max_day[0] +"\n" + "\nLast Day MinVar:"+ min_day[0],fontsize=15)
    












