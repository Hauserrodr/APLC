### Welcome to Animal Per Lot Calculator
import streamlit as st

st.session_state.mean_weight = 350.0
st.session_state.consumption = 2.5
st.session_state.risk = 2.0
st.session_state.max_area = 29
st.session_state.ms_production = 10000
st.session_state.time = 90.0
st.session_state.animals = 100
st.session_state.animal_per_hectare = 3.17
st.session_state.total_animals=91.90
st.session_state.area_needed=31.50
st.title('Animal Per Lot Calculator')
st.subheader('Change de variables to calculate the number of animals each hectare can hold')
st.markdown('''

''')
st.markdown('''

''')
st.markdown('''

''')
t1 = st.empty()
t2 = st.empty()
t3 = st.empty()
t1.markdown(f'**Animals per hectare:** {"{:.2f}".format(st.session_state.animal_per_hectare)} animals')
t2.markdown(f'**Total animals supported in property:** {"{:.2f}".format(st.session_state.total_animals)} animals')
t3.markdown(f'**Total area needed:** {"{:.2f}".format(st.session_state.area_needed)} hectare')
bt1,bt2,bt3 = st.columns(3)

st.session_state.mean_weight = bt1.number_input('Animals mean weight \n ', min_value=50.0,max_value=700.0,value=350.0)
st.session_state.consumption = bt2.number_input('Consumption per animal in %  of LW', min_value=0.01,max_value=100.0,value=2.5)
st.session_state.risk = bt3.number_input('Correction factor', min_value=0.0,max_value=10.0,value=2.0)
st.session_state.max_area = bt1.number_input('Total area (in ha)\n ', min_value=0.1,max_value=10000.0,value=29.0)
st.session_state.ms_production = bt2.number_input('Pasture production in kg of DM per ha', min_value=100.0,max_value=50000.0,value=10000.0)
st.session_state.time = bt3.number_input('Length of stay in days', min_value=1.0,max_value=365.0,value=90.0)
st.session_state.animals = bt1.number_input('Number of animals', min_value=1.0,max_value=5000.0,value=100.0)
bt3.subheader('\n')
def calculate_apl():
    cons_per_animal = st.session_state.mean_weight*(st.session_state.consumption/100)*st.session_state.risk
    st.session_state.animal_per_hectare = st.session_state.ms_production/(cons_per_animal*st.session_state.time)
    st.session_state.total_animals = st.session_state.animal_per_hectare*st.session_state.max_area
    st.session_state.area_needed = (cons_per_animal*st.session_state.animals*st.session_state.time)/st.session_state.ms_production
calculate_apl()
t1.markdown(f'**Animals per hectare:** {"{:.2f}".format(st.session_state.animal_per_hectare)} animals')
t2.markdown(f'**Total animals supported in property:** {"{:.2f}".format(st.session_state.total_animals)} animals')
t3.markdown(f'**Total area needed:** {"{:.2f}".format(st.session_state.area_needed)} hectare')

