from services.batch_optimizer import process_query_logs

results = process_query_logs()

for row in results:
    print(row)