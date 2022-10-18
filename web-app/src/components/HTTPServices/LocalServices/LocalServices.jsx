class LocalServices{
  changeState = async (path, queryParams) => {
    await fetch(`http://${path}${queryParams}`, { mode: 'no-cors', method: 'POST', referrerPolicy: 'unsafe_url' })
  }
}

export default new LocalServices()