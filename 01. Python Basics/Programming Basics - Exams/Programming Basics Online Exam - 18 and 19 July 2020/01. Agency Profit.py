agency_name = input()
adult_tickets_count = int(input())
children_tickets_count = int(input())
adult_ticket_price = float(input())
service_tax = float(input())

children_ticket_price = adult_ticket_price * 0.3 + service_tax
adult_ticket_price += service_tax

total_price = (adult_ticket_price * adult_tickets_count + children_ticket_price * children_tickets_count) * 0.2

print(f'The profit of your agency from {agency_name} tickets is {total_price:.2f} lv.')