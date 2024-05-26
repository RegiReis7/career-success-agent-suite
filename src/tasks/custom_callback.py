import streamlit as st
from crewai.tasks.task_output import TaskOutput


def writeTaskResult(task: TaskOutput):
    st.divider()
    st.subheader(task.summary)
    st.caption(task.description)
    with st.expander("See the task output"):
        st.write(task.raw_output)
    
    return None
