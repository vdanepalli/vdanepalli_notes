# ZTM Excel 

## Excel 101


## Filtering and Sorting Data


## Excel Formulas 101


## Crunchng Numbers with Excel Functions


## Conditional Calculations


## Date and Time Functions


## Text Fnctions


## Logical and Lookup Functions

- `IF(logical_test, true_val, false_val)`
- Can nest if conditions. More restrictive -- outer function; less restrictive == inner function
- `AND(test1, test2, ...)`
- `OR(test1, test2, ...)`
 
<br/><br/>

- vlookup
  - function searches first column of the lookup table for a match to the input value-- hence V or vertical Lookup
  - When the function finds the first match, it jumps over a specified number of columns to fetch the value we are looking up
  - `VLOOKUP(lookup_val, table_arr_range, col_index_num, TRUE/FALSE)` False -- Exact Match; True -- Approximate Match.
  - `#N/A` -- value cannot be found or identified
- `IFERROR(value, value_if_error)`
  
<br/><br/>
  
- `=IF(F4>D4,"Fail","Pass")`
- `=IF(F2=D2,"Meets",IF(F2>D2,"Fail","Exceeds"))`
- `=IF(AND(C2="Yes",F2>D2),"Yes","No")`
- `=IFERROR(VLOOKUP($A2,'Customer Data'!$A:$E,2,FALSE),"Not Found")`

## Modeling in Excel

- `PMT(Rate, Number of periods, Present value, Fv, Type)`
- Data Tools > Data Validation Lists
- Models in Excel allow you to quickly change the inputs, to see the effect on the output. 
- Formulas > Defined Names > Define Name
- Formulas > Defined Names > Name Manager

## Data Visualization in Excel

- `NOW() --- m/d/yyyy h:mm` 
- `dddd` -- Monday
- `mmmm` --- July
- `mmm` --- Jul

<br/><br/>

- Home > Styles > Conditional Formatting > Highlight Cells Rules
- Home > Styles > Conditional Formatting > Top/Bottom Rules
- Home > Styles > Conditional Formatting > Data Bars
- Home > Styles > Conditional Formatting > Color Scales

<br/><br/>

- Charts
- Vertical (Value) axis
- Horizontal (Category) axis
- Plot Area
- Chart Title
- Insert > Charts
- Chart Design -- Contextual Tab
- Chart Design > Select Data
- Chart Design > Add Chart Element

## Working with Structured Data in Excel

- Data > Text To Columns
- Insert > Table `Ctrl + T`
- `[@ColumnName]` -- In Tables
- Table Design > Properties > Table Name
- `COUNTA(tableName[colName])` -- all rows of the column except header
- `COUNTA(CellRange)` 
- Tables act as Named Ranges. 


## Pivot Tables


## Macros and VBA


## Build a Retirement Planner with Excel


# ZTM Advanced Excel

## Power Query 

- Extract, Transform, Load
- Power Query Editor
- Promoted Headers (1st row as column headers)
- Basic/Editing/Numerical/Text/Date/Conditional Transformations
- Merging Datasets -- Merging Queries
- Append Queries

## Excel Data Model

- 


## Analyzing Data Model with DAX



## Advanced DAX



## Data Visualization Techniques


# ZTM BA for Excel


## Introducing Macros and VBA

- Macros : Record actions that can be run again later at the click of a button; can say named subroutine
- Excel Macro Enabled Workbook -- xlsm
- VBA : Visual Basic for Applications
- `Alt +  F11` Enter into VBA Editor environment
- Macros are organized into Modules (Subroutines aka Procedures are present)
- `Call MacroName`
  ```vbscript
    Sub MacroName(optional args ...)
    ' Comments
    '

        Range("A1").Select
        ActiveCell.FormulaR1C1 = "Hello there!"

        Call ProcessComplete
    End Sub

    Sub ProcessComplete()
        MsgBox("Process Complete!")
    End Sub
    ```
