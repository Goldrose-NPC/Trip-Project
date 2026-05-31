module.exports = {
  // http://localhost:8080/api/test
  // =>
  // http://127.0.0.1:8000/test
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000/',
        changeOrigin: true,
        pathRewrite: {
          // 需要重写的URL
          '^/api': ''
        }
      }
    }
  }
}
