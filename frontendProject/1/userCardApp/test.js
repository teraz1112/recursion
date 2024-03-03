function fruitImgUrl(fruit){
    fruit = fruit.toLowerCase();

    // === はデータ型もcheckする演算子
    if(fruit === "banana") return "https://www.kroger.com/product/images/xlarge/front/0000000004011";
    else if(fruit === "pineapple") return "https://www.kroger.com/product/images/medium/front/0000000004430";
    else if(fruit === "pear") return "https://www.producemarketguide.com/media/user_RZKVrm5KkV/22481/forelle-pears_variety-page.png";

    // デフォルト
    else return "https://upload.wikimedia.org/wikipedia/commons/2/2f/Culinary_fruits_front_view.jpg";
}

let fruitP = document.createElement("p");
fruitP.innerHTML = "Our fruit is banana";

// imgタグを作成します。
let fruitImg = document.createElement("img");
// createElementメソッドで要素を作成した後は、src、height、width、title、alt属性等を設定することができます。
fruitImg.src = fruitImgUrl("banana");

// フルーツの画像にスタイリングをつけます。classListはクラスのリストを表すオブジェクトで様々なメソッドを保持しています。
// fruitImgにfruitImgというクラスを追加します。
fruitImg.classList.add("fruitImg");

// 作成したものをdivに入れます。
let fruitDiv = document.createElement("div");

// divにfruitDivというクラスを追加します。
fruitDiv.classList.add("fruitDiv");
fruitDiv.append(fruitP);
fruitDiv.append(fruitImg);

// 入れたい要素の中に追加します。
document.getElementById("fruit-container").append(fruitDiv);