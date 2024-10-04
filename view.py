import math

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
        Let me try your favorite tea!
        Any recommendations are welcomed (except for vanilla- or caramel-flavoured ones).
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

    # Table.
    st.header("Reviews")
    st.write(f"Number of reviews: `{len(st.session_state.df)}`")
    visualise_df = st.session_state.df.copy()
    visualise_df['score'] = visualise_df['score'].apply(lambda score: f"{str(score)} " + ("⭐️" * math.floor(score)))
    st.dataframe(
        visualise_df,
        column_config={
            "date_added": st.column_config.DatetimeColumn(
                "date added",
                format="DD-MM-YYYY"
            ),
            "link": st.column_config.LinkColumn(
                "link",
                width="small"
            )
        }
        )
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

    st.divider()
    st.header("Statistics")

    # Metrics.
    col1_1, col1_2 = st.columns(2)
    num_reviewed_brands = st.session_state.df['brand'].nunique()
    col1_1.metric(label="Number of teas reviewed", 
                  value=len(st.session_state.df))
    col1_2.metric(label="Number of brands reviewed", 
                  value=num_reviewed_brands)
    
    col2_1, col2_2 = st.columns(2)
    col2_1.metric(label="Average score", 
                  value=round(st.session_state.df['score'].mean(), 2))
    col2_2.metric(label="Standard deviation of the scores", 
                  value=round(st.session_state.df['score'].std() ,2))
    
    # Distribution.
    st.write("")
    st.write("##### Score distribution")
    score_plot = (
        alt.Chart(st.session_state.df)
        .mark_bar()
        .encode(
            alt.X("score:Q", 
                  bin=alt.Bin(step=0.5),
                  scale=alt.Scale(domain=[0.0,5,0])),
            alt.Y("count()"),
            alt.Color("score",
                      bin=alt.Bin(step=0.5),
                      scale=alt.Scale(scheme="pinkyellowgreen"))
        )
        .configure_legend(
            orient="bottom", 
            titleFontSize=14, 
            labelFontSize=14, 
            titlePadding=5
        )
    )
    st.altair_chart(score_plot, use_container_width=True, theme="streamlit")

    st.write("##### Current reviewed genres")
    genre_plot = (
        alt.Chart(st.session_state.df)
        .mark_arc()
        .encode(theta="count():Q", color="genre:N")
        .properties(height=300)
        .configure_legend(
            orient="bottom", titleFontSize=14, labelFontSize=14, titlePadding=5
        )
    )
    st.altair_chart(genre_plot, use_container_width=True, theme="streamlit")