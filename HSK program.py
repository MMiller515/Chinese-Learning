import tkinter as tk
import random
import traceback

# HSK banks with pinyin and meanings
hsk_bank1 = {
    "爱": {"english": "Love", "pinyin": "Ài"},
    "八": {"english": "Eight", "pinyin": "Bā"},
    "爸爸": {"english": "Dad", "pinyin": "Bàba"},
    "杯子": {"english": "Cup", "pinyin": "Bēizi"},
    "本": {"english": "Book", "pinyin": "Běn"},
    "不客气": {"english": "You're welcome", "pinyin": "Bù kèqì"},
    "不": {"english": "Not", "pinyin": "Bù"},
    "菜": {"english": "Vegetable", "pinyin": "Cài"},
    "茶": {"english": "Tea", "pinyin": "Chá"},
    "吃": {"english": "Eat", "pinyin": "Chī"},
    "出租车": {"english": "Taxi", "pinyin": "Chūzūchē"},
    "打电话": {"english": "Make a phone call", "pinyin": "Dǎ diànhuà"},
    "大": {"english": "Big", "pinyin": "Dà"},
    "的": {"english": "Of, possessive particle", "pinyin": "De"},
    "点": {"english": "O'clock, a little", "pinyin": "Diǎn"},
    "电脑": {"english": "Computer", "pinyin": "Diànnǎo"},
    "电视": {"english": "Television", "pinyin": "Diànshì"},
    "电影": {"english": "Movie", "pinyin": "Diànyǐng"},
    "东西": {"english": "Thing, stuff", "pinyin": "Dōngxi"},
    "都": {"english": "Both, all", "pinyin": "Dōu"},
    "读": {"english": "Read", "pinyin": "Dú"},
    "对不起": {"english": "Sorry", "pinyin": "Duìbùqǐ"},
    "多": {"english": "Many, much", "pinyin": "Duō"},
    "多少": {"english": "How many", "pinyin": "Duōshǎo"},
    "儿子": {"english": "Son", "pinyin": "Érzi"},
    "二": {"english": "Two", "pinyin": "Èr"},
    "饭店": {"english": "Restaurant", "pinyin": "Fàndiàn"},
    "飞机": {"english": "Airplane", "pinyin": "Fēijī"},
    "分钟": {"english": "Minute", "pinyin": "Fēnzhōng"},
    "高兴": {"english": "Happy", "pinyin": "Gāoxìng"},
    "个": {"english": "Individual, a measure word", "pinyin": "Gè"},
    "工作": {"english": "Job, work", "pinyin": "Gōngzuò"},
    "狗": {"english": "Dog", "pinyin": "Gǒu"},
    "汉语": {"english": "Chinese language", "pinyin": "Hànyǔ"},
    "好": {"english": "Good", "pinyin": "Hǎo"},
    "号": {"english": "Number, date", "pinyin": "Hào"},
    "喝": {"english": "Drink", "pinyin": "Hē"},
    "和": {"english": "And", "pinyin": "Hé"},
    "很": {"english": "Very", "pinyin": "Hěn"},
    "后面": {"english": "Behind", "pinyin": "Hòumiàn"},
    "会": {"english": "Can, know how to", "pinyin": "Huì"},
    "回": {"english": "Return, go back", "pinyin": "Huí"},
    "几": {"english": "How many", "pinyin": "Jǐ"},
    "家": {"english": "Family, home", "pinyin": "Jiā"},
    "叫": {"english": "To call, be called", "pinyin": "Jiào"},
    "今天": {"english": "Today", "pinyin": "Jīntiān"},
    "九": {"english": "Nine", "pinyin": "Jiǔ"},
    "开": {"english": "Open; Start", "pinyin": "Kāi"},
    "看": {"english": "See; Look at", "pinyin": "Kàn"},
    "看见": {"english": "See; Catch sight of", "pinyin": "Kànjiàn"},
    "口": {"english": "Mouth", "pinyin": "Kǒu"},
    "块": {"english": "Piece", "pinyin": "Kuài"},
    "来": {"english": "Come", "pinyin": "Lái"},
    "老师": {"english": "Teacher", "pinyin": "Lǎoshī"},
    "了": {"english": "Particle indicating a completed action", "pinyin": "Le"},
    "冷": {"english": "Cold", "pinyin": "Lěng"},
    "里": {"english": "Inside", "pinyin": "Lǐ"},
    "六": {"english": "Six", "pinyin": "Liù"},
    "妈妈": {"english": "Mom", "pinyin": "Māma"},
    "吗": {"english": "Question particle", "pinyin": "Ma"},
    "买": {"english": "Buy", "pinyin": "Mǎi"},
    "猫": {"english": "Cat", "pinyin": "Māo"},
    "没关系": {"english": "It doesn't matter", "pinyin": "Méi guānxi"},
    "没有": {"english": "Don't have", "pinyin": "Méiyǒu"},
    "米饭": {"english": "Cooked rice", "pinyin": "Mǐfàn"},
    "名字": {"english": "Name", "pinyin": "Míngzì"},
    "明天": {"english": "Tomorrow", "pinyin": "Míngtiān"},
    "哪": {"english": "Which", "pinyin": "Nǎ"},
    "哪儿": {"english": "Where", "pinyin": "Nǎr"},
    "那": {"english": "That", "pinyin": "Nà"},
    "呢": {"english": "Question particle", "pinyin": "Ne"},
    "能": {"english": "Can; Be able to", "pinyin": "Néng"},
    "你": {"english": "You", "pinyin": "Nǐ"},
    "年": {"english": "Year", "pinyin": "Nián"},
    "女儿": {"english": "Daughter", "pinyin": "Nǚ'ér"},
    "朋友": {"english": "Friend", "pinyin": "Péngyǒu"},
    "漂亮": {"english": "Pretty", "pinyin": "Piàoliang"},
    "苹果": {"english": "Apple", "pinyin": "Píngguǒ"},
    "七": {"english": "Seven", "pinyin": "Qī"},
    "前面": {"english": "Front; In front of", "pinyin": "Qiánmiàn"},
    "钱": {"english": "Money", "pinyin": "Qián"},
    "请": {"english": "Please", "pinyin": "Qǐng"},
    "去": {"english": "Go", "pinyin": "Qù"},
    "热": {"english": "Hot", "pinyin": "Rè"},
    "人": {"english": "Person", "pinyin": "Rén"},
    "认识": {"english": "Know; Be acquainted with", "pinyin": "Rènshi"},
    "三": {"english": "Three", "pinyin": "Sān"},
    "商店": {"english": "Store", "pinyin": "Shāngdiàn"},
    "上": {"english": "Above; On top of", "pinyin": "Shàng"},
    "少": {"english": "Few; Little", "pinyin": "Shǎo"},
    "谁": {"english": "Who", "pinyin": "Shéi"},
    "什么": {"english": "What", "pinyin": "Shénme"},
    "十": {"english": "Ten", "pinyin": "Shí"},
    "时候": {"english": "Time; When", "pinyin": "Shíhòu"},
    "是": {"english": "To be", "pinyin": "Shì"},
    "书": {"english": "Book", "pinyin": "Shū"},
    "水": {"english": "Water", "pinyin": "Shuǐ"},
    "水果": {"english": "Fruit", "pinyin": "Shuǐguǒ"},
    "睡觉": {"english": "Sleep", "pinyin": "Shuìjiào"},
    "说": {"english": "Say; Speak", "pinyin": "Shuō"},
    "四": {"english": "Four", "pinyin": "Sì"},
    "岁": {"english": "Year (of age)", "pinyin": "Suì"},
    "他": {"english": "He", "pinyin": "Tā"},
    "她": {"english": "She", "pinyin": "Tā"},
    "它": {"english": "It", "pinyin": "Tā"},
    "太": {"english": "Too; Very", "pinyin": "Tài"},
    "天气": {"english": "Weather", "pinyin": "Tiānqì"},
    "听": {"english": "Listen", "pinyin": "Tīng"},
    "同学": {"english": "Classmate", "pinyin": "Tóngxué"},
    "喂": {"english": "Hello (on the phone)", "pinyin": "Wèi"},
    "我": {"english": "I; Me", "pinyin": "Wǒ"},
    "我们": {"english": "We; Us", "pinyin": "Wǒmen"},
    "五": {"english": "Five", "pinyin": "Wǔ"},
    "喜欢": {"english": "Like", "pinyin": "Xǐhuān"},
    "下": {"english": "Under; Below", "pinyin": "Xià"},
    "下午": {"english": "Afternoon", "pinyin": "Xiàwǔ"},
    "下雨": {"english": "Rain", "pinyin": "Xiàyǔ"},
    "先生": {"english": "Mr.; Sir", "pinyin": "Xiānsheng"},
    "现在": {"english": "Now", "pinyin": "Xiànzài"},
    "想": {"english": "Think; Want", "pinyin": "Xiǎng"},
    "些": {"english": "Some; Few", "pinyin": "Xiē"},
    "写": {"english": "Write", "pinyin": "Xiě"},
    "谢谢": {"english": "Thank you", "pinyin": "Xièxiè"},
    "星期": {"english": "Week", "pinyin": "Xīngqī"},
    "学生": {"english": "Student", "pinyin": "Xuéshēng"},
    "学习": {"english": "Study", "pinyin": "Xuéxí"},
    "学校": {"english": "School", "pinyin": "Xuéxiào"},
    "一": {"english": "One", "pinyin": "Yī"},
    "衣服": {"english": "Clothes", "pinyin": "Yīfu"},
    "医生": {"english": "Doctor", "pinyin": "Yīshēng"},
    "医院": {"english": "Hospital", "pinyin": "Yīyuàn"},
    "椅子": {"english": "Chair", "pinyin": "Yǐzi"},
    "一点儿": {"english": "A little", "pinyin": "Yīdiǎnr"},
    "有": {"english": "Have", "pinyin": "Yǒu"},
    "月": {"english": "Month", "pinyin": "Yuè"},
    "再见": {"english": "Goodbye", "pinyin": "Zàijiàn"},
    "在": {"english": "At; In", "pinyin": "Zài"},
    "怎么": {"english": "How", "pinyin": "Zěnme"},
    "怎么样": {"english": "How about", "pinyin": "Zěnmeyàng"},
    "这": {"english": "This", "pinyin": "Zhè"},
    "中午": {"english": "Noon", "pinyin": "Zhōngwǔ"},
    "住": {"english": "Live; Reside", "pinyin": "Zhù"},
    "桌子": {"english": "Table", "pinyin": "Zhuōzi"},
    "字": {"english": "Character; Word", "pinyin": "Zì"},
    "昨天": {"english": "Yesterday", "pinyin": "Zuótiān"},
    "坐": {"english": "Sit", "pinyin": "Zuò"},
    "做": {"english": "Do; Make", "pinyin": "Zuò"}
}

