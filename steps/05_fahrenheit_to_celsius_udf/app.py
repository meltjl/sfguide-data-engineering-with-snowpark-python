#------------------------------------------------------------------------------
# Hands-On Lab: Data Engineering with Snowpark
# Script:       05_fahrenheit_to_celsius_udf/app.py
# Author:       Jeremiah Hansen, Caleb Baechtold
# Last Updated: 1/9/2023
#------------------------------------------------------------------------------

# SNOWFLAKE ADVANTAGE: Snowpark Python programmability
# SNOWFLAKE ADVANTAGE: Python UDFs (with third-party packages)
# SNOWFLAKE ADVANTAGE: SnowCLI (PuPr)

import sys
from scipy.constants import convert_temperature

def main(temp_f: float) -> float:
    print('using scipy.convert_temperature')
    return convert_temperature(float(temp_f), 'F', 'C')

def main_OLD(temp_f: float) -> float:
    return (float(temp_f) - 32) * (5/9)

# ref: https://docs.snowflake.com/developer-guide/udf/python/udf-python-introduction
# ref: https://quickstarts.snowflake.com/guide/data_engineering_pipelines_with_snowpark_python/index.html?index=..%2F..index#6

# For local debugging
# Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(*sys.argv[1:]))  # type: ignore
    else:
        print(main())  # type: ignore


# To deploy to snowflake
# cd steps/05_fahrenheit_to_celsius_udf
# snow function create

# Then login to snowsight and run
# SELECT ANALYTICS.FAHRENHEIT_TO_CELSIUS_UDF(35);