- Modular Programming 
- Personal Workbook -- Macros stored in here can be applied to any excel file  -- PERSONAL.XLSB -- `username/AppData/Roaming/Microsoft/Excel/XLSTART/PERSONAL.XLSB`

    ```vbscript
    Sub VIBGYOR()
    '
    ' VIBGYOR Macro
    '

    '
        Range("A1").Select
        ActiveCell.FormulaR1C1 = "VIOLET"
        Range("A1").Select
        With Selection.Interior
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .Color = 10498160
            .TintAndShade = 0
            .PatternTintAndShade = 0
        End With
        With Selection.Font
            .ThemeColor = xlThemeColorDark1
            .TintAndShade = 0
        End With
        Range("A2").Select
        ActiveCell.FormulaR1C1 = "INDIGO"
        Range("A2").Select
        With Selection.Interior
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .Color = 6299648
            .TintAndShade = 0
            .PatternTintAndShade = 0
        End With
        With Selection.Font
            .ThemeColor = xlThemeColorDark1
            .TintAndShade = 0
        End With
        Range("A3").Select
        ActiveCell.FormulaR1C1 = "BLUE"
        Range("A3").Select
        With Selection.Interior
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .Color = 12611584
            .TintAndShade = 0
            .PatternTintAndShade = 0
        End With
        With Selection.Font
            .ThemeColor = xlThemeColorDark1
            .TintAndShade = 0
        End With
        Range("A4").Select
        ActiveCell.FormulaR1C1 = "GREEN"
        Range("A4").Select
        With Selection.Interior
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .Color = 5287936
            .TintAndShade = 0
            .PatternTintAndShade = 0
        End With
        With Selection.Font
            .ThemeColor = xlThemeColorDark1
            .TintAndShade = 0
        End With
        Range("A5").Select
        ActiveCell.FormulaR1C1 = "YELLOW"
        Range("A5").Select
        With Selection.Interior
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .Color = 65535
            .TintAndShade = 0
            .PatternTintAndShade = 0
        End With
        Range("A6").Select
        ActiveCell.FormulaR1C1 = "ORANGE"
        Range("A6").Select
        With Selection.Interior
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .Color = 49407
            .TintAndShade = 0
            .PatternTintAndShade = 0
        End With
        Range("A7").Select
        ActiveCell.FormulaR1C1 = "RED"
        Range("A7").Select
        With Selection.Interior
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .Color = 255
            .TintAndShade = 0
            .PatternTintAndShade = 0
        End With
        Range("A1:A7").Select
        Selection.Font.Bold = True
        Columns("A:A").ColumnWidth = 24.09
        Range("A1").Select
    End Sub
    ```

## Variables and User Input

- Integer, Long, Double, String, Boolean, Date, Variant (default)
  ```vbscript
  Dim VariableName As Integer
  Num1 = 39
  Num2 = InputBox("Enter a number")
  Result = Num1 * 2
  MsgBox("Result is " & Result)

  Dim Today As Date
  Today = Date
  Today = Today - 1
  ```

- `Option Explicit` -- declared at the top of the module. Forces us to declare variables properly. Otherwise, `Num1 * N2` will result in 0 as N2 is interpreted as a new variable of variant type that can morph into any value based on the expression at hand. Here, 0. 
- `A = P * (1 + I) ^ N`
- `A = P * (1 + R/N) ^ (N * T)` -- Rate of Interest, Number of times interest is compounded per unit time, Amount of time in years that money is invested

    ```vbscript
    Sub AgeInHours()

    Dim BirthDate As Date
    Dim AgeInHours As Long

    BirthDate = InputBox("Please enter your date of birth in mm/dd/yyyy format")

    AgeInHours = (Date - BirthDate) * 24

    MsgBox ("You are " & AgeInHours & " hours old")

    End Sub
    ```

## Programming in VBA

- [automateexcel.com]()
    ```vbscript
        If Not IsNumeric(P) Or Not IsNumeric(i) Then
        MsgBox("Enter valid data")
        Exit Sub
        End If

        If ... Then
        ... 
        ElseIf ... Then
        ...
        Else 
        ...
        End If 
    ```
- camelCase, UpperCamelCase, snake_case
- `PMT(rate, nper, pv)` -- annual interest rate, term of loan in years, loan amount
- `PMT(rate/12, nper*12, pv)` present value
- `Application.WorksheetFunction.Pmt(i/12, n * 12, P)`
  ```vbscript
    function FunctionName(name As String)
        FunctionName = "Hello " & name & "!" 'same as setting a return value
    End Function
  ```
- `A = CVErr(xlErrValue)` --- #VALUE! error
- Excel Add-in --- .xlam ; To create add-ins just save your functions to a separate excel workbook and save the file with the .xlam extension; Go to add add-ins, browse and import custom add-in file. Now these are available for you to use. The file should not contain anything other than the functions.
- Everything is Object; Objects have hierarchy. 
- Object Hierarchy
  - Application (Excel Itself)
  - Excel Workbook
    - Excel Worksheet
      - Range
      - Pivot Table
    - Excel Worksheet
      - Range 
      - Chart
- Properties : attribute of the object that describes its characteristics
- Methods : An action that you can take on the object
- `Range("A1").Value` ; `Sheets("Sheet1").Delete`
- `Applications.Workbooks("name").Sheets("name").Range("A1")`
  ```vbscript
    Sub CalculateAge()

    Dim BirthDate As Date
    Dim Interval As String
    'Dim AgeInHours As Long
    Dim Age As Long

    BirthDate = InputBox("Please enter your date of birth in mm/dd/yyyy format")
    Interval = InputBox("Please enter how you'd like your age to be calculated (months, weeks, days, or hours)")

    'AgeInHours = (Date - BirthDate) * 24

    If Interval = "months" Then
        Age = DateDiff("m", BirthDate, Date)
    ElseIf Interval = "weeks" Then
        Age = DateDiff("ww", BirthDate, Date)
    ElseIf Interval = "days" Then
        Age = DateDiff("d", BirthDate, Date)
    Else
        Age = DateDiff("h", BirthDate, Date)
    End If

    MsgBox ("You are " & Age & " " & Interval & " old")

    End Sub
  ```

