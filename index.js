const {Builder,By} = require('selenium-webdriver');

var data = async function(){
        driver = new Builder().forBrowser('chrome').build();
    await driver.get('https://imadaboulhouda.com/')
    images = await driver.findElements(By.css('img'))
for(let x of images)
{
    var sr = await x.getAttribute('src')
    console.log(sr)
}

};
data();
