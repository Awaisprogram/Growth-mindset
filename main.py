import streamlit as st
from datetime import datetime, timedelta

def main():
    st.title("Growth Mindset Dashboard")
    st.write("Welcome to your personal growth tracker!")
    
    # Add a sidebar for navigation
    with st.sidebar:
        st.header("Navigation")
        page = st.radio("Select a page:", ["Dashboard", "Progress Tracker", "Resources"])
    
    # Main content based on selection
    if page == "Dashboard":
        show_dashboard()
    elif page == "Progress Tracker":
        show_progress_tracker()
    else:
        show_resources()

def show_dashboard():
    st.header("Your Growth Dashboard")
    
    # Sample metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Learning Hours", value="42", delta="8")
    with col2:
        st.metric(label="Books Read", value="5", delta="1")
    with col3:
        st.metric(label="Challenges Completed", value="12", delta="3")
    
    # Sample chart
    st.subheader("Weekly Progress")
    dates = [datetime.now().date() - timedelta(days=x) for x in range(6, -1, -1)]
    chart_data = {
        'Date': dates,
        'Learning': [4, 3, 5, 2, 4, 3, 5],
        'Practice': [2, 4, 3, 4, 3, 5, 4],
        'Reflection': [3, 3, 4, 3, 5, 4, 3]
    }
    st.line_chart(chart_data, x='Date')
    
    st.info("Remember: Growth is a continuous process, and every step counts. 🚀")

def show_progress_tracker():
    st.header("Track Your Progress")
    
    # Initialize session state for progress data if it doesn't exist
    if 'progress_data' not in st.session_state:
        st.session_state.progress_data = {
            "Date": ["2023-06-01", "2023-06-02", "2023-06-03"],
            "Hours": [2.5, 1.0, 3.0],
            "Topic": ["Python Basics", "Data Visualization", "Machine Learning"]
        }
    
    # Sample form for logging progress
    with st.form("progress_form"):
        date = st.date_input("Date", datetime.now().date())
        hours = st.number_input("Hours spent learning", min_value=0.0, max_value=24.0, step=0.5)
        topic = st.text_area("What did you learn today?")
        st.text_area("Challenges faced")
        st.text_area("How did you overcome them?")
        submitted = st.form_submit_button("Save Progress")
        
        if submitted:
            errors = []
            if not date:
                errors.append("Please select a date.")
            if hours <= 0:
                errors.append("Hours spent learning must be greater than 0.")
            if not topic:
                errors.append("Please describe what you learned.")

            if errors:
                for error in errors:
                    st.error(error)
            else:
                # Add new entry to progress data
                st.session_state.progress_data["Date"].insert(0, date.strftime("%Y-%m-%d"))
                st.session_state.progress_data["Hours"].insert(0, hours)
                st.session_state.progress_data["Topic"].insert(0, topic)

                st.success("Progress saved successfully!")
                st.write("Your progress has been recorded. Keep up the good work!")
    
    # Display progress data
    st.subheader("Recent Progress")
    st.table(st.session_state.progress_data)

def show_resources():
    st.header("Growth Mindset Resources")
    
    st.subheader("Recommended Books")
    books = [
        {"title": "Mindset: The New Psychology of Success", "author": "Carol S. Dweck"},
        {"title": "Atomic Habits", "author": "James Clear"},
        {"title": "Deep Work", "author": "Cal Newport"}
    ]
    for book in books:
        st.write(f"**{book['title']}** by {book['author']}")
    
    st.subheader("Helpful Articles")
    st.markdown("* [The Power of Believing You Can Improve](https://www.ted.com/talks/carol_dweck_the_power_of_believing_that_you_can_improve)")
    st.markdown("* [Growth Mindset: A Driving Philosophy](https://fs.blog/carol-dweck-mindset/)")
    st.markdown("* [Fixed vs. Growth: The Two Basic Mindsets That Shape Our Lives](https://www.brainpickings.org/2014/01/29/carol-dweck-mindset/)")

if __name__ == "__main__":
    main()