hsk_bank2 = {
    "吧": {"pinyin": "ba", "english": "suggestion request or command."},
    "白": {"pinyin": "bái", "english": "white"},
    "百": {"pinyin": "bǎi", "english": "Hundred"},
    "帮助": {"pinyin": "bāngzhù", "english": "to help, assist, to aid"},
    "报纸": {"pinyin": "bàozhǐ", "english": "newspaper"},
    "比": {"pinyin": "bǐ", "english": "Comparison"},
    "别": {"pinyin": "bié", "english": "Don't"},
    "宾馆": {"pinyin": "bīnguǎn", "english": "Hotel"},
    "长": {"pinyin": "chàng", "english": "long"},
    "唱歌": {"pinyin": "chànggē", "english": "To sing"},
    "出": {"pinyin": "chū", "english": "To come/Go out"},
    "穿": {"pinyin": "chuān", "english": "To wear/put on"},
    "次": {"pinyin": "cì", "english": "Time"},
    "从": {"pinyin": "cóng", "english": "from"},
    "错": {"pinyin": "cuò", "english": "wrong, incorrect"},
    "打篮球": {"pinyin": "dǎ lánqiú", "english": "play basketball"},
    "大家": {"pinyin": "dàjiā", "english": "Everyone"},
    "但是": {"pinyin": "dànshì", "english": "but, still, yet"},
    "到": {"pinyin": "dào", "english": "arrive"},
    "得": {"pinyin": "dé", "english": "used after a verb or an adjective to introduce a complement of result or degree"},
    "等": {"pinyin": "děng", "english": "wait"},
    "弟弟": {"pinyin": "dìdì", "english": "younger brother"},
    "第一": {"pinyin": "dì yī", "english": "First"},
    "懂": {"pinyin": "dǒng", "english": "Understand/To know"},
    "对": {"pinyin": "duì", "english": "right, correct"},
    "房间": {"pinyin": "fángjiān", "english": "Room"},
    "非常": {"pinyin": "fēicháng", "english": "Very"},
    "服务员": {"pinyin": "fúwùyuán", "english": "waiter/waitress"},
    "高": {"pinyin": "gāo", "english": "Tall/high"},
    "告诉": {"pinyin": "gàosù", "english": "To tell"},
    "哥哥": {"pinyin": "gēgē", "english": "elder brother"},
    "给": {"pinyin": "gěi", "english": "Give"},
    "公共汽车": {"pinyin": "gōnggòng qìchē", "english": "bus"},
    "公司": {"pinyin": "gōngsī", "english": "company"},
    "贵": {"pinyin": "guì", "english": "expensive"},
    "还": {"pinyin": "hái", "english": "passably, fairly, rather (return)"},
    "孩子": {"pinyin": "háizi", "english": "child"},
    "好吃": {"pinyin": "hào chī", "english": "tasty/delicious"},
    "黑": {"pinyin": "hēi", "english": "black"},
    "红": {"pinyin": "hóng", "english": "red"},
    "火车站": {"pinyin": "huǒ chēzhàn", "english": "TRAIN STATION"},
    "机场": {"pinyin": "jīchǎng", "english": "Airport"},
    "鸡蛋": {"pinyin": "jīdàn", "english": "egg"},
    "件": {"pinyin": "jiàn", "english": "pieces (of clothing)"},
    "觉得": {"pinyin": "juédé", "english": "to think/feel"},
    "教室": {"pinyin": "jiàoshì", "english": "classroom"},
    "姐姐": {"pinyin": "Jiějiě", "english": "elder sister"},
    "介绍": {"pinyin": "jièshào", "english": "introduce/recommend"},
    "进": {"pinyin": "jìn", "english": "Enter"},
    "近": {"pinyin": "jìn", "english": "close"},
    "就": {"pinyin": "jiù", "english": "used to indicate a conclusion or resolution"},
    "咖啡": {"pinyin": "kāfēi", "english": "coffee"},
    "开始": {"pinyin": "kāishǐ", "english": "to begin/ start"},
    "考试": {"pinyin": "kǎoshì", "english": "test/ take an exam"},
    "可能": {"pinyin": "kěnéng", "english": "maybe, perhaps, possible"},
    "可以": {"pinyin": "kěyǐ", "english": "Can"},
    "课": {"pinyin": "kè", "english": "class, lesson"},
    "快": {"pinyin": "kuài", "english": "fast, quick"},
    "快乐": {"pinyin": "kuàilè", "english": "happy/glad"},
    "离": {"pinyin": "lí", "english": "Leave"},
    "两": {"pinyin": "liǎng", "english": "two"},
    "零": {"pinyin": "líng", "english": "zero"},
    "路": {"pinyin": "lù", "english": "road"},
    "旅游": {"pinyin": "lǚyóu", "english": "travel"},
    "慢": {"pinyin": "màn", "english": "slow"},
    "忙": {"pinyin": "máng", "english": "busy"},
    "每": {"pinyin": "měi", "english": "Every"},
    "妹妹": {"pinyin": "mèimei", "english": "younger sister"},
    "门": {"pinyin": "mén", "english": "Door"},
    "面条": {"pinyin": "miàn tiáo", "english": "Noodle"},
    "男": {"pinyin": "nán", "english": "man/male"},
    "牛奶": {"pinyin": "niúnǎi", "english": "milk"},
    "女": {"pinyin": "nǚ", "english": "female"},
    "旁边": {"pinyin": "pángbiān", "english": "beside"},
    "跑步": {"pinyin": "pǎobù", "english": "running"},
    "便宜": {"pinyin": "piányí", "english": "Cheap"},
    "票": {"pinyin": "piào", "english": "ticket"},
    "妻子": {"pinyin": "qīzi", "english": "wife"},
    "起床": {"pinyin": "qǐchuáng", "english": "get up"},
    "千": {"pinyin": "qiān", "english": "thousand"},
    "铅笔": {"pinyin": "qiānbǐ", "english": "pencil"},
    "晴": {"pinyin": "qíng", "english": "clear"},
    "去年": {"pinyin": "qùnián", "english": "last year"},
    "让": {"pinyin": "ràng", "english": "to let/ allow"},
    "日": {"pinyin": "rì", "english": "day/date"},
    "上班": {"pinyin": "shàngbān", "english": "work"},
    "身体": {"pinyin": "shēntǐ", "english": "Body"},
    "生病": {"pinyin": "shēngbìng", "english": "Get ill"},
    "生日": {"pinyin": "shēngrì", "english": "Birthday"},
    "时间": {"pinyin": "shíjiān", "english": "time"},
    "事情": {"pinyin": "shìqíng", "english": "thing,matter,or affair"},
    "手表": {"pinyin": "shǒubiǎo", "english": "watch"},
    "手机": {"pinyin": "shǒujī", "english": "cell phone"},
    "说话": {"pinyin": "shuōhuà", "english": "say"},
    "送": {"pinyin": "sòng", "english": "to send, to deliver"},
    "虽然": {"pinyin": "suīrán", "english": "Although"},
    "所以": {"pinyin": "suǒyǐ", "english": "so"},
    "它": {"pinyin": "tā", "english": "it"},
    "踢足球": {"pinyin": "tī zúqiú", "english": "play soccer"},
    "题": {"pinyin": "tí", "english": "question"},
    "跳舞": {"pinyin": "tiàowǔ", "english": "Dance"},
    "外": {"pinyin": "wài", "english": "outside"},
    "玩": {"pinyin": "wán", "english": "Play"},
    "玩儿": {"pinyin": "wán er", "english": "play"},
    "晚上": {"pinyin": "wǎnshàng", "english": "night"},
    "往": {"pinyin": "wǎng", "english": "Past"},
    "为什么": {"pinyin": "wèishéme", "english": "Why"},
    "问": {"pinyin": "wèn", "english": "ask"},
    "问题": {"pinyin": "wèntí", "english": "question"},
    "西瓜": {"pinyin": "xīguā", "english": "watermelon"},
    "希望": {"pinyin": "xīwàng", "english": "hope"},
    "洗": {"pinyin": "xǐ", "english": "wash"},
    "小时": {"pinyin": "xiǎoshí", "english": "Hour"},
    "笑": {"pinyin": "xiào", "english": "laugh"},
    "新": {"pinyin": "xīn", "english": "new"},
    "姓": {"pinyin": "xìng", "english": "surname"},
    "休息": {"pinyin": "xiūxí", "english": "rest"},
    "雪": {"pinyin": "xuě", "english": "Snow"},
    "颜色": {"pinyin": "yánsè", "english": "color"},
    "眼睛": {"pinyin": "yǎnjīng", "english": "Eye"},
    "羊肉": {"pinyin": "yángròu", "english": "mutton"},
    "药": {"pinyin": "yào", "english": "medicine"},
    "要": {"pinyin": "yào", "english": "want"},
    "也": {"pinyin": "yě", "english": "also"},
    "一下": {"pinyin": "yīxià", "english": "one time- used after a verb, indicating an act or attempt"},
    "已经": {"pinyin": "yǐjīng", "english": "already"},
    "一起": {"pinyin": "yīqǐ", "english": "Together"},
    "意思": {"pinyin": "yìsi", "english": "meaning"},
    "因为": {"pinyin": "yīnwèi", "english": "because"},
    "阴": {"pinyin": "yīn", "english": "overcast/cloudy"},
    "游泳": {"pinyin": "yóuyǒng", "english": "swim"},
    "右边": {"pinyin": "yòubiān", "english": "right"},
    "鱼": {"pinyin": "yú", "english": "fish"},
    "远": {"pinyin": "yuǎn", "english": "Far"},
    "运动": {"pinyin": "yùndòng", "english": "sports"},
    "再": {"pinyin": "zài", "english": "Again"},
    "早上": {"pinyin": "zǎoshang", "english": "Morning"},
    "丈夫": {"pinyin": "zhàngfū", "english": "husband"},
    "找": {"pinyin": "zhǎo", "english": "to look for/ try to find"},
    "着": {"pinyin": "zhe", "english": "(used to indicate a state)With"},
    "真": {"pinyin": "zhēn", "english": "really, indeed"},
    "正在": {"pinyin": "zhèng zài", "english": "in the process of (are)"},
    "知道": {"pinyin": "zhīdào", "english": "Know"},
    "准备": {"pinyin": "zhǔnbèi", "english": "Prepare/ plan"},
    "走": {"pinyin": "zǒu", "english": "Walk"},
    "最": {"pinyin": "zuì", "english": "the most, to the greatest extent"},
    "左边": {"pinyin": "zuǒbiān", "english": "left side"},
}   

