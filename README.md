# tda-cell-classification-full

In summer 2026 term, I worked with Dr. Leah Edelstein-Keshet and Dr. Dhananjay Bhaskar on a
project: building a shape descriptor for segmented cell images using topological data analysis (TDA).
We developed an unsupervised cell classification tool that provides quantitative visualization of
perturbation effects. This tool can be applied to differentiate healthy from diseased cells.
Cell shape is a rich, label-free readout of a cell’s state and environment, but the common way of
storing shape as a raw 2D pixels is very sensitive to imaging noise and small deformations. Our
goal was to come up with a descriptor represents 2D segmented cell shape that is interpretable
and maintain translation and rotation invariants that is compatible with unsupervised classification
pipeline. In this report I describe the motivation and the pipeline I implemented. This project is
inspired by Dr. Dhananjay Bhaskar’s Master Thesis (University of British Columbia, 2017). 

In PMA_cells folder

01 - Extract features

02 - Extract Persistent diagrams and images

03 - Extract latent from Autoencoder 

