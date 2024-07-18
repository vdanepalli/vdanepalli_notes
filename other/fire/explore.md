## Fire Incident

### Fact

- We are not receiving lat longs from 11/10/2023
- If Unit Arrival Time is null, it is cancelled enroute? | Unit action taken 1 (93) == Cancelled enroute ?
- 
- 

### Check

- Is Alarm Handling Time (PSAP to Alarm) different from Alarm Processing Time (Dispatch to Alarm): Basic Module
- Alarm Transfer Time (PSAP to Dispatch) -- is it > 0 for any of the incidents
- Response Time PSAP to arrival -- is it correctly calculated in snowflake?
- Do we have values for Alarm Count field : Basic Module

### Check


- 

## General Question

- When personnel fill their Unit Reports, do they fill it on ESO? Is it directly stored on ESO side or is first stored somewhere else and then sent to ESO 
- CAD data is sent to ESO in flat files? Fixed width? CSV? What fields are sent, and can we get the mapping information (column header or ...)
- Who writes Incident Narratives? Is it a combination of Unit Narratives?
- Should we decide to build a streamlit based app, where do we want to process our data?
  - Process it on snowflake end and only share the data related to visualizations on the streamlit end?
    - Might not allow filters to effect visuals
  - Fetch data from snowflake and process data on streamlit end as required?

## Specific Question 

- Does Unit Cleared Scene Datetime represent when it is back in service?
- Does Unit Turnout Time = Enroute - Dispatch
- What does it mean to have Unit records same except in exposure id and fire incident apparatus id for a specific unit and incident id (T1 : "e7dcc681-8347-4a17-ad6d-b1a101308611") Unit Dispatched DateTime (2024-07-02T13:29:43.000Z)?
- How to identify a deleted incident recordd in database?
- Can multiple incident ids have one single incident number with incident/alarm date varying across years 
  - `SELECT * FROM "Basic Module" WHERE "Incident Number" = '0018477'`  | `'0053785'`
- Why are we getting null values in shifts. `Incident Number = 240032992`
- 


## Scenario

- Say, a unit is dispatched and is cancelled enroute
  - it has dispatch time -- Unit dispatched datetime -- does it represent the time unit was notified by dispatch/communications center?
  - it has clear time -- Unit cleared scene datetime
  - but no Unit Enroute Datetime?


## Analysis

- Fire Module
  - How does fire incident count vary against 
    - "Area of Origin" (Bathroom, Checkroom, Locker room, Lavatory...)
    - "Heat Source"
    - "Item First Ignited"
    - "Type of Material First Ignited"
    - "Cause of Ignition" -- Intentional
    - "Factors Contributing to Ignition [12]"
    - "Human Factors Contributing to Ignition"
    - "Structure Type" -- Enclosed Building
    - "Building Stories [Above|Below] Grade"
    - "Building Status"
    - "Fire Spread" -- confined to buildiing of origin
    - "Prescence of detector"
    - "Prescence of Automatic Extinguishing System"

## Ideas

- Analyze Fire module to understand how fire incidents vary
  - source, cause, spread etc
- Find properties without detector | automatic fire extinguishing system
- 