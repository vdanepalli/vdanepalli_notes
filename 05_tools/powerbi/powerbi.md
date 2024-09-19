# <center> ZTM : Power BI 


<details>
  <summary></summary>
  
- Power BI -- interactive data visualization software product developed by Microsoft primarily for Business Intelligence
- Business Intelligence -- art and science of transforming data into actionable insights that help organizations make decisions
- fetch data from different sources, modeling data by forming relationships between different data sources, analyzing it, and then translating that analysis into a wide range of visualizations
- Power Query -- built in ETL tool that enables to fetch data from different sources, and then clean and transform data to prepare it for analysis and visualization
- Data Modeling -- Power BI lets us combine the datasets into a data model, where we can link those datasets together so they can be analyzed holistically
- Visualizations -- Power BI has a wide range of visualizations that can help you tell a story about all the data fetched, transformed, and modeled
- Data Analysis -- Power BI has built in formula language -- DAX -- allows you to create incredibly powerful and sophisticated calculations that you can add to your visualizations
- Power BI Desktop -- free, has everything you need to build sophisticated visualizations, reports, and end to end BI solutions
- Power BI Pro -- cloud based, subscription service offered by Microsoft, that provides sophisticated options for sharing reports, collaborating with other report developers, and automating workflows. 


<hr>


- We start off with Power Query Screen. Once closed, we see the actual Power BI screen page. It contains a ribbon similar to Excel that contains many functionality.
- Data View -- click on the datasets to see the data that it holds. Expand to see information on attributes. 
- Model view -- Diagram view -- links / relationships between the datasets; Entity Relationship Diagram ERD
- Report View -- Visualizations. Organized in tabs or pages
- File > Options and Settings > Options > Current File > Regional Settings > Local for Import 
- Imports are available in the Fields section with the name of the query. Query names are same as imported database names
- ETL 
  - Home > Get Data > Connect -- gives preview before loading -- (Load  | Transform Data); Hitting Transform Data loads the Power BI Power Query Editor
    - Power Query Translates our applied changes into a programming language called M
  - Returns to Report View once we click on Load
  - Save loaded file in .pbix format
- Fetching Data from Databases
  - SQL Server Database (server, [ database ])
  - You can provide SQL Query in the Advanced section to fetch only the output of the SQL query --- however, now the query is named query 1 instead of the database name
  - Home > Refresh
- Introducing power query
  - Each query has properties called name(s)
- Basic Transformations
  - Transform tab
  - Add Column tab
    - General
    - From Text
    - From NUmber
    - From Date and TIme
    - All Insights
  - Close and Apply button -- after making the necessary transformations, you can load data to Power BI
- Editing transformations
  - Clicking on Transform Data tab will take you back to power query editor. You can select any change, and modify or delete transformations, basically travel back in time
  - Gear icon on the applied step will let you edit the step
- Numeric transformations
  - diurnal range -- difference between lowest and highest temperature in a day
- Date & Text transformations
  - 
</details>

-----
<br/><br/>
-----

# <center> ZTM Power BI


<details open>
<summary>  </summary>


