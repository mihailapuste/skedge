# skedge

> 470 term project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:3000
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

## Production Setup

``` bash
sudo docker build -t frontend .
sudo docker run -it -p 80:80 --rm --name dockerize-vuejs-app-1 frontend
```

## Dev-Help

#### Pages
See src/router/index.js file for all routes

For an explanation of Vue see: [guide](https://vuejs.org/v2/guide/index.html)

For an explanation of Vue components: [single file components](https://vuejs.org/v2/guide/single-file-components.html)

Vue Router: [router](https://router.vuejs.org/)

For a detailed explanation on how things related to webpack work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

The API requests will need to follow the format described here:
[drf-authentication](https://www.django-rest-framework.org/api-guide/authentication/)

