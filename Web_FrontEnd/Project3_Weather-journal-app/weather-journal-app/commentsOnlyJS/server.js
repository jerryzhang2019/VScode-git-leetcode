// Setup empty JS object to act as endpoint for all routes设置空的JS对象作为所有路由的端点
projectData = {};
// Express to run server and routes快速运行服务器和路由
const express = require('express');
// Start up an instance of app启动应用程序实例
const app =  express();
/* Dependencies依存关系 */
/* Middleware中间件*/

//Here we are configuring express to use body-parser as middle-ware.
//在这里，我们将Express配置为使用body-parser作为中间件
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());
// Cors for cross origin allowance交叉原点津贴
const cors = require('cors');
app.use(cors());
// Initialize the main project folder初始化主项目文件夹
app.use(express.static('website'));

// Spin up the server启动服务器
const port = 8000;
const server = app.listen(port, listening);
function listening(){
    console.log("server running");
    console.log('running on localhost: $(port)');
}
// Callback to debug 回调调试

// Initialize all route with a callback function使用回调函数初始化所有路由

// Callback function to complete GET '/all'回调函数完成GET'/ all'

// Post Route发布路线
  