import datetime
import pandas as pd

import streamlit as st
from session import session_update

def handle_form_submit(*args, **kwargs):
    print(args)
    print(kwargs)
    # if st.session_state.submitted:
        
        # Make a dataframe for the new ticket and append it to the dataframe in session
        # state.
        # recent_ticket_number = int(max(st.session_state.df.ID).split("-")[1])
        # today = datetime.datetime.now().strftime("%m-%d-%Y")
        # df_new = pd.DataFrame(
        #     [
        #         {
        #             "ID": f"TICKET-{recent_ticket_number+1}",
        #             "Issue": issue,
        #             "Status": "Open",
        #             "Priority": priority,
        #             "Date Submitted": today,
        #         }
        #     ]
        # )
        # session_update({"df": df_new})
        # # Show a little success message.
        # st.write("Your recommendation was submitted! Here are the details:")
        # st.dataframe(df_new, use_container_width=True, hide_index=True)
        # st.session_state.df = pd.concat([df_new, st.session_state.df], axis=0)