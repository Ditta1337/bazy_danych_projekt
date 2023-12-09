from datetime import datetime, timedelta

def generate_dates(date_range_start, date_range_end, n):
    start_date = datetime.strptime(date_range_start, "%Y-%m-%d")
    end_date = datetime.strptime(date_range_end, "%Y-%m-%d")

    time_difference = end_date - start_date

    interval = time_difference / (n - 1) if n > 1 else timedelta(days=0)

    generated_dates = [start_date + i * interval for i in range(n)]

    result_dates = [date.strftime("%Y-%m-%d") for date in generated_dates]

    return result_dates