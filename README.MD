# New Relic API Parser

- ## [Getting Started](#getting-started)
    * [Prerequiste](#prerequiste)
    * [Installation](#installation)
    * [Examples](#example)
- ## [Available Methods](#available-methods)
- ## [Reference](#reference)

## Getting Started

- ### Prerequisites
    - Python >= 3.6.x
    - pip

- ### Installation
    ```
    $ pip install newrelic-api-parser
    ```

- ### Examples
    - Calling the insights API
    ```
    # import the class
    from NewRelic.Insights import Insights
    
    query_key = 'NRIQ-xxxxxxxxxxxxxxxxxxxx'
    # Call the api by passing the query key
    # pass the account ID and the query you want to execute
    Insights(query_key=query_key)
    .query(<account_id>, nrql='SELECT * from PageView')
    ```

### Available Methods

- For REST APIs

| Class | Method | Params | Description |
| --- | --- | --- | --- |
| BrowserApplications | get_list | N.A. | return the list of browser applications
| BrowserApplications | create | browser_application_name | returns the detail of a browser application based on the application name passed
| Applications | get_list | N.A. | return the list of apm applications
| Applications | show | app_id | returns the detail of a an application based on the app id passed
| Applications | delete | app_id | delete an apm app on new relic based on the app id passed

- For Insights API

| Module | Method | Params | Description 
| --- | --- | --- | --- |
| Insights | query | account_id, nrql | execute the passed new relic query and return the data


### Reference
- Please refer the official New Relic Documentation for more details on the endpoints

### Note:
 - The package is under development and will be prone to more frequent updates