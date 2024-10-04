import altair as alt
import streamlit as st

from form_submission import handle_form_submit

def load_page():
    # Title.
    st.set_page_config(page_title="Tea reviews", page_icon="🫖")
    st.title("🫖 Tea reviews")
    st.write(
        """
        A list of teas that I tried and their reviews.  
        """
    )

    # Form.
    st.header("Recommend your favorite tea")
    st.write(
        """
        I'd love to try your recommended tea.
        Any recommendations (except for vanilla- or caramel-flavoured ones) are welcomed!
        """
    )
    with st.form("add_recommendation_form"):
        brand = st.text_input("Brand",
                            max_chars=64,
                            placeholder="e.g., Lipton")
        name = st.text_input("Name",
                            max_chars=128,
                            placeholder="e.g., I don't remember the name but the standard black tea.")
        st.session_state.submitted = st.form_submit_button("Submit", 
                                                           on_click=handle_form_submit,
                                                           kwargs={
                                                               "brand": brand,
                                                               "name": name
                                                           })


    # Show section to view and edit existing tickets in a table.
    st.header("Reviews")
    st.write(f"Number of reviews: `{len(st.session_state.df)}`")
    st.dataframe(st.session_state.df)
    # st.info(
    #     "You can edit the tickets by double clicking on a cell. Note how the plots below "
    #     "update automatically! You can also sort the table by clicking on the column headers.",
    #     icon="✍️",
    # )

    # # Show the tickets dataframe with `st.data_editor`. This lets the user edit the table
    # # cells. The edited data is returned as a new dataframe.
    # edited_df = st.data_editor(
    #     st.session_state.df,
    #     use_container_width=True,
    #     hide_index=True,
    #     column_config={
    #         "Status": st.column_config.SelectboxColumn(
    #             "Status",
    #             help="Ticket status",
    #             options=["Open", "In Progress", "Closed"],
    #             required=True,
    #         ),
    #         "Priority": st.column_config.SelectboxColumn(
    #             "Priority",
    #             help="Priority",
    #             options=["High", "Medium", "Low"],
    #             required=True,
    #         ),
    #     },
    #     # Disable editing the ID and Date Submitted columns.
    #     disabled=["ID", "Date Submitted"],
    # )

    # # Show some metrics and charts about the ticket.
    # st.header("Statistics")

    # # Show metrics side by side using `st.columns` and `st.metric`.
    # col1, col2, col3 = st.columns(3)
    # num_open_tickets = len(st.session_state.df[st.session_state.df.Status == "Open"])
    # col1.metric(label="Number of open tickets", value=num_open_tickets, delta=10)
    # col2.metric(label="First response time (hours)", value=5.2, delta=-1.5)
    # col3.metric(label="Average resolution time (hours)", value=16, delta=2)

    # # Show two Altair charts using `st.altair_chart`.
    # st.write("")
    # st.write("##### Ticket status per month")
    # status_plot = (
    #     alt.Chart(edited_df)
    #     .mark_bar()
    #     .encode(
    #         x="month(Date Submitted):O",
    #         y="count():Q",
    #         xOffset="Status:N",
    #         color="Status:N",
    #     )
    #     .configure_legend(
    #         orient="bottom", titleFontSize=14, labelFontSize=14, titlePadding=5
    #     )
    # )
    # st.altair_chart(status_plot, use_container_width=True, theme="streamlit")

    # st.write("##### Current ticket priorities")
    # priority_plot = (
    #     alt.Chart(edited_df)
    #     .mark_arc()
    #     .encode(theta="count():Q", color="Priority:N")
    #     .properties(height=300)
    #     .configure_legend(
    #         orient="bottom", titleFontSize=14, labelFontSize=14, titlePadding=5
    #     )
    # )
    # st.altair_chart(priority_plot, use_container_width=True, theme="streamlit")