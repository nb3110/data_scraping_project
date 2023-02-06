import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import difflib



def str_match_index(df1,col1,df2,col2):
    """
    This function has as an input the name and desired index matching for 2 dataframes. Its outputs its the closest match between each string from dataframe 1
    and the series corresponding to dataframe 2
    """

    df1[col2] = df1[col1].copy()
    df1[col2] = df1[col2].apply(lambda x: difflib.get_close_matches(x, df2[col2]))
    df1[col2] = df1[col2].apply(lambda x: x[0] if len(x)>0 else "nan")
    return df1


def barplot_sns(data, x_index , y_index , pallete_type , title , xlabel , ylabel):
    """
    Plot barplot in seaborn defining titles and standard formatting for this report
    """
    sns.barplot(data=data, x= x_index, y= y_index , palette=pallete_type )
    plt.title(title, size=18, weight='bold', pad=30)
    plt.xlabel(xlabel,size=15, weight='bold')
    plt.ylabel(ylabel,size=15, weight='bold')
    return plt.show()


def summary_statistics(df):
    df.info()
    #nulls for only numerical values
    print("\n ############### NULL % ################\n")
    df[df.columns].isnull().sum()/(df.shape[0])

    print("\n ############### Numerical Variables Sumarry Statistics ################\n")
    df.describe().round(2)