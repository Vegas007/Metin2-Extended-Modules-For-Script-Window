import uiScriptLocale

UI_WIDTH	= 115
UI_HEIGHT	= 130

window = {
	"name" : "MainWindow",
	"style" : ("movable", "float",),
	"x" : SCREEN_WIDTH / 2 - UI_WIDTH / 2,
	"y" : SCREEN_HEIGHT / 2 - UI_HEIGHT / 2,
	"width" : UI_WIDTH,
	"height" : UI_HEIGHT,
	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			"x" : 0,
			"y" : 0,
			"width" : UI_WIDTH,
			"height" : UI_HEIGHT,
			"title" : "Window",
			"children" :
			(
			    {
					"name" : "HideButton",
					"type" : "button",
					"x" : 15,
					"y" : 40,
					"text" : "HideButton",
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "ShowButton",
					"type" : "button",
					"x" : 15,
					"y" : 40 + (30 * 1),
					"text" : "ShowButton",
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "UpdateButton",
					"type" : "button",
					"x" : 15,
					"y" : 40 + (30 * 2),
					"text" : "UpdateButton",
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
			),
		},
	),
}