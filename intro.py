def intro():
    import streamlit as st

    st.markdown(
        """
        # Goal ⛰
        >*The goal of this analysis is to get a more intiment understanding of how
        real users are talking about us and competitors on Credit Karma. In turn this should provide actionable
        insights to improve our experience with. **Note:** Each dataset is only using a total of 35 pages worth of reviews. 
        This means it's not over a specific period of time and that they aren't exactly even by size or time.*
        
        ---
        
        # Strategy
        ### Text Analysis
        Apply several text mining methods to the unstructured responses that users submit on Credit Karma. 

        ** Methods ** \n
        1. N-Grams
        2. Nounchunks
        3. Sentiment (WIP)
        4. Topic Modeling (WIP)

        ### Ratings Analysis
        Plot ratings over a series of charts to better understand these scores.
        
        ** Charts ** \n
        1. Ratings Distribution
        2. Total Trend Analysis
        3. Month of Year
        4. Day of Week
        
        ---
        
        #  Dataset

        ** Companies **  \n
        1. Payoff
        2. Upstart
        3. SoFi
        4. Others... TBD

        ** Websites **  \n
        1. Credit Karma
        2. Other... TBD
        
    """
    )

    