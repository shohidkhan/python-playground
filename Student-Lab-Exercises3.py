
def estimate_deployment_cost(instance_count, hourly_rate_per_instance, budget_cap):
    thirty_day_hours = 30 * 24
    monthly_cost = instance_count * hourly_rate_per_instance * thirty_day_hours

    if monthly_cost > budget_cap:
        return f"REJECTED: Budget Exceeded by ${monthly_cost - budget_cap:.2f}!"
    else:
        return (
            f"APPROVED: Total Estimated Cost is ${monthly_cost:.2f} "
            f"for {instance_count} instances at "
            f"${hourly_rate_per_instance:.2f}/hour."
        )

print(estimate_deployment_cost(5, 0.45, 1500.00))
print(estimate_deployment_cost(12, 0.85, 5000.00))
