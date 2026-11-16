
import streamlit as st
import requests

st.set_page_config(
    page_title="Patient Management System",
    page_icon="🏥",
    layout="wide"
)

# API configuration
try:
    default_url = st.secrets.get(
        "API_URL",
        "http://127.0.0.1:8000"
    )
except Exception:
    default_url = "http://127.0.0.1:8000"

st.title("🏥 Patient Management System")
st.caption("Manage patient records using FastAPI and Streamlit")

API_URL = st.sidebar.text_input(
    "FastAPI Backend URL",
    value=default_url
).strip().rstrip("/")


# Common API request function
def call_api(method, endpoint, **kwargs):
    try:
        response = requests.request(
            method,
            f"{API_URL}{endpoint}",
            timeout=20,
            **kwargs
        )

        if response.ok:
            st.success(f"Success! Status: {response.status_code}")
            try:
                st.json(response.json())
            except ValueError:
                st.write(response.text)
        else:
            st.error(f"API Error: {response.status_code}")
            try:
                st.json(response.json())
            except ValueError:
                st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to FastAPI. Check your backend URL and server.")

    except requests.exceptions.Timeout:
        st.error("The API request timed out.")

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")


# Dashboard tabs
view_tab, search_tab, add_tab, update_tab, delete_tab, sort_tab = st.tabs(
    ["📋 View", "🔍 Search", "➕ Add", "✏️ Update", "🗑️ Delete", "↕️ Sort"]
)


# 1. VIEW ALL PATIENTS
with view_tab:
    st.subheader("All Patient Records")

    if st.button("Load All Patients"):
        call_api("GET", "/view")


# 2. SEARCH PATIENT
with search_tab:
    st.subheader("Search Patient by ID")

    with st.form("search_form"):
        patient_id = st.text_input("Patient ID", placeholder="P001")
        search_button = st.form_submit_button("Search")

    if search_button:
        if patient_id.strip():
            call_api(
                "GET",
                f"/patient/{patient_id.strip()}"
            )
        else:
            st.warning("Please enter a patient ID.")


# 3. ADD PATIENT
with add_tab:
    st.subheader("Add New Patient")

    with st.form("add_form"):
        patient_id = st.text_input("Patient ID", placeholder="P008")
        name = st.text_input("Patient Name")
        city = st.text_input("City")

        age = st.number_input(
            "Age", min_value=1, max_value=119, value=21
        )

        gender = st.selectbox(
            "Gender", ["Male", "Female", "other"]
        )

        height = st.number_input(
            "Height (meters)", min_value=0.1,
            max_value=2.5, value=1.70, step=0.01
        )

        weight = st.number_input(
            "Weight (kg)", min_value=1.0,
            max_value=300.0, value=60.0
        )

        add_button = st.form_submit_button("Add Patient")

    if add_button:
        if not patient_id.strip() or not name.strip() or not city.strip():
            st.warning("Please fill in Patient ID, Name and City.")
        else:
            payload = {
                "id": patient_id.strip().upper(),
                "name": name.strip(),
                "city": city.strip(),
                "age": age,
                "gender": gender,
                "height": height,
                "weight": weight
            }

            call_api("POST", "/create", json=payload)


# 4. UPDATE PATIENT
with update_tab:
    st.subheader("Update Patient Details")

    with st.form("update_form"):
        update_id = st.text_input("Patient ID to update")

        new_name = st.text_input("New Name (leave blank to skip)")
        new_city = st.text_input("New City (leave blank to skip)")
        new_age = st.text_input("New Age (leave blank to skip)")
        new_height = st.text_input("New Height (leave blank to skip)")
        new_weight = st.text_input("New Weight (leave blank to skip)")

        new_gender = st.selectbox(
            "New Gender",
            ["No change", "Male", "Female"]
        )

        update_button = st.form_submit_button("Update Patient")

    if update_button:
        payload = {}

        if new_name.strip():
            payload["name"] = new_name.strip()

        if new_city.strip():
            payload["city"] = new_city.strip()

        try:
            if new_age.strip():
                payload["age"] = int(new_age)

            if new_height.strip():
                payload["height"] = float(new_height)

            if new_weight.strip():
                payload["weight"] = float(new_weight)

            if new_gender != "No change":
                payload["gender"] = new_gender

            if not update_id.strip():
                st.warning("Enter a patient ID.")
            elif not payload:
                st.warning("Enter at least one field to update.")
            else:
                call_api(
                    "PUT",
                    f"/edit/{update_id.strip()}",
                    json=payload
                )

        except ValueError:
            st.error("Age, height and weight must contain valid numbers.")


# 5. DELETE PATIENT
with delete_tab:
    st.subheader("Delete Patient")

    with st.form("delete_form"):
        delete_id = st.text_input("Patient ID to delete")
        confirm = st.checkbox("I confirm that I want to delete this patient")
        delete_button = st.form_submit_button("Delete Patient")

    if delete_button:
        if not delete_id.strip():
            st.warning("Enter a patient ID.")
        elif not confirm:
            st.warning("Please confirm before deleting.")
        else:
            call_api(
                "DELETE",
                f"/delete/{delete_id.strip()}"
            )


# 6. SORT PATIENTS
with sort_tab:
    st.subheader("Sort Patient Records")

    with st.form("sort_form"):
        sort_by = st.selectbox(
            "Sort By", ["height", "weight", "bmi"]
        )

        order = st.selectbox(
            "Order", ["asc", "desc"]
        )

        sort_button = st.form_submit_button("Sort Records")

    if sort_button:
        call_api(
            "GET",
            "/sort",
            params={
                "sort_by": sort_by,
                "order": order
            }
        )


st.sidebar.divider()
st.sidebar.markdown("### Project Information")
st.sidebar.write("Frontend: Streamlit")
st.sidebar.write("Backend: FastAPI")
st.sidebar.write("Data: JSON file")
st.sidebar.caption("Built for FastAPI practice")
