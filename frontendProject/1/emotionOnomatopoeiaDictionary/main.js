class Word{
    constructor(word, defintion, pictureUrl){
        this.word = word;
        this.defintion = defintion;
        this.pictureUrl = pictureUrl;
    }
}

class EmotionObject{
    constructor(emotion, description, color, onomatopoeia){
        this.emotion = emotion;
        this.description = description;
        this.color = color;
        this.onomatopoeia = onomatopoeia; // List of strings
    }

    getOnomatopoeiaWords(){
        return this.onomatopoeia;
    }

    getHtmlContainerString(){
        return this.description;
    }
}

const dictionary = {
    "bark":"the sound made by a dog",
    "grunt":"issue a low, animal-like noise",
    "roar":"make a loud noise, as of an animal",
    "whack":"the act of hitting vigorously",
    "smack":"a blow from a flat object (as an open hand)",
    "hiss":`make a sharp, elongated "s" sound`,
    "ahem":"the utterance of a sound similar to clearing the throat",
    "bawl":"cry loudly",
    "bling":"flashy, ostentatious jewelry",
    "boom":"a deep prolonged loud noise",
    "buzz":"the sound of rapid vibration",
    "caw":"utter a cry, characteristic of crows, rooks, or ravens",
    "chatter":"talk socially without exchanging too much information",
    "chant":"a repetitive song in which syllables are assigned to a tone",
    "clatter":"a continuous rattling sound as of hard objects falling or striking each other.",
    "clunk":"a heavy dull sound (as made by impact of heavy objects)",
    "crawl":"move forward on the hands and knees or by dragging the body close to the ground.",
    "flick":"throw or toss with a quick motion",
    "giggle":"a light, silly laugh.",
    "gargle":"an act or instance or the sound of washing one's mouth and throat with a liquid kept in motion by exhaling through it.",
    "honk":"the cry of a goose or any loud sound resembling it",
    "oink":"the short low gruff noise of the kind made by hogs",
    "whine":"a complaint uttered in a plaintive way",
    "waah":"sound made when crying by babies",
    "zing":"sound my by something energetic"
};

const pictureDictionary = {
    "bark":"https://cdn.pixabay.com/photo/2013/07/25/11/59/german-shepherd-166972_1280.jpg",
    "grunt":"https://cdn.pixabay.com/photo/2010/11/29/nepal-419__480.jpg",
    "roar":"https://cdn.pixabay.com/photo/2018/04/13/21/24/lion-3317670_1280.jpg",
    "whack":"https://cdn.pixabay.com/photo/2017/10/27/11/49/boxer-2894025_1280.jpg",
    "smack":"https://cdn.pixabay.com/photo/2015/03/20/19/38/hammer-682767_1280.jpg",
    "hiss":"https://cdn.pixabay.com/photo/2016/10/13/23/30/cat-1739091_1280.jpg",
    "ahem":"https://cdn.pixabay.com/photo/2014/03/13/10/12/man-286476_1280.jpg",
    "bawl":"https://cdn.pixabay.com/photo/2015/06/26/10/17/smiley-822365_960_720.jpg",
    "bling":"https://cdn.pixabay.com/photo/2017/12/30/13/37/happy-new-year-3050088_1280.jpg",
    "boom":"https://cdn.pixabay.com/photo/2016/04/12/21/17/explosion-1325471_1280.jpg",
    "buzz":"https://cdn.pixabay.com/photo/2020/02/13/10/29/bees-4845211_1280.jpg",
    "caw":"https://cdn.pixabay.com/photo/2017/02/16/11/13/bird-2071185_1280.jpg",
    "chatter":"https://cdn.pixabay.com/photo/2014/07/25/08/55/bar-401546_1280.jpg",
    "chant":"https://cdn.pixabay.com/photo/2016/07/19/07/43/parchment-1527650__340.jpg",
    "clatter":"https://cdn.pixabay.com/photo/2020/02/06/19/01/clutter-4825256_1280.jpg",
    "clunk":"https://cdn.pixabay.com/photo/2017/01/10/03/06/steel-1968194_1280.jpg",
    "crawl":"https://cdn.pixabay.com/photo/2017/11/23/07/47/baby-2972221__340.jpg",
    "flick":"https://cdn.pixabay.com/photo/2012/02/23/08/48/disgust-15793_1280.jpg",
    "giggle":"https://cdn.pixabay.com/photo/2017/08/07/15/18/people-2604850_1280.jpg",
    "gargle":"https://cdn.pixabay.com/photo/2017/04/03/16/32/girl-smoke-cigarette-2198839_1280.jpg",
    "honk":"https://cdn.pixabay.com/photo/2017/02/28/14/37/geese-2105918_1280.jpg",
    "oink":"https://cdn.pixabay.com/photo/2019/03/02/15/32/pig-4030013_1280.jpg",
    "whine":"https://cdn.pixabay.com/photo/2020/05/01/01/57/girl-5115192_960_720.jpg",
    "waah":"https://cdn.pixabay.com/photo/2017/01/18/02/18/emotions-1988745_1280.jpg",
    "zing":"https://cdn.pixabay.com/photo/2017/09/14/16/38/fiber-optic-2749588_1280.jpg"
};