## Userforms

- UserForm
- `Sub ShowForm() LPC.Show  End Sub`
- Controls : Label, Text, Frame, OptionButton, ComboBox, ListBox, Command
- `Unload LPC` -- form goes awaya and inputs are cleared.
- `LPC.LoanTerm.AddItem 10`
- `LPC.LoanTerm.ListIndex = 2`
  ```vbscript
    Private Sub Calculate_Click()
        'Calculates future value(A) of an initial investment (P)
        'based on the interest rate (i) and the number of years
        'over which the money will be invested (n)
        
        'Declare variables:
        Dim P           As String
        Dim i           As String
        Dim n           As String
        Dim A           As Double
        
        'Set variable values:
        P = CompoundInterest.AmtInvested.Value
        i = CompoundInterest.ROR.Value
        n = CompoundInterest.YrsInvested.Value
        
        
        'Validate user input
        
        
        If Not IsNumeric(P) Or Not IsNumeric(i) Or Not IsNumeric(n) Then
            MsgBox ("Please enter numeric input")
            Exit Sub
        End If
        
        'Calculate compound interest:
        
        If CompoundInterest.Monthly.Value = True Then
            A = P * ((1 + i / 12) ^ (n * 12))
        Else
            A = P * ((1 + i) ^ n)
        End If
        
        CompoundInterest.FIV.Caption = FormatCurrency(A)
    End Sub

    Private Sub Quit_Click()
        Unload CompoundInterest
    End Sub
  ```

## Working with Ranges in VBA

- `ActiveCell.Value`; `ActiveCell.Address`; `Range("B2").Value`; `Range("A1:D3").Select`
- `Sheets("Seet1").Select` 
- `ActiveCell.Offset(nrows, ncols).Select`
  ```vbscript
  Sub OffsetSelect()
    ActiveCell.Offset(-3,-3).Select
  End Sub

  Sub OffsetValue()
    ActiveCell.Offset(1,0).Value = "below"
    ActiveCell.Offset(0,2).Value = "two to the right"
    ActiveCell.Offset(-3,-3).Value = "three above and left"
    MsgBox(Cells(3, 3).Value)
  End Sub
  ```
- Object Browser `F2`
  ```vbscript
    Sub Exercise1()
        Dim ActiveVal As String
        Dim ActiveAddress As String
        Dim Message As String
        
        ActiveVal = ActiveCell.Value
        ActiveAddress = ActiveCell.Address
        
        Message = "The value of the active cell is: " & ActiveVal & "." & vbNewLine _
        & "The address of the active cell is: " & ActiveAddress & "."
        
        MsgBox (Message)
    End Sub

    Sub Exercise2()
        Range("C4:C10").Select
        Selection.Interior.ThemeColor = xlThemeColorAccent1
        Selection.Font.ThemeColor = xlThemeColorDark1
        Selection.Font.Bold = True
    End Sub

    Sub Exercise3()
        Cells(12, 4).Value = "Cells is swell!"
    End Sub


    Sub Exercise4()
        
        Selection.Interior.ThemeColor = xlThemeColorAccent1
    
        ActiveCell.Offset(-2, 0).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(-2, 1).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(-2, 2).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(-1, 2).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(0, 2).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(1, 2).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(2, 2).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(2, 1).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(2, 0).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(2, -1).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(2, -2).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(1, -2).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(0, -2).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(-1, -2).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(-2, -2).Interior.ThemeColor = xlThemeColorAccent1
        ActiveCell.Offset(-2, -1).Interior.ThemeColor = xlThemeColorAccent1
    End Sub
  ``` 
