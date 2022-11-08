class LocalServices{
  changeState = async (path, queryParams) => {
    await fetch(`https://192.168.1.141/`, { mode: 'no-cors', method: 'POST' })
  }
}

export default new LocalServices()