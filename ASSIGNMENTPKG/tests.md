# TESTS.md

## Usage 

```python
!pip install git+https://github.com/marwaamostafa/Summative_Assignmet_pkg
from assignmentpkg import Analysis

analysis_obj = Analysis('configs/analysis_config.yml')
analysis_obj.load_data()

analysis_output = analysis_obj.compute_analysis()
print(analysis_output)

analysis_figure = analysis_obj.plot_data()
