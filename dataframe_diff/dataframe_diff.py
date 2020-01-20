def dataframe_diff(df_x,df_y,key):
    import pandas as pd
    set_x=['df_x' for i in range(len(df_x))]
    df_x['sets']=set_x
    set_y=['df_y' for i in range(len(df_y))]
    df_y['sets']=set_y
    columns=list(df_x.columns)
    columns.remove('sets')
    df_concat=pd.concat([df_x,df_y]).drop_duplicates(subset=columns,keep=False).reset_index(drop=True)
    df_set1=df_concat[df_concat['sets']=='df_x']
    df_set2=df_concat[df_concat['sets']=='df_y']
    df_merged=pd.merge(df_set1, df_set2, on=key)
    nonkey=set(columns)- set(key)
    list_diff=[]
    for i in range(len(df_merged)):
        for col in nonkey:
            if df_merged.iloc[i][col + '_x'] != df_merged.iloc[i][col + '_y']:
                list_diff.append(list(df_merged.iloc[i][key + [col + '_x',col + '_y']]) + [col])
    df_diff=pd.DataFrame(list_diff,columns=key + ['value' + '_x','value' + '_y' ,'column_name'] )
    df_additional = pd.concat([df_x,df_y]).drop_duplicates(subset=key,keep=False).reset_index(drop=True)
    df_x.drop(['sets'],axis=1,inplace=True)
    df_y.drop(['sets'],axis=1,inplace=True)
    return df_diff,df_additional