- Imposter Syndrome : Feeling that you are not good enough
  ```vbscript
    Range("A2").Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selecction.End(xlDown)).Select
    Selection.Copy
    Sheets("Archive").Select
    Selection.End(xlDown).Select
    ActiveCell.Offset(1, 0).Select
    ActiveSheet.Paste
    Range("A1").Select

    Sub FillNBold()
        Dim UserSelection As Range
        Set UserSelection = Application.InputBox("Please select a range", Type:=8)
        UserSelection.Select

        With Selection.Interior
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .ThemeColor = xlTemeColorAccent1
        End With

        Selection.Font.Bold = True
    End Sub
  ```

  ```vbscript
    Sub FreqDist()
        Dim Source As Range
        Dim Dest As Range

        Set Source = Application.InputBox("Please select a column of values", Type:= 8)
        Set Dest = Application.InputBox("Please select a destination cell", Type:= 8) 

        Source.Select
        Selection.Copy

        Dest.Select
        ActiveSheet.Paste

        Selection.RemoveDuplicates Columns:=1, Header:= x1No

        Dest.Select
        Range(Selection, Selection.End(xlDown)).Select

        Selection.Offset(0, 1).Formula = "=COUNTIF(" & Source.Address & "," & Dest.Address(0,0) & ")" ' Address(0,0) 0 indicates we want relative address
    End Sub
  ```

  ```vbscript
    Private Sub AddRecord_Click()
        
        If AddRecordForm.Username.Value = "" Then
            MsgBox ("Please enter a value for Username")
            Exit Sub
        End If
        
        If Application.WorksheetFunction.CountIf(Columns("A:A"), AddRecordForm.Username.Value) > 0 Then
            MsgBox ("Please enter a unique value for Username")
            Exit Sub
        End If
        
        Range("A1").End(xlDown).Select
        
        
        Selection.Offset(1, 0).Value = AddRecordForm.Username.Value
        Selection.Offset(1, 1).Value = AddRecordForm.EmployeeName.Value
        Selection.Offset(1, 2).Value = AddRecordForm.JobTitle.Value
        Selection.Offset(1, 3).Value = CDec(AddRecordForm.HourlyRate.Value)
        Selection.Offset(1, 4).Value = CInt(AddRecordForm.VacationHours.Value)
        
        AddRecordForm.Username.Value = ""
        AddRecordForm.EmployeeName.Value = ""
        AddRecordForm.JobTitle.Value = ""
        AddRecordForm.HourlyRate.Value = ""
        AddRecordForm.VacationHours.Value = ""
    End Sub

    Private Sub Quit_Click()
        Unload AddRecordForm
    End Sub
  ```
## Loops

- Step Into `F8`
- View > Locals window == built-in debugging tools
- Do Loop, Do While, Do Until, For ... Next, For Each .. In ... ....... Next
  ```vbscript
    Sub infinite()
        Dim counter As Integer
        counter = 1

        Do 
            If counter > 12 Then Exit Do
            MsgBox(counter)
            counter = counter + 1
        Loop


        Do While counter <= 12
            MsgBox(counter)
            counter = counter + 1
        Loop


        Do Until counter > 7 
            MsgBox(counter)
            counter = counter + 1
        Loop

        For counter = 1 To 5
            MsgBox(Counter)
        Next Coounter

        For counter = 0 To 10 Step 2 
            MsgBox(Counter)
        Next Counter        
    End Sub
    ```


    ```vbscript
    Sub CountToN()
        Dim Counter As Integer
        Dim Num As Integer

        Num = InputBox("Please enter a number")

        For Counter = 1 To Num
            ActiveCell.Offset(Counter - 1, 0).Value = Counter
        Next Counter
    End Sub

    Sub FindNegatives()
        Dim Counter As Integer
        Dim RCount As Integer
        Dim NegativeCount As Integer

        RCount = Selection.Rows.Count

        For Counter = 1 To RCount
            If Selection.Cells(Counter, 1).value < 0 Then
                Selection.Cells(Counter, 1).ClearContents
                NegativeCount NegativeCount + 1
            End If
        Next Counter

        MsgBox("NegativeCount :" & NegativeCount)
    End Sub   
    ```
    ```vbscriptf
    Sub FindNegatives2D()
        Dim A As Integer
        Dim B As Integer
        Dim RCount As Integer
        Dim CCount As Integer
        Dim NegativeCount As Integer

        RCount = Selection.Rows.Count
        CCount = Selection.Columns.Count

        For A = 1 To RCount
            For B = 1 To CCount
                If Selection.Cells(A, B).value < 0 Then
                    Selection.Cells(A, B).ClearContents
                    NegativeCount NegativeCount + 1
                End If
            Next B
        Next A

        MsgBox("NegativeCount :" & NegativeCount)
    End Sub   


    Sub FindNegativesForEach()
        Dim Cell As Range
        Dim NegativeCount As Integer

        For Each Cell In Selection
            If Cell.Value < 0 Then
                Cell.ClearContents
                NegativeCount = NegativeCount + 1
            End If
        Next Cell
    End Sub
  ```

- IsNumeric(P), LCase(String)
- `MsgBox("Please enter ""annual"" or ""monthly""")` -- we use two double quotes for escaping

