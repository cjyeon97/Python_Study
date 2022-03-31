import pandas as pd

df = pd.read_csv('Submit.csv')

def find_submit(payer_id, ins_com):
    result = {}
    result['ins_com'] = ins_com
    df_filtered1 = df[df['PayerID'] == payer_id]
    result['Submission'] = df_filtered1['NET7'].sum()

    df_filtered_paid = df[(df['PayerID'] == payer_id) & (df['Paid']=='O')]
    result['Paid'] = df_filtered_paid['PaymentAmount'].sum()

    df_filtered_paid = df[(df['PayerID'] == payer_id) & (df['Reject']=='O')]
    result['Reject'] = df_filtered_paid['NET7'].sum()

    df_filtered_reject = df[(df['PayerID'] == payer_id) & (df['Pending']=='O') & (df['Days']>=46)]
    result['Pending'] = df_filtered_reject['NET7'].sum()
    return result

report = []
report.append(find_submit('INS026', 'DAMAN'))
report.append(find_submit('INS078', "THIQA"))

df_result = pd.DataFrame(report)

print(df_result)
df_result.to_excel("output.xlsx", sheet_name='Sheet_name_1')

