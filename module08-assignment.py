# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
services={"Web Development": 150, "Data Analysis": 120, "Animated Explainer Video": 220, "Content Creation": 90, "Troubleshooting Website": 140}

# TODO 2: Create customer dictionaries
customer1={"company_name": "Plex Web", "contact_person": "Bob Ross", "email": "bob@plexweb.com", "phone": "888-999-909"}
customer2={"company_name": "Wlex Peb", "contact_person": "Rob Boss", "email": "rob@wlexpeb.com", "phone": "999-888-808"}
customer3={"company_name": "Web Plex", "contact_person": "Leonardo Da Vinci", "email": "leonardo@webplex.com", "phone": "222-999-999"}
customer4={"company_name": "Peb Wlex", "contact_person": "Veonardo Da Linci", "email": "veonardo@pebwlex.com", "phone": "999-999-222"}

# TODO 3: Create a master customers dictionary
customers={"C001": customer1, "C002": customer2, "C003": customer3, "C004": customer4}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
for customer_id, details in customers.items():
    print(f"ID: {customer_id} | Company: {details['company_name']} | Contact: {details['contact_person']} | Email: {details['email']}")

# TODO 5: Look up specific customers
c002_info = customers.get("C002")
c003_contact = customers.get("C003", {}).get("contact_person", "Contact Not Found")
c999_info = customers.get("C999", "Customer ID C999 does not exist. Try again!")

print("\n\nCustomer Lookups:")
print("-" * 60)
print(f"C002 Info: {c002_info}")
print(f"C003 Contact Person: {c003_contact}")
print(f"C999 Info: {c999_info}")

# TODO 6: Update customer information
customers["C001"]["contact"] = "999-888-999"
customers["C002"]["industry"] = "Cybersecurity"
print("\n\nUpdating Customer Information:")
print("-" * 60)
print("C001's New Contact:", customers["C001"]["contact"])
print("C002's Industry:", customers["C002"]["industry"])

# TODO 7: Create project dictionaries for each customer
project1= {"name": "Website Building", "service": "Web Development", "hours": 50, "budget": 8000}
project2={"name": "Customer Base Analysis", "service": "Data Analysis", "hours": 30, "budget": 9000}
project3={"name": "Advertisment - Youtube", "service": "Animated Explainer Video", "hours": 180, "budget": 20000}
project4={"name": "Website Update", "service": "Troubleshooting Website", "hours": 50, "budget": 8000}
project5={"name": "Advertisement - Live T.V", "service": "Animated Explainer Video", "hours": 170, "budget": 19000}
projects = {
    "C001": [project1],
    "C002": [project2],
    "C003": [project3],
    "C004": [project4, project5]
}
print("\n\nProject Information:")
print("-" * 60)
for customer_id, project_list in projects.items():
    print(f"Customer {customer_id}: {len(project_list)} project(s)")
    for project in project_list:
        print(f"{project['name']} ({project['service']})")

# TODO 8: Calculate project costs
print("\n\nProject Cost Calculations:")
print("-" * 60)
for customer_id, project_list in projects.items():
    if project_list:
        print(f"Customer {customer_id} Projects:")
        for project in project_list:
            service_rate = services.get(project['service']) 
            calculated_cost = service_rate * project['hours']
            print(f"  - {project['name']:20} | Hours: {project['hours']:4} | Rate: ${service_rate:.2f} | Cost: ${calculated_cost:,.2f}")

# TODO 9: Customer statistics using dictionary methods
print("\n\nCustomer Statistics:")
print("-" * 60)
customer_ids = list(customers.keys())
print(f"Customer IDs: {customer_ids}")
customer_companies = [details['company_name'] for details in customers.values()]
print(f"Companies: {customer_companies}")
total_customer_count = len(customers)
print(f"Total Number of Customers: {total_customer_count}")

# TODO 10: Service usage analysis
service_counts = {}
for project_list in projects.values():
    for project in project_list:
        service_name = project['service']
        service_counts[service_name] = service_counts.get(service_name, 0) + 1
print("\n\nService Usage Analysis:")
print("-" * 60)
for service, count in service_counts.items():
    print(f"{service:20}: {count} projects")

# TODO 11: Financial aggregations
all_project_budgets = []
all_project_hours = []
for project_list in projects.values():
    for project in project_list:
        all_project_budgets.append(project['budget'])
        all_project_hours.append(project['hours'])
total_hours = sum(all_project_hours)
total_budget = sum(all_project_budgets)
avg_budget = total_budget / len(all_project_budgets) if all_project_budgets else 0
max_budget = max(all_project_budgets) if all_project_budgets else 0
min_budget = min(all_project_budgets) if all_project_budgets else 0
print("\n\nFinancial Summary:")
print("-" * 60)
print(f"Total Hours Across All Projects: {total_hours}")
print(f"Total Project Budget: ${total_budget:,.2f}")
print(f"Average Project Budget: ${avg_budget:,.2f}")
print(f"Maximum Project Budget: ${max_budget:,.2f}")
print(f"Minimum Project Budget: ${min_budget:,.2f}")

