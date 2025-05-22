import numpy as np
import pandas as pd

### RESCALING WEIGHTS TO HAVE POPULATION PROPORTIONAL REPRESENTATION FROM EACH COUNTRY
def rescale_weights_prop_pop_size(original_df, pop_size_df, weight_col, country_col):
    rescaled_weights_df = original_df.copy()

    # Original Weights
    country_weight_sums = rescaled_weights_df.groupby(country_col)[weight_col].sum()
    overall_weight_sum = country_weight_sums.sum()
    country_weight_proportions = country_weight_sums / overall_weight_sum

    # Population size
    overall_total_population = pop_size_df['Population size estimate'].sum()
    country_population_proportions = pop_size_df.set_index(country_col)['Population size estimate'] / overall_total_population

    # Adjustment factor
    adjustment_factors = country_population_proportions / country_weight_proportions
    adjustment_dict = adjustment_factors.to_dict()

    # Use adjustment fcator to rescale weights
    rescaled_weights_df['rescaled_weights'] = rescaled_weights_df.apply(lambda row: row[weight_col] * adjustment_dict[row[country_col]], axis=1)
    
    return rescaled_weights_df



