import pandas as pd
from utils import CompanyUtil
from company import Company

if __name__ == '__main__':
    """
    read all the records from the csv, calculate profit per click on each record and sort the companies by taking
    average of all the profit per click calculated against keywords

    code will print the companies in sorted order of their performance
    """
    companies = []
    df = pd.read_csv('sample.csv')
    df.columns = ["keyword", "impressions", "ctr", "cost", "position", "company", "revenue"]

    for index, row in df.iterrows():
        company = CompanyUtil.get_if_exists(companies, row['company'])
        if company:
            company.ppc.append(CompanyUtil.calculate_ppc(
                ctr=row['ctr'],
                impressions=row['impressions'],
                revenue=row['revenue'],
                cost=row['cost'],
            ))
        else:
            company = Company(row['company'])
            companies.append(company)

    company_data = [{'name': company.name, 'performance': company.get_performance()} for company in companies]
    company_sorted_data = sorted(company_data, key=lambda k: k['performance'], reverse=True)

    for company in company_sorted_data:
        print("Company Name: {}, Performance: {}".format(company['name'], company['performance']))
