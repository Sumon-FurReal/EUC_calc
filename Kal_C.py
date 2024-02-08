import streamlit as st
import pandas as pd
from PIL import Image

# Image Source
image = Image.open("Go Flex.png")


def calculate_resources(input_type, total_input):
    if input_type == "Total Users":
        total_ticket = total_input * 1.2
    else:
        total_ticket = total_input

    total_ticket_per_month = total_ticket / 12

    total_rs_ticket_per_month = total_ticket_per_month * 0.4
    total_fs_ticket_per_month = total_ticket_per_month * 0.6

    # 24x7
    total_rs_ticket_per_day_24x7 = total_rs_ticket_per_month / 31
    total_fs_ticket_per_day_24x7 = total_fs_ticket_per_month / 31

    # 8x5
    total_rs_ticket_per_day_8x5 = total_rs_ticket_per_month / 22
    total_fs_ticket_per_day_8x5 = total_fs_ticket_per_month / 22

    # FTE-24x7
    rs_count_24x7 = total_rs_ticket_per_day_24x7 / 6
    fs_count_24x7 = total_fs_ticket_per_day_24x7 / 5

    # FTE-8x5
    rs_count_8x5 = total_rs_ticket_per_day_8x5 / 6
    fs_count_8x5 = total_fs_ticket_per_day_8x5 / 5

    return total_ticket_per_month, total_rs_ticket_per_month, total_fs_ticket_per_month, \
        total_rs_ticket_per_day_24x7, total_fs_ticket_per_day_24x7, \
        total_rs_ticket_per_day_8x5, total_fs_ticket_per_day_8x5, \
        rs_count_24x7, fs_count_24x7, \
        rs_count_8x5, fs_count_8x5


def main():
    st.title("EUC Resource Calculator :rocket:")
    st.info("Assumptions:\n\n"
            "- Total ticket count is assumed to be 1.2 times the total number of users in case of calculation by Total Users .\n"
            "- 40% of the total tickets are considered for remote support.\n"
            "- 60% of total tickets are considered for field support.\n\n"
            "Please note that these numbers are approximate values and may not represent the exact count.")
    st.sidebar.image(image)
    st.sidebar.title("Resource Calculator")
    st.sidebar.write("Calculate By:")
    input_type = st.sidebar.radio("", ("Total Users", "Total Ticket", ))

    if input_type == "Total Ticket":
        total_input = st.number_input("Enter Total Ticket:", min_value=0)
    else:
        total_input = st.number_input("Enter Total Users:", min_value=0)

    if st.button("Calculate"):
        (total_ticket_per_month, total_rs_ticket_per_month, total_fs_ticket_per_month, total_rs_ticket_per_day_24x7,
         total_fs_ticket_per_day_24x7, total_rs_ticket_per_day_8x5, total_fs_ticket_per_day_8x5, rs_count_24x7, fs_count_24x7,
         rs_count_8x5, fs_count_8x5) = calculate_resources(input_type, total_input)

        df_tickets = pd.DataFrame({"Metric": ["Total Tickets per Month", "Remote Tickets per Month", "Field Tickets per Month"],
                                   "value": [total_ticket_per_month, total_rs_ticket_per_month, total_fs_ticket_per_month]
                                   })
        df_tickets.index = (df_tickets.index + 1).astype(str)
        st.write("##### Ticket Count")
        st.table(df_tickets)

        df_24x7 = pd.DataFrame({
            "Metric": ["Remote Tickets per Day (24x7)", "Field Tickets per day (24x7)", "Remote FTE Required (24x7)", "Field FTE Required (24x7)"],
            "Value": [total_rs_ticket_per_day_24x7, total_fs_ticket_per_day_24x7, rs_count_24x7, fs_count_24x7]
        })
        df_24x7.index = (df_24x7.index + 1).astype(str)
        st.write("##### Results 24x7 ")
        st.table(df_24x7)

        df_8x5 = pd.DataFrame({
            "Metric": ["Remote Tickets per Day (8x5)", "Field Tickets per day (8x5)", "Remote FTE Required (8x5)", "Field FTE Required (8x5)"],
            "Value": [total_rs_ticket_per_day_8x5,  total_fs_ticket_per_day_8x5, rs_count_8x5, fs_count_8x5]
        })
        df_8x5.index = (df_8x5.index + 1).astype(str)
        st.write("##### Results 8x5")
        st.table(df_8x5)


if __name__ == "__main__":
    main()
