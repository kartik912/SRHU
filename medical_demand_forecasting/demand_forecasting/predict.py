import matplotlib
import pandas as pd

class predict_class :
    def pred():
        expiration_df = pd.read_csv('D:\Projects\code_quest_202\SRHU\medical_demand_forecasting\demand_forecasting\data\pharmacyDatasetEx.csv')
        purchase_df = pd.read_csv('D:\Projects\code_quest_202\SRHU\medical_demand_forecasting\demand_forecasting\data\pharmacyDatasetpurchase.csv')
        sales_df = pd.read_csv('D:\Projects\code_quest_202\SRHU\medical_demand_forecasting\demand_forecasting\data\pharmacyDatasetSales.csv')

        print(sales_df.shape)
        print(purchase_df.shape)
        print(expiration_df .shape)


        new_df = pd.DataFrame()
        new_df['winter'] = sales_df[['January_sales', 'December_sales', 'November_sales']].sum(axis=1)

        # Create a DataFrame from sales_df containing only 'drug_name' and 'drug_type' columns
        drug_info_df = sales_df[['drug_name', 'drug_type']]

        # Concatenate new_df and drug_info_df along the columns axis
        new_df = pd.concat([new_df, drug_info_df], axis=1)

        print(new_df)

        new_df_s = pd.DataFrame()
        new_df_s['summer'] = sales_df[['May_sales', 'June_sales', 'July_sales']].sum(axis=1)

        # Create a DataFrame from sales_df containing only 'drug_name' and 'drug_type' columns
        drug_info_df = sales_df[['drug_name', 'drug_type']]

        # Concatenate new_df and drug_info_df along the columns axis
        new_df_s = pd.concat([new_df_s, drug_info_df], axis=1)

        print(new_df_s)

        new_df_sp = pd.DataFrame()
        new_df_sp['spring'] = sales_df[['February_sales', 'March_sales', 'April_sales']].sum(axis=1)

        # Create a DataFrame from sales_df containing only 'drug_name' and 'drug_type' columns
        drug_info_df = sales_df[['drug_name', 'drug_type']]

        # Concatenate new_df and drug_info_df along the columns axis
        new_df_sp = pd.concat([new_df_sp, drug_info_df], axis=1)

        print(new_df_sp)

        new_df_aut = pd.DataFrame()
        new_df_aut['autum'] = sales_df[['August_sales', 'September_sales', 'October_sales']].sum(axis=1)

        # Create a DataFrame from sales_df containing only 'drug_name' and 'drug_type' columns
        drug_info_df = sales_df[['drug_name', 'drug_type']]

        # Concatenate new_df and drug_info_df along the columns axis
        new_df_aut = pd.concat([new_df_aut, drug_info_df], axis=1)

        print(new_df_aut)

        sorted_df_winter = new_df.sort_values('winter',ascending=False)
        sorted_df_summer = new_df_s.sort_values('summer',ascending=False)
        sorted_df_spring = new_df_sp.sort_values('spring',ascending=False)
        sorted_df_autum = new_df_aut.sort_values('autum',ascending=False)

        s= []
        w= []
        aut = []
        sp = []
        seasons = {
            'winter': sorted_df_winter,
            'summer': sorted_df_summer,
            'autumn': sorted_df_autum,
            'spring': sorted_df_spring
        }


        for _, row in sorted_df_winter.iterrows():
            w.append(row['drug_name'])
        for _, row in sorted_df_summer.iterrows():
            s.append(row['drug_name'])
        for _, row in sorted_df_spring.iterrows():
            sp.append(row['drug_name'])
        for _, row in sorted_df_autum.iterrows():
            aut.append(row['drug_name'])

        print(s)
        print(w)
        print(sp)
        print(aut)

        summer = []
        winter = []
        autumn = []
        spring = []
        for i in range(0,10):
            summer.append(s[i])
        for i in range(11,20):
            winter.append(w[i])
        for i in range(21,30): 
            spring.append(sp[i])
        for i in range(31,40):
            autumn.append(aut[i])

        return summer, winter, autumn, spring