- [Course resources](https://cdn.fs.teachablecdn.com/79HZUsIS0GrUoODwfEjH)
  
## Power BI 101

- Power BI : Interactive data visualization software (Microsoft) with primary focus on BI 
  - Fetch data from variety of data sources
  - Modeling data by forming relationships between different sources
  - Analyzing it
  - Translating analysis into Visualizations
- BI : Art and Science of transforming data into actionable insights that help organizations make decisions
  
<br/><br/>

- ETL tool -- Power Query
- Data Modeling -- lets us combine separate datasets into a data model
- Visualizations -- tell a story
- Data Analysis -- DAX -- formula language -- powerful calculations
- Just as visualization tool vs complete BI in a box solution
- PowerBI Desktop -- free
- PowerBI Pro -- cloud based subscription -- share reports, collaborate and automate workflows
  
<br/><br/>

- Ribbon -- Home, Transform, Add Column, 
- Report View, Table View, Model View, DAX Query View
- File > Options and Settings > Options > Regional Settings --- date settings on a file by file basis

<br/><br/>

- ETL : Extract, Transform (PowerQuery Editor), Load (PowerBI)
- Preview Data -- when loading 
  - File Origin, Delimiter, Data Type Distinction, Load, Transform Data
- Query -- external dataset -- default : name of the file imported
- Get Data > SQL Server > Advanced > Custom SQL 
- Programming Language M is built into Power Query
- Rename Columns 
- Change Data Type -- Change Type
- Remove Columns
- Filter
- Query Settings
  - Properties
  - Applied Steps
- Home > Transform Data -- takes you to power query editor
- Transform -- Inplace
- Add Column -- new column -- conditional column, 

<br/><br/>

- Date Transformations -- Date, Month, Year, Day of the Week, ...
- Text Transformations -- Split, Merger, Find and Replace, Format (Add prefix/suffix ...)
- Report Canvas, Data pane, Visualizations pane, 
- Numeric Fields
- Categorical Fields -- Dimensions
- Concept of data point's address relative to the row and column headers in a report determining how that data point is calculated is called filter context
- Matrix Visualizations -- similar to pivot tables
- 


## Visualizing Data with Power BI

- column chart 
  - stacked column chart -- each bar is broken into parts corresponding to legend
    - x, y axes, legend
  - clustered column chart -- bars are side by side for each legend
    - each x axis category gets its own cluster
- bar charts
  - clustered bar chart
  - stacked bar chart
- format your visualization
- line chart
- pie chart -- we assess by area
- donut chart -- we assess by length
- tree map -- rectangle size indicate proportinality
  - Category -- parent
  - Details -- child
- small multiples -- create multiple charts
- tooltips
- drill down
- Zoom slider
- Map Charts
  - Column Tools > Properties > Data Category
  - bubble size 
- Visualizations > General > Canvas Settings
- Dashboards
  - Readability of visuals
  - View > Gridlines 
  - View > Snap to grid
  - View > Themes
- Format > Interactions > Edit Interactions
- Slicers
  - are filters that apply to all the visualizations on the page
  - Slicer Headers
  - Field
- Date Slicers
- Insert > Image

## Advanced Power Query

- Data Profiling
  - View > Data Preview > Column Profile
    - Summary Statistics
  - View > Data Preview > Column Distribution -- only useful for categorical columns, doesn't make much sense for continuous columns
  - View > Data Preview > Column quality -- valid, error, empty
- Configurng refresh
  - Right click query > Include in report refresh
- Merging datasets
  - While selecting the dataset you want to merge into, Home > Combine > Merge Queries | Merge Queries As New
- Appending Datasets -- stack them vertically
  - same number of cols and same data types
  - Home > Combine > Append Queries
- Aggregate Calculations
  - Transform > Any Column | Text | Number
- File > Options and Settings > Options > Current File > Data Load > Autodetect new relationships after data is loaded

<br/><br/>

- M Code
- `#"column/step name" `
- Home > Query > Advanced Editor
  ```vbscript
  let
    Source = Csv.Document(File.Contents())
    .. 
    ...

  in 
    LastStep -- the one that produces the output
  ```

- Add Column > Custom Column
- Clicking on fx adds new step
- Custom filters with M Code

## Modeling Data in Power BI

- snowflake schema
- modeling data
- 

## Analyzing Data with DAX


## Advanced DAX


## Advanced Visualizations


</details>

-----
<br/><br/>
-----

# <center> Udemy : Microsoft Power BI Desktop for Business Intelligence


<details open>
  <summary>  </summary>

## Introduction 

![](assets/2024-08-29-15-52-13.png)
![](assets/2024-08-29-15-52-25.png)
![](assets/2024-08-29-15-52-45.png)

- frontend 
  - model view
  - data view
  - report view
- backend
  - power query editor
- resources
  - help 
  - Microsoft Power BI Blog
  - Microsoft Power BI Youtube -- Also, Guy in a Cube
  - Power BI User Groups -- pbiusergroup.com

## Connecting and Shaping 

- ![](assets/2024-08-29-16-00-22.png)
- Home > Get Data
- Power Query Editor 
  - Queries Pane
  - Query Editing Tools
    - Home 
    - Transform
      - Replace Values
    - Add Column
      - Extract
        - Text Before Delimitter
  - Formula Bar
  - Table Name and Properties
  - Applied Steps
  - Table Preview
- ![](assets/2024-08-29-16-17-34.png)
- Right click on a query and uncheck enable load in Power Query Editor -- data is not loaded to data model 
- You can connect to a database or get data from web 
- Data profiling  
  - Column Quality 
    - Valid 
    - Error 
    - Empty
  - Column Distribution 
    - Distinct 
    - Unique
  - Column Profile
    - Column Statistics 
    - Value Distribution
    - Includes sample distribution and profiling statistics
    - Count, Distinct, Error, Empty, Unique, Min, Max, ...
- Keep/Remove Errors/Empty/Duplicates

<br/>

- ![](assets/2024-08-29-16-37-47.png)
- ![](assets/2024-08-29-16-38-25.png)
- ![](assets/2024-08-29-16-42-23.png)
- Date.StartOfWeek(DateColumn, 1) -- 1 Monday 2 Tuesday ...;
- Date.StartOfWeek(DateColumn, Day.Monday)
- Right Click Column > Using Locale > Select Data Type and Locale
- ![Rolling Calendars](assets/2024-08-30-09-14-44.png)
  - convert list to table as a final step
- Add Column 
  - Index Column
  - Conditional Column
- Power BIs internal engine called Verticap uses something called query plan to optimize data when storing it in a data model. Say, if you are applying transformations in the front end then they are not part of the same query plan and might cause performance issues. 
- ![Grouping and Aggregating](assets/2024-08-30-09-28-41.png)
- ![Pivoting and Unpivoting](assets/2024-08-30-09-36-24.png)
- ![Merging Queries](assets/2024-08-30-09-36-52.png)
- ![Appending Queries](assets/2024-08-30-09-39-47.png)
- ![Appending Files from Folder](assets/2024-08-30-09-48-45.png)
- ![Data Source Settings](assets/2024-08-30-09-49-04.png)
- ![Data Source Parameters](assets/2024-08-30-09-49-21.png)
- ![Refreshing Queries](assets/2024-08-30-09-59-21.png)
- ![Importing Excel Models](assets/2024-08-30-09-59-47.png)
- ![Power Query Best Practices](assets/2024-08-30-10-00-14.png)

## Data Model

- ![Creating a Data Model](assets/2024-08-30-10-10-34.png)
- ![Not a Data Model](assets/2024-08-30-10-11-15.png)
- ![Data Model](assets/2024-08-30-10-11-29.png)
- ![Data Normalization](assets/2024-08-30-10-19-19.png)
- ![Fact and Dimension Tables](assets/2024-08-30-10-19-54.png)
- ![Primary and Foreign Keys](assets/2024-08-30-10-20-17.png)
- ![Relationships vs Merged Tables](assets/2024-08-30-10-20-50.png)
- ![Model view](assets/2024-08-30-10-26-11.png)
- ![Creating Table Relationships](assets/2024-08-30-10-26-28.png)
- ![Managing and Editing Relationships](assets/2024-08-30-10-26-51.png)
- ![Star and Snowflake Schemas](assets/2024-08-30-10-27-14.png)
- ![Active and Inactive relationships](assets/2024-08-30-10-35-11.png)
- 

## Measures with DAX

## Visualize

## Optimize performance

</details>

-----
<br/><br/>
-----

# 