hsk_bank3 = {
    "阿姨": {"pinyin": "Āyí", "english": "Aunt"},
    "啊": {"pinyin": "a", "english": "ah"},
    "矮": {"pinyin": "ǎi", "english": "short"},
    "爱好": {"pinyin": "àihào", "english": "Hobby, interest"},
    "安静": {"pinyin": "ānjìng", "english": "Quiet"},
    "把": {"pinyin": "bǎ", "english": "Used for things w/ handle"},
    "班": {"pinyin": "bān", "english": "class"},
    "搬家": {"pinyin": "bānjiā", "english": "To move or carry"},
    "办法": {"pinyin": "bànfǎ", "english": "Way, approach"},
    "办公室": {"pinyin": "bàngōngshì", "english": "office"},
    "半": {"pinyin": "bàn", "english": "Half"},
    "帮忙": {"pinyin": "bāngmáng", "english": "To help"},
    "包": {"pinyin": "bāo", "english": "Bag, sack"},
    "饱": {"pinyin": "bǎo", "english": "full, from eating"},
    "北方": {"pinyin": "běifāng", "english": "north"},
    "被": {"pinyin": "bèi", "english": "Used to indicate passive voice"},
    "鼻子": {"pinyin": "bízi", "english": "nose"},
    "比较": {"pinyin": "bǐjiào", "english": "Fairly, Rather"},
    "比赛": {"pinyin": "bǐsài", "english": "Match or competition"},
    "笔记本": {"pinyin": "Bǐjìběn", "english": "Notebook, laptop"},
    "必须": {"pinyin": "bìxū", "english": "must"},
    "变化": {"pinyin": "biànhuà", "english": "To change"},
    "别(qítā)": {"pinyin": "qítā", "english": "other people"},
    "冰箱": {"pinyin": "bīngxiāng", "english": "refrigerator"},
    "不但": {"pinyin": "Bùdàn", "english": "Not only.."},
    "而且": {"pinyin": "érqiě", "english": "But also.."},
    "菜单": {"pinyin": "càidān", "english": "menu"},
    "参加": {"pinyin": "cānjiā", "english": "join, to participate"},
    "草": {"pinyin": "cǎo", "english": "Grass"},
    "层": {"pinyin": "céng", "english": "used for floors"},
    "差": {"pinyin": "chà", "english": "To fall short of"},
    "超市": {"pinyin": "chāoshì", "english": "supermarket"},
    "衬衫": {"pinyin": "chènshān", "english": "shirt"},
    "成绩": {"pinyin": "chéngjī", "english": "Grade, performance, achievement"},
    "城市": {"pinyin": "chéngshì", "english": "city"},
    "迟到": {"pinyin": "chídào", "english": "be late"},
    "除了": {"pinyin": "Chúle", "english": "Other than"},
    "船": {"pinyin": "chuán", "english": "Boat"},
    "春天": {"pinyin": "chūntiān", "english": "spring"},
    "词典": {"pinyin": "Cídiǎn", "english": "dictionary"},
    "聪明": {"pinyin": "cōngmíng", "english": "smart, clever"},
    "打扫": {"pinyin": "dǎsǎo", "english": "To clean, to sweep"},
    "打算": {"pinyin": "dǎsuàn", "english": "To Plan, Intend"},
    "带": {"pinyin": "dài", "english": "To take along, to bring"},
    "担心": {"pinyin": "dānxīn", "english": "Worry"},
    "蛋糕": {"pinyin": "dàngāo", "english": "cake"},
    "当然": {"pinyin": "dāngrán", "english": "certainly, of course"},
    "地": {"pinyin": "de", "english": "connects adv. Mod and verb it mods."},
    "灯": {"pinyin": "dēng", "english": "light, lamp"},
    "地方": {"pinyin": "dìfāng", "english": "place"},
    "地铁": {"pinyin": "dìtiě", "english": "subway"},
    "地图": {"pinyin": "dìtú", "english": "map"},
    "电梯": {"pinyin": "diàntī", "english": "elevator"},
    "电子邮件": {"pinyin": "diànzǐ yóujiàn", "english": "e-mail"},
    "东": {"pinyin": "dōng", "english": "East"},
    "冬天": {"pinyin": "dōngtiān", "english": "winter"},
    "动物": {"pinyin": "dòngwù", "english": "animal"},
    "短": {"pinyin": "duǎn", "english": "short"},
    "段": {"pinyin": "duàn", "english": "used for sections or periods"},
    "锻炼": {"pinyin": "duànliàn", "english": "to do physical exercise"},
    "多么": {"pinyin": "Duōme", "english": "Very, to a great extent"},
    "饿": {"pinyin": "è", "english": "Hungry"},
    "耳朵": {"pinyin": "ěrduǒ", "english": "ear"},
    "发": {"pinyin": "fā", "english": "To send"},
    "发烧": {"pinyin": "Fāshāo", "english": "To have a fever"},
    "发现": {"pinyin": "fāxiàn", "english": "Discover"},
    "方便": {"pinyin": "fāngbiàn", "english": "convenient"},
    "放": {"pinyin": "fàng", "english": "to put, to place"},
    "放心": {"pinyin": "fàngxīn", "english": "To ease one's mind, rest assured"},
    "分": {"pinyin": "fēn", "english": "To distinguish"},
    "附近": {"pinyin": "fùjìn", "english": "nearby, vicinity"},
    "复习": {"pinyin": "fùxí", "english": "review"},
    "干净": {"pinyin": "gānjìng", "english": "Clean"},
    "感冒": {"pinyin": "gǎnmào", "english": "to catch a cold"},
    "感兴趣": {"pinyin": "gǎn xìngqù", "english": "to be interested in"},
    "刚才": {"pinyin": "gāngcái", "english": "Just now"},
    "个子": {"pinyin": "gèzi", "english": "Height, stature"},
    "根据": {"pinyin": "gēnjù", "english": "according to, based on"},
    "跟": {"pinyin": "gēn", "english": "With"},
    "更": {"pinyin": "gèng", "english": "More, even more"},
    "公斤": {"pinyin": "gōngjīn", "english": "Kilogram"},
    "公园": {"pinyin": "gōngyuán", "english": "park"},
    "故事": {"pinyin": "gùshì", "english": "story"},
    "刮风": {"pinyin": "guā fēng", "english": "To be windy"},
    "关": {"pinyin": "guān", "english": "To turn off, to close"},
    "关系": {"pinyin": "guānxì", "english": "Relationship"},
    "关心": {"pinyin": "guānxīn", "english": "To care for, to be interested in"},
    "关于": {"pinyin": "guānyú", "english": "about, regarding"},
    "国家": {"pinyin": "guó jiā", "english": "country, nation"},
    "过": {"pinyin": "guò", "english": "To spend, to pass"},
    "过去": {"pinyin": "guòqù", "english": "past"},
    "还是": {"pinyin": "háishì", "english": "Or, still"},
    "害怕": {"pinyin": "hàipà", "english": "To be afraid, to fear"},
    "航班": {"pinyin": "hángbān", "english": "Flight"},
    "黑板": {"pinyin": "hēibǎn", "english": "blackboard"},
    "后来": {"pinyin": "hòulái", "english": "Later"},
    "护照": {"pinyin": "hùzhào", "english": "passport"},
    "花": {"pinyin": "huā", "english": "to spend"},
    "画": {"pinyin": "huà", "english": "drawing, painting"},
    "坏": {"pinyin": "huài", "english": "Bad, broken"},
    "欢迎": {"pinyin": "huānyíng", "english": "Welcome"},
    "环": {"pinyin": "Huán", "english": "ring"},
    "环境": {"pinyin": "huánjìng", "english": "Environment, surroundings"},
    "换": {"pinyin": "huàn", "english": "To change"},
    "黄河": {"pinyin": "huánghé", "english": "Yellow River"},
    "回答": {"pinyin": "huídá", "english": "To answer"},
    "会议": {"pinyin": "huìyì", "english": "meeting, conference"},
    "或者": {"pinyin": "huòzhě", "english": "Or, either"},
    "几乎": {"pinyin": "jīhū", "english": "Almost"},
    "机会": {"pinyin": "jīhuì", "english": "Opportunity"},
    "极": {"pinyin": "jí", "english": "Extremely, to the highest degree"},
    "记得": {"pinyin": "jìdé", "english": "To remember"},
    "季节": {"pinyin": "jìjié", "english": "Season"},
    "检查": {"pinyin": "jiǎnchá", "english": "To check, to inspect"},
    "简单": {"pinyin": "jiǎndān", "english": "Simple"},
    "见面": {"pinyin": "jiànmiàn", "english": "To meet"},
    "健康": {"pinyin": "jiànkāng", "english": "Health"},
    "讲": {"pinyin": "jiǎng", "english": "To speak, to say"},
    "教": {"pinyin": "jiāo", "english": "To teach"},
    "角": {"pinyin": "jiǎo", "english": "Corner, angle"},
    "脚": {"pinyin": "jiǎo", "english": "Foot"},
    "接": {"pinyin": "jiē", "english": "To catch, to receive"},
    "街道": {"pinyin": "jiēdào", "english": "Street, neighborhood"},
    "节目": {"pinyin": "jiémù", "english": "Show, program"},
    "节日": {"pinyin": "jiérì", "english": "Holiday, festival"},
    "结婚": {"pinyin": "jiéhūn", "english": "To get married"},
    "结束": {"pinyin": "jiéshù", "english": "To end, to finish"},
    "解决": {"pinyin": "jiějué", "english": "To solve, to resolve"},
    "借": {"pinyin": "jiè", "english": "To borrow, to lend"},
    "经常": {"pinyin": "jīngcháng", "english": "Often, regularly"},
    "经过": {"pinyin": "jīngguò", "english": "To pass, to go through"},
    "经理": {"pinyin": "jīnglǐ", "english": "manager"},
    "久": {"pinyin": "jiǔ", "english": "Long time"},
    "旧": {"pinyin": "jiù", "english": "Old, used"},
    "句子": {"pinyin": "jùzi", "english": "Sentence"},
    "决定": {"pinyin": "juédìng", "english": "To decide, decision"},
    "渴": {"pinyin": "kě", "english": "Thirsty"},
    "刻": {"pinyin": "kè", "english": "Quarter (of an hour)"},
    "客人": {"pinyin": "kèrén", "english": "Guest"},
    "空调": {"pinyin": "kòngtiáo", "english": "Air conditioner"},
    "口": {"pinyin": "kǒu", "english": "Mouth"},
    "哭": {"pinyin": "kū", "english": "To cry"},
    "裤子": {"pinyin": "kùzi", "english": "Pants"},
    "筷子": {"pinyin": "kuàizi", "english": "chopsticks"},
    "蓝": {"pinyin": "lán", "english": "Blue"},
    "老": {"pinyin": "lǎo", "english": "Old"},
    "离开": {"pinyin": "líkāi", "english": "To leave, to depart"},
    "礼物": {"pinyin": "lǐwù", "english": "Gift"},
    "历史": {"pinyin": "lìshǐ", "english": "History"},
    "脸": {"pinyin": "liǎn", "english": "Face"},
    "练习": {"pinyin": "liànxí", "english": "To practice"},
    "辆": {"pinyin": "liàng", "english": "Used for vehicles"},
    "聊天": {"pinyin": "liáotiān", "english": "To chat"},
    "了解": {"pinyin": "liǎojiě", "english": "To understand, to know"},
    "邻居": {"pinyin": "línjū", "english": "Neighbor"},
    "楼": {"pinyin": "lóu", "english": "Building, floor"},
    "绿": {"pinyin": "lǜ", "english": "Green"},
    "马": {"pinyin": "mǎ", "english": "Horse"},
    "马上": {"pinyin": "mǎshàng", "english": "Immediately"},
    "满意": {"pinyin": "mǎnyì", "english": "Satisfied"},
    "帽子": {"pinyin": "màozi", "english": "Hat"},
    "米": {"pinyin": "mǐ", "english": "Meter"},
    "面包": {"pinyin": "miànbāo", "english": "Bread"},
    "面条": {"pinyin": "miàntiáo", "english": "Noodles"},
    "明白": {"pinyin": "míngbái", "english": "Clear, obvious"},
    "拿": {"pinyin": "ná", "english": "To hold, to take"},
    "奶奶": {"pinyin": "nǎinai", "english": "Grandmother"},
    "南": {"pinyin": "nán", "english": "South"},
    "难": {"pinyin": "nán", "english": "Difficult"},
    "难过": {"pinyin": "nánguò", "english": "Sad"},
    "年级": {"pinyin": "niánjí", "english": "Grade"},
    "年轻": {"pinyin": "niánqīng", "english": "Young"},
    "鸟": {"pinyin": "niǎo", "english": "Bird"},
    "努力": {"pinyin": "nǔlì", "english": "To strive, to work hard"},
    "爬山": {"pinyin": "páshān", "english": "To climb a mountain"},
    "盘子": {"pinyin": "pánzi", "english": "Plate, dish"},
    "胖": {"pinyin": "pàng", "english": "Fat"},
    "啤酒": {"pinyin": "píjiǔ", "english": "beer"},
    "皮鞋": {"pinyin": "píxié", "english": "Leather shoes"},
    "瓶子": {"pinyin": "píngzi", "english": "Bottle"},
    "其实": {"pinyin": "qíshí", "english": "Actually"},
    "其他": {"pinyin": "qítā", "english": "Other"},
    "骑": {"pinyin": "qí", "english": "To ride"},
    "奇怪": {"pinyin": "qíguài", "english": "Strange"},
    "起飞": {"pinyin": "qǐfēi", "english": "To take off"},
    "起来": {"pinyin": "qǐlái", "english": "To rise, to get up"},
    "清楚": {"pinyin": "qīngchǔ", "english": "Clear"},
    "请假": {"pinyin": "qǐngjià", "english": "To request leave"},
    "秋": {"pinyin": "qiū", "english": "Autumn"},
    "裙子": {"pinyin": "qúnzi", "english": "Skirt"},
    "然后": {"pinyin": "ránhòu", "english": "Then, after that"},
    "热情": {"pinyin": "rèqíng", "english": "Warm, enthusiastic"},
    "认为": {"pinyin": "rènwéi", "english": "To think, to consider"},
    "认真": {"pinyin": "rènzhēn", "english": "Serious, conscientious"},
    "容易": {"pinyin": "róngyì", "english": "Easy"},
    "如果": {"pinyin": "rúguǒ", "english": "If"},
    "伞": {"pinyin": "sǎn", "english": "Umbrella"},
    "上网": {"pinyin": "shàngwǎng", "english": "To go online"},
    "声音": {"pinyin": "shēngyīn", "english": "Sound, voice"},
    "生气": {"pinyin": "shēngqì", "english": "To get angry"},
    "世界": {"pinyin": "shìjiè", "english": "World"},
    "试": {"pinyin": "shì", "english": "To try"},
    "瘦": {"pinyin": "shòu", "english": "Thin, lean"},
    "叔叔": {"pinyin": "shūshu", "english": "Uncle"},
    "舒服": {"pinyin": "shūfú", "english": "Comfortable"},
    "树": {"pinyin": "shù", "english": "Tree"},
    "数学": {"pinyin": "shùxué", "english": "Mathematics"},
    "刷牙": {"pinyin": "shuāyá", "english": "To brush one's teeth"},
    "双": {"pinyin": "shuāng", "english": "Pair"},
    "水平": {"pinyin": "shuǐpíng", "english": "Level, standard"},
    "司机": {"pinyin": "sījī", "english": "Driver"},
    "太阳": {"pinyin": "tàiyáng", "english": "Sun"},
    "特别": {"pinyin": "tèbié", "english": "Special"},
    "疼": {"pinyin": "téng", "english": "Painful"},
    "提高": {"pinyin": "tígāo", "english": "To improve"},
    "体育": {"pinyin": "tǐyù", "english": "Physical education"},
    "甜": {"pinyin": "tián", "english": "Sweet"},
    "条": {"pinyin": "tiáo", "english": "Used for thin objects"},
    "同事": {"pinyin": "tóngshì", "english": "Colleague"},
    "同意": {"pinyin": "tóngyì", "english": "To agree"},
    "头发": {"pinyin": "tóufǎ", "english": "Hair"},
    "突然": {"pinyin": "túrán", "english": "Suddenly"},
    "图书馆": {"pinyin": "túshū guǎn", "english": "Library"},
    "腿": {"pinyin": "tuǐ", "english": "Leg"},
    "完成": {"pinyin": "wánchéng", "english": "To complete"},
    "碗": {"pinyin": "wǎn", "english": "Bowl"},
    "万": {"pinyin": "wàn", "english": "Ten thousand"},
    "忘记": {"pinyin": "wàngjì", "english": "To forget"},
    "为": {"pinyin": "wèi", "english": "For"},
    "为了": {"pinyin": "Wèile", "english": "In order to"},
    "位": {"pinyin": "wèi", "english": "Used for people"},
    "文化": {"pinyin": "wénhuà", "english": "Culture"},
    "西": {"pinyin": "xī", "english": "West"},
    "习惯": {"pinyin": "xíguàn", "english": "Habit"},
    "洗手间": {"pinyin": "xǐshǒujiān", "english": "Toilet"},
    "洗澡": {"pinyin": "xǐzǎo", "english": "To bathe"},
    "夏": {"pinyin": "xià", "english": "Summer"},
    "先": {"pinyin": "xiān", "english": "First"},
    "相信": {"pinyin": "xiāngxìn", "english": "To believe"},
    "香蕉": {"pinyin": "xiāngjiāo", "english": "Banana"},
    "向": {"pinyin": "xiàng", "english": "Towards"},
    "像": {"pinyin": "xiàng", "english": "To be like"},
    "小心": {"pinyin": "xiǎoxīn", "english": "To be careful"},
    "校长": {"pinyin": "xiàozhǎng", "english": "Principal"},
    "新鲜": {"pinyin": "xīnxiān", "english": "Fresh"},
    "信用卡": {"pinyin": "xìnyòngkǎ", "english": "Credit card"},
    "行李箱": {"pinyin": "xínglǐ xiāng", "english": "Suitcase"},
    "熊猫": {"pinyin": "xióngmāo", "english": "Panda"},
    "需要": {"pinyin": "xūyào", "english": "To need"},
    "选择": {"pinyin": "xuǎnzé", "english": "To choose"},
    "要求": {"pinyin": "yāoqiú", "english": "To require"},
    "爷爷": {"pinyin": "yéyé", "english": "Grandfather"},
    "一直": {"pinyin": "yīzhí", "english": "All the time"},
    "一般": {"pinyin": "yībān", "english": "Generally"},
    "一样": {"pinyin": "yīyàng", "english": "The same"},
    "以前": {"pinyin": "yǐqián", "english": "Before"},
    "以为": {"pinyin": "yǐwéi", "english": "To think"},
    "应该": {"pinyin": "yīnggāi", "english": "Should"},
    "音乐": {"pinyin": "yīnyuè", "english": "Music"},
    "银行": {"pinyin": "yínháng", "english": "Bank"},
    "饮料": {"pinyin": "yǐnliào", "english": "Drink"},
    "影响": {"pinyin": "yǐngxiǎng", "english": "Influence"},
    "用": {"pinyin": "yòng", "english": "To use"},
    "游戏": {"pinyin": "yóuxì", "english": "Game"},
    "有名": {"pinyin": "yǒumíng", "english": "Famous"},
    "遇到": {"pinyin": "yù dào", "english": "To come across"},
    "月亮": {"pinyin": "yuèliàng", "english": "Moon"},
    "越": {"pinyin": "yuè", "english": "The more"},
    "站": {"pinyin": "zhàn", "english": "To stand"},
    "张": {"pinyin": "zhāng", "english": "Used for flat objects"},
    "长": {"pinyin": "zhǎng", "english": "To grow"},
    "着急": {"pinyin": "zhāojí", "english": "Worried"},
    "照顾": {"pinyin": "zhàogù", "english": "To look after"},
    "照片": {"pinyin": "zhàopiàn", "english": "Photograph"},
    "照相机": {"pinyin": "zhàoxiàngjī", "english": "Camera"},
    "只": {"pinyin": "zhǐ", "english": "Only"},
    "只有": {"pinyin": "Zhǐyǒu", "english": "Only if"},
    "中间": {"pinyin": "zhōngjiān", "english": "middle"},
    "中文": {"pinyin": "zhōngwén", "english": "Chinese"},
    "终于": {"pinyin": "zhōngyú", "english": "Finally"},
    "种": {"pinyin": "zhǒng", "english": "Type"},
    "重要": {"pinyin": "zhòngyào", "english": "Important"},
    "周末": {"pinyin": "zhōumò", "english": "Weekend"},
    "主要": {"pinyin": "zhǔyào", "english": "main"},
    "注意": {"pinyin": "zhùyì", "english": "to pay attention to"},
    "自己": {"pinyin": "zìjǐ", "english": "self"},
    "自行车": {"pinyin": "zìxíngchē", "english": "bicycle"},
    "总是": {"pinyin": "zǒng shì", "english": "always"},
    "嘴": {"pinyin": "zuǐ", "english": "Mouth"},
    "最后": {"pinyin": "zuìhòu", "english": "the last one"},
    "最近": {"pinyin": "zuìjìn", "english": "lately, recently"},
    "作业": {"pinyin": "zuòyè", "english": "Homework"},
    "词语": {"pinyin": "cíyǔ", "english": "word, expression"},
    "各": {"pinyin": "gè", "english": "each"},
    "举行": {"pinyin": "jǔxíng", "english": "hold"},
    "可乐": {"pinyin": "kělè", "english": "Cola"},
    "秘书": {"pinyin": "mìshū", "english": "secretary"},
    "情况": {"pinyin": "qíngkuàng", "english": "Condition"},
    "生活": {"pinyin": "shēnghuó", "english": "Life"},
    "睡着": {"pinyin": "shuìzhe", "english": "to fall asleep"},
    "太太": {"pinyin": "tàitài", "english": "Mrs., wife"},
    "特点": {"pinyin": "tèdiǎn", "english": "Features"},
    "眼镜": {"pinyin": "Yǎnjìng", "english": "Eye Glasses"},
    "真正": {"pinyin": "zhēnzhèng", "english": "really, truly"},
    "中介": {"pinyin": "zhōngjiè", "english": "intermediary"},
    "办事": {"pinyin": "bànshì", "english": "work"},
    "便": {"pinyin": "biàn", "english": "To change, to become"},
    "春节": {"pinyin": "chūnjié", "english": "Spring Festival"},
    "打": {"pinyin": "dǎ", "english": "to send, to remit"},
    "到时候": {"pinyin": "dào shíhòu", "english": "By the time"},
    "房子": {"pinyin": "fángzi", "english": "house"},
    "刚": {"pinyin": "gāng", "english": "Just, only a short while ago"},
    "贵": {"pinyin": "guì", "english": "(honorific term) your"},
    "歌舞": {"pinyin": "gēwǔ", "english": "Song and dance"},
    "红酒": {"pinyin": "hóngjiǔ", "english": "red wine"},
    "句": {"pinyin": "jù", "english": "measure word for sentences"},
    "开": {"pinyin": "kāi", "english": "open"},
    "每天": {"pinyin": "měitiān", "english": "every day"},
    "哪里": {"pinyin": "nǎlǐ", "english": "where"},
    "女孩儿": {"pinyin": "nǚhái ér", "english": "girl"},
    "钱包": {"pinyin": "qiánbāo", "english": "wallet"},
    "人名": {"pinyin": "rénmíng", "english": "name"},
    "认": {"pinyin": "rèn", "english": "recognize"},
    "上网": {"pinyin": "shàngwǎng", "english": "Internet access"},
    "听说": {"pinyin": "tīng shuō", "english": "to hear about"},
    "外地": {"pinyin": "wàidì", "english": "other places"},
    "鲜花": {"pinyin": "xiānhuā", "english": "fresh flowers"},
    "香瓜": {"pinyin": "xiāngguā", "english": "cantaloupe"},
    "一般来说": {"pinyin": "yībān lái shuō", "english": "Generally speaking"},
    "以后": {"pinyin": "yǐhòu", "english": "after"},
    "音乐会": {"pinyin": "yīnyuè huì", "english": "concert"},
    "有点儿": {"pinyin": "yǒudiǎn er", "english": "A little bit"},
    "早": {"pinyin": "zǎo", "english": "Early morning"},
    "怎么办": {"pinyin": "zěnme bàn", "english": "what to do"},
    "照": {"pinyin": "zhào", "english": "To photograph"},
    "中秋节": {"pinyin": "zhōngqiū jié", "english": "Mid-Autumn Festival"},
}

