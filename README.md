# normaliser

Project folder structure: 

<ul>
<li> Analysis : contains the notebook files </li>
<li> Results : contains generated data </li>
<li> Data : contains original LFP data </li>
<li> Figures : contains generated figures </li>
</ul>


Project analysis pipeline: 

<ul>

<li> Setter.ipynb : The first notebook to run. Sets trial markers and study related information such as sampling rate, trial type, .... </li>

<li> Infographics.ipynb : Run this notebook to plot experimental setup and protocol related figures </li>

<li> Compute_dominant_frequency.ipynb : Run this notebook to compute the theta dominant frequency. It will save numpy array (log_welch) in '../Results/log_welch'. The following notebooks will need this data. </li>

<li> Stats_on_dominant_frequency.ipynb : Run this notebook to organize dominant frequency among conditions (cues_per_sec, speed (low,mid,high), density(low,mid,high)). Each cell saves a model containing the averaged data of its corresponding analysis (cues_sec, speed, density). </li>

<li> Compute_ITC.ipynb : Run this notebook to get Inter-trial phase coherence at movement onset. </li>


<li> Power_movement_onset.ipynb : Run this notebook to get oscillatory power throughout navigation. </li>


</ul>
