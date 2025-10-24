class Solution:
    def dayOfYear(self, date):
        """
        Given a date string in format "YYYY-MM-DD", return the day of the year.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
        
        # Days in each month (non-leap year)
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Check if leap year
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        
        # Add extra day to February if leap year
        if is_leap:
            days_in_month[1] = 29
        
        # Sum days from previous months plus current day
        return sum(days_in_month[:month-1]) + day


# Alternative Solution: Using datetime (one-liner)
def dayOfYearDatetime(date):
    from datetime import datetime
    return datetime.strptime(date, "%Y-%m-%d").timetuple().tm_yday


# Alternative Solution: Without sum() - more explicit
def dayOfYearExplicit(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust February for leap year
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        days_in_month[1] = 29
    
    # Count days from previous months
    total_days = 0
    for i in range(month - 1):
        total_days += days_in_month[i]
    
    # Add current day
    total_days += day
    
    return total_days


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ("2019-01-09", 9),
        ("2019-02-10", 41),
        ("2003-03-01", 60),
        ("2004-03-01", 61),  # Leap year
        ("1900-03-01", 60),  # Not a leap year (divisible by 100 but not 400)
        ("2000-03-01", 61),  # Leap year (divisible by 400)
        ("2019-12-31", 365),
        ("2016-12-31", 366),  # Leap year
    ]
    
    print("Testing Solution:")
    for date, expected in test_cases:
        result = sol.dayOfYear(date)
        status = "✓" if result == expected else "✗"
        print("{} Input: {} | Output: {} | Expected: {}".format(status, date, result, expected))