hsk_bank4 = {
    "本": {"pinyin": "běn", "english": "origin, source"},
    "不客气": {"pinyin": "bù kèqi", "english": "you're welcome"},
    "菜": {"pinyin": "cài", "english": "dish, cuisine"}
}

hsk_bank5 = {
    "茶": {"pinyin": "chá", "english": "tea"},
    "吃": {"pinyin": "chī", "english": "to eat"},
    "出": {"pinyin": "chū", "english": "to go out"}
}

hsk_bank6 = {
    "穿": {"pinyin": "chuān", "english": "to wear, to put on"},
    "次": {"pinyin": "cì", "english": "time, occurrence"},
    "从": {"pinyin": "cóng", "english": "from, since"}
}

vocab_bank = {
    "名词": {"pinyin": "Míngcí", "english": "Noun"},
    "动词": {"pinyin": "Dòngcí", "english": "Verb"},
    "形容词": {"pinyin": "Xíngróngcí", "english": "Adjective"},
}

# List to store wrong answers
wrong_answers = []
correctly_answered = set()

# Initialize GUI
root = tk.Tk()
root.title("Mikes HSK Flashcard Game!")

bank = hsk_bank1  # Default to hsk_bank1

# Global variables
current_question = ""
asked_questions = []
correct_answers = 0
incorrect_answers = 0
is_reviewing = False

