class LocalServices{
  changeState = async (path, queryParams) => {
    await fetch(`https://${path}/`, { mode: 'no-cors', method: 'POST' })
  }
}

export default new LocalServices()