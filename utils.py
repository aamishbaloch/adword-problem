class CompanyUtil:

    @staticmethod
    def get_if_exists(companies, name):
        """
        check if any company exists with the name specified
        :param companies: list of companies
        :param name: name to search for
        :return: company object if exists
        """
        company = [company for company in companies if company.name == name]
        if len(company) > 0:
            return company[0]

    @staticmethod
    def calculate_ppc(ctr, impressions, revenue, cost):
        """
        calculate profit per click for the record
        :param ctr: clickthrough rate
        :param impressions: number of impressions
        :param revenue: total revenue mentioned in the record
        :param cost: cost mentioned in the record
        :return: profit per click of the specified record
        """
        number_of_clicks = ctr * impressions
        profit = revenue - cost

        return number_of_clicks / profit