# TODO 12: Customer summary report
print("\n\nCustomer Summary Report:")
print("-" * 60)
for customer_id, details in customers.items():
    company_name = details['company_name']
    customer_projects = projects.get(customer_id, [])
    num_projects = len(customer_projects)
    customer_total_hours = sum(p['hours'] for p in customer_projects)
    customer_total_budget = sum(p['budget'] for p in customer_projects)
    print(f" ID: {customer_id:} | Company: {company_name:} | Number of Projects : {num_projects:} | Total Hours: {customer_total_hours:} | Total Budget: ${customer_total_budget:,.2f}")

# TODO 13: Create rate adjustments using dictionary comprehension
adjusted_rates = {service:(rate * 1.1) for service, rate in services.items()}
print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
for service, rate in adjusted_rates.items():
    print(f"{service:}: ${rate:,.2f}")

# TODO 14: Filter customers using dictionary comprehension
active_customers ={
    cid: details for cid, details in customers.items() if cid in projects and projects[cid]
}
print("\n\nActive Customers (with projects):")
print("-" * 60)
for cid, details in active_customers.items():
    print(f"{cid}: {details['company_name']}")

# TODO 15: Create project summaries using dictionary comprehension
customer_budgets = {
    cid: sum(project['budget'] for project in project_list)
    for cid, project_list in projects.items()
    if project_list # Only include customers with projects
}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
for cid, budget in customer_budgets.items():
    print(f"{cid} ({customers[cid]['company_name']}): ${budget:,.2f}")

# TODO 16: Service pricing tiers using dictionary comprehension
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if 100 <= rate <= 199 else "Basic" for service, rate in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
for service, tier in service_tiers.items():
    print(f"{service:20}: {tier}")
    
# TODO 17: Customer validation function
def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]
    is_valid = all(field in customer_dict and customer_dict[field] for field in required_fields)
    return is_valid
#main!!!
print("\n\nCustomer Validation:")
print("-" * 60)
for cid, details in customers.items():
    is_valid = validate_customer(details)
    print(f"Customer {cid} ({details['company_name']}): {'Valid' if is_valid else 'Invalid'}")

# TODO 18: Project status tracking with loops and conditionals
project1["Status"]="active"
project2["Status"]="completed"
project3["Status"]="active"
project4["Status"]="pending"
project5["Status"]="active"
status_counts = {"active": 0, "completed": 0, "pending": 0}
for project_list in projects.values():
    for project in project_list:
        status = project.get("Status")
        if status in status_counts:
            status_counts[status] += 1

print("\n\nProject Status Summary:")
print("-" * 60)
for status, count in status_counts.items():
    print(f"Projects {status.title()}: {count}")

# TODO 19: Budget analysis function with aggregation
def analyze_customer_budgets(projects_dict):
    budget_stats = {}
    for cid, project_list in projects_dict.items():
        if not project_list:
            continue
        budgets = [p['budget'] for p in project_list]
        count = len(budgets)
        total = sum(budgets)
        average = total / count
        budget_stats[cid] = {
            'total': total,
            'average': average,
            'count': count
        }
    return budget_stats

detailed_budget_analysis = analyze_customer_budgets(projects)

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
for cid, stats in detailed_budget_analysis.items():
    print(f"Customer {cid}: Count={stats['count']}, Total Budget=${stats['total']:,.2f}, Avg Budget=${stats['average']:,.2f}")
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys


# TODO 20: Service recommendation system
def recommend_services(customer_id, customers, projects, services):
    recommendations = []
    services_used = set()
    if customer_id in projects:
        for project in projects[customer_id]:
            services_used.add(project['service'])
    all_services = set(services.keys())
    services_notused = all_services - services_used
    customers_projects = projects.get(customer_id, [])
    max_spent = max(p['budget'] for p in customers_projects) if customers_projects else 0
    for service_name in services_notused:
        rate = services[service_name]
        if 100.00 <= rate <= 220.00: 
            recommendations.append(f"{service_name} (Rate: ${rate:.2f})")
        elif max_spent < 10000 and rate < 100.00:
            recommendations.append(f"{service_name} (Rate: ${rate:.2f})")
    if not recommendations:
        return ["Customer has used all services."]
        
    return recommendations

print("\n\nService Recommendations:")
print("-" * 60)
print(f"Recommendations for {customer_id}:")
for rec in recommend_services(customer_id, customers, projects, services):
    print(f"  - {rec}")
