  # Using the Opentrons OT-2 for Liquid Handling and Loading Fronds
  Examples of previous protocols are also on the lab computer.

  ## Loading duckweed fronds
  This works best for 96-well plates. Other well sizes will lead to inconsistencies in the number of plants loaded per well (i.e., much more than 1). In the 'older documents' folder, there is a PDF from Talha with instructions on how to use the OT-2 for duckweed loading. Some parts of the software may look different due to recent updates, but most of it is the same. There is also an older version of the duckweed loading protocol on the lab computer.

  ## Liquid handling
  - Opentrons has an online designer tool that makes it easy to create robot protocols: https://designer.opentrons.com/
  
  The output is a .json file that can be uploaded onto the OT-2
  
  An example of a protocol created using the designer tool is provided. Note that this was originally created on an older version of the Opentrons Protocol Designer.

  - Opentrons also has the Python API for more customization in the workflow: https://docs.opentrons.com/v2/

  - There is also the Protocol Library, which contains workflows created using the Python API: https://protocols.opentrons.com/
  Not all of these have been verified by the Opentrons team, so use and adapt at your own risk.
