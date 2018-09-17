import pandas as pd

user_usage = pd.read_csv("user_usage.csv")
user_device = pd.read_csv("user_device.csv")
devices = pd.read_csv("android_devices.csv")
devices.rename(columns={"Retail Branding": "manufacturer"}, inplace=True)
user_usage.head()
user_device.head()
devices.head(10)
result = pd.merge(user_usage, user_device[['use_id', 'platform', 'device']], on='use_id')
result.head()
#  First, add the platform and device to the user usage
result = pd.merge(user_usage, user_device[['use_id', 'platform', 'device']], on='use_id', how='left')

#  Now, based on the "device"  column in result, match the "Model" column in devices.
devices.rename(columns={"Retail Branding": "manufacturer"}, inplace=True)
result = pd.merge(result, devices[['manufacturer', 'Model']], left_on='device', right_on='Model', how='left')
result.head()
