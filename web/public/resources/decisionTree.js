var simple_chart_config = {
	chart: {
		container: "#tree-simple"
	},
	
	nodeStructure: {
		text: { name: "odor == none" },
		children: [
			{
				text: { name: "spore-print-color == green"},
				children:[
					{
						text: {name: "poisonous"}
					},
					{
						text: {name: "stalk-surface-below-ring == scaly"},
						children:[
							{
								text: {name: "gill-size == narrow"},
								children:[
									{
										text: {name: "poisonous"},
									},
									{
										text: {name: "eatable"},
									}
								]
							},
							{
								text: {name: "cap-surface == grooves"},
								children:[
									{
										text: {name: "poisonous"},
									},
									{
										text: {name: "eatable"},
									}
								]
							}
						]
					}
				]
			},
			{
				text: { name: "bruises == bruises"},
				children:[
					{
						text: {name: "stalk-root == club"},
						children:[
							{
								text: {name: "eatable"}
							},
							{
								text: {name: "stalk-root == rooted"},
								children:[
									{
										text: {name: "eatable"}
									},
									{
										text: {name: "gill-spacing == close"},
										children:[
											{
												text: {name: "poisonous"}
											},
											{
												text: {name: "eatable"}
											}
										]
									}
								]
							}
						]
					},
					{
						text: {name: "poisonous"}
					}
				]
			}
		]
	}
};