# Function to start the game with selected bank and settings
def start_game(selected_bank):
    global bank, current_question, asked_questions, correct_answers, incorrect_answers, is_reviewing, wrong_answers, correctly_answered
    bank = selected_bank
    current_question = ""
    asked_questions = []
    correct_answers = 0
    incorrect_answers = 0
    is_reviewing = False
    wrong_answers = []
    correctly_answered = set()
    
    start_frame.pack_forget()
    show_settings_frame()

def show_settings_frame():
    settings_frame.pack(pady=20)
    
# Function to set the review mode
def set_review_mode():
    global bank
    review_mode = review_mode_var.get()
    if review_mode == "Whole Bank":
        start_review()
    else:
        try:
            num_words = int(num_words_entry.get())
            if num_words > len(bank):
                num_words = len(bank)
            # Select a random sample of words
            sample_keys = random.sample(list(bank.keys()), num_words)
            bank = {key: bank[key] for key in sample_keys}
            start_review()
        except ValueError:
            error_label.config(text="Please enter a valid number.")

def start_review():
    settings_frame.pack_forget()
    question_frame.pack(pady=20)
    answer_frame.pack(pady=20)
    score_label.pack(pady=20)
    for btn in answer_buttons:
        btn.config(state=tk.NORMAL)  # Re-enable answer buttons
    generate_question()