const emotions = [
    new EmotionObject("fearful", "feeling afraid; showing fear or anxiety.", "green", ["buzz","caw","crawl"]),
    
    new EmotionObject("happy", "feeling or showing pleasure or contentment.", "yellow", ["bling","chatter","chant","giggle"]),
    
    new EmotionObject("bad", "not such as to be hoped for or desired; unpleasant or unwelcome.", "beige", ["ahem","clatter","clunk"]),
    new EmotionObject("angry", "feeling or showing strong annoyance, displeasure, or hostility; full of anger.", "red", ["bark","grunt", "roar","whack","smack","hiss"]),
    new EmotionObject("sad", "feeling or showing sorrow; unhappy.", "grey", ["bawl","whine","waah"]),
    new EmotionObject("disgusted", "feeling or showing strong annoyance, displeasure, or hostility; full of anger.", "orange", ["flick","gargle","oink"]),
    new EmotionObject("surprised", "to feel mild astonishment or shock.", "purple", ["boom","honk","zing"])
];

const emojiClassDict = {
    "happy": "fa-laugh-beam",
    "angry": "fa-angry",
    "bad": "fa-dizzy",
    "sad": "fa-sad-tear",
    "surprised": "fa-surprise",
    "fearful": "fa-tired",
    "disgusted": "fa-grimace"
};

function addClassToEmotionDiv(emojiDiv, emotion) {
    emojiDiv.classList.add("far");
    emojiDiv.classList.add(emojiClassDict[emotion]);
    emojiDiv.classList.add("fa-5x");
    emojiDiv.classList.add("emoji");
};

function createEmotionCard(emotionObject) {
    const emotionCardDiv = document.createElement("div");
    emotionCardDiv.id = "emotionCardDiv"
    const anker = document.createElement("a");

    const emojiNameDiv = document.createElement("div");
    const emojiName = document.createElement("h3");
    const emojiDiv = document.createElement("div");
    const emoji = document.createElement("i");
    const meaningDiv = document.createElement("div");
    const meaning = document.createElement("p");

    anker.href = `#${emotionObject.emotion}`;
    emotionCardDiv.append(anker);

    emojiName.innerHTML = emotionObject.emotion;
    emojiName.classList.add("emotion-text");
    emojiNameDiv.append(emojiName);

    addClassToEmotionDiv(emoji, emotionObject.emotion);
    emojiDiv.classList.add("pt-3");
    emojiDiv.append(emoji);

    meaning.innerHTML = emotionObject.description;
    meaning.classList.add("emotion-text");
    meaningDiv.append(meaning);
    meaningDiv.classList.add("d-flex");
    meaningDiv.classList.add("align-items-center");
    meaningDiv.classList.add("h100");

    emotionCardDiv.append(emojiNameDiv);
    emotionCardDiv.append(emojiDiv);
    emotionCardDiv.append(meaningDiv);
    emotionCardDiv.classList.add("d-flex");
    emotionCardDiv.classList.add("flex-column");
    emotionCardDiv.classList.add("align-items-center");
    emotionCardDiv.classList.add("myCard");
    emotionCardDiv.classList.add("pt-4");
    emotionCardDiv.classList.add("mx-sm-1");
    emotionCardDiv.classList.add("my-3");
    const color = emotionObject.emotion + "-color";
    emotionCardDiv.classList.add(color);

    emotionCardDiv.classList.add("col-xs-12");
    emotionCardDiv.classList.add("col-sm-12");
    emotionCardDiv.classList.add("col-md-8");
    emotionCardDiv.classList.add("col-lg-3");
    return emotionCardDiv;
};

