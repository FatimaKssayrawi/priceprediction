import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# Define custom CSS styles
custom_css = """
<style>
    body {
        background-color: #f5f5f5; /* Background color for the entire page */
        font-family: Arial, sans-serif; /* Font for the entire page */
    }

    .title {
        font-size: 30px; /* Font size for the title */
        color: #000; /* Set title color to black */
        text-align: center; /* Center the title */
        padding: 5px 0; /* Add some padding */
    }

    .container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .column {
        width: 45%; /* Adjust the width as needed */
        background-color: #fff; /* Background color for the columns */
        border: 1px solid #ddd; /* Add a border around columns */
        padding: 10px; /* Add padding to columns */
        margin: 10px 0; /* Add margin between columns */
    }

    .text-input {
        background-color: #eee; /* Background color for text inputs */
    }
</style>
"""


def display_day_of_week(choice):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    st.write(f"**You chose {days_of_week[choice]}.**")


def display_month(choice):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    st.write(f"**You chose {months[choice - 1]}.**")  # Adjusting for 1-based indexing of months


# Main function to run the Streamlit app
def main():
    st.set_page_config(
        page_title="Price Prediction",
        page_icon="✅",
        layout="wide"  # Use wide layout for fixed sidebar
    )
    
    # Include custom CSS styles

    # Sidebar style
    st.sidebar.title("Navigation Menu")
    menu = st.sidebar.selectbox("Choose an option:", ["Home", "Crew-Edit EDA", "Production EDA", "Transmission EDA", "Crew-Edit Price Prediction", "Production Price Prediction",
                                                      "Transmission Price Prediction"])

    if menu == "Home":
        image1 = "logo.jpg"
        image2 = "logo2.jpg"

        st.markdown(custom_css, unsafe_allow_html=True)
        # Display images on the top left and top right
        st.image(image1, width=200)
        st.image(image2, width=100)
        st.markdown('<p class="title"> Amar Abbani </p>', unsafe_allow_html=True)
        st.markdown('<p class="title"> Welcome to Predictive Dynamics: Crew-Edit, Production, Transmission, and Beyond </p>', unsafe_allow_html=True)
        st.write("Tailored Predictions Across Crew-Edit, Production, and Transmission Departments: Your Insights, Your Way!")
        
        col1, col2 = st.columns(2)
        # Display images in each column
        with col1:
            st.image("col2.png", use_column_width=True)
        with col2:
            st.image("col3.png", use_column_width=True)        
        
        st.write("The fast pace technological era we live in has forced industries of all sorts to constantly evolve at a rapid pace, "
                 "one industry who has to go through significant conversions is the broadcasting industry, it is crucial for companies in this segment "
                 "adjust and optimize their strategies constantly. Founded in the year 2000 in Beirut city, ISOL, a leading supplier of communications "
                 "solutions which includes specialist broadcast solutions, media facilities, and operational services stands at the head of this complex dynamic environment. "
                 "By offering a wide range of services, such as production, editing, and post-production, media monitoring, news gathering and transmission, and satellite "
                 "space capacity, ISOL has established out a unique place for itself in the market. Due to its wide range of services, "
                  "which it offers to both domestic and foreign customers, the company has established itself as a major participant in the market.")
        st.write("")  # This adds an empty line
        col3, col4 = st.columns(2)
        # Display images in the second row
        with col3:
            st.image("col5.png", use_column_width=True)        
        with col4:
            st.image("col6.png",  use_column_width=True)
        st.write("Although ISOL how's experienced success it still needs to overcome obstacles common to the broadcast sector this includes intricate "
                 "and ever-changing pricing schemes and the requirement for the efficient use of resources the dynamic character of the customer and the swift "
                 "advancements of the transmission technologies also leads to a more intricate and multifaceted pricing Scheme. Managing operational efficiency "
                 "requires optimizing the use of the resources such as the personnel equipment and studios needed for the job.")
    
        
    if menu == "Crew-Edit EDA":
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown('<p class="title"> Crew-Edit EDA </p>', unsafe_allow_html=True)
        st.write("")


        # Load data
        data = pd.read_csv("crew-edit.csv")

        # Setting the aesthetic style of the plots
        sns.set(style="whitegrid")
        # Sidebar with user input
        st.sidebar.header("Filter Options")
        st.sidebar.header("Distribution of Jobs Across Clients")
        num_clients_to_display = st.sidebar.slider("Number of Clients to Display", min_value=1, max_value=len(data['Client'].unique()), value=5)
        selected_clients = st.sidebar.multiselect("Select Clients", data['Client'].unique(), default=data['Client'].unique()[:num_clients_to_display])
        if not selected_clients:
            st.error("Please choose at least one client.")
        else:
            # Filter data based on user input
            filtered_data = data[data['Client'].isin(selected_clients)]
            # Setting the aesthetic style of the plots
            sns.set(style="whitegrid")
            # Distribution of jobs across clients
            client_distribution = filtered_data['Client'].value_counts()
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            sns.barplot(x=client_distribution.values, y=client_distribution.index, palette="viridis", ax=ax1)
            ax1.set_title('Distribution of Jobs Across Selected Clients')
            ax1.set_xlabel('Number of Jobs')
            ax1.set_ylabel('Client')
            st.pyplot(fig1)
            st.write("The bar plot above showcases the number of jobs per client. The length of the bars clearly indicates which clients are bringing in the most work. ")
            st.write("")  # This adds an empty line
            st.write("")
        
        
        # Distribution of jobs by type
        st.sidebar.header("Distribution of Jobs by Type")
        # Allow user to choose the number of types and specific types
        selected_num_types = st.sidebar.slider("Select Number of Types", min_value=1, max_value=len(data['Type'].unique()), value=3)
        selected_types = st.sidebar.multiselect("Select Types of Services", data['Type'].unique(), default=data['Type'].unique()[:selected_num_types])

        # Display an error if no service is selected
        if not selected_types:
            st.error("Please choose at least one type.")
        else:
            # Filter data based on selected types
            filtered_data_types = data[data['Type'].isin(selected_types)]
            type_distribution = filtered_data_types['Type'].value_counts()
            fig2, ax2 = plt.subplots(figsize=(8, 5))
            sns.barplot(x= type_distribution.values, y=type_distribution.index, data=filtered_data_types, palette="mako", ax=ax2)
            ax2.set_title('Distribution of Jobs by Selected Types')
            ax2.set_xlabel('Type of Service')
            ax2.set_ylabel('Number of Jobs')
            ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
            st.pyplot(fig2)
            st.write("The bar plot above visualizes the distribution of jobs by their type, showing the frequency of each service type offered by the company. ")
            st.write("")  # This adds an empty line
            st.write("")
       
        
        # Visualization: Jobs over time
        # Ensure 'Date' column is in datetime format
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
        # Creating a new column 'Month' for aggregating data by month
        data['Month'] = data['Date'].dt.to_period('M')
        # Aggregating job counts by month
        jobs_over_time = data.groupby('Month').size()
        # Visualization: Jobs over time
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        jobs_over_time.plot(kind='line', color='blue', ax=ax3)
        ax3.set_title('Jobs Trend Over Time')
        ax3.set_xlabel('Month')
        ax3.set_ylabel('Number of Jobs')
        st.pyplot(fig3)
        st.write("The line graph above visualizes the trend of jobs over time, aggregated by month. This visualization provides insights into how the demand for the company's services fluctuates throughout the year. ")
        st.write("")  # This adds an empty line
        st.write("")
        
        # Pricing Analysis for Different Types of Services
        st.sidebar.header("Pricing Analysis for Different Types of Services")
        # Correcting the column name for pricing and converting it to numeric
        data[' Pricing '] = data[' Pricing '].replace('[\$,]', '', regex=True).astype(float)
        # Allow user to choose number of services and types of services
        selected_num_services = st.sidebar.slider("Select Number of Services", min_value=1, max_value=len(data['Type'].unique()), value=3)
        selected_services = st.sidebar.multiselect("Select Services", data['Type'].unique(), default=data['Type'].unique()[:selected_num_services])
        # Display an error if no service is selected
        if not selected_services:
            st.error("Please choose at least one service.")
        else:
            # Filter data for the selected services
            filtered_data_services = data[data['Type'].isin(selected_services)]
            # Creating a boxplot for Pricing analysis for different types of services with blue color palette
            fig4, ax4 = plt.subplots(figsize=(8, 6))
            sns.boxplot(x='Type', y=' Pricing ', data=filtered_data_services, palette="Blues", ax=ax4)
            ax4.set_title('Pricing Analysis for Selected Types of Services')
            ax4.set_xlabel('Type of Service')
            ax4.set_ylabel('Pricing ($)')
            st.pyplot(fig4)
        st.write("The box plot visualizes the pricing structure for different types of services offered by the company, revealing critical insights into how pricing varies and how it might impact business strategy. ")
        st.write("")  # This adds an empty line
        st.write("")
        
    
        st.image("crew5.png", caption="Crew Duration vs. Edit Duration", use_column_width=True)
        st.write("The scatter plot provided shows the relationship between 'Crew Duration' and 'Edit Duration' for various projects or jobs. Understanding the dynamics between crew and edit durations can provide strategic insights into operational efficiency, cost management, and potentially customer satisfaction through faster delivery times. ")
        st.write("")  # This adds an empty line
        st.write("")
        
        
        st.image("crew6.png", caption="Client segmentation analysis", use_column_width=True)
        st.write("Distribution of Clients Across Segments: This bar chart presents the number of clients in each of the 'High Value', 'Moderate Value', and 'Low Value' segments. It shows a concentration of clients in the 'Moderate Value' segment. ")
        st.write("")  # This adds an empty line
        st.write("")
        
        
        st.image("crew7.png", caption="Average Frequency and Pricing by segment", use_column_width=True)
        st.write("**Average Frequency by Segment**: The bar chart shows the average frequency of transactions for each segment, giving insights into how often clients in each segment engage with the services. ")
        st.write("")  # This adds an empty line
        st.write("")
        st.write("**Average Pricing by Segment**: This bar chart displays the average pricing within each segment, indicating the average spending level of clients in each category. ")
                
    if menu == "Production EDA":
        data = pd.read_csv("Production-fixed.csv")
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown('<p class="title"> Production EDA </p>', unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.image("pr1.png", caption="Number of Jobs Over Time", use_column_width=True)
        st.write("The time series graph shows the number of jobs over time for ISOL. From the graph, it appears that the jobs are not evenly distributed over time. There are specific periods where the number of jobs spikes significantly, indicating a much higher workload during these times.")
        st.write("")  # This adds an empty line
        st.write("")
        
        # Sidebar with user input for the Distribution of Job Types
        st.sidebar.header("Distribution of Job Types")
        # Allow user to choose the number of job types and specific types
        selected_num_job_types = st.sidebar.slider("Select Number of Job Types", min_value=1, max_value=len(data['TYPE'].unique()), value=3)
        selected_job_types = st.sidebar.multiselect("Select Job Types", data['TYPE'].unique(), default=data['TYPE'].unique()[:selected_num_job_types])

        # Display an error if no job type is selected
        if not selected_job_types:
            st.error("Please choose at least one job type.")
        else:
            # Filter data based on selected job types
            filtered_data_job_types = data[data['TYPE'].isin(selected_job_types)]

            # Distribution of job types
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(y='TYPE', data=filtered_data_job_types, order=filtered_data_job_types['TYPE'].value_counts().index)
            ax.set_title('Distribution of Selected Job Types')
            ax.set_xlabel('Count')
            ax.set_ylabel('Job Type')
            st.pyplot(fig)
        st.write("The bar chart you've provided shows the distribution of job types for the broadcasting company.")
        st.write("")  # This adds an empty line
        st.write("")
        
        st.image("pr3.png", caption="Top 10 Clients", use_column_width=True)
        st.write("The bar chart presents the distribution of the top clients for the broadcasting company, showing how many times services were provided to each over a given time period.")
        st.write("")  # This adds an empty line
        st.write("")
        
        st.image("pr4.png", caption="Relationship between Job Duration and Price", use_column_width=True)
        st.write("The scatter plot illustrates the relationship between job duration and price for the broadcasting company's services. ")
        
        
    if menu == "Transmission EDA":
        # Load the data
        data = pd.read_csv("transmission-clean.csv")
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown('<p class="title"> Transmission EDA </p>', unsafe_allow_html=True)
        st.write("")
        # Sidebar with user input for the Frequency of Transactions by Client
        st.sidebar.header("Frequency of Transactions by Client")
        # Allow user to choose the number of clients and specific clients
        selected_num_clients = st.sidebar.slider("Select Number of Clients", min_value=1, max_value=len(data['Client'].unique()), value=5)
        selected_clients = st.sidebar.multiselect("Select Clients", data['Client'].unique(), default=data['Client'].unique()[:selected_num_clients])
        # Display an error if no client is selected
        if not selected_clients:
            st.error("Please choose at least one client.")
        else:
            # Filter data based on selected clients
            filtered_data_clients = data[data['Client'].isin(selected_clients)]

            # Frequency of transactions by client
            client_counts = filtered_data_clients['Client'].value_counts()

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x=client_counts.index, y=client_counts.values, palette="viridis")
            ax.set_title('Frequency of Transactions by Selected Clients')
            ax.set_ylabel('Number of Transactions')
            ax.set_xlabel('Client')
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig)
        st.write("Frequency of Transactions by Client: It highlights which clients use the services most frequently. Some clients have significantly higher transaction counts compared to others.")
        st.write("")  # This adds an empty line
        
        
        st.write("")
       # Sidebar with user input for the Types of Transactions
        st.sidebar.header("Types of Transactions")
        # Allow the user to choose the number of transaction types and specific types
        selected_num_types = st.sidebar.slider("Select Number of Transaction Types", min_value=1, max_value=len(data['Type Of Txn'].unique()), value=3)
        selected_types = st.sidebar.multiselect("Select Transaction Types", data['Type Of Txn'].unique(), default=data['Type Of Txn'].unique()[:selected_num_types])
        # Display an error if no transaction type is selected
        if not selected_types:
            st.error("Please choose at least one transaction type.")
        else:
            # Filter data based on selected transaction types
            filtered_data_types = data[data['Type Of Txn'].isin(selected_types)]
            # Calculate the frequency of each type of transaction
            txn_counts = filtered_data_types['Type Of Txn'].value_counts()
            # Types of transactions
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.barplot(x=txn_counts.index, y=txn_counts.values, palette="rocket")
            ax.set_title('Types of Selected Transactions', fontsize=14)
            ax.set_ylabel('Count', fontsize=12)
            ax.set_xlabel('Type of Transaction', fontsize=12)
            ax.tick_params(axis='x', rotation=45, labelsize=10)  # Adjusting the font size and rotation for x labels
            ax.tick_params(axis='y', labelsize=10)
            plt.tight_layout()
            st.pyplot(fig)
        st.write("The graph shows specific transaction types like Live Studio Transmission, Space Segment, and others, each represented by a bar indicating its frequency. The variation in the frequency of different transaction types gives insights into how diversified the service offerings are and also reflect client preferences and needs.")
        st.write("")  # This adds an empty line
        st.write("")
        
        
        st.image("tr3.png", caption="Duration analysis", use_column_width=True)
        st.write("The histogram shows the frequency of transactions across different duration intervals, The spread of the histogram shows the range of transaction durations. A wide spread indicates a diverse range of service durations, from very short to very long.")
        st.write("")  # This adds an empty line
        st.write("")
        
        
        # Sidebar with user input for Satellite Usage Frequency
        st.sidebar.header("Satellite Usage Frequency")
        # Allow user to choose the number of satellites and specific satellites
        selected_num_satellites = st.sidebar.slider("Select Number of Satellites", min_value=1, max_value=len(data['Satellite'].unique()), value=3)
        selected_satellites = st.sidebar.multiselect("Select Satellites", data['Satellite'].unique(), default=data['Satellite'].unique()[:selected_num_satellites])
        # Display an error if no satellite is selected
        if not selected_satellites:
            st.error("Please choose at least one satellite.")
        else:
            # Filter data based on selected satellites
            filtered_data_satellites = data[data['Satellite'].isin(selected_satellites)]

            # Calculate the frequency of transactions for each satellite
            satellite_counts = filtered_data_satellites['Satellite'].value_counts()

            # Satellite usage frequency
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x=satellite_counts.index, y=satellite_counts.values, palette="mako")
            ax.set_title('Satellite Usage Frequency', fontsize=14)
            ax.set_ylabel('Count', fontsize=12)
            ax.set_xlabel('Satellite', fontsize=12)
            ax.tick_params(axis='x', rotation=45, labelsize=10)  # Adjusting the font size and rotation for x labels
            ax.tick_params(axis='y', labelsize=10)
            plt.tight_layout()
            st.pyplot(fig)
        st.write("Frequent usage of certain satellites may warrant strategic partnerships or negotiations for better rates or dedicated services. This information is key for strategic decisions regarding technology investments, partnerships with satellite providers, and understanding thelimitations of services")
        st.write("")  # This adds an empty line
        st.write("")
        
        
        st.image("tr5.png", caption="Client segmentation analysis", use_column_width=True) 
        st.write("The visualizations provide a detailed view of the client segmentation analysis")
        st.write("Distribution of Clients Across Segments:")
        st.write("The bar graph shows the number of clients in each segment: 'High Value', 'Moderate Value', and 'Low Value'. It's evident that the majority of clients fall into the 'Moderate Value' category, with fewer clients in the 'High Value' and 'Low Value' segments.")
        st.write("")  # This adds an empty line
        st.write("")
        
        
        st.image("tr6.png", caption="Average Frequency and Pricing by segment", use_column_width=True) 
        st.write("**Average Frequency by Segment:**")
        st.write("This graph compares the average frequency of transactions for clients in each segment. 'High Value' clients have the highest average frequency, indicating they engage with the services more often.")
        st.write("**Average Pricing by Segment:**")
        st.write("This graph shows the average pricing for each segment.")
        
    if menu == "Crew-Edit Price Prediction":
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown('<p class="title"> Crew-Edit Price Prediction </p>', unsafe_allow_html=True)
        def create_format_dataframe(user_choice):
            # Define the formats
            all_formats = ['Format_MP4-HD', 'Format_MXF', 'Format_MXF OP1A', 'Format_MXF-HD 50i', 'Format_No format']

            # Create a dictionary with zeros for all formats
            data = {format_choice: 0 for format_choice in all_formats}

            # Set the chosen format to 1
            data[user_choice] = 1

            # Create a dataframe from the dictionary
            df = pd.DataFrame([data])
            return df
       
       
        def create_access_dataframe(user_choice):
            # Define the formats
            all_other_Access = ['Others Acces_No Acces', 'Others Acces_Pro-X', 'Others Acces_Torch']

            # Create a dictionary with zeros for all formats
            data = {other_Access_choice: 0 for other_Access_choice in all_other_Access}

            # Set the chosen format to 1
            data[user_choice] = 1

            # Create a dataframe from the dictionary
            df = pd.DataFrame([data])
            return df
        
        def create_truck_dataframe(user_choice):
            # Define the formats
            all_trucks = ['Truck_Nissan Sunny', 'Truck_Nissan X.Trail', 'ruck_Renault Duster', 'Truck_Suzuki Cias', 'Truck_other Truck']

            # Create a dictionary with zeros for all formats
            data = {truck_choice: 0 for truck_choice in all_trucks}

            # Set the chosen format to 1
            data[user_choice] = 1

            # Create a dataframe from the dictionary
            df = pd.DataFrame([data])
            return df
        
        
        def create_client_dataframe(user_choice):
            # Define the formats
            all_clients = ['Client_bbc arabic', 'Client_beirutsat', 'Client_bloomberg asharq', 'Client_byblos medya', 'Client_newstime','Client_priyanka cgtn','Client_russia today']

            # Create a dictionary with zeros for all formats
            data = {client_choice: 0 for client_choice in all_clients}

            # Set the chosen format to 1
            data[user_choice] = 1

            # Create a dataframe from the dictionary
            df = pd.DataFrame([data])
            return df
        
        def display_choice_result(choice):
            if choice == 1:
                st.write("Yes")

            else:
                st.write("No")

        
        # Get user input for a binary value (0 or 1) using a slider
        four_G = st.sidebar.slider("Select 0 or 1 for 4G: ", min_value=0, max_value=1, step=1)
        st.write("**You chose for the 4G feature:**")
        display_choice_result(four_G)
        
        reporter = st.sidebar.slider("Select 0 or 1 for Reporter: ", min_value=0, max_value=1, step=1)
        st.write("**You chose for the reporter feature:**")
        display_choice_result(reporter)
        
        crew_Duration = st.sidebar.number_input("Enter a non-negative integer for Crew duration:", min_value=0, step=1)
        st.write("**You chose for the Crew Duration feature:**")
        st.write(crew_Duration)
        
        edit_Duration = st.sidebar.number_input("Enter a non-negative integer for Edit duration:", min_value=0, step=1)
        st.write("**You chose for the Edit Duration feature:**")
        st.write(edit_Duration)
        
        daysOfWeek = st.sidebar.slider("Select a number between 0 and 6 for Days of Week:", min_value=0, max_value=6, step=1)
        # Call the function to display the selected day of the week
        display_day_of_week(daysOfWeek)

        
        report_Duration = st.sidebar.number_input("Enter a non-negative integer for Report duration:", min_value=0, step=1)
        st.write("**You chose for the Report Duration feature in seconds:**")
        st.write(report_Duration)
       
        client = st.sidebar.selectbox('Client',('Client_bbc arabic','Client_beirutsat','Client_bloomberg asharq','Client_byblos medya','Client_newstime','Client_priyanka cgtn','Client_russia today'))
        st.write("**You chose for the Client feature:**")
        st.write(client)
        df_client= create_client_dataframe(client)
        #st.write("Encoded Client DataFrame:")
        #st.write(df_client)
        
        truck = st.sidebar.selectbox('Truck',('Truck_Nissan Sunny','Truck_Nissan X.Trail','Truck_Renault Duster','Truck_Suzuki Cias','Truck_other Truck'))
        st.write("**You chose for the Truck feature:**")
        st.write(truck)
        df_truck = create_truck_dataframe(truck)
        #st.write("Encoded Truck DataFrame:")
        #st.write(df_truck)
        
        other_Access = st.sidebar.selectbox('Others Access',('Others Acces_No Acces','Others Acces_Pro-X','Others Acces_Torch'))
        st.write("**You chose for the Other Access feature:**")
        st.write(other_Access)
        df_access = create_access_dataframe(other_Access)
        #st.write("Encoded Access DataFrame:")
        #st.write(df_access)
        
        format = st.sidebar.selectbox('Format',('Format_MP4-HD','Format_MXF','Format_MXF OP1A','Format_MXF-HD 50i','Format_No format'))
        st.write("**You chose for the Format feature:**")
        st.write(format)
        df_format = create_format_dataframe(format)
        #st.write("Encoded Format DataFrame:")
        #st.write(df_format)
        
        
        data = { '4G' : four_G,
                'Reporter': reporter,
                 'Crew Duration' : crew_Duration,
                 'edit duration': edit_Duration,
                 'DayOfWeek': daysOfWeek,
                 'Report Duration' : report_Duration,
                 
                 'Client_bbc arabic': df_client.iloc[0, 0],
                 'Client_beirutsat':df_client.iloc[0, 1], 
                 'Client_bloomberg asharq':df_client.iloc[0, 2],
                 'Client_byblos medya': df_client.iloc[0, 3],
                 'Client_newstime': df_client.iloc[0, 4], 
                 'Client_priyanka cgtn': df_client.iloc[0, 5],
                 'Client_russia today': df_client.iloc[0, 6],
                     
                 'Truck_Nissan Sunny': df_truck.iloc[0, 0],
                 'Truck_Nissan X.Trail': df_truck.iloc[0, 1],
                 'Truck_Renault Duster': df_truck.iloc[0, 2],
                 'Truck_Suzuki Cias': df_truck.iloc[0, 3],
                 'Truck_other Truck': df_truck.iloc[0, 4],
                 
                 'Others Acces_No Acces':df_access.iloc[0, 0],
                 'Others Acces_Pro-X':df_access.iloc[0, 1],
                 'Others Acces_Torch': df_access.iloc[0, 2],
                 
                 'Format_MP4-HD': df_format.iloc[0, 0],
                 'Format_MXF': df_format.iloc[0, 1],
                 'Format_MXF OP1A': df_format.iloc[0, 2],
                 'Format_MXF-HD 50i': df_format.iloc[0, 3],
                 'Format_No format': df_format.iloc[0, 4]
                      
        }
        features = pd.DataFrame(data,index = [0])
        #st.write(features)
        
        crew_edit_raw= pd.read_csv('crew-edit-preprocessed.csv')
        #st.write(crew_edit_raw.head(1))
        crew_edit_raw.drop(columns=['Unnamed: 0'], inplace=True)
        # Display the first row of the dataset
        #st.write("First Row of the Dataset:")
        #st.write(crew_edit_raw.head(1))
        crew_edit = crew_edit_raw.drop(columns=['Price'])
        #st.write("First Row of the Dataset after removing price column:")
        #st.write(crew_edit.head(1))
        df = pd.concat([features,crew_edit],axis=0)
        df = df.fillna(0)
        #st.write("First Row of the Dataset after combining:")
        #st.write(df.head(1))
        #st.write(df.tail(1))

        
        # Reads in saved classification model
        load_clf = pickle.load(open('best_rf_reg.pkl', 'rb'))
        
        # Apply model to make predictions
        prediction = load_clf.predict(df) 
        
        # Extract the predicted price
        predicted_price = prediction[0]

        # Display the extracted predicted price
        st.write("")
        st.write("**Your Predicted Price for Crew-Edit chosen the above features is:**")
        st.write(predicted_price)

            
    if menu == "Production Price Prediction":
        
        def display_choice_result(choice):
            if choice == 1:
                st.write("Yes")

            else:
                st.write("No")
        
        def create_client_dataframe(user_choice):
                # Define the formats
            all_clients = ['CLIENT_Other','CLIENT_Russia_Today','CLIENT_Skynews Arabia']

            # Create a dictionary with zeros for all formats
            data = {client_choice: 0 for client_choice in all_clients}

            # Set the chosen format to 1
            data[user_choice] = 1

            # Create a dataframe from the dictionary
            df = pd.DataFrame([data])
            return df
        
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown('<p class="title"> Production Price Prediction </p>', unsafe_allow_html=True)
        GVG_Focus_75 = st.sidebar.slider("Select a number between 0 and 6 for GVG Focus 75:", min_value=0, max_value=6, step=1)
        st.write(f"**You chose {GVG_Focus_75} for the GVG focus 75 feature.**")
        
        LDX_80 = st.sidebar.slider("Select a number between 0 and 6 for LDX-80:", min_value=0, max_value=6, step=1)
        st.write(f"**You chose {LDX_80} for the LDX 80 feature.**")
        
        Sony = st.sidebar.slider("Select a number 0 or 3 or 4 for Sony:", min_value=0, max_value=4, step=1)
        # Display a message based on the user's choice
        if Sony == 0:
            st.write("**You chose 0.**")
        elif Sony == 3:
            st.write("**You chose 3.**")
        elif Sony == 4:
            st.write("**You chose 4.**")
        else:
            st.write("**Invalid choice. Please choose 0, 3, or 4.**")
        
        
        Lenses_Tele_lens = st.sidebar.slider("Select a number between 0 and 2 for Lenses: Tele lens:", min_value=0, max_value=2, step=1)
        st.write(f"**You chose {Lenses_Tele_lens} for the Lenses Tele lens feature.**")
        
        Lenses_Box_lenses = st.sidebar.slider("Select a number between 0 and 2 for Lenses: Box lenses:", min_value=0, max_value=2, step=1)
        st.write(f"**You chose {Lenses_Box_lenses} for the Lenses Box lenses feature.**")
        
        Lenses_Fujinon = st.sidebar.slider("Select a number between 0 and 2 for Lenses: Fujinon:", min_value=0, max_value=2, step=1)
        st.write(f"**You chose {Lenses_Fujinon} for the Lenses_Fujinon feature.**")
        
        Canon_Digisuper_75_XSW_EDFS = st.sidebar.slider("Select a number between 0 and 2 for Canon Digisuper 75 XSW / EDFS:", min_value=0, max_value=2, step=1)
        st.write(f"**You chose {Canon_Digisuper_75_XSW_EDFS} for the Canon Digisuper 75 XSW EDFS feature.**")
        
        Video_server = st.sidebar.slider("Select a number between 0 and 2 for Video server:", min_value=0, max_value=2, step=1)
        st.write(f"**You chose {Video_server} for the Video server feature.**")
        
        Headset_microphones = st.sidebar.slider("Select a number either 0 or 2 for Headset microphones:", min_value=0, max_value=2, step=2)
        if Headset_microphones == 0:
            st.write("**You chose 0.**")
        elif Headset_microphones == 2:
            st.write("**You chose 2.**")
        else:
            st.write("**Invalid choice. Please choose 0 or 2.**")
        
        Handled_microphone = st.sidebar.slider("Select a number between 0 and 2 for Handled microphone:", min_value=0, max_value=2, step=1)
        st.write(f"**You chose {Handled_microphone} for the  Handled microphone feature.**")
        
        Audio_monitor = st.sidebar.slider("Select a number between 0 and 2 for Audio monitor:", min_value=0, max_value=2, step=1)
        st.write(f"**You chose {Audio_monitor} for the Audio monitor feature.**")
        
        Audio_Mixer = st.sidebar.slider("Select 0 or 1 for Audio Mixer:", min_value=0, max_value=1, step=1)
        st.write(f"**You chose {Audio_Mixer} for the Audio Mixer feature:**")
        
        Microphones = st.sidebar.slider("Select a number between 0 and 4 for Microphones:", min_value=0, max_value=4, step=1)
        st.write(f"**You chose {Microphones} for the  Microphones feature.**")
        
        LCD_Screen = st.sidebar.slider("Select 0 or 1 for LCD Screen:", min_value=0, max_value=1, step=1)
        st.write(f"**You chose {LCD_Screen}for the LCD_Screen feature:**")
        
        Wireless_intercom_1 = st.sidebar.slider("Select a number between 0 and 2 for Wireless intercom.1:", min_value=0, max_value=2, step=1)
        st.write(f"**You chose {Wireless_intercom_1} for the  Wireless intercom 1 feature.**")
        
        view_finders = st.sidebar.slider("Select a number between 0 and 3 for view finders:", min_value=0, max_value=3, step=1)
        st.write(f"**You chose {view_finders} for the  view finders feature.**")
        
        HF_wireless = st.sidebar.slider("Select 0 or 1 for HF wireless:", min_value=0, max_value=1, step=1)
        st.write(f"**You chose {HF_wireless} for the HF wireless feature:**")
        
        BLT_slow_motion = st.sidebar.slider("Select 0 or 1 for BLT slow motion:", min_value=0, max_value=1, step=1)
        st.write(f"**You chose {BLT_slow_motion} for the BLT slow motion:**")
        
        Playout_server = st.sidebar.slider("Select a number between 0 and 6 for Playout server:", min_value=0, max_value=6, step=1)
        # Display a message based on the user's choice
        if Playout_server == 0:
            st.write("**You chose 0.**")
        elif Playout_server == 1:
            st.write("**You chose 1.**")
        elif Playout_server == 6:
            st.write("**You chose 6.**")
        else:
            st.write("**Invalid choice. Please choose 0, 1, or 6.**")
        
        Converters_from_HDMI_to_SDI = st.sidebar.slider("Select a number either 0 or 2 for Converters from HDMI to SDI:", min_value=0, max_value=2, step=2)
        if Converters_from_HDMI_to_SDI == 0:
            st.write("**You chose 0.**")
        elif Converters_from_HDMI_to_SDI == 2:
            st.write("**You chose 2.**")
        else:
            st.write("**Invalid choice. Please choose 0 or 2.**")
        
        Other_Accessories = st.sidebar.slider("Select 0 or 1 for Other Accessories:", min_value=0, max_value=1, step=1)
        st.write(f"**You chose {Other_Accessories} for the Other Accessories feature:**")

        CAMERAMEN_STUDIO_OPERATOR = st.sidebar.slider("Select 0 or 1 for CAMERAMEN STUDIO OPERATOR:", min_value=0, max_value=1, step=1)
        st.write(f"**You chose  {CAMERAMEN_STUDIO_OPERATOR} for the CAMERAMEN STUDIO OPERATOR feature:**")
        
        Technician_OBVAN = st.sidebar.slider("Select 0 or 1 for Technician OBVAN:", min_value=0, max_value=1, step=1)
        st.write(f"**You chose {Technician_OBVAN} for the Technician OBVAN feature:**")
        
        Month = st.sidebar.slider("Select a number between 1 and 12 for Month:", min_value=1, max_value=12, step=1)
        # Call the function to display the selected month
        display_month(Month)
        
        DayOfWeek = st.sidebar.slider("Select a number between 0 and 6 for DayOfWeek:", min_value=0, max_value=6, step=1)
        display_day_of_week(DayOfWeek)
        
        Client = st.sidebar.selectbox('Client',('CLIENT_Other','CLIENT_Russia_Today','CLIENT_Skynews Arabia'))## check the values of client
        st.write("**You chose for the Client feature:**")
        st.write(Client)
        df_client = create_client_dataframe(Client)
        #st.write("Encoded client DataFrame:")
        #st.write(df_client)
        
        Distance_Category = st.sidebar.slider("Select a number between 0 and 2 for Distance_Category:", min_value=0, max_value=2, step=1)
        st.write(f"**You chose {Distance_Category} for the Distance_Category feature:**")
       
       
       
        data = { 'GVG Focus 75' : GVG_Focus_75,
                'LDX-80': LDX_80,
                 'Sony' : Sony,
                 'Lenses: Tele lens': Lenses_Tele_lens,
                 'Lenses: Box lenses': Lenses_Box_lenses,
                 'Lenses:Fujinon' : Lenses_Fujinon,
        
                 'Canon Digisuper 75 XSW / EDFS': Canon_Digisuper_75_XSW_EDFS,
                 'Video server':Video_server, 
                 'Headset microphones':Headset_microphones,
                 'Handled microphone': Handled_microphone,
                 'Audio monitor': Audio_monitor, 
                 'Audio Mixer': Audio_Mixer,
                 'Microphones': Microphones,
                     
                 'video server': Video_server ,
                 'LCD Screen': LCD_Screen,
                 'Wireless intercom.1': Wireless_intercom_1,
                 'view finders': view_finders,
                 'HF wireless': HF_wireless,
                 
                 'BLT slow motion':BLT_slow_motion,
                 'Playout server':Playout_server,
                 'Converters from HDMI to SDI': Converters_from_HDMI_to_SDI,
                 
                 'Other Accessories': Other_Accessories,
                 'CAMERAMEN STUDIO OPERATOR': CAMERAMEN_STUDIO_OPERATOR,
                 'Technician OBVAN': Technician_OBVAN,
                 'Month': Month,
                 'DayOfWeek': DayOfWeek,
                 
                 'CLIENT_Other': df_client.iloc[0, 0],
                 'CLIENT_Russia Today': df_client.iloc[0, 1],
                 'CLIENT_Skynews Arabia': df_client.iloc[0, 2],
                 
                 'Distance_Category': Distance_Category,
                 
                      
        }
        features = pd.DataFrame(data,index = [0])
        #st.write(features)
        
        production_raw= pd.read_csv('production-preprocessed.csv')
        #st.write(production_raw.head(1))
        production_raw.drop(columns=['Unnamed: 0'], inplace=True)
        # Display the first row of the dataset
        #st.write("First Row of the Dataset:")
        #st.write(production_raw.head(1))
        production = production_raw.drop(columns=['Price'])
        #st.write("First Row of the Dataset after removing price column:")
        #st.write(production.head(1))
        df = pd.concat([features,production],axis=0)
        df = df.fillna(0)
        #st.write("First Row of the Dataset after combining:")
        #st.write(df.head(1))
        #st.write(df.tail(1))

        
        # Reads in saved classification model
        load_clf = pickle.load(open('best_ridge_reg_production.pkl', 'rb'))
        
        # Apply model to make predictions
        prediction = load_clf.predict(df) 
        
        # Extract the predicted price
        predicted_price = prediction[0]
        if predicted_price < 0:
            # Make it positive
            predicted_price = abs(predicted_price)
        # Display the extracted predicted price
        st.write("**Your Predicted Price for Production chosen the above features is:**")
        st.write(predicted_price)
        
    
    if menu == "Transmission Price Prediction":
        
        def display_choice_result(choice):
            if choice == 1:
                st.write("Yes")

            else:
                st.write("No")
        
        def create_txp_dataframe(user_choice):
            # Define the formats
            all_txp = ['Txp_AlGhad Slot 2','Txp_AlGhad Slot 3','Txp_B2','Txp_Ch 1','Txp_Ch 3','Txp_Ch X'
                                    ,'Txp_Ch Y','Txp_Link','Txp_No Txp','Txp_Other Ch','Txp_Other Slots','Txp_Other Txp'
                                    ,'Txp_Output 1','Txp_Output 2','Txp_Output 3','Txp_Output 4','Txp_Slot 1 7A','Txp_Slot 2 7A'
                                    ,'Txp_Slot 3 7A','Txp_Slot 4 7A']

            # Create a dictionary with zeros for all formats
            data = {txp_choice: 0 for txp_choice in all_txp}

            # Set the chosen format to 1
            data[user_choice] = 1

            # Create a dataframe from the dictionary
            df = pd.DataFrame([data])
            return df
        
        def create_camera_dataframe(user_choice):
            # Define the formats
            all_cameras = ['Camera_Canon C305','Camera_Canon XF305','Camera_Sony HDV270','Camera_Sony S150','Camera_Sony XDcam'
                                        ,'Camera_Sony XDcam X150','Camera_Sony XDcam X190','Camera_Sony XDcam X320']

            # Create a dictionary with zeros for all formats
            data = {camera_choice: 0 for camera_choice in all_cameras}

            # Set the chosen format to 1
            data[user_choice] = 1

            # Create a dataframe from the dictionary
            df = pd.DataFrame([data])
            return df
        
        def create_sat_charges_dataframe(user_choice):
            # Define the formats
            all_sat_charges = ['Sat Charges Paid_ISOL','Sat Charges Paid_No Sat Charges']

            # Create a dictionary with zeros for all formats
            data = {charge_choice: 0 for charge_choice in all_sat_charges}

            # Set the chosen format to 1
            data[user_choice] = 1

            # Create a dataframe from the dictionary
            df = pd.DataFrame([data])
            return df
        
        
        client_mapping = {
            'bbc arabic': 2,
            'ap gms': 1,
            'ap mes': 1,
            'other client': 0
        }
        
        type_mapping = {
            'other txn': 0,
            'turnaround': 1,
            'ftp': 2,
            'we transfer': 2,
            'internet consumption': 2,
            'aspera': 2,
            'live studio transmission': 3,
            'live position transmission': 3,
            'space segment': 3,
            'tape feed transmission': 3,
            'live from 4g': 4,
            'renting 4g': 4,
            'sng': 5
        }
        
        antenna_mapping = {
            'No Antenna': 0,
            'Other Antenna': 1,
            'Link': 2,
            'Dacia G175677': 2,
            'Sunny G365649': 2,
            'DownLink Dish': 3,
            'Aviwest': 4,
            'WMT': 4,
            'FLW': 5,
            'VPS': 6,
            'Patrol': 7,
            'Chevrolet': 7
        }
        
        satellite_mapping = {
            'No Satellite': 0,
            'Other Satellite': 1,
            'AVIWEST': 3,
            'E21B': 4
        }
        
        studio_mapping = {
            'No Studio': 0,
            '7(3thfloor)': 1,
            '4(4thfloor)': 1,
            '3(5thfloor)': 1,
            '6(3thfloor)': 1,
            'other': 1,
            'underthebuilding':1,
            '1(6thfloor)': 2,
            
        }
        
        
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown('<p class="title"> Transmission Price Prediction </p>', unsafe_allow_html=True)
        
        Client = st.sidebar.slider("Select a number between 0 and 2 for Client:", min_value=0, max_value=2, step=1)
        # Display the corresponding client based on the user's choice
        if Client in client_mapping.values():
            selected_type = [key for key, value in client_mapping.items() if value == Client][0]
            st.write(f"**You chose {selected_type} as the client.**")
            st.write("")
        
        
        Type_Of_Txn = st.sidebar.slider("Select a number between 0 and 5 for Type Of Txn:", min_value=0, max_value=5, step=1)
        if Type_Of_Txn in type_mapping.values():
            selected_type = [key for key, value in type_mapping.items() if value == Type_Of_Txn][0]
            st.write(f"**You chose {selected_type} as the type.**")
            st.write("")
        
        Filmed_By = st.sidebar.slider("Select 0 or 1 for Filmed By:", min_value=0, max_value=1, step=1)
        st.write("**You chose for the Filmed By feature:**")
        display_choice_result(Filmed_By)
        
        Antenna = st.sidebar.slider("Select a number between 0 and 7 for Antenna:", min_value=0, max_value=7, step=1)
        if Antenna in antenna_mapping.values():
            selected_antenna = [key for key, value in antenna_mapping.items() if value == Antenna][0]
            st.write(f"**You chose {selected_antenna} as the antenna.**")
            st.write("")
        
        Location = st.sidebar.slider("Select 0 or 1 for Location:", min_value=0, max_value=1, step=1)
        st.write("**You chose for the Location feature:**")
        display_choice_result(Location)
        
        Satellite = st.sidebar.slider("Select a number between 0 and 4 for Satellite:", min_value=0, max_value=4, step=1)
        if Satellite in satellite_mapping.values():
            selected_satellite = [key for key, value in satellite_mapping.items() if value == Satellite][0]
            st.write(f"**You chose {selected_satellite} as the satellite.**")
            st.write("")
        
        Sat_Provider = st.sidebar.slider("Select 0 or 1 for Sat Provider:", min_value=0, max_value=1, step=1)
        st.write("**You chose for the Sat Provider feature:**")
        display_choice_result(Sat_Provider)
        
        Engineer2 = st.sidebar.slider("Select 0 or 1 for Engineer2:", min_value=0, max_value=1, step=1)
        st.write("**You chose for the Engineer2 feature:**")
        display_choice_result(Engineer2)
        
        Comments = st.sidebar.slider("Select 0 or 1 for Comments:", min_value=0, max_value=1, step=1)
        st.write("**You chose for the Comments feature:**")
        display_choice_result(Comments)
        
        Guest_Reporter = st.sidebar.slider("Select 0 or 1 for Guest / Reporter:", min_value=0, max_value=1, step=1)
        st.write("**You chose for the Guest Reporter feature:**")
        display_choice_result(Guest_Reporter)
        
        Studio = st.sidebar.slider("Select between 0 and 2 for Studio:", min_value=0, max_value=2, step=1)
        # Display the studio_mapping dictionary on the Streamlit app
        #st.write("Studio Mapping:")
        #for key, value in studio_mapping.items():
            #st.write(f"{key}: {value}")
        if Studio in studio_mapping.values():
            selected_studio = [key for key, value in studio_mapping.items() if value == Studio][0]
            st.write(f"**You chose {selected_studio} as the studio.**")
            st.write("")
        
        Guest_fee = st.sidebar.slider("Select 0 or 1 for Guest fee:", min_value=0, max_value=1, step=1)
        st.write("**You chose for the Guest fee feature:**")
        display_choice_result(Guest_fee)
        
        Duration_in_minutes = st.sidebar.number_input("Enter a non-negative integer for Duration in minutes:", min_value=0, step=1)
        st.write("**You chose for the Duration feature in minutes:**")
        st.write(Duration_in_minutes)
        
        Month = st.sidebar.slider("Select a number between 1 and 12 for Month:", min_value=1, max_value=12, step=1)
        # Call the function to display the selected month
        display_month(Month)
        
        DayOfWeek = st.sidebar.slider("Select a number between 0 and 6 for DayOfWeek:", min_value=0, max_value=6, step=1)
        display_day_of_week(DayOfWeek)
        
        Txp = st.sidebar.selectbox('Txp',('Txp_AlGhad Slot 2','Txp_AlGhad Slot 3','Txp_B2','Txp_Ch 1','Txp_Ch 3','Txp_Ch X'
                                  ,'Txp_Ch Y','Txp_Link','Txp_No Txp','Txp_Other Ch','Txp_Other Slots','Txp_Other Txp'
                                  ,'Txp_Output 1','Txp_Output 2','Txp_Output 3','Txp_Output 4','Txp_Slot 1 7A','Txp_Slot 2 7A'
                                  ,'Txp_Slot 3 7A','Txp_Slot 4 7A'))
        
        st.write("**You chose for the Txp feature:**")
        st.write(Txp)
        df_Txp = create_txp_dataframe(Txp)
        #st.write("Encoded Txp DataFrame:")
        #st.write(df_Txp)
        

        Camera = st.sidebar.selectbox('Camera',('Camera_Canon C305','Camera_Canon XF305','Camera_Sony HDV270','Camera_Sony S150','Camera_Sony XDcam'
                                        ,'Camera_Sony XDcam X150','Camera_Sony XDcam X190','Camera_Sony XDcam X320'))
        

        st.write("**You chose for the Camera feature:**")
        st.write(Camera)
        df_Camera = create_camera_dataframe(Camera)
        #st.write("Encoded Camera DataFrame:")
        #st.write(df_Camera)
        
        Sat_Charges = st.sidebar.selectbox('Sat Charges',('Sat Charges Paid_ISOL','Sat Charges Paid_No Sat Charges'))

        st.write("**You chose for the Sat Charges feature:**")
        st.write(Sat_Charges)
        df_Sat_Charges = create_sat_charges_dataframe(Sat_Charges)
        #st.write("Encoded Sat Charges DataFrame:")
        #st.write(df_Sat_Charges)
        
        
        data = { 'Client' : Client,
                'Type Of Txn': Type_Of_Txn ,
                 'Filmed By' : Filmed_By,
                 'Antenna': Antenna,
                 'Location': Location,
                 'Satellite' : Satellite,
                 'Sat Provider': Sat_Provider,
                 'Engineer2':Engineer2, 
                 'Comments':Comments,
                 'Guest / Reporter': Guest_Reporter,
                 'Studio': Studio, 
                 'Guest fee': Guest_fee,
                 'Duration_in_minutes': Duration_in_minutes,
                 'Month': Month,
                 'DayOfWeek': DayOfWeek,
                 
                 'Txp_AlGhad Slot 2': df_Txp.iloc[0, 0],
                 'Txp_AlGhad Slot 3': df_Txp.iloc[0, 1],
                 'Txp_B2': df_Txp.iloc[0, 2],
                 'Txp_Ch 1': df_Txp.iloc[0,3],
                 'Txp_Ch 3': df_Txp.iloc[0, 4],
                 'Txp_Ch X': df_Txp.iloc[0, 5],
                 'Txp_Ch Y': df_Txp.iloc[0, 6],
                 'Txp_Link': df_Txp.iloc[0, 7],
                 'Txp_No Txp': df_Txp.iloc[0, 8],
                 'Txp_Other Ch': df_Txp.iloc[0, 9],
                 'Txp_Other Slots': df_Txp.iloc[0, 10],
                 'Txp_Other Txp': df_Txp.iloc[0, 11],
                 'Txp_Output 1': df_Txp.iloc[0, 12],
                 'Txp_Output 2': df_Txp.iloc[0, 13],
                 'Txp_Output 3': df_Txp.iloc[0, 14],
                 'Txp_Output 4': df_Txp.iloc[0, 15],
                 'Txp_Slot 1 7A': df_Txp.iloc[0, 16],
                 'Txp_Slot 2 7A': df_Txp.iloc[0, 17],
                 'Txp_Slot 3 7A': df_Txp.iloc[0, 18],
                 'Txp_Slot 4 7A': df_Txp.iloc[0, 19],
                 
                 'Camera_Canon C305':df_Camera.iloc[0, 0],
                 'Camera_Canon XF305':df_Camera.iloc[0, 1],
                 'Camera_Sony HDV270':df_Camera.iloc[0, 2],
                 'Camera_Sony S150':df_Camera.iloc[0, 3],
                 'Camera_Sony XDcam':df_Camera.iloc[0, 4],
                 'Camera_Sony XDcam X150':df_Camera.iloc[0, 5],
                 'Camera_Sony XDcam X190':df_Camera.iloc[0, 6],
                 'Camera_Sony XDcam X320':df_Camera.iloc[0, 7],
                 
                 'Sat Charges Paid_ISOL': df_Sat_Charges.iloc[0, 0],
                 'Sat Charges Paid_No Sat Charges': df_Sat_Charges.iloc[0, 1],

                      
        }
        features = pd.DataFrame(data,index = [0])
        #st.write(features)
        
        transmission_raw= pd.read_csv('transmission-preprocessed.csv')
        #st.write(transmission_raw.head(1))
        transmission_raw.drop(columns=['Unnamed: 0'], inplace=True)
        #Display the first row of the dataset
        #st.write("First Row of the Dataset:")
        #st.write(transmission_raw.head(1))
        transmission = transmission_raw.drop(columns=['Pricing'])
        #st.write("First Row of the Dataset after removing price column:")
        #st.write(transmission.head(1))
        df = pd.concat([features,transmission],axis=0)
        df = df.fillna(0)
        #st.write("First Row of the Dataset after combining:")
        #st.write(df.head(1))
        #st.write(df.tail(1))

        
        # Reads in saved classification model
        load_clf = pickle.load(open('best_rf_reg_transmission.pkl', 'rb'))
        
        # Apply model to make predictions
        prediction = load_clf.predict(df) 
        
        # Extract the predicted price
        predicted_price = prediction[0]

        # Display the extracted predicted price
        st.write("")
        st.write("**Your Predicted Price for Transmission chosen the above features is:**")
        st.write(predicted_price)
  
if __name__ == "__main__":
    main()