# Function to generate a new question
def generate_question():
    try:
        global current_question, asked_questions, is_reviewing, wrong_answers

        print("Generating new question...")
        print(f"Currently reviewing: {is_reviewing}, Wrong answers left: {wrong_answers}")

        if is_reviewing and not wrong_answers:
            print("Review completed, no more wrong answers.")
            is_reviewing = False
            asked_questions = []

        if not is_reviewing and len(correctly_answered) >= len(bank):
            question_label.config(text="You've answered all questions correctly! Game over.")
            for btn in answer_buttons:
                btn.config(state=tk.DISABLED)
            show_end_buttons()
            print("Game over.")
            return

        if is_reviewing and wrong_answers:
            current_question = random.choice(wrong_answers)
            print(f"Reviewing question: {current_question}")
        else:
            current_question = random.choice(list(bank.keys()))
            while current_question in asked_questions or current_question in correctly_answered:
                current_question = random.choice(list(bank.keys()))
            asked_questions.append(current_question)
            print(f"New question: {current_question}")

        question_type = random.choice(["english", "pinyin"])
        if question_type == "english":
            question = f"What does this mean?\n{current_question} ({bank[current_question]['pinyin']})"
            correct_answer = bank[current_question]["english"]
        else:
            question = f"What is the pinyin for this?\n{current_question}"
            correct_answer = bank[current_question]["pinyin"]

        wrong_choices = random.sample([bank[key][question_type] for key in bank if key != current_question], 2)
        choices = wrong_choices + [correct_answer]
        random.shuffle(choices)

        question_label.config(text=question)
        for i, choice in enumerate(choices):
            answer_buttons[i].config(text=choice, command=lambda c=choice: check_answer(c, correct_answer))

        score_label.config(text=f"Correct: {correct_answers}   Incorrect: {incorrect_answers}")
    except Exception as e:
        print("An error occurred in generate_question:")
        traceback.print_exc()

