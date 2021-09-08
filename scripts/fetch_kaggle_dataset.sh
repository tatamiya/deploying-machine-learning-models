#!/usr/bin/env bash
export DIR_DATASETS=regression_model/datasets/

poetry run kaggle competitions download -c house-prices-advanced-regression-techniques -p $DIR_DATASETS
unzip $DIR_DATASETS*.zip -d $DIR_DATASETS