- InSTR(containing_string, string_we_are_looking_for)
  ```vbscript
    Sub FindMatches()
        Dim Sel As Range
        Dim Target As Range
        Dim Cell As Range
        Dim Term As String
        Dim MatchCount As Integer

        Set Sel = Application.InputBox("Please select a range to search", Type:=8)
        Set Target = Application.InputBox("Please select a destination for list of matches", Type:=8)
        Term = InputBox("Please enter a search term")

        For Each Cell In Sel
            If InSTR(LCase(Cell.Value), LCase(Term)) >= 1 Then
                Target.Offset(MatchCount, 0).Value = Cell.Value
                Target.Offset(MatchCount, 1).Value = Cell.Address
                MatchCount = MatchCount + 1
            End If
        Next Cell

        MsgBox("There were " & MatchCount & " matches to your search term")
    End Sub
  ```

  ```vbscript
    Function ExtractNumbers(Str As String)
        Dim I As Integer
        Dim Result As String

        For I = 1 To Len(Str)
            If IsNumeric(Mid(Str, I, 1)) Then
                Result = Result & Mid(Str, I, 1)
            End If
        Next I

        ExtractNumbers = Result
    End Function
  ```

  ```vbscript
    Option Explicit

    Sub CreateGreenRectangle()
        Dim Height As Integer
        Dim Width As Integer
        
        Dim A As Integer
        Dim B As Integer
        
        Height = InputBox("How tall should the rectangle be (number of cells)?")
        Width = InputBox("How wide should the rectangle be (number of cells)?")
    
        For A = 1 To Height
            For B = 1 To Width
                ActiveCell.Offset(A - 1, B - 1).Interior.Color = 5287936
            Next B
        Next A
        
    End Sub

    Sub CountHighSales()

        Dim Cell As Range
        Dim Counter As Integer

        Sheets("Monthly Sales By Employee").Activate
        Range("B2").Select
        Range(Selection, Selection.End(xlToRight)).Select
        Range(Selection, Selection.End(xlDown)).Select
        
        For Each Cell In Selection
            If Cell.Value >= 200000 Then
                Counter = Counter + 1
            End If
        Next Cell
        
        MsgBox ("There were " & Counter & " instances of a salesperson selling at least $200,000 in a single month")
    End Sub


    Sub CheckPassword()

        Dim Password As String
        
        Dim Counter As Integer
        Dim CurrentChar As String
        Dim ErrorMsg As String
        
        Dim UCaseCount As Integer
        Dim LCaseCount As Integer
        Dim NumericCount As Integer
        Dim SpecialCount As Integer

        Do
            Password = InputBox("Please enter a password.")
            
            For Counter = 1 To Len(Password)
                CurrentChar = Mid(Password, Counter, 1)
                If IsNumeric(CurrentChar) Then
                    NumericCount = NumericCount + 1
                ElseIf LCase(CurrentChar) = UCase(CurrentChar) Then
                    SpecialCount = SpecialCount + 1
                ElseIf LCase(CurrentChar) = CurrentChar Then
                    LCaseCount = LCaseCount + 1
                ElseIf UCase(CurrentChar) = CurrentChar Then
                    UCaseCount = UCaseCount + 1
                End If
            Next Counter
            
            If Len(Password) < 8 Then
                ErrorMsg = ErrorMsg & "Passwords should be at least eight characters in length." & vbNewLine
            End If
            
            If NumericCount < 2 Then
                ErrorMsg = ErrorMsg & "Passwords should include at least two numbers." & vbNewLine
            End If
            
            If SpecialCount < 1 Then
                ErrorMsg = ErrorMsg & "Passwords should include at least one special character." & vbNewLine
            End If
            
            If LCaseCount < 1 Then
                ErrorMsg = ErrorMsg & "Passwords should include at least one lowercase letter." & vbNewLine
            End If
            
            If UCaseCount < 1 Then
                ErrorMsg = ErrorMsg & "Passwords should include at least one uppercase letter." & vbNewLine
            End If
            
            If Len(ErrorMsg) > 0 Then
                MsgBox ("Password not accepted:" & vbNewLine & ErrorMsg)
                ErrorMsg = ""
            Else
                MsgBox ("Password accepted!")
                Exit Do
            End If
        Loop
        
    End Sub
  ```

- `LCase(char) = UCase(char)` => char is a special character

## Arrays

- `Arr(3)` -- 0, 1, 2, 3
- `Option Base 1`; `Arr(3)` -- 1, 2, 3
- `Arr(1)` -- fetches value; `Arr(1) = "Value1"`
- `Dim NegativeNums() As Integer` -- empty array, re-dimming
- `ReDim NegativeNums(4)` -- resizes array and wipes out all data
- `ReDim Preserve NegativeNums(4)` -- resizes and preserves data
  ```vbscript
    Sub SummarizeNegatives()
        Dim Cell As Range
        Dim NegativeCount As Integer
        Dim NegativeNums() As Integer
        Dim Addresses() As String

        For Each Cell In Selection
            If Cell.Value < 0 Then
                NegativeCount = NegativeCount + 1
                ReDim Preserve NegativeNums(NegativeCount)
                ReDim Preserve Addresses(NegativeCount)
                NegativeNums(NegativeCount) = Cell.Value
                Addresses(NegativeCount) = Cell.Address
            End If
        Next Cell

        MsgBox("Minimum : " & Application.WorksheetFunction.Min(NegativeNums))
        MsgBox("Average : " & Application.WorksheetFunction.Average(NegativeNums))
        MsgBox("Standard Deviation : " & Application.WorksheetFunction.StDev_P(NegativeNums))
        MsgBox("Cell Addresses: " & Join(Addresses, ", "))
    End Sub
  ```

