class LocalServices{
  changeState = async (path, queryParams) => {
    await fetch(`http://${path}${queryParams}`, { mode: 'no-cors', method: 'POST' })
  }
}

export default new LocalServices()