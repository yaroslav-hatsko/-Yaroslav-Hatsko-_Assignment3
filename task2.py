deposit_account = {
    "client_id": "C1025",
    "balance": 5000.0,
    "currency": "UAH",
    "interest_rate": 0.08,
    "is_active": True
}
balance = deposit_account["balance"]
interest_rate = deposit_account["interest_rate"]
interest_sum = balance*interest_rate
deposit_account["balance"] += interest_sum
deposit_account["last_update_type"] = "interest accrual"
deposit_account["is_active"] = False
print(deposit_account)