- Arrays returned by Split is 0-indexed and ignores Option Base 1
  ```vbscript
    Sub ThirdWord()
        Dim Sentence As Range
        Dim Words() As String

        Set Sentence = Application.InputBox("Please select a cell", Type:=8)

        Words = Split(Sentence.Value, " ")
        
        MsgBox(Words(2))
    End Sub


    Function NegativityScore(Sentence As String, NegativeWords As Range)
        Dim Words() As String
        Dim Counter As Integer
        Dim NegativeWordCount As Integer
        Dim Cell As Range

        Words = Split(Sentence, " ")

        For Counter = 0 To UBound(Words)
            For Each Cell In NegativeWords
                If LCase(Words(Counter)) = LCase(Cell.Value) Then
                    NegativeWordCount = NegativeWordCount + 1
                End If
            Next Cell
        Next Counter
        NegativityScore = NegativeWordCount
    End Function
  ```

  ```vbscript
    Option Base 1
    Sub ExerciseOne()
        Dim City As String
        Dim Cities As Range
        Dim Cell As Range
        Dim SalePrices() As Double
        Dim MatchCount As Integer
        Dim Result As String
        
        City = Application.InputBox("Please enter the name of a city")
    
        Range("B2").Select
        Range(Selection, Selection.End(xlDown)).Select
        
        Set Cities = Selection
        
        Range("A1").Select
        
        For Each Cell In Cities
            If LCase(Cell.Value) = LCase(City) Then
                MatchCount = MatchCount + 1
                ReDim Preserve SalePrices(MatchCount)
                SalePrices(MatchCount) = Cell.Offset(0, 2)
            End If
        Next Cell
        
        Result = "Average sale price in " & City & ": " & FormatCurrency(Application.WorksheetFunction.Average(SalePrices)) & vbNewLine
        Result = Result & "Median sale price in " & City & ": " & FormatCurrency(Application.WorksheetFunction.Median(SalePrices)) & vbNewLine
        Result = Result & "Standard Deviation of sale prices in " & City & ": " & FormatCurrency(Application.WorksheetFunction.StDev_P(SalePrices))

        MsgBox (Result)
    End Sub


    Sub ExerciseTwo()
        Dim Sales As Range
        Dim Cell As Range
        Dim Emails() As String
        Dim MatchCount As Integer

        Range("C2").Select
        Range(Selection, Selection.End(xlDown)).Select
        
        Set Sales = Selection
        
        Range("A1").Select
        
        For Each Cell In Sales
            If Cell.Value >= 800000 Then
                MatchCount = MatchCount + 1
                ReDim Preserve Emails(MatchCount)
                Emails(MatchCount) = Cell.Offset(0, -1)
            End If
        Next Cell
        
        Range("G2").Value = Join(Emails, ";")
    End Sub

    Function ExerciseThree(Text As String, NaughtyWords As Range)
        Dim Words() As String
        Dim Counter As Integer
        Dim Cell As Range
        
        Words = Split(Text, " ")
        
        For Counter = 0 To UBound(Words)
            For Each Cell In NaughtyWords
                If LCase(Words(Counter)) = Cell.Value Then
                    Words(Counter) = "****"
                End If
            Next Cell
        Next Counter
        
        ExerciseThree = Join(Words, " ")
    End Function
  ```
- `vbNewLine`

## Worksheets and Workbooks