# Function to check the answer
def check_answer(selected, correct):
    try:
        global correct_answers, incorrect_answers, wrong_answers, correctly_answered, is_reviewing
        if selected == correct:
            correct_answers += 1
            correctly_answered.add(current_question)
            if current_question in wrong_answers:
                wrong_answers.remove(current_question)
                incorrect_answers -= 1
            print(f"Correct answer! Total correct: {correct_answers}")
        else:
            incorrect_answers += 1
            if current_question not in wrong_answers:
                wrong_answers.append(current_question)
            print(f"Wrong answer! Total incorrect: {incorrect_answers}")

        if incorrect_answers > 0 and not is_reviewing:
            is_reviewing = True

        generate_question()
    except Exception as e:
        print("An error occurred in check_answer:")
        traceback.print_exc()

# Function to restart the game
def restart_game():
    global current_question, asked_questions, correct_answers, incorrect_answers, is_reviewing, wrong_answers, correctly_answered
    current_question = ""
    asked_questions = []
    correct_answers = 0
    incorrect_answers = 0
    is_reviewing = False
    wrong_answers = []
    correctly_answered = set()

    for btn in answer_buttons:
        btn.config(state=tk.NORMAL)
    end_frame.pack_forget()
    question_frame.pack(pady=20)
    answer_frame.pack(pady=20)
    score_label.pack(pady=20)
    generate_question()

