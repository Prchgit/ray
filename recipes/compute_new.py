# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
customers_unlabeled_prepared_scored = dataiku.Dataset("customers_unlabeled_prepared_scored")
customers_unlabeled_prepared_scored_df = customers_unlabeled_prepared_scored.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

new_df = customers_unlabeled_prepared_scored_df # For this sample code, simply copy input to output


# Write recipe outputs
new = dataiku.Dataset("new")
new.write_with_schema(new_df)
