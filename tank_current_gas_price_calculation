def current_gas_cost_calculate(litters, prices, current_litters):
    for i in range(len(litters)):
        litters_last_visit = litters[i]
        price_unit_last_visit = prices[i] / litters[i]
        if current_litters <= litters_last_visit:
            return current_litters*price_unit_last_visit
        else:
            rest_litters = current_litters-litters_last_visit
            return current_gas_cost_calculate(litters[1:], prices[1:], rest_litters) + litters_last_visit*price_unit_last_visit


quantity_records = [3,4,6,8,6,8,6,8]
prices_records = [6,8,12,16,12,16,12,16]
gauge_current_litter_indicator = 20

print(current_gas_cost_calculate(quantity_records, prices_records, gauge_current_litter_indicator))
