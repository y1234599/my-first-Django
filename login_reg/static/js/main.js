//获取页面跳转路径
function get_link(link) {
    window.location.href = link
}


//图片类
img_class = [
    { url: '../static/img/1.jpg', title: '图片1', color: 'rgb(69, 141, 172)' },
    { url: '../static/img/3.jpg', title: '图片2', color: 'blue' },
    { url: '../static/img/4.jpg', title: '图片3', color: 'green' },
    { url: '../static/img/5.jpg', title: '图片4', color: 'yellow' },
    { url: '../static/img/6.jpg', title: '图片5', color: 'rgb(69, 141, 172)' },
    { url: '../static/img/7.jpg', title: '图片6', color: 'blue' },
    { url: '../static/img/8.jpg', title: '图片7', color: 'green' },
    { url: '../static/img/9.jpg', title: '图片8', color: 'yellow' },
];

// 轮播图
let i = 0 //控制图片起始位置
function Loop_picture() {
    if (i < img_class.length) {

        const img = document.querySelector(".txt_main img");
        img.src = img_class[i].url;

        const txt = document.querySelector('.txt_main p');
        txt.innerHTML = img_class[i].title;

        // const background = document.querySelector('.txt_main')
        // background.style.backgroundColor = img_class[i].color;

        const drop_white = document.querySelector(`.txt_main #img_bottom .drop`)
        drop_white.classList.remove('drop')

        const drop = document.querySelector(`.txt_main #img_bottom li:nth-child(${i + 1})`)
        drop.classList.add('drop')
        i++;
    }
    else {
        i = 0;
        //以函数递归的方式防止多余循环造成计时器的多余等待
        return Loop_picture();
    }
}

// 图片轮播计时器
function startTimer() {
    if (!timerStarted) {
        n = setInterval(Loop_picture, 1000);
        timerStarted = true;
    }
}

function stopTimer() {
    clearInterval(n);
    timerStarted = false;
}

//点击切换图片

//下一张
function next_switch() {
    i++;
    if (i < img_class.length) {
        const img = document.querySelector(".txt_main img");
        img.src = img_class[i].url;

        const txt = document.querySelector('.txt_main p');
        txt.innerHTML = img_class[i].title;


        const drop_white = document.querySelector(`.txt_main #img_bottom .drop`);
        drop_white.classList.remove('drop');

        const drop = document.querySelector(`.txt_main #img_bottom li:nth-child(${i+1})`);
        drop.classList.add('drop');
        
    }
    else {

        //避免递归执行i++语句时使得i无法等于0
        i = -1;

        //通过递归避免计时器多余等待
        return next_switch();
    }
}

//上一张
function previous_switch ()
{
    i--;
    if (i >= 0)
    {
        const img = document.querySelector(".txt_main img");
        img.src = img_class[i].url;

        const txt = document.querySelector('.txt_main p');
        txt.innerHTML = img_class[i].title;


        const drop_white = document.querySelector(`.txt_main #img_bottom .drop`);
        drop_white.classList.remove('drop');

        const drop = document.querySelector(`.txt_main #img_bottom li:nth-child(${i+1})`);
        drop.classList.add('drop');
    }

    else 
    {
        //如上面
        i = img_class.length;
        return previous_switch()
    }
}