import streamlit as st
import pandas as pd
from datetime import datetime
import os

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Attendance Management System",
    page_icon="📋",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align:center;
    color:#1f77b4;
    font-size:40px;
    font-weight:bold;
}

.card {
    padding:20px;
    border-radius:15px;
    background:white;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📋 Attendance Management System</div>",
            unsafe_allow_html=True)

# -----------------------------------
# FILE SETUP
# -----------------------------------
FILE_NAME = "attendance.csv"

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=[
        "Employee ID",
        "Employee Name",
        "Date",
        "Check In",
        "Check Out",
        "Working Hours"
    ])
    df.to_csv(FILE_NAME, index=False)

# -----------------------------------
# LOAD DATA
# -----------------------------------
attendance_df = pd.read_csv(FILE_NAME)

# -----------------------------------
# SIDEBAR
# -----------------------------------
menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Mark Attendance",
        "View Attendance",
        "Download Report"
    ]
)

# ===================================
# MARK ATTENDANCE
# ===================================
if menu == "Mark Attendance":

    st.subheader("🕒 Employee Attendance")

    col1, col2 = st.columns(2)

    with col1:
        emp_id = st.text_input("Employee ID")

    with col2:
        emp_name = st.text_input("Employee Name")

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    c1, c2 = st.columns(2)

    # CHECK-IN
    with c1:
        if st.button("✅ Check In", use_container_width=True):

            if emp_id and emp_name:

                new_record = {
                    "Employee ID": emp_id,
                    "Employee Name": emp_name,
                    "Date": today,
                    "Check In": current_time,
                    "Check Out": "",
                    "Working Hours": ""
                }

                attendance_df.loc[len(attendance_df)] = new_record
                attendance_df.to_csv(FILE_NAME, index=False)

                st.success(
                    f"{emp_name} checked in at {current_time}"
                )
            else:
                st.error("Please enter Employee Details")

    # CHECK-OUT
    with c2:
        if st.button("🚪 Check Out", use_container_width=True):

            mask = (
                (attendance_df["Employee ID"].astype(str) == str(emp_id))
                &
                (attendance_df["Date"] == today)
                &
                (attendance_df["Check Out"].isna() |
                 (attendance_df["Check Out"] == ""))
            )

            if mask.any():

                index = attendance_df[mask].index[-1]

                checkin_time = attendance_df.loc[index, "Check In"]

                in_time = datetime.strptime(
                    checkin_time,
                    "%H:%M:%S"
                )

                out_time = datetime.strptime(
                    current_time,
                    "%H:%M:%S"
                )

                duration = out_time - in_time

                attendance_df.loc[index,
                                  "Check Out"] = current_time

                attendance_df.loc[index,
                                  "Working Hours"] = str(duration)

                attendance_df.to_csv(FILE_NAME, index=False)

                st.success(
                    f"{emp_name} checked out at {current_time}"
                )

            else:
                st.warning(
                    "No active Check-In record found."
                )

# ===================================
# VIEW ATTENDANCE
# ===================================
elif menu == "View Attendance":

    st.subheader("📊 Attendance Records")

    search = st.text_input(
        "Search Employee Name / ID"
    )

    filtered_df = attendance_df.copy()

    if search:
        filtered_df = filtered_df[
            filtered_df["Employee Name"]
            .astype(str)
            .str.contains(search, case=False)
            |
            filtered_df["Employee ID"]
            .astype(str)
            .str.contains(search, case=False)
        ]

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    st.markdown("---")

    total_employees = filtered_df[
        "Employee ID"
    ].nunique()

    total_records = len(filtered_df)

    col1, col2 = st.columns(2)

    col1.metric(
        "Employees",
        total_employees
    )

    col2.metric(
        "Attendance Records",
        total_records
    )

# ===================================
# DOWNLOAD REPORT
# ===================================
elif menu == "Download Report":

    st.subheader("📥 Download Attendance Report")

    excel_file = "Attendance_Report.xlsx"

    attendance_df.to_excel(
        excel_file,
        index=False
    )

    with open(excel_file, "rb") as file:
        st.download_button(
            label="⬇ Download Excel Report",
            data=file,
            file_name=excel_file,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    st.dataframe(
        attendance_df,
        use_container_width=True
    )