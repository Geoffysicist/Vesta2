from pyropy import firebehaviour as fb
from pyropy import weatherdata as wd

#read the weather data into a pandas DataFrame
weather_fn = 'weather_gridded_in.csv'
weather_df = wd.gridded_to_df(weather_fn)

#create an Incident using the weather data
incident = fb.Incident(weather_df)

#add the parameters necessary to run the desired models
incident_params = {
    #forest_mk5
    'waf': 3.5,
    'fuel_load': 15,
    #forest_vesta
    'fhs_surf': 3.5,
    'fhs_n_surf': 2,
    'fuel_height_ns': 20
}
incident.set_params(incident_params)

#run the desired models
incident.run_forest_mk5()
incident.run_forest_vesta()

#output results
incident.print(head=True)

   
