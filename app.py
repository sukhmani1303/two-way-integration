import requests
import streamlit as st

def callback():
    st.session_state.button_clicked = True

def page1():
    st.title("Customer Catalog")
    if "button_clicked" not in st.session_state:    
        st.session_state.button_clicked = False
    
    if st.button("Load Data"):

        api_url = "http://127.0.0.1:8080/get_all" 

        response = requests.post(api_url)

        data = response.json() 
        st.table(data)
   
    if (st.button("update", on_click = callback) or st.session_state.button_clicked):
        id_to_update = st.text_input("Enter ID to update")
    
        if (st.button("Submit", on_click = callback) or st.session_state.button_clicked):
            api_url = "http://127.0.0.1:8080/update_data" 

            payload = {"id": str(id_to_update)}

            response = requests.post(api_url, json=payload)
            
            if ((response.status_code == 404)):
                st.error('Cannot Find Customer', icon="🚨")
                return "pp"
            
            data1 = response.json()

            id_disabled = st.text_input("ID of customer",value = data1['id'], disabled=True)
            name_new = st.text_input("Enter new name", value = data1['name'])
            email_new = st.text_input("Enter new email", value = data1['email'])

            if st.button("confirm"):
                api_url = "http://127.0.0.1:8080/outward_sync/update" 

                payload = {"id": id_to_update, "name" : name_new, "email" : email_new}

                response = requests.post(api_url, json=payload)

                if response.status_code == 200:
                    st.success('Customer Catalog Updated Successfully!', icon="✅")
                else:
                    st.error('Cannot Update Customer Catalog', icon="🚨")
        
    st.title("ADD DATA")
    # if (st.button("ADD DATA", on_click = callback) or st.session_state.button_clicked):
    name_main = st.text_input("Enter Name")
    email_main = st.text_input("Enter Email")

    if (st.button("Confirm")):
        api_url = "http://127.0.0.1:8080/outward_sync/add" 

        payload = {"name" : name_main, "email" : email_main}

        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            st.success('Customer Added Successfully!', icon="✅")
        else:
            st.error('Cannot add Customer!', icon="🚨")


if __name__ == "__main__":
    page1()
