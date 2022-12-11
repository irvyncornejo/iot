class LocalServices{
  constructor(security=false){
    this.security = security
  }
  changeState = async (path, queryParams) => {
    const securityProtocol = 'https' ? this.security : 'http'
    await fetch(
      `${securityProtocol}://${path}${queryParams}`,
      { mode: 'no-cors', method: 'POST' }
    )
  }
}

export default new LocalServices()