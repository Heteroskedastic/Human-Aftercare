# human_aftercare_ui

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## Configuration to run dev by connecting remote api server
add a local environment file called ".env.development.local" in root of UI project containing this content:
```
VUE_APP_API_BASE_URL=http://dev.bagandroom.com
```
