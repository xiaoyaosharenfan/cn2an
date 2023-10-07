NUMBER_CN2AN = {
    "零": 0,
    "〇": 0,
    "一": 1,
    "壹": 1,
    "幺": 1,
    "二": 2,
    "贰": 2,
    "两": 2,
    "三": 3,
    "叁": 3,
    "四": 4,
    "肆": 4,
    "五": 5,
    "伍": 5,
    "六": 6,
    "陆": 6,
    "七": 7,
    "柒": 7,
    "八": 8,
    "捌": 8,
    "九": 9,
    "玖": 9,
}
UNIT_EN2AN = {
    "q": "千",
    "k": "千",
    "w": "万",
    "e": "亿",
    "y": "亿",
}
UNIT_CN2AN = {
    "十": 10,
    "拾": 10,
    "百": 100,
    "佰": 100,
    "千": 1000,
    "仟": 1000,
    "万": 10000,
    "亿": 100000000,
}
UNIT_LOW_AN2CN = {
    10: "十",
    100: "百",
    1000: "千",
    10000: "万",
    100000000: "亿",
}
NUMBER_LOW_AN2CN = {
    0: "零",
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    6: "六",
    7: "七",
    8: "八",
    9: "九",
}
NUMBER_UP_AN2CN = {
    0: "零",
    1: "壹",
    2: "贰",
    3: "叁",
    4: "肆",
    5: "伍",
    6: "陆",
    7: "柒",
    8: "捌",
    9: "玖",
}
UNIT_LOW_ORDER_AN2CN = [
    "",
    "十",
    "百",
    "千",
    "万",
    "十",
    "百",
    "千",
    "亿",
    "十",
    "百",
    "千",
    "万",
    "十",
    "百",
    "千",
]
UNIT_UP_ORDER_AN2CN = [
    "",
    "拾",
    "佰",
    "仟",
    "万",
    "拾",
    "佰",
    "仟",
    "亿",
    "拾",
    "佰",
    "仟",
    "万",
    "拾",
    "佰",
    "仟",
]
STRICT_CN_NUMBER = {
    "零": "零",
    "一": "一壹",
    "二": "二贰",
    "三": "三叁",
    "四": "四肆",
    "五": "五伍",
    "六": "六陆",
    "七": "七柒",
    "八": "八捌",
    "九": "九玖",
    "十": "十拾",
    "百": "百佰",
    "千": "千仟",
    "万": "万",
    "亿": "亿",
}
NORMAL_CN_NUMBER = {
    "零": "零〇",
    "一": "一壹幺",
    "二": "二贰两",
    "三": "三叁仨",
    "四": "四肆",
    "五": "五伍",
    "六": "六陆",
    "七": "七柒",
    "八": "八捌",
    "九": "九玖",
    "十": "十拾",
    "百": "百佰",
    "千": "千仟",
    "万": "万",
    "亿": "亿",
}
CN_NUM_AFTER_INTERTNAL_ZERO = {
    "零十": "零一十",
    "零百": "零一百",
    "零千": "零一千",
    "零万": "零一万",
    "零亿": "零一亿",
}