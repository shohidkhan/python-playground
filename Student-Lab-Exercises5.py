is_active = True
cpu_percent = 94.5
is_production = True

should_alert = (not is_active ) or (cpu_percent > 90 and is_production)
# print (should_alert)

if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")
