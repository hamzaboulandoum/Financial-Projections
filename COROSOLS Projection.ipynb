import math
import matplotlib.pyplot as plt
import numpy as np

class InvestmentModel:
    def __init__(self, params):
        # Unpack parameters
        self.params = params
        self.exchange_rate = params['exchange_rate']  # Dh to USD

        # Investment Plan
        self.initial_investment_year0 = params['initial_investment_year0']
        self.additional_investment_year1 = params['additional_investment_year1']
        self.annual_investment_per_service = params['annual_investment_per_service']

        # Operator Salaries 
        self.operator_gross_salary_usd = params['operator_gross_salary_usd'] 

        # Founders' and Staff Salaries (in) USD)
        self.founder_salary_usd = params['founder_salary_usd']
        self.assistant_salary_usd = params['assistant_salary_usd']
        self.additional_engineer_salary_usd = params['additional_engineer_salary_usd']
        self.additional_architect_salary_usd = params['additional_architect_salary_usd']
        self.financial_analyst_salary_usd = params['financial_analyst_salary_usd']

        # Operational Parameters
        self.operational_speed = params['operational_speed']
        self.effective_working_hours = params['effective_working_hours']
        self.days_per_week = params['days_per_week']
        self.weeks_per_year = params['weeks_per_year']
        self.tracing_cost_per_meter = params['tracing_cost_per_meter']
        self.variable_cost_per_meter = params['variable_cost_per_meter']

        # Market Parameters
        self.average_room_space = params['average_room_space']
        self.total_surface_area = params['total_surface_area']

        # Robots Used for Tracing
        self.robots_used_for_tracing = params['robots_used_for_tracing']

    def calculate_total_meters_to_trace(self):
        Ptt_shared = 3 * math.sqrt(self.average_room_space)
        rooms_to_trace = self.total_surface_area / self.average_room_space
        total_meters_to_trace = rooms_to_trace * Ptt_shared
        return total_meters_to_trace

    def calculate_daily_tracing_capacity(self):
        total_meters_per_day = (self.robots_used_for_tracing * self.operational_speed *
                                self.effective_working_hours * 3600)
        return total_meters_per_day

    def calculate_annual_tracing_capacity(self):
        daily_capacity = self.calculate_daily_tracing_capacity()
        print(daily_capacity)
        annual_capacity = daily_capacity * self.days_per_week * self.weeks_per_year
        return annual_capacity

    def calculate_yearly_financials(self):
        years = [0, 1, 2, 3, 4, 5]
        market_shares = [0, 0, 5, 10, 15, 20]
        financials = []

        total_meters_to_trace = self.calculate_total_meters_to_trace()
        capacity_per_service = self.calculate_annual_tracing_capacity()

        current_operating_services = 0
        previous_year_investment = 0

        for i, year in enumerate(years):
            total_investment = 0
            market_share = market_shares[i]
            meters_needed = total_meters_to_trace * (market_share / 100)

            # Calculate required operating services
            required_services = math.ceil(meters_needed / capacity_per_service)

            # Determine new services and investments
            new_services = max(0, required_services - current_operating_services)
            
            if year == 0:
                total_investment = self.initial_investment_year0
            elif year == 1:
                total_investment = self.additional_investment_year1
                
            elif required_services >1:
                total_investment = new_services * self.annual_investment_per_service
                        
            current_operating_services = required_services

            # Staff costs
            operator_salaries = 0
            additional_staff_salary = 0
            founders_salary = 0
            assistant_salary = 0
            
            if market_share >= 10:
                operator_salaries = current_operating_services * 2 * self.operator_gross_salary_usd * 12
                founders_salary = 4 * self.founder_salary_usd * 12
                assistant_salary = self.assistant_salary_usd * 12
            
            if market_share >= 15:
                additional_architect_salary = self.additional_architect_salary_usd * 12
                financial_analyst_salary = self.financial_analyst_salary_usd * 12
                additional_engineers_salary = 2 * self.additional_engineer_salary_usd * 12
                
                additional_staff_salary = (additional_architect_salary + 
                                        financial_analyst_salary + 
                                        additional_engineers_salary)

            staff_costs = operator_salaries + founders_salary + additional_staff_salary + assistant_salary

            variable_cost = meters_needed * self.variable_cost_per_meter
            turnover = meters_needed * self.tracing_cost_per_meter
            profit = turnover - variable_cost - staff_costs - previous_year_investment

            financials.append({
                'year': year,
                'market_share': market_share,
                'operating_services': current_operating_services,
                'new_services': new_services,
                'meters_traced': meters_needed,
                'turnover': turnover,
                'total_investment': total_investment,
                'staff_costs': staff_costs,
                'variable_cost': variable_cost,
                'profit': profit,
            })

            # Update previous_year_investment for the next iteration
            previous_year_investment = total_investment

        return financials
    def save_yearly_financials_to_file(self, filename):
        financials = self.calculate_yearly_financials()
        with open(filename, 'w') as f:
            f.write("Yearly Financials (Years 0-5):\n")
            f.write("------------------------------------------------------------\n")
            for fin in financials:
                f.write(f"Year {fin['year']}:\n")
                f.write(f"  Market Share: {fin['market_share']}%\n")
                f.write(f"  Operating Services: {fin['operating_services']}\n")
                f.write(f"  New Services Added: {fin['new_services']}\n")
                f.write(f"  Meters Traced: {int(fin['meters_traced']):,} meters\n")
                f.write(f"  Turnover: ${fin['turnover'] / 1e6:,.2f} million\n")
                f.write(f"  Total Investment This Year: ${fin['total_investment'] / 1e3:,.0f} thousand\n")
                f.write(f"  Staff Costs: ${fin['staff_costs'] / 1e3:,.0f} thousand\n")
                f.write(f"  Variable Costs: ${fin['variable_cost'] / 1e3:,.0f} thousand\n")
                f.write(f"  Profit: ${fin['profit'] / 1e6:,.2f} million\n")
                f.write("------------------------------------------------------------\n")
    def calculate_cumulative_financials(self):
        financials = self.calculate_yearly_financials()
        cumulative_profit = []
        cumulative_turnover = []
        cumulative_investment = []
        years = []
        total_profit = 0
        total_turnover = 0
        total_investment = 0

        for fin in financials:
            year = fin['year']
            investment = fin['total_investment']
            profit = fin['profit']
            turnover = fin['turnover']

            total_investment = investment
            total_profit = profit
            total_turnover = turnover

            cumulative_profit.append(total_profit)
            cumulative_investment.append(total_investment)
            cumulative_turnover.append(total_turnover)
            years.append(year)

        return years, cumulative_profit, cumulative_turnover, cumulative_investment
    
    def calculate_profit_by_market_share(self, max_market_share=100, step=5):
        """Calculate profit for market shares from 0% to 100% with the same logic as yearly financials."""
        market_shares = list(range(0, max_market_share + step, step))
        profits = []
        required_services_list = []
        total_investments = []

        total_meters_to_trace = self.calculate_total_meters_to_trace()
        capacity_per_service = self.calculate_annual_tracing_capacity()

        
        current_operating_services = 1
        for market_share in market_shares:
            # Meters needed
            total_investment = 0
            meters_needed = total_meters_to_trace * (market_share / 100)

            # Calculate required operating services
            required_services = math.ceil(meters_needed / capacity_per_service)

            # Total investment for new services
            
            New_added_service = required_services - current_operating_services
            
            if (New_added_service > 0): 
                total_investment = self.annual_investment_per_service
                current_operating_services +=1
                
                
            if(market_share == 0):
                total_investment = self.initial_investment_year0 
            if(market_share == 5):
                total_investment = self.additional_investment_year1

            # Staff costs - consistent with yearly financial logic
            operator_salaries = 0
            additional_staff_salary = 0
            founders_salary = 0
            assistant_salary = 0
            
            if market_share >= 10:
                operator_salaries = required_services * 2 * self.operator_gross_salary_usd * 12
                founders_salary = 4 * self.founder_salary_usd * 12
                assistant_salary = self.assistant_salary_usd * 12
            
            if market_share >= 15:
                
                additional_architect_salary = self.additional_architect_salary_usd * 12
                financial_analyst_salary = self.financial_analyst_salary_usd * 12
                additional_engineers_salary = 2 * self.additional_engineer_salary_usd * 12
                
                additional_staff_salary = additional_architect_salary + financial_analyst_salary + additional_engineers_salary

            staff_costs = operator_salaries + founders_salary + additional_staff_salary + assistant_salary

            variable_cost = meters_needed * self.variable_cost_per_meter
            turnover = meters_needed * self.tracing_cost_per_meter
            profit = turnover - variable_cost - staff_costs - total_investment

            profits.append(profit)
            required_services_list.append(required_services)
            total_investments.append(total_investment)

        return market_shares, profits, required_services_list, total_investments

    def save_profit_by_market_share_to_file(self, filename):
        """Save the profit by market share data to a text file."""
        market_shares, profits_by_market_share, required_services_list, total_investments = self.calculate_profit_by_market_share(max_market_share=100, step=5)
        with open(filename, 'w') as f:
            f.write("Profit by Market Share (Up to 100%):\n")
            f.write("------------------------------------------------------------\n")
            f.write("Market Share (%) | Required Services | Total Investment ($ thousands) | Profit ($ millions)\n")
            f.write("------------------------------------------------------------\n")
            for ms, rs, ti, p in zip(market_shares, required_services_list, total_investments, profits_by_market_share):
                f.write(f"{ms:>15}% | {rs:>17} | {ti / 1e3:>24,.0f} | {p / 1e6:>20,.2f}\n")
            f.write("------------------------------------------------------------\n")
    def plot_yearly_financials(self):
        """Plot the yearly financials (profit, turnover, and yearly investment) over 5 years with enhanced design."""
        financials = self.calculate_yearly_financials()

        # Extract yearly data
        years = [fin['year'] for fin in financials]
        yearly_profit_millions = [fin['profit'] / 1e6 for fin in financials]
        yearly_turnover_millions = [fin['turnover'] / 1e6 for fin in financials]
        yearly_investment_millions = [fin['total_investment'] / 1e6 for fin in financials]  # Use total_investment per year

        # Define COROSOLS colors
        corosols_blue = '#0A3466'
        corosols_orange = '#FF9900'
        corosols_green = '#00A86B'  # Green for yearly investment
        white = '#FFFFFF'

        # Create the figure and axis
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.set_facecolor(white)

        # Plot yearly profit, turnover, and investment
        ax.plot(years, yearly_profit_millions, marker='o', label='Profit (Millions)', color=corosols_orange, linewidth=2)
        ax.plot(years, yearly_turnover_millions, marker='o', label='Turnover (Millions)', color=corosols_blue, linewidth=2)
        ax.plot(years, yearly_investment_millions, marker='o', label='Investment (Millions)', color=corosols_green, linewidth=2)

        # Set axis labels and title with enhanced design
        ax.set_title('Yearly Financials Over 5 Years (Profit, Turnover, Investment)', fontsize=16, color=corosols_blue)
        ax.set_xlabel('Year', fontsize=14, color=corosols_blue)
        ax.set_ylabel('Amount (Millions of USD)', fontsize=14, color=corosols_blue)

        # Add grid for better readability
        ax.grid(True, linestyle='--', linewidth=0.5)

        # Customize ticks for better visibility
        ax.set_xticks(years)
        ax.set_xticklabels(years, fontsize=12)

        # Adjust y-axis ticks and range with more divisions
        y_min = min(min(yearly_profit_millions), min(yearly_turnover_millions), min(yearly_investment_millions))
        y_max = max(max(yearly_profit_millions), max(yearly_turnover_millions), max(yearly_investment_millions))
        y_step = max(0.5, (y_max - y_min) / 10)  # Ensure finer divisions on y-axis
        ax.set_yticks(np.arange(math.floor(y_min), math.ceil(y_max) + y_step, y_step))
        ax.tick_params(axis='y', labelsize=12)

        # Set y-axis limits to give some padding
        ax.set_ylim(y_min - y_step/2, y_max + y_step/2)

        # Add a legend and finalize layout
        ax.legend(loc='upper left', fontsize=12)
        plt.tight_layout()

        # Show the plot
        plt.show()


    def plot_profit_by_market_share(self):
        """Plot profit and investments by market share, showing the evolution with enhanced readability."""
        # Calculate the profit by market share
        market_shares, profits_by_market_share, required_services_list, total_investments = self.calculate_profit_by_market_share()
        profits_by_market_share_millions = [p / 1e6 for p in profits_by_market_share]
        total_investments_millions = [ti / 1e6 for ti in total_investments]

        # Define COROSOLS colors
        corosols_blue = '#0A3466'
        corosols_orange = '#FF9900'
        white = '#FFFFFF'

        # Create the figure and axis
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.set_facecolor(white)

        # Plot profit and investment lines
        ax.plot(market_shares, profits_by_market_share_millions, marker='o', label='Profit (Millions)', color=corosols_orange, linewidth=2)
        ax.plot(market_shares, total_investments_millions, marker='o', label='Investment (Millions)', color=corosols_blue, linewidth=2)

        # Set axis labels and title with enhanced design
        ax.set_title('Evolution of Profit and Investments by Market Share (5% to 100%)', fontsize=16, color=corosols_blue)
        ax.set_xlabel('Market Share (%)', fontsize=14, color=corosols_blue)
        ax.set_ylabel('Amount (Millions of USD)', fontsize=14, color=corosols_blue)

        # Add grid for better readability
        ax.grid(True, linestyle='--', linewidth=0.5)

        # Customize ticks for better visibility
        ax.set_xticks(market_shares[::2])  # Show every other tick for readability
        ax.set_xticklabels(market_shares[::2], fontsize=12)

        # Adjust y-axis ticks and range
        y_min = min(min(profits_by_market_share_millions), min(total_investments_millions))
        y_max = max(max(profits_by_market_share_millions), max(total_investments_millions))
        y_step = max(1, (y_max - y_min) // 10)  # Aim for about 10 ticks
        ax.set_yticks(np.arange(math.floor(y_min), math.ceil(y_max) + y_step, y_step))
        ax.tick_params(axis='y', labelsize=12)

        # Set y-axis limits to give some padding
        ax.set_ylim(y_min - y_step/2, y_max + y_step/2)

        # Add a legend and finalize layout
        ax.legend(loc='upper left', fontsize=12)
        plt.tight_layout()

        # Show the plot
        plt.show()


# Main invocation code
if __name__ == "__main__":
    # Parameters Dictionary
    params = {
        # Exchange Rate
        'exchange_rate': 10,  # 1 USD = 10 Dh

        # Investment Plan
        'initial_investment_year0': 100000,  # USD at start of Year 0
        'additional_investment_year1': 200000,  # USD at start of Year 1
        'annual_investment_per_service': 137000,  # USD per new operating service

        # Operator Salaries
        'operator_gross_salary_usd': 1000,  # Net salary in Dh

        # Founders' and Staff Salaries (in Dh)
        'founder_salary_usd': 2000,  # Per founder per month in Dh
        'assistant_salary_usd': 1000,  # Per month in Dh
        'additional_engineer_salary_usd': 2000,  # Per engineer per month in Dh

        # Additional Staff Salaries (in USD)
        'additional_architect_salary_usd': 2000,  # Per month
        'financial_analyst_salary_usd': 2000,     # Per month

        # Operational Parameters
        'operational_speed': 0.4,  # in meters per second
        'effective_working_hours': 5,  # per robot per day
        'days_per_week': 4,
        'weeks_per_year': 50,
        'tracing_cost_per_meter': 1.5,    # USD per meter
        'variable_cost_per_meter': 0.02,  # USD per meter

        # Market Parameters
        'average_room_space': 20,    # in square meters
        'total_surface_area': 20_000_000,  # in square meters

        # Robots Used for Tracing
        'robots_used_for_tracing': 2,  # Two robots used simultaneously
    }

    # Create an instance of the InvestmentModel with the given parameters
    model = InvestmentModel(params)

    # Calculate and print the annual tracing capacity
    annual_capacity = model.calculate_annual_tracing_capacity()
    print(f"Annual tracing capacity of one operating service: {annual_capacity:,.0f} meters")

    # Calculate and print the total meters to trace
    total_meters = model.calculate_total_meters_to_trace()
    print(f"Total meters to trace in the market: {total_meters:,.0f} meters")

    # Calculate and print the market share that can be covered by one operating service
    market_share_covered = (annual_capacity / total_meters) * 100
    print(f"Market share that can be covered by one operating service: {market_share_covered:.2f}%")

    # Save yearly financials (years 0-5) to a text file
    model.save_yearly_financials_to_file('yearly_financials.txt')

    # Save profit by market share data to another text file
    model.save_profit_by_market_share_to_file('profit_by_market_share.txt')

    # Plot the cumulative financials over 5 years
    model.plot_yearly_financials()

    # Plot the profit by market share graph
    model.plot_profit_by_market_share()

    print("Analysis complete. Please check the generated text files and plots.")   
        
        
        
