# Streamlit

- Industry workflow 
  - Step 1
    - define the business need
    - use case - what and why
    - data
    - set the metrics list
  - Step 2
    - EDA 
    - Prototype in Sandbox
    - Present and Collect Feedback
    - Update
  - Step 3 
    - Deploy
    - Present to wider audience
    - Collect feedback
    - Update
  - Step 4
    - Integrate into stakeholders workflow
    - Maintain and Upgrade

- ![](assets/2024-07-05-21-39-56.png)


# Streamlit Docs

- `python -m streamlit run your_script.py` | `streamlit run your_script.py`
- `-- args` -- treats as user args `-args` --treats as args to streamlit
- `streamlit run url_to_application.py`
- Pandas Styler object to highlight elements of a table `st.dataframe(dataframe.style.highlight_max(axis=0))`
- `Matplotlib, Altair, Deck.gl, Bokeh, Plotly, ...`
- `.streamlit/secrets.toml` -- holds connection details; type, username, password. host, port. database, ...
- `pages/page_name[s]` -- create multiple pages by adding single pages to the pages folder
- static file serving -- to get direct url to the app files by the user, they need to be placed in static folder `static/files.*`
- `pytest` for streamlit app testing
- cached values are stored by reference and hence mutating the output of a function cached should be avoided
- Streamlit Server -- Host -- Python backend server -- the machine that runs `streamlit run` command
- App Chrome -- includes a status area, toolbar, 



<br/><br/>

- `st.write()`
- `st.dataframe()`
- `st.table()`
- `st.line_chart()`
- `st.bar_chart()`
- `st.pydeck_chart()`
- `st.map()`
- `st.slider()`
- `st.button()`
- `st.selectbox()`
- `st.sidebar`
  - `st.sidebar.slider`
  - `st.sidebar.selectbox`
- `st.columns`
- `st.expander`
- `st.echo`
- `st.spinner`
- `st.progress()`
- `st.empty()`
- `@st.cache_data` -- it creates a new copy of the data at each function call making it safe against mutations and race conditions; anything you can store in a database
- `@st.cache_resource` -- to cache global resources such as ML Models or database connections. Returns the object itself and is shared across all reruns and sessions; anything you can't store in a database
- `st.session_state`
  - `st.session_state["key_notation"]`
  - `st.session_state.attribute_notation`
  - values in session state are only available in the single session where it was saved
  - recommended to be used when pulling data specific to a user
- 
