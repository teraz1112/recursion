class Employee {
    constructor(firstName,lastName,job,skills,country,avatarUrl){
        this.firstName=firstName;
        this.lastName=lastName;
        this.job=job;
        this.skills=skills;
        this.country=country;
        this.avatarUrl=avatarUrl;
    }

    getFullName(){
        return this.firstName + " " + this.lastName;
    }

}

function createEmployeeCard(employeeObject){
    let innerFlex= document.createElement("div");
    innerFlex.classList.add("d-flex", "align-items-center", "col-md-7", "col-10", "m-1");

    let innerProfileCard = document.createElement("div");
    innerFlex.append(innerProfileCard);
    innerProfileCard.classList.add("d-flex", "col-12", "profile-card");

    let leftInfo = document.createElement("div");
    leftInfo.classList.add("col-8", "py-3");

    let div1 = document.createElement("div");
    div1.classList.add("py-2");

    let div2= div1.cloneNode(True);
    let div3= div1.cloneNode(True);

    let nameTitle = document.createElement("h4");
    nameTitle.innerHTML = employeeObject.getFullName();

    let employeeJob= document.createElement("p");
    let employeeSkill= document.createElement("p");
    let employeeCountry= document.createElement("p");

    employeeJob.innerHTML = "Job: " + "<br>" + employeeObject.job;
    div1.append(employeeJob);

    employeeSkill.innerHTML = "Skill: " + "<br>" + employeeObject.skills;
    div2.append(employeeSkill);

    employeeCountry.innerHTML = "Country: " + "<br>" + employeeObject.country;
    div3.append(employeeCountry);

    leftInfo.append(nameTitle);
    leftInfo.append(div1);
    leftInfo.append(div2);
    leftInfo.append(div3);

    let rightInfo = document.createElement("div");
    let div4 = document.createElement("div");
    rightInfo.classList.add("col-4", "d-flex", "justify-content-center", "align-items-center");

    let avatar = document.createElement("img");
    avatar.classList.add("avatar");
    avatar.src = employeeObject.avatarUrl;

    div4.append(avatar);
    rightInfo.append(div4);

    innerProfileCard.append(leftInfo);
    innerProfileCard.append(rightInfo);

    document.getElementById("profiles").append(innerFlex);

    return innerFlex;
}

const profileDiv=document.getElementById("profiles");

let employee1 = new Employee("Kaiden" ,"Herman", "Software Engineer", "C++, C#, Java, PHP, JavaScript, Python","United States", "https://pbs.twimg.com/profile_images/501759258665299968/3799Ffxy.jpeg");
let employee2 = new Employee("Elizabeth", "Dunn", "Accountant", "Excel, Word, Quickbooks", "England", "https://randomuser.me/api/portraits/women/76.jpg");
let employee3 = new Employee("Duan", "Moreno", "Teacher",  "Working with children, History, Word", "Argentina", "https://randomuser.me/api/portraits/med/men/93.jpg");

let employees = [employee1, employee2, employee3];

employees.map(employee => profileDiv.append(createEmployeeCard(employee)));