#Preparing data for time series
def create_timeseries_data(df):
    import pandas as pd
    from writeto_onedrive import write_to_onedrive

    print("Fetching Triage Datetime")
    df = df[['TRIAGE_DATETIME']]
    df.columns = df.columns.str.title()

    write_to_onedrive(df, 'time_series_data.xlsx')

