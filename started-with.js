/////////////////////////////////////////////////////////

let coursesLinks = [];

//develop first cursus list
document.querySelectorAll('div[ng-repeat="parcours in vm.mediatheque.parcours"] h4')[0].click();

//get Items data
setTimeout(scrap, 1000);

function scrap() {
    const modules = document.querySelectorAll(".planning-item-content");
    const numberOfModule = modules.length;
    console.log(numberOfModule);

    //loop through modules
    for (let currentModule = 0; currentModule < numberOfModule; currentModule++) {
        modules[currentModule].click();

        //get course list
        let courses = document.querySelectorAll(".ressource-title");
        let nuberOfCourse = courses.length;

        //loop through course



        for (let currentCourse = 0; currentCourse < nuberOfCourse; currentCourse++) {
            //select course
            courses[currentCourse].click();



            setTimeout(() => {

                coursesLinks.push(document.getElementById("courseframecontent").src);
                //window.location = "https://app.studi.fr/#/dashboard/planning";

                window.history.back();

            }, 500);
        }//course loop end
        console.log(coursesLinks);


        break;
    }//module loop end

}//scrap function end




/////////////////////////
/////////////////////////////////////////////////////////

let coursesLinks = [];

//develop first cursus list
document.querySelectorAll('div[ng-repeat="parcours in vm.mediatheque.parcours"] h4')[0].click();

//get Items data
setTimeout(scrap, 1500);

function scrap() {
    const modules = document.querySelectorAll(".planning-item-content");
    const numberOfModule = modules.length;
    console.log(numberOfModule);

    //loop through modules
    for (let currentModule = 0; currentModule < numberOfModule; currentModule++) {
        modules[currentModule].click();

        //get course list
        let courses = document.querySelectorAll(".ressource-title");
        let nuberOfCourse = courses.length;

        console.log(courses, nuberOfCourse);

        //loop through course



        for (let currentCourse = 0; currentCourse < nuberOfCourse; currentCourse++) {
            //select course
            courses[currentCourse].click();

            setTimeout(() => {
                coursesLinks.push(document.getElementById("courseframecontent").src);
                //window.location = "https://app.studi.fr/#/dashboard/planning";

                window.history.back();

            }, 1000);
        }//course loop end
        console.log(coursesLinks);

        window.history.back();
        break;
        document.querySelectorAll('div[ng-repeat="parcours in vm.mediatheque.parcours"] h4')[0].click();
    }//module loop end

}//scrap function end