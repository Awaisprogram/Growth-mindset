import streamlit as st
from datetime import datetime, timedelta

def main():
    st.title("🌱 My Growth Journey Dashboard 🌱")
    st.markdown("Track your learning and growth with this interactive dashboard.")

    # Initialize session state for progress data
    if 'progress_data' not in st.session_state:
        st.session_state.progress_data = []

    # --- Sidebar for Navigation and Quick Actions ---
    with st.sidebar:
        st.header("🧭 Navigation & Actions 🚀")
        page = st.radio("Explore:", ["Overview", "Log New Entry", "Learning Resources"])

        st.subheader("⚡ Quick Log")
        with st.form("quick_log_form"):
            quick_date = st.date_input("Date", datetime.now().date())
            quick_focus = st.text_input("Focus:")
            quick_hours = st.number_input("Hours:", min_value=0.0, max_value=24.0, step=0.5)
            quick_learnings = st.text_area("Quick Learning Point:")
            submitted_quick = st.form_submit_button("Add Quick Entry")

            if submitted_quick:
                if quick_focus and quick_hours > 0 and quick_learnings:
                    st.session_state.progress_data.insert(0, {
                        "Date": quick_date.strftime("%Y-%m-%d"),
                        "Focus": quick_focus,
                        "Hours": quick_hours,
                        "Learnings": quick_learnings,
                        "Challenges": "",
                        "Overcame": ""
                    })
                    st.success("Quick entry saved!")
                else:
                    st.error("Please fill in Date, Focus, Hours, and Quick Learning.")

    # --- Main Content Area ---
    if page == "Overview":
        show_overview()
    elif page == "Log New Entry":
        show_log_entry_form()
    elif page == "Learning Resources":
        show_resources()

def show_overview():
    st.header("📊 Your Growth Summary 📈")

    if st.session_state.progress_data:
        total_hours = sum(entry["Hours"] for entry in st.session_state.progress_data)
        num_entries = len(st.session_state.progress_data)
        latest_entry = st.session_state.progress_data[0]
        latest_focus = latest_entry["Focus"]
        latest_date = latest_entry["Date"]

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Learning Hours", f"{total_hours:.1f} hours")
        col2.metric("Total Entries", num_entries)
        col3.metric("Last Focus", f"{latest_focus} ({latest_date})")

        st.subheader("Learning Hours Over Time")
        # Prepare data for line chart
        chart_data = {}
        for entry in st.session_state.progress_data:
            date_str = entry["Date"]
            hours = entry["Hours"]
            if date_str not in chart_data:
                chart_data[date_str] = 0
            chart_data[date_str] += hours
        if chart_data:
            dates = sorted(chart_data.keys())
            hours_list = [chart_data[date] for date in dates]
            st.line_chart({"Date": dates, "Hours": hours_list}, x="Date", y="Hours")
        else:
            st.info("No learning data available for the chart yet.")

        st.subheader("Recent Activities")
        st.table(st.session_state.progress_data)
    else:
        st.info("No progress data available yet. Start logging your learning!")

def show_log_entry_form():
    st.header("📝 Log Your Learning Session")
    with st.form("new_progress_form"):
        date = st.date_input("Date", datetime.now().date())
        focus = st.text_input("What was your main focus of learning today?")
        hours = st.number_input("Hours spent learning:", min_value=0.0, max_value=24.0, step=0.5)
        learnings = st.text_area("Key takeaways and learnings:")
        challenges = st.text_area("What challenges did you encounter?")
        overcame = st.text_area("How did you overcome these challenges?")
        submitted = st.form_submit_button("Save Progress Entry")

        if submitted:
            errors = []
            if not date:
                errors.append("Please select a date.")
            if not focus:
                errors.append("Please describe your learning focus.")
            if hours <= 0:
                errors.append("Learning hours must be greater than 0.")
            if not learnings:
                errors.append("Please share your key learnings.")

            if errors:
                for error in errors:
                    st.error(error)
            else:
                st.session_state.progress_data.insert(0, {
                    "Date": date.strftime("%Y-%m-%d"),
                    "Focus": focus,
                    "Hours": hours,
                    "Learnings": learnings,
                    "Challenges": challenges,
                    "Overcame": overcame
                })
                st.success("Progress entry saved successfully!")

def show_resources():
    st.header("📚 Learning Resources & Inspiration ✨")

    st.subheader("Recommended Reads 📖")
    st.markdown("* **Mindset: The New Psychology of Success** by Carol S. Dweck")
    st.markdown("* **Atomic Habits** by James Clear")
    st.markdown("* **Deep Work: Rules for Focused Success in a Distracted World** by Cal Newport")

    st.subheader("Inspiring Talks & Articles 💡")
    st.markdown("* [TED Talk: The power of believing that you can improve](https://www.ted.com/talks/carol_dweck_the_power_of_believing_that_you_can_improve)")
    st.markdown("* [Article: What is a Growth Mindset?](https://www.mindsetworks.com/science/impact)")
    st.markdown("* [Blog Post: Cultivating a Growth Mindset](https://fs.blog/2015/01/growth-mindset/)")

    st.subheader("Your Notes & Reflections 📝")
    st.text_area("Space for your thoughts and reflections on your learning journey.")

if __name__ == "__main__":
    main()
