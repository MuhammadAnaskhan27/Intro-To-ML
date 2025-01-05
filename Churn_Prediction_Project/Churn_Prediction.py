import pandas as pd

# Load the dataset
url = "https://github.com/YBIFoundation/Dataset/raw/main/TelecomCustomerChurn.csv"
churn_df = pd.read_csv(url)

# Handle Missing Values
churn_df.fillna(churn_df.median(),inplace=True)

# Data Preprocessing