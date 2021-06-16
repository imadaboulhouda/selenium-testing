const { Builder, By } = require('selenium-webdriver');

var data = async function () {
    driver = new Builder().forBrowser('chrome').build();
    await driver.get('https://www.youtube.com/')
     driver.findElement(By.css('#search')).sendKeys('Tersea')
     driver.findElement(By.css('#search-icon-legacy')).click()
    dataWeb = await driver.findElements(By.css('#video-title.ytd-video-renderer'));
    console.log(dataWeb)
    for(let x of dataWeb)
    {
        let xz = await (x.getText())
        console.log(xz)
    }

};
data();
