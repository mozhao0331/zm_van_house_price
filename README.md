# Vancouver Housing Market Dashboard

-   Author: Morris Zhao

Thank you for being interested in the Vancouver Housing Market App!

Render Link click [here](https://van-house.onrender.com/)

The app is designed to provide an interactive and informative way to explore the Vancouver housing market. Whether you're a real estate professional, a data analyst, or simply curious about housing trends in Vancouver, our app has something for you.

I hope you find our app useful and informative. Happy exploring!

The purpose of the app is to provide a user-friendly, interactive, and informative tool for monitoring Vancouver's housing market. The app aggregates data on housing prices from the City of Vancouver Open Data Portal and presents it in an engaging format, allowing users to gain insights into trends and patterns over time.

The motivation for developing this app was to create a comprehensive and informative app that can serve as a valuable resource for anyone interested in understanding Vancouver's housing market. The app is designed to be user-friendly and interactive, with a range of visualizations that help users make sense of the presented information. Ultimately, the goal is to help users stay informed about the state of the market and make better-informed decisions.

More details can be found in the proposal [here](https://github.com/UBC-MDS/van_houses/blob/main/reports/proposal.md).

## Description & Usage

-   **Bar Chart 1**: You can choose different year of built of the houses from the drop box and use slide bar to define a range for house price. Then the bar chart will show average property price for each report year according to your interested.
-   **Bar Chart 2**: You can choose different year of built of the houses from the drop box and use slide bar to define a range for house price. Then the bar chart will show average property price for each legal type according to your interested.

Ideally all the interactive features in these 2 visualizations are linked together. When you make a selection on one chart, the other one will update accordingly as well.

On the top of the app there are drop down menu, and slide bar to let you select data points under certain criteria. Currently the design is to let you filter by `price` and `year built`. These filters will apply to all the 2 visualizations in the bottom.

## Installation

To install `van_houses` locally, run the app by following these instructions:

1.  Clone this repository locally.
2.  Open Visual Studio Code and navigate to the directory where you downloaded this repository.
3.  Open the van_app.py file in Visual Studio Code.
4.  Use the terminal console to run the following command to install the required packages:

```{r}
pip.install(dash, dash_bootstrap_components, pandas, altair)
```

5.  Run the app by clicking the "Run" button in the top right corner of the Visual Studio Code window.

6.  Copy and paste the link to your website and run the app.

Your web browser should now open the app. You may interact with the app and explore information about the housing market in Vancouver.

## Contributing

I welcome anyone who is interested in contributing to our app for Vancouver's housing market. The project is open-source, which means that anyone can view and contribute to the code on our GitHub repository.

If you are interested in getting involved, check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## Contact us

If you have any questions, feedback, or suggestions about our Vancouver Housing Market app, I would love to hear from you! You can contact me by visiting our GitHub repository and creating a new issue. This is the best way to reach us if you have technical questions or issues with the app.

## License

Licensed under the terms of the MIT license.

## Reference

The data set I am going to visualize is the data set contains information on properties from [BC Assessment (BCA) and City sources](https://opendata.vancouver.ca/api/v2/console) from 2020. There are 871,053 observation in this data set. Each data point has 29 associated variables that describe the property.