function createWordCard(word) {
    const cardDiv = document.createElement("div");
    cardDiv.classList.add("d-flex", "flex-frow");
    cardDiv.classList.add("bg-light");

    const leftContent = document.createElement("div");
    const rightContent = document.createElement("div");
    rightContent.classList.add("d-flex");
    rightContent.classList.add("align-items-center");
    rightContent.classList.add("pl-0");
    rightContent.classList.add("pr-2");
    const name = document.createElement("h3");
    const meaning =  document.createElement("p");
    const image = document.createElement("img");

    name.innerHTML = word;
    meaning.innerHTML = dictionary[word];
    leftContent.append(name);
    leftContent.append(meaning);

    image.src = pictureDictionary[word];
    image.classList.add("w100");
    image.classList.add("p-0");
    rightContent.append(image)

    leftContent.classList.add("col-8");
    leftContent.classList.add("py-3");
    leftContent.classList.add("m-0")
    leftContent.classList.add("pr-0");

    rightContent.classList.add("col-4");

    cardDiv.append(leftContent);
    cardDiv.append(rightContent);
    cardDiv.classList.add("col-12");
    cardDiv.classList.add("col-md-5");
    cardDiv.classList.add("col-5");
    cardDiv.classList.add("m-3");
    cardDiv.classList.add("p-0");
    return cardDiv;


};

function createWordCardContainer(emotionObject) {
    const wordCardContainerDiv = document.createElement("div");
    const color = emotionObject.emotion + "-color";
    wordCardContainerDiv.classList.add(color);
    wordCardContainerDiv.classList.add("w100");

    const wordCardWrapperDiv = document.createElement("div");
    wordCardWrapperDiv.classList.add("container");
    wordCardWrapperDiv.classList.add("p-4");
    wordCardWrapperDiv.classList.add("d-flex");
    wordCardWrapperDiv.classList.add("flex-column");
    wordCardWrapperDiv.classList.add("align-items-center");

    const emotionNameDiv = document.createElement("div");
    emotionNameDiv.classList.add("w100");
    emotionNameDiv.classList.add("d-flex");
    emotionNameDiv.classList.add("justify-content-start");
    emotionNameDiv.classList.add("px-4");
    const emotionName = document.createElement("h2");
    const meaningDiv = document.createElement("div");
    const meaning = document.createElement("p");

    emotionName.innerHTML = emotionObject.emotion;
    emotionName.classList.add("white-text");
    emotionNameDiv.append(emotionName);

    meaning.innerHTML = emotionObject.description;
    meaning.classList.add("white-text");
    meaningDiv.classList.add("w100");
    meaningDiv.classList.add("d-flex");
    meaningDiv.classList.add("justify-content-start");
    meaningDiv.classList.add("px-4");
    meaningDiv.append(meaning);

    const cardsDiv = document.createElement("div");
    emotionObject.onomatopoeia.map(word => cardsDiv.append(createWordCard(word)));
    cardsDiv.classList.add("d-flex");
    cardsDiv.classList.add("flex-wrap");
    cardsDiv.classList.add("justify-content-between");


    wordCardWrapperDiv.append(emotionNameDiv);
    wordCardWrapperDiv.append(meaningDiv);
    wordCardWrapperDiv.append(cardsDiv);

    wordCardContainerDiv.append(wordCardWrapperDiv);
    wordCardWrapperDiv.id = emotionObject.emotion;
    return wordCardContainerDiv;
}

const outer = document.getElementById("target")

const upperSectionDiv = document.createElement("div");
upperSectionDiv.classList.add("container");
upperSectionDiv.classList.add("d-flex");
upperSectionDiv.classList.add("flex-column");
upperSectionDiv.classList.add("align-items-center");

const emotionCardSectionDiv = document.createElement("div");
emotionCardSectionDiv.classList.add("col-11");
emotionCardSectionDiv.classList.add("d-flex");
emotionCardSectionDiv.classList.add("justify-content-around");
emotionCardSectionDiv.classList.add("flex-wrap");


const lowerSectionDiv = document.createElement("div");
lowerSectionDiv.classList.add("vw100");


const wordsSectionDiv = document.createElement("div");
wordsSectionDiv.classList.add("d-flex");
wordsSectionDiv.classList.add("flex-wrap");
wordsSectionDiv.classList.add("justify-content-around");
wordsSectionDiv.classList.add("wv100");
wordsSectionDiv.classList.add("mx-0")

emotions.map(emotionObj => {
    emotionCardSectionDiv.append(createEmotionCard(emotionObj));
    wordsSectionDiv.append(createWordCardContainer(emotionObj));
    }
);

upperSectionDiv.append(emotionCardSectionDiv);
lowerSectionDiv.append(wordsSectionDiv);

outer.append(upperSectionDiv);
outer.append(lowerSectionDiv)