- `Sheets("name")`; `Sheets(1)`
- `Sheets(1).Name`
- `Worksheets.Count`
- `Sheets(2).Delete`
- `Sheets.Add`
  ```vbscript
    Sub DeleteSheets()
        Application.DisplayAlerts = False

        Dim WS As Worksheet

        For Each WS In ThisWorkbook.Worksheets
            If WS.Name <> "Summary" Then
                WS.Delete
            End If
        Next WS

        Application.DisplayAlerts = True
    End Sub 


    Sub CreateSheets()
        Dim Names As Range
        Dim NumNames As Integer
        Dim Counter As Integer

        Set Names = Sheets("Names").Range("A:A")

        NumNames = Application.WorksheetFunction.CountA(Names)

        For Counter = 1 To NumNames
            Sheets.Add
            ActiveSheet.Name = Sheets("Names").Cells(Counter, 1).Value
            ActiveSheet.Range("A1").Vale = "Month"
            ActiveSheet.Range("B1").Vale = "Gross Sales"
        Next Counter
    End Sub
  ```

  ```vbscript
    Sub GenerateSummary()
        Dim WS As Worksheet
        Dim Months As Range
        Dim NumMonths As Integer
        Dim Counter As Integer

        Set Months = Sheets("Summary").Range("A:A")

        NumMonths = Application.WorksheetFunction.CountA(Months) - 1

        For Each WS In ThisWorkbook.Worksheets
            If WS.Name <> "Summary" Then
                For Counter = 1 To NumMonths
                    Sheets("Summary").Cells(Counter + 1, 2).Value = Sheets("Summary").Cells(Counter + 1, 2).Value + WS.Cells(Counter + 1, 2).Value
                Next Counter
            End If
        Next WS
    End Sub 
  ```

  ```vbscript
    Sub CreateFile()
        Dim Today As String
        Dim Path As String

        Today = Format(Date, "mm-dd-yyyy")
        Path = "Path to location " & Today & ".xlsx"

        Workbooks.Add
        ChDir "Path to the directory where file is saved"
        ActiveWorkBook.SaveAs Filename:= _
            Path, _
            FileFormat:= xlOpenXMLWorkbook, CreateBackup:= False
        ActiveCell.FormulaR1C1 = "VBA For Workbooks"
        ActiveWorkbook.Save
        ActiveWorkbook.Close
    End Sub
  ```

  ```vbscript
    Sub OpenWorkBooksInfo()
        Dim WB As Workbook

        For Each WB In Workbooks 
            MsgBox(WB.Name)
        Next WB

        MsgBox(Workbooks.Count)
    End Sub

    Sub OpenFiles()
        Dim Folder As String
        Dim FileName As String

        Folder = "Path to the folder"
        FileName = Dir(Folder & "*.xlsx")

        Do 
            Workbooks.Open(Folder & FileName)
            FileName = Dir
        Loop Unitl FileName = ""
    End Sub
  ```

  ```vbscript
    Sub ConsolidateWorksheets(WB As Workbook, NumMonths As Integer)
        Dim WS As Worksheet
        Dim Counter As Integer
        
        For Each WS In WB.Worksheets
            If WS.Name <> "Summary" Then
                For Counter = 1 To NumMonths
                    ThisWorkbook.Sheets("Summary").Cells(Counter + 1, 2).Value = ThisWorkbook.Sheets("Summary").Cells(Counter + 1, 2).Value + WS.Cells(Counter + 1, 2).Value
                Next Counter
            End If
        Next WS
    End Sub



    Sub ConsolidateWorkbooks()
        Dim Months As Range
        Dim NumMonths As Integer
        Dim Folder As String
        Dim FileName As String
        Dim WB As Workbook
        
        Set Months = Sheets("Summary").Range("A:A")
        
        NumMonths = Application.WorksheetFunction.CountA(Months) - 1
        
        Folder = "C:\Users\travi\Desktop\Courses\VBA Course\Example Files\Consolidating Workbooks\"
        
        FileName = Dir(Folder & "*.xlsx")
        
        Application.DisplayAlerts = False
        
        Do
            Workbooks.Open (Folder & FileName)
            FileName = Dir
        Loop Until FileName = ""
        
        For Each WB In Workbooks
            If InStr(WB.Name, ".xlsm") = 0 Then
                Call ConsolidateWorksheets(WB, NumMonths)
                WB.Close
            End If
        Next WB

        Application.DisplayAlerts = True

    End Sub
  ```

- Private subroutine can only be called by other VBA code within the same module
  ```vbscript
    Sub ConsolidateWorksheets(WB As Workbook)
        Dim WS As Worksheet
        Dim Cell As Range
        Dim Counter As Integer
        
        For Each WS In WB.Worksheets
            For Each Cell In WS.Range("B2:H17")
                If LCase(Cell.Value) = "y" Then
                    ThisWorkbook.Sheets("Schedule").Cells(Cell.Row, Cell.Column).Value = ThisWorkbook.Sheets("Schedule").Cells(Cell.Row, Cell.Column).Value + 1
                End If
            Next Cell
        Next WS
    End Sub



    Sub ConsolidateWorkbooks()
        Dim Folder As String
        Dim FileName As String
        Dim WB As Workbook
        
        Folder = "path to the folder"
        
        FileName = Dir(Folder & "*.xlsx")
        
        Range("B2:H17").ClearContents
        
        Application.DisplayAlerts = False
        
        Do
            Workbooks.Open (Folder & FileName)
            FileName = Dir
        Loop Until FileName = ""
        
        For Each WB In Workbooks
            If InStr(WB.Name, ".xlsm") = 0 Then
                Call ConsolidateWorksheets(WB)
                WB.Close
            End If
        Next WB

        Application.DisplayAlerts = True

    End Sub
  ```

  ```vbscript
    Private Sub Workbook_Open()
        Dim TargetRow As Integer
        Dim Entries As Range
        
        Set Entries = Range("A:A")
        
        TargetRow = Application.WorksheetFunction.CountA(Entries) + 1
        
        Cells(TargetRow, 1).Value = Now
    End Sub
  ```

