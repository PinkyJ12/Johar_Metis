import pickle
import pandas as pd

model_info = pickle.load( open( "pkl_muffins_cupcakes.p", "rb" ), encoding='latin1' )
mc_model = model_info['muffin_cupcake_model']

def muffin_or_cupcake(flour_cups_float, milk_cups_float, sugar_cups_float,
                        butter_cups_float, eggs_num_float, bp_tsp_float,
                        vanilla_tsp_float, salt_tsp_float, mc_model=mc_model):
    
    total = 16 * flour_cups_float + \
            16 * milk_cups_float + \
            16 * sugar_cups_float + \
            16 * butter_cups_float + \
            3 * eggs_num_float + \
            .33 * bp_tsp_float + \
            .33 * vanilla_tsp_float + \
            .33 * salt_tsp_float

    flour_cups_prop = 16 * flour_cups_float * 100.0 / total
    milk_cups_prop = 16 * milk_cups_float * 100.0 / total
    sugar_cups_prop = 16 * sugar_cups_float * 100.0 / total
    butter_cups_prop = 16 * butter_cups_float * 100.0 / total
    eggs_num_prop = 3 * eggs_num_float * 100.0 / total
    bp_tsp_prop = .33 * bp_tsp_float * 100.0 / total
    vanilla_tsp_prop = .33 * vanilla_tsp_float * 100.0 / total
    salt_tsp_prop = .33 * salt_tsp_float * 100.0 / total

    input_df = pd.DataFrame({'Flour': flour_cups_prop,
                             'Sugar': sugar_cups_prop}, index=[0])
                             #'Milk': milk_cups_prop,
                             #'Butter': butter_cups_prop,
                             #'Eggs': eggs_num_prop,
                             #'Baking Powder': bp_tsp_prop,
                             #'Vanilla': vanilla_tsp_prop
                             #'Salt': salt_tsp_prop

    prediction = mc_model.predict(input_df)[0]

    message_array = ["You have a muffin!",
                     "You have a cupcake!"]

    return message_array[prediction]