
class Wallpaper{
    constructor(text,colorCode,wallpaperUrl,verticalLocation,horizontalLocation){
        this.text = text;
        this.colorCode = colorCode;
        this.wallpaperUrl = wallpaperUrl;
        this.verticalLocation = verticalLocation;
        this.horizontalLocation = horizontalLocation;
    }

    changeVerticalLocation(){
        if (this.verticalLocation === "top" ){
            return "align-items-start";
        }
        else if (this.verticalLocation === "center"){
            return "align-items-center";
        }
        else if (this.verticalLocation === "bottom"){
            return "align-items-end";
        }
    }

    changeHorizontalLocation(){
        if (this.horizontalLocation === "left" ){
            return "justify-content-start";
        }
        else if (this.horizontalLocation === "center"){
            return "justify-content-center";
        }
        else if (this.horizontalLocation === "right"){
            return "justify-content-end";
        }
    }
}

function motivationalSpeechWallpaper(object,domObj){
    
    //(2)画像と文字を入れる箱を生成
    let containerDiv = document.createElement("div");
    containerDiv.classList.add("container","d-flex","justify-content-center","py-4");
    //(3)画像を入れる箱を生成
    let imgDiv = document.createElement("div");
    imgDiv.classList.add("box","vh-75","d-flex","col-12","col-md-8",object.changeVerticalLocation(),object.changeHorizontalLocation());
   
    imgDiv.style = "background-image: url(" + object.wallpaperUrl + ")";
    //(4)文字を入れる箱を生成
    let textDiv = document.createElement("div");
    textDiv.classList.add("col-8");

    let textH3 = document.createElement("h3");
    textH3.innerHTML = object.text;
    textH3.style.color = object.colorCode;
    textH3.classList.add("textStyle","text-light");

    textDiv.append(textH3);
    imgDiv.append(textDiv);
    containerDiv.append(imgDiv);
    
    domObj.append(containerDiv);

    return domObj;
}


object1 = new Wallpaper("Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. - Antoine de Saint", "2c3e50", "https://cdn.pixabay.com/photo/2020/06/12/03/06/magnifying-glass-5288877__340.jpg", "center", "center");

object2 = new Wallpaper("The scientist discovers a new type of material or energy and the engineer discovers a new use for it. - Gordon Lindsay Glegg", "2c3e50", "https://cdn.pixabay.com/photo/2018/02/23/04/38/laptop-3174729_1280.jpg", "bottom", "left");

object3 = new Wallpaper("Scientists study the world as it is, engineers create the world that never has been. - Theodore von Karman", "ecf0f1", "https://cdn.pixabay.com/photo/2017/05/10/19/29/robot-2301646_1280.jpg", "top", "right");


let targetDiv = document.getElementById("target")
motivationalSpeechWallpaper(object1,targetDiv);
motivationalSpeechWallpaper(object2,targetDiv);
motivationalSpeechWallpaper(object3,targetDiv);

console.log(targetDiv);