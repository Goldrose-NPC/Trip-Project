/**
 * 用户名称脱敏
 * @param {*} name 用户名称
 * @returns
 */
function unameFormat (name) {
  if (!name) {
    return name
  }
  return name.substr(0, 2) + '***'
}

export {
  unameFormat
}
