"""
This script is used to parse the AWS public IP ranges
into various file formats

Documentation:
https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html

URL:
https://ip-ranges.amazonaws.com/ip-ranges.json
"""
# Import modules
import requests
from requests.exceptions import HTTPError


def retrieve_url(url):
    """
    Retrieve the URL and parse the response for
    success/failure and a structured data output.

    :param url: The fully qualified URL which you want to query.
        Example: https://www.google.com.au
    :type url: string

    :return resp_ok: A True/False boolean to indicate whether a
    valid response was retrieved from the URL request
    :type resp_ok: boolean
    :return output: The JSON decoded output from the request.
        Example:
            - When URL is successful, a dictionary is returned
            - When URL is not successful, a string is returned
    """
    # Try/Except block to retrieve the URL
    try:
        # Get the URL
        resp = requests.get(url)
    # Raise exception, print HTTP error
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    # Raise exception, print other error
    except Exception as err:
        print(f"Other error occurred: {err}")
    # Debug printouts
    # print(f"Response {resp}")
    # print(f"Response OK? - {resp.ok}")
    # Assign response OK to a variable
    resp_ok = resp.ok
    # If/Else block to assess whether response is OK
    if resp_ok is True:
        # Assign JSON decoded output to a variable
        output = resp.json()
    else:
        # Assign the raw text string output to a variable
        output = resp.text
    # Return response ok and output
    return resp_ok, output


def parse_output(output):
    """
    Parse the dictionary output into a usable format, so it
    can be saved to a file.

    :param output: The dict output which needs to be parsed
    :type output: dict

    :return ipv4_dict: A dictionary containing IPv4 prefixes
    and an auto-generated description.
        Example:
        {
            'ipv4_results':
                {'3.5.140.0/22': 'us-east-2-ec2-ap-east-2-11'}
        }
    :type ipv4_dict: dict
    """
    """
    Below is the data structure that we are attempting to parse:
    {
        "syncToken": "0123456789",
        "createDate": "yyyy-mm-dd-hh-mm-ss",
        "prefixes": [
            {
            "ip_prefix": "cidr",
            "region": "region",
            "network_border_group": "network_border_group",
            "service": "subset"
            }
        ],
        "ipv6_prefixes": [
            {
            "ipv6_prefix": "cidr",
            "region": "region",
            "network_border_group": "network_border_group",
            "service": "subset"
            }
        ]
    }
    """
    # Retrieve series of values
    # sync_token = output["syncToken"]
    # create_date = output["createDate"]
    # Debug printouts
    # print(f"Sync Token is: {sync_token}")
    # print(f"Create Date is: {create_date}")
    # Assign the IPv4 prefixes to a variable
    ipv4_prefixes = output["prefixes"]
    # Debug printout
    # print(f"IPv4 Prefixes: {ipv4_prefixes}")
    # Create an empty dictionary to add our results to
    ipv4_dict = {"ipv4_results": {}}
    # Create a unique count to be added to each entry
    aws_counter = 0
    # Iterate over the ipv4_prefixes
    for prefix in ipv4_prefixes:
        # Retrieve values and assign to variables
        ipv4_prefix = prefix["ip_prefix"]
        region = prefix["region"]
        network_border_group = prefix["network_border_group"]
        service = prefix["service"]
        # Increment unique counter
        aws_counter += 1
        # Debug printouts
        # print(f"IPv4 Prefix: {ipv4_prefix}")
        # print(f"Region: {region}")
        # print(f"Network Border Group: {network_border_group}")
        # print(f"Service: {service}")
        # print(f"Counter: {aws_counter}")
        # String together the region, network_border_group, service
        # and AWS counter into a description variable
        description = (
            region
            + "-"
            + service.lower()
            + "-"
            + network_border_group
            + "-"
            + str(aws_counter)
        )
        # Debug printouts
        # print(f"Description: {description}")
        # Append IPv4 prefix and description to the IPv4 dict
        ipv4_dict["ipv4_results"][ipv4_prefix] = description
    # Return ipv4_dict for processing
    return ipv4_dict


def output_results(
    ipv4_dict, filename_prefix="aws_public_ip_ranges", text=True, csv=False
):
    """
    Output the result to a text file.
    TODO: Add more output types

    :param ipv4_dict: A dictionary containing an IP prefix
    and description, ready to be outputted to a file
    :type ipv4_dict: dict
    :param filename_prefix: A name which would you like
    to prefix the file with.
        Example: filename_prefix = "bob". Output file(s) would be "bob.txt" and
        "bob.csv"
    :type filename_prefix: string
    :param text: A boolean flag to indicate whether you would like
    the results outputted to a text file
        Default: True
    :type text: boolean
    :param csv: A boolean flag to indicate whether you would like
    the results outputted to a CSV file
        Default: True
    :type csv: boolean


    :return text_filename: The text file format filename where the
    data was stored
    :type text_filename: string
    :return csv_filename: The CSV file format filename where the
    data was stored
    :type csv_filename: string
    """
    # If text is set to True, process results to a text file
    if text is True:
        # Assign the text filename, by adding the txt extension
        text_filename = filename_prefix + ".txt"
        # Open a text file and save the contents of the ipv4_dict
        # to a file
        with open(text_filename, mode="w+") as text_file:
            # Write a header
            text_file.write("IP Prefix\tDescription\n")
            # Iterate over ipv4_dict and save results to the file
            for ip, description in ipv4_dict["ipv4_results"].items():
                # Format our output_line seperated by commas
                output_line = ip + "\t" + description + "\n"
                # Write output line to file
                text_file.write(output_line)
    # Else, return blank string if set to False
    else:
        text_filename = ""
    # If csv is set to True, process results to a csv file
    if csv is True:
        # Assign the csv filename, by adding the csv extension
        csv_filename = filename_prefix + ".csv"
        # Open a csv file and save the contents of the ipv4_dict
        # to a file
        with open(csv_filename, mode="w+") as csv_file:
            # Write a header
            csv_file.write("IP Prefix,Description\n")
            # Iterate over ipv4_dict and save results to the file
            for ip, description in ipv4_dict["ipv4_results"].items():
                # Format our output_line seperated by commas
                output_line = ip + "," + description + "\n"
                # Write output line to file
                csv_file.write(output_line)
        # Else, return blank string if set to False
    else:
        csv_filename = ""
    # Return the filename for further processing
    return text_filename, csv_filename


def main():
    """
    Main workflow which executes the entire solution.
    """
    # Define the AWS URL
    url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
    # Execute the function and assign to a variable
    response = retrieve_url(url)
    # Retrieve the resp_ok result and assign to a variable
    resp_ok = response[0]
    # Retrieve the output result and assign to a variable
    output = response[1]
    # print(f"Output: {output}")
    # If/Else block to assess whether response is OK
    if resp_ok is True:
        print("Response was successful, commencing parsing")
        # Execute function to parse output
        ipv4_dict = parse_output(output=output)
        # Execute function to output results to file
        text_filename = output_results(
            ipv4_dict=ipv4_dict,
            filename_prefix="updated_aws_data",
            text=True,
            csv=True,
        )
        # Debug printouts by accessing the appropriate
        # tuple result from the function
        print(f"Text Outputs were saved at: {text_filename[0]}")
        print(f"CSV Outputs were saved at: {text_filename[1]}")
    # Else, printout not successful message and output
    else:
        print("The URL response was not successful:")
        print(f"Response: {output}")


# Execute main workflow
if __name__ == "__main__":
    main()