# Function to exit the game
def exit_game():
    root.destroy()

# Function to return to main menu
def return_to_main_menu():
    question_frame.pack_forget()
    answer_frame.pack_forget()
    score_label.pack_forget()
    end_frame.pack_forget()
    start_frame.pack(pady=20)

# Function to show end buttons
def show_end_buttons():
    end_frame.pack(pady=20)

# Add a frame for the starting menu
start_frame = tk.Frame(root)
start_frame.pack(pady=20)

tk.Label(start_frame, text="Choose the bank to review:", font=("Helvetica", 20)).pack(pady=10)

hsk1_button = tk.Button(start_frame, text="HSK1 Bank", font=("Helvetica", 16), command=lambda: start_game(hsk_bank1))
hsk1_button.pack(pady=5)

hsk2_button = tk.Button(start_frame, text="HSK2 Bank", font=("Helvetica", 16), command=lambda: start_game(hsk_bank2))
hsk2_button.pack(pady=5)

hsk3_button = tk.Button(start_frame, text="HSK3 Bank", font=("Helvetica", 16), command=lambda: start_game(hsk_bank3))
hsk3_button.pack(pady=5)

hsk4_button = tk.Button(start_frame, text="HSK4 Bank", font=("Helvetica", 16), command=lambda: start_game(hsk_bank4))
hsk4_button.pack(pady=5)

hsk5_button = tk.Button(start_frame, text="HSK5 Bank", font=("Helvetica", 16), command=lambda: start_game(hsk_bank5))
hsk5_button.pack(pady=5)

hsk6_button = tk.Button(start_frame, text="HSK6 Bank", font=("Helvetica", 16), command=lambda: start_game(hsk_bank6))
hsk6_button.pack(pady=5)
# Add more buttons for other banks as needed...

settings_frame = tk.Frame(root)

review_mode_var = tk.StringVar(value="Whole Bank")
tk.Label(settings_frame, text="Review Mode:", font=("Helvetica", 16)).pack()
tk.Radiobutton(settings_frame, text="Whole Bank", variable=review_mode_var, value="Whole Bank", font=("Helvetica", 14)).pack()
tk.Radiobutton(settings_frame, text="Number of Characters", variable=review_mode_var, value="Number of Characters", font=("Helvetica", 14)).pack()

num_words_label = tk.Label(settings_frame, text="Enter number of characters:", font=("Helvetica", 14))
num_words_label.pack()
num_words_entry = tk.Entry(settings_frame, font=("Helvetica", 14))
num_words_entry.pack()

error_label = tk.Label(settings_frame, text="", font=("Helvetica", 12), fg="red")
error_label.pack()

tk.Button(settings_frame, text="Start Review", font=("Helvetica", 16), command=set_review_mode).pack(pady=10)

question_frame = tk.Frame(root)
question_label = tk.Label(question_frame, text="", font=("Helvetica", 26))
question_label.pack()

answer_frame = tk.Frame(root)
answer_buttons = [
    tk.Button(answer_frame, text="", font=("Helvetica", 16), width=50),
    tk.Button(answer_frame, text="", font=("Helvetica", 16), width=50),
    tk.Button(answer_frame, text="", font=("Helvetica", 16), width=50),
]

for btn in answer_buttons:
    btn.pack(side=tk.BOTTOM, padx=10)

score_label = tk.Label(root, text="Correct: 0   Incorrect: 0", font=("Helvetica", 16))

end_frame = tk.Frame(root)
restart_button = tk.Button(end_frame, text="Restart", font=("Helvetica", 16), command=restart_game)
exit_button = tk.Button(end_frame, text="Exit", font=("Helvetica", 16), command=exit_game)
main_menu_button = tk.Button(end_frame, text="Main Menu", font=("Helvetica", 16), command=return_to_main_menu)
restart_button.pack(side=tk.LEFT, padx=10)
exit_button.pack(side=tk.LEFT, padx=10)
main_menu_button.pack(side=tk.LEFT, padx=10)

root.mainloop()