# Running the UDF Locally
To test the UDF locally, you will execute the steps/05_fahrenheit_to_celsius_udf/app.py script. Like we did in the previous steps, we'll execute it from the terminal. So go back to the terminal in VS Code, make sure that your snowflake-demo conda environment is active, then run the following commands (which assume that your terminal has the root of your repository open):

    cd steps/05_fahrenheit_to_celsius_udf
    python app.py 35


While you're developing the UDF you can simply run it locally in VS Code. And if your UDF doesn't need to query data from Snowflake, this process will be entirely local.

# Deploying the UDF to Snowflake
To deploy your UDF to Snowflake we will use the SnowCLI tool. The SnowCLI tool will do all the heavy lifting of packaging up your application, copying it to a Snowflake stage, and creating the object in Snowflake. Like we did in the previous steps, we'll execute it from the terminal. So go back to the terminal in VS Code, make sure that your snowflake-demo conda environment is active, then run the following commands (which assume that your terminal has the root of your repository open):

    cd steps/05_fahrenheit_to_celsius_udf
    snow function create

While that is running, please open the script in VS Code and continue on this page to understand what is happening.


# Running the UDF in Snowflake
In order to run the UDF in Snowflake you have a few options. Any UDF in Snowflake can be invoked through SQL as follows:

SELECT ANALYTICS.FAHRENHEIT_TO_CELSIUS_UDF(35);

And with the SnowCLI utility you can also invoke the UDF from the terminal in VS Code as follows:

snow function execute -f "fahrenheit_to_celsius_udf(35)"
That will result in the SnowCLI tool generating the SQL query above and running it against your Snowflake account.