- `Match(lookup_val, lookup_range, exact/inexact match)` --- 0 for exact match
  
  ```vbscript
    ' Edit Record Form
    Private Sub EditRecord_Click()

        If EditRecordForm.Username.Value = "" Then
            MsgBox ("Please enter a value for Username")
            Exit Sub
        End If
        
        If Application.WorksheetFunction.CountIf(Columns("A:A"), EditRecordForm.Username.Value) > 0 Then
            If Cells(RowNum.Value, 1) <> EditRecordForm.Username.Value Then
                MsgBox ("Please enter a unique value for Username")
                Exit Sub
            End If
        End If
        
        Cells(RowNum.Value, 1) = EditRecordForm.Username.Value
        Cells(RowNum.Value, 2) = EditRecordForm.EmployeeName.Value
        Cells(RowNum.Value, 3) = EditRecordForm.JobTitle.Value
        Cells(RowNum.Value, 4) = EditRecordForm.HourlyRate.Value
        Cells(RowNum.Value, 5) = EditRecordForm.VacationHours.Value
        
        Unload EditRecordForm
        Unload SearchForm
    End Sub
  ```

  ```vbscript
    ' Search form
    Private Sub Action_Click()
        Dim RowNum As Integer
        
        RowNum = Application.WorksheetFunction.Match(SearchForm.SearchResults.Value, Range("A:A"), 0)
        
        If ActionType.Value = "edit" Then
            Load EditRecordForm
            
            EditRecordForm.Username.Value = Cells(RowNum, 1)
            EditRecordForm.EmployeeName.Value = Cells(RowNum, 2)
            EditRecordForm.JobTitle.Value = Cells(RowNum, 3)
            EditRecordForm.HourlyRate.Value = Cells(RowNum, 4)
            EditRecordForm.VacationHours.Value = Cells(RowNum, 5)
            
            EditRecordForm.RowNum.Value = RowNum
            
            EditRecordForm.Show
        Else
            DeleteRecordForm.Show
        End If
    End Sub
  ```
## Pivot Tables

- `ThisWorkbook.RefreshAll` -- refreshes all external data connections
- `Sheets("Summary").PivotTables("CallCenterStats").RefreshTable`
- Uncheck Enable Background Refresh for Pivot Tables from PivotTable Analyze > Refresh > Connecction Properties
  ```vbscript
    Sub HideFields()

        If Sheets("Summary").PivotTables("TotalSales").PivotFields("Agent").Orientation <> xlHidden Then
        
            Sheets("Summary").PivotTables("TotalSales").PivotFields("Agent").Orientation = xlHidden
        End If
        
        If Sheets("Summary").PivotTables("TotalSales").PivotFields("SaleDate").Orientation <> xlHidden Then
        
            Sheets("Summary").PivotTables("TotalSales").PivotFields("SaleDate").Orientation = xlHidden
        End If
        
        If Sheets("Summary").PivotTables("TotalSales").PivotFields("Region").Orientation <> xlHidden Then
        
            Sheets("Summary").PivotTables("TotalSales").PivotFields("Region").Orientation = xlHidden
        End If
        
        If Sheets("Summary").PivotTables("TotalSales").PivotFields("City").Orientation <> xlHidden Then
        
            Sheets("Summary").PivotTables("TotalSales").PivotFields("City").Orientation = xlHidden
        End If
    End Sub


    Sub ShowAgent()

    Call HideFields
            
        With Sheets("Summary").PivotTables("TotalSales").PivotFields("Agent")
            .Orientation = xlRowField
            .Position = 1
        End With
    End Sub

    Sub ShowSaleDate()

    Call HideFields
            
        With Sheets("Summary").PivotTables("TotalSales").PivotFields("SaleDate")
            .Orientation = xlRowField
            .Position = 1
        End With
    End Sub

    Sub ShowCityRegion()

    Call HideFields
            
        With Sheets("Summary").PivotTables("TotalSales").PivotFields("Region")
            .Orientation = xlRowField
            .Position = 1
        End With
        
        With Sheets("Summary").PivotTables("TotalSales").PivotFields("City")
            .Orientation = xlRowField
            .Position = 2
        End With
            
    End Sub

    Sub RefreshData()
        Sheets("Summary").PivotTables("TotalSales").RefreshTable
    End Sub
  ```

- `Rows(4).Delete`
- `If MsgBox("Do you like me", vbYesNo) = vbYes Then  MsgBox("Yayy, you're awesome!")`

# 