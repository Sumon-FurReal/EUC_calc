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

remote_support_ticket = total_ticket * 0.4
    remote_tickets_per_month = remote_support_ticket / 12

    field_support_ticket = total_ticket * 0.6
    field_tickets_per_month = field_support_ticket / 12

    # For 24x7 Remote
    remote_tickets_per_day_24x7 = remote_support_ticket / 31
    remote_support_FTE_24x7 = remote_tickets_per_day_24x7 / 6

    # For 24x7 Field
    field_tickets_per_day_24x7 = field_support_ticket / 31
    field_support_FTE_24x7 = field_tickets_per_day_24x7 / 5

    # For 8x5 Remote
    remote_tickets_per_day_8x5 = remote_support_ticket / 22
    remote_support_FTE_8x5 = remote_tickets_per_day_8x5 / 6

    # For 8x5 Field
    field_tickets_per_day_8x5 = field_support_ticket / 22
    field_support_FTE_8x5 = field_tickets_per_day_8x5 / 5

    return remote_tickets_per_month, field_tickets_per_month, \
        remote_tickets_per_day_24x7, field_tickets_per_day_24x7, \
        remote_support_FTE_24x7, field_support_FTE_24x7, \
        remote_tickets_per_day_8x5, field_tickets_per_day_8x5, \
        remote_support_FTE_8x5, field_support_FTE_8x5


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
        (remote_tickets_per_month, field_tickets_per_month, remote_tickets_per_day_24x7, field_tickets_per_day_24x7,
         remote_support_FTE_24x7, field_support_FTE_24x7, remote_tickets_per_day_8x5, field_tickets_per_day_8x5,
         remote_support_FTE_8x5, field_support_FTE_8x5) = calculate_resources(input_type, total_input)

        df_tickets = pd.DataFrame({"Metric": ["Remote Tickets per Month", "Field Tickets per Month"],
                                   "value": [remote_tickets_per_month, field_tickets_per_month]
                                   })
        df_tickets.index = (df_tickets.index + 1).astype(str)
        st.write("##### Ticket Count")
        st.table(df_tickets)

        df_24x7 = pd.DataFrame({
            "Metric": ["Remote Tickets per Day (24x7)", "Field Tickets per day (24x7)", "Remote FTE Required (24x7)", "Field FTE Required (24x7)"],
            "Value": [remote_tickets_per_day_24x7, field_tickets_per_day_24x7, remote_support_FTE_24x7, field_support_FTE_24x7]
        })
        df_24x7.index = (df_24x7.index + 1).astype(str)
        st.write("##### Results 24x7 ")
        st.table(df_24x7)

        df_8x5 = pd.DataFrame({
            "Metric": ["Remote Tickets per Day (8x5)", "Field Tickets per day (8x5)", "Remote FTE Required (8x5)", "Field FTE Required (8x5)"],
            "Value": [remote_tickets_per_day_8x5, field_tickets_per_day_8x5, remote_support_FTE_8x5, field_support_FTE_8x5]
        })
        df_8x5.index = (df_8x5.index + 1).astype(str)
        st.write("##### Results 8x5")
        st.table(df_8x5)


if __name__ == "__main__":
    main()
