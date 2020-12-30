# Workflow

Document the workflow of the solution here:

1) Work out where AWS Public ranges are situated? - COMPLETE
    - Find the URL? (https://ip-ranges.amazonaws.com/ip-ranges.json)
    - We want URL, so we can query programmatically

2) Retrieve the URL
    - Report success/failure - COMPLETE
    - Convert that response into a data structure so we can work with it - COMPLETE

3) Parse the data structure - COMPLETE
    - Retrieve the "interesting data" out of it.
    - At minimum, the public IP addresses - COMPLETE
    - Ideally add a description - COMPLETE

4) Output the data structure to a file format
    - Simple text file - COMPLETE
    - Potentially be able to save outputs to other formats (CSV?) - COMPLETE